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
def part_one(file: str, day: int = 6, year: int = 2019) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    orbit_map = _parse_orbit_map(file_path=input_file_path)
    checksum = 0
    for orbiter, orbited in orbit_map.items():
        checksum += 1
        current_key = orbited
        while current_key in orbit_map.keys():
            checksum += 1
            current_key = orbit_map[current_key]
    return checksum


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 6, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    orbit_map = _parse_orbit_map(file_path=input_file_path)
    from_san = []
    current_key = orbit_map["SAN"]
    from_san.append(current_key)
    while current_key in orbit_map.keys():
        current_key = orbit_map[current_key]
        from_san.append(current_key)
    current_key = orbit_map["YOU"]
    orbital_transfers = 1
    while current_key in orbit_map.keys():
        current_key = orbit_map[current_key]
        orbital_transfers += 1
        if current_key in from_san:
            orbital_transfers += from_san.index(current_key) - 1
            break
    return orbital_transfers


part_two(file="eg2")
part_two(file="input")
