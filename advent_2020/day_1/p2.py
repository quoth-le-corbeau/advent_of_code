from typing import Tuple, List
from functools import reduce
import time
import pathlib
import re
import os
import sys

import day_1.p1

_TARGET_SUM = 2020


def product_of_target_triple(file_path: str) -> int:
    triple = _get_target_triple(file=file_path)
    return triple[0] * triple[1] * triple[2]


def _get_target_triple(file: str) -> Tuple[int, int, int]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read()
        all_entries = list(map(int, re.findall(r"\d+", lines)))
        return _get_triple_with_target_sum(all_entries=all_entries)


def _get_triple_with_target_sum(all_entries: List[int]) -> Tuple[int, int, int]:
    for i, entry in enumerate(all_entries):
        try:
            coupled_pair = day_1.p1._get_pair_with_target_sum(
                entries=all_entries[i + 1 :], target_sum=_TARGET_SUM - entry
            )
            return entry, coupled_pair[0], coupled_pair[1]
        except RuntimeError:
            continue
    raise RuntimeError("No matching Triple found")


start = time.perf_counter()
print(product_of_target_triple("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(product_of_target_triple("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
