import time
import pathlib
from collections import deque

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


def _get_boxes_to_move(
    grid: list[list[str]], start: tuple[int, int], move_1: str, move_2: str
):
    queue = deque([start])
    visited = {start}
    box_coordinates = [start]
    types = ["[", "]"]

    while queue:
        current = queue.popleft()
        for direction in [_DIRECTION_VECTORS[move_1], _DIRECTION_VECTORS[move_2]]:
            next_node = current[0] + direction[0], current[1] + direction[1]
            if next_node not in visited and grid[next_node[0]][next_node[1]] in types:
                queue.append(next_node)
                visited.add(next_node)
                box_coordinates.append(next_node)

    return box_coordinates


def _find_pushed_boxes(grid, contact_point, direction):
    rows, cols = len(grid), len(grid[0])
    dr, dc = direction

    # Validate contact point
    r, c = contact_point
    if not (0 <= r < rows and 0 <= c < cols):
        return []

    # Check if the contact point is part of a box
    if grid[r][c] != "]" or c == 0 or grid[r][c - 1] != "[":
        return []

    queue = [(r, c - 1, r, c)]
    visited = set()
    result = []

    while queue:
        left_r, left_c, right_r, right_c = queue.pop(0)
        if (left_r, left_c, right_r, right_c) in visited:
            continue
        visited.add((left_r, left_c, right_r, right_c))

        result.extend([(left_r, left_c), (right_r, right_c)])

        next_left_r, next_left_c = left_r + dr, left_c + dc
        next_right_r, next_right_c = right_r + dr, right_c + dc

        if (
            0 <= next_left_r < rows
            and 0 <= next_left_c < cols
            and 0 <= next_right_r < rows
            and 0 <= next_right_c < cols
            and grid[next_left_r][next_left_c] == "["
            and grid[next_right_r][next_right_c] == "]"
        ):
            queue.append((next_left_r, next_left_c, next_right_r, next_right_c))

        for adj_left_c, adj_right_c in [
            (left_c - 2, left_c - 1),
            (right_c + 1, right_c + 2),
        ]:
            if (
                0 <= left_r < rows
                and 0 <= adj_left_c < cols
                and 0 <= right_r < rows
                and 0 <= adj_right_c < cols
                and grid[left_r][adj_left_c] == "["
                and grid[right_r][adj_right_c] == "]"
            ):
                queue.append((left_r, adj_left_c, right_r, adj_right_c))

    return sorted(set(result))


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
            print("-------------------------------------------------------")
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
                        look_ahead.append(p)
                        i += 1
                    if not any([grid[node[0]][node[1]] == "." for node in look_ahead]):
                        continue  # boxes all the way to the wall
                    else:
                        # TODO: do horizontal move if possible
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
                    # perform a bfs starting at next_ get all connected boxes
                    boxes_to_move = _find_pushed_boxes(
                        grid=grid,
                        contact_point=next_,
                        direction=_DIRECTION_VECTORS[move],
                    )
                    all_box_rows = sorted([box[0] for box in boxes_to_move])

                    if move == "^":
                        last_box_row = min(all_box_rows)
                        assert last_box_row == all_box_rows[0]
                    else:
                        assert move == "v"
                        last_box_row = max(all_box_rows)
                        assert last_box_row == all_box_rows[-1]
                    # then make sure all squares in the direction of travel are "."
                    cols_to_check = [
                        box[1] for box in boxes_to_move if box[0] == last_box_row
                    ]
                    if any(
                        [grid[last_box_row + dr][col] != "." for col in cols_to_check]
                    ):
                        continue  # Assumption: if one box cannot move none can move (check edge case!)
                    else:
                        # move all box-parts in direction of travel
                        for row in all_box_rows:
                            for box in boxes_to_move:
                                if box[0] == row:
                                    symbol = grid[box[0]][box[1]]
                                    prev_symbol = grid[box[0] - dr][box[1]]
                                    if symbol in ["]", "["]:
                                        grid[box[0] + dr][box[1]] = symbol
                                    if prev_symbol == "." or prev_symbol == "@":
                                        grid[box[0]][box[1]] = prev_symbol

                        # evacuate the robot one position
                        grid[current[0]][current[1]] = "."
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

# start = time.perf_counter()
# print(
#    sum_gps_coordinates_2(
#        str(
#            (
#                pathlib.Path(__file__).resolve().parents[2]
#                / "my_inputs/2024/day_15"
#                / "eg.txt"
#            )
#        )
#    )
# )
# print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
#
# start = time.perf_counter()
# print(
#    sum_gps_coordinates_2(
#        str(
#            (
#                pathlib.Path(__file__).resolve().parents[2]
#                / "my_inputs/2024/day_15"
#                / "input.txt"
#            )
#        )
#    )
# )
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
