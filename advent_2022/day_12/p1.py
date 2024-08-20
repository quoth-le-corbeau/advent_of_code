from typing import Any, Union
import time
import pathlib
import numpy as np
import astar


def get_minimal_steps_to_goal(file_path: str) -> None:
    elevation_map_grid = _read_grid_from_file(file=file_path)
    start, goal = _get_start_end_coordinates(grid=elevation_map_grid)
    a_star = astar.AStar(
        start=start,
        grid=elevation_map_grid,
        height=len(elevation_map_grid),
        width=len(elevation_map_grid[0]),
    )
    path_to_goal = a_star.compute_path(end_node=astar.Node(position=goal))
    print(f"Solution: {len(path_to_goal)=}")
    print("The path:")
    for coordinate in path_to_goal:
        print(elevation_map_grid[coordinate[1]][coordinate[0]])


def _get_start_end_coordinates(
    grid: list[list[str]],
) -> tuple[tuple[int, int], tuple[int, int]]:
    points = dict()
    for y, row in enumerate(grid):
        if "S" in row or "E" in row:
            for x, col in enumerate(row):
                if col == "S":
                    points["start"] = (x, y)
                elif col == "E":
                    points["goal"] = (x, y)
                else:
                    continue

    return points["start"], points["goal"]


def _read_grid_from_file(
    file: str,
) -> Union[np.ndarray[Any, np.dtype[Any]], list[list[str]]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        grid = np.array([[s for s in line] for line in lines])
        return grid


start = time.perf_counter()
get_minimal_steps_to_goal("eg.txt")
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
get_minimal_steps_to_goal("input.txt")
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
