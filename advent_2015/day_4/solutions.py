from pathlib import Path
import hashlib
from multiprocessing import Pool

from reusables import timer, INPUT_PATH

"""
Unfortunately, because MD5 is deliberately designed to behave like a pseudo-random function, 
there’s no mathematical shortcut to predict where a hash will begin with certain zeroes. 
In other words:
There’s no algorithm faster than brute-force (in the cryptographic sense) 
for finding MD5 values with a given prefix pattern.

Parallelization

MD5 computations are independent per candidate integer — perfect for parallel execution.
...wish I knew how to do this!
"""


def _find_n_zeroes_hash(day: int, file: str, year: int, n: int) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    with open(input_file_path, "r") as puzzle_input:
        input_secret: str = puzzle_input.read().strip()
    md5_hex: str = ""
    i = 0
    encoded_secret = input_secret.encode()
    while md5_hex[:n] != "0" * n:
        md5_hex = hashlib.md5(string=encoded_secret + str(i).encode()).hexdigest()
        i += 1
    return i - 1


@timer
def part_one(file: str, day: int = 4, year: int = 2015) -> int:
    """Brute Force version"""
    return _find_n_zeroes_hash(file=file, day=day, year=year, n=5)


# part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 4, year: int = 2015):
    return _find_n_zeroes_hash(file=file, day=day, year=year, n=6)


# part_two(file="eg")
part_two(file="input")
