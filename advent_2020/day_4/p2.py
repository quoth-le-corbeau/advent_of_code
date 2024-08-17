from typing import List, Dict
import time
import pathlib

_FIELDS = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid",
}

_EYE_COLOURS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

class InvalidPassport(Exception):
    pass


def count_valid_passports(file_path: str) -> int:
    passports = _get_passports(file=file_path)
    return len(passports)


def _get_passports(file: str) -> List[Dict[str, str]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().split("\n\n")
        passports: List[Dict[str, str]] = list()
        for line in lines:
            try:
                passports.append(_make_valid_passport(fields_string=line))
            except InvalidPassport:
                continue
        return passports


def _make_valid_passport(fields_string: str) -> Dict[str, str]:
    fields = fields_string.replace("\n", " ").strip().split(" ")
    if len(fields) < 7:
        raise InvalidPassport()
    passport = dict()
    for field in fields:
        assert len(field.split(":")) == 2
        passport[field.split(":")[0]] = field.split(":")[1]
    if (
        set(passport.keys()) == _FIELDS
        or _FIELDS.difference(set(passport.keys())) == {"cid"}
    ) and _passport_is_valid(passport=passport):
        return passport
    else:
        raise InvalidPassport()


def _passport_is_valid(passport: Dict[str, str]) -> bool:
    if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
        return False
    if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
        return False
    if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
        return False
    if len(passport["pid"]) != 9:
        return False
    if passport["ecl"] not in _EYE_COLOURS or len(passport["ecl"]) != 3:
        return False
    if len(passport["hcl"]) != 7 or passport["hcl"][0] != "#":
        return False
    height = passport["hgt"]
    units = height[-2:]
    try:
        value = int(height[:-2])
    except ValueError:
        raise InvalidPassport
    assert units in ["in", "cm"]
    if units == "in" and (value < 59 or value > 76):
        return False
    elif units == "cm" and (value < 150 or value > 193):
        return False
    return True


start = time.perf_counter()
print(count_valid_passports("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(count_valid_passports("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
