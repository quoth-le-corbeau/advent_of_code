import time
import pathlib
import re


def scan_enabled_corrupted_memory(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read()
        mul_pattern = r"mul\((-?\d+),\s*(-?\d+)\)"


        substring_start_index = 0
        i = 0
        while i < len(substring):
            substring = lines[substring_start_index:i]
            if len(re.findall(mul_pattern, substring)) >0:
                substring_end = i
                print(f"{lines[substring_start_index: substring_end]=}")
                substring_start_index = i
            i += 1






start = time.perf_counter()
print(scan_enabled_corrupted_memory("eg2.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(scan_enabled_corrupted_memory("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
