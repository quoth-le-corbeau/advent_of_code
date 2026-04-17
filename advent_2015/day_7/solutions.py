from pathlib import Path

from reusables import timer, INPUT_PATH


# https://wiki.python.org/moin/BitwiseOperators


def _parse_instructions(file_path: Path):
    graph = {}
    with open(file_path, "r") as puzzle_input:
        for line in puzzle_input.read().strip().splitlines():
            op, target = line.split(" -> ")
            op = (
                op.replace("LSHIFT", "<<")
                .replace("RSHIFT", ">>")
                .replace("AND", "&")
                .replace("OR", "|")
                .replace("NOT", "~")
            )
            graph[target] = op
    return graph


@timer
def part_one(file: str, day: int = 7, year: int = 2015, wire: str = "a") -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    graph = _parse_instructions(input_file_path)
    processed_graph = _replace_with_int_where_possible(graph)

    print(f"Post processing: {processed_graph=}")

    while True:
        for letter, value in processed_graph.items():
            if isinstance(value, int):
                if letter == wire:
                    print(f"BEFORE RETURN: {processed_graph=}")
                    return value
                processed_graph = _replace_with_int_where_possible(processed_graph)
                continue
            split_val = value.split(" ")
            if len(split_val) == 1:
                continue
            try:
                int(split_val[0])
                int(split_val[-1])
            except ValueError:
                continue
            if len(split_val[0]) > 1 and split_val[0][0] == "0":
                split_val[0] = split_val[0][1:]
                value = " ".join(split_val)
            if len(split_val[-1]) > 1 and split_val[-1][0] == "0":
                split_val[-1] = split_val[-1][1:]
                value = " ".join(split_val)
            processed_graph[letter] = eval(value)
            processed_graph = _replace_with_int_where_possible(processed_graph)
            if letter == wire:
                print(f"BEFORE RETURN: {processed_graph=}")
                return graph[letter]
        continue

    return -1


def _replace_with_int_where_possible(graph: dict[str, str]) -> dict[str, str]:
    for letter, value in graph.items():
        try:
            val = int(value)
        except ValueError:
            continue
        for l, v in graph.items():
            if not isinstance(v, int) and letter in v:
                graph[l] = v.replace(letter, str(val))
    return graph


# part_one(file="eg", wire="e")
part_one(file="input", wire="a")


@timer
def part_two(file: str, day: int = 7, year: int = 2015):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    return _parse_instructions(file_path=input_file_path)


# part_two(file="eg")
# part_two(file="input")
