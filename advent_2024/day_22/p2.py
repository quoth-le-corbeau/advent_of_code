import time
import pathlib
from collections import defaultdict

"""
Monkey Market Part II

create a dictionary with the secret starts as keys
the values are dictionaries storing the bananas and the diffs list
create a sequence-banana defaultdict(int)

now choose a diffs list BUT HOW BEST TO CHOOSE?
loop through it in groups of four i:i+4
find this sequence in all the other diffs lists if it exists
if the sequence is found break and return the last index in the sequence
    - this will be i+4 in the first diffs list and whatever in the other diff lists
get the banana value at that index in all the lists store it in the sequence-banana dict
if the sequence is not found in a diffs list then simply do not add any bananas to the total for that sequence

"""


def _get_next_secret_number(secret_number: int) -> int:
    step_one = ((secret_number * 64) ^ secret_number) % 16777216
    step_two = ((step_one // 32) ^ step_one) % 16777216
    return ((step_two * 2048) ^ step_two) % 16777216


def _get_price_diffs_by_start(
    secret_starts: list[int], _limit: int = 2000
) -> dict[int, dict[str, list[int]]]:
    bananas_by_start = {secret_start: {} for secret_start in secret_starts}
    for secret_start in secret_starts:
        bananas = []
        secret = secret_start
        bananas.append(int(str(secret)[-1]))
        for _ in range(_limit):
            secret = _get_next_secret_number(secret_number=secret)
            bananas.append(int(str(secret)[-1]))
        diffs = []
        for i in range(len(bananas) - 1):
            diffs.append(bananas[i + 1] - bananas[i])
        bananas_by_start[secret_start]["bananas"] = bananas
        bananas_by_start[secret_start]["diffs"] = diffs
    return bananas_by_start


def find_best_sequence(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        secret_starts = list(map(int, puzzle_input.read().splitlines()))
        diffs_by_start = _get_price_diffs_by_start(secret_starts)
        seq_bananas = defaultdict(int)
        all_diffs = [diffs_by_start[s]["diffs"] for s in diffs_by_start]
        all_bananas = [diffs_by_start[s]["bananas"] for s in diffs_by_start]


start = time.perf_counter()
print(
    find_best_sequence(
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

# start = time.perf_counter()
# print(
#    find_best_sequence(
#        str(
#            (
#                    pathlib.Path(__file__).resolve().parents[2]
#                    / "my_inputs/2024/day_22"
#                    / "input.txt"
#            )
#        )
#    )
# )
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
