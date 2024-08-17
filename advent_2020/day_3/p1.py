from typing import List
import time
import pathlib

_TREE = "#"


def count_trees_on_trajectory(file_path: str) -> int:
    i = 0
    j = 0
    grid = _read_grid_from_forest(file=file_path)
    bottom_row_index = len(grid) - 1
    grid_line_length = len(grid[j])
    tree_count: int = 0
    while j <= bottom_row_index - 1:
        j += 1
        last_index = i
        current_index: int = (last_index + 3) % grid_line_length
        grid_point = grid[j][current_index]
        if grid_point == _TREE:
            tree_count += 1
        i = current_index

    return tree_count


def _read_grid_from_forest(file: str) -> List[str]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        return puzzle_input.read().splitlines()


start = time.perf_counter()
print(count_trees_on_trajectory("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(count_trees_on_trajectory("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
