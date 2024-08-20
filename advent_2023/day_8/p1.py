import time
import pathlib


def count_moves_to_navigate_wasteland(file: str) -> int:
    directional_instructions, network_look_up = _parse_instructions(file=file)
    current_string = "AAA"
    final_string = "ZZZ"
    number_of_directional_instructions = len(directional_instructions)
    i = 0
    while current_string != final_string:
        if i >= number_of_directional_instructions:
            direction = directional_instructions[i % number_of_directional_instructions]
        else:
            direction = directional_instructions[i]
        direction = int(direction)
        current_string = network_look_up[current_string][direction]
        i += 1
    return i


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
print(count_moves_to_navigate_wasteland("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(count_moves_to_navigate_wasteland("eg1.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(count_moves_to_navigate_wasteland("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
