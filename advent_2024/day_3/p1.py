import time
import pathlib
import re


def scan_corrupted_memory(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read()
        pattern = r"mul\((-?\d+),\s*(-?\d+)\)"
        matches = re.findall(pattern, lines)
        return sum([int(X) * int(Y) for X, Y in matches])


timer_start = time.perf_counter()
print(
    scan_corrupted_memory(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_3"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    scan_corrupted_memory(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_3"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
