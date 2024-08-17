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
    if set(passport.keys()) == _FIELDS or _FIELDS.difference(set(passport.keys())) == {
        "cid"
    }:
        return passport
    else:
        raise InvalidPassport()


start = time.perf_counter()
print(count_valid_passports("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(count_valid_passports("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
