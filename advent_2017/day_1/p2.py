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


timer_start = time.perf_counter()
print(
    sum_digits_a_step_away(
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
    sum_digits_a_step_away(
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
