import heapq
import pathlib
from collections import deque

_UNIT_VECTORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def _get_grid(file_path: str):

    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        grid = [list(line) for line in puzzle_input.read().splitlines()]
    start = None
    end = None
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "S":
                start = r, c
            if col == "E":
                end = r, c
    if start is None:
        start = (0, 0)
    if end is None:
        end = len(grid) - 1, len(grid[0]) - 1
    return grid, start, end, len(grid), len(grid[0])


def _show_all_nodes(
    grid: list[list[str]],
    path: list[tuple[int, int]],
    message: str = "",
) -> None:
    for node in path:
        grid[node[0]][node[1]] = "*"
    pprint(grid=grid, path=path, message=message)


def pprint(grid: list[list[str]], path: list[tuple[int, int]], message: str) -> None:
    print("------------------------------------------------")
    print(message)
    print(path)
    for line in grid:
        print("".join(line))


def bfs(file_path) -> list[tuple[int, int]]:
    grid, start, end, rows, cols = _get_grid(file_path)
    q = deque([[start]])
    visited = {start}

    while q:
        path = q.popleft()
        current = path[-1]

        if current == end:
            _show_all_nodes(
                grid=grid,
                path=path,
                message=f"BFS searched {len(visited)} nodes and found shortest path: with length {len(path)} ",
            )
            return path

        for direction in _UNIT_VECTORS:
            next_ = current[0] + direction[0], current[1] + direction[1]
            if 0 <= next_[0] < rows and 0 <= next_[1] < cols:
                if grid[next_[0]][next_[1]] != "#" and next_ not in visited:
                    q.append(path + [next_])
                    visited.add(next_)

    raise ValueError


def bfs_least_turns(file_path: str) -> list[tuple[int, int]]:
    grid, start, end, rows, cols = _get_grid(file_path)
    q = deque([[start]])
    visited = {start}

    while q:
        path = q.popleft()
        current = path[-1]

        if current == end:
            _show_all_nodes(
                grid=grid,
                path=path,
                message=f"BFS_LT searched {len(visited)} nodes and found path with least turns with length {len(path)}: ",
            )
            return path

        for direction in _UNIT_VECTORS:
            next_ = current[0] + direction[0], current[1] + direction[1]
            if 0 <= next_[0] < rows and 0 <= next_[1] < cols:
                if grid[next_[0]][next_[1]] != "#" and next_ not in visited:
                    q.append(path + [next_])
                    visited.add(next_)

    raise ValueError


def a_star(file_path: str) -> list[tuple[int, int]]:
    grid, start, end, rows, cols = _get_grid(file_path)

    def heuristic(node1: tuple[int, int], node2: tuple[int, int]) -> int:
        return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

    pq = []
    heapq.heappush(pq, (0, start, [start]))
    visited = {start}

    while pq:
        cost, current, path = heapq.heappop(pq)

        if current == end:
            _show_all_nodes(
                grid=grid,
                path=path,
                message=f"A_STAR searched {len(visited)} nodes and found shortest path with length {len(path)}: ",
            )
            return path
        for direction in _UNIT_VECTORS:
            next_ = current[0] + direction[0], current[1] + direction[1]
            if (
                0 <= next_[0] < rows
                and 0 <= next_[1] < cols
                and grid[next_[0]][next_[1]] != "#"
                and next_ not in visited
            ):
                heapq.heappush(
                    pq, (cost + 1 + heuristic(next_, end), next_, path + [next_])
                )
                visited.add(next_)
    raise ValueError


bfs(
    file_path=str(
        (
            pathlib.Path(__file__).resolve().parents[2]
            / "my_inputs/2024/day_16"
            / "eg.txt"
        )
    )
)
a_star(
    file_path=str(
        (
            pathlib.Path(__file__).resolve().parents[2]
            / "my_inputs/2024/day_16"
            / "eg.txt"
        )
    )
)
bfs(file_path="day_18_input.txt")
a_star(file_path="day_18_input.txt")
