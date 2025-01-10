from collections import defaultdict, deque
from pathlib import Path
from reusables import timer, INPUT_PATH


class Network:
    def __init__(self, file: Path):
        with open(
            file=Path(__file__).resolve().parents[2] / file, mode="r"
        ) as puzzle_input:
            self.edges = [
                line.split("-") for line in puzzle_input.read().strip().splitlines()
            ]

            self.connections_by_node = defaultdict(set)
            for pair in self.edges:
                c1, c2 = pair[0], pair[1]
                self.connections_by_node[c1].add(c2)
                self.connections_by_node[c2].add(c1)

    def find_three_connected(self):
        triples = set()
        for node, connected in self.connections_by_node.items():
            for c1 in connected:
                for c2 in connected:
                    if (
                        c1 != c2
                        and node in self.connections_by_node[c1]
                        and c2 in self.connections_by_node[c1]
                        and node in self.connections_by_node[c2]
                        and c1 in self.connections_by_node[c2]
                        and any(x.startswith("t") for x in [node, c1, c2])
                    ):
                        triple = sorted([node, c1, c2])
                        triples.add(tuple(triple))
        return len(triples)

    def crack_password(self) -> str:
        groups = []
        for edge in self.edges:
            group = self.get_group(edge=edge)
            if (len(group), sorted(group)) not in groups:
                groups.append((len(group), sorted(group)))
        size, largest_group = sorted(groups, reverse=True)[0]
        print(f"The largest group is {largest_group} of size: {size}")
        result_group = sorted(largest_group)
        return ",".join(result_group)

    def get_group(self, edge: list[str]) -> list[str]:
        group = set()
        group.add(edge[0])
        group.add(edge[1])
        queue = deque(edge)

        while len(queue) > 0:
            node = queue.popleft()
            connections = self.connections_by_node[node]
            for connection in connections:
                if (
                    all(
                        connection in self.connections_by_node[member]
                        for member in group
                    )
                    and connection not in group
                ):
                    group.add(connection)
                    queue.append(connection)
        return list(group)


@timer
def part_one(filename: str, year: int = 2024, day: int = 23):
    input_path = INPUT_PATH.format(file=filename, year=year, day=day)
    network = Network(file=input_path)
    print(f"part one: {network.find_three_connected()}")


# part_one("eg")
part_one("input")


@timer
def part_two(filename: str, year: int = 2024, day: int = 23):
    input_path = INPUT_PATH.format(file=filename, year=year, day=day)
    network = Network(file=input_path)
    print(network.crack_password())


# part_two("eg")
part_two("input")
