from pathlib import Path

from reusables import timer, INPUT_PATH


def _is_composed_of_repeated_digits(number_str: str) -> bool:
    num_length = len(number_str)
    mid = num_length // 2
    factor_pairs = [
        (i, num_length // i) for i in range(1, mid + 1) if num_length % i == 0
    ]
    for pair in factor_pairs:
        potential_pattern_length, required_repetitions = pair
        potential_pattern = number_str[:potential_pattern_length]
        if number_str == potential_pattern * required_repetitions:
            return True
    return False


@timer
def part_one(file: str, day: int = 2, year: int = 2025) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    with open(input_file_path, "r") as puzzle_input:
        invalid = []
        for r in puzzle_input.read().strip().split(","):
            s, e = int(r.split("-")[0]), int(r.split("-")[1])
            for n in range(s, e + 1):
                sn = str(n)
                mid = len(sn) // 2
                if sn[:mid] == sn[mid:]:
                    invalid.append(n)
    return sum(invalid)


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 2, year: int = 2025) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    with open(input_file_path, "r") as puzzle_input:
        invalid = []
        for r in puzzle_input.read().strip().split(","):
            s, e = int(r.split("-")[0]), int(r.split("-")[1])
            for n in range(s, e + 1):
                sn = str(n)
                if _is_composed_of_repeated_digits(sn):
                    invalid.append(n)
    return sum(invalid)


part_two(file="eg")
part_two(file="input")
