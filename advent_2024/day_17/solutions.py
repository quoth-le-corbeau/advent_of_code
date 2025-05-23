import re
from pathlib import Path
from typing import Callable

from reusables import timer, INPUT_PATH


class ChronospatialComputer:
    def __init__(self, register_A: int, register_B: int, register_C: int):
        self.register_A = register_A
        self.register_B = register_B
        self.register_C = register_C
        self.output = ""
        self.operand_map = {
            0: {"combo": lambda: 0, "literal": 0},
            1: {"combo": lambda: 1, "literal": 1},
            2: {"combo": lambda: 2, "literal": 2},
            3: {"combo": lambda: 3, "literal": 3},
            4: {"combo": lambda: self.register_A, "literal": 4},
            5: {"combo": lambda: self.register_B, "literal": 5},
            6: {"combo": lambda: self.register_C, "literal": 6},
            7: {
                "combo": lambda: (_ for _ in ()).throw(
                    ValueError("Invalid combo for 7")
                ),
                "literal": 7,
            },
        }
        self.instruction_map = {
            0: self._adv,
            1: self._bxl,
            2: self._bst,
            3: self._jnz,
            4: self._bxc,
            5: self._out,
            6: self._bdv,
            7: self._cdv,
        }

    def run(self, program: list[int]) -> str:
        i = 0
        while i < len(program) - 1:
            if program[i] == 3 and self.register_A != 0:
                i = self._jnz(operand=program[i + 1])
                continue
            else:
                op_code, operand = program[i], program[i + 1]
                self.instruction_map[op_code](operand)
                i += 2
        if len(self.output) > 0:
            # print(f"output after program: {program} = {self.output}")
            return self.output[:-1]
        else:
            assert self.output == ""
            return self.output

    def _adv(self, operand: int):
        self.register_A = self.register_A >> self.operand_map[operand]["combo"]()

    def _bxl(self, operand: int):
        self.register_B = self.register_B ^ self.operand_map[operand]["literal"]

    def _bst(self, operand: int):
        self.register_B = self.operand_map[operand]["combo"]() % 8

    def _bxc(self, operand: int):
        # print(f"Ignoring {operand} for legacy reasons")
        self.register_B = self.register_B ^ self.register_C

    def _jnz(self, operand: int):
        return self.operand_map[operand]["literal"]

    def _out(self, operand: int):
        self.output += str(self.operand_map[operand]["combo"]() % 8) + ","
        return self.operand_map[operand]["combo"]() % 8

    def _bdv(self, operand):
        self.register_B = self.register_B >> self.operand_map[operand]["combo"]()

    def _cdv(self, operand: int):
        self.register_C = self.register_A >> self.operand_map[operand]["combo"]()

    def parse_program(self, program: list[int]):
        pairs = []
        for i in range(0, len(program) - 1, 2):
            op_code = program[i]
            operand = program[i + 1]
            if op_code == 5:
                continue
            elif op_code == 0:
                assert operand == 3
                continue
            operation = self.instruction_map[op_code]
            pairs.append((operation, operand))
        return pairs

    def reverse_engineer(
        self,
        program: list[int],
        program_pairs: list[tuple[Callable, int]],
        expected: int,
    ) -> int:
        if len(program) == 0:
            return expected
        for i in range(8):
            self.register_A = (expected << 3) + i
            for pair in program_pairs:
                f, o = pair[0], pair[1]
                f(o)
            if (self.register_B % 8) == program[-1]:
                previous = self.reverse_engineer(
                    program=program[:-1],
                    program_pairs=program_pairs,
                    expected=self.register_A,
                )
                if previous is None:
                    continue
                else:
                    return previous
            else:
                continue


def _parse_input(file_path: Path) -> tuple[list[int], list[int]]:
    with open(Path(__file__).resolve().parents[2] / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().split("\n\n")
        registers = list(map(int, re.findall(r"\d+", lines[0])))
        program = list(map(int, re.findall(r"\d+", lines[1])))
        return registers, program


def chronospatial_output(file_path: Path) -> str:
    registers, program = _parse_input(file_path)
    computer = ChronospatialComputer(
        register_A=registers[0], register_B=registers[1], register_C=registers[2]
    )
    output = computer.run(program)
    return output


@timer
def part_one(file: str, year: int = 2024, day: int = 17) -> str:
    input_file_path = INPUT_PATH.format(year=year, day=day, file=file)
    return chronospatial_output(file_path=input_file_path)


# part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, year: int = 2024, day: int = 17) -> int:
    input_file_path = INPUT_PATH.format(year=year, day=day, file=file)
    print(f"part 2 with {file}.txt: ")
    registers, program = _parse_input(file_path=input_file_path)
    a, b, c = registers
    computer = ChronospatialComputer(register_A=a, register_B=b, register_C=c)
    pairs = computer.parse_program(program=program)
    return computer.reverse_engineer(program=program, program_pairs=pairs, expected=0)


# part_two(file="eg_p2")
part_two(file="input")


# debugging
def check(a: int) -> None:
    b = a % 8
    b = b ^ 5
    c = a >> b
    b = b ^ c
    b = b ^ 6
    if a != 0:
        a = a >> 3
    print(f"check for a = {a}, b= {b}, c={c}: {b % 8}")
