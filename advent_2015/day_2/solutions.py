from pathlib import Path
from reusables import timer, INPUT_PATH


def _parse_dimensions(file_path: Path) -> int:
    with open(file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
    total = 0
    for line in lines:
        l, w, b = line.split("x")
        sides = [int(l) * int(w), int(w) * int(b), int(l) * int(b)]
        total += 2 * sum(sides) + min(sides)

    return total


@timer
def part_one(file: str, day: int = 2, year: int = 2015) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    return _parse_dimensions(file_path=input_file_path)


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 2, year: int = 2015):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    return _parse_dimensions(file_path=input_file_path)


part_two(file="eg")
part_two(file="input")
