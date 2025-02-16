import itertools
from pathlib import Path
from reusables import timer, INPUT_PATH


def _initialize_puzzle(filename: str) -> list[tuple[int, list[int]]]:
    input_path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        file=filename, year=2024, day=7
    )
    with open(file=input_path, mode="r") as puzzle_input:
        calibration_lines = puzzle_input.read().strip().splitlines()
        results_by_callibrations = [
            (int(line.split(": ")[0]), list(map(int, line.split(": ")[1].split(" "))))
            for line in calibration_lines
        ]
        return results_by_callibrations


def _is_possible_equation(result: int, operands: list[int], operators: str) -> bool:
    operation_spaces = len(operands) - 1
    operation_orders = [
        "".join(operator_symbol)
        for operator_symbol in itertools.product(operators, repeat=operation_spaces)
    ]
    if any(
        result == _evaluate_left_to_right(operands=operands, operators=order)
        for order in operation_orders
    ):
        return True
    return False


def _evaluate_left_to_right(operands: list[int], operators: str) -> int:
    result = operands[0]
    for i, operation in enumerate(operators):
        if operation == "+":
            result += operands[i + 1]
        elif operation == "*":
            result *= operands[i + 1]
        elif operation == "|":
            result = int(str(result) + str(operands[i + 1]))
        else:
            raise ValueError(f"Unknown operator {operation}")
    return result


def find_possible_equations(
    calibrations: list[tuple[int, list[int]]], operators: str
) -> list[int]:
    results = []
    for result, operands in calibrations:
        if _is_possible_equation(result=result, operands=operands, operators=operators):
            results.append(result)
    return results


@timer
def part_one(filename: str, operators: str) -> list[int]:
    calibrations = _initialize_puzzle(filename=filename)
    possible_results = find_possible_equations(
        calibrations=calibrations, operators=operators
    )
    return possible_results


# part_one(filename="eg", operators="+*")
part_one(filename="input", operators="+*")


@timer
def part_two(filename: str, operators: str) -> int:
    calibrations = _initialize_puzzle(filename=filename)
    possible_results = find_possible_equations(
        calibrations=calibrations, operators=operators
    )
    return sum(possible_results)


# part_two(filename="eg", operators="+*|")
part_two(filename="input", operators="+*|")
