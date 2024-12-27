import time
import pathlib


def RENAME_FUNC(file_path: str):
    RENAME = _RENAME_FUNC(file=file_path)
    pass


def _RENAME_FUNC(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read()
        print(lines)


timer_start = time.perf_counter()
print(
    RENAME_FUNC(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2019/day_7"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

# timer_start = time.perf_counter()
# print(RENAME_FUNC(str((pathlib.Path(__file__).resolve().parents[2] / "my_inputs/2019/day_7" / "input.txt"))))
# print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
