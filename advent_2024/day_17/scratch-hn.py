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

    return output


@timer
def part_1(file: str, year: int = 2024, day: int = 17):
    input_file_path = INPUT_PATH.format(year=year, day=day, file=file)
    registers, program = _parse_input(file=input_file_path)
    a, b, c = registers
    print(
        f"part1: output for a={a}, b={b}, c={c}: {_run_program(a=a, b=b, c=c, program=program)}"
    )


part_1(file="input")


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

24 in binary is 11000
so to have 24 in A at the beginning of the penultimate loop we need ...11000xxx
for example 11000000 128 + 64 = 192 (check works ;-) 

so so far we know that in round:
16/6 a = 3 (b011) then 3 << 3 = 24
15/16 a = 24 (b11000) then 24 << 3 = 192 
14/16 a = 192  (b11000000) then 192 << 3 = 1536 
So try 1536 + (0-8)
13/16 1538
12/16 12304 works 
"""


def _reverse_engineer(program: list[int], expected: int) -> int:
    if len(program) == 0:
        return expected
    for i in range(8):
        a = (expected << 3) + i
        b = a % 8
        b = b ^ 5
        c = a >> b
        b = b ^ c
        b = b ^ 6
        if (b % 8) == program[-1]:
            previous = _reverse_engineer(program[:-1], expected=a)
            if previous is None:
                continue
            print(f"a = {a}")
            return previous


@timer
def part_2(file: str, year: int = 2024, day: int = 17):
    input_file_path = INPUT_PATH.format(year=year, day=day, file=file)
    _, program = _parse_input(file=input_file_path)
    print(program)
    # test_a = 3 (found manually)
    # test_a = 3 << 3
    # test_a = 12304 # works
    # test_a = 98434 # works 0, 3, 5, 5, 3, 0
    test_a = 12304  # not yet
    print(
        f"(Test A value: {test_a}): {_run_program(a=test_a, b=0, c=0, program=program)}"
    )
    print(f"part 2: {_reverse_engineer(program=program, expected=0)}")


part_2(file="input")
