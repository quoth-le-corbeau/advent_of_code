import time
import pathlib
import re


def scan_corrupted_memory(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read()
        pattern = r"mul\((-?\d+),\s*(-?\d+)\)"
        matches = re.findall(pattern, lines)
        return sum([int(X) * int(Y) for X, Y in matches])


start = time.perf_counter()
print(scan_corrupted_memory("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(scan_corrupted_memory("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")