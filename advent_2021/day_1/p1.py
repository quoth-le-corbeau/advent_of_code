import time
import pathlib
import re


def count_number_of_increased_depths(file_path: str) -> int:
    depths = _parse_depths(file=file_path)
    count = 0
    for i, depth in enumerate(depths):
        if i != 0 and depth > depths[i - 1]:
            count += 1
    return count


def _parse_depths(file: str) -> list[int]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read()
        return list(map(int, re.findall(r"\d+", lines)))


timer_start = time.perf_counter()
print(
    count_number_of_increased_depths(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2021/day_1"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
timer_start = time.perf_counter()
print(
    count_number_of_increased_depths(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2021/day_1"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
