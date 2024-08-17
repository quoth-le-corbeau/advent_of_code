from typing import Tuple, List
from functools import reduce
import time
import pathlib
import re

_TARGET_SUM = 2020


def product_of_target_pair(file_path: str) -> int:
    pair = _get_target_pair(file=file_path)
    multiply = lambda x, y: x * y
    return reduce(multiply, pair)


def _get_target_pair(file: str) -> Tuple[int, int]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read()
        all_entries = list(map(int, re.findall(r"\d+", lines)))
        return _get_pair_with_target_sum(entries=all_entries)


def _get_pair_with_target_sum(
    entries: List[int], target_sum: int = _TARGET_SUM
) -> Tuple[int, int]:
    visited = list()
    for entry in entries:
        delta = target_sum - entry
        if delta in visited:
            return (entry, delta)
        else:
            visited.append(entry)
    raise RuntimeError("No target pair found in input!")


start = time.perf_counter()
print(product_of_target_pair("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(product_of_target_pair("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
