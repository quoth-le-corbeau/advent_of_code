from typing import List
import time
import pathlib
import math

_TREE = "#"
_SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def _count_trees_on_trajectory(
    grid: List[str], down_increment: int, right_increment: int
) -> int:
    i = 0
    j = 0
    bottom_row_index = len(grid) - 1
    grid_line_length = len(grid[j])
    tree_count: int = 0
    while j <= bottom_row_index - 1:
        j += down_increment
        last_index = i
        current_index: int = (last_index + right_increment) % grid_line_length
        grid_point = grid[j][current_index]
        if grid_point == _TREE:
            tree_count += 1
        i = current_index

    return tree_count


def count_trees_on_trajectories(file_path: str) -> int:
    grid = _read_grid_from_forest(file=file_path)
    tree_counts: List[int] = list()
    for right, down in _SLOPES:
        tree_counts.append(
            _count_trees_on_trajectory(
                grid=grid, right_increment=right, down_increment=down
            )
        )
    return math.prod(tree_counts)


def _read_grid_from_forest(file: str) -> List[str]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        return puzzle_input.read().splitlines()


start = time.perf_counter()
print(count_trees_on_trajectories("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(count_trees_on_trajectories("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
