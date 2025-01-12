from collections import defaultdict
from pathlib import Path

from reusables import timer, INPUT_PATH


class SafteyManual:
    def __init__(self, file: str):
        with open(
            file=Path(__file__).resolve().parents[2] / file, mode="r"
        ) as puzzle_input:

            rules_lines, update_lines = puzzle_input.read().strip().split("\n\n")
            rules = [
                (int(line.split("|")[0]), int(line.split("|")[1]))
                for line in rules_lines.splitlines()
            ]
            self.updates = [
                list(map(int, line.split(","))) for line in update_lines.splitlines()
            ]
            self.rules_by_page = defaultdict(list)
            for rule in rules:
                before, after = rule
                self.rules_by_page[before].append(after)

    @property
    def ordered_updates(self) -> list[tuple[list[int], bool]]:
        ordered_updates = []
        for update in self.updates:
            switch_count = 0
            for i, value in enumerate(update):
                for j, other in enumerate(update[:i] + update[i + 1 :]):
                    if other in self.rules_by_page[value] and j < i:
                        update[i], update[j] = update[j], update[i]
                        switch_count += 1
            if switch_count > 1:
                already_ordered = False
            else:
                already_ordered = True
            ordered_updates.append((update, already_ordered))
        return ordered_updates

    def sum_middles(self) -> tuple[int, int]:
        already_ordered_middles_total = 0
        unordered_middles_total = 0
        for update, already_ordered in self.ordered_updates:
            if already_ordered:
                already_ordered_middles_total += update[len(update) // 2]
            else:
                assert already_ordered is False
                unordered_middles_total += update[len(update) // 2]
        return already_ordered_middles_total, unordered_middles_total


def _initialise_puzzle(file: str) -> SafteyManual:
    return SafteyManual(file=INPUT_PATH.format(file=file, year=2024, day=5))


@timer
def part_one(file: str) -> None:
    safety_manual = _initialise_puzzle(file=file)
    result, _ = safety_manual.sum_middles()
    print(f"part 1: {result} <- ({file})")


# part_one("eg")
part_one("input")


@timer
def part_two(file: str) -> None:
    safety_manual = _initialise_puzzle(file=file)
    _, result = safety_manual.sum_middles()
    print(f"part 2: {result} <- ({file})")


# part_two("eg")
part_two("input")
