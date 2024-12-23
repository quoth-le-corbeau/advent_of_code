import time
import pathlib
from collections import deque
from typing import List, Tuple

"""
Warehouse Woes Part II

having blown up the grid
follow similar rules to part I
Note: horizontal moves are similar but now require moving two brackets
      vertical moves are more complex and require a bfs to find connected boxes 
        of which some will still not move


"""

_DIRECTION_VECTORS = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}


def _blow_up_grid(grid: list[list[str]]) -> list[list[str]]:
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if grid[r][c] == "#":
                grid[r][c] = "#,#"
            elif grid[r][c] == ".":
                grid[r][c] = ".,."
            elif grid[r][c] == "O":
                grid[r][c] = "[,]"
            elif grid[r][c] == "@":
                grid[r][c] = "@,."
            else:
                raise ValueError(f"Unknown character in grid: {grid[r][c]}")
    blown_up_grid = []
    for row in grid:
        blown_up_row = []
        for elem in row:
            blown_up_row += elem.split(",")
        blown_up_grid.append(blown_up_row)
    return blown_up_grid


def _get_start_position(grid: list[list[str]]) -> tuple[int, int]:
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "@":
                return r, c
    raise ValueError(f"No start_position position found")


def _get_adjacent_boxes(
    grid: list[list[str]], start: tuple[int, int]
) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    queue = deque([start])
    visited = {start}
    box_coordinates = [start]
    types = ["[", "]"]

    while queue:
        current = queue.popleft()
        for direction in _DIRECTION_VECTORS.values():
            next_node = current[0] + direction[0], current[1] + direction[1]
            if next_node not in visited and grid[next_node[0]][next_node[1]] in types:
                queue.append(next_node)
                visited.add(next_node)
                box_coordinates.append(next_node)
    boxes = []
    coordinates = sorted(box_coordinates)
    for i in range(0, len(coordinates) - 1, 2):
        boxes.append((coordinates[i], coordinates[i + 1]))
    return sorted(boxes, key=lambda x: (x[1], x[0]))


def _should_move(
    box: tuple[tuple[int, int], tuple[int, int]],
    contact_box: tuple[tuple[int, int], tuple[int, int]],
    move: str,
) -> bool:
    dr, dc = _DIRECTION_VECTORS[move]
    if dc != 0 or dr not in [1, -1]:
        raise ValueError("Invalid non vertical move direction!")
    f, b = box
    cf, cb = contact_box
    row_delta = f[0] - cf[0]
    if row_delta == 0:
        raise ValueError(
            "should not have any boxes at the same level as the contact box!"
        )
    col_range = range(cf[1] - abs(row_delta), cb[1] + abs(row_delta) + 1)
    if row_delta < 0:
        if dr != -1:
            return False
        else:
            assert dr == -1
    else:
        assert row_delta > 0
        if dr == -1:
            return False
        else:
            assert dr == 1
    if f[1] in col_range and b[1] in col_range:
        return True
    else:
        return False


def _can_move(
    box: tuple[tuple[int, int], tuple[int, int]], move: str, grid: list[list[str]]
) -> bool:
    dr, dc = _DIRECTION_VECTORS[move]
    return all(
        [grid[box_half[0] + dr][box_half[1]] in ["[", "]", "."] for box_half in box]
    )


def _move_boxes(
    to_move: list[tuple[tuple[int, int], tuple[int, int]]],
    move: str,
    grid: list[list[str]],
    robot: tuple[int, int],
) -> list[list[str]]:
    dr, dc = _DIRECTION_VECTORS[move]
    if dr == -1:
        reversed_ = False
    else:
        reversed_ = True
    to_move_in_row_order = sorted(to_move, key=lambda x: x[0][0], reverse=reversed_)
    for box in to_move_in_row_order:
        l, r = box
        grid[l[0] + dr][l[1]] = "["
        grid[r[0] + dr][r[1]] = "]"
        grid[l[0]][l[1]] = "."
        grid[r[0]][r[1]] = "."
    grid[robot[0]][robot[1]] = "."
    grid[robot[0] + dr][robot[1]] = "@"
    return grid


def sum_gps_coordinates_2(file_path: str):
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        grid, moves = puzzle_input.read().strip().split("\n\n")
        grid = [list(line) for line in grid.splitlines()]
        moves = moves.replace("\n", "")
        grid = _blow_up_grid(grid=grid)
        start_position = _get_start_position(grid=grid)
        cols = len(grid[0])
        rows = len(grid)
        current = start_position
        for n, move in enumerate(moves):
            dr, dc = _DIRECTION_VECTORS[move]
            print("---------------------DEBUGGING-----------------------------")
            if n >= 1:
                print(f"Next move: {moves[n]}")
            else:
                print("Start position: ")
            for line in grid:
                print("".join(line))
            r, c = current
            next_ = r + dr, c + dc
            if grid[next_[0]][next_[1]] == "#":
                continue  # immediately blocked by wall no move
            elif grid[next_[0]][next_[1]] == ".":
                grid[next_[0]][next_[1]] = "@"
                grid[current[0]][current[1]] = "."
                current = next_
                continue  # simply move into the space and await next move
            else:
                # horizontal move preparation only looks at the row
                if move in ["<", ">"]:
                    look_ahead = []
                    i = 1
                    p = start_position
                    while 0 < p[0] < rows - 1 and 0 < p[1] < cols - 1:
                        p = r + (i * dr), c + (i * dc)
                        if grid[p[0]][p[1]] == "#":
                            break
                        look_ahead.append(p)
                        i += 1
                    if not any([grid[node[0]][node[1]] == "." for node in look_ahead]):
                        continue  # boxes all the way to the wall
                    else:
                        i = 0
                        while grid[look_ahead[i][0]][look_ahead[i][1]] in [
                            "[",
                            "]",
                        ]:
                            i += 1
                        if grid[look_ahead[i][0]][look_ahead[i][1]] == "#":
                            current = next_
                            continue
                        else:
                            assert grid[look_ahead[i][0]][look_ahead[i][1]] == "."
                            # shift each node along one space in direction
                            for node in look_ahead[1:i]:
                                if grid[node[0]][node[1]] == "[":
                                    grid[node[0]][node[1]] = "]"
                                else:
                                    assert grid[node[0]][node[1]] == "]"
                                    grid[node[0]][node[1]] = "["
                            if move == "<":
                                grid[look_ahead[i][0]][look_ahead[i][1]] = "["
                            else:
                                assert move == ">"
                                grid[look_ahead[i][0]][look_ahead[i][1]] = "]"
                            grid[look_ahead[0][0]][look_ahead[0][1]] = "@"
                            grid[current[0]][current[1]] = "."
                        current = next_
                else:
                    will_move = True
                    # perform a bfs starting at next_ get all connected boxes
                    adjacent_boxes = _get_adjacent_boxes(start=next_, grid=grid)
                    contact_filter = [
                        box
                        for box in adjacent_boxes
                        if box[0][0] == next_[0]
                        and (box[0][1] == next_[1] or box[1][1] == next_[1])
                    ]
                    try:
                        assert len(contact_filter) == 1
                    except AssertionError:
                        print(f"contact filter {contact_filter} SOMETHING WRONG!")
                        print(f"robot at: {current}")
                        print(f"current move: {move}")
                        print(f"last_move: {moves[n - 1]}")
                        print(f"{len(moves) - n} moves left")
                        print(f"move number: {n}")
                        raise AssertionError
                    contact_box = contact_filter[0]
                    touching_boxes = [contact_box]
                    for box in adjacent_boxes:
                        if box == contact_box:
                            continue
                        elif box[0][0] == contact_box[0][0]:
                            continue
                        else:
                            if _should_move(
                                box=box, contact_box=contact_box, move=move
                            ):
                                touching_boxes.append(box)
                    for box in touching_boxes:
                        if not _can_move(box=box, move=move, grid=grid):
                            will_move = False
                            break
                    if will_move:
                        # perform the move
                        grid = _move_boxes(
                            to_move=touching_boxes, move=move, grid=grid, robot=current
                        )
                        current = next_

        gps_sums = []
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == "[":
                    gps_sums.append(100 * r + c)
        return sum(gps_sums)


start = time.perf_counter()
print(
    sum_gps_coordinates_2(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_15"
                / "small_eg_2.txt"
            )
        )
    )
)
print(f"SMALL TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    sum_gps_coordinates_2(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_15"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    sum_gps_coordinates_2(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_15"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
# 1576353
