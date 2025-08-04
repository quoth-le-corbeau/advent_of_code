from pathlib import Path
import re

from reusables import timer, INPUT_PATH


def _parse_ips(file_path: Path) -> list[tuple[str, str, str]]:
    with open(file_path, "r") as puzzle_input:
        return [
            (
                line.split("[")[0],
                line.split("[")[1].split("]")[0],
                line.split("[")[1].split("]")[1],
            )
            for line in puzzle_input.read().strip().splitlines()
        ]


def _has_abba(string_: str) -> bool:
    pattern = r"(?=([a-zA-Z])([a-zA-Z])\2\1)(?!\1\1\1\1)"
    matches = [
        string_[m.start() : m.start() + 4] for m in re.finditer(pattern, string_)
    ]
    return len(matches) != 0


@timer
def part_one(file: str, day: int = 7, year: int = 2016) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    ip_address_hypernet_tuples = _parse_ips(file_path=input_file_path)
    count = 0
    for part_1, hypernet, part_2 in ip_address_hypernet_tuples:
        if (_has_abba(part_1) or _has_abba(part_2)) and not _has_abba(hypernet):
            print(part_1 + "[" + hypernet + "]" + part_2)
            count += 1
    return count


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 7, year: int = 2016):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )


part_two(file="eg")
part_two(file="input")
