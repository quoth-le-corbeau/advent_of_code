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


start = time.perf_counter()
print(find_first_freq_reached_twice("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(find_first_freq_reached_twice("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")