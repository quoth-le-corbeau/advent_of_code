import math
from collections import defaultdict
from pathlib import Path

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


def _get_asteroid_locations(day: int, file: str, year: int) -> list[tuple[int, int]]:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    locations: list[tuple[int, int]] = _parse_grid(file_path=input_file_path)
    return locations


def _gcd(x: int, y: int) -> int:
    if x == 0:
        return abs(y)
    return _gcd(y % x, x)


def _get_unit_vector(from_: tuple[int, int], to_: tuple[int, int]) -> tuple[int, int]:
    vector = (to_[0] - from_[0], to_[1] - from_[1])
    x, y = vector
    gcd = _gcd(x, y)
    if gcd == 1:
        return vector
    return vector[0] // gcd, vector[1] // gcd


def _angle_clockwise(coord):
    x, y = coord
    angle = math.atan2(y, x)
    return -angle % (2 * math.pi)


def _manhattan_distance(coord):
    x, y = coord
    return abs(x) + abs(y)


@timer
def part_one(file: str, day: int = 10, year: int = 2019) -> int:
    locations = _get_asteroid_locations(day=day, file=file, year=year)
    count_by_location: dict[tuple[int, int], int] = {
        location: 0 for location in locations
    }
    for i, asteroid in enumerate(locations):
        visited_unit_vectors = set()
        for other_asteroid in locations[:i] + locations[i + 1 :]:
            visited_unit_vectors.add(
                _get_unit_vector(from_=other_asteroid, to_=asteroid)
            )
        count_by_location[asteroid] += len(visited_unit_vectors)
    # sorted_by_location = dict(sorted(count_by_location.items(), key=lambda d: d[1]))
    # print(sorted_by_location)
    return max(count_by_location.values())


@timer
def part_two(file: str, day: int = 10, year: int = 2019) -> int:
    locations = _get_asteroid_locations(day=day, file=file, year=year)
    others_by_unit_vector_by_location: dict[
        tuple[int, int], dict[tuple[int, int], list[tuple[int, int]]]
    ] = {location: defaultdict(list) for location in locations}
    for i, asteroid_location in enumerate(locations):
        others_by_unit_vector = defaultdict(list)
        for other in locations[:i] + locations[i + 1 :]:
            unit_vector = _get_unit_vector(from_=other, to_=asteroid_location)
            others_by_unit_vector[unit_vector].append(other)
        others_by_unit_vector_by_location[asteroid_location] = others_by_unit_vector
    monitoring_station_coordinates = max(
        others_by_unit_vector_by_location,
        key=lambda k: len(others_by_unit_vector_by_location[k]),
    )
    relevant_asteroids_by_unit_vector = others_by_unit_vector_by_location[
        monitoring_station_coordinates
    ]
    sorted_relevant_asteroids_by_unit_vector = {}
    sorted_keys = sorted(relevant_asteroids_by_unit_vector.keys(), key=_angle_clockwise)

    for key in sorted_keys:
        sorted_values = sorted(
            relevant_asteroids_by_unit_vector[key], key=_manhattan_distance
        )
        sorted_relevant_asteroids_by_unit_vector[key] = sorted_values

    counter = -1
    i = 0
    target = None
    while not target:
        for asteroid_list in sorted_relevant_asteroids_by_unit_vector.values():
            try:
                next_ = asteroid_list[i]
                counter += 1
                if counter == 200:
                    target = next_
                    print(f"200th vaporized asteroid at: {target}")
                    break
                    # return next_[0] * 100 + next_[1]
            except IndexError:
                continue
        i += 1
    return target[0] * 100 + target[1]


if __name__ == "__main__":
    part_one(file="eg")
    #    part_one(file="eg_1_2_35")
    #    part_one(file="eg_5_8_33")
    #    part_one(file="eg_6_3_41")
    #    part_one(file="eg_11_13_210")
    part_one(file="input")

    part_two(file="input")
