import re
from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_input(file_path: Path):
    with open(file_path, "r") as puzzle_input:
        for line in puzzle_input.read().strip().splitlines():
            number_pattern = r"\d+"
            checksum_pattern = r"\[(.*?)\]"
            sector_id = re.findall(pattern=number_pattern, string=line)[0]
            checksum = re.findall(pattern=checksum_pattern, string=line)[0]
            print(f"{sector_id=}")
            print(f"{checksum=}")
            name = line[: line.index(sector_id)]
            print(f"{name=}")


@timer
def part_one(file: str, day: int = 4, year: int = 2016):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    _parse_input(file_path=input_file_path)


part_one(file="eg")
# part_one(file="input")


@timer
def part_two(file: str, day: int = 4, year: int = 2016):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    print(f"part 2: {_parse_input(file_path=input_file_path)}")


# part_two(file="eg")
# part_two(file="input")
