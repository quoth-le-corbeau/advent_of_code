from typing import Optional
import time
import pathlib
import pandas


def calculate_bingo_score(file_path: str):
    to_be_drawn_numbers, bingo_boards = _parse_bingo_game(file=file_path)
    winning_number, board_number, drawn_numbers = _get_winner_board_and_marked(
        numbers=to_be_drawn_numbers, boards=bingo_boards
    )
    unmarked_sum = _sum_unmarked_on_board(
        marked_numbers=drawn_numbers, board=bingo_boards[board_number]
    )
    if winning_number is not None:
        return winning_number * unmarked_sum
    else:
        raise RuntimeError("No Winning number found!")


def _sum_unmarked_on_board(marked_numbers: set[str], board: pandas.DataFrame) -> int:
    total = 0
    for _, row in board.iterrows():
        for row_item in row:
            if not row_item in marked_numbers:
                total += int(row_item)
    return total


def _get_winner_board_and_marked(
    numbers: list[str], boards: list[pandas.DataFrame]
) -> tuple[Optional[int], Optional[int], set[str]]:
    comparison_set = set(numbers[:4])
    for drawn_number in numbers:
        comparison_set.add(drawn_number)
        for board_number, board in enumerate(boards):
            for column_name in board:
                if set(board[column_name]).issubset(comparison_set):
                    return int(drawn_number), board_number, comparison_set
            for _, row in board.iterrows():
                if set(row).issubset(comparison_set):
                    return int(drawn_number), board_number, comparison_set
    return None, None, comparison_set


def _parse_bingo_game(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        to_be_drawn_numbers = puzzle_input.readline().strip().split(",")
        puzzle_input.readline()
        blocks = puzzle_input.read().split("\n\n")
        cards: list[list[list[str]]] = list()
        for block in blocks:
            card = list()
            for line in block.splitlines():
                card.append(line.strip().split())
            cards.append(card)
        bingo_cards = list()
        for card in cards:
            bingo_cards.append(
                pandas.DataFrame(card, columns=[str(i + 1) for i in range(len(card))])
            )
        return to_be_drawn_numbers, bingo_cards


start = time.perf_counter()
print(calculate_bingo_score("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(calculate_bingo_score("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
