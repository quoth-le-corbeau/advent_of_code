from collections import deque
from pathlib import Path
from functools import cache

from reusables import timer, INPUT_PATH


def _parse_grid(file_path: Path):
    with open(file_path, "r") as puzzle_input:
        grid = puzzle_input.read().strip().splitlines()
        start = [
            (i, j)
            for j, row in enumerate(grid)
            for i, char in enumerate(row)
            if char == "S"
        ][0]
        return grid, start


def _bfs(grid: list[str], start: tuple[int, int]) -> int:
    total = 0
    q = deque([start])
    visited = set(start)

    while q:
        node = q.popleft()
        x, y = node
        if y >= len(grid) - 1:
            continue
        if grid[y][x] == "." or grid[y][x] == "S":
            if node not in visited:
                next_ = (x, y + 1)
                q.append(next_)
                visited.add(node)
        elif grid[y][x] == "^":
            total += 1
            if node not in visited:
                next_1 = (x + 1, y)
                next_2 = (x - 1, y)
                q.append(next_1)
                q.append(next_2)
                visited.add(node)
    return total


@timer
def part_one(file: str, day: int = 7, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    grid, start = _parse_grid(file_path=input_file_path)
    return _bfs(grid, start)


part_one(file="eg")
part_one(file="input")


def _trace_beam(
    node: tuple[int, int],
    grid: list[str],
    total: int = 0,
    homemade_cache: dict[tuple[int, int], int] | None = None,
):
    if homemade_cache is None:
        homemade_cache = dict()
    x, y = node
    if y >= len(grid) - 1:
        return 1

    if node in homemade_cache:
        return homemade_cache[node]

    if grid[y][x] == "." or grid[y][x] == "S":
        total += _trace_beam(node=(x, y + 1), grid=grid, homemade_cache=homemade_cache)
    elif grid[y][x] == "^":
        total += _trace_beam(node=(x + 1, y), grid=grid, homemade_cache=homemade_cache)
        total += _trace_beam(node=(x - 1, y), grid=grid, homemade_cache=homemade_cache)
    homemade_cache[node] = total
    return total


@timer
def part_two(file: str, day: int = 7, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    grid, start = _parse_grid(file_path=input_file_path)
    return _trace_beam(node=start, grid=grid)


part_two(file="eg")
part_two(file="input")


@timer
def part_two_syntactic_sugar(file: str, day: int = 7, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )

    @cache
    def _trace_beam_no_non_hashables_passed(node: tuple[int, int], total: int = 0):
        x, y = node
        if y >= len(grid):
            return 1
        if grid[y][x] == "." or grid[y][x] == "S":
            total += _trace_beam_no_non_hashables_passed((x, y + 1))
        elif grid[y][x] == "^":
            total += _trace_beam_no_non_hashables_passed((x + 1, y))
            total += _trace_beam_no_non_hashables_passed((x - 1, y))
        return total

    grid, start = _parse_grid(file_path=input_file_path)
    return _trace_beam_no_non_hashables_passed(node=start)


part_two_syntactic_sugar(file="eg")
part_two_syntactic_sugar(file="input")
