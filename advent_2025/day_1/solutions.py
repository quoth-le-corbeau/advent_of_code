from pathlib import Path

from reusables import timer, INPUT_PATH

_DIAL_LENGTH = 100


def _parse_input(file_path: Path) -> list[str]:
    with open(file_path, "r") as puzzle_input:
        return puzzle_input.read().strip().splitlines()


@timer
def part_one(file: str, day: int = 1, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    instructions = _parse_input(file_path=input_file_path)
    current = 50
    count = 0
    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])
        if direction == "L":
            current -= steps
        elif direction == "R":
            current += steps
        current = current % _DIAL_LENGTH
        if current == 0:
            count += 1
    return count


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 1, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    instructions = _parse_input(file_path=input_file_path)
    current = 50
    count = 0
    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])
        i = 1
        while i <= steps:
            if direction == "L":
                current -= 1
            elif direction == "R":
                current += 1
            else:
                raise ValueError(f"Unknown direction '{direction}'")
            if current < 0:
                current = current % _DIAL_LENGTH
            if current >= _DIAL_LENGTH:
                current = current % _DIAL_LENGTH
            if current == 0:
                count += 1
            i += 1
    return count


part_two(file="eg")
part_two(file="input")
