from pathlib import Path

from reusables import timer, INPUT_PATH


class Grid:
    def __init__(self, file_path: Path):
        with open(file_path, "r") as puzzle_input:
            self.moves = puzzle_input.read().strip().split(", ")
            self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            self.initial_position = (0, 0)
            self.direction_increment = 0
            self.visited = {(0, 0)}
            for move in self.moves:
                assert move[0] in ["R", "L"]

    def move_until_cross(self) -> int:
        pr = 0
        pc = 0
        for move in self.moves:
            increment = 1 if move[0] == "R" else -1
            self.direction_increment += increment
            direction_vector = self.directions[self.direction_increment % 4]
            dr, dc = direction_vector[0], direction_vector[1]
            for i in range(int(move[1:])):
                pr += dr
                pc += dc
                if (pr, pc) in self.visited:
                    return self.manhattan(point=(pr, pc))
                else:
                    self.visited.add((pr, pc))

    def move(self) -> int:
        pr = 0
        pc = 0
        for move in self.moves:
            increment = 1 if move[0] == "R" else -1
            self.direction_increment += increment
            direction_vector = self.directions[self.direction_increment % 4]
            dr, dc = direction_vector[0], direction_vector[1]
            for i in range(int(move[1:])):
                pr += dr
                pc += dc
        return self.manhattan(point=(pr, pc))

    def manhattan(self, point: tuple[int, int]) -> int:
        return abs(point[0] - self.initial_position[0]) + abs(
            point[1] - self.initial_position[1]
        )


def locate_easter_bunny_hq(file_path: Path) -> int:
    grid = Grid(file_path=file_path)
    location = grid.move()
    return location


def locate_easter_bunny_hq_2(file_path: Path) -> int:
    grid = Grid(file_path=file_path)
    location = grid.move_until_cross()
    return location


@timer
def part_one(file: str, day: int = 1, year: int = 2016):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    print(f"Part 1: {locate_easter_bunny_hq(file_path=input_file_path)}")


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 1, year: int = 2016):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    print(f"Part 2: {locate_easter_bunny_hq_2(file_path=input_file_path)}")


part_two(file="eg2")
part_two(file="input")
