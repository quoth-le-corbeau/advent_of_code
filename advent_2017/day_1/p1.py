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


timer_start = time.perf_counter()
print(
    sum_same_adjacent_digits(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2017/day_1"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    sum_same_adjacent_digits(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2017/day_1"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
