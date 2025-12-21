from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_santas_instructions_to_intcode(file_path: Path) -> list[list[int]]:
    intcodes = []
    with open(file_path, "r") as puzzle_input:
        for line in puzzle_input.read().strip().splitlines():
            intcode = []
            parsed = (
                line.replace("turn on", "1")
                .replace("turn off", "0")
                .replace("toggle", "-1")
                .replace(" through", "")
                .split(" ")
            )
            print(f"{parsed=}")

            pass


@timer
def part_one(file: str, day: int = 6, year: int = 2015):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    return _parse_santas_instructions_to_intcode(file_path=input_file_path)


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 6, year: int = 2015):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    return _parse_santas_instructions_to_intcode(file_path=input_file_path)


# part_two(file="eg")
# part_two(file="input")
