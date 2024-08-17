import time
import pathlib


DISK_SIZE = 70000000
SPACE_NEEDED = 30000000

ALL_DIRECTORY_SIZES = list()


def find_smallest_directory_to_delete(file: str) -> int:
    file_structure = _build_nested_file_structure(file=file)
    _get_all_directory_sizes(file_structure)
    potentially_deletable_directories = list()
    current_free_space = DISK_SIZE - ALL_DIRECTORY_SIZES[-1]
    for directory in ALL_DIRECTORY_SIZES:
        if current_free_space + directory >= SPACE_NEEDED:
            potentially_deletable_directories.append(directory)
    return min(potentially_deletable_directories)


def _get_all_directory_sizes(file_structure) -> None:
    root_dir_size = 0
    for _, value in file_structure.items():
        if isinstance(value, int):
            root_dir_size += value
        else:
            # assume values can only be integers or dictionaries
            size_of_next_inner_directory = _recursive_sum_of_nested_dicts(
                nested_dict=value
            )
            root_dir_size += size_of_next_inner_directory
            ALL_DIRECTORY_SIZES.append(size_of_next_inner_directory)
    ALL_DIRECTORY_SIZES.append(root_dir_size)


def _recursive_sum_of_nested_dicts(nested_dict) -> int:
    sum_of_integers_in_outer_dict = 0
    for _, value in nested_dict.items():
        if isinstance(value, int):
            sum_of_integers_in_outer_dict += value
        else:
            sum_of_integers_in_next_inner_dict = _recursive_sum_of_nested_dicts(
                nested_dict=value
            )
            ALL_DIRECTORY_SIZES.append(sum_of_integers_in_next_inner_dict)
            sum_of_integers_in_outer_dict += sum_of_integers_in_next_inner_dict
    return sum_of_integers_in_outer_dict


def _build_nested_file_structure(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        current_dir = dict()
        stack = list()
        for line in lines:
            if line.split()[-1] == "ls":
                continue
            elif line.split()[1] == "cd":
                directory_name = line.split()[-1]
                if directory_name == "/":
                    current_dir = dict()
                    stack = list()
                elif directory_name == "..":
                    current_dir = stack.pop()
                else:
                    if directory_name not in current_dir:
                        current_dir[directory_name] = dict()
                    stack.append(current_dir)
                    current_dir = current_dir[directory_name]
            else:
                dir_or_file_size, dir_or_file_name = line.split()
                if dir_or_file_size == "dir":
                    current_dir[dir_or_file_name] = dict()
                else:
                    current_dir[dir_or_file_name] = int(dir_or_file_size)
        return stack[0]


start = time.perf_counter()
print(find_smallest_directory_to_delete("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(find_smallest_directory_to_delete("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
