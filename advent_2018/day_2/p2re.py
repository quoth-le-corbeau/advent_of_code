import time
import pathlib
from typing import Optional
import re


def get_common_box_id_letters(file_path: str) -> str:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        box_ids = puzzle_input.read().splitlines()
        for i, box_id in enumerate(box_ids):
            for b_id in box_ids[i + 1 :]:
                if single_difference(box_id, b_id) is not None:
                    print(single_difference(box_id, b_id))
                    return box_id.replace(single_difference(box_id, b_id), "")
        return "EPIC FAIL"


def single_difference(s1: str, s2: str) -> Optional[str]:
    if len(s1) != len(s2):
        raise ValueError("s1 and s2 do not have the same length")
    for i in range(len(s1)):
        pattern = re.escape(s1[:i]) + "." + re.escape(s1[i + 1 :])
        match = re.fullmatch(pattern, s2)
        if match is not None:
            return s1[i]
    return None


start = time.perf_counter()
print(get_common_box_id_letters("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(get_common_box_id_letters("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
