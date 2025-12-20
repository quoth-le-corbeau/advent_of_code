from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_lines(file_path: Path) -> list[str]:
    with open(file_path, "r") as puzzle_input:
        return puzzle_input.read().strip().splitlines()


_VERBOTEN = ["ab", "cd", "pq", "xy"]
_VOWELS = {"a", "e", "i", "o", "u"}


def _contains_repeated_char(string: str) -> bool:
    i = 0
    while i < len(string) - 1:
        if string[i] == string[i + 1]:
            return True
        i += 1
    return False


def _is_nice(string: str) -> bool:
    if any(v in string for v in _VERBOTEN):
        return False
    elif len(_VOWELS.intersection(set(string))) >= 3 and _contains_repeated_char(
        string
    ):
        return True
    else:
        return False


@timer
def part_one(file: str, day: int = 5, year: int = 2015) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    nice = 0
    for line in _parse_lines(file_path=input_file_path):
        if _is_nice(line):
            nice += 1
    return nice


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 5, year: int = 2015):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    return _parse_lines(file_path=input_file_path)


# part_two(file="eg")
# part_two(file="input")
