import re
from pathlib import Path

from reusables import timer, INPUT_PATH


class Computer:
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
            return self.output[:-1]
        else:
            assert self.output == ""
            return self.output

    def _adv(self, operand: int):
        numerator = self.register_A
        denominator = 2 ** self.operand_map[operand]["combo"]()
        self.register_A = numerator // denominator

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

    def _bdv(self, operand):
        numerator = self.register_A
        denominator = 2 ** self.operand_map[operand]["combo"]()
        self.register_B = numerator // denominator

    def _cdv(self, operand: int):
        numerator = self.register_A
        denominator = 2 ** self.operand_map[operand]["combo"]()
        self.register_C = numerator // denominator


def _parse_input(file_path: Path) -> tuple[list[int], list[int]]:
    with open(Path(__file__).resolve().parents[2] / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().split("\n\n")
        registers = list(map(int, re.findall(r"\d+", lines[0])))
        program = list(map(int, re.findall(r"\d+", lines[1])))
        return registers, program


def chronospatial_output(file_path: Path) -> str:
    registers, program = _parse_input(file_path)
    computer = Computer(
        register_A=registers[0], register_B=registers[1], register_C=registers[2]
    )
    output = computer.run(program)
    return output


def chronospatial_output_reversed(file_path: Path):
    registers, program = _parse_input(file_path)
    assert registers[1] == registers[2] == 0
    # want to overwrite registers[0] with a value such that computer.run(program) -> program
    # 2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0


@timer
def part_one(file: str, year: int = 2024, day: int = 17):
    input_file_path = INPUT_PATH.format(year=year, day=day, file=file)
    print(f"day {day} p1 with {file}: ")
    print(chronospatial_output(file_path=input_file_path))


# part_one(file="eg")
# part_one(file="input")


@timer
def part_two(file: str, year: int = 2024, day: int = 17):
    input_file_path = INPUT_PATH.format(year=year, day=day, file=file)
    print(f"day {day} p2 with {file}: ")
    print(chronospatial_output_reversed(file_path=input_file_path))


# part_two(file="eg")
# part_two(file="input")
