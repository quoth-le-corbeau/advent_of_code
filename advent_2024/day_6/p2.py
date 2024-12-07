import time
import pathlib


def count_possible_loop_creators(file_path: str) -> int:
    start, col_bound, row_bound, grid = _parse_map(file=file_path)
    loop_count = 0
    for row_idx in range(row_bound):
        for col_idx in range(col_bound):
            if grid[row_idx][col_idx] != ".":
                continue
            grid[row_idx][col_idx] = "#"
            if _check_for_infinite_loop(
                start=start,
                altered_grid=grid,
                row_bound=row_bound,
                col_bound=col_bound,
            ):
                loop_count += 1
            grid[row_idx][col_idx] = "."
    return loop_count


def _check_for_infinite_loop(
    start: tuple[int, int],
    altered_grid: list[list[str]],
    row_bound: int,
    col_bound: int,
):
    row, col = start
    j, i = -1, 0
    visited = set()
    while True:
        if (row, col, j, i) in visited:
            return True
        visited.add((row, col, j, i))
        if not (0 <= row + j < row_bound and 0 <= col + i < col_bound):
            return False
        if altered_grid[row + j][col + i] == "#":
            i, j = -j, i
        else:
            row += j
            col += i


def _parse_map(file: str) -> tuple[tuple[int, int], int, int, list[list[str]]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        col_bound = len(lines)
        start = None
        row_bound = len(lines[0])
        for row, line in enumerate(lines):
            if len(line) == 0:
                pass
            for col, char in enumerate(line):
                if char == "^":
                    start = (row, col)
                else:
                    continue
        return start, col_bound, row_bound, [list(line) for line in lines]


start = time.perf_counter()
print(
    count_possible_loop_creators(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_6"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    count_possible_loop_creators(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_6"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
