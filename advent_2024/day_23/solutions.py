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
        return len(triples)

    def crack_password_fail_for_real_input(self) -> str:
        for key, connected in self.connections.items():
            for conn in connected:
                self.connections[conn].remove(key)

        largest_group_size = 0
        largest_group = {}
        for key, values in self.connections.items():
            values_list = list(values)
            group = {key}
            for i, val in enumerate(values_list):
                for other in values_list[:i] + values_list[i + 1 :]:
                    if other in self.connections[val] or val in self.connections[other]:
                        group.add(other)
                        group.add(val)

                    if len(group) > largest_group_size:
                        largest_group_size = len(group)
                        largest_group = group

        print(largest_group_size, largest_group)
        alphabetical_group = sorted(list(largest_group))
        return ",".join(alphabetical_group)

    def generate_edges(self):
        edges = []
        # for each node in self.connections
        for node in self.connections:

            # for each neighbour node of a single node
            for neighbour in self.connections[node]:
                # if edge exists then append
                edges.append((node, neighbour))
        return edges


@timer
def part_one(filename: str, year: int = 2024, day: int = 23):
    input_path = INPUT_PATH.format(file=filename, year=year, day=day)
    network = Network(file=input_path)
    print(f"part one: {network.find_three_connected()}")


part_one("input")


@timer
def part_two(filename: str, year: int = 2024, day: int = 23):
    input_path = INPUT_PATH.format(file=filename, year=year, day=day)
    network = Network(file=input_path)
    edges = network.generate_edges()
    print(f"{edges=}")
    # password = network.crack_password_fail_for_real_input()
    # print(password)


part_two("eg")
part_two("input")
