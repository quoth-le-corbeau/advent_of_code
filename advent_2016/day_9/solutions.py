from pathlib import Path

from reusables import timer, INPUT_PATH


def _parse_compressed_file(file_path: Path) -> str:
    with open(file_path, "r") as puzzle_input:
        return puzzle_input.read().strip()


def _parse(marker: str) -> tuple[int, int]:
    stripped = marker[1:-1].split("x")
    return int(stripped[0]), int(stripped[1])


@timer
def part_one_naive(file: str, day: int = 9, year: int = 2016) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    compressed = _parse_compressed_file(file_path=input_file_path)
    print(f"{compressed=}")
    decompressed = ""
    pointer = 0
    while pointer < len(compressed):
        char = compressed[pointer]
        if char == "(":
            marker = ""
            i = 0
            while compressed[pointer + i] != ")":
                marker += compressed[pointer + i]
                i += 1
            pointer += i
            end_marker = compressed[pointer]
            if end_marker != ")":
                raise ValueError(f"Unknown end marker: {end_marker}")
            marker = marker + end_marker
            number_of_chars_to_repeat, repetitions = _parse(marker)
            pointer += 1
            end_pointer = pointer + number_of_chars_to_repeat
            to_repeat = compressed[pointer:end_pointer]
            decompressed += to_repeat * repetitions
            pointer = end_pointer - 1
        else:
            decompressed += char
        pointer += 1

    print(f"{decompressed=}")
    return len(decompressed)


@timer
def part_one(file: str, day: int = 9, year: int = 2016) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    compressed = _parse_compressed_file(file_path=input_file_path)


part_one(file="eg")
part_one(file="eg2")
part_one(file="eg3")
part_one(file="eg4")
part_one(file="eg5")
part_one(file="eg6")
part_one(file="input")


@timer
def part_two(file: str, day: int = 9, year: int = 2016):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    compressed = _parse_compressed_file(file_path=input_file_path)
    print(f"{compressed=}")


# part_two(file="eg3")
# part_two(file="eg6")
# part_two(file="input")
