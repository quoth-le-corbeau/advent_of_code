from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_grid(file_path: Path) -> tuple[dict[tuple[int, int], bool], list[list[str]]]:
    with open(file_path, "r") as puzzle_input:
        grid = [list(line) for line in puzzle_input.read().strip().splitlines()]
        return {
            (x, y): grid[y][x] == "#"
            for y in range(len(grid))
            for x in range(len(grid[0]))
        }, grid


def _get_vectors(y: int, x: int, rows: int, cols: int) -> list[tuple[int, int]]:
    pass


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
            unit_vectors = _get_vectors(r, c, rows, cols)


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
