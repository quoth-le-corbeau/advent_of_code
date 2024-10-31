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


start = time.perf_counter()
print(calculate_resulting_freq("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(calculate_resulting_freq("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
