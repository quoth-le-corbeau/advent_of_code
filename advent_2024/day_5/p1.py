import time
import pathlib


def sum_middle_pages(file_path: str):
    RENAME = _sum_middle_pages(file=file_path)
    pass


def _sum_middle_pages(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read()
        print(lines)


start = time.perf_counter()
print(
    sum_middle_pages(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_5"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

# start = time.perf_counter()
# print(sum_middle_pages(str((pathlib.Path(__file__).resolve().parents[2] / "my_inputs/2024/day_5" / "input.txt"))))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
