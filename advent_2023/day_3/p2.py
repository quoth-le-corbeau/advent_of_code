import time
import pathlib


def sum_gear_ratios(file: str) -> int:
    return sum(_get_gear_ratios(file=file))


def _get_gear_ratios(file: str) -> list[int]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        grid = puzzle_input.readlines()
        gear_ratios = list()
        for row_index, row in enumerate(grid):
            for column_index, column in enumerate(row):
                if column != "*":
                    continue
                part_numbers_per_gear = set()
                for vertical_index in [row_index - 1, row_index, row_index + 1]:
                    for horizontal_index in [
                        column_index - 1,
                        column_index,
                        column_index + 1,
                    ]:
                        if (
                            vertical_index < 0
                            or vertical_index > len(grid)
                            or horizontal_index >= len(grid[vertical_index])
                            or not grid[vertical_index][horizontal_index].isdigit()
                        ):
                            continue
                        while grid[vertical_index][horizontal_index - 1].isdigit():
                            horizontal_index -= 1
                        part_numbers_per_gear.add((vertical_index, horizontal_index))
                if len(part_numbers_per_gear) != 2:
                    continue
                else:
                    part_number1 = _get_part_numbers_by_coordinates(
                        grid=grid, coordinates=part_numbers_per_gear
                    )[0]
                    part_number2 = _get_part_numbers_by_coordinates(
                        grid=grid, coordinates=part_numbers_per_gear
                    )[1]
                    gear_ratios.append(part_number1 * part_number2)
        return gear_ratios


def _get_part_numbers_by_coordinates(
    grid: list[str], coordinates: set[tuple[int, int]]
) -> list[int]:
    assert len(coordinates) == 2
    part_numbers = list()
    for coordinate in coordinates:
        row, column = coordinate
        part_number_string = ""
        while column < len(grid[row]) and grid[row][column].isdigit():
            part_number_string += grid[row][column]
            column += 1
        part_numbers.append(int(part_number_string))
    return part_numbers


start = time.perf_counter()
print(sum_gear_ratios("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(sum_gear_ratios("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
