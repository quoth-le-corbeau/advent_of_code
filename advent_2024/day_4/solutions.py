from pathlib import Path

from reusables import timer, INPUT_PATH


class WordSearch:
    def __init__(self, file: str):
        with open(
            file=Path(__file__).resolve().parents[2] / file, mode="r", encoding="utf-8"
        ) as puzzle_input:
            self.grid = [
                list(line) for line in puzzle_input.read().strip().splitlines()
            ]

    def print_grid(self, occurrences: list[tuple[int, int]]) -> None:
        """For debugging purposes"""

        for r, row in enumerate(self.grid):
            for c, col in enumerate(row):
                if (r, c) in occurrences:
                    continue
                else:
                    self.grid[r][c] = "."
        for row in self.grid:
            print("".join(row))

    def count_all_occurrences(self, pattern: str = "XMAS") -> int:
        accepted = [list(pattern), list(pattern[::-1])]
        search_distance = len(pattern)
        count = 0
        occurrences = []
        for r, row in enumerate(self.grid):
            vertical_condition = r <= len(self.grid) - search_distance
            for c, col in enumerate(row):
                horizontal_end_condition = c <= len(self.grid[0]) - search_distance
                horizontal_start_condition = c >= search_distance - 1
                if (
                    vertical_condition
                    and [self.grid[r + i][c] for i in range(search_distance)]
                    in accepted
                ):
                    count += 1
                    occurrences += [(r + i, c) for i in range(search_distance)]
                if (
                    horizontal_end_condition
                    and [self.grid[r][c + i] for i in range(search_distance)]
                    in accepted
                ):
                    count += 1
                    occurrences += [(r, c + i) for i in range(search_distance)]
                if (
                    vertical_condition
                    and horizontal_end_condition
                    and [self.grid[r + i][c + i] for i in range(search_distance)]
                    in accepted
                ):
                    count += 1
                    occurrences += [(r + i, c + i) for i in range(search_distance)]
                if (
                    vertical_condition
                    and horizontal_start_condition
                    and [self.grid[r + i][c - i] for i in range(search_distance)]
                    in accepted
                ):
                    count += 1
                    occurrences += [(r + i, c - i) for i in range(search_distance)]
        # self.print_grid(occurrences=occurrences)
        return count

    def count_all_criss_cross(self, pattern: str = "MAS") -> int:
        accepted = [list(pattern), list(pattern[::-1])]
        search_distance = (
            len(pattern[: len(pattern) // 2] + pattern[(len(pattern) // 2) + 1 :]) // 2
        )
        count = 0
        occurrences = []
        for r, row in enumerate(self.grid):
            vertical_condition = (
                0 + search_distance <= r < len(self.grid) - search_distance
            )
            for c, col in enumerate(row):
                horizontal_condition = (
                    0 + search_distance <= c < len(self.grid[0]) - search_distance
                )
                if (
                    col == pattern[len(pattern) // 2]
                    and vertical_condition
                    and horizontal_condition
                    and [
                        self.grid[r + i][c + i]
                        for i in range(-search_distance, search_distance + 1)
                    ]
                    in accepted
                    and [
                        self.grid[r + i][c - i]
                        for i in range(-search_distance, search_distance + 1)
                    ]
                    in accepted
                ):
                    count += 1
                    occurrences += [
                        (r + i, c + i)
                        for i in range(-search_distance, search_distance + 1)
                    ] + [
                        (r + i, c - i)
                        for i in range(-search_distance, search_distance + 1)
                    ]
        # self.print_grid(occurrences=occurrences)
        return count


def _initialise_puzzle(file: str) -> WordSearch:
    return WordSearch(file=INPUT_PATH.format(file=file, year=2024, day=4))


@timer
def part_one(filename: str) -> int:
    word_search = _initialise_puzzle(file=filename)
    return word_search.count_all_occurrences()


# part_one("eg")
part_one("input")


@timer
def part_two(filename: str) -> int:
    word_search = _initialise_puzzle(file=filename)
    return word_search.count_all_criss_cross()


# part_two("eg")
part_two("input")
