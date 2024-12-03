import time
import pathlib


def calculate_similarity_score(file_path: str) -> int:
    locations_1, locations_2 = _parse_into_equal_length_lists(file_path)
    similarity_score = 0
    for location in locations_1:
        similarity_score += location * locations_2.count(location)
    return similarity_score


def _parse_into_equal_length_lists(file_path: str) -> tuple[list[int], list[int]]:
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


start = time.perf_counter()
print(
    calculate_similarity_score(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_1"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    calculate_similarity_score(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_1"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
