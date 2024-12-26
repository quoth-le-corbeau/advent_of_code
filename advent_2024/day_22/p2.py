import time
import pathlib
from collections import defaultdict

"""
Monkey Market Part II

create a dictionary with the secret starts as keys
the values are dictionaries storing the bananas and the diffs list
create a sequence-banana defaultdict(list) 
which collects all four-digit sequences as keys
where the corresponding value is a tuple
the number of bananas at the index of the sequence's end 
from the bananas list is stored in position 0 of the tuple
and the number of the buyer is stored in position 1
making sure to only take one bunch of bananas from each buyer 
return the largest sum of bananas

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
        all_diffs = [diffs_by_start[s]["diffs"] for s in diffs_by_start]
        all_bananas = [diffs_by_start[s]["bananas"] for s in diffs_by_start]
        bananas_by_sequence = defaultdict(list)
        for j, diff_list in enumerate(all_diffs):
            for i in range(len(all_diffs[j]) - 3):
                sequence = tuple(diff_list[i : i + 4])
                bananas_by_sequence[sequence].append((all_bananas[j][i + 4], j))
        max_bananas = 0
        for seq, banana_secrets in bananas_by_sequence.items():
            total = 0
            seen_buyers = set()
            for banana_secret in banana_secrets:
                buyer = banana_secret[1]
                bananas = banana_secret[0]
                if buyer in seen_buyers:
                    # Each buyer only wants to buy one hiding spot,
                    # so after the hiding spot is sold, the monkey will move on to the next buyer.
                    continue
                else:
                    total += bananas
                    seen_buyers.add(buyer)
            if total > max_bananas:
                max_bananas = total
        return max_bananas


start = time.perf_counter()
print(
    find_best_sequence(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_22"
                / "eg2.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    find_best_sequence(
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
