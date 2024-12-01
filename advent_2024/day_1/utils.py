import pathlib


def parse_into_equal_length_lists(file_path: str) -> tuple[list[int], list[int]]:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        list_1 = []
        list_2 = []
        for line in lines:
            integer_1, integer_2 = tuple(map(int, line.replace("   ", ",").split(",")))
            list_1.append(integer_1)
            list_2.append(integer_2)
        assert len(list_1) == len(list_2)
        return list_1, list_2
