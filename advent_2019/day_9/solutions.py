from collections import defaultdict
from pathlib import Path
from dataclasses import dataclass

from reusables import timer, INPUT_PATH


@dataclass(frozen=True, order=True)
class Parameter:
    mode: str
    raw_value: int

    def value(self, program: dict[int, int], relative_base: int) -> int:
        if self.mode == "0":
            # access the value stored at the raw value address
            return program[self.raw_value]
        elif self.mode == "1":
            # literal mode
            return self.raw_value
        elif self.mode == "2":
            # relative mode
            return program[self.raw_value + relative_base]
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


def _get_write_address(mode: str, raw_value: int, relative_base: int) -> int:
    if mode == "0":
        return raw_value
    elif mode == "2":
        return raw_value + relative_base
    else:
        raise ValueError(f"Invalid mode for write parameter: {mode}")


def _run(program: dict[int, int], relative_base: int = 0) -> int:
    output = -1
    pointer = 0
    while pointer < len(program) - 2:
        position_zero = str(program[pointer])
        while len(position_zero) < 5:
            position_zero = "0" + position_zero
        opcode = int(position_zero[-2:])
        mode_1 = position_zero[-3]
        mode_2 = position_zero[-4]
        mode_3 = position_zero[-5]
        if opcode == 99:
            break
        elif opcode == 1:
            parameter_1 = Parameter(mode=mode_1, raw_value=program[pointer + 1]).value(
                program=program, relative_base=relative_base
            )
            parameter_2 = Parameter(mode=mode_2, raw_value=program[pointer + 2]).value(
                program=program, relative_base=relative_base
            )
            write_address = _get_write_address(
                mode=mode_3, raw_value=program[pointer + 3], relative_base=relative_base
            )
            program[write_address] = parameter_1 + parameter_2
            pointer += 4
        elif opcode == 2:
            parameter_1 = Parameter(mode=mode_1, raw_value=program[pointer + 1]).value(
                program=program, relative_base=relative_base
            )
            parameter_2 = Parameter(mode=mode_2, raw_value=program[pointer + 2]).value(
                program=program, relative_base=relative_base
            )
            write_address = _get_write_address(
                mode=mode_3, raw_value=program[pointer + 3], relative_base=relative_base
            )
            program[write_address] = parameter_1 * parameter_2
            pointer += 4
        elif opcode == 3:
            input_code = int(
                input("input please (1 for test mode, 2 for sensor mode): ")
            )
            write_address = _get_write_address(
                mode_1, program[pointer + 1], relative_base
            )
            program[write_address] = input_code
            pointer += 2
        elif opcode == 4:
            parameter_1 = Parameter(mode=mode_1, raw_value=program[pointer + 1]).value(
                program=program, relative_base=relative_base
            )
            output = parameter_1
            print(f"output without halting: {output}")
            pointer += 2
        elif opcode == 5:
            parameter_1 = Parameter(mode=mode_1, raw_value=program[pointer + 1]).value(
                program=program, relative_base=relative_base
            )
            parameter_2 = Parameter(mode=mode_2, raw_value=program[pointer + 2]).value(
                program=program, relative_base=relative_base
            )
            if parameter_1 != 0:
                pointer = parameter_2
            else:
                pointer += 3
        elif opcode == 6:
            parameter_1 = Parameter(mode=mode_1, raw_value=program[pointer + 1]).value(
                program=program, relative_base=relative_base
            )
            parameter_2 = Parameter(mode=mode_2, raw_value=program[pointer + 2]).value(
                program=program, relative_base=relative_base
            )
            if parameter_1 == 0:
                pointer = parameter_2
            else:
                pointer += 3
        elif opcode == 7:
            parameter_1 = Parameter(mode=mode_1, raw_value=program[pointer + 1]).value(
                program=program, relative_base=relative_base
            )
            parameter_2 = Parameter(mode=mode_2, raw_value=program[pointer + 2]).value(
                program=program, relative_base=relative_base
            )
            write_address = _get_write_address(
                mode=mode_3, raw_value=program[pointer + 3], relative_base=relative_base
            )
            program[write_address] = 1 if parameter_1 < parameter_2 else 0
            pointer += 4
        elif opcode == 8:
            parameter_1 = Parameter(mode=mode_1, raw_value=program[pointer + 1]).value(
                program=program, relative_base=relative_base
            )
            parameter_2 = Parameter(mode=mode_2, raw_value=program[pointer + 2]).value(
                program=program, relative_base=relative_base
            )
            write_address = _get_write_address(
                mode=mode_3, raw_value=program[pointer + 3], relative_base=relative_base
            )
            program[write_address] = 1 if parameter_1 == parameter_2 else 0
            pointer += 4
        elif opcode == 9:
            parameter_1 = Parameter(mode=mode_1, raw_value=program[pointer + 1]).value(
                program=program, relative_base=relative_base
            )
            relative_base += parameter_1
            pointer += 2
        else:
            raise ValueError(f"Invalid opcode: {opcode}")
    if output == -1:
        raise ValueError("No diagnostic output")
    print("Final output after halting: ")
    return output


@timer
def both_parts(file: str, day: int = 9, year: int = 2019) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    program = _parse_file(input_file_path)
    print("=================================================================")
    print(f"running program with input file: {input_file_path} ----------->")
    return _run(program=program)


# both_parts(file="eg_copy")
# both_parts(file="eg_large")
# both_parts(file="eg_16")
both_parts(file="input")
