import time
import pathlib
import re


def count_scratch_cards_and_copies(file: str) -> int:
    all_cards_won = _get_scratchcard_copies(file=file)
    total = 0
    for card, copies in all_cards_won.items():
        total += copies
    return total


def _get_scratchcard_copies(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        cards = puzzle_input.readlines()
        card_copies = {i + 1: 1 for i in range(len(cards))}
        for index, card in enumerate(cards):
            current_number_of_copies = card_copies[index + 1]
            pipe_card = card.replace(":", "|")
            winning_numbers = set(map(int, re.findall(r"\d+", pipe_card.split("|")[1])))
            card_numbers = set(map(int, re.findall(r"\d+", pipe_card.split("|")[2])))
            matches = len(winning_numbers.intersection(card_numbers))
            if matches > 0:
                for i in range(1, matches + 1):
                    card_copies[index + 1 + i] += current_number_of_copies
        return card_copies


start = time.perf_counter()
print(count_scratch_cards_and_copies("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(count_scratch_cards_and_copies("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
