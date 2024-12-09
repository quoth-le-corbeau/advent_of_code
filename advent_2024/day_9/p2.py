import time
import pathlib

"""
Disk Fragmenter Part II
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
create a copy of this showing the start index and the length of free space starting there
    e.g [(2,3), (8,3) ...]
    
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
    file_length = blocks
    if counter == len(free_idxs):
        stop = True
        break
    if free_idxs[counter][1] >= file_length:
        for i in range(file_length):
         
00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..
"""


def calculate_new_checksum(file_path: str):
    disk_map = _parse_input(file=file_path)
    free_idxs, result = _get_free_indexes_and_current_array(disk_map)
    print(f"{free_idxs=}")
    removed_count = 0
    for key in range(len(disk_map) - 1, -1, -1):
        file_size = disk_map[key][0]
        for j, free_idx in enumerate(free_idxs):
            free_space_in_block = free_idx[1] - free_idx[0]
            if free_space_in_block < file_size:
                continue
            else:
                next_insert_start_idx = free_idx[0]
                for i in range(file_size):
                    next_insert_start_idx += i
                    result[next_insert_start_idx] = key
                free_idxs[j][0] = next_insert_start_idx + 1
                removed_count += file_size
                break
    print(f"{result=}")
    print(f"{result[:-removed_count]=}")

    final_result = []
    checksum = 0
    for i, num in enumerate(final_result):
        checksum += num * i
    return checksum


def _get_free_indexes_and_current_array(
    disk_map,
) -> tuple[list[list[int, int]], list[int]]:
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
        start = free_idx_counter
        for i in range(space_after):
            # free_idxs.append(free_idx_counter)
            result.append(".")
            free_idx_counter += 1
        free_idxs.append([start, free_idx_counter])
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


start = time.perf_counter()
print(
    calculate_new_checksum(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_9"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

# start = time.perf_counter()
# print(
#    calculate_new_checksum(
#        str(
#            (
#                    pathlib.Path(__file__).resolve().parents[2]
#                    / "my_inputs/2024/day_9"
#                    / "input.txt"
#            )
#        )
#    )
# )
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
