from pathlib import Path
from itertools import permutations
from collections import defaultdict
from typing import Optional

from reusables import timer, INPUT_PATH

_PHASE_SETTINGS = [0, 1, 2, 3, 4]
_PHASE_SETTINGS_FEEDBACK_MODE = [5, 6, 7, 8, 9]


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
            param_1, param_2 = _get_param_values(pointer, mode_1, mode_2, program)
            program[program[pointer + 3]] = param_1 + param_2
            pointer += 4
        elif opcode == 2:
            param_1, param_2 = _get_param_values(pointer, mode_1, mode_2, program)
            program[program[pointer + 3]] = param_1 * param_2
            pointer += 4
        elif opcode == 3:
            if phase_input_entered:
                program[program[pointer + 1]] = previous_output
            else:
                program[program[pointer + 1]] = phase_input
                phase_input_entered = True
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


def _run_feedback_mode(
    program: list[int],
    pointer: int = 0,
    input_signal: int = 0,
    phase_input: Optional[int] = None,
    waiting_for_signal: bool = False,
) -> tuple[list[int], int, int, bool]:
    output = input_signal
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
            param_1, param_2 = _get_param_values(pointer, mode_1, mode_2, program)
            program[program[pointer + 3]] = param_1 + param_2
            pointer += 4
        elif opcode == 2:
            param_1, param_2 = _get_param_values(pointer, mode_1, mode_2, program)
            program[program[pointer + 3]] = param_1 * param_2
            pointer += 4
        elif opcode == 3:
            if waiting_for_signal:
                program[program[pointer + 1]] = input_signal
            else:
                assert phase_input is not None
                program[program[pointer + 1]] = phase_input
                waiting_for_signal = True
            pointer += 2
        elif opcode == 4:
            param_1 = (
                program[program[pointer + 1]] if mode_1 == "0" else program[pointer + 1]
            )
            output = param_1
            pointer += 2
            return program, pointer, output, False
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

    return program, pointer, output, True


def _get_max_thrust_permutation_feedback_mode(program: list[int]) -> tuple[int, tuple]:
    phase_settings_by_thrust = defaultdict(tuple)
    for phase_inputs in permutations(_PHASE_SETTINGS_FEEDBACK_MODE):
        initial_input = 0
        a_software = program.copy()
        b_software = program.copy()
        c_software = program.copy()
        d_software = program.copy()
        e_software = program.copy()
        a_software, a_pointer, output_a, halted = _run_feedback_mode(
            program=a_software,
            phase_input=phase_inputs[0],
            input_signal=initial_input,
        )
        b_software, b_pointer, output_b, halted = _run_feedback_mode(
            program=b_software, phase_input=phase_inputs[1], input_signal=output_a
        )
        c_software, c_pointer, output_c, halted = _run_feedback_mode(
            program=c_software, phase_input=phase_inputs[2], input_signal=output_b
        )
        d_software, d_pointer, output_d, halted = _run_feedback_mode(
            program=d_software, phase_input=phase_inputs[3], input_signal=output_c
        )
        e_software, e_pointer, output_e, halted = _run_feedback_mode(
            program=e_software, phase_input=phase_inputs[4], input_signal=output_d
        )
        while True:
            a_software, a_pointer, output_a, halted = _run_feedback_mode(
                program=a_software,
                pointer=a_pointer,
                input_signal=output_e,
                waiting_for_signal=True,
            )
            if halted:
                break
            b_software, b_pointer, output_b, halted = _run_feedback_mode(
                program=b_software,
                pointer=b_pointer,
                input_signal=output_a,
                waiting_for_signal=True,
            )
            if halted:
                break
            c_software, c_pointer, output_c, halted = _run_feedback_mode(
                program=c_software,
                pointer=c_pointer,
                input_signal=output_b,
                waiting_for_signal=True,
            )
            if halted:
                break
            d_software, d_pointer, output_d, halted = _run_feedback_mode(
                program=d_software,
                pointer=d_pointer,
                input_signal=output_c,
                waiting_for_signal=True,
            )
            if halted:
                break
            e_software, e_pointer, output_e, halted = _run_feedback_mode(
                program=e_software,
                pointer=e_pointer,
                input_signal=output_d,
                waiting_for_signal=True,
            )
            if halted:
                break

        phase_settings_by_thrust[output_e] = tuple(phase_inputs)
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


# part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 7, year: int = 2019) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    max_possible_thrust, phase_setting = _get_max_thrust_permutation_feedback_mode(
        program=_parse_file(input_file_path)
    )
    print(f"Max thrust obtained from phase setting: {phase_setting}: ")
    return max_possible_thrust


# part_two(file="eg")
part_two(file="input")
