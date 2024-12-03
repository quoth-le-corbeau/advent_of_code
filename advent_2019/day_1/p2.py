import time
import pathlib
import re


def sum_recursive_fuel_requirements(file_path: str) -> int:
    masses = _parse_input(file=file_path)
    total = 0
    for mass in masses:
        total += _sum_all_mass_fuels(mass=mass)
    return total


def _sum_all_mass_fuels(mass: int) -> int:
    total = 0
    while mass // 3 - 2 > 0:
        fuel = (mass // 3) - 2
        total += fuel
        mass = fuel
    return total


def _parse_input(file: str) -> int:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read()
        return map(int, re.findall(r"\d+", lines))


start = time.perf_counter()
print(
    sum_recursive_fuel_requirements(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2019/day_1"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    sum_recursive_fuel_requirements(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2019/day_1"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
