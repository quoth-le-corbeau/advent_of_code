import time
import pathlib


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

    def move(self, direction: str):
        if direction == "N":
            self.col -= 1
            self.visited.add((self.row, self.col))
        elif direction == "S":
            self.col += 1
            self.visited.add((self.row, self.col))
        elif direction == "E":
            self.row += 1
            self.visited.add((self.row, self.col))
        elif direction == "W":
            self.row -= 1
            self.visited.add((self.row, self.col))
        else:
            raise ValueError(f"Invalid direction: {direction}")

    def is_clear(self, obstacle_map, direction: str) -> bool:
        if direction == "N":
            return all(
                [self.col not in obstacle_map[r] for r in range(self.row - 1, -1, -1)]
            )
        elif direction == "S":
            return all(
                [
                    self.col not in obstacle_map[r]
                    for r in range(self.row, max(obstacle_map.keys()), 1)
                ]
            )
        elif direction == "W":
            return all(
                [c not in obstacle_map[self.row] for c in range(self.col - 1, -1, -1)]
            )
        elif direction == "E":
            return all(
                [
                    c not in obstacle_map[self.row]
                    for c in range(self.col + 1, max(obstacle_map[self.row]), 1)
                ]
            )
        else:
            raise ValueError(f"Invalid direction: {direction}")

    def is_blocked(self, obstacle_map: dict[int, set[int]], direction: str) -> str:
        if direction == "N":
            if self.col in obstacle_map[self.row + 1]:
                direction = "E"
        elif direction == "S":
            if self.col in obstacle_map[self.row - 1]:
                direction = "W"
        elif direction == "E":
            if self.col + 1 in obstacle_map[self.row]:
                direction = "S"
        elif direction == "W":
            if self.col - 1 in obstacle_map[self.row]:
                direction = "N"
        else:
            raise ValueError(f"Invalid direction: {direction}")
        return direction


def unique_guard_positions(file_path: str) -> int:
    start, obstacles_by_row, col_bound, row_bound = _parse_map(file=file_path)
    print(f"{col_bound=}")
    print(f"{row_bound=}")
    print(f"{start=}")
    print(f"{obstacles_by_row=}")
    guard = Guard(row=start[0], col=start[1], visited={(start[0], start[1])})
    direction = "N"
    while not guard.is_clear(obstacle_map=obstacles_by_row, direction=direction):
        guard.move(direction)
        direction = guard.is_blocked(obstacle_map=obstacles_by_row, direction=direction)

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

# start = time.perf_counter()
# print(unique_guard_positions(str((pathlib.Path(__file__).resolve().parents[2] / "my_inputs/2024/day_6" / "input.txt"))))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
