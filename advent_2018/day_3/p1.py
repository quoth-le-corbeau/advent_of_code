import time
import pathlib


def count_overlaps(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        visited = list()
        for line in puzzle_input.read().splitlines():
            vertices = (
                line.replace(" ", "")
                .split("@")[1]
                .replace(":", ",")
                .replace("x", ",")
                .split(",")
            )
            print("---------")
            print(vertices)
            print("---------")
            for x in range(int(vertices[0], int(vertices[0]) + int(vertices[2]))):
                for y in range(int(vertices[1]), int(vertices[1]) + int(vertices[3])):
                    print(x, y)


start = time.perf_counter()
print(count_overlaps("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

# start = time.perf_counter()
# print(count_overlaps("input.txt"))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
