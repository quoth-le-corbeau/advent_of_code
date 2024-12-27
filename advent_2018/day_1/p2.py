import time
import pathlib


def find_first_freq_reached_twice(file_path: str) -> int:
    entries = _parse_entries(file=file_path)
    res = 0
    seen = set()
    i = 0
    while True:
        res += int(entries[i % len(entries)])
        if res in seen:
            return res
        seen.add(res)
        i += 1


def _parse_entries(file: str) -> list[str]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        return puzzle_input.read().splitlines()


timer_start = time.perf_counter()
print(
    find_first_freq_reached_twice(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2018/day_1"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    find_first_freq_reached_twice(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2018/day_1"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
