import time
import pathlib

"""
Race Condition Part I

create the initial grid
run a bfs to calculate the normal number of picoseconds
list the positions of all the walls that are not at the edge and 

"""


def RENAME_FUNC(file_path: str):
    RENAME = _RENAME_FUNC(file=file_path)
    pass


def _RENAME_FUNC(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read()
        print(lines)


start = time.perf_counter()
print(
    RENAME_FUNC(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_20"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    RENAME_FUNC(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_20"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
