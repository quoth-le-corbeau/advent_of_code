import time
import pathlib


def RENAME_FUNC(file_path: str):
    RENAME = _RENAME_FUNC(file=file_path)
    pass


def _RENAME_FUNC(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read()
        print(lines)


start = time.perf_counter()
RENAME_FUNC(
    str(
        (
            pathlib.Path(__file__).resolve().parents[2]
            / "my_inputs/2022/day_12"
            / "eg.txt"
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
RENAME_FUNC(
    str(
        (
            pathlib.Path(__file__).resolve().parents[2]
            / "my_inputs/2022/day_12"
            / "input.txt"
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
