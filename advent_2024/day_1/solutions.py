from pathlib import Path

from reusables import timer, INPUT_PATH


class AdjacentList:
    def __init__(self, file: str):
        with open(
            file=Path(__file__).resolve().parents[2] / file, mode="r"
        ) as puzzle_input:
            list_lines = puzzle_input.read().strip().splitlines()
            self.left_list = []
            self.right_list = []
            for list_line in list_lines:
                x, y = list_line.split("  ")[0], list_line.split("  ")[1]
                self.left_list.append(int(x))
                self.right_list.append(int(y))
            # print(f"{self.left_list=}")
            # print(f"{self.right_list=}")

    def sum_ordered_diffs(self) -> int:
        left_list = sorted(self.left_list)
        right_list = sorted(self.right_list)
        total = 0
        for i, n in enumerate(left_list):
            total += abs(right_list[i] - n)
        return total

    @property
    def similarity_score(self) -> int:
        total = 0
        for n in self.left_list:
            total += n * self.right_list.count(n)
        return total


def _initialize_puzzle(file: str, year: int = 2024, day: int = 1) -> AdjacentList:
    return AdjacentList(file=INPUT_PATH.format(file=file, year=year, day=day))


@timer
def part_one(file: str):
    adjacent_lists = _initialize_puzzle(file=file)
    print(adjacent_lists.sum_ordered_diffs())


# part_one("eg")
part_one("input")


@timer
def part_two(file: str, year: int = 2024, day: int = 1):
    adjacent_lists = _initialize_puzzle(file=file)
    print(adjacent_lists.similarity_score)


# part_two("eg")
part_two("input")
