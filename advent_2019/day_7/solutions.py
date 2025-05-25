from pathlib import Path
from itertools import permutations
from collections import defaultdict

from reusables import timer, INPUT_PATH

_PHASE_SETTINGS = [0, 1, 2, 3, 4]


def _parse_file(file_path: Path) -> list[int]:
    with open(file_path, "r") as puzzle_input:
        return list(map(int, puzzle_input.read().strip().split(",")))


def _get_param_values(
    pointer: int, mode_1: str, mode_2: str, program: list[int]
) -> tuple[int, int]:
    param_1 = program[program[pointer + 1]] if mode_1 == "0" else program[pointer + 1]
    param_2 = program[program[pointer + 2]] if mode_2 == "0" else program[pointer + 2]
    return param_1, param_2


def _run(
    program: list[int],
    phase_input: int,
    previous_output: int = 0,
    phase_input_entered: bool = False,
) -> int:
    output = -1
    pointer = 0
    input_counter = 0
    while pointer < len(program) - 2:
        position_zero = str(program[pointer])
        while len(position_zero) < 5:
            position_zero = "0" + position_zero
        opcode = int(position_zero[-2:])
        mode_1 = position_zero[-3]
        mode_2 = position_zero[-4]
        if opcode == 99:
            print("got opcode 99")
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
            if input_counter > 2:
                raise ValueError("There should only be two inputs for each run!")
            if phase_input_entered:
                assert input_counter == 1
                program[program[pointer + 1]] = previous_output
            else:
                program[program[pointer + 1]] = phase_input
                phase_input_entered = True
                input_counter += 1
            pointer += 2
        elif opcode == 4:
            param_1 = (
                program[program[pointer + 1]] if mode_1 == "0" else program[pointer + 1]
            )
            output = param_1
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
            program[program[pointer + 3]] = 1 if param_1 < param_2 else 0
            pointer += 4
        elif opcode == 8:
            param_1, param_2 = _get_param_values(pointer, mode_1, mode_2, program)
            program[program[pointer + 3]] = 1 if param_1 == param_2 else 0
            pointer += 4
        else:
            raise ValueError(f"Invalid opcode: {opcode}")
    if output == -1:
        raise ValueError("No diagnostic output")
    return output


def _get_max_thrust_permutation(program: list[int]) -> tuple[int, tuple]:
    phase_settings_by_thrust = defaultdict(tuple)
    for phase_inputs in permutations(_PHASE_SETTINGS):
        next_input = 0
        fresh_program = program.copy()
        for phase_input in phase_inputs:
            output = _run(
                program=fresh_program,
                phase_input=phase_input,
                previous_output=next_input,
            )
            next_input = output
        phase_settings_by_thrust[next_input] = tuple(phase_inputs)
    max_thrust = int(max(phase_settings_by_thrust.keys()))
    return max_thrust, phase_settings_by_thrust[max_thrust]


@timer
def part_one(file: str, day: int = 7, year: int = 2019) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    max_possible_thrust, phase_setting = _get_max_thrust_permutation(
        program=_parse_file(input_file_path)
    )
    print(f"Max thrust obtained from phase setting: {phase_setting}")
    return max_possible_thrust


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 7, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    program = _parse_file(file_path=input_file_path)
    return _run(program=program)


# part_two(file="eg")
# part_two(file="input")
