import re
import pathlib
import time


def get_possible_games(file: str) -> int:
    possible_games = _get_possible_games(file=file)
    return sum(possible_games)


def _get_possible_games(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.readlines()
        possible = []
        for line in lines:
            game_number = int(re.findall(r"Game \d+", line.strip())[0].split()[1])
            cubes = line.strip().split(":")[1]
            all_red = re.findall(r"\d+ red", cubes)
            all_green = re.findall(r"\d+ green", cubes)
            all_blue = re.findall(r"\d+ blue", cubes)
            impossible_red = _is_game_impossible(
                cubes_by_colour=all_red, max_for_colour=12
            )
            impossible_green = _is_game_impossible(
                cubes_by_colour=all_green, max_for_colour=13
            )
            impossible_blue = _is_game_impossible(
                cubes_by_colour=all_blue, max_for_colour=14
            )
            if any([impossible_red, impossible_green, impossible_blue]):
                continue
            else:
                possible.append(game_number)
        return possible


def _is_game_impossible(cubes_by_colour: list[str], max_for_colour: int):
    return any(int(entry.split()[0]) > max_for_colour for entry in cubes_by_colour)


start = time.perf_counter()
print(get_possible_games("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(get_possible_games("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
