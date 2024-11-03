import time
import pathlib


def calculate_checksum(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        letter_lines = puzzle_input.read().splitlines()
        two_count = 0
        three_count = 0
        for line in letter_lines:
            two = False
            three = False
            for char in set(line):
                if line.count(char) == 2:
                    two = True
                    continue
                if line.count(char) == 3:
                    three = True
                    continue
            if two:
                two_count += 1
            if three:
                three_count += 1
        return three_count * two_count


start = time.perf_counter()
print(calculate_checksum("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(calculate_checksum("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
