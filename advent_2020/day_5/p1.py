from typing import List, Tuple
import time
import pathlib


def get_highest_seat_id(file_path: str) -> int:
    boarding_passes = _get_boarding_passes(file=file_path)
    seat_ids: List[int] = list()
    for boarding_pass in boarding_passes:
        row_number = _do_specificied_binary_search(
            binary_code=boarding_pass[0],
            starting_range_size=128,
            starting_binary_index=6,
            take_lower_signifier="F",
            take_upper_signifier="B",
        )
        column_number = _do_specificied_binary_search(
            binary_code=boarding_pass[1],
            starting_range_size=8,
            starting_binary_index=2,
            take_lower_signifier="L",
            take_upper_signifier="R",
        )
        seat_ids.append(row_number * 8 + column_number)
    return max(seat_ids)


def _do_specificied_binary_search(
    binary_code: str,
    starting_range_size: int,
    starting_binary_index: int,
    take_upper_signifier: str,
    take_lower_signifier: str,
) -> int:
    lower_bound = 0
    upper_bound = lower_bound + starting_range_size - 1
    i = 0
    char = "x"
    while len(range(lower_bound, upper_bound)) >= 2:
        range_size = 2 ** (starting_binary_index - i)
        char = binary_code[i]
        if char == take_upper_signifier:
            lower_bound = lower_bound + range_size
        elif char == take_lower_signifier:
            upper_bound = lower_bound + range_size - 1
        i += 1
    char = binary_code[i]
    if char == take_upper_signifier:
        return upper_bound
    elif char == take_lower_signifier:
        return lower_bound
    else:
        raise RuntimeError("Incorrect take_upper or take_lower identifier!")


def _get_boarding_passes(file: str) -> List[Tuple[str, str]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        boarding_passes: List[Tuple[str, str]] = list()
        for line in lines:
            boarding_passes.append((line[:-3], line[-3:]))
        return boarding_passes


start = time.perf_counter()
print(get_highest_seat_id("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(get_highest_seat_id("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
