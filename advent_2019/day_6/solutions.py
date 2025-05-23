from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_orbit_map(file_path: Path) -> dict[str, str]:
    with open(file_path, "r") as puzzle_input:
        return {
            direct_orbiter: directly_orbited
            for directly_orbited, direct_orbiter in list(
                map(lambda x: x.split(")"), puzzle_input.read().strip().splitlines())
            )
        }


@timer
def part_one(file: str, day: int = 6, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    orbit_map = _parse_orbit_map(file_path=input_file_path)
    print(f"{orbit_map=}")
    print(orbit_map.keys())
    print(orbit_map.values())


part_one(file="eg")
# part_one(file="input")


@timer
def part_two(file: str, day: int = 6, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )


# part_two(file="eg")
# part_two(file="input")
