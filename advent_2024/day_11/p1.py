import time
import pathlib

"""
Plutonian Pebbles Part I


read in the input string
create a function that takes in a string and outputs a new string
initialize a counter at 0
run the function 25 times
functionality:
create a dictionary of each element with its index as key:
    e.g. {
            1: "1250"
            2: "17"
            3: "0"
            4: "11"
            5: "1"
         }
        result should be
            1: "12 50"
            2: "1 7"
            3: "1"
            4: "1 1"
            5: "2024"
from this the next string is created:
"".join(val) for val in d.values()

finally return the length of the last output string.split(" ")

"""


def _apply_rules(row: str) -> str:
    stone_by_idx = {idx: stone for idx, stone in enumerate(row.split(" "))}
    new_stone_by_idx = {idx: "" for idx in stone_by_idx}
    for position, stone in stone_by_idx.items():
        if stone == "0":
            new_stone_by_idx[position] += "1"
        elif len(stone) % 2 == 0:
            new_stone_by_idx[position] += (
                stone[: len(stone) // 2] + " " + str(int(stone[len(stone) // 2 :]))
            )
        else:
            new_stone_by_idx[position] += str(int(stone) * 2024)
    new_string = ""
    for value in new_stone_by_idx.values():
        for v in value.split(" "):
            new_string += v
            new_string += " "
    return new_string.strip()


def count_the_stones_after_25(file_path: str):
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        row = puzzle_input.read().strip()

    counter = 0
    while counter < 25:
        row = _apply_rules(row)
        counter += 1
    return len(row.split(" "))


start = time.perf_counter()
print(
    count_the_stones_after_25(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_11"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    count_the_stones_after_25(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_11"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
