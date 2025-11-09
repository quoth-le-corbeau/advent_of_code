from collections import deque
from dataclasses import dataclass
from pathlib import Path

from reusables import timer, INPUT_PATH

UNIT_VECTORS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

SYMBOL_BY_UNIT_VECTOR = {(1, 0): ">", (-1, 0): "<", (0, 1): "v", (0, -1): "^"}
node = tuple[int, int]


@dataclass(frozen=True)
class Grid:
    start_node: node
    end_node: node
    rows: list[list[int]]
    all_possible_starts: list[node]

    def __post_init__(self):
        row_length = len(self.rows[0])
        for row in self.rows:
            if len(row) != row_length:
                raise ValueError(
                    f"Rows must all be of length: {row_length}. Not {len(row)}!"
                )

    def bfs_shortest_s_to_e(self, start: node | None = None) -> list[node]:
        start = self.start_node if start is None else start
        q = deque([[start]])
        seen = {start}

        while q:
            path = q.popleft()
            current_node = path[-1]
            current_node_value = self.rows[current_node[1]][current_node[0]]
            if current_node == self.end_node:
                return path

            for vector in UNIT_VECTORS:
                next_i = current_node[0] + vector[0]
                next_j = current_node[1] + vector[1]
                if 0 <= next_i < len(self.rows[0]) and 0 <= next_j < len(self.rows):
                    next_node = (next_i, next_j)
                    next_node_value = self.rows[next_node[1]][next_node[0]]
                    if next_node in seen or next_node_value > 1 + current_node_value:
                        continue
                    else:
                        q.append(path + [next_node])
                        seen.add(next_node)
        raise ValueError("No path found!")

    def pprint_path(self) -> None:
        grid_to_print = []
        path = self.bfs_shortest_s_to_e()
        for j in range(len(self.rows)):
            row_to_print = []
            for i in range(len(self.rows[0])):
                current_node = (i, j)
                if self.rows[j][i] == 0:
                    row_to_print.append("S")
                    continue
                if self.rows[j][i] == 27:
                    row_to_print.append("E")
                    continue
                if current_node in path:
                    node_index = path.index(current_node)
                    if node_index < len(path) - 1:
                        next_path_node = path[node_index + 1]
                        vector = next_path_node[0] - i, next_path_node[1] - j
                        row_to_print.append(SYMBOL_BY_UNIT_VECTOR[vector])
                else:
                    row_to_print.append(".")
            grid_to_print.append(row_to_print)
        for row in grid_to_print:
            print("".join(row))


def _parse_grid(file_path: Path) -> Grid:
    grid = []
    s = None
    e = None
    possible_starts = []
    with open(file_path, "r") as puzzle_input:
        for j, line in enumerate(puzzle_input.read().strip().splitlines()):
            row = []
            for i, char in enumerate(line):
                if char == "S":
                    s = (i, j)
                    row.append(1)
                    possible_starts.append(s)
                elif char == "E":
                    e = (i, j)
                    row.append(27)
                elif char == "a":
                    possible_starts.append((i, j))
                    row.append(ord(char) - 96)
                else:
                    row.append(ord(char) - 96)
            grid.append(row)
    return Grid(
        start_node=s, end_node=e, rows=grid, all_possible_starts=possible_starts
    )


@timer
def part_one(file: str, day: int = 12, year: int = 2022):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    grid = _parse_grid(file_path=input_file_path)
    shortest_path = grid.bfs_shortest_s_to_e()
    # grid.pprint_path()
    return len(shortest_path) - 1


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 12, year: int = 2022):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    grid = _parse_grid(file_path=input_file_path)
    shortest_path_lengths = []
    for start in grid.all_possible_starts:
        try:
            shortest_path_lengths.append(len(grid.bfs_shortest_s_to_e(start)) - 1)
        except ValueError:
            # print(f"No path found from {start} to {grid.end_node}!")
            continue
    return min(shortest_path_lengths)


part_two(file="eg")
part_two(file="input")
