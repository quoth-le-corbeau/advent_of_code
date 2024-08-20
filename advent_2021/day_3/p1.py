import time
import pathlib
import pandas


def calculate_power_consumption(file_path: str):
    diagnostic: pandas.DataFrame = _read_diagnostic(file=file_path)
    gamma_rate_bin = diagnostic.mode(axis=0).values[0]
    epsilon_rate_bin = [abs(1 - digit) for digit in gamma_rate_bin]
    gamma_rate = _binary_to_base_ten(binary_digits=gamma_rate_bin)
    epsilon_rate = _binary_to_base_ten(binary_digits=epsilon_rate_bin)
    print(f"{gamma_rate=}")
    print(f"{epsilon_rate=}")
    return gamma_rate * epsilon_rate


def _binary_to_base_ten(binary_digits: list[int]) -> int:
    order = len(binary_digits)
    rate = 0
    for i, value in enumerate(binary_digits):
        rate += 2 ** (order - (i + 1)) * value
    return rate


def _read_diagnostic(file: str) -> pandas.DataFrame:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        grid = [list(map(int, line)) for line in lines]
        return pandas.DataFrame(grid, columns=[i + 1 for i in range(len(lines[0]))])


start = time.perf_counter()
print(calculate_power_consumption("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(calculate_power_consumption("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
