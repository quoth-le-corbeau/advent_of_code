import time
import pathlib
from collections import defaultdict


def find_manhattan_closest_intersection(file_path: str) -> int:
    wires = _parse_wires(file=file_path)
    all_visited = list()
    for wire in wires:
        visited: dict[int, set[tuple[int, int]]] = defaultdict(set)
        steps = 0
        x = 0
        y = 0
        current_node = [x, y]
        for instruction in wire.split(","):
            direction = instruction[0]
            spaces = int(instruction[1:])
            if direction == "i":
                if spaces >= 0:
                    p = 0
                    while p < spaces:
                        steps += 1
                        new_node = current_node[0] + 1, current_node[1]
                        visited[steps].add(new_node)
                        current_node = new_node
                        p += 1
                else:
                    p = 0
                    while p > spaces:
                        steps += 1
                        new_node = current_node[0] - 1, current_node[1]
                        visited[steps].add(new_node)
                        current_node = new_node
                        p -= 1
            else:
                assert direction == "j"
                if spaces >= 0:
                    p = 0
                    while p < spaces:
                        steps += 1
                        new_node = current_node[0], current_node[1] + 1
                        visited[steps].add(new_node)
                        current_node = new_node
                        p += 1
                else:
                    p = 0
                    while p > spaces:
                        steps += 1
                        new_node = current_node[0], current_node[1] - 1
                        visited[steps].add(new_node)
                        current_node = new_node
                        p -= 1
        all_visited.append(visited.values())
    print(f"{all_visited=}")
    # intersections = set.intersection(*all_visited.values())
    # print(f"{len(intersections)=}")
    return 0


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

# start = time.perf_counter()
# print(find_manhattan_closest_intersection("input.txt"))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
