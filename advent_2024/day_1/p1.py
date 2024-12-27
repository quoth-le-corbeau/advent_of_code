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


timer_start = time.perf_counter()
print(
    sum_location_differences(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_1"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    sum_location_differences(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_1"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
