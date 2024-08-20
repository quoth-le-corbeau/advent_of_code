import time
import pathlib


def get_total_rock_paper_scissor_points(file: str) -> int:
    strategy_guides = _get_strategy_guides(file=file)
    points = 0
    for game in strategy_guides:
        elf_choice = game[0]
        my_choice = game[1]
        points += _points_per_choice(choice=my_choice)
        points += _win_or_draw(elf_choice=elf_choice, my_choice=my_choice)
    return points


def _win_or_draw(elf_choice: str, my_choice: str) -> int:
    if (
        (elf_choice == "A" and my_choice == "B")
        or (elf_choice == "B" and my_choice == "C")
        or (elf_choice == "C" and my_choice == "A")
    ):
        return 6
    elif elf_choice == my_choice:
        return 3
    else:
        return 0


def _points_per_choice(choice: str) -> int:
    if choice == "A":
        return 1
    elif choice == "B":
        return 2
    elif choice == "C":
        return 3
    else:
        raise ValueError("choice must be A B or C")


def _get_strategy_guides(file: str) -> list[tuple[str, str]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        games = puzzle_input.read().splitlines()
        strategy_guides = list()
        for game in games:
            game = game.replace("X", "A").replace("Y", "B").replace("Z", "C")
            strategy_guides.append((game.split()[0], game.split()[1]))
    return strategy_guides


start = time.perf_counter()
print(get_total_rock_paper_scissor_points("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(get_total_rock_paper_scissor_points("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
