from pathlib import Path

from reusables import INPUT_PATH, timer


def _initialise_puzzle(filename: str) -> tuple[list[list[str]], tuple[int, int]]:
    path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        file=filename, year=2024, day=6
    )
    with path.open(mode="r", encoding="utf-8") as puzzle_input:
        grid = [list(line) for line in puzzle_input.read().strip().splitlines()]
        start = (-float("inf"), float("inf"))
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == "^":
                    start = (r, c)
        if start[0] > len(grid) or start[1] > len(grid[0]):
            raise ValueError("Invalid start!")
    return grid, start


def _trace_guard_path(
    grid: list[list[str]], start: tuple[int, int]
) -> set[tuple[int, int]]:
    visited = set()
    j, i = (-1, 0)
    position = start
    visited.add(position)
    while 0 <= position[0] + j < len(grid) and 0 <= position[1] + i < len(grid[0]):
        nr, nc = position[0] + j, position[1] + i
        if grid[nr][nc] == "#":
            j, i = i, -j
        else:
            visited.add((nr, nc))
            position = nr, nc
    return visited


def _contains_loop(altered_grid: list[list[str]], start: tuple[int, int]) -> bool:
    r, c = start
    j, i = -1, 0
    visited = set()
    while True:
        if (r, c, j, i) in visited:
            return True
        visited.add((r, c, j, i))
        if not (0 <= r + j < len(altered_grid) and 0 <= c + i < len(altered_grid[0])):
            return False
        if altered_grid[r + j][c + i] == "#":
            j, i = i, -j
        # without this else shit goes wrong!
        else:
            r += j
            c += i


@timer
def part_one(filename: str) -> None:
    grid, start = _initialise_puzzle(filename=filename)
    total_steps = len(_trace_guard_path(grid=grid, start=start))
    print(f"part 1: {total_steps} <- ({filename})")


part_one(filename="eg")
part_one(filename="input")


@timer
def part_two(filename: str) -> None:
    grid, start = _initialise_puzzle(filename=filename)
    guard_path = _trace_guard_path(grid=grid, start=start)
    guard_trappers = set()
    for r, c in guard_path:
        if grid[r][c] != ".":
            continue
        else:
            grid[r][c] = "#"
            if _contains_loop(altered_grid=grid, start=start):
                guard_trappers.add((r, c))
            grid[r][c] = "."
    print(f"part 2: {len(guard_trappers)} <- ({filename})")


part_two(filename="eg")
part_two(filename="input")
