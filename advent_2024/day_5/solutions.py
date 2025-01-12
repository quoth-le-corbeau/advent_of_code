from pathlib import Path
from collections import defaultdict

from reusables import timer, INPUT_PATH


def _parse_puzzle_input(filename: str) -> tuple[list[list[int]], dict[int, list[int]]]:
    input_path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        file=filename, year=2024, day=5
    )
    with open(file=input_path, mode="r", encoding="utf-8") as puzzle_input:
        rules_lines, update_lines = puzzle_input.read().strip().split("\n\n")
        rules = [
            (int(line.split("|")[0]), int(line.split("|")[1]))
            for line in rules_lines.splitlines()
        ]
        updates = [
            list(map(int, line.split(","))) for line in update_lines.splitlines()
        ]
        rules_by_page = defaultdict(list)
        for rule in rules:
            before, after = rule
            rules_by_page[before].append(after)
    return updates, rules_by_page


def _get_ordered_and_unordered_updates(
    updates: list[list[int]], rules_by_page: dict[int, list[int]]
) -> tuple[list[list[int]], list[list[int]], list[list[int]]]:
    ordered_updates = []
    unordered_updates = []
    re_ordered_updates = []
    for update in updates:
        original_update = update.copy()
        switch_count = 0
        for i, value in enumerate(update):
            for j, other in enumerate(update[:i] + update[i + 1 :]):
                if other in rules_by_page[value] and j < i:
                    update[i], update[j] = update[j], update[i]
                    switch_count += 1
        if switch_count != 0:
            unordered_updates.append(original_update)
            re_ordered_updates.append(update)
        else:
            assert switch_count == 0
            assert update == original_update
            ordered_updates.append(update)
    return ordered_updates, unordered_updates, re_ordered_updates


def sum_middle_values(updates: list[list[int]]) -> int:
    total = 0
    for update in updates:
        total += update[len(update) // 2]
    return total


@timer
def part_one(filename: str) -> None:
    updates, rules_by_page = _parse_puzzle_input(filename=filename)
    ordered, unordered, re_ordered_updates = _get_ordered_and_unordered_updates(
        updates=updates, rules_by_page=rules_by_page
    )
    print(f"Part one: {sum_middle_values(updates=ordered)} <- ({filename})")


# part_one(filename="eg")
part_one(filename="input")


@timer
def part_two(filename: str) -> None:
    updates, rules_by_page = _parse_puzzle_input(filename=filename)
    ordered, unordered, re_ordered_updates = _get_ordered_and_unordered_updates(
        updates=updates, rules_by_page=rules_by_page
    )
    print(f"Part two: {sum_middle_values(updates=re_ordered_updates)} <- ({filename})")


# part_two(filename="eg")
part_two(filename="input")
