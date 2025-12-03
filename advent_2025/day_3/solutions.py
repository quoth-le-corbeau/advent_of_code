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


def _find_largest_twelve_digit_voltage(bank: list[int], num_str: str = "") -> str:
    if len(num_str) == 12:
        return num_str
    max_t = len(bank) - 1
    max_u = len(bank)
    tens = 0
    tens_i = 0
    units = 0
    units_i = 0
    for t in range(max_t):
        if bank[t] > tens:
            tens = bank[t]
            tens_i = t
    for u in range(max_u):
        if bank[u] > units and u > tens_i:
            units = bank[u]
            units_i = u
    n = tens * 10 + units
    bank = bank[:tens_i] + bank[tens_i + 1 :]
    bank = bank[: units_i - 1] + bank[units_i:]
    return _find_largest_twelve_digit_voltage(bank, num_str + str(n))


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
        total += int(largest)
    return total


part_two(file="eg")
# part_two(file="input")
