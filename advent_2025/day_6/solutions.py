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
    subtotals = []
    for mp in math_problems:
        op = mp[-1]
        match op:
            case "*":
                r = 1
                for i in range(n):
                    r *= mp[i]
                subtotals.append(r)
            case "+":
                r = 0
                for i in range(n):
                    r += mp[i]
                subtotals.append(r)
            case _:
                raise ValueError(f"Unknown op: {op}!")
    return subtotals


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
        input_line: str = puzzle_input.read().replace(" ", ".")
        row_len: int = _find_row_length(input_line)
        rows: list[str] = [line.replace(" ", ".") for line in input_line.split("\n")]
        delimiter_indexes: list[int] = _find_delimiter_indexes(
            row_len=row_len, rows=rows
        )
        parsed: list[str] = _parse_vertical_blocks(
            indexes=delimiter_indexes, row_len=row_len, rows=rows
        )
        groups: list[list[str]] = _split_groups_at_op_lines(parsed)
    return groups


def _split_groups_at_op_lines(horizontal: list[str]) -> list[list[str]]:
    groups = []
    start_index = 0
    for i, line in enumerate(horizontal):
        if "+" in line or "*" in line:
            group = horizontal[start_index : i + 1]
            groups.append(group)
            start_index = i + 1
    return groups


def _parse_vertical_blocks(
    indexes: list[int], row_len: int, rows: list[str]
) -> list[str]:
    parsed = []
    current_i = 0
    for i, index in enumerate(indexes):
        for row in rows:
            to_append = row[current_i:index]
            parsed.append(to_append)
        current_i = index
    for row in rows:
        to_append = row[current_i:]
        parsed.append(to_append)
    return parsed


def _find_delimiter_indexes(row_len: int, rows: list[str]) -> list[int]:
    indexes = []
    for i in range(row_len):
        if all(row[i] == "." for row in rows):
            indexes.append(i)
    return indexes


def _find_row_length(line: str) -> int:
    i = 0
    while line[i] != "\n":
        i += 1
    return i


def _solve_p2(math_problems: list[list[str]]) -> list[int]:
    subtotals = []
    for mp in math_problems:
        subtotals.append(_cephalopod_transform_solve(mp))
    return subtotals


def _cephalopod_transform_solve(problem: list[str]) -> int:
    powers = len(problem[0])
    op_line = problem[-1]
    if "+" in op_line:
        op = "+"
    elif "*" in op_line:
        op = "*"
    else:
        raise ValueError("unknown op")
    assert op in ["+", "*"]
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
            continue
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
    return sum(_solve_p2(math_problems))


part_two(file="eg")
part_two(file="input")
