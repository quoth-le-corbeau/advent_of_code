import pathlib
from collections import deque

file_path = str(
    (pathlib.Path(__file__).resolve().parents[2] / "my_inputs/2024/day_16" / "eg.txt")
)
with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
    grid = [list(line) for line in puzzle_input.read().splitlines()]


def pprint(grid: list[list[str]]) -> None:
    for line in grid:
        print("".join(line))


start = None
end = None
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == "S":
            start = r, c
        if col == "E":
            end = r, c


def bfs(
    start: tuple[int, int], end: tuple[int, int], grid: list[list[str]]
) -> list[tuple[int, int]]:
    rows = len(grid)
    cols = len(grid[0])

    q = deque([[start]])
    visited = {start}

    while q:
        path = q.popleft()
        current = path[-1]

        if current == end:
            return path

        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_ = current[0] + direction[0], current[1] + direction[1]
            if 0 <= next_[0] < rows and 0 <= next_[1] < cols:
                if grid[next_[0]][next_[1]] != "#" and next_ not in visited:
                    q.append(path + [next_])
                    visited.add(next_)

    raise ValueError


def simulate(grid: list[list[str]], path: list[tuple[int, int]]) -> None:
    for p in path:
        grid[p[0]][p[1]] = "O"
    pprint(grid=grid)


path = bfs(start=start, end=end, grid=grid)
print(f"Path found with bfs: {path}")
simulate(grid=grid, path=path)
