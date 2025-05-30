from collections import defaultdict
from pathlib import Path
from dataclasses import dataclass

from reusables import timer, INPUT_PATH


@dataclass(frozen=True, order=True)
class Parameter:
    mode: str
    raw_value: int

    def value(self, program: dict[int, int]) -> int:
        if self.mode == "0":
            # access the value stored at the raw value address
            return program[self.raw_value]
        elif self.mode == "1":
            # literal mode
            return self.raw_value
        else:
            raise NotImplementedError


def _parse_file(file_path: Path) -> dict[int, int]:
    with open(file_path, "r") as puzzle_input:
        software_memory_map = defaultdict(int)
        for i, value in enumerate(
            list(map(int, puzzle_input.read().strip().split(",")))
        ):
            software_memory_map[i] = value
        return software_memory_map


def _run(program: dict[int, int]) -> int:
    output = -1
    pointer = 0
    while pointer < len(program) - 2:
        position_zero = str(program[pointer])
        while len(position_zero) < 5:
            position_zero = "0" + position_zero
        opcode = int(position_zero[-2:])
        mode_1 = position_zero[-3]
        mode_2 = position_zero[-4]
        if opcode == 99:
            break
        elif opcode == 1:
            parameter_1 = Parameter(mode=mode_1, raw_value=program[pointer + 1]).value(
                program
            )
            parameter_2 = Parameter(mode=mode_2, raw_value=program[pointer + 2]).value(
                program
            )
            write_address = program[pointer + 3]
            program[write_address] = parameter_1 + parameter_2
            pointer += 4
        elif opcode == 2:
            parameter_1 = Parameter(mode=mode_1, raw_value=program[pointer + 1]).value(
                program
            )
            parameter_2 = Parameter(mode=mode_2, raw_value=program[pointer + 2]).value(
                program
            )
            write_address = program[pointer + 3]
            program[write_address] = parameter_1 * parameter_2
            pointer += 4
        elif opcode == 3:
            input_code = int(input("input (day 5 part 1 is 1, part 2 is 5): "))
            if input_code not in [1, 5]:
                print("^^^^^^^^read this prompt oida! ^^^^^^^^^^^^^^^^")
                exit(1)
            write_address = program[pointer + 1]
            program[write_address] = input_code
            pointer += 2
        elif opcode == 4:
            parameter_1 = Parameter(mode=mode_1, raw_value=program[pointer + 1]).value(
                program
            )
            output = parameter_1
            if output == 0:
                print(
                    f"Test at position {pointer} success! "
                    f"{round(((pointer + 1) / len(program)) * 100, ndigits=2)}%"
                )
            pointer += 2
        elif opcode == 5:
            parameter_1 = Parameter(mode=mode_1, raw_value=program[pointer + 1]).value(
                program
            )
            parameter_2 = Parameter(mode=mode_2, raw_value=program[pointer + 2]).value(
                program
            )
            if parameter_1 != 0:
                pointer = parameter_2
            else:
                pointer += 3
        elif opcode == 6:
            parameter_1 = Parameter(mode=mode_1, raw_value=program[pointer + 1]).value(
                program
            )
            parameter_2 = Parameter(mode=mode_2, raw_value=program[pointer + 2]).value(
                program
            )
            if parameter_1 == 0:
                pointer = parameter_2
            else:
                pointer += 3
        elif opcode == 7:
            parameter_1 = Parameter(mode=mode_1, raw_value=program[pointer + 1]).value(
                program
            )
            parameter_2 = Parameter(mode=mode_2, raw_value=program[pointer + 2]).value(
                program
            )
            write_address = program[pointer + 3]
            program[write_address] = 1 if parameter_1 < parameter_2 else 0
            pointer += 4
        elif opcode == 8:
            parameter_1 = Parameter(mode=mode_1, raw_value=program[pointer + 1]).value(
                program
            )
            parameter_2 = Parameter(mode=mode_2, raw_value=program[pointer + 2]).value(
                program
            )
            write_address = program[pointer + 3]
            program[write_address] = 1 if parameter_1 == parameter_2 else 0
            pointer += 4
        else:
            raise ValueError(f"Invalid opcode: {opcode}")
    if output == -1:
        raise ValueError("No diagnostic output")
    print("Diagnostic output: ")
    return output


@timer
def part_one(file: str, day: int = 5, year: int = 2019) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    program = _parse_file(input_file_path)
    return _run(program=program)


# part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 5, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    program = _parse_file(file_path=input_file_path)
    return _run(program=program)


# part_two(file="eg")
part_two(file="input")
