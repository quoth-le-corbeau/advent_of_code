import time
import pathlib


def count_possible_passwords(file_path: str):
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        password_range_map = tuple(map(int, puzzle_input.read().strip().split("-")))
        # define mathematical condition for counting number of possible repeated digits
        # define mathematical condition for counting number of possible numbers with increasing digits




start = time.perf_counter()
print(count_possible_passwords("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
