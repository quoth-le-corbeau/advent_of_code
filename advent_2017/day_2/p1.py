import time
import pathlib
import re


def calculate_check_sum(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        checksum = 0
        for line in lines:
            nums = list(map(int, re.findall(r"-?\d+", line)))
            largest = max(nums)
            smallest = min(nums)
            checksum += largest - smallest
        return checksum


start = time.perf_counter()
print(
    calculate_check_sum(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2017/day_2"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    calculate_check_sum(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2017/day_2"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
