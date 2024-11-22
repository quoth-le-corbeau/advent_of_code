import time
import pathlib


def get_common_box_id_letters(file_path: str) -> str:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        box_ids = puzzle_input.read().splitlines()
        for i, box_id in enumerate(box_ids):
            box_dict = {k: box_id[k] for k in range(len(box_id))}
            for remaining_id in box_ids[i + 1 :]:
                remaining_dict = {k: remaining_id[k] for k in range(len(remaining_id))}
                diff = set(box_dict.items()) - set(remaining_dict.items())
                if len(diff) == 1:
                    print(type(diff))
                    index, _ = diff.pop()
                    print(f"{index}")
                    print(f"{box_id}")
                    return box_id[:index] + box_id[index:]



start = time.perf_counter()
print(get_common_box_id_letters("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(get_common_box_id_letters("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
