from pathlib import Path
from collections import Counter
from reusables import timer, INPUT_PATH


def _parse_signal(file_path: Path):
    with open(file_path, "r") as puzzle_input:
        return puzzle_input.read().strip().splitlines()


@timer
def part_one(file: str, day: int = 6, year: int = 2016) -> str:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    signal_rows = _parse_signal(file_path=input_file_path)
    return "".join(
        [
            Counter([signal_row[i] for signal_row in signal_rows]).most_common()[0][0]
            for i in range(len(signal_rows[0]))
        ]
    )


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 6, year: int = 2016):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    signal_rows = _parse_signal(file_path=input_file_path)
    return "".join(
        [
            Counter([signal_row[i] for signal_row in signal_rows]).most_common()[-1][0]
            for i in range(len(signal_rows[0]))
        ]
    )


part_two(file="eg")
part_two(file="input")
