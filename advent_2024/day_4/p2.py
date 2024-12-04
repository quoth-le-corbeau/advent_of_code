import time
import pathlib
import pandas


def find_x_mas(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        df = pandas.DataFrame([list(line) for line in puzzle_input.read().splitlines()])
        a_coordinates_criss = _bottom_left_to_top_right(df)
        a_coordinates_cross = _bottom_right_to_top_left(df)
        return len(set(a_coordinates_criss).intersection(a_coordinates_cross))


def _bottom_left_to_top_right(df: pandas.DataFrame) -> list[tuple[int, int]]:
    results = []
    for offset in range(-df.shape[0] + 1, df.shape[1]):
        diagonal = df.values.diagonal(offset)
        for i in range(len(diagonal) - 2):
            if (
                diagonal[i] == "M" and diagonal[i + 1] == "A" and diagonal[i + 2] == "S"
            ) or (
                diagonal[i] == "S" and diagonal[i + 1] == "A" and diagonal[i + 2] == "M"
            ):
                if offset < 0:
                    a_col_row_ref = 1 + i, abs(offset) + i + 1
                else:
                    a_col_row_ref = abs(offset) + i + 1, 1 + i
                results.append(a_col_row_ref)
    return results


def _bottom_right_to_top_left(df: pandas.DataFrame) -> list[tuple[int, int]]:
    results = []
    flipped_df = df.iloc[:, ::-1]
    for offset in range(-flipped_df.shape[0] + 1, flipped_df.shape[1]):
        diagonal = flipped_df.values.diagonal(offset)
        for i in range(len(diagonal) - 2):
            if (
                diagonal[i] == "M" and diagonal[i + 1] == "A" and diagonal[i + 2] == "S"
            ) or (
                diagonal[i] == "S" and diagonal[i + 1] == "A" and diagonal[i + 2] == "M"
            ):
                if offset < 0:
                    a_col_row_ref = len(df) - 1 - (i + 1), abs(offset) + i + 1
                else:
                    a_col_row_ref = (len(df) - 1 - offset) - i - 1, i + 1
                results.append(a_col_row_ref)
    return results


start = time.perf_counter()
print(
    find_x_mas(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_4"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    find_x_mas(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_4"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
