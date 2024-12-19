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


def _bfs(grid: list[list[str]], start: tuple[int, int]) -> list[tuple[int, int]]:
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

    return box_coordinates


def _get_boxes_to_move(
    grid: list[list[str]], first_box: tuple[int, int]
) -> list[tuple[int, int]]:
    boxes = _bfs(grid=grid, start=first_box)
    return boxes  # Assume the bfs gets everything correctly for now
    # boxes_to_move = [first_box]
    # next_neighbours = [
    #     (first_box[0], first_box[1] - 1),
    #     (first_box[0], first_box[1] + 1),
    # ]
    # if grid[first_box[0][0]][first_box[0][1]] == "[":
    #     boxes_to_move.append(next_neighbours[1])
    # else:
    #     assert grid[first_box[0]][first_box[1]] == "]"
    #     assert (
    #         grid[first_box[0]][first_box[1]]
    #         + grid[next_neighbours[0][0]][next_neighbours[0][1]]
    #         == "["
    #     )
    #     boxes_to_move.append(next_neighbours[0])
    # for box in boxes:
    #     if box[0] != first_box[0]:
    #         boxes_to_move.append(box)
    # return boxes_to_move


def _get_start_position(grid: list[list[str]]) -> tuple[int, int]:
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "@":
                return r, c
    raise ValueError(f"No start_position position found")


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
                print(f"Next move: {moves[n - 1]}")
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
                        while look_ahead[i] == "[" or look_ahead[i] == "]":
                            i += 1
                        for j, node in enumerate(look_ahead[i:]):
                            grid[node[0]][node[1] * j * dc] = "#"
                        current = next_

                else:
                    # perform a bfs starting at next_ get all connected boxes
                    boxes_to_move = _get_boxes_to_move(grid=grid, first_box=next_)
                    all_box_rows = [box[0] for box in boxes_to_move]
                    cols_to_check = [
                        box[1] for box in boxes_to_move if box[0] == row_to_check
                    ]
                    if move == "^":
                        row_to_check = min(all_box_rows) - 1
                    else:
                        assert move == "v"
                        row_to_check = max(all_box_rows) + 1
                    # then make sure all squares in the direction of travel are "."
                    for col in cols_to_check:
                        if grid[row_to_check][col] != ".":
                            continue  # Assumption: if one box cannot move none can move (check edge case!)

                    # move all box-parts in direction of travel
                    new_box_positions_by_half = {
                        grid[br][bc]: (br + dr, bc + dc) for br, bc in boxes_to_move
                    }

                    # move the robot one position

                    current = next_

        gps_sums = []
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == "O":
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
