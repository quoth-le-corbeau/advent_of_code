from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_program(file_path: Path) -> list[int]:
    with open(file_path, "r") as puzzle_input:
        return list(map(int, puzzle_input.read().strip().split(",")))


def _run(program: list[int]) -> list[int]:
    i = 0
    while i < len(program) - 4:
        chunk = program[i : i + 4]
        opcode = chunk[0]
        pos_1 = chunk[1]
        pos_2 = chunk[2]
        target_index = chunk[3]
        if opcode == 99:
            break
        elif opcode == 1:
            program[target_index] = program[pos_1] + program[pos_2]
        elif opcode == 2:
            program[target_index] = program[pos_1] * program[pos_2]
        else:
            raise ValueError(f"Invalid opcode: {opcode}")
        i += 4
    return program


@timer
def part_one(file: str, day: int = 2, year: int = 2019) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    program = _parse_program(file_path=input_file_path)
    # adjust program for real input
    if file == "input":
        program[1] = 12
        program[2] = 2
    result = _run(program)
    return result[0]


part_one(file="eg")
part_one(file="input")

_TARGET = 19690720


@timer
def part_two(file: str, day: int = 2, year: int = 2019) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    original_program = _parse_program(file_path=input_file_path)
    for noun in range(100):
        for verb in range(100):
            program = original_program.copy()
            program[1] = noun
            program[2] = verb
            result = _run(program)
            if result[0] == _TARGET:
                return 100 * noun + verb
    return -1


# part_two(file="eg")
part_two(file="input")
