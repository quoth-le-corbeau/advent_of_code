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
            if child.startswith("dir "):
                dir_name = child.split(" ")[1]
                new_node = node.rstrip("/") + "/" + dir_name
                s, _ = _dfs(tree, new_node, size_map)
                size += s
            else:
                size += int(child.split(" ")[0])
        size_map[node] = size
    return size, size_map


def _parse_terminal_output(file_path: Path) -> dict:
    with open(file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        tree = defaultdict(set)
        path = []
        for line in lines:
            parts = line.split(" ")
            if parts == ["$", "ls"]:
                continue
            elif parts == ["$", "cd", ".."]:
                path.pop()
            elif parts[0] == "$" and parts[1] == "cd":
                if parts[2] == "/":
                    path = [""]
                else:
                    path.append(parts[2])
            else:
                current_path = "/".join(path).replace("//", "/") or "/"
                tree[current_path].add(line)
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
