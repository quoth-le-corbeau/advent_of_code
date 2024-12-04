import time
import pathlib
import pandas

_X_MAS = ["MAS", "SAM"]


def find_xmas(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        df = pandas.DataFrame([list(line) for line in puzzle_input.read().splitlines()])
        count = 0
        _bottom_left_to_top_right(df)
        _bottom_right_to_top_left(df)
    return count


def _bottom_left_to_top_right(df: pandas.DataFrame) -> list[str]:
    diagonals = []
    for offset in range(-df.shape[0] + 1, df.shape[1]):
        diagonals.append(''.join(df.values.diagonal(offset)))
    for bl_tr in diagonals:
        print(f"{bl_tr=}")


def _bottom_right_to_top_left(df):
    diagonals = []
    flipped_df = df.iloc[:, ::-1]
    for offset in range(-flipped_df.shape[0] + 1, flipped_df.shape[1]):
        diagonals.append(''.join(flipped_df.values.diagonal(offset)))
    for br_tl in diagonals:
        print(f"{br_tl=}")


start = time.perf_counter()
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
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

#start = time.perf_counter()
#print(
#    find_xmas(
#        str(
#            (
#                    pathlib.Path(__file__).resolve().parents[2]
#                    / "my_inputs/2024/day_4"
#                    / "input.txt"
#            )
#        )
#    )
#)
#print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
