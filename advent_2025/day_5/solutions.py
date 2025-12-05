from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_input(file_path: Path):
    with open(file_path, "r") as puzzle_input:
        ingredient_ids, ingredients = puzzle_input.read().split("\n\n")
        all_ingredients = list(map(int, ingredients.strip().splitlines()))
        id_ranges = [
            (int(line.split("-")[0]), int(line.split("-")[1]))
            for line in ingredient_ids.strip().splitlines()
        ]
    return sorted(id_ranges, key=lambda x: x[0]), all_ingredients


@timer
def part_one(file: str, day: int = 5, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    id_ranges, ingredients = _parse_input(file_path=input_file_path)
    count = 0
    for i in ingredients:
        if any([a <= i <= b for a, b in id_ranges]):
            count += 1
    return count


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 5, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    id_ranges, _ = _parse_input(file_path=input_file_path)
    preliminary = id_ranges[-1][1] - id_ranges[0][0] + 1
    deltas = []
    for range_pair in zip(id_ranges[:-1], id_ranges[1:]):
        first, second = range_pair
        if second[0] > first[1]:
            deltas.append(second[0] - first[1] - 1)
    return preliminary - sum(deltas)


part_two(file="eg")
part_two(file="input")
# 315004568769605
