import re
from pathlib import Path
from reusables import timer, INPUT_PATH


def _parse_input(file: str) -> tuple[tuple[int, int, int], list[int]]:
    path = Path(__file__).resolve().parents[2] / file
    with path.open(mode="r") as puzzle_input:
        a, b, c, *program = map(int, re.findall(r"\d+", puzzle_input.read()))
        return (a, b, c), program


def _run_program(a: int, b: int, c: int, program: list[int]) -> list[int]:
    def combo(operand: int) -> int:
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return a
        elif operand == 5:
            return b
        elif operand == 6:
            return c
        else:
            raise RuntimeError

    pointer = 0
    output = []
    while pointer < len(program):
        instruction = program[pointer]
        operand = program[pointer + 1]
        match instruction:
            case 0:
                a = a >> combo(operand)
            case 1:
                b = b ^ operand
            case 2:
                b = combo(operand) % 8
            case 3:
                if a != 0:
                    pointer = operand
                    continue
            case 4:
                b = b ^ c
            case 5:
                output.append(combo(operand) % 8)
            case 6:
                b = a >> combo(operand)
            case 7:
                c = a >> combo(operand)
        pointer += 2
    print(f"output for program: {program}: {output}")
    return output


@timer
def part_1(file: str, year: int = 2024, day: int = 17):
    input_file_path = INPUT_PATH.format(year=year, day=day, file=file)
    registers, program = _parse_input(file=input_file_path)
    a, b, c = registers
    _run_program(a=a, b=b, c=c, program=program)


part_1(file="input")


@timer
def part_2(file: str, year: int = 2024, day: int = 17):
    input_file_path = INPUT_PATH.format(year=year, day=day, file=file)
    _, program = _parse_input(file=input_file_path)
    _run_program(a=24, b=0, c=0, program=program)


part_2(file="input")
"""
prog: 2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0

b = a % 8
b = b ^ 5
c = a >> b
b = b ^ c
b = b ^ 6
a = a >> 3
out(b % 8)
if a != 0: jump to position 0

on the final iteration 0 <= a <= 7 so that a >> 3 = 0
and b % 8 needs to be 0 so the last three bits of b must be 0

try a == 3 bin 011
b = 3 bin 011
b = b ^ 5 = 011 ^ 101 = 110 = 6
c = a >> b shift a by 6 bits to the right = 0 
b = 6 ^ 0 = 6
b = 6 ^ 6 = 0
a = 0 (last 3 bits of 0 = 0)
out(b % 8) = 3

so in the last loop a needs to be 3 
so the result of a = a >> 3 is 3 so a = ...011xxx so minimum 24

"""


def check(a):
    b = a % 8
    b = b ^ 5
    c = a >> b
    b = b ^ c
    b = b ^ 6
    a = a >> 3
    print("check")
    print(b % 8)


print(check(a=24))
