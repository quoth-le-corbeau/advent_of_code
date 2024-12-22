import pathlib
import time
import re
import itertools


def sum_completable_equations(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        # total_reachable = set()
        total = 0
        for line in lines:
            target = int(line.split(":")[0])
            nums = list(map(int, re.findall(r"\d+", line.split(":")[1])))
            check_product_sum = nums[0]
            for num in nums[1:]:
                check_product_sum *= num
            if check_product_sum < target or sum(nums) > target:
                continue
            spaces = len(nums) - 1
            possible_ops_orders = [
                "".join(combo) for combo in itertools.product("+*", repeat=spaces)
            ]
            for possible_ops_order in possible_ops_orders:
                if _evaluate_left_to_right(op=possible_ops_order, nums=nums) == target:
                    # total_reachable.add(target)
                    total += target
                    break
        # print(f"FAIL: {total_reachable}")
        # print(sum(total_reachable))
        return total


def _evaluate_left_to_right(op: str, nums: list) -> bool:
    expression = ""
    for idx, symbol in enumerate(op):
        expression += "".join(f"{nums[idx]} {symbol} ")
    expression += str(nums[-1])
    parts = expression.split()
    result = int(parts[0])
    for idx in range(1, len(parts), 2):
        operator = parts[idx]
        operand = int(parts[idx + 1])
        if operator == "+":
            result += int(operand)
        elif operator == "*":
            result *= int(operand)
        else:
            raise ValueError(f"Invalid operator: {operator}")
    return result


START = time.perf_counter()
print(
    sum_completable_equations(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_7"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - START:2.4f} seconds.")

START = time.perf_counter()
print(
    sum_completable_equations(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_7"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - START:2.4f} seconds.")
