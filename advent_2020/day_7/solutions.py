from collections import defaultdict
from pathlib import Path
from typing import Optional

from reusables import timer, INPUT_PATH

contains_mapping_example = {
    "light red": {"1 bright white", "2 muted yellow"},
    "dark orange": {"4 muted yellow", "3 bright white"},
    "bright white": {"1 shiny gold"},
    "muted yellow": {"2 shiny gold", "9 faded blue"},
    "shiny gold": {"2 vibrant plum", "1 dark olive"},
    "dark olive": {"4 dotted black", "3 faded blue"},
    "vibrant plum": {"6 dotted black", "5 faded blue"},
    "faded blue": set(),
    "dotted black": set(),
}


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


def _dfs(graph: dict[str, set[str]]) -> set[str]:
    stack = ["shiny gold"]
    seen = set()
    # end_nodes = list()
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        if node in graph:
            for child in graph[node]:
                stack.append(child)
    #    else:
    #        end_nodes.append(node)

    # print(f"End nodes: {end_nodes}")
    # print(f"Seen nodes: {seen}")
    return seen


def _dfs_sum_node_values(graph: dict[str, set[str]], node_colour: str) -> int:
    if node_colour == "shiny gold":
        pass
    else:
        node_colour = " ".join(node_colour.split(" ")[1:])

    count = 0
    if node_colour in graph:
        for child in graph[node_colour]:
            n = int(child.split(" ")[0].strip())
            count += n
            count += n * _dfs_sum_node_values(graph, child)
    return count


def _dfs_recursive(
    graph: dict[str, set[str]],
    seen: Optional[set[str]] = None,  # to avoid having a mutable default arg
    node: str = "shiny gold",
) -> set[str]:
    if seen is None:
        seen = set()
    seen.add(node)
    if node in graph:
        for child in graph[node]:
            if child not in seen:
                _dfs_recursive(graph, seen, child)
    # print(f"Seen nodes: {seen}")
    return seen


@timer
def part_one(file: str, day: int = 7, year: int = 2020) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    _, contained_by_mapping = _parse_input_rules(file_path=input_file_path)
    # print(f"{contains_mapping=}, \n{contained_by_mapping=}")
    # return len(_dfs(graph=contained_by_mapping)) - 1
    return len(_dfs_recursive(graph=contained_by_mapping)) - 1


print("---------------Part 1 example-------------------------")
part_one(file="eg")
print("---------------Part 2 input-------------------------")
part_one(file="input")


@timer
def part_two(file: str, day: int = 7, year: int = 2020):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    contains_mapping, _ = _parse_input_rules(file_path=input_file_path)
    # print(f"{contains_mapping=}")

    return _dfs_sum_node_values(graph=contains_mapping, node_colour="shiny gold")


print("---------------Part 2 example-------------------------")
part_two(file="eg")
print("---------------Part 2 input-------------------------")
part_two(file="input")
