import time
import pathlib
import re


def count_depth_increases_in_window(file_path: str) -> int:
    window_sums = _parse_depth_windows(file=file_path)
    count = 0
    for i, window_sum in enumerate(window_sums):
        if i != 0 and window_sum > window_sums[i - 1]:
            count += 1
    return count


def _parse_depth_windows(file: str) -> list[int]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read()
        depths = list(map(int, re.findall(r"\d+", lines)))
        windows = list()
        for i in range(len(depths) - 2):
            window = [depths[k] for k in range(i, i + 3)]
            windows.append(sum(window))
        return windows


timer_start = time.perf_counter()
print(
    count_depth_increases_in_window(
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
    count_depth_increases_in_window(
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
