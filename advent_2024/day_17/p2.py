import re
import time
import pathlib


"""
Chronospatial Computer Part II

Analyze the program:
    - look for the first _out 
        - e.g 5, 4: 
        - the result_1 of this must be the beginning of the program: 0
        - the operand is 4 so we look at register A's current value and do % 8 
        - deduce that result_1 at first output % 8 = 0
    look at the previous command(s)
        - e.g 0, 3
        - so register A current // 2 ** 3 == result_1 so (register_A start // 8) % 8 == 0  
        
"""


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
        print(f"Ignoring {operand} for legacy reasons")
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


def chronospatial_output_copy(file_path: str):
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().split("\n\n")
        registers = list(map(int, re.findall(r"\d+", lines[0])))
        program = list(map(int, re.findall(r"\d+", lines[1])))
        computer = Computer(
            register_A=registers[0], register_B=registers[1], register_C=registers[2]
        )
        output = computer.run(program)
        print(f"{program=}")
        print(f"{output=}")
        assert list(map(int, output.split(","))) == program


timer_start = time.perf_counter()
print(
    chronospatial_output_copy(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_17"
                / "eg_p2.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

# timer_start = time.perf_counter()
# print(
#    chronospatial_output_copy(
#        str(
#            (
#                pathlib.Path(__file__).resolve().parents[2]
#                / "my_inputs/2024/day_17"
#                / "input.txt"
#            )
#        )
#    )
# )
# print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
