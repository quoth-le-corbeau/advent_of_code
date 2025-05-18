from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_input(file_path: Path) -> tuple[str, str]:
    with open(file_path, "r") as puzzle_input:
        return tuple(puzzle_input.read().strip().split("-"))


@timer
def part_one(file: str, day: int = 4, year: int = 2019) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    start_str, end_str = _parse_input(file_path=input_file_path)
    count = 0
    for n in range(int(start_str), int(end_str)):
        n_str = str(n)
        if len(set(n_str)) != len(n_str) and all(
            [int(n_str[i + 1]) - int(n_str[i]) >= 0 for i in range(len(n_str[:-1]))]
        ):
            count += 1
    return count


part_one(file="input")


@timer
def part_two(file: str, day: int = 4, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    print(f"part 2: {_parse_input(file_path=input_file_path)}")


part_two(file="input")
