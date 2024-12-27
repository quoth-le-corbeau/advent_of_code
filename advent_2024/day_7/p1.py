import time
import pathlib
import re
from itertools import product


def sum_completable_equations(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        reachable_totals = 0
        for line in lines:
            target = int(line.split(":")[0])
            nums = list(map(int, re.findall(r"\d+", line.split(":")[1])))
            check_product_sum = nums[0]
            for num in nums[1:]:
                check_product_sum *= num
            if check_product_sum < target or sum(nums) > target:
                continue
            number_of_spaces = len(nums) - 1
            possible_operation_orders = [
                "".join(combination)
                for combination in product("*+", repeat=number_of_spaces)
            ]
            for possible_operation_order in possible_operation_orders:
                if (
                    _evaluate_left_to_right(
                        operation_order=possible_operation_order, values=nums
                    )
                    == target
                ):
                    reachable_totals += target
                    break
        return reachable_totals


def _evaluate_left_to_right(operation_order: str, values: list[int]):
    assert len(operation_order) == len(values) - 1
    expression = "".join(
        f"{values[i]} {op} " for i, op in enumerate(operation_order)
    ) + str(values[-1])
    nums_and_symbols = expression.split()
    result = int(nums_and_symbols[0])
    for i in range(1, len(nums_and_symbols), 2):
        operator = nums_and_symbols[i]
        operand = int(nums_and_symbols[i + 1])
        if operator == "+":
            result += operand
        elif operator == "*":
            result *= operand
        else:
            raise ValueError(f"Unsupported operator: {operator}")
    return result


timer_start = time.perf_counter()
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
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
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
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
