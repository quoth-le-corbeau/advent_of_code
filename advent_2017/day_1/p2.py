import time
import pathlib


def sum_digits_a_step_away(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip()
        total = 0
        step = len(lines) // 2
        for index, char in enumerate(lines):
            if index == len(lines) - 1:
                if int(char) == int(lines[step]):
                    return total + int(char)
                else:
                    return total
            elif index >= len(lines) - step:
                if int(char) == int(lines[(step + index) % len(lines)]):
                    total += int(char)
            else:
                if char == lines[index + step]:
                    total += int(char)
                else:
                    continue


start = time.perf_counter()
print(sum_digits_a_step_away("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(sum_digits_a_step_away("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
