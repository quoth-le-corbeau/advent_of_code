from typing import List, Set
import time
import pathlib


def sum_of_yes_counts(file_path: str) -> int:
    grouped_yesses = _count_yesses(file=file_path)
    count = 0
    for group in grouped_yesses:
        count += len(group)
    return count


def _count_yesses(file: str) -> List[Set[str]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        people = puzzle_input.read().split("\n\n")
        yesses = list()
        for person in people:
            yesses.append(set("".join(person.split())))
        return yesses


start = time.perf_counter()
print(sum_of_yes_counts("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(sum_of_yes_counts("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
