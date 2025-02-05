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


def _create_sub_grid(
    search_range: int, row_bound: int, col_bound: int, node: tuple[int, int]
) -> list[tuple[int, int]]:
    left_col_bound = max(node[1] - search_range, 0)
    right_col_bound = min(node[1] + search_range, col_bound)
    top_bound = max(node[0] - search_range, 0)
    bottom_bound = min(node[0] + search_range, row_bound)
    sub_grid = []
    for row in range(top_bound, bottom_bound + 1):
        for col in range(left_col_bound, right_col_bound + 1):
            sub_grid.append((row, col))
    return sub_grid


def _count_cheats(
    grid: list[list[str]], path: list[tuple[int, int]], search_range: int
) -> dict[int, int]:
    """
    loop through the path nodes
    create a sub-grid around the current path node search using bfs
    total picoseconds without cheats is len(path) - path.index(node)
    if we arrive at another path node with a higher index in the path list
    total picoseconds with cheat is len(path) - path.index_of(other_node) + path.index(current_node)
    ...
    .x.
    ...
    """
    picoseconds_by_cheat_count = defaultdict(int)
    for i, step in enumerate(path):
        distance_to_end = i
        sub_grid = _create_sub_grid(
            search_range=search_range,
            row_bound=len(grid),
            col_bound=len(grid[0]),
            node=step,
        )

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
