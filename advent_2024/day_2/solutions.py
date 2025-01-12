from pathlib import Path

from reusables import INPUT_PATH, timer


class RedNoseReport:
    def __init__(self, file: str):
        with open(
            file=Path(__file__).resolve().parents[2] / file, mode="r"
        ) as puzzle_input:
            self.reports = [
                [int(n) for n in line.split()]
                for line in puzzle_input.read().strip().splitlines()
            ]
            # print(f"{self.reports=}")

    @property
    def safe_count(self) -> int:
        counter = 0
        for report in self.reports:
            if self._is_safe(report):
                counter += 1
        return counter

    @staticmethod
    def _is_safe(report: list[int]) -> bool:
        diffs = [abs(x - y) for x, y in zip(report[:-1], report[1:])]
        return all([0 < diff <= 3 for diff in diffs]) and (
            report == sorted(report) or report == sorted(report, reverse=True)
        )

    @property
    def tolerant_safe_count(self) -> int:
        counter = 0
        for report in self.reports:
            if not self._is_safe(report):
                for i in range(len(report)):
                    if self._is_safe(report[:i] + report[i + 1 :]):
                        counter += 1
                        break
            else:
                counter += 1
        return counter


def _initialise_puzzle(file: str, year: int = 2024, day: int = 2) -> RedNoseReport:
    return RedNoseReport(file=INPUT_PATH.format(file=file, year=year, day=day))


@timer
def part_one(file: str):
    report = _initialise_puzzle(file=file)
    print(report.safe_count)


# part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str):
    report = _initialise_puzzle(file=file)
    print(report.tolerant_safe_count)


# part_two("eg")
part_two("input")
