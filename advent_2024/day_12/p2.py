import time
import pathlib
from collections import deque, defaultdict

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
    first get all squares that border the egde of the grid or another patch
    consider each direction separately
    sort the peripheral stones (note that east and west will be sorted by col first)
    loop through the peripheral stones only adding to the side count if a line is finished
    or if the level of indent changes. this will also handle internal borders
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
    v_north = sorted(list(visited_north))
    n_dict = defaultdict(list)
    for r, c in v_north:
        n_dict[r].append(c)
    n = 0
    for row, cols in n_dict.items():
        s_cols = sorted(cols)
        n += 1
        i = 0
        while i < len(s_cols) - 1:
            if abs(s_cols[i] - s_cols[i + 1]) == 1:
                i += 1
                continue
            n += 1
            i += 1

    # count south sides
    v_south = sorted(list(visited_south))
    s_dict = defaultdict(list)
    for r, c in v_south:
        s_dict[r].append(c)
    s = 0
    for row, cols in s_dict.items():
        s_cols = sorted(cols)
        s += 1
        i = 0
        while i < len(s_cols) - 1:
            if abs(s_cols[i] - s_cols[i + 1]) == 1:
                i += 1
                continue
            s += 1
            i += 1

    # count west sides
    v_west = sorted(list(visited_west), key=lambda x: (x[1], x[0]))
    w_dict = defaultdict(list)
    for r, c in v_west:
        w_dict[c].append(r)
    w = 0
    for col, rows in w_dict.items():
        s_rows = sorted(rows)
        w += 1
        i = 0
        while i < len(s_rows) - 1:
            if abs(s_rows[i] - s_rows[i + 1]) == 1:
                i += 1
                continue
            w += 1
            i += 1
    # count east sides
    v_east = sorted(list(visited_east), key=lambda x: (x[1], x[0]))
    e_dict = defaultdict(list)
    for r, c in v_east:
        e_dict[c].append(r)
    e = 0
    for col, rows in e_dict.items():
        s_rows = sorted(rows)
        e += 1
        i = 0
        while i < len(s_rows) - 1:
            if abs(s_rows[i] - s_rows[i + 1]) == 1:
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


timer_start = time.perf_counter()
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
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
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
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
