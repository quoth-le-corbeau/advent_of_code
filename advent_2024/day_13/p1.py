import re
import time
import pathlib
import sympy as sym

"""
Claw Contraption Part I

    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400 

Goal: find the smallest linear combinations that make the totals
    i.e. find the smallest m and n such that 94m + 22n = 8400 and 34m + 67n = 5400
So we are solving simultaneous equations
... and since I am tight for time today I will use a library for this :-)

welcome sympy!
"""


def least_tokens_to_win(file_path: str):
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().split("\n\n")
        total_tokens = 0
        for line in lines:
            x_y_prize = list(map(int, re.findall(r"\d+", line)))
            print(x_y_prize)  # [94, 34, 22, 67, 8400, 5400]
            x, y = sym.symbols("x, y")
            eq1 = sym.Eq(x_y_prize[0] * x + x_y_prize[2] * y, x_y_prize[-2])
            eq2 = sym.Eq(x_y_prize[1] * x + x_y_prize[3] * y, x_y_prize[-1])
            result = sym.solve([eq1, eq2], (x, y))
            x_tokens, y_tokens = result[x], result[y]
            if not (
                isinstance(x_tokens, sym.core.numbers.Integer)
                and isinstance(y_tokens, sym.core.numbers.Integer)
            ):
                continue
            else:
                total_tokens += (x_tokens * 3) + y_tokens
        return total_tokens


timer_start = time.perf_counter()
print(
    least_tokens_to_win(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_13"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    least_tokens_to_win(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_13"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
