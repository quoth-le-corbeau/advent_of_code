from pathlib import Path
import numpy as np

from reusables import timer, INPUT_PATH


class Schematic:
    def __init__(self, file: str):
        with open(
            file=Path(__file__).resolve().parents[2] / file, mode="r"
        ) as puzzle_input:
            self.keys = []
            self.locks = []
            self.max_height = 0
            self.max_pin_rows = 0
            keys = []
            locks = []
            height_map = []
            for schematic in [
                s.splitlines() for s in puzzle_input.read().split("\n\n")
            ]:
                self.max_pin_rows = len(schematic) - 2
                if all(char == "#" for char in schematic[0]):
                    locks.append(schematic)
                else:
                    assert all(char == "#" for char in schematic[-1])
                    keys.append(schematic)
                max_pin_heights = [0 for c in range(len(schematic[0]))]
                for r, row in enumerate(schematic):
                    pin = "#" if schematic in locks else "."
                    label = "key" if schematic in keys else "lock"
                    for c, col in enumerate(row):
                        if col == pin:
                            max_pin_heights[c] = (
                                r if label == "lock" else self.max_pin_rows - r
                            )
                self.max_height = r - 1
                height_map.append((max_pin_heights, schematic, label))

            for elem in height_map:
                if elem[2] == "key":
                    self.keys.append((elem[0]))
                else:
                    assert elem[2] == "lock"
                    self.locks.append(elem[0])

            # print(f"{self.keys=}")
            # print(f"{self.locks=}")
            # print(f"{self.max_pin_rows=}")

    def find_fits(self) -> int:
        fits = 0
        for lock in self.locks:
            for key in self.keys:
                if all(
                    abs(x) <= self.max_pin_rows for x in np.array(lock) + np.array(key)
                ):
                    fits += 1
        return fits


@timer
def part_one(file: str, year: int = 2024, day: int = 25):
    input_file = INPUT_PATH.format(file=file, year=year, day=day)
    schematic = Schematic(file=input_file)
    print(f"Fits: {schematic.find_fits()}")


# part_one("eg")
part_one("input")
