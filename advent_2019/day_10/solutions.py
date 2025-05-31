from pathlib import Path
import itertools
from reusables import timer, INPUT_PATH

NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)
NESW_UNIT_VECTORS = {(0, 1), (0, -1), (1, 0), (-1, 0)}


def _parse_grid(file_path: Path) -> tuple[dict[tuple[int, int], bool], list[list[str]]]:
    with open(file_path, "r") as puzzle_input:
        grid = [list(line) for line in puzzle_input.read().strip().splitlines()]
        return {
            (x, y): grid[y][x] == "#"
            for y in range(len(grid))
            for x in range(len(grid[0]))
        }, grid


def _get_nesw_vectors(
    point: tuple[int, int], rows: int, cols: int
) -> set[tuple[int, int]]:
    vectors = NESW_UNIT_VECTORS
    x, y = point
    if x == 0:
        vectors.remove(WEST)
    if y == 0:
        vectors.remove(NORTH)
    if x == cols - 1:
        vectors.remove(EAST)
    if y == rows - 1:
        vectors.remove(SOUTH)
    return vectors


def _get_vectors(point: tuple[int, int], rows: int, cols: int) -> set[tuple[int, int]]:
    vectors = _get_nesw_vectors(point=point, rows=rows, cols=cols)
    x, y = point
    for i in range(1, cols - x):
        # q1
        for j in range(1, y + 1):
            vectors.add((i, -j))
        # q2
        for j in range(1, rows - y):
            vectors.add((i, j))
    for i in range(1, x + 1):
        # q3
        for j in range(1, rows - y):
            vectors.add((-i, j))
        # q4
        for j in range(1, y + 1):
            vectors.add((-i, -j))
    return vectors


def _count_visible(
    vectors: list[tuple[int, int]], look_up: dict[tuple[int, int], bool]
) -> int:
    pass


@timer
def part_one(file: str, day: int = 10, year: int = 2019) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    look_up, grid = _parse_grid(file_path=input_file_path)
    rows = len(grid)
    cols = len(grid[0])
    visible_look_up = {k: 0 for k in look_up if look_up[k]}
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "#":
                continue
            # unit_vectors = _get_vectors(point=(c, r), rows=rows, cols=cols)


#            visible_look_up[(c, r)] = _count_visible(
#                vectors=unit_vectors, look_up=look_up
#            )
#    max_asteroids = max(visible_look_up.values())
#    for k, v in visible_look_up.items():
#        if v == max_asteroids:
#            asteroid = k
#    print(f"max visible asteroids: {max_asteroids} at {k}")
#    return max_asteroids


part_one(file="eg")
part_one(file="eg_1_2_35")
# part_one(file="eg_5_8_33")
# part_one(file="eg_6_3_41")
# part_one(file="eg_11_13_210")
# part_one(file="input")


@timer
def part_two(file: str, day: int = 10, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    print(f"part 2: {_parse_grid(file_path=input_file_path)}")


# part_two(file="eg")
# part_two(file="input")
