from pathlib import Path

from reusables import timer, INPUT_PATH

tree = {
    "dir /": {"dir d", "dir a", "14848514 b.txt", "8504156 c.dat"},
    "dir a": {"62596 h.lst", "29116 f", "2557 g", "dir e"},
    "dir e": {"584 i"},
    "dir d": {"8033020 d.log", "7214296 k", "5626152 d.ext", "4060174 j"},
}


def _dfs(
    tree: dict[str, set[str]],
    size_map: dict[str, int],
    node: str = "dir /",
):
    size = 0
    if node in tree:
        for child in tree[node]:
            if child.split(" ")[0].strip() == "dir":
                size += _dfs(tree, size_map, child)
            else:
                size += int(child.split(" ")[0])
        size_map[node] += size
    print(size_map)
    return size


def _parse_terminal_output(file_path: Path) -> dict[str, set[str]]:
    with open(file_path, "r") as puzzle_input:
        lines: list[str] = puzzle_input.read().strip().splitlines()
        # print(f"{lines=}")
        tree = dict()
        current_dir_contents = set()
        current_dir_name = "/"
        for line in lines:
            if line == "$ ls":
                continue
            elif (
                line.split(" ")[0].strip() == "cd" or line.split(" ")[1].strip() == "cd"
            ):
                if line.split(" ")[2].strip() == "..":
                    continue
                else:
                    tree["dir " + current_dir_name] = current_dir_contents
                    current_dir_name = line.split(" ")[2].strip()
                    current_dir_contents = set()
            else:
                current_dir_contents.add(line)
        tree["dir " + current_dir_name] = current_dir_contents
        # print(f"{tree=}")
        return tree


@timer
def part_one(file: str, day: int = 7, year: int = 2022):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    tree = _parse_terminal_output(file_path=input_file_path)
    size_map = {k: 0 for k in tree}
    return _dfs(tree=tree, size_map=size_map, node="dir /")


part_one(file="eg")
# part_one(file="input")


@timer
def part_two(file: str, day: int = 7, year: int = 2022):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    return _parse_terminal_output(file_path=input_file_path)


# part_two(file="eg")
# part_two(file="input")
