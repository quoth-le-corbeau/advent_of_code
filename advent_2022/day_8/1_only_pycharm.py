import os

import helpers


def count_visible_trees(file_path: os.path):
    grid = _get_tree_height_grid(file=file_path)
    return _count_visible_trees_in_grid(grid=grid)


def _count_visible_trees_in_grid(grid: list[list[int]]) -> int:
    visible_tree_count = 0
    for y, row in enumerate(grid):
        for x, tree in enumerate(row):
            if y == 0 or x == 0 or y == len(grid) - 1 or x == len(row) - 1:
                visible_tree_count += 1
            else:
                # look left
                if all(row[i] < tree for i in range(x)):
                    visible_tree_count += 1
                # look right
                elif all(row[i] < tree for i in range(x + 1, len(row))):
                    visible_tree_count += 1
                # look up
                elif all(grid[j][x] < tree for j in range(y)):
                    visible_tree_count += 1
                # look down
                elif all(grid[j][x] < tree for j in range(y + 1, len(grid))):
                    visible_tree_count += 1
    return visible_tree_count


def _get_tree_height_grid(file: os.path) -> list[list[int]]:
    with open(file) as puzzle_input:
        lines = puzzle_input.read().split("\n")
        grid = list()
        for line in lines:
            line = line.split()
            for string in line:
                row = list()
                for char in string:
                    row.append(int(char))
                grid.append(row)

        return grid


helpers.print_timed_results(solution_func=count_visible_trees)
