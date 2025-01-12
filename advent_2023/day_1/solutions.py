from pathlib import Path
import re

from reusables import timer, INPUT_PATH


def _parse_input(filename: str) -> list[str]:
    input_file = INPUT_PATH.format(file=filename, year=2023, day=1)
    input_path = Path(__file__).resolve().parents[2] / input_file
    with input_path.open(mode="r") as puzzle_input:
        return puzzle_input.read().strip().splitlines()


@timer
def part1(filename: str) -> None:
    calibration_lines = _parse_input(filename=filename)
    total = 0
    for line in calibration_lines:
        line_digits = []
        all_digits = [list(digits) for digits in re.findall(r"(\d+)", line)]
        for digits in all_digits:
            line_digits.extend(digits)
        calibration_value = line_digits[0] + line_digits[-1]
        total += int(calibration_value)
    print(total)


# part1(filename="eg")
part1(filename="input")


@timer
def part2(filename: str) -> None:
    calibration_lines = _parse_input(filename=filename)
    digit_words = "zero,one,two,three,four,five,six,seven,eight,nine".split(",")
    total = 0
    for line in calibration_lines:
        # Define regex pattern for digits and written-out numbers with lookahead (?=(...)) allows overlaps
        pattern = r"(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))"
        matches = [
            match.group(1) for match in re.finditer(pattern, line, re.IGNORECASE)
        ]
        first_digit = matches[0]
        last_digit = matches[-1]
        if len(first_digit) > 1:
            total += 10 * digit_words.index(first_digit)
        else:
            total += 10 * int(first_digit)
        if len(last_digit) > 1:
            total += digit_words.index(last_digit)
        else:
            total += int(last_digit)
    print(total)


# part2(filename="eg2")
part2(filename="input")
