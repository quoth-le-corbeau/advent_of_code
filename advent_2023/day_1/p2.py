import re
import pathlib
import time

SPELLED_DIGITS = "one two three four five six seven eight nine".split()


def sum_calibration_values_2(file: str) -> int:
    return find_and_sum_spelled_digits(file=file)


def find_and_sum_spelled_digits(file: str) -> int:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.readlines()
        pattern = "(?=(one|two|three|four|five|six|seven|eight|nine|\\d))"
        # pattern = "(?=(" + "|".join(SPELLED_DIGITS) + "|\\d))"  # equivalent
        all_calibration_values = []
        for line in lines:
            line = line.strip()
            all_digits = list(map(_convert_digit, re.findall(pattern, line)))
            all_calibration_values.append((all_digits[0] * 10) + all_digits[-1])
        return sum(all_calibration_values)


def _convert_digit(string: str) -> int:
    if string.isdigit():
        return int(string)
    else:
        return SPELLED_DIGITS.index(string) + 1


start = time.perf_counter()
print(sum_calibration_values_2("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(sum_calibration_values_2("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
