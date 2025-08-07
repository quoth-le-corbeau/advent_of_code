from pathlib import Path

from reusables import timer, INPUT_PATH

SCREEN_SIZE = (50, 6)
EG_SCREEN_SIZE = (7, 3)


def _parse_instructions(file_path: Path) -> list[str]:
    with open(file_path, "r") as puzzle_input:
        return puzzle_input.read().strip().splitlines()


def _pprint_grid(pixels: list[tuple[int, int]], screen_size: tuple[int, int]) -> None:
    grid = [["."] * screen_size[0]] * screen_size[1]
    print(grid)


@timer
def part_one(file: str, screen_size: tuple[int, int], day: int = 8, year: int = 2016):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    instructions = _parse_instructions(file_path=input_file_path)
    print(f"{instructions=}")
    _pprint_grid(pixels=[], screen_size=screen_size)


part_one(file="eg", screen_size=EG_SCREEN_SIZE)
part_one(file="input", screen_size=SCREEN_SIZE)


@timer
def part_two(file: str, day: int = 8, year: int = 2016):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    print(f"part 2: {_parse_instructions(file_path=input_file_path)}")


part_two(file="eg")
part_two(file="input")
