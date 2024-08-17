from typing import List, Dict
import time
import pathlib

_SHINY_GOLD = "shiny gold bag"


def get_number_of_shiny_gold_bag_holders(file_path: str) -> int:
    rules = _get_bag_holding_rules(file=file_path)
    count = 0
    bags_containing_gold = set()
    for color, contains in rules.items():
        if any(_SHINY_GOLD in contents for contents in contains):
            bags_containing_gold.add(color)
            count += 1

    while len(bags_containing_gold) > 0:
        target_content = bags_containing_gold.pop()
        for color, contains in rules.items():
            if any(target_content in contents for contents in contains):
                current_length = len(bags_containing_gold)
                bags_containing_gold.add(color)
                new_length = len(bags_containing_gold)
                count += new_length - current_length

    return count


def _get_bag_holding_rules(file: str) -> Dict[str, List[str]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        rules_by_bag = dict()
        for line in lines:
            line = (
                line.replace(" contain", ",")
                .replace(".", "")
                .replace("bags", "bag")
                .replace(", ", ",")
            )
            split_line = line.split(",")
            rules_by_bag[split_line[0]] = split_line[1:]
        return rules_by_bag


start = time.perf_counter()
print(get_number_of_shiny_gold_bag_holders("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(get_number_of_shiny_gold_bag_holders("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
