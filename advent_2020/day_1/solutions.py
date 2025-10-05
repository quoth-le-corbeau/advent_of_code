from pathlib import Path

from reusables import timer, INPUT_PATH


def _find_target_pair(file_path: Path) -> int:
    with open(file_path, "r") as puzzle_input:
        numbers = [int(line) for line in puzzle_input.read().strip().splitlines()]
        seen = set()
        for number in numbers:
            target = 2020 - number
            if target in seen:
                return number * target
            seen.add(number)
        raise RuntimeError(f"Could not find a solution for {file_path}")


def _find_target_triple(file_path: Path) -> int:
    with open(file_path, "r") as puzzle_input:
        numbers = [int(line) for line in puzzle_input.read().strip().splitlines()]
        for i, number in enumerate(numbers):
            seen = set()
            target = 2020 - number
            for n in numbers[i + 1 :]:
                compliment = target - n
                if compliment in seen:
                    return n * compliment * number
                seen.add(n)

        raise RuntimeError(f"Could not find a solution for {file_path}")


@timer
def part_one(file: str, day: int = 1, year: int = 2020) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    return _find_target_pair(file_path=input_file_path)


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 1, year: int = 2020) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    return _find_target_triple(file_path=input_file_path)


part_two(file="eg")
part_two(file="input")
