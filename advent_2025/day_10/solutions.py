import itertools
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


def _parse_joltages(joltage_str) -> list[int]:
    return list(
        int(j) for j in joltage_str.replace("{", "").replace("}", "").split(",")
    )


def _parse_buttons(button_str) -> list[tuple[int, ...]]:
    buttons = []
    for b in button_str:
        buttons.append(tuple(map(int, b.replace(")", "").replace("(", "").split(","))))
    return buttons


def _parse_lights(light_str) -> list[bool]:
    lights = []
    for light in light_str[1:-1]:
        if light == ".":
            lights.append(False)
        else:
            assert light == "#"
            lights.append(True)
    return lights


def _count_required_presses(config: list) -> int:
    goal = config[0]
    buttons = config[1]
    start = [False for _ in range(len(goal))]

    # Start with combinations of size 1, 2, 3, etc.
    for combination_size in range(1, len(buttons) + 1):
        for (
            button_combination
        ) in itertools.combinations_with_replacement(  # this is f***ing awesome
            buttons, combination_size
        ):
            candidate = _toggle(button_combination, start)
            if candidate == goal:
                return len(button_combination)

    return -1


def _toggle(button_combination: tuple, start: list[bool]) -> list[bool]:
    state = start.copy()
    for button in button_combination:
        for index in button:
            state[index] = not state[index]
    return state


@timer
def part_one(file: str, day: int = 10, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    configs = _parse_input(file_path=input_file_path)
    total = 0
    for config in configs:
        required_presses = _count_required_presses(config)
        # print(f"For config: {config}")
        # print(f"{required_presses=}")
        # print("------------------------")
        total += required_presses
    return total


# part_one(file="eg")
# part_one(file="input")


def _count_required_joltage_presses(config: list) -> int:
    goal = config[-1]
    buttons = config[1]
    counters = [0 for _ in range(len(goal))]

    # Start with combinations of size 1, 2, 3, etc.
    for combination_size in range(min(goal), len(buttons) + 100):
        for button_combination in itertools.combinations_with_replacement(
            buttons, combination_size
        ):
            candidate = _increment_counters(button_combination, counters)
            if candidate == goal:
                return len(button_combination)

    return -1


def _increment_counters(button_combination: tuple, start: list[int]) -> list[int]:
    state = start.copy()
    for button in button_combination:
        for index in button:
            state[index] += 1
    return state


@timer
def part_two(file: str, day: int = 10, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    configs = _parse_input(file_path=input_file_path)
    total = 0
    for config in configs:
        required_presses = _count_required_joltage_presses(config)
        print(f"For config: {config}")
        print(f"{required_presses=}")
        print("------------------------")
        total += required_presses
    return total


part_two(file="eg")
part_two(file="input")
