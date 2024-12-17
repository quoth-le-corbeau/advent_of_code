import time
import pathlib

"""
Warehouse Woes Part I

parse the grid into a list of lists representing each line with individual replaceable elements
parse the moves into a single string with no new lines
note the start position of the robot
set current = start
loop through each move
note the direction
get the next_ position
note all nodes until the edge in the given direction
check if a move is possible
    this involves checking if there is space to move a box into before hitting a wall
if not, continue
else: perform the move replacing the necessary grid points

after loop completion loop through the grid to get all box positions and calculate the gps values
finally return the sum of all gps values

"""

_DIRECTION_VECTORS = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}


def sum_gps_coordinates(file_path: str):
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        grid, moves = puzzle_input.read().strip().split("\n\n")
        grid = [list(line) for line in grid.splitlines()]
        moves = moves.replace("\n", "")
        rows = len(grid)
        cols = len(grid[0])
        # print(f"{cols=}")

        def get_start_position() -> tuple[int, int]:
            for r, row in enumerate(grid):
                for c, col in enumerate(row):
                    if col == "@":
                        return r, c
            raise ValueError(f"No start_position position found")

        start_position = get_start_position()
        current = start_position
        for n, move in enumerate(moves):
            dr, dc = _DIRECTION_VECTORS[move]
            r, c = current
            next_ = r + dr, c + dc
            if grid[next_[0]][next_[1]] == "#":
                continue  # immediately blocked by wall no move
            elif grid[next_[0]][next_[1]] == ".":
                grid[next_[0]][next_[1]] = "@"
                grid[current[0]][current[1]] = "."
                current = next_
                continue  # simply move into the space and await next move
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
                assert grid[next_[0]][next_[1]] == "O"
                # must have a box in front of us and there must be space somewhere in the direction of travel
                # but the space may be behind a wall!
                j = 0
                while grid[look_ahead[j][0]][look_ahead[j][1]] != "#":
                    if grid[look_ahead[j][0]][look_ahead[j][1]] == ".":
                        grid[look_ahead[j][0]][look_ahead[j][1]] = "O"
                        grid[next_[0]][next_[1]] = "@"
                        grid[current[0]][current[1]] = "."
                        current = next_
                        break
                    else:
                        j += 1

        gps_sums = []
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == "O":
                    gps_sums.append(100 * r + c)
        return sum(gps_sums)


start = time.perf_counter()
print(
    sum_gps_coordinates(
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
    sum_gps_coordinates(
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
