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
    paths = []
    while q:
        path = q.popleft()
        current_node = path[-1]
        if current_node == "out":
            paths.append(path)
            continue
        for neighbor in tree[current_node]:
            q.append(path + [neighbor])
    return paths


@timer
def part_one(file: str, day: int = 11, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    tree = _parse_tree(file_path=input_file_path)
    paths = _bfs(start_node="you", tree=tree)
    return len(paths)


part_one(file="eg")
part_one(file="input")


def _dfs(
    node: str,
    tree: dict[str, set[str]],
    seen_dac: bool = False,
    seen_fft: bool = False,
    cache: dict[tuple[str, bool, bool], int] | None = None,
) -> int:
    if cache is None:
        cache = {}
    if node == "out":
        if seen_dac and seen_fft:
            return 1
        else:
            return 0

    count = 0
    for neighbor in tree[node]:
        new_seen_fft = seen_fft or (neighbor == "fft")
        new_seen_dac = seen_dac or (neighbor == "dac")
        if (neighbor, new_seen_fft, new_seen_dac) in cache:
            neighbor_count = cache[(neighbor, new_seen_fft, new_seen_dac)]
        else:
            neighbor_count = _dfs(
                node=neighbor,
                tree=tree,
                seen_dac=new_seen_dac,
                seen_fft=new_seen_fft,
                cache=cache,
            )
            cache[(neighbor, new_seen_fft, new_seen_dac)] = neighbor_count
        count += neighbor_count

    return count


@timer
def part_two(file: str, day: int = 11, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    tree = _parse_tree(file_path=input_file_path)
    valid_path_count = _dfs(node="svr", tree=tree)
    return valid_path_count


part_two(file="eg2")
part_two(file="input")
