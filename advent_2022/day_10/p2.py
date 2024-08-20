import os
import time
from pathlib import Path


def print_pixels_on_screen(file: str) -> None:
    program = _parse_program_file(file=file)
    sprite_position = [0, 1, 2]
    register = 1
    cycle_count = 0
    row = ""
    for line in program:
        i = 0
        while i < line[0]:
            if cycle_count % 40 == 0:
                print(row)
                row = ""
            if cycle_count % 40 in sprite_position:
                row += "# "
            else:
                row += ". "
            cycle_count += 1
            i += 1
        register += line[1]
        sprite_position = [register - 1, register, register + 1]
    print(row)


def _parse_program_file(file: str) -> list[tuple[int, int]]:
    with open(Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        program = list()
        for line in lines:
            if line.split()[0] == "noop":
                program.append((1, 0))
            else:
                program.append((2, int(line.split()[1])))
        return program


start = time.perf_counter()
print_pixels_on_screen("eg.txt")
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print_pixels_on_screen("input.txt")
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
