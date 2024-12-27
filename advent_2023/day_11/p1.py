import time
import pathlib


def blah_blah(file: str):
    RENAME = _RENAME_FUNC(file=file)
    pass


def _RENAME_FUNC(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read()
        print(lines)


timer_start = time.perf_counter()
print(
    blah_blah(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2023/day_11"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
timer_start = time.perf_counter()
print(
    blah_blah(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2023/day_11"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
