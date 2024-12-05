import time
import pathlib
import re


def sum_middle_pages_with_brute_force(file_path: str) -> int:
    rules, updates = _parse_input(file=file_path)
    middles = 0
    for update in updates:
        if len(update) == 0:
            continue
        ordered = True
        for i, n in enumerate(update):
            if not ordered:
                break
            relevant_rules = [rule for rule in rules if n == rule[1]]
            for other in update[i + 1 :]:
                if any([other == rule[0] for rule in relevant_rules]):
                    ordered = False
                    break
        if ordered:
            middles += update[len(update) // 2]
    return middles


def _parse_input(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read()
        rules, updates = lines.split("\n\n")
        rules = [
            (int(rule.split("|")[0]), int(rule.split("|")[1]))
            for rule in rules.split("\n")
        ]
        updates = [
            list(map(int, re.findall(r"(\d+)", line))) for line in updates.split("\n")
        ]
        return rules, updates


start = time.perf_counter()
print(
    sum_middle_pages_with_brute_force(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_5"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    sum_middle_pages_with_brute_force(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_5"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
