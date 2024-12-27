import time
import pathlib

"""
Linen Layout - Part I

use backtracking and memoization

"""


def _can_be_formed(string: str, substrings: list[str], memo=None):
    if memo is None:
        memo = {}
    if len(string) == 0:
        return True
    if string in memo:
        return memo[string]
    for substring in substrings:
        if string.startswith(substring):
            remainder = string[len(substring) :]
            if _can_be_formed(string=remainder, substrings=substrings, memo=memo):
                memo[string] = True
                return True
    memo[string] = False
    return False


def count_possible_designs(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().split("\n\n")
        available_patterns = lines[0].strip().replace(" ", "").split(",")
        designs = lines[1].strip().split("\n")
        result = {
            design: _can_be_formed(design, available_patterns) for design in designs
        }
        possible = [k for k in result if result[k]]
        return len(possible)


timer_start = time.perf_counter()
print(
    count_possible_designs(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_19"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    count_possible_designs(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_19"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
