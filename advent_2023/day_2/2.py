import time
import re
import pathlib


def get_minimum_cube_powers(file: str) -> int:
    powers = _get_powers(file=file)
    return sum(powers)


def _get_powers(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.readlines()
        powers = []
        for line in lines:
            cubes = line.strip().split(":")[1]
            all_red = re.findall(r"\d+ red", cubes)
            all_green = re.findall(r"\d+ green", cubes)
            all_blue = re.findall(r"\d+ blue", cubes)
            highest_red = _find_highest_for_colour(cubes_by_colour=all_red)
            highest_green = _find_highest_for_colour(cubes_by_colour=all_green)
            highest_blue = _find_highest_for_colour(cubes_by_colour=all_blue)
            powers.append(highest_red * highest_green * highest_blue)
        return powers


def _find_highest_for_colour(cubes_by_colour: list[str]) -> int:
    return max([int(entry.split()[0]) for entry in cubes_by_colour])


start = time.perf_counter()
print(get_minimum_cube_powers("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(get_minimum_cube_powers("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
