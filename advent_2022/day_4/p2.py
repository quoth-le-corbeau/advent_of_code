import time
import pathlib
import re


def find_overlapping_ranges(file: str) -> int:
    range_pairs = _get_range_pairs(file=file_path)
    overlap_count = 0
    for pair in range_pairs:
        range_1_start, range_1_end = pair[0][0], pair[0][1]
        range_2_start, range_2_end = pair[1][0], pair[1][1]
        if (
            (range_2_start <= range_1_start <= range_2_end)
            or (range_2_start <= range_1_end <= range_2_end)
            or (range_1_start <= range_2_start <= range_1_end)
            or (range_1_start <= range_2_end <= range_1_end)
        ):
            overlap_count += 1
    return overlap_count


def _get_range_pairs(file: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        range_pairs: list[tuple[tuple[int, int], tuple[int, int]]] = list()
        for line in lines:
            range_1, range_2 = (
                re.findall(r"\d+", line.split(",")[0]),
                re.findall(r"\d+", line.split(",")[1]),
            )
            range_1_pair = int(range_1[0]), int(range_1[1])
            range_2_pair = int(range_2[0]), int(range_2[1])
            range_pairs.append((range_1_pair, range_2_pair))
        return range_pairs


start = time.perf_counter()
print(find_overlapping_ranges("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(find_overlapping_ranges("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
