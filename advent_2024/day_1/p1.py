import time
import numpy as np
from advent_2024.day_1 import utils


def sum_location_differences(file_path: str) -> int:
    locations_1, locations_2 = utils.parse_into_equal_length_lists(file_path)
    l1 = np.array(sorted(locations_1))
    l2 = np.array(sorted(locations_2))
    return sum(abs(l2 - l1))


start = time.perf_counter()
print(sum_location_differences("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(sum_location_differences("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
