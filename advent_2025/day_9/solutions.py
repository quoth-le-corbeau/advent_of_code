from pathlib import Path

from reusables import timer, INPUT_PATH

GridPoint = tuple[int, int]


def _parse_coordinates(
    file_path: Path,
) -> list[GridPoint]:
    red_tile_x_y_coordinates = list()
    with open(file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        for line in lines:
            x, y = line.split(",")
            red_tile_x_y_coordinates.append((int(x), int(y)))
    return red_tile_x_y_coordinates


def _area(a: GridPoint, b: GridPoint) -> int:
    x, y = a
    x1, y1 = b
    area = (abs(y - y1) + 1) * (abs(x - x1) + 1)
    return area


@timer
def part_one(file: str, day: int = 9, year: int = 2025) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    red_tile_coordinates = _parse_coordinates(file_path=input_file_path)
    areas = sorted(
        [
            (_area(a, b), a, b)
            for i, a in enumerate(list(red_tile_coordinates))
            for b in list(red_tile_coordinates)[i + 1 :]
        ]
    )
    return areas[-1][0]


# part_one(file="eg")
# part_one(file="input")


def _inside_condition(lower: int, upper: int, point: int) -> bool:
    return lower < point < upper


def _rectangle_inside_perimeter(
    corner: GridPoint,
    opposite_corner: GridPoint,
    perimeter_lines: list[tuple[GridPoint, GridPoint]],
) -> bool:
    valid = True
    rectangle_min_x = min(corner[0], opposite_corner[0])
    rectangle_min_y = min(corner[1], opposite_corner[1])
    rectangle_max_x = max(corner[0], opposite_corner[0])
    rectangle_max_y = max(corner[1], opposite_corner[1])

    for perimeter_line in perimeter_lines:
        (x1, y1), (x2, y2) = perimeter_line
        # all horizontal or vertical lines so x1 == y1 or y1 == y2
        p_min_x = min(x1, x2)
        p_max_x = max(x1, x2)
        p_min_y = min(y1, y2)
        p_max_y = max(y1, y2)
        # guarantee direction of perimeter line N -> E and S -> N (x2 > x1) and (y2 > y1)
        x1, x2 = p_min_x, p_max_x
        y1, y2 = p_min_y, p_max_y

        if (
            _inside_condition(lower=rectangle_min_x, upper=rectangle_max_x, point=x1)
            and _inside_condition(
                lower=rectangle_min_y, upper=rectangle_max_y, point=y1
            )
            and _inside_condition(
                lower=rectangle_min_x, upper=rectangle_max_x, point=x2
            )
            and _inside_condition(
                lower=rectangle_min_y, upper=rectangle_max_y, point=y2
            )
        ):
            valid = False

        if (
            x1 == x2
            and _inside_condition(
                lower=rectangle_min_x, upper=rectangle_max_x, point=x1
            )
            and y2 > rectangle_min_y
            and y1 < rectangle_max_y
        ):
            valid = False

        if (
            y1 == y2
            and _inside_condition(
                lower=rectangle_min_y, upper=rectangle_max_y, point=y1
            )
            and x2 > rectangle_min_x
            and x1 < rectangle_max_x
        ):
            valid = False

    return valid


@timer
def part_two(file: str, day: int = 9, year: int = 2025) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    red_tile_coordinates = _parse_coordinates(file_path=input_file_path)
    perimeter_lines = list(zip(red_tile_coordinates[:-1], red_tile_coordinates[1:]))
    valid_areas = [
        (_area(a, b), a, b)
        for i, a in enumerate(list(red_tile_coordinates))
        for b in list(red_tile_coordinates)[i + 1 :]
        if _rectangle_inside_perimeter(a, b, perimeter_lines)
    ]

    return max(valid_areas)[0]


part_two(file="eg")
part_two(file="input")  # 1554370486
