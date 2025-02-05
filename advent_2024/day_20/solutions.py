from collections import deque, defaultdict
from pathlib import Path
from reusables import timer, INPUT_PATH

_VECTORS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def _parse_input(file: str) -> tuple[tuple[int, int], tuple[int, int], list[list[str]]]:
    path = Path(__file__).resolve().parents[2] / file
    with path.open(mode="r") as puzzle_input:
        grid_lines = puzzle_input.read().splitlines()
        start = (-1, -1)
        end = (-1, -1)
        grid = [list(line) for line in grid_lines]
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == "S":
                    start = (r, c)
                elif col == "E":
                    end = (r, c)
                else:
                    continue
        assert start != (-1, -1) and end != (-1, -1)
        assert all(
            [
                grid[r][c] == "#"
                for r in range(len(grid))
                for c in range(len(grid[0]))
                if r in [0, len(grid) - 1] or c in [0, len(grid[0]) - 1]
            ]
        )
        return start, end, grid


def _bfs(
    start: tuple[int, int], end: tuple[int, int], grid: list[list[str]]
) -> list[tuple[int, int]]:
    queue = deque([[start]])
    visited = set()

    while len(queue) > 0:
        path = queue.popleft()
        current = path[-1]

        if current == end:
            return path

        for dr, dc in _VECTORS:
            nr, nc = current[0] + dr, current[1] + dc
            if (
                0 < nr < len(grid) - 1
                and 0 < nc < len(grid[0]) - 1
                and grid[nr][nc] != "#"
                and (nr, nc) not in visited
            ):
                queue.append(path + [(nr, nc)])
                visited.add((nr, nc))
    raise ValueError


def _verify_path(grid: list[list[str]], path: list[tuple[int, int]]) -> None:
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            current_symbol = col
            if (r, c) in path:
                assert (
                    current_symbol == "."
                    or current_symbol == "S"
                    or current_symbol == "E"
                )


def _count_cheats(
    grid: list[list[str]], path: list[tuple[int, int]], search_range: int
) -> dict[int, int]:
    picoseconds_by_cheat_count = defaultdict(int)
    for step in path:
        for vector in _VECTORS:
            nr, nc = step[0] + vector[0], step[1] + vector[1]
            sr, sc = (
                step[0] + search_range * vector[0],
                step[1] + search_range * vector[1],
            )
            if 0 < sr < len(grid) and 0 < sc < len(grid[0]):
                if grid[nr][nc] == "#" and (sr, sc) in path:
                    pass

        pass

    return picoseconds_by_cheat_count


@timer
def part_one(file: str) -> None:
    input_file = INPUT_PATH.format(file=file, year=2024, day=20)
    start, end, racecourse = _parse_input(file=input_file)
    racetrack: list[tuple[int, int]] = _bfs(start=start, end=end, grid=racecourse)
    # _verify_path(grid=racecourse, path=racetrack)
    pico_seconds_by_cheat_count = _count_cheats(
        grid=racecourse, path=racetrack, search_range=2
    )


part_one(file="eg")
