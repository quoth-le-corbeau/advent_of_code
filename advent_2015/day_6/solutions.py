from collections import defaultdict
from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_santas_instructions(
    file_path: Path,
) -> list[tuple[int, tuple[int, int], tuple[int, int]]]:
    instructions = []
    with open(file_path, "r") as puzzle_input:
        for line in puzzle_input.read().strip().splitlines():
            parsed = (
                line.replace("turn on", "1")
                .replace("turn off", "-1")
                .replace("toggle", "2")
                .replace(" through", "")
                .split(" ")
            )
            assert len(parsed) == 3
            instructions.append(
                (
                    int(parsed[0]),
                    (int(parsed[1].split(",")[0]), int(parsed[1].split(",")[1])),
                    (int(parsed[2].split(",")[0]), int(parsed[2].split(",")[1])),
                ),
            )
    return instructions


@timer
def part_one(file: str, day: int = 6, year: int = 2015) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    lights = set()
    for instruction in _parse_santas_instructions(file_path=input_file_path):
        cmd = instruction[0]
        assert cmd in [-1, 2, 1]
        x1, y1 = instruction[1]
        x2, y2 = instruction[2]
        assert x1 <= x2 and y1 <= y2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                light = (i, j)
                if light in lights:
                    if cmd in [-1, 2]:
                        lights.remove(light)
                else:
                    if cmd == 1 or cmd == 2:
                        lights.add(light)
    return len(lights)


# part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 6, year: int = 2015):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    brightness_by_lights = defaultdict(int)
    for instruction in _parse_santas_instructions(file_path=input_file_path):
        increment = instruction[0]
        x1, y1 = instruction[1]
        x2, y2 = instruction[2]
        assert x1 <= x2 and y1 <= y2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                light = (i, j)
                if light in brightness_by_lights:
                    value = brightness_by_lights[light]
                    if value == 0 and increment == -1:
                        continue
                    brightness_by_lights[light] += increment
                else:
                    if increment != -1:
                        brightness_by_lights[light] = increment
    return sum(brightness_by_lights.values())


# part_two(file="eg")
part_two(file="input")
