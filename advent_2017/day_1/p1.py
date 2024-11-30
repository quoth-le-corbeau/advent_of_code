import time
import pathlib


def sum_same_adjacent_digits(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip()
        first = int(lines[0])
        total = 0
        for index, char in enumerate(lines):
            if index == len(lines) - 1:
                if int(char) == first:
                    total += int(char)
                    return total
                else:
                    return total
            else:
                if char == lines[index + 1]:
                    total += int(char)
                else:
                    continue


start = time.perf_counter()
print(sum_same_adjacent_digits("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(sum_same_adjacent_digits("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
