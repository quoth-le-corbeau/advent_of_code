import re
from pathlib import Path
from collections import defaultdict

from reusables import timer, INPUT_PATH


def _count_real(file_path: Path) -> tuple[int, list[str]]:
    with open(file_path, "r") as puzzle_input:
        real_sum = 0
        real_names = []
        for line in puzzle_input.read().strip().splitlines():
            number_pattern = r"\d+"
            checksum_pattern = r"\[(.*?)\]"
            sector_id = re.findall(pattern=number_pattern, string=line)[0]
            checksum = re.findall(pattern=checksum_pattern, string=line)[0]
            name = line[: line.index(sector_id)].replace("-", "")
            if _is_real(name=name, checksum=checksum):
                real_sum += int(sector_id)
                real_names.append(name)
        return real_sum, real_names


def _is_real(name: str, checksum: str) -> bool:
    count_look_up = defaultdict(set)
    for char in name:
        count_look_up[name.count(char)].add(char)
    calculated_full_checksum = ""
    for count in sorted(count_look_up, reverse=True):
        chars = count_look_up[count]
        calculated_full_checksum += "".join(sorted(list(chars)))
    calculated_checksum = calculated_full_checksum[:5]
    return calculated_checksum == checksum


@timer
def part_one(file: str, day: int = 4, year: int = 2016):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    total, real_names = _count_real(file_path=input_file_path)
    return total


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 4, year: int = 2016):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    total, real_names = _count_real(file_path=input_file_path)
    print(real_names)


part_two(file="eg")
part_two(file="input")
