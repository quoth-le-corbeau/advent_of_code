import time
import pathlib
import re


def count_safe_reports_with_dampener(file_path: str):
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        safe_count = 0
        for line in lines:
            nums = list(map(int, re.findall(r"(\d+)", line)))
            if len(nums) < 2:
                continue
            diffs = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
            is_increasing = all(diff > 0 for diff in diffs)
            is_decreasing = all(diff < 0 for diff in diffs)
            anomalies = 0
            for diff in diffs:
                if (
                    abs(diff) < 1
                    or abs(diff) > 3
                    or (diff > 0 and not is_increasing)
                    or (diff < 0 and not is_decreasing)
                ):
                    anomalies += 1
            if anomalies == 0 or anomalies == 1:
                safe_count += 1
        return safe_count


start = time.perf_counter()
print(count_safe_reports_with_dampener("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(count_safe_reports_with_dampener("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
