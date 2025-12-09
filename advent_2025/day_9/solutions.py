from pathlib import Path

from reusables import timer, INPUT_PATH

GridPoint = tuple[int, int]


def _parse_coordinates(file_path: Path) -> list[GridPoint]:
    red_tile_x_y = []
    with open(file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        for line in lines:
            x, y = line.split(",")
            red_tile_x_y.append((int(x), int(y)))
    return red_tile_x_y


def _area(a: GridPoint, b: GridPoint) -> int:
    x, y = a
    x1, y1 = b
    return (abs(y - y1) + 1) * (abs(x - x1) + 1)


@timer
def part_one(file: str, day: int = 9, year: int = 2025) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    red_tile_coordinates = _parse_coordinates(file_path=input_file_path)
    areas = sorted(
        [
            (_area(a, b), a, b)
            for i, a in enumerate(red_tile_coordinates)
            for b in red_tile_coordinates[i + 1 :]
        ]
    )
    return areas[-1][0]


# part_one(file="eg")
# part_one(file="input")


def _form_boundary(red_tiles: list[GridPoint]) -> set[GridPoint]:
    # shoot out rays in all directions

    # cull these to the given red tiles
    pass


@timer
def part_two(file: str, day: int = 9, year: int = 2025) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    red_tile_coordinates: list[GridPoint] = _parse_coordinates(
        file_path=input_file_path
    )
    boundary = _form_boundary(red_tile_coordinates)
    areas = sorted(
        [
            (_area(a, b), a, b)
            for i, a in enumerate(red_tile_coordinates)
            for b in red_tile_coordinates[i + 1 :]
            # filter by being within boundary
        ]
    )


part_two(file="eg")
# part_two(file="input")
