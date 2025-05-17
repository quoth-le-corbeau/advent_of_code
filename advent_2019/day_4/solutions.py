from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_input(file_path: Path):
    with open(file_path, "r") as puzzle_input:
        return tuple(map(int, puzzle_input.read().strip().split("-")))


@timer
def part_one(file: str, day: int = 4, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    interval = _parse_input(file_path=input_file_path)
    print(interval)
    for n in range(*interval):
        print(n)


part_one(file="input")


@timer
def part_two(file: str, day: int = 4, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    print(f"part 2: {_parse_input(file_path=input_file_path)}")


part_two(file="input")
