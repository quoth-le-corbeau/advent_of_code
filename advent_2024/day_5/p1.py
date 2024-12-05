import time
import pathlib
import re


def sum_middle_pages(file_path: str) -> int:
    rules, updates = _parse_input(file=file_path)
    print(f"{rules=}")
    print(f"{updates=}")
    order = _get_order(rules)
    middles = 0
    for update in updates:
        if _is_ordered(update, order):
            middles += update[len(update)//2 + 1]
    return middles

def _is_ordered(update: list[int], order: list[int]) -> bool:
    is_ordered = False
    return is_ordered
def _get_order(rules: list[tuple[int, int]]) -> list[int]:
    result = []
    return result


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
    sum_middle_pages(
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

# start = time.perf_counter()
# print(sum_middle_pages(str((pathlib.Path(__file__).resolve().parents[2] / "my_inputs/2024/day_5" / "input.txt"))))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
