import time
import pathlib
from collections import deque

"""
Garden Groups Part II

create an empty list of patches
loop through the grid
check if the current r, c is already in a patch in the patches
if so continue
otherwise starting at that square perform a bfs to get the whole patch it is in 
append the patch to the patches list
instantiate a total = 0
loop through the patches and get the area 

count the number of sides in a separate function
add area * number of sides to the total
return the total

"""


def get_discount_garden_group_price(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip()
        grid = [line for line in lines.split("\n")]
        patches = []
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                square = r, c
                if any([square in patch for patch in patches]):
                    continue
                else:
                    patches.append(_bfs(start=square, grid=grid))
        total_price = 0
        for patch in patches:
            area = len(patch)
            number_of_sides = _get_number_of_sides(grid=grid, patch=patch)
            print(
                f"A region of type: {grid[patch[0][0]][patch[0][1]]} with "
                f"area: {area}, number of sides: {number_of_sides}"
            )
            total_price += number_of_sides * area
        return total_price


def _get_number_of_sides(grid: list, patch: list[tuple[int, int]]) -> int:
    count = 0
    rows = sorted(patch)
    c = rows[0][1]
    return count


def _bfs(start: tuple[int, int], grid: list[str]) -> list[tuple[int, int]]:
    r, c = start
    type_ = grid[r][c]
    queue = deque([start])
    visited = {start}
    patch = [start]

    while queue:
        current = queue.popleft()
        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_node = current[0] + direction[0], current[1] + direction[1]
            if (
                0 <= next_node[0] < len(grid)
                and 0 <= next_node[1] < len(grid[0])
                and next_node not in visited
                and grid[next_node[0]][next_node[1]] == type_
            ):
                queue.append(next_node)
                visited.add(next_node)
                patch.append(next_node)

    return patch


start = time.perf_counter()
print(
    get_discount_garden_group_price(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_12"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    get_discount_garden_group_price(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_12"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
