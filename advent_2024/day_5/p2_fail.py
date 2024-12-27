import time
import pathlib
import re
from collections import defaultdict


def reorder_and_sum_middle_pages(file_path: str) -> int:
    rules, updates = _parse_input(file=file_path)
    order_map = _get_order_map(rules=rules)
    reordered_middles = 0
    updates = [update for update in updates if len(update)]
    ordered, unordered = _divide_updates(order_map=order_map, updates=updates)
    reordered = []
    for update in unordered:
        # re_ordered.append(_reorder(to_sort=update, rules=rules))
        reordered.append(_reorder2(to_sort=update, order_map=order_map))
    print(f"{reordered=}")
    for update in reordered:
        reordered_middles += update[len(update) // 2]
    return reordered_middles


def _reorder2(to_sort: list[int], order_map: dict[int, set[int]]) -> list[int]:
    to_sort_copy = to_sort.copy()
    for key, afters in order_map.items():
        for after in afters:
            if after in to_sort_copy and key in to_sort_copy:
                a_idx = to_sort_copy.index(after)
                k_idx = to_sort_copy.index(key)
                if k_idx > a_idx:
                    to_sort_copy[a_idx], to_sort_copy[k_idx] = (
                        to_sort_copy[k_idx],
                        to_sort_copy[a_idx],
                    )
        if key in to_sort and len(afters) == 0:
            print("got here")
            to_sort_copy.remove(key)
            to_sort_copy.append(key)

    return to_sort_copy


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


def _divide_updates(
    order_map: dict[int, set[int]],
    updates: list[list[int]],
) -> tuple[list[list[int]], list[list[int]]]:
    unordered = []
    ordered = []
    in_order = False
    for update in updates:
        if len(update) == 0:
            continue
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
    return ordered, unordered


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
        return rules, updates


timer_start = time.perf_counter()
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
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
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
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
