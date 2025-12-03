from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_input(file_path: Path) -> list[list[int]]:
    with open(file_path, "r") as puzzle_input:
        banks = []
        for line in puzzle_input.read().strip().splitlines():
            banks.append(list(map(int, line)))
    return banks


def _find_largest_n_digit_joltage(bank: list[int], digits: int) -> int:
    total = 0
    digit_count = 0
    last_index = -1
    digits_left = digits - 1
    while digits_left >= 0:
        max_ = 0
        pool = bank[digit_count : len(bank) - digits_left]
        for i, n in enumerate(pool):
            if n > max_ and i >= last_index:
                max_ = n
                last_index = i
        total += max_ * 10**digits_left
        digit_count += 1
        digits_left -= 1

    return total


@timer
def part_one(file: str, day: int = 3, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    banks = _parse_input(file_path=input_file_path)
    total = 0
    for bank in banks:
        largest = _find_largest_n_digit_joltage(bank, digits=2)
        total += int(largest)
    return total


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 3, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    banks = _parse_input(file_path=input_file_path)
    total = 0
    for bank in banks:
        largest = _find_largest_n_digit_joltage(bank, digits=12)
        total += largest
    return total


part_two(file="eg")
part_two(file="input")
