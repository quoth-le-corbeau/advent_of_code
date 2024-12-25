import time
import pathlib


def _get_next_secret_number(secret_number: int) -> int:
    step_one = ((secret_number * 64) ^ secret_number) % 16777216
    step_two = ((step_one // 32) ^ step_one) % 16777216
    return ((step_two * 2048) ^ step_two) % 16777216


def find_2000th_secret_number(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        secret_starts = list(map(int, puzzle_input.read().splitlines()))
        total = 0
        for ss in secret_starts:
            secret = ss
            for _ in range(2000):
                secret = _get_next_secret_number(secret_number=secret)
            print(f"secret_start: {ss}, 2000th: {secret}")
            total += secret
        return total


start = time.perf_counter()
print(
    find_2000th_secret_number(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_22"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    find_2000th_secret_number(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_22"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
