from pathlib import Path
from math import log10, ceil

from reusables import INPUT_PATH, timer


def _check_invalid(low: int, high: int) -> set[int]:
    invalid = set()
    # limit each function call to be the full range of integers with n digits
    min_digits, max_digits = ceil(log10(low) + 1e-9), ceil(log10(high) + 1e-9)
    if max_digits > min_digits:
        return _check_invalid(low, 10**min_digits - 1).union(
            _check_invalid(10**min_digits, high)
        )
    digits = min_digits
    # loop through all possible sequence lengths (from 1 up to and including half the number of digits
    for sequence_len in range(1, digits // 2 + 1):
        start_pattern = low // 10 ** (digits - sequence_len)
        end_pattern = high // 10 ** (digits - sequence_len)
        for pattern in range(start_pattern, end_pattern + 1):
            candidate = 0
            # find all integers made of repeated pattern of sequence_len with this number of digits
            for j in range(digits // sequence_len):
                candidate += pattern * 10 ** (j * sequence_len)
            # only append if within the given bounds
            if low <= candidate <= high:
                invalid.add(candidate)
    return invalid


@timer
def part_two(file: str, day: int = 2, year: int = 2025) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    with open(input_file_path, "r") as puzzle_input:
        invalid = set()
        for interval in puzzle_input.read().strip().split(","):
            low, high = int(interval.split("-")[0]), int(interval.split("-")[1])
            invalid |= _check_invalid(low, high)
    return sum(invalid)


part_two("egelant")
