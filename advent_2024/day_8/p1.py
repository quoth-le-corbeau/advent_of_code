import collections
import time
import pathlib

"""
Resonant Collinearity

scan through the map
note the total rows and columns
create an antenna_dict with:
key = freq str
value = location tuples (row, col)
    e.g {
            '0': [(1, 8), (2, 5), (3, 7), (4, 4)]
            'A': [(5, 6), (8, 8), (9,9)]
        }
create an antinode dict using all keys {antenna: set(), for antenna in a_dict}
    use a set since the locations must be unique!
loop through antenna_dict.items()
for each node in values find distance to another
    e.g (1, 8), (2, 5) = (1, -3) in direction a -> b !
and append the antinodes on either side:
    e.g apply 2 x vector (2, -6) -> (3, 2)
        and the inverse vector (-1, 3) -> (0, 11)
    e.g antinode_dict now looks like this:
        {'0': {(3,2), (0, 11)}}
finally sum the lengths of all values in the antinode_dict

"""


def count_unique_antinodes(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        row_count = len(lines)
        col_count = len(lines[0])
        antenna_dict = collections.defaultdict(list)
        for r, row in enumerate(lines):
            for c, col in enumerate(row):
                if col != ".":
                    if col in antenna_dict:
                        antenna_dict[col].append((r, c))
                    else:
                        antenna_dict[col] = [(r, c)]
        # print(f"{antenna_dict=}")
        antinode_dict = {antenna: set() for antenna in antenna_dict}
        # print(f"{antinode_dict=}")
        for antenna, positions in antenna_dict.items():
            for idx, position in enumerate(positions):
                for other in positions[idx:]:
                    distance = other[0] - position[0], other[1] - position[1]
                    dd = (distance[0] * 2, distance[1] * 2)
                    di = (-distance[0], -distance[1])
                    new_1 = position[0] + dd[0], position[1] + dd[1]
                    new_2 = position[0] + di[0], position[1] + di[1]
                    if 0 <= new_1[0] < row_count and 0 < new_1[1] < col_count:
                        antinode_dict[antenna].add(new_1)
                    if 0 <= new_2[0] < row_count and 0 <= new_2[1] < col_count:
                        antinode_dict[antenna].add(new_2)
        print(f"{antinode_dict=}")
        return sum([len(vals) for vals in antinode_dict.values()])


start = time.perf_counter()
print(
    count_unique_antinodes(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_8"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

# start = time.perf_counter()
# print(count_unique_antinodes(str((pathlib.Path(__file__).resolve().parents[2] / "my_inputs/2024/day_8" / "input.txt"))))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
