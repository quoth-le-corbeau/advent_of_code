from pathlib import Path

from reusables import timer, INPUT_PATH

"""
[....] (3)
[...#] (1,3)
[.#..] (2)
[.##.] done
"""


def _parse_input(file_path: Path) -> list[list]:
    configs = []
    with open(file_path, "r") as puzzle_input:
        for config_str in [
            line.split(" ") for line in puzzle_input.read().strip().splitlines()
        ]:
            config = []
            config.append(_parse_lights(config_str[0]))
            config.append(_parse_buttons(config_str[1:-1]))
            config.append(_parse_joltages(config_str[-1]))
            configs.append(config)
    return configs


def _parse_joltages(joltage_str):
    return tuple(
        int(j) for j in joltage_str.replace("{", "").replace("}", "").split(",")
    )


def _parse_buttons(button_str):
    buttons = []
    for b in button_str:
        buttons.append(tuple(map(int, b.replace(")", "").replace("(", "").split(","))))
    return buttons


def _parse_lights(light_str):
    lights = []
    for l in light_str[1:-1]:
        if l == ".":
            lights.append(False)
        else:
            assert l == "#"
            lights.append(True)
    return lights


@timer
def part_one(file: str, day: int = 10, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    configs = _parse_input(file_path=input_file_path)
    print(f"{configs=}")


part_one(file="eg")
# part_one(file="input")


@timer
def part_two(file: str, day: int = 10, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    return _parse_input(file_path=input_file_path)


# part_two(file="eg")
# part_two(file="input")
