import time
import pathlib
import re


def count_safe_reports_fail(file_path: str):
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        safe_count: int = 0
        for line in lines:
            nums = list(map(int, re.findall(r"(\d+)", line)))
            paired = zip(nums[:-1], nums[1:])
            if all(num2 - num1 <= 3 and num2 > num1 for num1, num2 in paired):
                safe_count += 1
            elif all(num1 - num2 <= 3 and num2 < num1 for num1, num2 in paired):
                safe_count += 1
            else:
                continue
        return safe_count


def count_safe_reports_fail_fixed(file_path: str):
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        safe_count: int = 0
        for line in lines:
            nums = list(map(int, re.findall(r"(\d+)", line)))
            paired = list(zip(nums[:-1], nums[1:]))
            if all(num2 - num1 <= 3 and num2 > num1 for num1, num2 in paired):
                safe_count += 1
            elif all(num1 - num2 <= 3 and num2 < num1 for num1, num2 in paired):
                safe_count += 1
            else:
                continue
        return safe_count


def count_safe_reports_alternative_equivalent(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        safe_count = 0
        for line in lines:
            nums = list(map(int, re.findall(r"(\d+)", line)))
            if len(nums) < 2:
                continue
            if _is_safe(nums):
                safe_count += 1
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
    count_safe_reports_fail_fixed(
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
    count_safe_reports_fail_fixed(
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
