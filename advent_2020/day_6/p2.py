from typing import List, Set
import time
import pathlib


def count_unanimous_yesses(file_path: str) -> int:
    unanimous_yesses = _get_unanimous_yesses(file=file_path)
    count = 0
    for unanimous_yes in unanimous_yesses:
        count += len(unanimous_yes)
    return count


def _get_unanimous_yesses(file: str) -> List[Set[str]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().split("\n\n")
        unanimous_yesses = list()
        for line in lines:
            people = [set(answers) for answers in line.splitlines()]
            unanimous_yesses.append(set.intersection(*people))
        return unanimous_yesses


timer_start = time.perf_counter()
print(
    count_unanimous_yesses(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2020/day_6"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    count_unanimous_yesses(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2020/day_6"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
