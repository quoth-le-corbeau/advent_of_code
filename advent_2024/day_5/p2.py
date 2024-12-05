import time
import pathlib
import re
from collections import defaultdict


def reorder_and_sum_middle_pages(file_path: str) -> int:
    rules, updates = _parse_input(file=file_path)
    order_map = _get_order_map(rules=rules)
    unordered = []
    for update in updates:
        if _is_unordered(order_map=order_map, update=update):
            unordered.append(update)
    for update in unordered:
        while _is_unordered(order_map=order_map, update=update):
            update = _reorder(rules=rules, to_sort=update)
    middle_sum = 0
    for update in unordered:
        middle_sum += update[len(update) // 2]
    return middle_sum


def _reorder(
    to_sort: list[int],
    rules: list[tuple[int, int]],
) -> list[int]:
    for rule in rules:
        x, y = rule
        if x in to_sort and y in to_sort:
            x_index = to_sort.index(x)
            y_index = to_sort.index(y)
            if x_index > y_index:
                to_sort[x_index], to_sort[y_index] = to_sort[y_index], to_sort[x_index]
    return to_sort


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
        order_map[x].add(y)
    for num in all_nums:
        if num not in order_map:
            order_map[num] = set()
    return dict(order_map)


def _parse_input(file: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
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


start = time.perf_counter()
print(
    reorder_and_sum_middle_pages(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_5"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    reorder_and_sum_middle_pages(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_5"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
