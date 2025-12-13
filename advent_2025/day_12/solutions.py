from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_input(file_path: Path):
    shapes_by_index = {}
    area_rule_pairs = []
    with open(file_path, "r") as puzzle_input:
        blocks = puzzle_input.read().split("\n\n")
        for i, block in enumerate(blocks):
            if i == len(blocks) - 1:
                for line in block.strip().splitlines():
                    dimensions, rules = line.strip().split(":")
                    w, h = dimensions.split("x")
                    area_rule_pairs.append(
                        (int(w) * int(h), list(map(int, rules.strip().split())))
                    )
            else:
                idx, shape = block.split(":")
                shape = shape.strip().splitlines()
                shape_volume = sum(s.count("#") for s in shape)
                shapes_by_index[int(idx)] = (shape, shape_volume)
    print(f"{area_rule_pairs=}")
    print(f"{shapes_by_index=}")
    return shapes_by_index, area_rule_pairs


@timer
def part_one(file: str, day: int = 12, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    shapes_by_index, area_rule_pairs = _parse_input(file_path=input_file_path)
    count = 0
    for area, rule in area_rule_pairs:
        rule_volume = 0
        for idx, n in enumerate(rule):
            rule_volume += shapes_by_index[idx][1] * n
        if rule_volume <= area:
            count += 1
    return count


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 12, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    return _parse_input(file_path=input_file_path)


# part_two(file="eg")
# part_two(file="input")
