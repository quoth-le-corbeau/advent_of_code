import time
import pathlib
from collections import Counter


def count_overlaps(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        visited = list()
        for line in puzzle_input.read().splitlines():
            vertices = (
                line.replace(" ", "")
                .split("@")[1]
                .replace(":", ",")
                .replace("x", ",")
                .split(",")
            )
            for x in range(int(vertices[0]), int(vertices[0]) + int(vertices[2])):
                for y in range(int(vertices[1]), int(vertices[1]) + int(vertices[3])):
                    visited.append((x, y))
        counter = Counter(visited)
        return sum(1 for count in counter.values() if count > 1)


start = time.perf_counter()
print(
    count_overlaps(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2018/day_3"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    count_overlaps(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2018/day_3"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
