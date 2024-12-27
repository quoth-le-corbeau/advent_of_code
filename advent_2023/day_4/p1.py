import time
import re
import pathlib


def get_scratchcard_points(file: str) -> int:
    return _get_scratchcard_points(file=file)


def _get_scratchcard_points(file: str) -> int:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        cards = puzzle_input.readlines()
        score = 0
        for card in cards:
            pipe_card = card.replace(":", "|")
            winning_numbers = set(map(int, re.findall(r"\d+", pipe_card.split("|")[1])))
            card_numbers = set(map(int, re.findall(r"\d+", pipe_card.split("|")[2])))
            matches = len(winning_numbers.intersection(card_numbers))
            points = 2 ** (matches - 1) if matches != 0 else 0
            score += points
        return score


timer_start = time.perf_counter()
print(
    get_scratchcard_points(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2023/day_4"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
timer_start = time.perf_counter()
print(
    get_scratchcard_points(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2023/day_4"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
