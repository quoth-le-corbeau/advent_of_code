import time
import pathlib
from collections import defaultdict

"""
Garden Groups Part I

loop through the grid
build a dictionary where the keys are the plant type
    coordinates_by_plant_type = {
                                    R: [
                                        (0,0), (0, 1), (0, 2), (1, 0), (1, 1) ... 
                                        ],
                                    I: [(0, 4), (0, 5),  ... 
                                }
whilst creating the dictionary check the last entry tuple for that type 
if its manhattan distance >= 2 add an end-marker "end"




"""


def get_garden_group_price(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip()
        grid = [line for line in lines.split("\n")]
        new_plan = _get_patches_by_type(grid=grid)
        print(f"{new_plan=}")
        total_price = 0
        for type, patches in new_plan.items():
            for patch in patches:
                perimeter = _get_patch_perimeter(grid=grid, patch=patch, type=type)
                area = len(patch)
                print(
                    f"A region of type: {type} with area: {area}, perimeter: {perimeter}"
                )
                total_price += perimeter * area
        return total_price


def _get_patch_perimeter(grid: list, patch: list[tuple[int, int]], type: str) -> int:
    count = 0
    for square in patch:
        r, c = square
        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (
                r + direction[0] < 0
                or r + direction[0] >= len(grid)
                or c + direction[1] < 0
                or c + direction[1] >= len(grid[0])
            ):
                count += 1
            elif grid[r + direction[0]][c + direction[1]] != type:
                count += 1
    return count


def _get_patches_by_type(grid: list[str]) -> dict[str, list[list[tuple[int, int]]]]:
    patches_by_type = defaultdict(list)
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            current = (r, c)
            if col in patches_by_type:
                if all(
                    _manhattan(p1=current, p2=latest) > 2
                    for latest in patches_by_type[col]
                    if latest != "end"
                ):
                    patches_by_type[col].append("end")
            patches_by_type[col].append(current)
    new_plan = {type: [] for type in patches_by_type}
    for type, patch_maps in patches_by_type.items():
        i = 0
        patch = []
        while i < len(patch_maps):
            if patch_maps[i] == "end":
                new_plan[type].append(patch)
                patch = []
            else:
                patch.append(patch_maps[i])
            i += 1
        new_plan[type].append(patch)
    return new_plan


def _manhattan(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


timer_start = time.perf_counter()
print(
    get_garden_group_price(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_12"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

# timer_start = time.perf_counter()
# print(
#    get_garden_group_price(
#        str(
#            (
#                pathlib.Path(__file__).resolve().parents[2]
#                / "my_inputs/2024/day_12"
#                / "input.txt"
#            )
#        )
#    )
# )
# print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

new_plan = {
    "R": [
        [
            (0, 0),
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 0),
            (1, 1),
            (1, 2),
            (1, 3),
            (2, 2),
            (2, 3),
            (2, 4),
            (3, 2),
        ]
    ],
    "I": [
        [(0, 4), (0, 5), (1, 4), (1, 5)],
        [(5, 2), (6, 2), (6, 3), (6, 4)],
        [
            (7, 1),
            (7, 2),
            (7, 3),
            (7, 4),
            (7, 5),
            (8, 1),
            (8, 2),
            (8, 3),
            (8, 5),
            (9, 3),
        ],
    ],
    "C": [
        [(0, 6), (0, 7), (1, 6), (1, 7), (1, 8)],
        [(2, 5), (2, 6)],
        [(3, 3), (3, 4), (3, 5), (4, 4)],
        [(4, 7), (5, 4), (5, 5), (6, 5)],
    ],
    "F": [
        [(0, 8), (0, 9), (1, 9)],
        [(2, 7), (2, 8), (2, 9), (3, 7), (3, 8), (3, 9), (4, 8)],
    ],
    "V": [
        [
            (2, 0),
            (2, 1),
            (3, 0),
            (3, 1),
            (4, 0),
            (4, 1),
            (4, 2),
            (4, 3),
            (5, 0),
            (5, 1),
            (5, 3),
            (6, 0),
            (6, 1),
        ]
    ],
    "J": [
        [(3, 6)],
        [
            (4, 5),
            (4, 6),
            (5, 6),
            (5, 7),
            (6, 6),
            (6, 7),
            (7, 6),
            (7, 7),
            (8, 6),
            (9, 6),
        ],
    ],
    "E": [
        [(4, 9)],
        [(5, 8), (5, 9), (6, 8), (6, 9), (7, 8), (7, 9)],
        [(8, 7), (8, 8), (8, 9), (9, 7), (9, 8), (9, 9)],
    ],
    "M": [[(7, 0), (8, 0), (9, 0), (9, 1), (9, 2)]],
    "S": [[(8, 4), (9, 4), (9, 5)]],
}
