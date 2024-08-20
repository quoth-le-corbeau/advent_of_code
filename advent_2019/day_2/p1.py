import time
import pathlib
import re


def restore_1202_program_alarm(file_path: str):
    programs = _parse_programs(file=file_path)
    i = 0
    while i < len(programs):
        if i == len(programs) - 1:
            print(f"This better be the end: {programs[i]}")
            break
        elif programs[i] == 99:
            print(f"Better be {programs[i]} Luftballons!")
            i += 1
            continue
        else:
            program = programs[i : i + 4]
            print(f"{program=}")
        i += 4


def _parse_programs(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        return list(map(int, re.findall(r"\d+", puzzle_input.read())))


start = time.perf_counter()
print(restore_1202_program_alarm("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

# start = time.perf_counter()
# print(restore_1202_program_alarm("input.txt"))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
