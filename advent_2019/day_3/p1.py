from typing import Set
import time
import pathlib
import dataclasses


@dataclasses.dataclass(frozen=True)
class Node:
    x: int
    y: int

    def move_one_space(self, i: int, j: int):
        return Node(self.x + i, self.y + j)

    @property
    def manhattan(self) -> int:
        return abs(self.x) + abs(self.y)


def find_manhattan_closest_intersection(file_path: str) -> int:
    wires = _parse_wires(file=file_path)
    all_visited = list()
    for wire in wires:
        visited: Set[Node] = set()
        current_node = Node(x=0, y=0)
        for instruction in wire.split(","):
            direction = instruction[0]
            spaces = int(instruction[1:])
            if direction == "i":
                if spaces >= 0:
                    steps = 0
                    while steps < spaces:
                        new_node = current_node.move_one_space(i=1, j=0)
                        visited.add(new_node)
                        current_node = new_node
                        steps += 1
                else:
                    steps = 0
                    while steps > spaces:
                        new_node = current_node.move_one_space(i=-1, j=0)
                        visited.add(new_node)
                        current_node = new_node
                        steps -= 1
            else:
                assert direction == "j"
                if spaces >= 0:
                    steps = 0
                    while steps < spaces:
                        new_node = current_node.move_one_space(i=0, j=1)
                        visited.add(new_node)
                        current_node = new_node
                        steps += 1
                else:
                    steps = 0
                    while steps > spaces:
                        new_node = current_node.move_one_space(i=0, j=-1)
                        visited.add(new_node)
                        current_node = new_node
                        steps -= 1
        all_visited.append(visited)
    intersections = set.intersection(*all_visited)
    return min([node.manhattan for node in intersections])


def _parse_wires(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = (
            puzzle_input.read()
            .replace("R", "i")
            .replace("U", "j")
            .replace("L", "i-")
            .replace("D", "j-")
            .strip()
            .splitlines()
        )
        return lines


start = time.perf_counter()
print(find_manhattan_closest_intersection("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(find_manhattan_closest_intersection("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
