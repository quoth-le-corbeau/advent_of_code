import time
import pathlib


def sum_item_priorities(file: str) -> int:
    all_compartments = _get_compartments(file=file)
    elf_items = list()
    for compartments in all_compartments:
        first, second = set(compartments[0]), set(compartments[1])
        elf_items += [item for item in first.intersection(second)]
    priorities = list()
    for item in elf_items:
        priorities.append(_get_item_priority(item=item))
    return sum(priorities)


def _get_item_priority(item: str) -> int:
    if ord(item) >= 97:
        return ord(item) - 96
    else:
        return (ord(item) - 64) + 26


def _get_compartments(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        rucksacks = puzzle_input.read().splitlines()
        all_compartments = list()
        for rucksack in rucksacks:
            half_length = len(rucksack) // 2
            compartment_1, compartment_2 = (
                rucksack[:half_length],
                rucksack[half_length:],
            )
            all_compartments.append((compartment_1, compartment_2))
        return all_compartments


start = time.perf_counter()
print(sum_item_priorities("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(sum_item_priorities("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
