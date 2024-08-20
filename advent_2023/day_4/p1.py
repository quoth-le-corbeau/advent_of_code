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


start = time.perf_counter()
print(get_scratchcard_points("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(get_scratchcard_points("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
