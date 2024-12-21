import heapq
import time
import pathlib


def _pprint(grid: list[list[str]], message: str = "") -> None:
    print(message)
    for line in grid:
        print("".join(line))


def _prepare_grid(
    fallen_byte_coordinates: list[str],
    number_of_fallen_bytes: int,
    rows: int,
    cols: int,
) -> list[list[str]]:
    grid = [["."] * cols for _ in range(rows)]
    for coordinates in fallen_byte_coordinates[:number_of_fallen_bytes]:
        r, c = int(coordinates.split(",")[1]), int(coordinates.split(",")[0])
        grid[r][c] = "#"
    return grid


def _a_star(
    grid: list[list[str]],
    start: tuple[int, int],
    end: tuple[int, int],
    fallen_bytes: int,
) -> list[tuple[int, int]]:
    rows = len(grid)
    cols = len(grid[0])

    def heuristic(node: tuple[int, int], end: tuple[int, int]) -> int:
        return abs(node[0] - end[0]) + abs(node[1] - end[1])

    pq = []
    heapq.heappush(pq, (0, start, [start]))
    visited = set()

    while pq:
        cost, current, path = heapq.heappop(pq)
        if current == end:
            for p in path:
                grid[p[0]][p[1]] = "O"
            _pprint(grid, message=f"Shortest path after {fallen_bytes} fallen bytes: ")
            return path

        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_ = current[0] + direction[0], current[1] + direction[1]
            if 0 <= next_[0] < rows and 0 <= next_[1] < cols:
                if grid[next_[0]][next_[1]] != "#" and next_ not in visited:
                    heapq.heappush(
                        pq, (cost + 1 + heuristic(next_, end), next_, path + [next_])
                    )
                    visited.add(next_)

    raise ValueError("No path found!")


def find_best_escape_path(
    file_path: str, rows: int = 71, cols: int = 71, fallen_bytes: int = 1024
) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        grid = _prepare_grid(
            fallen_byte_coordinates=puzzle_input.read().splitlines(),
            number_of_fallen_bytes=fallen_bytes,
            rows=rows,
            cols=cols,
        )
        _pprint(grid=grid, message=f"Grid after {fallen_bytes} fallen bytes: ")
        best_escape_path = _a_star(
            grid=grid, start=(0, 0), end=(rows - 1, cols - 1), fallen_bytes=fallen_bytes
        )
        print(f"{best_escape_path=}")
        return len(best_escape_path) - 1  # exclude start


start = time.perf_counter()
print(
    find_best_escape_path(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_18"
                / "eg.txt"
            )
        ),
        rows=7,
        cols=7,
        fallen_bytes=12,
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    find_best_escape_path(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_18"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
