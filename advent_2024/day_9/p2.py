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

create a free index mapper using tuples showing the start of free space index and until which index is free
    e.g [(2,3), (8,3) ...]
    
create a result array = []
loop through the dictionary:
    append key * blocks to the array
    "." * space_after
result = [0,0,.,.,.,1,1,1,.,.,.2,.,.,.,3,3,3 etc]

loop through the dictionary backwards
    record the index of the start of each key (file)
    loop through the free index mapper tuples
    look for enough space to insert the whole file
    ! make sure to abort if the index of the file to be moved is less than the start of free space block
    insert the file in the free space if it fits and update the start of the free space block
    finally change the original positions of the file (dict key) to "."s

calculate the checksum as before

"""


def calculate_new_checksum(file_path: str):
    disk_map = _parse_input(file=file_path)
    free_idxs, result = _get_free_indexes_and_current_array(disk_map)
    for key in range(len(disk_map) - 1, -1, -1):
        index_of_file = result.index(key)
        file_size = disk_map[key][0]
        for j, free_idx in enumerate(free_idxs):
            free_space_in_block = free_idx[1] - free_idx[0]
            if free_space_in_block < file_size:
                continue
            if index_of_file <= free_idx[0]:
                continue
            else:
                indexes_of_file_entries = [
                    index for index, value in enumerate(result) if value == key
                ]
                for index in indexes_of_file_entries:
                    result[index] = "."
                next_insert_start_idx = free_idx[0]
                i = 0
                while i < file_size:
                    result[next_insert_start_idx + i] = key
                    i += 1
                free_idxs[j][0] = next_insert_start_idx + i
                break

    checksum = 0
    for i, num in enumerate(result):
        if num == ".":
            continue
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

start = time.perf_counter()
print(
    calculate_new_checksum(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_9"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
