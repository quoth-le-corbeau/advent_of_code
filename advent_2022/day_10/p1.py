import pathlib
import time


def calculate_signal_strength(file_path: str) -> int:
    program = _parse_program_file(file=file_path)
    cycle_count = 0
    register = 1
    signal_strengths = list()
    for line in program:
        i = 0
        while i < line[0]:
            cycle_count += 1
            if (
                cycle_count == 20
                or cycle_count == 60
                or cycle_count == 100
                or cycle_count == 140
                or cycle_count == 180
                or cycle_count == 220
            ):
                signal_strengths.append(register * cycle_count)
            i += 1
        register += line[1]
    return sum(signal_strengths)


def _parse_program_file(file: str) -> list[tuple[int, int]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        program = list()
        for line in lines:
            if line.split()[0] == "noop":
                program.append((1, 0))
            else:
                program.append((2, int(line.split()[1])))
        return program


start = time.perf_counter()
print(calculate_signal_strength("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(calculate_signal_strength("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
