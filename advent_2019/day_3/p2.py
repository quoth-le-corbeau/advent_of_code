import time
import pathlib
import dataclasses
from typing import List


@dataclasses.dataclass(frozen=True)
class Node:
    x: int
    y: int


def find_earliest_intersection(file_path: str) -> int:
    wires = _parse_wires(file=file_path)
    turning_points: List[Node] = list()
    for wire in wires:
        for point in wire.split(","):
            print(point)




def _parse_wires(file: str) -> list[str]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        return puzzle_input.read().strip().splitlines()


start = time.perf_counter()
print(find_earliest_intersection("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
# print(find_earliest_intersection("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
