import time
import pathlib
import re


def scan_enabled_corrupted_memory(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read()
        do_pattern = r"do\(\)"
        do_not_pattern = r"don't\(\)"
        mul_pattern = r"mul\((-?\d+),\s*(-?\d+)\)"
        do_matches = re.finditer(do_pattern, lines)
        do_not_matches = re.finditer(do_not_pattern, lines)
        mul_matches = re.finditer(mul_pattern, lines)
        do_groups = [
            (match.group(), match.start(), match.end()) for match in do_matches
        ]
        do_not_groups = [
            (match.group(), match.start(), match.end()) for match in do_not_matches
        ]
        mul_groups = [
            (match.group(), match.start(), match.end()) for match in mul_matches
        ]
        do_starts = [int(group[1]) for group in do_groups]
        do_not_starts = [int(group[1]) for group in do_not_groups]
        mul_starts = [int(group[1]) for group in mul_groups]
        do = True
        final_muls = []
        for i, char in enumerate(lines):
            if i in do_not_starts:
                do = False
            elif i in do_starts:
                do = True
            if do:
                if i in mul_starts:
                    for group in mul_groups:
                        if i in group:
                            final_muls.append(group[0])

        nums = list(map(int, re.findall(r"\d+", "".join(final_muls))))
        # print(f"{list(zip(nums[::2], nums[1::2]))=}")
        total = 0
        for pair in list(zip(nums[::2], nums[1::2])):
            total += pair[0] * pair[1]
        return total
        # return sum([x * y for x, y in list(zip(nums[::2], nums[1::2]))])


START = time.perf_counter()
print(
    scan_enabled_corrupted_memory(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_3"
                / "eg2.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - START:2.4f} seconds.")

START = time.perf_counter()
print(
    scan_enabled_corrupted_memory(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_3"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - START:2.4f} seconds.")
