import time
import pathlib


def sum_part_numbers(file: str) -> int:
    return sum(_get_all_part_numbers(file=file))


def _get_all_part_numbers(file: str) -> list[int]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        grid = puzzle_input.readlines()
        part_number_start_coordinates: set[tuple] = set()
        for row_index, row in enumerate(grid):
            row = row.strip()
            for index, column in enumerate(row):
                if not (column.isdigit() or column == ".") and 0 < index < len(row) - 1:
                    for vertical_index in [
                        row_index - 1,
                        row_index,
                        row_index + 1,
                    ]:
                        for horizontal_index in [
                            index - 1,
                            index,
                            index + 1,
                        ]:
                            if grid[vertical_index][horizontal_index].isdigit():
                                i = horizontal_index
                                while grid[vertical_index][i].isdigit() and i >= 0:
                                    i -= 1
                                part_number_start_coordinates.add(
                                    (vertical_index, i + 1)
                                )
        all_part_numbers = parse_part_numbers(grid, part_number_start_coordinates)
        return all_part_numbers


def parse_part_numbers(
    grid: list[str], part_number_start_coordinates: set[tuple[int, int]]
) -> list[int]:
    all_part_numbers = list()
    for coordinate in part_number_start_coordinates:
        row, column = coordinate
        part_number_string = ""
        while grid[row][column].isdigit():
            part_number_string += grid[row][column]
            column += 1
        all_part_numbers.append(int(part_number_string))
    return all_part_numbers


start = time.perf_counter()
print(sum_part_numbers("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(sum_part_numbers("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
