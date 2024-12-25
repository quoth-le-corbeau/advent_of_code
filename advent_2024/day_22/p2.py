import time
import pathlib


def _get_next_secret_number(secret_number: int) -> int:
    step_one = ((secret_number * 64) ^ secret_number) % 16777216
    step_two = ((step_one // 32) ^ step_one) % 16777216
    return ((step_two * 2048) ^ step_two) % 16777216


BANA = [3]
SEC = _get_next_secret_number(123)
BANA.append(int(str(SEC)[-1]))
for _ in range(8):
    SEC = _get_next_secret_number(SEC)
    BANA.append(int(str(SEC)[-1]))
print(f"{BANA=}")
DIFFS = []
for i in range(len(BANA) - 1):
    DIFFS.append(BANA[i + 1] - BANA[i])
print(f"{DIFFS=}")
MOST_BANA = max(BANA)
print(f"{MOST_BANA=}")
INDEXES_OF_MO = []
for n, B in enumerate(BANA):
    if B == MOST_BANA:
        INDEXES_OF_MO.append(n)
print(f"{INDEXES_OF_MO=}")
SEQ = []
for I in INDEXES_OF_MO:
    if I < 3:
        continue
    else:
        SEQ += DIFFS[I : I - 4 : -1]
print(f"{SEQ=}")


def find_best_sequence(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        secret_starts = list(map(int, puzzle_input.read().splitlines()))
        total = 0
        bananas = []
        for ss in secret_starts:
            secret = ss
            bananas.append(int(str(secret)[-1]))
            for _ in range(2000):
                secret = _get_next_secret_number(secret_number=secret)
                bananas.append(int(str(secret)[-1]))
            total += secret
        print(bananas)
        diffs = []
        for i in range(len(bananas) - 1):
            diffs.append(bananas[i + 1] - bananas[i])
        print(diffs)
        return total


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
