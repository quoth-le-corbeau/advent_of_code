from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_input(file_path: Path) -> list[int]:
    with open(file_path, "r") as puzzle_input:
        return list(map(int, puzzle_input.read().strip().splitlines()))


def _calculate_fuel(mass: int) -> int:
    return mass // 3 - 2


@timer
def part_one(file: str, day: int = 1, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    masses = _parse_input(file_path=input_file_path)
    total_fuel_requirement = 0
    for mass in masses:
        total_fuel_requirement += _calculate_fuel(mass)
    return total_fuel_requirement


# part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 1, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    masses = _parse_input(file_path=input_file_path)
    total_fuel_requirement = 0
    for mass in masses:
        while mass > 0:
            mass = _calculate_fuel(mass)
            if mass > 0:
                total_fuel_requirement += mass
    return total_fuel_requirement


# part_two(file="eg")
part_two(file="input")
