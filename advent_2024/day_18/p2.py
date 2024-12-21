import pathlib
import time
from collections import deque

"""
Ram Run Part II

same as part I
but include an add_byte_to_grid function that tracks the index of the fallen bytes
use bfs to check for paths after adding each byte until it fails to find path
return the coordinates at the index reached

"""


class MemorySpace:
    def __init__(self, size: int, cutoff: int):
        self.grid = [["."] * size for _ in range(size)]
        self.cutoff = cutoff

    def add_bytes_to_grid(self, fallen_bytes: list[str]):
        for coordinates in fallen_bytes[: self.cutoff]:
            r, c = int(coordinates.split(",")[1]), int(coordinates.split(",")[0])
            self.grid[r][c] = "#"

    def add_single_byte_to_grid(self, fallen_bytes: list[str]) -> str:
        coordinates = fallen_bytes[self.cutoff]
        r, c = int(coordinates.split(",")[1]), int(coordinates.split(",")[0])
        self.grid[r][c] = "#"
        self.cutoff += 1
        return coordinates

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
    return []


def part_two(input: str, size: int, cutoff: int) -> str:
    with open(input, mode="r") as f:
        lines = f.read().strip().splitlines()
        memory_space = MemorySpace(size=size, cutoff=cutoff)
        # memory_space.pprint(message="original grid")
        memory_space.add_bytes_to_grid(fallen_bytes=lines)
        # memory_space.pprint(message=f"grid after {cutoff} fallen bytes")
        path = _bfs(memory_space.grid)
        coordinates = lines[cutoff]
        print(f"first cutoff is {coordinates}")
        while len(path) > 0:
            coordinates = memory_space.add_single_byte_to_grid(fallen_bytes=lines)
            path = _bfs(memory_space.grid)

        return coordinates


start = time.perf_counter()
result_eg = part_two(
    input=str(
        pathlib.Path(__file__).resolve().parents[2] / "my_inputs/2024/day_18" / "eg.txt"
    ),
    size=7,
    cutoff=12,
)

print(f"Part 1 example: {result_eg}")
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
result = part_two(
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
