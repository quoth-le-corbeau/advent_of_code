import heapq
import pathlib
from collections import deque


def _get_grid():
    file_path = str(
        (
            pathlib.Path(__file__).resolve().parents[2]
            / "my_inputs/2024/day_16"
            / "eg.txt"
        )
    )
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
    return grid, start, end, len(grid), len(grid[0])


GRID, START, END, ROWS, COLS = _get_grid()

_UNIT_VECTORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(
    start: tuple[int, int], end: tuple[int, int], grid: list[list[str]]
) -> tuple[list[tuple[int, int]], set[tuple[int, int]]]:
    q = deque([[start]])
    visited = {start}

    while q:
        path = q.popleft()
        current = path[-1]

        if current == end:
            return path, visited

        for direction in _UNIT_VECTORS:
            next_ = current[0] + direction[0], current[1] + direction[1]
            if 0 <= next_[0] < ROWS and 0 <= next_[1] < COLS:
                if grid[next_[0]][next_[1]] != "#" and next_ not in visited:
                    q.append(path + [next_])
                    visited.add(next_)

    raise ValueError


def a_star(
    start: tuple[int, int], end: tuple[int, int], grid: list[list[str]]
) -> tuple[list[tuple[int, int]], set[tuple[int, int]]]:

    def heuristic(node1: tuple[int, int], node2: tuple[int, int]) -> int:
        return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

    pq = []
    heapq.heappush(pq, (0, start, [start]))  # cost, current, path
    visited = {start}

    while pq:
        cost, current, path = heapq.heappop(pq)

        if current == end:
            return path, visited

        for direction in _UNIT_VECTORS:
            next_ = current[0] + direction[0], current[1] + direction[1]
            if (
                0 <= next_[0] < ROWS
                and 0 <= next_[1] < COLS
                and grid[next_[0]][next_[1]] != "#"
                and next_ not in visited
            ):
                heapq.heappush(
                    pq, (cost + 1 + heuristic(next_, end), next_, path + [next_])
                )
                visited.add(next_)
    raise ValueError


def show_all_nodes(
    grid: list[list[str]], nodes: list[tuple[int, int]], message: str = ""
) -> None:
    for node in nodes:
        grid[node[0]][node[1]] = "*"
    pprint(grid=grid, message=message)


def pprint(grid: list[list[str]], message: str) -> None:
    print("------------------------------------------------")
    print(message)
    for line in grid:
        print("".join(line))


bfs_path, all_bfs_checked_nodes = bfs(start=START, end=END, grid=GRID)
a_star_path, all_a_star_checked_nodes = a_star(start=START, end=END, grid=GRID)
print(
    f"Path found with BFS: {bfs_path}\nwith length: {len(bfs_path)} \nhad to check: {len(all_bfs_checked_nodes)} nodes:"
)
print(
    f"Path found with A_STAR: {a_star_path}\nwith length: {len(a_star_path)} \nhad to check: {len(all_a_star_checked_nodes)} nodes:"
)
print(
    f"BFS-checked nodes ignored by A_STAR: {all_bfs_checked_nodes - all_a_star_checked_nodes}"
)
show_all_nodes(grid=GRID, nodes=bfs_path, message="BFS found best path: ")
show_all_nodes(grid=GRID, nodes=a_star_path, message="A_STAR found best path: ")
show_all_nodes(
    grid=GRID, nodes=list(all_bfs_checked_nodes), message="All BFS nodes checked: "
)
show_all_nodes(
    grid=GRID,
    nodes=list(all_a_star_checked_nodes),
    message="All A_STAR nodes checked: ",
)
