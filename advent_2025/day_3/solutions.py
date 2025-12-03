from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_input(file_path: Path) -> list[list[int]]:
    with open(file_path, "r") as puzzle_input:
        banks = []
        for line in puzzle_input.read().strip().splitlines():
            banks.append(list(map(int, line)))
    return banks


def _find_largest_two_digit_voltage(bank: list[int]) -> int:
    max_t = len(bank) - 1
    max_u = len(bank)
    tens = 0
    tens_i = 0
    units = 0
    for t in range(max_t):
        if bank[t] > tens:
            tens = bank[t]
            tens_i = t
    for u in range(max_u):
        if bank[u] > units and u > tens_i:
            units = bank[u]
    return tens * 10 + units


def _find_largest_twelve_digit_voltage(bank: list[int], digits_left: int = 11) -> int:
    total = 0
    digit_count = 0
    max_i = -1
    while digits_left >= 0:
        max_ = 0
        pool = bank[digit_count : len(bank) - digits_left]
        for i, n in enumerate(pool):
            if n > max_ and i >= max_i:
                max_ = n
                max_i = i
        total += max_ * 10**digits_left
        print(f"subtotal: {total}")
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
        largest = _find_largest_two_digit_voltage(bank)
        total += int(largest)
    return total


# part_one(file="eg")
# part_one(file="input")


@timer
def part_two(file: str, day: int = 3, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    banks = _parse_input(file_path=input_file_path)
    total = 0
    for bank in banks:
        largest = _find_largest_twelve_digit_voltage(bank)
        print("--------------")
        print(f"TOTAL: {largest}")
        print("--------------")
        total += largest
    return total


part_two(file="eg")
part_two(file="input")
