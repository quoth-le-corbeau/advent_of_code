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


def _gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    return _gcd(y, x % y)


def _get_unit_vector(from_: tuple[int, int], to_: [int, int]) -> tuple[int, int]:
    vector = (to_[0] - from_[0], to_[1] - from_[1])
    x, y = vector
    gcd = _gcd(x, y)
    if gcd == 1:
        return vector
    return vector[0] // abs(gcd), vector[1] // abs(gcd)


@timer
def part_one(file: str, day: int = 10, year: int = 2019) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    locations: list[tuple[int, int]] = _parse_grid(file_path=input_file_path)
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
    sorted_by_location = dict(sorted(count_by_location.items(), key=lambda d: d[1]))
    print(sorted_by_location)
    return max(count_by_location.values())


@timer
def part_two(file: str, day: int = 10, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    print(f"part 2: {_parse_grid(file_path=input_file_path)}")


# part_two(file="eg")
# part_two(file="input")
if __name__ == "__main__":
    part_one(file="eg")
    #    part_one(file="eg_1_2_35")
    #    part_one(file="eg_5_8_33")
    #    part_one(file="eg_6_3_41")
    #    part_one(file="eg_11_13_210")
    part_one(file="input")
