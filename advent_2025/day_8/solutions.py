from pathlib import Path
import math
from functools import cache
from reusables import timer, INPUT_PATH


Coordinate = type(tuple[int, int, int])


def _parse_input(file_path: Path) -> list[Coordinate]:
    with open(file_path, "r") as puzzle_input:
        return [
            tuple(map(int, line.split(",")))
            for line in puzzle_input.read().strip().splitlines()
        ]


@cache
def _str_ln_distance(a: Coordinate, b: Coordinate) -> float:
    p1, p2, p3 = a
    q1, q2, q3 = b
    d = math.sqrt(((p1 - q1) ** 2) + ((p2 - q2) ** 2) + ((p3 - q3) ** 2))
    return round(d, ndigits=8)


@timer
def part_one(file: str, day: int = 8, year: int = 2025, n: int = 1000):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    coordinates = _parse_input(file_path=input_file_path)
    distances = sorted(
        [
            (_str_ln_distance(a, b), a, b)
            for i, a in enumerate(coordinates)
            for b in coordinates[i + 1 :]  # Only compare each pair once
        ]
    )
    # print(
    #    f"Total unique pairs: {len(distances)} should be (n * (n-1)) / 2 where n = len(coordinates) "
    #    f"check: {(n**2)//2 - (n//2)}"
    # )
    circuits = []
    for i in range(n):
        _, a, b = distances[i]

        circuit_a = None
        circuit_b = None

        for circuit in circuits:
            if a in circuit:
                circuit_a = circuit
            if b in circuit:
                circuit_b = circuit

        if circuit_a is None and circuit_b is None:
            circuits.append([a, b])
        elif circuit_a == circuit_b:
            pass
        elif circuit_a is not None and circuit_b is None:
            circuit_a.append(b)
        elif circuit_b is not None and circuit_a is None:
            circuit_b.append(a)
        else:
            circuit_a.extend(circuit_b)
            circuits.remove(circuit_b)

    all_circuits = sorted(circuits, key=len, reverse=True)
    return len(all_circuits[0]) * len(all_circuits[1]) * len(all_circuits[2])


part_one(file="eg", n=10)
part_one(file="input")


@timer
def part_two(file: str, day: int = 8, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    coordinates = _parse_input(file_path=input_file_path)
    distances = sorted(
        [
            (_str_ln_distance(a, b), a, b)
            for i, a in enumerate(coordinates)
            for b in coordinates[i + 1 :]  # Only compare each pair once
        ]
    )
    # print(
    #    f"Total unique pairs: {len(distances)} should be (n * (n-1)) / 2 where n = len(coordinates) "
    #    f"check: {(n**2)//2 - (n//2)}"
    # )
    circuits = []
    counter = 0
    while True:
        _, a, b = distances[counter]

        circuit_a = None
        circuit_b = None

        for circuit in circuits:
            if a in circuit:
                circuit_a = circuit
            if b in circuit:
                circuit_b = circuit

        if circuit_a is None and circuit_b is None:
            circuits.append([a, b])
        elif circuit_a == circuit_b:
            pass
        elif circuit_a is not None and circuit_b is None:
            circuit_a.append(b)
        elif circuit_b is not None and circuit_a is None:
            circuit_b.append(a)
        else:
            circuit_a.extend(circuit_b)
            circuits.remove(circuit_b)

        if len(circuits) == 1 and len(circuits[0]) == len(coordinates):
            print(f"{a=}")
            print(f"{b=}")
            return a[0] * b[0]

        counter += 1


part_two(file="eg")
part_two(file="input")
