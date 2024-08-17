import time
import pathlib


def calculate_final_position_depth_aim_product(file_path: str) -> int:
    instructions = _parse_instructions(file=file_path)
    horizontal = 0
    depth = 0
    aim = 0
    for instruction in instructions:
        if instruction[0] == "forward":
            horizontal += instruction[1]
            depth += aim * instruction[1]
        elif instruction[0] == "down":
            aim += instruction[1]
        else:
            assert instruction[0] == "up"
            aim -= instruction[1]
    return horizontal * depth


def _parse_instructions(file: str) -> list[tuple[str, int]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        return [((line.split()[0], int(line.split()[1]))) for line in lines]


start = time.perf_counter()
print(calculate_final_position_depth_aim_product("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(calculate_final_position_depth_aim_product("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
