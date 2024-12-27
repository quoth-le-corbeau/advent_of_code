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

    def could_create_loop(
        self,
        direction_increment: int,
        obstacle_map: dict[int, set[int]],
        row_bound: int,
        col_bound: int,
    ) -> bool:
        next_direction = _DIRECTIONS[(direction_increment + 1) % len(_DIRECTIONS)]
        if next_direction == _DIRECTIONS[1]:
            # guard facing north
            for c in range(self.col, col_bound):
                if c in obstacle_map[self.row]:
                    for j in range(self.row + 1, row_bound):
                        if c - 1 in obstacle_map[j]:
                            if self.col - 1 in obstacle_map[j]:
                                return True
        elif next_direction == _DIRECTIONS[2]:
            # guard facing east
            for r in range(self.row + 1, row_bound):
                if self.col in obstacle_map[r]:
                    for c in range(self.col - 1, -1, -1):
                        if c in obstacle_map[r - 1]:
                            if c + 1 in obstacle_map[self.row - 1]:
                                return True
        elif next_direction == _DIRECTIONS[3]:
            # guard facing south
            for c in range(self.col - 1, -1, -1):
                if c in obstacle_map[self.row]:
                    for r in range(self.row - 1, -1, -1):
                        if c + 1 in obstacle_map[r]:
                            if self.col + 1 in obstacle_map[r + 1]:
                                return True
        elif next_direction == _DIRECTIONS[0]:
            # guard facing west
            for r in range(self.row - 1, -1, -1):
                if self.col in obstacle_map[r]:
                    for c in range(self.col + 1, col_bound):
                        if c in obstacle_map[r + 1]:
                            if c - 1 in obstacle_map[self.row + 1]:
                                return True
        else:
            raise ValueError("Guard facing unknown direction!")
        return False

    def must_change_direction(
        self, obstacle_map: dict[int, set[int]], vector: [tuple[int, int]]
    ):
        return self.col + vector[1] in obstacle_map[self.row + vector[0]]


def count_possible_loop_creators(file_path: str) -> int:
    start, obstacles_by_row, col_bound, row_bound = _parse_map(file=file_path)
    print(f"{col_bound=}")
    guard = Guard(row=start[0], col=start[1], visited={(start[0], start[1])})
    direction_increment = 0
    direction = _DIRECTIONS[direction_increment % len(_DIRECTIONS)]
    loop_nodes = 0
    while not guard.leaves_grid(
        vector=direction, row_bound=row_bound, col_bound=col_bound
    ):
        if guard.could_create_loop(
            direction_increment=direction_increment,
            obstacle_map=obstacles_by_row,
            row_bound=row_bound,
            col_bound=col_bound,
        ):
            loop_nodes += 1
        if guard.must_change_direction(obstacle_map=obstacles_by_row, vector=direction):
            direction_increment += 1
            direction = _DIRECTIONS[direction_increment % len(_DIRECTIONS)]
        else:
            guard.move_in_grid(vector=direction)
            guard.record_position()
    print(f"{len(guard.visited)=}")
    return loop_nodes


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


timer_start = time.perf_counter()
print(
    count_possible_loop_creators(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_6"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    count_possible_loop_creators(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_6"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
