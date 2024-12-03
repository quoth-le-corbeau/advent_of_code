import time
import pathlib
import re


def scan_enabled_corrupted_memory(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read()
        mul_pattern = r"mul\((-?\d+),\s*(-?\d+)\)"
        substring_start_index = 0
        i = 0
        matches = []
        do_flag = True
        while i < len(lines):
            substring = lines[substring_start_index:i]
            match = re.findall(mul_pattern, substring)
            if len(match) > 0:
                do = "do()" in substring
                do_not = "don't()" in substring
                if do and not do_not:
                    do_flag = True
                elif do and do_not:
                    do_i = substring.index("do()")
                    do_not_i = substring.index("don't()")
                    if do_i > do_not_i:
                        do_flag = True
                    else:
                        do_flag = False
                if do_flag:
                    if not do and not do_not:
                        matches += match
                    if do:
                        if not do_not:
                            matches += match
                            do_flag = True
                    if do_not and not do:
                        do_flag = False
                substring_start_index = i
            i += 1
        total = 0
        for match in matches:
            total += int(match[0]) * int(match[1])
        return total


start = time.perf_counter()
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
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
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
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
