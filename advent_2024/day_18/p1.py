import pathlib
import time
from collections import deque

"""
Ram Run Part I

create a grid n x n with specified n
read in the fallen bytes (switch to row, col)
add # to grid for cut off number of fallen bytes
calculate best path from top left to bottom right with bfs
return the length of the best path

"""


class MemorySpace:
    def __init__(self, size: int):
        self.grid = [["."] * size for _ in range(size)]

    def add_bytes_to_grid(self, fallen_bytes: list[str], cutoff: int):
        for coordinates in fallen_bytes[:cutoff]:
            r, c = int(coordinates.split(",")[1]), int(coordinates.split(",")[0])
            self.grid[r][c] = "#"

    def show_path(self, path: list[tuple[int, int]]) -> None:
        for node in path:
            self.grid[node[0]][node[1]] = ">"
        self.pprint(message="Showing best path:")

    def pprint(self, message: str = ""):
        print(message)
        for row in self.grid:
            print("".join(row))


def _bfs(grid: list[list[str]]) -> list[tuple[int, int]]:
    rows = len(grid)
    cols = len(grid[0])
    start_ = (0, 0)
    end_ = (rows - 1, cols - 1)

    queue = deque([[start_]])
    visited = {start_}

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == end_:
            return path

        for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            next_ = current[0] + direction[0], current[1] + direction[1]
            if 0 <= next_[0] < rows and 0 <= next_[1] < cols:
                if grid[next_[0]][next_[1]] != "#" and next_ not in visited:
                    queue.append(path + [next_])
                    visited.add(next_)
    raise Exception("No path found")


def part_one(input: str, size: int, cutoff: int) -> int:
    with open(input, mode="r") as f:
        lines = f.read().strip().splitlines()
        memory_space = MemorySpace(size=size)
        # memory_space.pprint(message="original grid")
        memory_space.add_bytes_to_grid(fallen_bytes=lines, cutoff=cutoff)
        # memory_space.pprint(message=f"grid after {cutoff} fallen bytes")
        path = _bfs(memory_space.grid)
        memory_space.show_path(path=path)
        return len(path) - 1


start = time.perf_counter()
result_eg = part_one(
    input=str(
        pathlib.Path(__file__).resolve().parents[2] / "my_inputs/2024/day_18" / "eg.txt"
    ),
    size=7,
    cutoff=12,
)

print(f"Part 1 example: {result_eg}")
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
result = part_one(
    input=str(
        pathlib.Path(__file__).resolve().parents[2]
        / "my_inputs/2024/day_18"
        / "input.txt"
    ),
    size=71,
    cutoff=1024,
)
print(f"Part 2 example: {result}")
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
