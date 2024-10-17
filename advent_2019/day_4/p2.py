import time
import pathlib


def count_possible_passwords_2(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        password_range_map = tuple(map(int, puzzle_input.read().strip().split("-")))
        count = 0
        for n in range(password_range_map[0], password_range_map[1]):
            if str(n) == "".join(sorted(str(n))) and _contains_adjacent_exact_pair(
                num_string=str(n)
            ):
                count += 1
        return count


def _contains_adjacent_exact_pair(num_string: str) -> bool:
    i = 0
    end_index = len(num_string) - 1
    count = 0
    while i < end_index:
        if num_string[i + 1] != num_string[i] and count == 1:
            return True
        elif num_string[i + 1] == num_string[i]:
            count += 1
        else:
            count = 0
        i += 1
    if count == 1:
        return True
    return False


start = time.perf_counter()
print(count_possible_passwords_2("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
