import time
import pathlib
from collections import deque, defaultdict
from typing import Optional


"""
Hoof It Part I

loop through the grid
make a list of all the 0 coordinates
make a list of all the 9 coordinates

instantiate a defaultdict to store the paths from each zero to each nine

for each 0:
    for each 9:
        use modified bfs to collect all paths
        e.g all_hiking_trails = {
                (0, 2): [
                            ((0, 1), [(0, 2), (1, 2), (1, 3), (2, 3), ... (0, 1)])
                        ]
            }
        
       
    bfs - concept
    create a queue Q 
    mark v as visited and put v into Q 
    while Q is non-empty 
        remove the head u of Q 
        mark and enqueue all (unvisited) neighbours of u 
        
finally sum the lengths of each set of values in the defaultdict
    
"""

_UNIT_VECTORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def _bfs(
    start: tuple[int, int], end: tuple[int, int], grid: list[list[int]]
) -> Optional[list[tuple[int, int]]]:
    row_count = len(grid)
    col_count = len(grid[0])
    queue = deque([[start]])
    visited = {start}
    while len(queue) != 0:
        path = queue.popleft()
        current = path[-1]
        if current == end:
            return path
        for direction in _UNIT_VECTORS:
            next_node = current[0] + direction[0], current[1] + direction[1]
            if 0 <= next_node[0] < row_count and 0 <= next_node[1] < col_count:
                if grid[next_node[0]][next_node[1]] - grid[current[0]][current[1]] == 1:
                    queue.append(path + [next_node])
                    visited.add(next_node)
    return None


def sum_trail_head_scores(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        grid = [[int(n) for n in line] for line in lines]

    zeros = [
        (r, c) for r, row in enumerate(grid) for c, col in enumerate(row) if col == 0
    ]
    nines = [
        (r, c) for r, row in enumerate(grid) for c, col in enumerate(row) if col == 9
    ]
    hike_trails_by_start = defaultdict(list)
    for zero in zeros:
        for nine in nines:
            path = _bfs(start=zero, end=nine, grid=grid)
            if path is not None:
                hike_trails_by_start[zero].append((nine, path))
    return sum(len(val) for val in hike_trails_by_start.values())


start = time.perf_counter()
print(
    sum_trail_head_scores(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_10"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    sum_trail_head_scores(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_10"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
