import time
import pathlib


def calculate_resulting_freq(file_path: str) -> int:
    RENAME = _RENAME_FUNC(file=file_path)
    pass


def _RENAME_FUNC(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read()
        print(lines)


start = time.perf_counter()
print(calculate_resulting_freq("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

# start = time.perf_counter()
# print(RENAME_FUNC("input.txt"))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
