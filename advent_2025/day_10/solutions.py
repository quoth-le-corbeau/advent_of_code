import itertools
from collections import deque
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


def _count_required_joltage_presses_bfs(config: list) -> int:
    goal = tuple(config[-1])
    buttons = [tuple(button) for button in config[1]]

    start_state = tuple([0] * len(goal))

    if start_state == goal:
        return 0

    q = deque([(start_state, 0)])
    visited = {start_state}

    while q:
        current_state, presses = q.popleft()
        for button in buttons:

            new_state = list(current_state)
            for idx in button:
                new_state[idx] += 1

            new_state = tuple(new_state)
            if any(new_state[i] > goal[i] for i in range(len(goal))):
                continue

            if new_state == goal:
                return presses + 1

            if new_state not in visited:
                q.append((new_state, presses + 1))
                visited.add(new_state)

    return -1


def _count_required_joltage_presses_dp(config: list) -> int:
    goal = tuple(config[-1])
    buttons = [tuple(b) for b in config[1]]
    n = len(goal)

    dp = {tuple([0] * n): 0}
    queue = [tuple([0] * n)]

    while queue:
        new_queue = []
        for state in queue:
            current_presses = dp[state]
            for button in buttons:
                new_state = list(state)
                valid = True
                for idx in button:
                    new_state[idx] += 1
                    if new_state[idx] > goal[idx]:
                        valid = False
                        break

                if not valid:
                    continue

                new_state = tuple(new_state)

                if new_state == goal:
                    return current_presses + 1

                if new_state not in dp:
                    dp[new_state] = current_presses + 1
                    new_queue.append(new_state)
        queue = new_queue

    return -1


@timer
def part_two(file: str, day: int = 10, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    configs = _parse_input(file_path=input_file_path)
    total = 0
    for config in configs:
        required_presses = _count_required_joltage_presses_dp(config)
        total += required_presses
    return total


part_two(file="eg")
part_two(file="input")
