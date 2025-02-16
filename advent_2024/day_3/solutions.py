from pathlib import Path
import re
from dataclasses import dataclass

from reusables import timer, INPUT_PATH


@dataclass(frozen=True)
class Interval:
    start_idx: int
    end_idx: int
    do: bool


class Computer:
    def __init__(self, file: str):
        self.mul_pattern = r"mul\(\d+\,\d+\)"
        with open(
            file=Path(__file__).resolve().parents[2] / file, mode="r"
        ) as puzzle_input:
            self.program = puzzle_input.read().strip()
        self._set_do_do_not_intervals()

    def _set_do_do_not_intervals(self):
        do_pattern = r"do\(\)"
        do_not_pattern = r"don\'t\(\)"
        do_end_indexes = [
            match.end(0)
            for match in re.finditer(pattern=do_pattern, string=self.program)
        ]
        do_not_end_indexes = [
            match.end(0)
            for match in re.finditer(pattern=do_not_pattern, string=self.program)
        ]
        relevant_do_end_indexes = []
        for do_end_idx in do_end_indexes:
            if do_end_idx < do_not_end_indexes[0]:
                continue
            else:
                relevant_do_end_indexes.append(do_end_idx)
        i = 0
        start_idx = 0
        self.intervals = []
        do = True
        while i < len(self.program):
            if i in do_not_end_indexes:
                self.intervals.append(Interval(start_idx=start_idx, end_idx=i, do=do))
                start_idx = i + 1
                do = False
            elif i in relevant_do_end_indexes:
                self.intervals.append(Interval(start_idx=start_idx, end_idx=i, do=do))
                start_idx = i + 1
                do = True
            i += 1
        self.intervals.append(Interval(start_idx=start_idx, end_idx=i, do=do))

    @staticmethod
    def _mul(x: int, y: int) -> int:
        return x * y

    @property
    def _filtered_multipliers(self) -> list[str]:
        multiplier_indexes = [
            (match.start(0), match.end(0))
            for match in re.finditer(pattern=self.mul_pattern, string=self.program)
        ]
        real_do_multipliers = []
        for multiplier_index in multiplier_indexes:
            for interval in self.intervals:
                if (
                    interval.start_idx <= multiplier_index[0]
                    and multiplier_index[1] < interval.end_idx
                    and interval.do
                ):
                    real_do_multipliers.append(
                        self.program[multiplier_index[0] : multiplier_index[1]]
                    )
        return real_do_multipliers

    def sum_multiplier_results(self, filter_by_do: bool = False) -> int:
        multipliers = (
            self._filtered_multipliers
            if filter_by_do
            else re.findall(pattern=self.mul_pattern, string=self.program)
        )
        mul = self._mul
        total = 0
        for real_multiplier in multipliers:
            total += eval(real_multiplier)
        return total


def _initialise_puzzle(file: str, year: int = 2024, day: int = 3) -> Computer:
    return Computer(file=INPUT_PATH.format(file=file, year=year, day=day))


@timer
def part_one(file: str) -> int:
    computer = _initialise_puzzle(file=file)
    return computer.sum_multiplier_results()


# part_one("eg")
part_one("input")


@timer
def part_two(file: str) -> int:
    computer = _initialise_puzzle(file=file)
    return computer.sum_multiplier_results(filter_by_do=True)


# part_two("eg2")
part_two("input")
