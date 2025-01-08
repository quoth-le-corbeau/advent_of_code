from pathlib import Path
from reusables import timer, INPUT_PATH


class RaceTrack:
    def __init__(self, file: str):
        with open(
            file=Path(__file__).resolve().parents[2] / file, mode="r"
        ) as puzzle_input:
            grid_lines = puzzle_input.read().strip().splitlines()
            self.row_count = len(grid_lines)
            self.col_count = len(grid_lines[0])
            self.barriers = set()
            self.start = ""
            self.end = ""
            for r, row in enumerate(grid_lines):
                for c, col in enumerate(row):
                    if col == "S":
                        self.start = (r, c)
                    elif col == "E":
                        self.end = (r, c)
                    elif (
                        col == "#"
                        and r != 0
                        and r != self.row_count - 1
                        and c != 0
                        and c != self.col_count - 1
                    ):
                        self.barriers.add((r, c))
                    else:
                        assert col == "." or (
                            col == "#"
                            and (
                                r == 0
                                or r == self.row_count - 1
                                or c == 0
                                or c == self.col_count - 1
                            )
                        )

    def get_path(self):
        print(self.barriers)


@timer
def part_one(filename: str, year=2024, day=20) -> None:
    input_file = INPUT_PATH.format(file=filename, year=year, day=day)
    racetrack = RaceTrack(file=input_file)
    racetrack.get_path()


part_one("eg")
