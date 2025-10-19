from pathlib import Path
from collections import defaultdict

from reusables import timer, INPUT_PATH


# decide on a data structure into which to parse the input
# base the decision on an appropriate algorithm to arrive at the solution
# assess if the data structure misses any edge cases (e.g - repeated dir names in nesting means flat won't work)
# assess if the algo misses edge cases
# proceed

_PART_ONE_SIZE = 100000
_ROOT_DIR = "/"
_TOTAL_DISK_SPACE = 70000000
_NEEDED_FREE_FOR_UPDATE = 30000000


def _parse_terminal_output(file_path: Path) -> dict[str, set[str]]:
    with open(file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        tree = defaultdict(set)
        path = []
        for line in lines:
            parts = line.split(" ")
            if line == "$ ls":
                continue
            elif line == "$ cd ..":
                path.pop()
            elif line.startswith("$ cd "):
                if len(parts) != 3:
                    raise ValueError(f"Unexpected command: {line}")
                dir_name = parts[2]
                if dir_name == "/":
                    path = [""]
                else:
                    path.append(dir_name)
                dir_name = "/".join(path).replace("//", "/") or "/"
            else:
                tree[dir_name].add(line)
    return dict(tree)


def _dfs_sum(
    tree: dict[str, set[str]], size_map: dict[str, int], node: str
) -> tuple[int, dict[str, int]]:
    size = 0
    for child in tree[node]:
        parts = child.split(" ")
        if len(parts) != 2:
            raise ValueError(f"Invalid dir content: {child}")

        if child.startswith("dir "):
            new_node = node.rstrip("/") + "/" + child.split(" ")[1].strip()
            s, _ = _dfs_sum(tree=tree, size_map=size_map, node=new_node)
            size += s
        else:
            try:
                file_size = int(parts[0])
            except ValueError:
                raise ValueError(f"Invalid file: {child}")
            size += file_size
    size_map[node] = size
    return size, size_map


def _get_file_system_size(input_file_path: Path) -> tuple[int, dict[str, int]]:
    file_system_tree = _parse_terminal_output(file_path=input_file_path)
    size_map = {dir_name: 0 for dir_name in file_system_tree}
    # print(f"{file_system_tree=}")
    return _dfs_sum(tree=file_system_tree, size_map=size_map, node=_ROOT_DIR)


@timer
def part_one(file: str, day: int = 7, year: int = 2022) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    root_dir_size, size_by_dir_name = _get_file_system_size(input_file_path)
    # print(f"{root_dir_size=}")
    # print(f"{size_by_dir_name=}")
    return sum(list(filter(lambda x: x <= _PART_ONE_SIZE, size_by_dir_name.values())))


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 7, year: int = 2022) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    root_dir_size, size_by_dir_name = _get_file_system_size(input_file_path)
    unused_space = _TOTAL_DISK_SPACE - root_dir_size
    required = _NEEDED_FREE_FOR_UPDATE - unused_space
    return sorted(list(filter(lambda x: x >= required, size_by_dir_name.values())))[0]


part_two(file="eg")
part_two(file="input")
