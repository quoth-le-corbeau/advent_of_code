import re
import time
import pathlib


class Computer:
    def __init__(self, register_A: int, register_B: int, register_C: int):
        self.register_A = register_A
        self.register_B = register_B
        self.register_C = register_C
        self.output = ""
        self.operand_map = {
            0: {"combo": 0, "literal": 0},
            1: {"combo": 1, "literal": 1},
            2: {"combo": 2, "literal": 2},
            3: {"combo": 3, "literal": 3},
            4: {"combo": self.register_A, "literal": 4},
            5: {"combo": self.register_B, "literal": 5},
            6: {"combo": self.register_C, "literal": 6},
            7: {"combo": ValueError, "literal": 7},
        }
        self.instruction_map = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

    def parse_program(self, program: list[int]) -> list[tuple[int, int]]:
        sub_programs = []
        for i in range(len(program) - 1):
            if program[i] == 3 and self.register_A == 0:
                try:
                    sub_programs.append((program[i + 1], program[i + 2]))
                except IndexError:
                    raise IndexError("wtfk dude?")
            else:
                sub_programs.append((program[i], program[i + 1]))
        return sub_programs

    def run(self, program: list[int]) -> None:
        sub_programs = self.parse_program(program)
        for sub_program in sub_programs:
            op_code, operand = sub_program
            self.instruction_map[op_code](operand)

    def adv(self, operand: int):
        numerator = self.register_A
        denominator = 2 ** self.operand_map[operand]["combo"]
        self.register_A = numerator // denominator

    def bxl(self, operand: int):
        self.register_B = self.register_B ^ self.operand_map[operand]["literal"]

    def bst(self, operand: int):
        self.register_B = self.operand_map[operand]["combo"] % 8

    def bxc(self, operand: int):
        print(f"Ignoring {operand} for legacy reasons")
        self.register_B = self.register_B ^ self.register_C

    def jnz(self, operand: int):
        print(f"operand 3 with regist")
        pass

    def out(self, operand: int):
        self.output += str(self.operand_map[operand]["combo"] % 8) + ","

    def bdv(self, operand):
        numerator = self.register_A
        denominator = 2 ** self.operand_map[operand]["combo"]
        self.register_B = numerator // denominator

    def cdv(self, operand: int):
        numerator = self.register_A
        denominator = 2 ** self.operand_map[operand]["combo"]
        self.register_C = numerator // denominator


def chronospatial_output(file_path: str):
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().split("\n\n")
        registers = list(map(int, re.findall(r"\d+", lines[0])))
        program = list(map(int, re.findall(r"\d+", lines[1])))
        computer = Computer(
            register_A=registers[0], register_B=registers[1], register_C=registers[2]
        )
        computer.run(program)
        return computer.output


start = time.perf_counter()
print(
    chronospatial_output(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_17"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

# start = time.perf_counter()
# print(chronospatial_output(str((pathlib.Path(__file__).resolve().parents[2] / "my_inputs/2024/day_17" / "input.txt"))))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
