import time
import pathlib


def calculate_resulting_freq(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        return sum([int(entry) for entry in puzzle_input.read().splitlines()])


def calculate_resulting_freq_v2(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        result = 0
        for entry in puzzle_input.read().splitlines():
            result += int(entry)
    return result


timer_start = time.perf_counter()
print(
    calculate_resulting_freq(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2018/day_1"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    calculate_resulting_freq(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2018/day_1"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
