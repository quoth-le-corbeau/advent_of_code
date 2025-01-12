import time
import pathlib
import pandas

_XMAS = ["XMAS", "SAMX"]


def find_xmas(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        df = pandas.DataFrame([list(line) for line in puzzle_input.read().splitlines()])
        count = 0
        for _, row in df.iterrows():
            row_string = "".join(row)
            print(f"{row_string=}")
            for xmas in _XMAS:
                count += row_string.count(xmas)
        for _, col in df.transpose().iterrows():
            col_string = "".join(col)
            for xmas in _XMAS:
                count += col_string.count(xmas)
        for diagonal in _get_diagonals(df):
            for xmas in _XMAS:
                count += diagonal.count(xmas)
    return count


def _get_diagonals(df: pandas.DataFrame) -> list[str]:
    diagonals = []
    for offset in range(-df.shape[0] + 1, df.shape[1]):
        diagonals.append("".join(df.values.diagonal(offset)))
    flipped_df = df.iloc[:, ::-1]
    for offset in range(-flipped_df.shape[0] + 1, flipped_df.shape[1]):
        diagonals.append("".join(flipped_df.values.diagonal(offset)))
    return diagonals


timer_start = time.perf_counter()
print(
    find_xmas(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_4"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    find_xmas(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_4"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
