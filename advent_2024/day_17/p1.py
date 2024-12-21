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
        self.instruction_map = {0: self.adv, 1: self.bxl, 2: self.bst, 7: self.cdv}

    def adv(self, operand: int):
        numerator = self.register_A
        denominator = 2 ** self.operand_map[operand]["combo"]
        self.register_A = numerator // denominator

    def bxl(self, operand: int):
        self.register_B = self.register_B ^ self.operand_map[operand]["literal"]

    def bst(self, operand: int):
        self.register_B = self.operand_map[operand]["combo"] % 8

    def cdv(self, operand: int):
        numerator = self.register_A
        denominator = 2 ** self.operand_map[operand]["combo"]
        self.register_C = numerator // denominator


def chronospatial_output(file_path: str):
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read()
        print(lines)


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
