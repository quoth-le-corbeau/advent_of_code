from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_instructions(file_path: Path) -> int:
    total: int = 0
    with open(file_path, "r") as puzzle_input:
        line = puzzle_input.read().strip()
    for char in line:
        match char:
            case "(":
                total += 1
            case ")":
                total -= 1
            case _:
                raise ValueError(f"Unexpected character: {char}")
    return total


@timer
def part_one(file: str, day: int = 1, year: int = 2015) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    total: int = 0
    with open(input_file_path, "r") as puzzle_input:
        line = puzzle_input.read().strip()
    for char in line:
        match char:
            case "(":
                total += 1
            case ")":
                total -= 1
            case _:
                raise ValueError(f"Unexpected character: {char}")
    return total


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 1, year: int = 2015) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    total: int = 0
    with open(input_file_path, "r") as puzzle_input:
        line = puzzle_input.read().strip()
    i = 0
    while i < len(line):
        char = line[i]
        if total == -1:
            return i
        match char:
            case "(":
                total += 1
            case ")":
                total -= 1
            case _:
                raise ValueError(f"Unexpected character: {char}")
        i += 1
    raise ValueError("Basement Floor -1 never reached!")


part_two(file="eg")
part_two(file="input")
