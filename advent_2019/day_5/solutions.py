from pathlib import Path

from reusables import timer, INPUT_PATH

_INPUT = 1


def _parse_file(file_path: Path) -> list[int]:
    with open(file_path, "r") as puzzle_input:
        return list(map(int, puzzle_input.read().strip().split(",")))


def _run(program: list[int]) -> int:
    output = -1
    i = 0
    while i < len(program) - 2:
        position_zero = str(program[i])
        while len(position_zero) < 5:
            position_zero = "0" + position_zero
        assert len(position_zero) == 5
        opcode = int(position_zero[-2:])
        mode_1 = position_zero[-3]
        mode_2 = position_zero[-4]
        if opcode == 99:
            print("Final diagnostic output: ")
            break
        elif opcode == 1:
            param_1 = program[program[i + 1]] if mode_1 == "0" else program[i + 1]
            param_2 = program[program[i + 2]] if mode_2 == "0" else program[i + 2]
            program[program[i + 3]] = param_1 + param_2
            i += 4
        elif opcode == 2:
            param_1 = program[program[i + 1]] if mode_1 == "0" else program[i + 1]
            param_2 = program[program[i + 2]] if mode_2 == "0" else program[i + 2]
            program[program[i + 3]] = param_1 * param_2
            i += 4
        elif opcode == 3:
            program[program[i + 1]] = _INPUT
            i += 2
        elif opcode == 4:
            param_1 = program[program[i + 1]] if mode_1 == "0" else program[i + 1]
            output = param_1
            if output == 0:
                print(
                    f"Test at position {i} success! {round(((i + 1) / len(program)) * 100, ndigits=2)}%"
                )
            i += 2
        else:
            raise ValueError(f"Invalid opcode: {opcode}")
    if output == -1:
        raise ValueError("No diagnostic output")
    return output


@timer
def part_one(file: str, day: int = 5, year: int = 2019) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    program = _parse_file(input_file_path)
    print(f"{len(program)=}")
    return _run(program)


# part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 5, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    program = _parse_file(file_path=input_file_path)


# part_two(file="eg")
# part_two(file="input")
