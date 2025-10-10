from collections import defaultdict
from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_input_rules(
    file_path: Path,
) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    with open(file_path, "r") as puzzle_input:
        contains_by_bag = defaultdict(list)
        contained_in_by_bag = defaultdict(list)
        lines = puzzle_input.read().strip().splitlines()
        for line in lines:
            line = line.replace(".", "")
            line = line.replace("bags", "")
            line = line.replace("bag", "")
            outer, inner = line.split(" contain ")
            outer = outer.strip()
            inner = inner.strip()
            all_inner = inner.split(" , ")
            in_outer_omit_number = set()
            for s in all_inner:
                if s == "no other":
                    contains_by_bag[outer] = []
                    continue
                bag_no_number = " ".join(s.split(" ")[1:])
                in_outer_omit_number.add(bag_no_number)
            contains_by_bag[outer] = list(in_outer_omit_number)
            for inner in in_outer_omit_number:
                contained_in_by_bag[inner].append(outer)
    return dict(contains_by_bag), dict(contained_in_by_bag)


@timer
def part_one(file: str, day: int = 7, year: int = 2020) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    contains_mapping, contained_by_mapping = _parse_input_rules(
        file_path=input_file_path
    )
    directly_containing_gold = contained_by_mapping["shiny gold"]


part_one(file="eg")
# part_one(file="input")


@timer
def part_two(file: str, day: int = 7, year: int = 2020):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    print(f"part 2: {_parse_input_rules(file_path=input_file_path)}")


# part_two(file="eg")
# part_two(file="input")

contains_by_bag = {
    "light red": ["bright white", "muted yellow"],
    "dark orange": ["bright white", "muted yellow"],
    "bright white": ["shiny gold"],
    "muted yellow": ["shiny gold", "faded blue"],
    "shiny gold": ["vibrant plum", "dark olive"],
    "dark olive": ["dotted black", "faded blue"],
    "vibrant plum": ["dotted black", "faded blue"],
    "faded blue": [],
    "dotted black": [],
}
contained_by_mapping = {
    "bright white": ["light red", "dark orange"],
    "muted yellow": ["light red", "dark orange"],
    "shiny gold": ["bright white", "muted yellow"],
    "faded blue": ["muted yellow", "dark olive", "vibrant plum"],
    "vibrant plum": ["shiny gold"],
    "dark olive": ["shiny gold"],
    "dotted black": ["dark olive", "vibrant plum"],
}
