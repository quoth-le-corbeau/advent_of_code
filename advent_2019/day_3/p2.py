import time
import pathlib
import re
import dataclasses
from typing import List, Dict, Tuple


@dataclasses.dataclass(frozen=True)
class Node:
    x: int
    y: int
    total_step_count: int

    @property
    def coordinates(self) -> Tuple[int, int]:
        return self.x, self.y

    def move_in_str_ln(self, direction: str, spaces: int):
        direction_map = {
            "R": (1, 0),
            "L": (-1, 0),
            "U": (0, 1),
            "D": (0, -1),
        }
        if direction not in direction_map:
            raise ValueError(f"Invalid direction: {direction}")
        dx, dy = direction_map[direction]
        return [
            Node(
                x=self.x + i * dx,
                y=self.y + i * dy,
                total_step_count=self.total_step_count + i,
            )
            for i in range(1, spaces + 1)
        ]


def find_earliest_intersection(file_path: str) -> int:
    wires = _parse_wires(file=file_path)
    visited_nodes_by_wire = _get_visited_nodes(instructions=wires)
    assert len(visited_nodes_by_wire) == 2
    intersections_with_step_counts = _get_intersections_with_step_counts(
        node_list_1=visited_nodes_by_wire[1], node_list_2=visited_nodes_by_wire[2]
    )
    step_counts_by_node_coordinates = _sum_step_counts_by_coordinates(
        nodes=intersections_with_step_counts
    )
    return min(step_counts_by_node_coordinates.values())


def _sum_step_counts_by_coordinates(nodes: List[Node]) -> Dict[Tuple[int, int], int]:
    step_counts_by_coordinates: Dict[Tuple[int, int], int] = dict()
    for node in nodes:
        if node.coordinates in step_counts_by_coordinates:
            step_counts_by_coordinates[node.coordinates] += node.total_step_count
        else:
            step_counts_by_coordinates[node.coordinates] = node.total_step_count
    return step_counts_by_coordinates


def _get_intersections_with_step_counts(
    node_list_1: List[Node], node_list_2: List[Node]
) -> List[Node]:
    coordinates_1 = {node.coordinates for node in node_list_1}
    coordinates_2 = {node.coordinates for node in node_list_2}
    common_coordinates = coordinates_1.intersection(coordinates_2)
    intersections = list()
    for node in node_list_1:
        if node.coordinates in common_coordinates:
            intersections.append(node)
    for node in node_list_2:
        if node.coordinates in common_coordinates:
            intersections.append(node)
    return intersections


def _get_visited_nodes(instructions: List[str]) -> Dict[int, List[Node]]:
    visited_nodes_by_wire = {k: [] for k in range(1, len(instructions) + 1)}
    for i, wire in enumerate(instructions):
        visited_nodes: List[Node] = list()
        current_node = Node(x=0, y=0, total_step_count=0)
        for instruction in wire.split(","):
            match = re.match(r"([A-Za-z])(\d+)", instruction)
            if match:
                direction = match.group(1)
                spaces = int(match.group(2))
            else:
                raise ValueError("The input string does not match the expected format")
            visited_nodes += current_node.move_in_str_ln(
                direction=direction, spaces=spaces
            )
            current_node = visited_nodes[-1]
        visited_nodes_by_wire[i + 1] += visited_nodes
    return visited_nodes_by_wire


def _parse_wires(file: str) -> List[str]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        return puzzle_input.read().strip().splitlines()


start = time.perf_counter()
print(find_earliest_intersection("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(find_earliest_intersection("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
