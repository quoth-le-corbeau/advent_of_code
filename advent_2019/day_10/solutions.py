from pathlib import Path
from math import gcd

from reusables import timer, INPUT_PATH


def _parse_grid(file_path: Path) -> list[tuple[int, int]]:
    with open(file_path, "r") as puzzle_input:
        grid = [list(line) for line in puzzle_input.read().strip().splitlines()]
        asteroid_locations = []
        for r, row in enumerate(grid):
            for c, col in enumerate(grid[0]):
                if grid[r][c] == "#":
                    asteroid_locations.append((c, r))
        return asteroid_locations


def _gcd(x: int, y: int) -> int:
    pass


def _get_unit_vector(from_: tuple[int, int], to_: [int, int]) -> tuple[int, int]:
    pass


@timer
def part_one(file: str, day: int = 10, year: int = 2019) -> dict[tuple[int, int], int]:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    locations: list[tuple[int, int]] = _parse_grid(file_path=input_file_path)
    count_by_location = {location: 0 for location in locations}
    for i, asteroid in enumerate(locations):
        visited_unit_vectors = set()
        for other_asteroid in locations[:i] + locations[i + 1 :]:
            visited_unit_vectors.add(
                _get_unit_vector(from_=other_asteroid, to_=asteroid)
            )
        count_by_location[asteroid] += len(visited_unit_vectors)
    return dict(sorted(count_by_location.items(), key=lambda d: d[1]))


part_one(file="eg")
# part_one(file="eg_1_2_35")
# part_one(file="eg_5_8_33")
# part_one(file="eg_6_3_41")
# part_one(file="eg_11_13_210")
# part_one(file="input")


@timer
def part_two(file: str, day: int = 10, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    print(f"part 2: {_parse_grid(file_path=input_file_path)}")


# part_two(file="eg")
# part_two(file="input")
