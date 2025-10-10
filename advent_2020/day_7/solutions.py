from collections import defaultdict
from pathlib import Path
import re

from reusables import timer, INPUT_PATH


def _parse_input_rules(file_path: Path) -> dict[str, list[str]]:
    with open(file_path, "r") as puzzle_input:
        contains_by_bag = defaultdict(list)
        seen = set()
        for line in puzzle_input.read().strip().splitlines():
            container, contained = line.split(" contain ")
            seen.add(container.replace(" bags", ""))
            for contained in contained.split(", "):
                contained = re.sub(
                    r"\d ", "", contained.replace(" bag", "").replace(".", "")
                )
                seen.add(contained)
                contains_by_bag[container].append(contained)
        assert list(seen) == list(contains_by_bag.keys())
        return dict(contains_by_bag)


@timer
def part_one(file: str, day: int = 7, year: int = 2020) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    contains_by_bag, seen = _parse_input_rules(file_path=input_file_path)
    print(f"{contains_by_bag=}")
    print(f"{seen=}")


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
