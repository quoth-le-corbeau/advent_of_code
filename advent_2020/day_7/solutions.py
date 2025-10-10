from collections import defaultdict
from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_input_rules(file_path: Path) -> dict[str, list[str]]:
    with open(file_path, "r") as puzzle_input:
        contains_by_bag = defaultdict(list)
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
    return dict(contains_by_bag)


@timer
def part_one(file: str, day: int = 7, year: int = 2020) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    contains_by_bag = _parse_input_rules(file_path=input_file_path)
    all_bags = list(contains_by_bag.keys())
    for bag, inner_bags in contains_by_bag.items():
        i = all_bags.index(bag)
        for inner in inner_bags:
            j = all_bags.index(inner)
            if j < i:
                all_bags[i], all_bags[j] = all_bags[j], all_bags[i]
    print(all_bags)
    return all_bags.index("shiny gold")


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
