from pathlib import Path
import re
from reusables import timer, INPUT_PATH


def _parse_input(file_path: Path, n: int) -> list[list[int | str]]:
    with open(file_path, "r") as puzzle_input:
        rows = []
        for i, line in enumerate(puzzle_input.read().splitlines()):
            if i == n:
                symbols = list(re.findall("[+,*]", line))
                rows.append(symbols)
            else:
                nums = list(map(int, re.findall(r"\d+", line)))
                rows.append(nums)

    return _transform(rows)


def _transform(rows: list[list[int | str]]) -> list[list[int | str]]:
    math_problems = []
    for i in range(len(rows[0])):
        problem = []
        for row in rows:
            problem.append(row[i])
        math_problems.append(problem)
    return math_problems


def _solve(math_problems: list[list[int | str]], n: int) -> list[int]:
    s = []
    for mp in math_problems:
        op = mp[-1]
        match op:
            case "*":
                r = 1
                for i in range(n):
                    r *= mp[i]
                s.append(r)
            case "+":
                r = 0
                for i in range(n):
                    r += mp[i]
                s.append(r)
            case _:
                raise ValueError(f"Unknown op: {op}!")
    return s


@timer
def part_one(file: str, day: int = 6, year: int = 2025, n: int = 4):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    math_problems = _parse_input(file_path=input_file_path, n=n)
    print(math_problems)
    return sum(_solve(math_problems, n))


# part_one(file="eg", n=3)
# part_one(file="input", n=4)


def _parse_input_p2(file_path: Path, n: int) -> list[list[int | str]]:
    with open(file_path, "r") as puzzle_input:
        rows = []


@timer
def part_two(file: str, day: int = 6, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    return _parse_input_p2(file_path=input_file_path)


part_two(file="eg")
# part_two(file="input")
