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


def _vowel_count(string: str) -> int:
    count = 0
    for char in string:
        if char in _VOWELS:
            count += 1
    return count


def _is_nice_p1(string: str) -> bool:
    if any(v in string for v in _VERBOTEN):
        return False
    elif _vowel_count(string) >= 3 and _contains_repeated_char(string):
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
        if _is_nice_p1(line):
            nice += 1
    return nice


part_one(file="eg")
part_one(file="input")


def _is_nice_p2(string: str) -> bool:
    has_repeated_pair = False
    has_palindromic_triple = False
    for i in range(len(string) - 2):
        pair = string[i : i + 2]
        if pair in string[i + 2 :]:
            has_repeated_pair = True
        if string[i] == string[i + 2]:
            has_palindromic_triple = True
    return has_repeated_pair and has_palindromic_triple


@timer
def part_two(file: str, day: int = 5, year: int = 2015):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    nice = 0
    for line in _parse_lines(file_path=input_file_path):
        if _is_nice_p2(line):
            nice += 1
    return nice


part_two(file="eg2")
part_two(file="input")
