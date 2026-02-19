from pathlib import Path

from reusables import timer, INPUT_PATH


# https://wiki.python.org/moin/BitwiseOperators


def _parse_instructions(file_path: Path):
    graph = {}
    with open(file_path, "r") as puzzle_input:
        for line in puzzle_input.read().strip().splitlines():
            op, target = line.split(" -> ")
            graph[target] = op
    return graph


def _dfs(graph, start: str):
    print(f"{start=}")
    command = graph[start]
    input_1, input_2 = command.split(" ")[0], command.split(" ")[-1]
    for input in [input_1, input_2]:
        if graph[input].isdigit():
            print(f"Bottom! {input} => {graph[input]}")
        else:
            _dfs(graph, input)


@timer
def part_one(file: str, day: int = 7, year: int = 2015, wire: str = "a") -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    graph = _parse_instructions(input_file_path)
    print(f"{graph=}")
    _dfs(graph, start=wire)
    return -1


part_one(file="eg", wire="e")
# part_one(file="input")


@timer
def part_two(file: str, day: int = 7, year: int = 2015):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    return _parse_instructions(file_path=input_file_path)


# part_two(file="eg")
# part_two(file="input")
