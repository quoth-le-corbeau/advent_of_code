import time
import pathlib
import numpy as np


def sum_location_differences(file_path: str) -> int:
    locations_1, locations_2 = _parse_into_equal_length_lists(file_path)
    l1 = np.array(sorted(locations_1))
    l2 = np.array(sorted(locations_2))
    return sum(abs(l2 - l1))


def _parse_into_equal_length_lists(file_path: str) -> tuple[list[int], list[int]]:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        list_1 = []
        list_2 = []
        for line in lines:
            integer_1, integer_2 = tuple(map(int, line.replace("   ", ",").split(",")))
            list_1.append(integer_1)
            list_2.append(integer_2)
        assert len(list_1) == len(list_2)
        return list_1, list_2


start = time.perf_counter()
print(sum_location_differences("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(sum_location_differences("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")