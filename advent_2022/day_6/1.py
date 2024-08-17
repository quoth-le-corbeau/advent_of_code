import time
import pathlib


def count_characters_until_marker_detected(file: str) -> int:
    data_stream = _get_data_stream(file=file)
    count = 0
    for i in range(4, len(data_stream), 1):
        last_four_characters = ""
        for x in range(-4, 0):
            last_four_characters += data_stream[i + x]
        if len(set(last_four_characters)) == 4:
            count = i
            break
    return count


def _get_data_stream(file: str) -> str:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        return puzzle_input.read()


start = time.perf_counter()
print(count_characters_until_marker_detected("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(count_characters_until_marker_detected("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
