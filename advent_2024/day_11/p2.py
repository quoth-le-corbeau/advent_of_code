import time
import pathlib
from functools import cache


def count_the_blinking_stones(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        stones = [int(stone) for stone in puzzle_input.read().split()]

        @cache
        def count_to_last_blink(stone: int, remaining: int):
            if remaining == 0:
                return 1
            if stone == 0:
                return count_to_last_blink(1, remaining - 1)
            string = str(stone)
            if len(string) % 2 == 0:
                return count_to_last_blink(
                    int(string[: len(string) // 2]), remaining - 1
                ) + count_to_last_blink(int(string[len(string) // 2 :]), remaining - 1)
            else:
                return count_to_last_blink(stone * 2024, remaining - 1)

        return sum(count_to_last_blink(stone, 75) for stone in stones)


timer_start = time.perf_counter()
print(
    count_the_blinking_stones(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_11"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    count_the_blinking_stones(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_11"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
