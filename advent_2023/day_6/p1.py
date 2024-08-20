import time
import pathlib
import functools
import math


def find_winners_product(file: str):
    games = _parse_games(file=file)
    ways_to_win = list()
    for game in games:
        ways_to_win.append(_find_winning_combinations(game=game))
    return functools.reduce(int.__mul__, ways_to_win)


def _find_winning_combinations(game: tuple[int, int]) -> int:
    time, distance = game
    discriminant = time**2 - (4 * distance)
    lower_root = math.floor((time - math.sqrt(discriminant)) / 2)
    upper_root = math.ceil((time + math.sqrt(discriminant)) / 2)
    return upper_root - lower_root - 1


def _parse_games(file: str) -> list[tuple[int, int]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        time_line = puzzle_input.readline()
        times = list(map(int, time_line.split(":")[1].strip().split()))
        distance_line = puzzle_input.readline()
        distances = list(map(int, distance_line.split(":")[1].strip().split()))
        return list(zip(times, distances))


start = time.perf_counter()
print(find_winners_product("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(find_winners_product("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
