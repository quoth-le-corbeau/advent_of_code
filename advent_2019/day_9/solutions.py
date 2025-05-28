from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_file(file_path: Path) -> list[int]:
    with open(file_path, "r") as puzzle_input:
        return list(map(int, puzzle_input.read().strip().split(",")))


def _run(program: list[int], relative_base=0) -> int:
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
            param_1, param_2 = _get_param_values(
                pointer, mode_1, mode_2, program, relative_base
            )
            program[program[pointer + 3]] = param_1 + param_2
            pointer += 4
        elif opcode == 2:
            param_1, param_2 = _get_param_values(
                pointer, mode_1, mode_2, program, relative_base
            )
            program[program[pointer + 3]] = param_1 * param_2
            pointer += 4
        elif opcode == 3:
            input_code = int(input("input: "))
            if input_code not in [1]:
                print(f"invalid input code: {input_code}")
                exit(1)
            program[program[pointer + 1]] = input_code
            pointer += 2
        elif opcode == 4:
            param_1 = _get_value(mode_1, pointer, program, relative_base)
            output = param_1
            print(f"Output without halting: {output}")
            pointer += 2
        elif opcode == 5:
            param_1, param_2 = _get_param_values(
                pointer, mode_1, mode_2, program, relative_base
            )
            if param_1 != 0:
                pointer = param_2
            else:
                pointer += 3
        elif opcode == 6:
            param_1, param_2 = _get_param_values(
                pointer, mode_1, mode_2, program, relative_base
            )
            if param_1 == 0:
                pointer = param_2
            else:
                pointer += 3
        elif opcode == 7:
            param_1, param_2 = _get_param_values(
                pointer, mode_1, mode_2, program, relative_base
            )
            program[program[pointer + 3]] = 1 if param_1 < param_2 else 0
            pointer += 4
        elif opcode == 8:
            param_1, param_2 = _get_param_values(
                pointer, mode_1, mode_2, program, relative_base
            )
            program[program[pointer + 3]] = 1 if param_1 == param_2 else 0
            pointer += 4
        elif opcode == 9:
            param_value = program[pointer + 1]
            relative_base += param_value
            pointer += 2
        else:
            raise ValueError(f"Invalid opcode: {opcode}")
    if output == -1:
        raise ValueError("No diagnostic output")
    print("Final output after halting: ")
    return output


def _get_param_values(
    pointer: int, mode_1: str, mode_2: str, program: list[int], relative_base: int
) -> tuple[int, int]:
    param_1 = _get_value(
        mode=mode_1, pointer=pointer, program=program, relative_base=relative_base
    )
    param_2 = _get_value(
        mode=mode_2, pointer=pointer, program=program, relative_base=relative_base
    )
    return param_1, param_2


def _get_value(mode: str, pointer: int, program: list[int], relative_base: int) -> int:
    if mode == "0":
        param_value = program[program[pointer + 1]]
    elif mode == "1":
        param_value = program[pointer + 1]
    else:
        assert mode == "2"
        value = program[pointer + 1]
        param_value = program[relative_base + value]
    return param_value


@timer
def part_one(file: str, day: int = 9, year: int = 2019) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    program = _parse_file(input_file_path)
    print(f"{program=}")
    for _ in range(10000):
        program.append(0)
    return _run(program=program)


part_one(file="eg_copy")
part_one(file="eg_large")
part_one(file="eg_16")
part_one(file="input")


@timer
def part_two(file: str, day: int = 9, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    program = _parse_file(file_path=input_file_path)
    return _run(program=program)


# part_two(file="eg")
# part_two(file="input")
