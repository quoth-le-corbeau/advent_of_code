import time
import pathlib
import re
from collections import defaultdict


def sum_ordered_middles(file_path: str) -> int:
    rules, updates = _parse_input(file=file_path)
    order_map = _get_order_map(rules=rules)
    ordered_middles = 0
    ordered = [
        update
        for update in updates
        if not _is_unordered(order_map=order_map, update=update)
    ]
    for update in ordered:
        ordered_middles += update[len(update) // 2]
    return ordered_middles


def _is_unordered(order_map: dict[int, set[int]], update: list[int]) -> bool:
    unordered = []
    ordered = []
    in_order = False
    for i, n in enumerate(update):
        if all(rest in order_map[n] for rest in update[i + 1 :]):
            in_order = True
        else:
            in_order = False
            break
    if in_order:
        ordered.append(update)
    else:
        unordered.append(update)
    return len(unordered) > 0


def _get_order_map(rules) -> dict[int, set[int]]:
    order_map = defaultdict(set)
    all_nums = []
    for rule in rules:
        x, y = rule
        all_nums.append(x)
        all_nums.append(y)
    for rule in rules:
        x, y = rule
        for other_rule in rules:
            if other_rule[0] == x:
                order_map[x].add(other_rule[1])
    for num in all_nums:
        if num not in order_map:
            order_map[num] = set()
    return dict(order_map)


def _parse_input(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read()
        rules, updates = lines.split("\n\n")
        rules = [
            (int(rule.split("|")[0]), int(rule.split("|")[1]))
            for rule in rules.split("\n")
        ]
        updates = [
            list(map(int, re.findall(r"(\d+)", line))) for line in updates.split("\n")
        ]
        updates = [update for update in updates if len(update) > 0]
        return rules, updates


timer_start = time.perf_counter()
print(
    sum_ordered_middles(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_5"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    sum_ordered_middles(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_5"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
