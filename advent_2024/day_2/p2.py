import time
import pathlib
import re


def count_safe_reports_with_dampener(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        safe_count = 0
        for line in lines:
            nums = list(map(int, re.findall(r"(\d+)", line)))
            if len(nums) < 2:
                continue
            if _is_safe(nums):
                safe_count += 1
            else:
                for i in range(len(nums)):
                    sub_list = nums[:i] + nums[i + 1 :]
                    if _is_safe(sub_list):
                        safe_count += 1
                        break
        return safe_count


def _is_safe(nums: list[int]) -> bool:
    diffs = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
    if all(1 <= abs(diff) <= 3 for diff in diffs):
        if all(diff > 0 for diff in diffs):
            return True
        elif all(diff < 0 for diff in diffs):
            return True
        else:
            return False
    return False


start = time.perf_counter()
print(
    count_safe_reports_with_dampener(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_2"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    count_safe_reports_with_dampener(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_2"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
