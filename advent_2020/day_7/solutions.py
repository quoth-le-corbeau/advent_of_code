from collections import defaultdict
from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_input_rules(
    file_path: Path,
) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    with open(file_path, "r") as puzzle_input:
        contains = defaultdict(set)
        contained_mapping = defaultdict(set)
        lines = puzzle_input.read().strip().splitlines()
        for line in lines:
            parsed_line = line.replace(".", "").replace("bags", "").replace("bag", "")
            outer, inner = parsed_line.split(" contain ")
            outer = outer.strip()
            all_inner = inner.strip().split(" , ")
            for inner in all_inner:
                if "no other" in inner:
                    contains[outer] = set()
                    continue
                contains[outer].add(inner)
            for inner in all_inner:
                parsed_inner = " ".join(inner.split(" ")[1:])
                contained_mapping[parsed_inner].add(outer)
    return dict(contains), dict(contained_mapping)


def _dfs(tree: dict[str, set[str]]) -> set[str]:
    stack = ["shiny gold"]
    seen = set()
    end_nodes = list()
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        if node in tree:
            for child in tree[node]:
                stack.append(child)
        else:
            end_nodes.append(node)

    print(f"End nodes: {end_nodes}")
    print(f"Seen nodes: {seen}")
    return seen


@timer
def part_one(file: str, day: int = 7, year: int = 2020) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    contains_mapping, contained_by_mapping = _parse_input_rules(
        file_path=input_file_path
    )
    # print(f"{contains_mapping=}, \n{contained_by_mapping=}")
    return len(_dfs(tree=contained_by_mapping)) - 1


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 7, year: int = 2020):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    print(f"part 2: {_parse_input_rules(file_path=input_file_path)}")


# part_two(file="eg")
# part_two(file="input")
