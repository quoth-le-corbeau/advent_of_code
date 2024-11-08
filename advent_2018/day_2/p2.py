import time
import pathlib


def get_common_box_id_letters(file_path: str) -> str:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        box_ids = puzzle_input.read().splitlines()
        for i, box_id in enumerate(box_ids):
            letters = box_id.split()
            print(letters)
            for b_id in box_ids[i + 1 :]:
                pass


start = time.perf_counter()
print(get_common_box_id_letters("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(get_common_box_id_letters("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
