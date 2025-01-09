from collections import defaultdict
from pathlib import Path
from reusables import timer, INPUT_PATH


class Network:
    def __init__(self, file: Path):
        with open(
            file=Path(__file__).resolve().parents[2] / file, mode="r"
        ) as puzzle_input:
            connection_pairs = [
                line.split("-") for line in puzzle_input.read().strip().splitlines()
            ]
            self.connections = defaultdict(set)
            for pair in connection_pairs:
                c1, c2 = pair[0], pair[1]
                self.connections[c1].add(c2)
                self.connections[c2].add(c1)

    def find_three_connected(self):
        triples = set()
        for node, connected in self.connections.items():
            for c1 in connected:
                for c2 in connected:
                    if (
                        c1 != c2
                        and node in self.connections[c1]
                        and c2 in self.connections[c1]
                        and node in self.connections[c2]
                        and c1 in self.connections[c2]
                        and any(x.startswith("t") for x in [node, c1, c2])
                    ):
                        triple = sorted([node, c1, c2])
                        triples.add(tuple(triple))
        # for triple in triples:
        #    print(triple)
        return len(triples)

    def find_most_connected(self):
        pass


@timer
def part_one(filename: str, year: int = 2024, day: int = 23):
    input_path = INPUT_PATH.format(file=filename, year=year, day=day)
    network = Network(file=input_path)
    print(network.find_three_connected())


# part_one("input")


@timer
def part_two(filename: str, year: int = 2024, day: int = 23):
    input_path = INPUT_PATH.format(file=filename, year=year, day=day)
    network = Network(file=input_path)
    print(network.find_most_connected())


part_two("eg")
