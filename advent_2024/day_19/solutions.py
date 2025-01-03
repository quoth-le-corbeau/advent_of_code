from collections import deque, defaultdict
from pathlib import Path

from reusables import timer, INPUT_PATH


class Onsen:
    def __init__(self, file: str):
        with open(
            file=Path(__file__).resolve().parents[2] / file, mode="r"
        ) as puzzle_input:
            designs, towel_lines = puzzle_input.read().strip().split("\n\n")
            self.designs = designs.split(", ")
            self.towels = towel_lines.splitlines()
            self.ways_by_towel = {towel: 0 for towel in self.possible_towels}

    @property
    def possible_towels(self):
        possible = []
        for towel in self.towels:
            if self._is_possible(towel=towel):
                possible.append(towel)
        return possible

    def sum_possible_ways(self) -> int:
        total = 0
        for towel in self.possible_towels:
                total += self._possible_ways(towel=towel)
        return total

    def _possible_ways(self, towel: str, memo=None) -> int:
        if memo is None:
            memo = {}
        if len(towel) == 0:
            return 1
        if towel in memo:
            return memo[towel]
        memo[towel] = 0
        heads = [design for design in self.designs if towel.startswith(design)]
        for head in heads:
             memo[towel] += self._possible_ways(towel=towel[len(head):], memo=memo)


    def _is_possible(self, towel: str, memo=None) -> bool:
        if memo is None:
            memo = {}
        if len(towel) == 0:
            return True
        if towel in memo:
            return memo[towel]
        for design in self.designs:
            if towel.startswith(design):
                if self._is_possible(towel=towel[len(design) :], memo=memo):
                    memo[towel] = True
                    return True
        memo[towel] = False
        return False


def _make_path(file: str, year=2024, day=19) -> str:
    return INPUT_PATH.format(year=year, day=day, file=file)


@timer
def part_one(file: str):
    input_file = _make_path(file=file)
    onsen = Onsen(file=input_file)
    print(f"day 19 p1 with {file}:")
    print(len(onsen.possible_towels))


# part_one(file="eg")
# part_one(file="input")


@timer
def part_two(file: str):
    print(f"day 19 p2 with {file}:")
    input_file = _make_path(file=file)
    onsen = Onsen(file=input_file)
    print(onsen.sum_possible_ways())


part_two(file="eg")
