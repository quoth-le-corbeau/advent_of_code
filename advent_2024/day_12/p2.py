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
    patch_type = grid[patch[0][0]][patch[0][1]]
    all_rows_in_patch = set()
    all_cols_in_patch = set()
    for p in patch:
        all_rows_in_patch.add(p[0])
        all_cols_in_patch.add(p[1])
    visited_north = set()
    visited_south = set()
    visited_west = set()
    visited_east = set()
    for square in sorted(patch):
        r, c = square
        if r - 1 < 0 or grid[r - 1][c] != patch_type:
            visited_north.add(square)
        if r + 1 >= len(grid) or grid[r + 1][c] != patch_type:
            visited_south.add(square)
        if c - 1 < 0 or grid[r][c - 1] != patch_type:
            visited_west.add(square)
        if c + 1 >= len(grid[0]) or grid[r][c + 1] != patch_type:
            visited_east.add(square)

    # count north sides
    v_north = sorted(list(visited_north), key=lambda x: (x[0], x[1]))
    n = 1
    i = 0
    while i < len(v_north) - 1:
        current = v_north[i]
        next_ = v_north[i + 1]
        if current[0] == next_[0] and abs(current[1] - next_[1]) == 0:
            i += 1
            continue
        n += 1
        i += 1

    # count south sides
    v_south = sorted(list(visited_south), key=lambda x: (x[0], x[1]))
    s = 1
    i = 0
    while i < len(v_south) - 1:
        current = v_south[i]
        next_ = v_south[i + 1]
        if current[0] == next_[0] and abs(current[1] - next_[1]) == 1:
            i += 1
            continue
        s += 1
        i += 1
    # count west sides
    v_west = sorted(list(visited_west), key=lambda x: (x[1], x[0]))
    w = 1
    i = 0
    while i < len(v_west) - 1:
        current = v_west[i]
        next_ = v_west[i + 1]
        if abs(current[0] - next_[0]) == 1 and current[1] == next_[1]:
            i += 1
            continue
        w += 1
        i += 1
    # count east sides
    v_east = sorted(list(visited_east), key=lambda x: (x[1], x[0]))
    e = 1
    i = 0
    while i < len(v_east) - 1:
        current = v_east[i]
        next_ = v_east[i + 1]
        if abs(current[0] - next_[0]) == 1 and current[1] == next_[1]:
            i += 1
            continue
        e += 1
        i += 1

    return n + e + s + w


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
