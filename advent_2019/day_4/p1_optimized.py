import time
import pathlib


def count_possible_passwords(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        password_range_map = tuple(map(int, puzzle_input.read().strip().split("-")))
        count = 0
        for n in range(password_range_map[0], password_range_map[1]):
            if str(n) == "".join(sorted(str(n))) and _contains_adjacent_pair(
                num_string=str(n)
            ):
                count += 1
        return count


def _contains_adjacent_pair(num_string: str) -> bool:
    i = 0
    while i < len(num_string) - 1:
        if num_string[i + 1] == num_string[i]:
            return True
        i += 1
    return False


timer_start = time.perf_counter()
print(
    count_possible_passwords(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2019/day_4"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
