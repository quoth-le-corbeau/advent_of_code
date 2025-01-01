from pathlib import Path

from reusables import timer, INPUT_PATH


def RENAME_FUNC(file_path: Path):
    with open(file_path, "r") as puzzle_input:
        lines = puzzle_input.read()
        print(lines)


@timer
def part_one(file: str, day: int = 8, year: int = 2016):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    print(f"<-----------{input_file_path} -------------->")
    print(f"part 1: {RENAME_FUNC(file_path=input_file_path)}")


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 8, year: int = 2016):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    print(f"part 2: {RENAME_FUNC(file_path=input_file_path)}")


part_two(file="eg")
part_two(file="input")
