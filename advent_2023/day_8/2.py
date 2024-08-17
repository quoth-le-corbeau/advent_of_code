import time
import pathlib
import math


def count_ghost_moves_to_navigate_wasteland(file: str) -> int:
    directional_instructions, network_look_up = _parse_instructions(file=file)
    number_of_directional_instructions = len(directional_instructions)
    start_positions = [key for key in network_look_up if key.endswith("A")]
    distances_to_zs = []
    for string in start_positions:
        i = 0
        distances_to_z = []
        while not string.endswith("Z"):
            if i >= number_of_directional_instructions:
                direction = directional_instructions[
                    i % number_of_directional_instructions
                ]
            else:
                direction = directional_instructions[i]
            string = network_look_up[string][int(direction)]
            i += 1
        distances_to_z.append(i)
        distances_to_zs += distances_to_z
    lcm = 1
    for number in distances_to_zs:
        lcm = lcm * number // math.gcd(lcm, number)
    return lcm


def _parse_instructions(file: str) -> tuple[str, dict[str, tuple[str, str]]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        directional_instructions = puzzle_input.readline()
        network_look_up = dict()
        for line in puzzle_input.readlines()[1:]:
            line = line.strip().replace("(", "").replace(")", "")
            network_look_up[line.split(" = ")[0].strip()] = (
                line.split(" = ")[1].split(",")[0].strip(),
                line.split(" = ")[1].split(",")[1].strip(),
            )
        directional_instructions = directional_instructions.replace("L", "0").replace(
            "R", "1"
        )
    return directional_instructions.strip(), network_look_up


start = time.perf_counter()
print(count_ghost_moves_to_navigate_wasteland("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(count_ghost_moves_to_navigate_wasteland("eg1.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(count_ghost_moves_to_navigate_wasteland("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
