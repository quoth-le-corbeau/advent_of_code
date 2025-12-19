from collections import defaultdict
from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_steps(file_path: Path) -> str:
    with open(file_path, "r") as puzzle_input:
        return puzzle_input.read().strip()


def _move(char: str, position: tuple[int, int]) -> tuple[int, int]:
    match char:
        case "^":
            return (position[0], position[1] - 1)
        case ">":
            return (position[0] + 1, position[1])
        case "<":
            return (position[0] - 1, position[1])
        case "v":
            return (position[0], position[1] + 1)
        case _:
            raise ValueError(f"Unexpected character: {char}")


@timer
def part_one(file: str, day: int = 3, year: int = 2015):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    visited = defaultdict(int)
    start = (0, 0)
    visited[start] = 1
    current = start
    for char in _parse_steps(file_path=input_file_path):
        current = _move(char=char, position=current)
        visited[current] += 1
    return len([k for k, v in visited.items() if v >= 1])


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 3, year: int = 2015):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    visited = defaultdict(int)
    start = (0, 0)
    visited[start] = 2
    santa = start
    robo = start
    for i, char in enumerate(_parse_steps(file_path=input_file_path)):
        if i % 2 == 0:
            santa = _move(char=char, position=santa)
            visited[santa] += 1
        else:
            robo = _move(char=char, position=robo)
            visited[robo] += 1

    return len([k for k, v in visited.items() if v >= 1])


part_two(file="eg")
part_two(file="input")
