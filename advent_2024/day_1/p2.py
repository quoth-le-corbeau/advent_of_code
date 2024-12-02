import time

from advent_2024.day_1 import utils


def calculate_similarity_score(file_path: str) -> int:
    locations_1, locations_2 = utils.parse_into_equal_length_lists(file_path)
    similarity_score = 0
    for location in locations_1:
        similarity_score += location * locations_2.count(location)
    return similarity_score


start = time.perf_counter()
print(calculate_similarity_score("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(calculate_similarity_score("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
