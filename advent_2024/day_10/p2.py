import pathlib
import time
from collections import defaultdict

"""
Hoof It Part II

loop through the grid
make a list of all the 0 coordinates
make a list of all the 9 coordinates

instantiate a defaultdict to store the paths from each zero to each nine

for each zero:
    for each nine:
       run a dfs() algorithm to get all the paths connecting the zero to the nine 
       append all_paths to the dict for the zero key

finally sum the lengths of each group of paths

"""

_UNIT_VECTORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def sum_trailhead_ratings(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        grid = [[int(n) for n in line] for line in lines]

    row_count = len(grid)
    col_count = len(grid[0])
    zeros = [
        (r, c) for r, row in enumerate(grid) for c, col in enumerate(row) if col == 0
    ]
    nines = [
        (r, c) for r, row in enumerate(grid) for c, col in enumerate(row) if col == 9
    ]

    def dfs(
        current: tuple[int, int],
        end: tuple[int, int],
        visited: set[tuple[int, int]],
        path: list[tuple[int, int]],
        all_paths: list[list[tuple[int, int]]],
    ):
        if current == end:
            all_paths.append(path)
            return
        for dr, dc in _UNIT_VECTORS:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < row_count and 0 <= nc < col_count:
                if grid[nr][nc] - grid[current[0]][current[1]] == 1:
                    next_pos = (nr, nc)
                    if next_pos not in visited:
                        visited.add(next_pos)
                        path.append(next_pos)
                        dfs(next_pos, end, visited, path, all_paths)
                        path.pop()
                        visited.remove(next_pos)

    all_paths_result = defaultdict(list)
    for zero in zeros:
        for nine in nines:
            visited = {zero}
            path = [zero]
            all_paths = []
            dfs(current=zero, end=nine, visited=visited, path=path, all_paths=all_paths)
            if len(all_paths) != 0:
                all_paths_result[zero].append((nine, all_paths))
    rating_score = 0
    for trailhead, all_paths in all_paths_result.items():
        for path in all_paths:
            rating_score += len(path[1])
    return rating_score


timer_start = time.perf_counter()
print(
    sum_trailhead_ratings(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_10"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    sum_trailhead_ratings(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_10"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
