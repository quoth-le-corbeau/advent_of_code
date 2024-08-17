import time
import pathlib
import math


def find_winners_product_2(file: str):
    game = _parse_games(file=file)
    return _find_winning_combinations(game=game)


def _find_winning_combinations(game: tuple[int, int]) -> int:
    time, distance = game
    discriminant = time**2 - (4 * distance)
    lower_root = math.floor((time - math.sqrt(discriminant)) / 2)
    upper_root = math.ceil((time + math.sqrt(discriminant)) / 2)
    return upper_root - lower_root - 1


def _parse_games(file: str) -> tuple[int, int]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        time_line = puzzle_input.readline()
        time = "".join(time_line.split(":")[1].strip().split())
        distance_line = puzzle_input.readline()
        distance = "".join(distance_line.split(":")[1].strip().split())
        return int(time), int(distance)


start = time.perf_counter()
print(find_winners_product_2("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(find_winners_product_2("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
