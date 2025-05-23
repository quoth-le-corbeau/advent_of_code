from pathlib import Path

from reusables import timer, INPUT_PATH

_AIR_CONDITIONER_UNIT_ID = 1
_THERMAL_RADIATOR_UNIT_ID = 5


def _parse_file(file_path: Path) -> list[int]:
    with open(file_path, "r") as puzzle_input:
        return list(map(int, puzzle_input.read().strip().split(",")))


def _run_1(program: list[int], input_code: int) -> int:
    output = -1
    pointer = 0
    while pointer < len(program) - 4:
        position_zero = str(program[pointer])
        while len(position_zero) < 5:
            position_zero = "0" + position_zero
        opcode = int(position_zero[-2:])
        mode_1 = position_zero[-3]
        mode_2 = position_zero[-4]
        if opcode == 99:
            print("Final diagnostic output: ")
            break
        elif opcode == 1:
            param_1, param_2 = _get_param_values(pointer, mode_1, mode_2, program)
            program[program[pointer + 3]] = param_1 + param_2
            pointer += 4
        elif opcode == 2:
            param_1, param_2 = _get_param_values(pointer, mode_1, mode_2, program)
            program[program[pointer + 3]] = param_1 * param_2
            pointer += 4
        elif opcode == 3:
            program[program[pointer + 1]] = input_code
            pointer += 2
        elif opcode == 4:
            param_1 = (
                program[program[pointer + 1]] if mode_1 == "0" else program[pointer + 1]
            )
            output = param_1
            if output == 0:
                print(
                    f"Test at position {pointer} success! {round(((pointer + 1) / len(program)) * 100, ndigits=2)}%"
                )
            pointer += 2
        else:
            raise ValueError(f"Invalid opcode: {opcode}")
    if output == -1:
        raise ValueError("No diagnostic output")
    return output


def _run_2(program: list[int], input_code: int) -> int:
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
            print("Final diagnostic output: ")
            break
        elif opcode == 1:
            param_1, param_2 = _get_param_values(pointer, mode_1, mode_2, program)
            program[program[pointer + 3]] = param_1 + param_2
            pointer += 4
        elif opcode == 2:
            param_1, param_2 = _get_param_values(pointer, mode_1, mode_2, program)
            program[program[pointer + 3]] = param_1 * param_2
            pointer += 4
        elif opcode == 3:
            program[program[pointer + 1]] = input_code
            pointer += 2
        elif opcode == 4:
            param_1 = (
                program[program[pointer + 1]] if mode_1 == "0" else program[pointer + 1]
            )
            output = param_1
            if output == 0:
                print(
                    f"Test at position {pointer} success! {round(((pointer + 1) / len(program)) * 100, ndigits=2)}%"
                )
            pointer += 2
        elif opcode == 5:
            param_1, param_2 = _get_param_values(pointer, mode_1, mode_2, program)
            if param_1 != 0:
                pointer = param_2
            else:
                pointer += 3
        elif opcode == 6:
            param_1, param_2 = _get_param_values(pointer, mode_1, mode_2, program)
            if param_1 == 0:
                pointer = param_2
            else:
                pointer += 3
        elif opcode == 7:
            param_1, param_2 = _get_param_values(pointer, mode_1, mode_2, program)
            if param_1 < param_2:
                program[program[pointer + 3]] = 1
            else:
                program[program[pointer + 3]] = 0
            pointer += 4
        elif opcode == 8:
            param_1, param_2 = _get_param_values(pointer, mode_1, mode_2, program)
            if param_1 == param_2:
                program[program[pointer + 3]] = 1
            else:
                program[program[pointer + 3]] = 0
            pointer += 4
        else:
            raise ValueError(f"Invalid opcode: {opcode}")
    if output == -1:
        raise ValueError("No diagnostic output")
    return output


def _get_param_values(
    pointer: int, mode_1: str, mode_2: str, program: list[int]
) -> tuple[int, int]:
    param_1 = program[program[pointer + 1]] if mode_1 == "0" else program[pointer + 1]
    param_2 = program[program[pointer + 2]] if mode_2 == "0" else program[pointer + 2]
    return param_1, param_2


@timer
def part_one(file: str, day: int = 5, year: int = 2019) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    program = _parse_file(input_file_path)
    return _run_1(program=program, input_code=_AIR_CONDITIONER_UNIT_ID)


# part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 5, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    program = _parse_file(file_path=input_file_path)
    return _run_2(program=program, input_code=_THERMAL_RADIATOR_UNIT_ID)


# part_two(file="eg")
part_two(file="input")
