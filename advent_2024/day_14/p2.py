import time
import pathlib
import re

"""
Restroom Redoubt Part II

rows: 103, cols: 101 
get all inputs as a list of 4 integers: pr, pc, vr, vc
end position for each robot = (pr + (100 * vr)) % 103, (pc + (100 * vc)) % 101


"""


def find_the_easter_egg(file_path: str, rows: int, cols: int) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        robots = [list(map(int, re.findall(r"([-+]?\d+)", line))) for line in lines]
        print(f"Robots: {robots}")
    # for i in range(100):
    # next_position = (r + (i * vr)) % rows, (c + (i * vc)) % cols


start = time.perf_counter()
print(
    find_the_easter_egg(
        file_path=str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_14"
                / "eg.txt"
            )
        ),
        rows=7,
        cols=11,
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    find_the_easter_egg(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_14"
                / "input.txt"
            )
        ),
        rows=103,
        cols=101,
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
