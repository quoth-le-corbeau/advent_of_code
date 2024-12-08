import collections
import time
import pathlib

"""
Resonant Collinearity Part 2

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
for each position_node get the unit vector to every other position_node in the set
make a list of every equally spaced diagonal within the grid bounds in both directions from the position_node
append every diagonal position to the antinodes dict
create the final set and append the unions of all values from the antinode dict
finally sum the lengths of all values in the final set

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
        antinode_dict = {antenna: set() for antenna in antenna_dict}
        for antenna, positions in antenna_dict.items():
            for idx, position in enumerate(positions):
                for other in positions[idx + 1 :]:
                    vector = other[0] - position[0], other[1] - position[1]
                    diagonal_1 = set()
                    diagonal_2 = set()
                    multiplier = 1
                    while (
                        0 <= position[0] + (vector[0] * multiplier) < row_count
                        and 0 <= position[1] + (vector[1] * multiplier) < col_count
                    ):
                        diagonal_1.add(
                            (
                                position[0] + (vector[0] * multiplier),
                                position[1] + (vector[1] * multiplier),
                            )
                        )

                        multiplier += 1
                    multiplier_2 = 0
                    while (
                        0 <= position[0] + (vector[0] * -multiplier_2) < row_count
                        and 0 <= position[1] + (vector[1] * -multiplier_2) < col_count
                    ):
                        diagonal_2.add(
                            (
                                position[0] + (vector[0] * -multiplier_2),
                                position[1] + (vector[1] * -multiplier_2),
                            )
                        )
                        multiplier_2 += 1
                    diagonal = diagonal_1 | diagonal_2
                    antinode_dict[antenna] |= diagonal
        final_set = set()
        for _, antinodes in antinode_dict.items():
            final_set |= antinodes
        return len(final_set)


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

start = time.perf_counter()
print(
    count_unique_antinodes(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_8"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
