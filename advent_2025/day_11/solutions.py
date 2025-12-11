from collections import deque
from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_tree(file_path: Path) -> dict[str, set[str]]:
    tree = dict()
    with open(file_path, "r") as puzzle_input:
        for line in puzzle_input.read().strip().splitlines():
            key, values = line.split(": ")
            tree[key.strip()] = set(values.split(" "))
    return tree


def _bfs(start_node: str, tree: dict[str, set[str]]):
    q = deque([[start_node]])
    # visited = set()
    paths = []
    while q:
        path = q.popleft()
        current_node = path[-1]
        if current_node == "out":
            paths.append(path)
            continue
        for neighbor in tree[current_node]:
            # if neighbor not in visited:
            q.append(path + [neighbor])
            # visited.add(neighbor)
    return paths


@timer
def part_one(file: str, day: int = 11, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    tree = _parse_tree(file_path=input_file_path)
    # print(f"{tree=}")
    paths = _bfs(start_node="you", tree=tree)
    # print(f"{paths=}")
    return len(paths)


# part_one(file="eg")
# part_one(file="input")


@timer
def part_two(file: str, day: int = 11, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    tree = _parse_tree(file_path=input_file_path)
    paths = _bfs(start_node="svr", tree=tree)
    res = []
    for path in paths:
        if "fft" in path and "dac" in path:
            res.append(path)
    print(f"{res=}")
    return len(res)


part_two(file="eg2")
# part_two(file="input")
