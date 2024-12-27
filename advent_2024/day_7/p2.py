import time
import pathlib
import re
import itertools


def sum_completable_concatenatable_equations(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        reachable_totals = 0
        for line in lines:
            target = int(line.split(":")[0])
            nums = list(map(int, re.findall(r"\d+", line.split(":")[1])))
            # Note to self: prune impossible nums!
            check_product_sum = nums[0]
            for num in nums[1:]:
                check_product_sum *= num
            if check_product_sum < target or sum(nums) > target:
                continue
            spaces = len(nums) - 1
            possible_ops = [
                "".join(combination)
                for combination in itertools.product("+*|", repeat=spaces)
            ]
            for possible_op in possible_ops:
                if _evaluate_left_to_right(op=possible_op, nums=nums) == target:
                    reachable_totals += target
                    break
        return reachable_totals


def _evaluate_left_to_right(op: str, nums: list) -> int:
    expression = ""
    for idx, symbol in enumerate(op):
        expression += "".join(f"{nums[idx]} {symbol} ")
    expression += str(nums[-1])
    equation = expression.split()
    result = int(equation[0])
    for idx in range(1, len(equation), 2):
        operator = equation[idx]
        operand = int(equation[idx + 1])
        if operator == "+":
            result += operand
        elif operator == "*":
            result *= operand
        elif operator == "|":
            result = int(str(result) + str(operand))
        else:
            raise Exception(f"Unknown operator: {operator}")
    return result


timer_start = time.perf_counter()
print(
    sum_completable_concatenatable_equations(
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
    sum_completable_concatenatable_equations(
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
