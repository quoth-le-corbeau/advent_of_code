import time
import pathlib

_DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Guard:
    def __init__(
        self,
        row: int,
        col: int,
        visited: set[tuple[int, int]],
    ):
        self.row = row
        self.col = col
        self.visited = visited

    def move_in_grid(self, vector: tuple[int, int]):
        self.row += vector[0]
        self.col += vector[1]

    def record_position(self) -> None:
        self.visited.add((self.row, self.col))

    def leaves_grid(
        self, vector: tuple[int, int], row_bound: int, col_bound: int
    ) -> bool:
        new_row = self.row + vector[0]
        new_col = self.col + vector[1]
        return (
            new_col < 0 or new_row < 0 or new_col >= col_bound or new_row >= row_bound
        )

    def must_change_direction(
        self, obstacle_map: dict[int, set[int]], vector: [tuple[int, int]]
    ):
        return self.col + vector[1] in obstacle_map[self.row + vector[0]]


def unique_guard_positions(file_path: str) -> int:
    start, obstacles_by_row, col_bound, row_bound = _parse_map(file=file_path)
    guard = Guard(row=start[0], col=start[1], visited={(start[0], start[1])})
    direction_increment = 0
    direction = _DIRECTIONS[direction_increment % len(_DIRECTIONS)]
    while not guard.leaves_grid(
        vector=direction, row_bound=row_bound, col_bound=col_bound
    ):
        if guard.must_change_direction(obstacle_map=obstacles_by_row, vector=direction):
            direction_increment += 1
            direction = _DIRECTIONS[direction_increment % len(_DIRECTIONS)]
        else:
            guard.move_in_grid(vector=direction)
            guard.record_position()

    return len(guard.visited)


def _parse_map(file: str) -> tuple[tuple[int, int], dict[int, set[int]], int, int]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        col_bound = len(lines)
        obstacles_by_row = {x: set() for x in range(col_bound)}
        start = None
        row_bound = len(lines[0])
        for row, line in enumerate(lines):
            if len(line) == 0:
                pass
            for col, char in enumerate(line):
                if char == "#":
                    obstacles_by_row[row].add(col)
                elif char == "^":
                    start = (row, col)
                else:
                    continue
        return start, obstacles_by_row, col_bound, row_bound


start = time.perf_counter()
print(
    unique_guard_positions(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_6"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    unique_guard_positions(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_6"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
