from pathlib import Path

from reusables import timer, INPUT_PATH

# n ne e se s sw w nw
_UNIT_VECTORS = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]


GridPoint = type(tuple[int, int])


def _parse_grid(file_path: Path) -> list[str]:
    with open(file_path, "r") as puzzle_input:
        grid = puzzle_input.read().strip().splitlines()
    return grid


def _find_removable_bogrolls(grid: list[str]) -> list[GridPoint]:
    forkliftables: list[GridPoint] = []
    for row, line in enumerate(grid):
        for col, grid_point in enumerate(line):
            if grid_point == "@":
                adj_count = 0
                for v in _UNIT_VECTORS:
                    r = row + v[1]
                    c = col + v[0]
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                        if grid[r][c] == "@":
                            adj_count += 1
                    if adj_count >= 4:
                        break
                if adj_count < 4:
                    forkliftables.append((col, row))
    return forkliftables


@timer
def part_one(file: str, day: int = 4, year: int = 2025) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    grid = _parse_grid(file_path=input_file_path)
    return len(_find_removable_bogrolls(grid))


# part_one(file="eg")
# part_one(file="input")


def _parse_grid_editable(file_path: Path) -> list[list[str]]:
    with open(file_path, "r") as puzzle_input:
        grid = [list(line) for line in puzzle_input.read().strip().splitlines()]
    return grid


def _find_and_remove_bogrolls(grid: list[list[str]]) -> list[list[str]]:
    forkliftables: list[GridPoint] = []
    for row, line in enumerate(grid):
        for col, grid_point in enumerate(line):
            if grid_point == "@":
                adj_count = 0
                for v in _UNIT_VECTORS:
                    r = row + v[1]
                    c = col + v[0]
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                        if grid[r][c] == "@":
                            adj_count += 1
                    if adj_count >= 4:
                        break
                if adj_count < 4:
                    forkliftables.append((col, row))
    print(f"Removing {len(forkliftables)} bogrolls")
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (c, r) in forkliftables:
                grid[r][c] = "x"
    return grid


def _print_grid(grid: list[list[str]]) -> None:
    for r in grid:
        print("".join(r))


@timer
def part_two(file: str, day: int = 4, year: int = 2025) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    grid = _parse_grid_editable(input_file_path)
    _print_grid(grid)
    g1 = _find_and_remove_bogrolls(grid)
    _print_grid(g1)


part_two(file="eg")
# part_two(file="input")
