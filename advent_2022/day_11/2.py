import time
import pathlib
import re
from typing import Union


def calculate_monkey_business_over_10000_rounds(file: str) -> int:
    monkeys, divisors = _get_attributes_per_monkey_and_divisors(file=file)
    divisors_lcm = _lcm(integers=divisors)
    i = 0
    while i < 10000:
        monkeys = _monkey_round(monkeys=monkeys, divisors_lcm=divisors_lcm)
        i += 1
    inspections = list()
    for monkey in monkeys:
        inspections.append(monkey["inspection_count"])
    inspections_asc = sorted(inspections)
    return inspections_asc[-1] * inspections_asc[-2]


def _lcm(integers: list[int]) -> int:
    lcm = 1
    for integer in integers:
        lcm = int(_lcm_two(lcm, integer))
    return lcm


def _lcm_two(a: int, b: int) -> int:
    return int(a * b / _gcd_two(a, b))


def _gcd_two(a: int, b: int) -> int:
    if a == 0:
        return b
    return _gcd_two(b % a, a)


def _monkey_round(
    monkeys: list[dict[str, Union[list[int], str, int, tuple[int, int]]]],
    divisors_lcm: int,
) -> list[dict[str, Union[list[int], str, int, tuple[int, int]]]]:
    for monkey in monkeys:
        operation_type = monkey["operation"].split()[1]
        operand = monkey["operation"].split()[-1]
        divisor = monkey["divisor"]
        targets = monkey["targets"]
        for item in monkey["items"]:
            worry_level = (
                _perform_operation(
                    item=item, operand=operand, operation_type=operation_type
                )
                % divisors_lcm
            )
            if worry_level % divisor == 0:
                monkeys[targets[0]]["items"].append(worry_level)
            else:
                monkeys[targets[1]]["items"].append(worry_level)
            monkey["inspection_count"] += 1
        monkey["items"] = []
    return monkeys


def _perform_operation(item: int, operand: str, operation_type: str) -> int:
    worry_level = item
    if operation_type == "*":
        if operand != "old":
            worry_level *= int(operand)
        else:
            worry_level *= worry_level
    else:
        if operand != "old":
            worry_level += int(operand)
        else:
            worry_level += worry_level
    return worry_level


def _get_attributes_per_monkey_and_divisors(
    file: str,
) -> tuple[list[dict[str, Union[list[int], str, int, tuple[int, int]]]], list[int]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        blocks = puzzle_input.read().split("\n\n")
        attributes_per_monkey = list()
        divisors: list[int] = list()
        for i, block in enumerate(blocks):
            attributes = {"inspection_count": 0}
            monkey = block.split("\n")
            attributes["monkey"] = i
            attributes["items"] = list(map(int, re.findall(r"\d+", monkey[1])))
            attributes["operation"] = monkey[2].split("=")[-1].strip()
            divisor = int(monkey[3].split()[-1])
            attributes["divisor"] = divisor
            divisors.append(divisor)
            attributes["targets"] = int(monkey[4].split()[-1]), int(
                monkey[5].split()[-1]
            )
            attributes_per_monkey.append(attributes)
        return sorted(attributes_per_monkey, key=lambda d: d["monkey"]), divisors


start = time.perf_counter()
print(calculate_monkey_business_over_10000_rounds("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(calculate_monkey_business_over_10000_rounds("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
