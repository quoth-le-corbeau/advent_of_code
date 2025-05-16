from pathlib import Path
from dataclasses import dataclass

from reusables import timer, INPUT_PATH

_VECTOR_LOOK_UP = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


@dataclass(frozen=True)
class Node:
    x: int
    y: int

    def __lt__(self, other):
        return self.manhattan() < other.manhattan()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def manhattan(self):
        return abs(self.x) + abs(self.y)


def _parse_input(file_path: Path) -> tuple[list[str], list[str]]:
    with open(file_path, "r") as puzzle_input:
        wires = puzzle_input.read().strip().splitlines()
        if len(wires) != 2:
            raise ValueError
        return wires[0].split(","), wires[1].split(",")


def _all_visited_nodes(instructions: list[str]) -> list[Node]:
    x, y = 0, 0
    visited = []
    for instruction in instructions:
        p, q = _VECTOR_LOOK_UP[instruction[0]]
        i = 0
        while i < int(instruction[1:]):
            x += p
            y += q
            visited.append(Node(x, y))
            i += 1
    return visited


@timer
def part_one(file: str, day: int = 3, year: int = 2019) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    wire_1, wire_2 = _parse_input(file_path=input_file_path)
    visited_1 = _all_visited_nodes(wire_1)
    visited_2 = _all_visited_nodes(wire_2)
    cross_nodes = sorted(list(set(visited_1).intersection(set(visited_2))))
    return min(cross_nodes).manhattan()


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 3, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    wire_1, wire_2 = _parse_input(file_path=input_file_path)
    visited_1 = _all_visited_nodes(wire_1)
    visited_2 = _all_visited_nodes(wire_2)
    cross_node = sorted(
        sorted(list(set(visited_1).intersection(set(visited_2)))),
        key=lambda x: sum([visited_1.index(x), visited_2.index(x)]),
    )[0]
    return visited_1.index(cross_node) + visited_2.index(cross_node) + 2


part_two(file="eg")
part_two(file="input")
