from pathlib import Path
from collections import defaultdict

from reusables import timer, INPUT_PATH


BASE_PATH = Path(__file__).resolve().parents[2]


class CityMap:
    def __init__(self, path: Path):
        with path.open(mode="r", encoding="utf-8") as puzzle_input:
            self.grid = [
                list(line) for line in puzzle_input.read().strip().splitlines()
            ]
            self.frequencies = defaultdict(list)
            for r, row in enumerate(self.grid):
                for c, col in enumerate(row):
                    if col != ".":
                        self.frequencies[col].append((r, c))
            # print(self.frequencies)

    @property
    def all_antinodes(self) -> set[tuple[int, int]]:
        antinodes = set()
        for frequency, locations in self.frequencies.items():
            for i, location in enumerate(sorted(locations)):
                for other in locations[i + 1 :]:
                    manhattan = other[0] - location[0], other[1] - location[1]
                    antenna_1 = location[0] - manhattan[0], location[1] - manhattan[1]
                    antenna_2 = other[0] + manhattan[0], other[1] + manhattan[1]
                    if 0 <= antenna_1[0] < len(self.grid) and 0 <= antenna_1[1] < len(
                        self.grid[0]
                    ):
                        antinodes.add(antenna_1)
                    if 0 <= antenna_2[0] < len(self.grid) and 0 <= antenna_2[1] < len(
                        self.grid[0]
                    ):
                        antinodes.add(antenna_2)
        return antinodes

    @property
    def resonant_antinodes(self) -> set[tuple[int, int]]:
        antinodes = set()
        for frequency, locations in self.frequencies.items():
            for i, location in enumerate(sorted(locations)):
                for other in locations[i + 1 :]:
                    manhattan = other[0] - location[0], other[1] - location[1]
                    # use while loop for each direction include antinodes outside grid filter later
                    antenna_1 = location[0] - manhattan[0], location[1] - manhattan[1]
                    antenna_2 = other[0] + manhattan[0], other[1] + manhattan[1]
                    antinodes.add(antenna_1)
                    antinodes.add(antenna_2)
                    n = 0
                    while 0 <= location[0] - (n * manhattan[0]) < len(
                        self.grid
                    ) and 0 <= location[1] - (n * manhattan[1]) < len(self.grid[0]):
                        ar, ac = location[0] - (n * manhattan[0]), location[1] - (
                            n * manhattan[1]
                        )
                        antinodes.add((ar, ac))
                        n += 1
                    m = 0
                    while 0 <= other[0] + (m * manhattan[0]) < len(
                        self.grid
                    ) and 0 <= other[1] + (m * manhattan[1]) < len(self.grid):
                        br, bc = other[0] + (m * manhattan[0]), other[1] + (
                            m * manhattan[1]
                        )
                        antinodes.add((br, bc))
                        m += 1
        return self.filter_in_grid(antinodes)

    def filter_in_grid(self, antinodes: set[tuple[int, int]]) -> set[tuple[int, int]]:
        filtered = set()
        for node in antinodes:
            if 0 <= node[0] < len(self.grid) and 0 <= node[1] < len(self.grid[1]):
                filtered.add(node)
        return filtered

    def print_antennae(self):
        base_grid = self.grid.copy()
        antenna_locations = self.all_antinodes
        for antenna_location in antenna_locations:
            r, c = antenna_location
            base_grid[r][c] = "#"
        for row in base_grid:
            print("".join(row))


@timer
def part_one(filename: str) -> int:
    city_map = CityMap(
        path=BASE_PATH / INPUT_PATH.format(file=filename, year=2024, day=8)
    )
    all_antinodes = city_map.all_antinodes
    return len(all_antinodes)
    # city_map.print_antennae()


# part_one(filename="eg")
part_one(filename="input")


@timer
def part_two(filename: str) -> int:
    city_map = CityMap(
        path=BASE_PATH / INPUT_PATH.format(file=filename, year=2024, day=8)
    )
    all_resonant_antinodes = city_map.resonant_antinodes
    return len(all_resonant_antinodes)
    # city_map.print_antennae()


# part_two(filename="eg")
part_two(filename="input")
