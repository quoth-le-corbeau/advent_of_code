from collections import defaultdict
from pathlib import Path

from reusables import timer, INPUT_PATH

# decide on a data structure into which to parse the input
# base the decision on an appropriate algorithm to arrive at the solution
# assess if the data structure misses any edge cases (e.g - repeated dir names in nesting means flat won't work)
# assess if the algo misses edge cases
# proceed


def _parse_terminal_output(file_path: Path) -> dict:
    with open(file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        current_dir_name = "/"
        tree = defaultdict(set)
        path = ["/"]
        for line in lines:
            parts = line.split(" ")
            if parts == ["$", "ls"]:
                continue
            elif parts == ["$", "cd", ".."]:
                current_dir_name = path.pop()
            elif parts[0] == "$" and parts[1] == "cd" and parts[2] != "..":
                current_dir_name += "/" + parts[2]
                path.append(current_dir_name)
            else:
                tree[current_dir_name].add(" ".join(parts))
        return dict(tree)


@timer
def part_one(file: str, day: int = 7, year: int = 2022):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    return _parse_terminal_output(file_path=input_file_path)


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
