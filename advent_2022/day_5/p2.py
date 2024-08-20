import collections
import time
import re
import pathlib


def stack_crates_9001(file: str):
    stacks, instructions = _get_stacks_and_instructions(file=file)
    new_stacks = _apply_instructions_to_stacks(stacks=stacks, instructions=instructions)
    top_crates = ""
    for _, value in new_stacks.items():
        top_crates += value[0]
    return top_crates


def _apply_instructions_to_stacks(
    stacks: dict[str, list[str]], instructions: list[list[int]]
) -> dict[str, list[str]]:
    for instruction in instructions:
        number, start_stack, end_stack = instruction[0], instruction[1], instruction[2]
        crates = stacks[str(start_stack)][:number]
        crates = reversed(crates)
        stacks[str(start_stack)] = stacks[str(start_stack)][number:]
        for crate in crates:
            stacks[str(end_stack)].insert(0, crate)
    return stacks


def _get_stacks_and_instructions(
    file: str,
) -> tuple[dict[str, list[str]], list[list[int]]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        blocks = puzzle_input.read().split("\n\n")
        crate_block, instructions_block = blocks[0], blocks[1]
        crate_block = crate_block.split("\n")[:-1]
        numbered_stacks = collections.defaultdict(list)
        stacks = [
            [
                block[k].replace("[", "").replace("]", "")
                for k in range(1, len(block), 4)
            ]
            for block in crate_block
        ]
        for stack in stacks:
            for i, crate in enumerate(stack):
                if crate == " ":
                    continue
                else:
                    numbered_stacks[str(i + 1)].append(crate)
        instructions = instructions_block.split("\n")
        numbered_instructions = list()
        for instruction in instructions:
            numbered_instructions.append(
                list(map(int, re.findall(r"\d+", instruction)))
            )
        stacks_ordered_by_number = dict(sorted(numbered_stacks.items()))
    return stacks_ordered_by_number, numbered_instructions


start = time.perf_counter()
print(stack_crates_9001("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(stack_crates_9001("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
