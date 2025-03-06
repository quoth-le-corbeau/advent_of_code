from pathlib import Path
import re

from reusables import timer, INPUT_PATH

_NUMBER_OF_SIDES = 3


def _parse_rows(file_path: Path) -> list[list[int]]:
    with open(file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        return [
            sorted(list(map(int, re.findall(pattern=r"\d+", string=line))))
            for line in lines
        ]


def _parse_columns(file_path: Path) -> dict[int, list[int]]:
    with open(file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        rows = [
            list(map(int, re.findall(pattern=r"\d+", string=line))) for line in lines
        ]
        cols = {i: [] for i in range(_NUMBER_OF_SIDES)}
        for x in range(0, len(rows), 3):
            group = [rows[x], rows[x + 1], rows[x + 2]]
            for y in range(_NUMBER_OF_SIDES):
                cols[y].append(sorted([triangle[y] for triangle in group]))
        return cols


@timer
def part_one(file: str, day: int = 3, year: int = 2016) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    sorted_triangle_lengths = _parse_rows(file_path=input_file_path)
    return _count_possible_triangles(sorted_triangle_lengths)


def _count_possible_triangles(sorted_triangle_lengths):
    possible = 0
    for lengths in sorted_triangle_lengths:
        a, b, c = lengths
        if a + b > c:
            possible += 1
    return possible


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 3, year: int = 2016):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    sorted_triangle_lengths_by_column = _parse_columns(file_path=input_file_path)
    possible = 0
    for col, sorted_triangle_lengths in sorted_triangle_lengths_by_column.items():
        possible += _count_possible_triangles(sorted_triangle_lengths)
    return possible


part_two(file="input")
