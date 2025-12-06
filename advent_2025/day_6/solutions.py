from pathlib import Path
import re
from reusables import timer, INPUT_PATH


def _parse_input(file_path: Path, n: int) -> list[list[int | str]]:
    rows = []
    with open(file_path, "r") as puzzle_input:
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
    return sum(_solve(math_problems, n))


part_one(file="eg", n=3)
part_one(file="input", n=4)


def _parse_input_p2(file_path: Path) -> list[list[str]]:
    with open(file_path, "r") as puzzle_input:
        lines = puzzle_input.read().replace(" ", ".")
        rows = [line.replace(" ", ".") for line in lines.split("\n")]
        row_len = _find_row_length(lines)
        delimiter_indexes = _find_delimiter_indexes(row_len, rows)
        parsed = _parse_vertical_blocks(
            indexes=delimiter_indexes, row_len=row_len, rows=rows
        )
        groups = _build_groups(parsed)
    return groups


def _build_groups(horizontal: list[str]):
    groups = []
    current_i = 0
    for j, p in enumerate(horizontal):
        if "+" in p or "*" in p:
            group = horizontal[current_i : j + 1]
            groups.append(group)
            current_i = j + 1
    return groups


def _parse_vertical_blocks(
    indexes: list[int], row_len: int, rows: list[str]
) -> list[str]:
    parsed = []
    current_i = 0
    for i, index in enumerate(indexes):
        if i == len(indexes):
            end = row_len
        else:
            end = index
        for row in rows:
            to_append = row[current_i:end]
            parsed.append(to_append)
        current_i = index
    return parsed


def _find_delimiter_indexes(row_len, rows):
    delimiter_indexes = []
    for i in range(row_len):
        if all(row[i] == "." for row in rows):
            delimiter_indexes.append(i)
    return delimiter_indexes


def _find_row_length(lines):
    i = 0
    while lines[i] != "\n":
        i += 1
    return i


def _solve_p2(math_problems: list[list[str]]) -> list[int]:
    s = []
    for mp in math_problems:
        s.append(_cephalopod_transform_solve(mp))
    return s


def _cephalopod_transform_solve(problem: list[str]) -> int:
    powers = len(problem[0])
    op_line = problem[-1]
    if "+" in op_line:
        op = "+"
    elif "*" in op_line:
        op = "*"
    else:
        raise ValueError("unknown op")
    try:
        assert op in ["+", "*"]
    except AssertionError:
        print("help")
    nums = []
    for i in range(powers):
        n = ""
        for prob in problem[:-1]:
            n += prob[powers - i - 1]
        nums.append(n)
    actually_nums = []
    for n in nums:
        try:
            actually_nums.append(int(n.replace(".", "")))
        except (ValueError, TypeError):
            print(f"TypeError:{n}")
    print(f"{actually_nums=}")
    return _cephalopod_solve(actually_nums, op)


def _cephalopod_solve(nums: list[int], op: str) -> int:
    match op:
        case "*":
            r = 1
            for n in nums:
                r *= n

        case "+":
            r = 0
            for n in nums:
                r += n
        case _:
            raise ValueError(f"unknown op: {op}")
    return r


@timer
def part_two(file: str, day: int = 6, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    math_problems = _parse_input_p2(file_path=input_file_path)
    print(f"{math_problems=}")
    return sum(_solve_p2(math_problems))


# part_two(file="eg")
part_two(file="input")
print(f"solution: {10442199702583 + 477 + 7737}")
