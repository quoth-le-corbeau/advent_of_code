import time
import pathlib

_DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Guard:
    def __init__(
        self,
        row: int,
        col: int,
        facing_direction: tuple[int, int],
        visited: set[tuple[int, int]],
    ):
        self.row = row
        self.col = col
        self.facing_direction = facing_direction
        self.visited = visited

    @property
    def position(self) -> tuple[int, int]:
        return (self.row, self.col)

    def move_in_grid(self):
        self.row += self.facing_direction[0]
        self.col += self.facing_direction[1]

    def record_position(self) -> None:
        self.visited.add((self.row, self.col))

    def leaves_grid(self, row_bound: int, col_bound: int) -> bool:
        new_row = self.row + self.facing_direction[0]
        new_col = self.col + self.facing_direction[1]
        return (
            new_col < 0 or new_row < 0 or new_col >= col_bound or new_row >= row_bound
        )

    def must_change_direction(self, obstacle_map: dict[int, set[int]]):
        return (
            self.col + self.facing_direction[1]
            in obstacle_map[self.row + self.facing_direction[0]]
        )

    def change_direction(self):
        current_direction_index = _DIRECTIONS.index(self.facing_direction)
        self.facing_direction = _DIRECTIONS[
            (current_direction_index + 1) % len(_DIRECTIONS)
        ]


def count_possible_loop_creators(file_path: str) -> int:
    start, obstacles_by_row, col_bound, row_bound = _parse_map(file=file_path)
    guard = Guard(
        row=start[0],
        col=start[1],
        visited={(start[0], start[1])},
        facing_direction=_DIRECTIONS[0],
    )
    loop_creators = set()
    while not guard.leaves_grid(row_bound=row_bound, col_bound=col_bound):
        prospective_node = (
            guard.row + guard.facing_direction[0],
            guard.col + guard.facing_direction[1],
        )
        if prospective_node in loop_creators:
            pass
        elif _loop_creator_check(
            obstacle_map=obstacles_by_row,
            row=guard.row,
            col=guard.col,
            facing_direction=guard.facing_direction,
            row_bound=row_bound,
            col_bound=col_bound,
        ):
            loop_creators.add(prospective_node)
        if guard.must_change_direction(obstacle_map=obstacles_by_row):
            guard.change_direction()
        else:
            guard.move_in_grid()
            guard.record_position()

    print(len(guard.visited))
    return len(loop_creators)


def _loop_creator_check(
    obstacle_map: dict[int, set[int]],
    row: int,
    col: int,
    facing_direction: tuple[int, int],
    row_bound: int,
    col_bound: int,
) -> bool:
    next_direction_index = _DIRECTIONS.index(facing_direction) + 1
    next_direction = _DIRECTIONS[next_direction_index % len(_DIRECTIONS)]
    theoretical_guard = Guard(
        row=row, col=col, visited={(row, col)}, facing_direction=next_direction
    )
    currently_facing = facing_direction
    current_position = row, col
    while not (
        theoretical_guard.position == current_position
        and theoretical_guard.facing_direction == currently_facing
    ):
        if theoretical_guard.leaves_grid(row_bound=row_bound, col_bound=col_bound):
            return False
        if theoretical_guard.must_change_direction(obstacle_map=obstacle_map):
            theoretical_guard.change_direction()
        else:
            theoretical_guard.move_in_grid()
            # theoretical_guard.record_position()
    print(
        f"got here for start: {current_position}. currently_facing: {currently_facing}"
    )
    return True


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
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
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
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
