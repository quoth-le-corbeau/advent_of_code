import time
import pathlib
import math
import re


def sum_fuel_requirements(file_path: str) -> int:
    masses = _parse_input(file=file_path)
    total = 0
    for mass in masses:
        total += math.floor(mass / 3) - 2
    return total


def _parse_input(file: str) -> list[int]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        return map(int, re.findall(r"\d+", puzzle_input.read()))


timer_start = time.perf_counter()
print(
    sum_fuel_requirements(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2019/day_1"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    sum_fuel_requirements(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2019/day_1"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
