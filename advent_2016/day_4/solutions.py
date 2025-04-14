import re
from pathlib import Path
from collections import defaultdict

from reusables import timer, INPUT_PATH

ALPHABET_LENGTH = 26


def _count_real(file_path: Path) -> tuple[int, list[tuple[str, int]]]:
    with open(file_path, "r") as puzzle_input:
        real_sum = 0
        real_names = []
        for line in puzzle_input.read().strip().splitlines():
            number_pattern = r"\d+"
            checksum_pattern = r"\[(.*?)\]"
            sector_id = re.findall(pattern=number_pattern, string=line)[0]
            checksum = re.findall(pattern=checksum_pattern, string=line)[0]
            name_raw = line[: line.index(sector_id)]
            name = name_raw.replace("-", "")
            if _is_real(name=name, checksum=checksum):
                real_sum += int(sector_id)
                real_names.append((name_raw, int(sector_id)))
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


def _alphabet_shift(input_string: str, shift_steps: int) -> str:
    chars = list(input_string)
    new_chars = []
    for char in chars:
        if char == "-":
            new_chars.append(" ")
            continue
        shifted_ord = ord(char) + (shift_steps % ALPHABET_LENGTH)
        if shifted_ord > ord("z"):
            shifted_ord -= ALPHABET_LENGTH
        elif shifted_ord < ord("a"):
            raise ValueError("somehow we subtracted from ord('a')")
        else:
            assert ord("a") <= shifted_ord <= ord("z")
        new_chars.append(chr(shifted_ord))
    return "".join(new_chars)


@timer
def part_one(file: str, day: int = 4, year: int = 2016):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    total, _ = _count_real(file_path=input_file_path)
    return total


# part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 4, year: int = 2016) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    _, real_names_and_sector_ids = _count_real(file_path=input_file_path)
    for pair in real_names_and_sector_ids:
        name, sector_id = pair
        decrypted = _alphabet_shift(input_string=name, shift_steps=sector_id)
        if "north" in decrypted:
            print(f"{decrypted}")
            return sector_id
    return -1


# part_two(file="eg")
part_two(file="input")
