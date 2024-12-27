import time
import pathlib
import re


def restore_1202_program_alarm(file_path: str) -> int:
    programs = _parse_programs(file=file_path)
    programs[1] = 12
    programs[2] = 2
    i = 0
    while i < len(programs):
        if programs[i] == 99:
            i += 1
            break
        else:
            program = programs[i : i + 4]
            opcode = program[0]
            if len(program) < 2:
                i += 1
                continue
            x = program[1]
            a = programs[x]
            if len(program) < 3:
                i += 1
                continue
            y = program[2]
            b = programs[y]
            if len(program) < 4:
                i += 1
                continue
            position = program[3]
            if opcode == 1:
                programs[position] = a + b
            elif opcode == 2:
                programs[position] = a * b
        i += 4
    return programs[0]


def _parse_programs(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        return list(map(int, re.findall(r"\d+", puzzle_input.read())))


timer_start = time.perf_counter()
print(
    restore_1202_program_alarm(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2019/day_2"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
