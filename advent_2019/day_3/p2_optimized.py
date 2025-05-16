from pathlib import Path
from dataclasses import dataclass

from reusables import timer, INPUT_PATH

_VECTOR_LOOK_UP = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


@dataclass(frozen=True)
class Node:
    x: int
    y: int


def _parse_input(file_path: Path) -> tuple[list[str], list[str]]:
    with open(file_path, "r") as puzzle_input:
        wires = puzzle_input.read().strip().splitlines()
        if len(wires) != 2:
            raise ValueError
        return wires[0].split(","), wires[1].split(",")


def _visited_with_step_count(instructions: list[str]) -> dict[tuple[int, int], int]:
    x = y = steps = 0
    shortest_steps_by_visited = dict()
    for instruction in instructions:
        dx, dy = _VECTOR_LOOK_UP[instruction[0]]
        step_count = int(instruction[1:])
        for _ in range(step_count):
            x += dx
            y += dy
            steps += 1
            shortest_steps_by_visited.setdefault(Node(x, y), steps)
    return shortest_steps_by_visited


@timer
def part_two(file: str, day: int = 3, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    wire1, wire2 = _parse_input(file_path=input_file_path)
    wire1_steps_by_visited_node = _visited_with_step_count(wire1)
    wire2_steps_by_visited_node = _visited_with_step_count(wire2)
    cross_nodes = set(wire1_steps_by_visited_node.keys()).intersection(
        set(wire2_steps_by_visited_node.keys())
    )
    return min(
        [
            wire1_steps_by_visited_node[node] + wire2_steps_by_visited_node[node]
            for node in cross_nodes
        ]
    )


part_two(file="eg")
part_two(file="input")
