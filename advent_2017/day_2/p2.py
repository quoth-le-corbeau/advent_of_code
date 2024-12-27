import time
import pathlib
import re


def calculate_divisiblity_checksum(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        checksum = 0
        for line in lines:
            nums = list(map(int, re.findall(r"-?\d+", line)))
            print(f"nums: {nums}")
            for i, num in enumerate(nums):
                for n in nums:
                    if num % n == 0 and n != num:
                        checksum += num // n
                        print(f"{num=} {n=} {num // n=}")
        return checksum


timer_start = time.perf_counter()
print(
    calculate_divisiblity_checksum(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2017/day_2"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    calculate_divisiblity_checksum(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2017/day_2"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
