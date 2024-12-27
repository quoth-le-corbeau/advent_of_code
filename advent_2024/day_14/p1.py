import time
import pathlib
import re

"""
Restroom Redoubt Part I

rows: 103, cols: 101 
get all inputs as a list of 4 integers: pr, pc, vr, vc
end position for each robot = (pr + (100 * vr)) % 103, (pc + (100 * vc)) % 101


"""


def calculate_safety_factor(file_path: str, rows: int, cols: int) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        end_positions = list()
        for line in lines:
            c, r, vc, vr = list(map(int, re.findall(r"([-+]?\d+)", line)))
            end_position = (r + (100 * vr)) % rows, (c + (100 * vc)) % cols
            end_positions.append(end_position)
        top_left = [
            position
            for position in end_positions
            if position[0] in range(0, rows // 2)
            and position[1] in range(0, cols // 2)
            and not (position[0] == rows // 2 or position[1] == cols // 2)
        ]
        top_right = [
            position
            for position in end_positions
            if position[0] in range(0, rows // 2)
            and position[1] in range(cols // 2, cols)
            and not (position[0] == rows // 2 or position[1] == cols // 2)
        ]
        bottom_left = [
            position
            for position in end_positions
            if position[0] in range(rows // 2, rows)
            and position[1] in range(0, cols // 2)
            and not (position[0] == rows // 2 or position[1] == cols // 2)
        ]
        bottom_right = [
            position
            for position in end_positions
            if position[0] in range(rows // 2, rows)
            and position[1] in range(cols // 2, cols)
            and not (position[0] == rows // 2 or position[1] == cols // 2)
        ]
        return len(top_left) * len(top_right) * len(bottom_left) * len(bottom_right)


timer_start = time.perf_counter()
print(
    calculate_safety_factor(
        file_path=str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_14"
                / "eg.txt"
            )
        ),
        rows=7,
        cols=11,
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    calculate_safety_factor(
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
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
