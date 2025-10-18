from collections import defaultdict
from pathlib import Path

from reusables import timer, INPUT_PATH

# decide on a data structure into which to parse the input
# base the decision on an appropriate algorithm to arrive at the solution
# assess if the data structure misses any edge cases (e.g - repeated dir names in nesting means flat won't work)
# assess if the algo misses edge cases
# proceed


def _dfs(tree: dict[str, set[str]], node: str, size_map: dict[str, int]):
    size = 0
    if node in tree:
        for child in tree[node]:
            if child.split(" ")[0] == "dir":
                if node == "/":
                    new_node = child.split(" ")[1]
                else:
                    new_node = node + "/" + child.split(" ")[1]
                s, _ = _dfs(tree, new_node, size_map)
                size += s
            else:
                size += int(child.split(" ")[0])
        size_map[node] = size
    return size, size_map


def _parse_terminal_output(file_path: Path) -> dict:
    with open(file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        current_dir_name = ""
        tree = defaultdict(set)
        path = []
        for line in lines:
            parts = line.split(" ")
            if parts == ["$", "ls"]:
                continue
            elif parts == ["$", "cd", ".."]:
                path.pop()
                current_dir_name = path[-1] if path else "/"
            elif parts[0] == "$" and parts[1] == "cd" and parts[2] != "..":
                prev_dir_name = current_dir_name
                current_dir_name = parts[2]
                if current_dir_name != "/" and prev_dir_name != "/":
                    current_dir_name = prev_dir_name + "/" + current_dir_name
                path.append(current_dir_name)
            else:
                tree[current_dir_name].add(" ".join(parts))
        return dict(tree)


@timer
def part_one(file: str, day: int = 7, year: int = 2022) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    tree = _parse_terminal_output(file_path=input_file_path)
    size_map = {dir_name: 0 for dir_name in tree}
    root_dir_size, size_map = _dfs(tree=tree, node="/", size_map=size_map)
    print(f"{root_dir_size=}")
    print(f"{size_map=}")
    total = 0
    for dir_name, dir_size in size_map.items():
        if dir_size <= 100000:
            total += dir_size
    return total


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 7, year: int = 2022):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    return _parse_terminal_output(file_path=input_file_path)


# part_two(file="eg")
# part_two(file="input")
