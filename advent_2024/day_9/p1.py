import time
import pathlib

"""
Disk Fragmenter Part I
read the string in groups of 2 (i, i + 1)
create a dictionary
    {
        id: (blocks, space_after)
    }
    e.g:
    {
        0: {blocks: 2, space_after: 3},
        1: {blocks: 3, space_after: 3},
        ...
        9: {blocks:2, space_after: 0} <- zero inferred by end of string
    }

create free index number array free_idxs = [2,3,4,8,9,10 ... ]
create a result array = []
loop through the dictionary:
    append key * blocks to the array
    "." * space_after
result = [0,0,.,.,.,1,1,1,.,.,.2,.,.,.,3,3,3 etc]

loop through the dictionary backwards:
counter = 0
stop = False
for key in range(len(dict), -1, -1):
    if stop:
        break
    for i in range blocks(2)
        counter += 1
        if counter == len(free_idxs):
            stop = True
            break
        result[free_idxs[counter]] = key
        Note: this will put a 9 at index 2 and index 3 and set our counter to 2
    
"""


def calculate_checksum(file_path: str):
    disk_map = _parse_input(file=file_path)
    free_idxs, result = _get_free_indexes_and_current_array(disk_map)
    stop = False
    counter = 0
    for key in range(len(disk_map) - 1, -1, -1):
        if stop:
            break
        for i in range(disk_map[key][0]):
            counter += 1
            if counter == len(free_idxs):
                stop = True
                break
            else:
                result[free_idxs[counter - 1]] = key
    to_remove = len(result) - counter
    final_result = result[:to_remove]
    checksum = 0
    for i, num in enumerate(final_result):
        checksum += num * i
    return checksum


def _get_free_indexes_and_current_array(disk_map):
    free_idxs = []
    result = []
    free_idx_counter = 0
    for id, block_space in disk_map.items():
        blocks = block_space[0]
        space_after = block_space[1]
        free_idx_counter += blocks
        b = 0
        while b < blocks:
            result.append(id)
            b += 1
        for i in range(space_after):
            free_idxs.append(free_idx_counter)
            result.append(".")
            free_idx_counter += 1
    return free_idxs, result


def _parse_input(file: str) -> dict[int, tuple[int, int]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().strip()
        disk_map = dict()
        for i in range(0, len(lines), 2):
            if i + 1 == len(lines):
                disk_map[i // 2] = (int(lines[i]), 0)
            else:
                disk_map[i // 2] = (int(lines[i]), int(lines[i + 1]))
        return disk_map


timer_start = time.perf_counter()
print(
    calculate_checksum(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_9"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    calculate_checksum(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_9"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
