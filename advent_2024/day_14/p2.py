import math
import time
import pathlib
import re

"""
Restroom Redoubt Part II

rows: 103, cols: 101 
get all inputs as a list of 4 integers: pr, pc, vr, vc
end position for each robot = (pr + (100 * vr)) % 103, (pc + (100 * vc)) % 101

increment the seconds one by one
feed the list of all robot positions after each second into a method that tests for a condition
condition: more than half the robots are adjacent (next to each other/ pythagorean distance <= √2)
break out of the loop and return the number of seconds when the condition is met

render the easter egg in the console and write it to a file for fun!


"""


def find_the_easter_egg(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        robots = [list(map(int, re.findall(r"([-+]?\d+)", line))) for line in lines]
        rows = 103
        cols = 101

        def more_than_half_are_adjacent(positions: list[tuple[int, int]]) -> bool:
            s_pos = sorted(positions)
            count = 0
            for i in range(len(s_pos) - 1):
                distance = math.sqrt(
                    (
                        abs(s_pos[i + 1][1] - s_pos[i][1])
                        + abs(s_pos[i + 1][0] - s_pos[i][0])
                    )
                )
                if distance <= math.sqrt(2):
                    count += 1
            return count > (len(robots) // 2) + 1

        seconds = 0
        while True:
            positions_post_second = []
            grid = [["."] * cols for _ in range(rows)]
            for robot in robots:
                c, r, vc, vr = robot
                nr, nc = (r + seconds * vr) % rows, (c + seconds * vc) % cols
                grid[nr][nc] = "#"
                positions_post_second.append((nr, nc))
            if more_than_half_are_adjacent(positions=positions_post_second):
                break
            seconds += 1

        for line in grid:
            print("".join(line))

        with open(f"after_{seconds}_seconds_{rows}_{cols}.txt", "w+") as f:
            for line in grid:
                f.write(f"{''.join(line)}\n")
        return seconds


timer_start = time.perf_counter()
print(
    find_the_easter_egg(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_14"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
