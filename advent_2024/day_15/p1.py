import time
import pathlib

"""
Warehouse Woes I

parse the grid into a list of lists representing each line with individual replaceable elements
parse the moves into a single string with no new lines
note the start position of the robot
set current = start
loop through each move
note the direction
get the next_ position
note all nodes until the edge in the given direction
check if a move is possible
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
        for move in moves:
            dr, dc = _DIRECTION_VECTORS[move]
            all_nodes_in_direction = []
            i = 1
            r, c = current
            while 0 < next_[0] < rows - 1 and 0 < next_[1] < cols - 1:
                next_ = r + (i * dr), c + (i * dc)
                all_nodes_in_direction.append(next_)
                i += 1

            if grid[next_[0]][next_[1]] == "#":
                continue


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

# start = time.perf_counter()
# print(sum_gps_coordinates(str((pathlib.Path(__file__).resolve().parents[2] / "my_inputs/2024/day_15" / "input.txt"))))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
