from pathlib import Path
import itertools
from reusables import timer, INPUT_PATH


def _parse_grid(file_path: Path) -> tuple[dict[tuple[int, int], bool], list[list[str]]]:
    with open(file_path, "r") as puzzle_input:
        grid = [list(line) for line in puzzle_input.read().strip().splitlines()]
        return {
            (x, y): grid[y][x] == "#"
            for y in range(len(grid))
            for x in range(len(grid[0]))
        }, grid


def _get_vectors(point: tuple[int, int], rows: int, cols: int) -> set[tuple[int, int]]:
    all_vectors = set()
    # vectors |= _add_unit_vectors(cols=cols, rows=rows, point=point)
    x, y = point
    cols_to_left = x
    rows_below = rows - y - 1
    rows_above = y
    cols_to_right = cols - x - 1
    for col in range(cols_to_right + 1):
        for row in range(rows_above + 1):
            all_vectors.add((col, -row))
        for row in range(rows_below + 1):
            all_vectors.add((col, row))
    for col in range(cols_to_left + 1):
        for row in range(rows_above + 1):
            all_vectors.add((-col, -row))
        for row in range(rows_below + 1):
            all_vectors.add((-col, row))
    vectors = _filter(all_vectors)
    return vectors


def _filter(all_vectors):
    vectors = set()
    for vector in all_vectors:
        i, j = vector
        if (
            (abs(i) == abs(j) and abs(i) != 1)
            or (j == 0 and abs(i) != 1)
            or (i == 0 and abs(j) != 1)
        ):
            continue
        vectors.add(vector)
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


# part_one(file="eg")
# part_one(file="eg_1_2_35")
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
