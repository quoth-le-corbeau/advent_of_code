from pathlib import Path
from reusables import timer, INPUT_PATH


class Lab:
    def __init__(self, file: str):
        self._vectors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        with open(
            file=Path(__file__).resolve().parents[2] / file, mode="r", encoding="utf-8"
        ) as puzzle_input:
            grid_lines = puzzle_input.read().strip()
            self.objects = set()
            self.points = set()
            self.position = None
            self.row_bound = 0
            self.column_bound = 0
            for r, row in enumerate(grid_lines.splitlines()):
                self.row_bound = r
                for c, col in enumerate(row):
                    self.column_bound = c
                    if col == "#":
                        self.objects.add((r, c))
                    elif col == "^":
                        # print(f"start = {r}, {c}")
                        self.position = (r, c)
                    else:
                        assert col == "."
                        self.points.add((r, c))
            if self.position is None:
                raise ValueError("No position found")
            if self.row_bound <= 0 or self.column_bound <= 0:
                raise ValueError("Row and column bounds must be positive")
            self.row_bound += 1
            self.column_bound += 1
            # print(f"{len(self.objects)=}")
            # print(f"{len(self.points)=}")
            # print(f"{sorted(list(self.points))=}")

    def step(self, vector: tuple[int, int]) -> None:
        self.position = self.position[0] + vector[0], self.position[1] + vector[1]

    def walk_out(self) -> list[tuple[int, int]]:
        visited = {self.position}
        vector_index = 0
        vector = self._vectors[vector_index]
        while (
            0 <= self.position[0] < self.row_bound
            and 0 <= self.position[1] < self.column_bound
        ):
            next_step = self.position[0] + vector[0], self.position[1] + vector[1]
            if next_step in self.objects:
                vector_index += 1
                vector_index = vector_index % len(self._vectors)
            vector = self._vectors[vector_index]
            self.step(vector=vector)
            if (
                0 <= self.position[0] < self.row_bound
                and 0 <= self.position[1] < self.column_bound
            ):
                visited.add(self.position)
        # debugging
        # self.print_path(visited)
        # print(f"{sorted(list(visited))=}")
        return sorted(list(visited))

    def _check_infinite_loop(self, start: tuple[int, int]) -> bool:
        self.position = start
        vector_index = 0
        vector = self._vectors[vector_index]
        visited = set()
        while True:
            if (self.position, vector) in visited:
                return True
            visited.add((self.position, vector))
            if not (
                0 <= self.position[0] + vector[0] < self.row_bound
                and 0 <= self.position[1] + vector[1] < self.column_bound
            ):
                return False
            nr, nc = self.position[0] + vector[0], self.position[1] + vector[1]
            if (nr, nc) in self.objects:
                vector_index += 1
                vector = self._vectors[vector_index % 4]
            else:
                self.step(vector)

    def create_infinite_loops(self) -> list[tuple[int, int]]:
        self.position = (45, 47)
        loop_creators = []
        for node in self.walk_out():
            self.objects.add(node)
            if self._check_infinite_loop(start=(45, 47)):
                loop_creators.append(node)
            self.objects.remove(node)
        # print(f"{sorted(loop_creators)=}")
        return loop_creators

    def print_path(self, visited: set[tuple[int, int]]) -> None:
        grid = [["."] * (self.column_bound + 1) for _ in range(self.row_bound + 1)]
        for r in range(self.row_bound + 1):
            for c in range(self.column_bound + 1):
                if (r, c) in visited:
                    assert (r, c) not in self.objects
                    grid[r][c] = "|"
                if (r, c) in self.objects:
                    grid[r][c] = "#"
        for line in grid:
            print("".join(line))


def _initialise_puzzle(file: str) -> Lab:
    return Lab(INPUT_PATH.format(file=file, year=2024, day=6))


@timer
def part_one(filename: str):
    lab = _initialise_puzzle(file=filename)
    print(f"part 1: {len(lab.walk_out())} <- ({filename})")


# part_one("eg")
part_one("input")


@timer
def part_two(filename: str):
    lab = _initialise_puzzle(file=filename)
    print(f"part 2: {len(lab.create_infinite_loops())} <- ({filename})")


# part_two("eg")
part_two("input")
