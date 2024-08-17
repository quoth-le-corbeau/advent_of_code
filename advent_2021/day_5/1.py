import time
import pathlib
from operator import *


def count_least_dangerous_points(file_path: str):
    coordinate_pairs = _get_start_end_coordinates(file=file_path)
    points_on_straight_lines = list()
    for pair in coordinate_pairs:
        if pair[0][0] == pair[1][0]:
            points_on_vertical = list()
            x = pair[0][0]
            y2 = max(pair[0][1], pair[1][1])
            y1 = min(pair[0][1], pair[1][1])
            for j in range(y1, y2 + 1):
                points_on_vertical.append((x, j))
            points_on_straight_lines += points_on_vertical
        elif pair[0][1] == pair[1][1]:
            y = pair[0][1]
            x2 = max(pair[0][0], pair[1][0])
            x1 = min(pair[0][0], pair[1][0])
            points_on_horizontal = list()
            for i in range(x1, x2 + 1):
                points_on_horizontal.append((i, y))
            points_on_straight_lines += points_on_horizontal
    count = 0
    for elem in set(points_on_straight_lines):
        if countOf(points_on_straight_lines, elem) >= 2:
            count += 1
    return count



def _get_start_end_coordinates(file: str) -> list[list[tuple[int, int]]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        coordinates = list()
        matrix = [line.replace(" -> ", ",").split(",") for line in lines]
        for nums in matrix:
            coordinates.append(
                [(int(nums[0]), int(nums[1])), (int(nums[2]), int(nums[3]))]
            )
        return coordinates


start = time.perf_counter()
print(count_least_dangerous_points("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
# start = time.perf_counter()
# print(count_least_dangerous_points("input.txt"))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
