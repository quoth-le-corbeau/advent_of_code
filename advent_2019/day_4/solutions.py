from pathlib import Path

from reusables import timer, INPUT_PATH

_DIGITS = "0,1,2,3,4,5,6,7,8,9".split(",")


def _parse_input(file_path: Path) -> tuple[str, str]:
    with open(file_path, "r") as puzzle_input:
        return tuple(puzzle_input.read().strip().split("-"))


def _has_exactly_two_adjacent_and_ascending_digits(number_str: str) -> int:
    if "".join(sorted(number_str)) != number_str:
        return 0
    for digit in _DIGITS:
        if number_str.count(digit) == 2:
            i = number_str.index(digit)
            if i != 5 and number_str[i + 1] == digit:
                return 1
    return 0


@timer
def part_one(file: str, day: int = 4, year: int = 2019) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    start_str, end_str = _parse_input(file_path=input_file_path)
    count = 0
    for n in range(int(start_str), int(end_str)):
        n_str = str(n)
        if len(set(n_str)) != len(n_str) and all(
            [int(n_str[i + 1]) - int(n_str[i]) >= 0 for i in range(len(n_str[:-1]))]
        ):
            count += 1
    return count


part_one(file="input")


@timer
def part_two(file: str, day: int = 4, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    start_str, end_str = _parse_input(file_path=input_file_path)
    count = 0
    for n in range(int(start_str), int(end_str)):
        count += _has_exactly_two_adjacent_and_ascending_digits(str(n))
    return count


part_two(file="input")
