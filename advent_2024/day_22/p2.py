import time
import pathlib


def _get_next_secret_number(secret_number: int) -> int:
    step_one = ((secret_number * 64) ^ secret_number) % 16777216
    step_two = ((step_one // 32) ^ step_one) % 16777216
    return ((step_two * 2048) ^ step_two) % 16777216


def find_best_sequence(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        secret_starts = list(map(int, puzzle_input.read().splitlines()))
        bananas_by_start = {secret_start: {} for secret_start in secret_starts}
        for secret_start in secret_starts:
            bananas = [int(str(secret_start)[-1])]
            secret = secret_start
            bananas.append(int(str(secret)[-1]))
            for _ in range(2000):
                secret = _get_next_secret_number(secret_number=secret)
                bananas.append(int(str(secret)[-1]))
            ordered_bananas = sorted(bananas, reverse=True)
            max_bananas = ordered_bananas[0:4]
            most_bananas = (max_bananas[0], -1)
            found = False
            for max_banana in max_bananas:
                if found:
                    break
                for i, banana in enumerate(bananas):
                    if banana == max_banana and i >= 3:
                        most_bananas = (banana, i)
                        found = True
                        break

            diffs = []
            for i in range(len(bananas) - 1):
                diffs.append(bananas[i + 1] - bananas[i])
            bananas_by_start[secret_start]["most_bananas"] = most_bananas
            bananas_by_start[secret_start]["diffs"] = diffs


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
