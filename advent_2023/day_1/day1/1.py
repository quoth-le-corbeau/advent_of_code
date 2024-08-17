import pathlib
import time
import re


def sum_calibration_values(file: str) -> int:
    return find_and_sum_digits(file=file)


def find_and_sum_digits(file: str) -> int:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        all_calibration_values = []
        for line in lines:
            all_digits = re.findall(r"[0-9]", line)
            calibration_value = f"{all_digits[0]}{all_digits[-1]}"
            all_calibration_values.append(int(calibration_value))
        return sum(all_calibration_values)


start = time.perf_counter()
print(sum_calibration_values("eg1.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(sum_calibration_values("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
