import time
import pathlib
import re
import dataclasses


@dataclasses.dataclass(frozen=True)
class Passwd:
    character: str
    index_1: int
    index_2: int

    def is_valid(self, entry: str) -> bool:
        return (
            entry[self.index_1 - 1] == self.character
            and entry[self.index_2 - 1] != self.character
        ) or (
            entry[self.index_1 - 1] != self.character
            and entry[self.index_2 - 1] == self.character
        )


def count_valid_passwords(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        valid_passwd_count: int = 0
        for line in lines:
            rule, entry = line.split(": ")
            indexes = list(map(int, re.findall(r"\d+", rule)))
            passwd = Passwd(character=rule[-1], index_1=indexes[0], index_2=indexes[1])
            if passwd.is_valid(entry=entry):
                valid_passwd_count += 1
        return valid_passwd_count


timer_start = time.perf_counter()
print(
    count_valid_passwords(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2020/day_2"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    count_valid_passwords(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2020/day_2"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
