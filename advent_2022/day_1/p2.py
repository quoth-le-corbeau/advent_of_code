import time
import pathlib


def find_top_three_most_calories(file: str):
    top_three_elves = [_get_all_elf_calories(file=file)[i] for i in range(-1, -4, -1)]
    return sum(top_three_elves)


def _get_all_elf_calories(file: str) -> list[int]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        calories_per_elf = puzzle_input.read().split("\n\n")
        total_calories_per_elf = list()
        for elf in calories_per_elf:
            all_calories_strings = elf.strip().split("\n")
            total_calories_per_elf.append(sum(list(map(int, all_calories_strings))))
    return sorted(total_calories_per_elf)


timer_start = time.perf_counter()
print(
    find_top_three_most_calories(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2022/day_1"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
timer_start = time.perf_counter()
print(
    find_top_three_most_calories(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2022/day_1"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
