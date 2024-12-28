from pathlib import Path
from collections import deque

from reusables import timer, INPUT_PATH


def _get_start_end(grid) -> tuple[tuple[int, int], tuple[int, int]]:
    start_ = None
    end_ = None
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "S":
                start_ = r, c
            if col == "E":
                end_ = r, c
    if start_ is None or end_ is None:
        raise ValueError("No start or end found")
    return start_, end_


def _get_path_score(path: list[tuple[int, int]]) -> int:
    turn_count = 0
    total_forward_steps = len(path) - 1
    current_direction = "east"
    for i in range(2, len(path)):
        next_direction = _get_current_direction(path[i], path[i - 1])
        if next_direction != current_direction:
            turn_count += 1
            current_direction = next_direction

    return turn_count * 1000 + total_forward_steps


def _get_current_direction(node, prev):
    if node[0] == prev[0]:
        if node[1] - prev[1] == 1:
            return "east"
        else:
            assert node[1] - prev[1] == -1
            return "west"
    else:
        assert node[0] != prev[0]
        if node[0] - prev[0] == 1:
            return "south"
        else:
            assert node[0] - prev[0] == -1
            return "north"


def _find_paths(grid, start, end):
    q = deque([[start]])
    paths = []

    while q:
        path = q.popleft()
        current = path[-1]

        # If the end point is reached, save the path
        if current == end:
            paths.append(path)
            continue

        # Explore neighbors in all four directions
        for vector in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            dr, dc = vector
            next_point = current[0] + dr, current[1] + dc
            nr, nc = next_point

            if (
                0 <= nr < len(grid)
                and 0 <= nc < len(grid[0])
                and next_point not in path  # Avoid revisiting nodes in the current path
                and (grid[nr][nc] == "." or grid[nr][nc] == "E")
            ):
                q.append(path + [next_point])

    return paths


def find_best_reindeer_path(file_path: Path):
    with open(Path(__file__).resolve().parents[2] / file_path, "r") as puzzle_input:
        grid = [list(line) for line in puzzle_input.read().splitlines()]
        start_, end_ = _get_start_end(grid)
        paths = _find_paths(grid=grid, start=start_, end=end_)
        print(len(paths))
        return min([_get_path_score(path) for path in paths])


@timer
def part_one(file: str, year: int = 2024, day: int = 16) -> None:
    input_file_path = INPUT_PATH.format(year=year, day=day, file=file)
    print(find_best_reindeer_path(file_path=input_file_path))
    print(f"solution ran with file: {file}.txt")


part_one(file="eg")
part_one(file="eg2")
part_one(file="input")
