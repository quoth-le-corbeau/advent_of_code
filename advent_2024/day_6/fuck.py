from pathlib import Path
from reusables import INPUT_PATH, timer

_VECTORS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def _parse_file(file: str) -> tuple[tuple[int, int], list[list[str]]]:
    with open(file=Path(__file__).resolve().parents[2] / file, mode="r") as f:
        grid = [list(lin) for lin in f.read().strip().splitlines()]
        start = None
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == "^":
                    start = (r, c)
        if start is None:
            raise ValueError
        return start, grid


def _escape(start: tuple[int, int], grid: list[list[str]]) -> set[tuple[int, int]]:
    position = start
    visited = set()
    vector_idx = 0
    vector = _VECTORS[vector_idx]
    visited.add(start)
    while 0 < position[0] < len(grid) - 1 and 0 < position[1] < len(grid[0]) - 1:
        nr, nc = position[0] + vector[0], position[1] + vector[1]
        if grid[nr][nc] == "#":
            vector_idx += 1
            vector_idx = vector_idx % len(_VECTORS)
        vector = _VECTORS[vector_idx]
        position = position[0] + vector[0], position[1] + vector[1]
        visited.add(position)
    return visited


def _loop_detected(start, grid) -> bool:
    position = start
    vector_idx = 0
    vector = _VECTORS[vector_idx]
    visited = set()
    while 0 < position[0] < len(grid) - 1 and 0 < position[1] < len(grid[0]) - 1:
        nr, nc = position[0] + vector[0], position[1] + vector[1]
        if grid[nr][nc] == "#":
            vector_idx += 1
            vector_idx = vector_idx % len(_VECTORS)
        vector = _VECTORS[vector_idx]
        position = position[0] + vector[0], position[1] + vector[1]
        if (position, vector) in visited:
            return True
        visited.add((position, vector))
    return False


@timer
def part_one(file: str):
    start, grid = _parse_file(file=INPUT_PATH.format(file=file, year=2024, day=6))
    print(f"part 1: {len(_escape(start, grid))}")


part_one("input")


@timer
def part_two(file: str):
    start, grid = _parse_file(file=INPUT_PATH.format(file=file, year=2024, day=6))
    route_positions = _escape(start, grid)
    loop_creators = []
    for node in route_positions:
        if node == start:
            continue
        nr, nc = node
        grid[nr][nc] = "#"
        if _loop_detected(start, grid):
            loop_creators.append(node)
        grid[nr][nc] = "."

    print(len(loop_creators))


part_two("eg")
part_two("input")


@timer
def part_two_alt(file: str):
    start, grid = _parse_file(file=INPUT_PATH.format(file=file, year=2024, day=6))
    loop_creators = []
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            node = (r, c)
            if node == start:
                continue
            grid[r][c] = "#"
            if _loop_detected(start, grid):
                loop_creators.append(node)
            grid[r][c] = "."

    print(len(loop_creators))


part_two_alt("eg")
part_two_alt("input")
