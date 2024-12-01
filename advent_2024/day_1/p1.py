import time
import pathlib
import numpy as np


def sum_location_differences(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        locations_1 = []
        locations_2 = []
        for line in lines:
            location_1, location_2 = tuple(map(int, line.replace("   ",",").split(",")))
            locations_1.append(location_1)
            locations_2.append(location_2)
        l1 = np.array(sorted(locations_1))
        l2 = np.array(sorted(locations_2))
        print(abs(l2 - l1))
        return sum(abs(l2 - l1))



start = time.perf_counter()
print(sum_location_differences("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(sum_location_differences("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
