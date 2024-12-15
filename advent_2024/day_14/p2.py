import time
import pathlib
import re

"""
Restroom Redoubt Part II

rows: 103, cols: 101 
get all inputs as a list of 4 integers: pr, pc, vr, vc
end position for each robot = (pr + (100 * vr)) % 103, (pc + (100 * vc)) % 101


"""


def find_the_easter_egg(file_path: str, rows: int, cols: int) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        robots = [list(map(int, re.findall(r"([-+]?\d+)", line))) for line in lines]

        def get_condition(positions: list[tuple[int, int]] = []) -> bool:
            lhs = [p for p in positions if p[1] < cols // 2]
            rhs = [p for p in positions if p[1] > cols // 2]
            return 0 < abs(len(lhs) - len(rhs)) <= 20

        i = 0
        condition = get_condition()  # conditions for most being arranged as xmas tree
        while not condition:
            positions_post_second = []
            grid = [["."] * cols for _ in range(rows)]
            for robot in robots:
                c, r, vc, vr = robot
                nr, nc = (r + i * vr) % rows, (c + i * vc) % cols
                grid[nr][nc] = "#"
                positions_post_second.append((nr, nc))
            condition = get_condition(positions=positions_post_second)
            i += 1

        with open(f"after_{i}_seconds_{rows}_{cols}.txt", "w+") as f:
            for line in grid:
                f.write(f"{line}\n")
        return i


# start = time.perf_counter()
# print(
#    find_the_easter_egg(
#        file_path=str(
#            (
#                pathlib.Path(__file__).resolve().parents[2]
#                / "my_inputs/2024/day_14"
#                / "eg.txt"
#            )
#        ),
#        rows=7,
#        cols=11,
#    )
# )
# print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    find_the_easter_egg(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_14"
                / "input.txt"
            )
        ),
        rows=103,
        cols=101,
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
