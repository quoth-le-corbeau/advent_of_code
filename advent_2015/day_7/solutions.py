from pathlib import Path

from reusables import timer, INPUT_PATH


# https://wiki.python.org/moin/BitwiseOperators


# Algorithm:
# represent as graph with a dict:
eg_dict: dict[str, int | str] = {
    "d": "x & y",
    "e": "d + x",
    "x": 123,
    "y": 456,
}


def _get_signals(eg_dict: dict[str, int | str]) -> dict[str, int]:
    res = dict()
    for k, v in eg_dict.items():
        if isinstance(v, int):
            res[k] = v
        else:
            assert isinstance(v, str)
            x, cmd, y = v.split(" ")


_get_signals(eg_dict)


def _parse_instructions(file_path: Path) -> [str, int | str]:
    with open(file_path, "r") as puzzle_input:
        for line in puzzle_input.read().strip().splitlines():
            cmd, k = line.split(" -> ")
            # use s.isdigit()


@timer
def part_one(file: str, day: int = 7, year: int = 2015) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    signals_by_wire = dict()
    for k, v in _parse_instructions(file_path=input_file_path).items():
        signals_by_wire[k] = eval(v)
    return signals_by_wire["a"]


# part_one(file="eg")
# part_one(file="input")


@timer
def part_two(file: str, day: int = 7, year: int = 2015):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    return _parse_instructions(file_path=input_file_path)


# part_two(file="eg")
# part_two(file="input")
