import time
import pathlib
from collections import deque
from typing import List, Tuple


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


def _dfs_all_paths(
    grid: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]
) -> List[List[Tuple[int, int]]]:
    row_count = len(grid)
    col_count = len(grid[0])
    all_paths = []
    path = []

    def dfs(r, c):
        if (r, c) == end:
            all_paths.append(path.copy())
            return

        # Explore neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < row_count
                and 0 <= nc < col_count
                and (grid[nr][nc] == "." or (nr, nc) == end)
            ):
                if (nr, nc) not in path:  # Avoid revisiting nodes in this path
                    path.append((nr, nc))
                    dfs(nr, nc)
                    path.pop()  # Backtrack

    path.append(start)
    dfs(start[0], start[1])
    return all_paths


def _get_current_direction(node, prev):
    r, c = node
    pr, pc = prev
    if r == pr:
        if c - pc == 1:
            return 0, 1
        else:
            return 0, -1
    else:
        if r - pr == 1:
            return 1, 0
        else:
            return -1, 0


def _get_path_score(path: list[tuple[int, int]]) -> int:
    path = sorted(path)
    turn_count = 0
    current_direction = _get_current_direction(node=path[1], prev=path[0])
    for i in range(2, len(path)):
        next_direction = _get_current_direction(path[i], path[i - 1])
        if next_direction != current_direction:
            turn_count += 1000
            current_direction = next_direction
        else:
            turn_count += 1
    return turn_count


def find_best_reindeer_path(file_path: str):
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        grid = [list(line) for line in puzzle_input.read().splitlines()]
        start_, end_ = _get_start_end(grid)
        print(f"{start_=}")
        print(f"{end_=}")
        paths = _dfs_all_paths(grid=grid, start=start_, end=end_)
        print(f"{paths=}")
        path_scores = []
        for path in paths:
            path_scores.append(_get_path_score(path))
        return min(path_scores)


start = time.perf_counter()
print(
    find_best_reindeer_path(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_16"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    find_best_reindeer_path(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_16"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
