import time
import pathlib
from collections import deque

"""
Warehouse Woes Part II

having blown up the grid
follow similar rules to part I
Note: horizontal moves are similar but now require moving two brackets
      vertical moves are more complex and require a bfs to find connected boxes 
      of which some will still not move.
  vertical and horizontal movement:
  when a box is encountered by the robot in the up or down directions use the following methods:
      - get all adjacent boxes
      - filter adjacent boxes for those that will be pushed
      - check the space at the end of the block into which the outer most boxes should move for walls
      - if walls do nothing
      - else move all the filtered selection of boxes one space in the direction


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


def _get_robo_start(grid: list[list[str]]) -> tuple[int, int]:
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "@":
                return r, c
    raise ValueError(f"No start_position position found")


def _get_adjacent_boxes(
    grid: list[list[str]], start_: tuple[int, int]
) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    queue = deque([start_])
    visited = {start_}
    box_coordinates = [start_]
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
    return boxes


def _debugger_print(grid, moves, n):
    print("---------------------DEBUGGING-----------------------------")
    if n >= 1:
        print(f"Next move: {moves[n]}. Move number: {n} of {len(moves)}")
    else:
        print("Start position: ")
    for line in grid:
        print("".join(line))


def _get_touching_boxes(
    boxes: list[tuple[tuple[int, int], tuple[int, int]]],
    dr: int,
    contact_start: tuple[int, int],
) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    adjacent_boxes = sorted(boxes, key=lambda box: (box[0][0], box[0][1]))
    contact_boxes = [
        box
        for box in adjacent_boxes
        if box[0][0] == contact_start[0]
        and (box[0][1] == contact_start[1] or box[1][1] == contact_start[1])
    ]
    touching_boxes = [contact_boxes[0]]
    if dr == -1:
        all_rows = sorted(
            list(
                set(
                    [
                        box[0][0]
                        for box in adjacent_boxes
                        if box[0][0] < contact_start[0]
                    ]
                )
            ),
            reverse=True,
        )
    else:
        all_rows = sorted(
            list(
                set(
                    [
                        box[0][0]
                        for box in adjacent_boxes
                        if box[0][0] > contact_start[0]
                    ]
                )
            ),
            reverse=False,
        )
    for row in all_rows:
        all_boxes_in_row = [box for box in adjacent_boxes if box[0][0] == row]
        contact_cols = []
        for contact_box in contact_boxes:
            contact_cols.append(contact_box[0][1])
            contact_cols.append(contact_box[1][1])
        new_contact_boxes = [
            box
            for box in all_boxes_in_row
            if box[0][1] in contact_cols or box[1][1] in contact_cols
        ]
        touching_boxes += new_contact_boxes
        contact_boxes = new_contact_boxes
    return touching_boxes


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


def sum_gps_coordinates_2(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        warehouse_floor, moves = puzzle_input.read().strip().split("\n\n")
        grid = [list(line) for line in warehouse_floor.splitlines()]
        moves = moves.replace("\n", "")
        grid = _blow_up_grid(grid=grid)
        start_position = _get_robo_start(grid=grid)
        current = start_position
        for n, move in enumerate(moves):
            dr, dc = _DIRECTION_VECTORS[move]
            # _debugger_print(grid, moves, n)
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
                    while 0 < p[0] < len(grid) - 1 and 0 < p[1] < len(grid[0]) - 1:
                        p = r, c + (i * dc)
                        if grid[p[0]][p[1]] == "#":
                            break
                        look_ahead.append(p)
                        i += 1
                    if not any([grid[node[0]][node[1]] == "." for node in look_ahead]):
                        continue  # boxes all the way to the wall
                    else:
                        i = 0
                        while grid[look_ahead[i][0]][look_ahead[i][1]] in ["[", "]"]:
                            i += 1
                        for node in look_ahead[1:i]:
                            if grid[node[0]][node[1]] == "[":
                                grid[node[0]][node[1]] = "]"
                            else:
                                grid[node[0]][node[1]] = "["
                            if move == "<":
                                grid[look_ahead[i][0]][look_ahead[i][1]] = "["
                            else:
                                grid[look_ahead[i][0]][look_ahead[i][1]] = "]"
                            grid[look_ahead[0][0]][look_ahead[0][1]] = "@"
                            grid[current[0]][current[1]] = "."
                        current = next_
                else:
                    will_move = True
                    adjacent_boxes = _get_adjacent_boxes(start_=next_, grid=grid)
                    touching_boxes = _get_touching_boxes(
                        boxes=adjacent_boxes, dr=dr, contact_start=next_
                    )
                    for box in touching_boxes:
                        if not _can_move(box=box, move=move, grid=grid):
                            will_move = False
                            break
                    if will_move:
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
