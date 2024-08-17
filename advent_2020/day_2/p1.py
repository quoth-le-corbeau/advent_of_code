import time
import pathlib
import re
import dataclasses


@dataclasses.dataclass(frozen=True)
class Passwd:
    character: str
    min_occurences: int
    max_occurences: int

    def is_valid(self, entry: str) -> bool:
        occurences = entry.count(self.character)
        return self.min_occurences <= occurences <= self.max_occurences


def count_valid_passwords(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        valid_passwd_count: int = 0
        for line in lines:
            rule, entry = line.split(": ")
            min_max = list(map(int, re.findall(r"\d+", rule)))
            passwd = Passwd(
                character=rule[-1], min_occurences=min_max[0], max_occurences=min_max[1]
            )
            if passwd.is_valid(entry=entry):
                valid_passwd_count += 1
        return valid_passwd_count


start = time.perf_counter()
print(count_valid_passwords("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(count_valid_passwords("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
