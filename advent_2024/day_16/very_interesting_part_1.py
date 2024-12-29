from pathlib import Path
from heapq import heappop, heappush
from reusables import timer, INPUT_PATH


class ReindeerMaze:
    def __init__(self, file_path: Path):
        self.grid = []
        self.start = None
        self.end = None
        self.initial_direction = (0, 1)
        self.step_score = 1
        self.rotation_score = 1000
        with open(file=file_path, mode="r") as maze_string:
            self.grid = list(
                list(line) for line in maze_string.read().strip().splitlines()
            )
            for r, row in enumerate(self.grid):
                for c, col in enumerate(row):
                    if col == "S":
                        self.start = (r, c)
                    elif col == "E":
                        self.end = (r, c)
                    else:
                        assert col in ["#", "."]
                    if r in [0, len(self.grid) - 1] or c in [0, len(self.grid[0]) - 1]:
                        assert col == "#"

    def print_maze(self) -> None:
        for row in self.grid:
            print("".join(row))

    def print_path(self, path: list[tuple[int, int]]) -> None:
        for point in path:
            r, c = point
            if point not in [self.start, self.end]:
                self.grid[r][c] = ">"
        return self.print_maze()

    def find_path(self) -> tuple[int, list[tuple[int, int]]]:
        priority_queue = []
        heappush(
            priority_queue, (0, 0, self.start, self.initial_direction, [self.start])
        )
        visited = {}

        def heuristic(a: tuple[int, int], b: tuple[int, int]) -> int:
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        while len(priority_queue) > 0:
            priority, cost, current_position, facing_direction, path = heappop(
                priority_queue
            )
            if current_position == self.end:
                return cost, path
            if current_position in visited and visited[current_position] <= cost:
                continue
            visited[current_position] = cost
            for move_cost, next_position, next_direction in self.look_ahead(
                position=current_position, direction=facing_direction
            ):
                heappush(
                    priority_queue,
                    (
                        cost + move_cost + heuristic(next_position, self.end),
                        cost + move_cost,
                        next_position,
                        next_direction,
                        path + [next_position],
                    ),
                )
        raise ValueError("No paths found!")

    def find_paths(self) -> tuple[int, list[list[tuple[int, int]]]]:
        priority_queue = []
        heappush(priority_queue, (0, self.start, self.initial_direction, [self.start]))
        visited = {}
        paths = []
        best_score = float("inf")
        while len(priority_queue) > 0:
            cost, current_position, facing_direction, path = heappop(priority_queue)
            visited[current_position] = cost
            if current_position == self.end:
                if cost <= best_score:
                    best_score = cost
                    paths.append(path)
                else:
                    return best_score, paths
            for move_cost, next_position, next_direction in self.look_ahead(
                position=current_position, direction=facing_direction
            ):
                if (
                    move_cost + cost
                    <= visited.get(next_position, float("inf")) + self.rotation_score
                ):
                    heappush(
                        priority_queue,
                        (
                            move_cost + cost,
                            next_position,
                            next_direction,
                            path + [next_position],
                        ),
                    )
        return best_score, paths

    def look_ahead(
        self, position: tuple[int, int], direction: tuple[int, int]
    ) -> list[tuple[int, tuple[int, int], tuple[int, int]]]:
        weighted_next_positions = []
        dr, dc = direction
        nr, nc = position[0] + dr, position[1] + dc
        symbol = self.grid[nr][nc]
        if symbol != "#":
            weighted_next_positions.append((self.step_score, (nr, nc), (dr, dc)))
        for possible_rotation in self.get_90_degree_rotations(unit_vector=direction):
            dr, dc = possible_rotation
            nr, nc = position[0] + dr, position[1] + dc
            symbol = self.grid[nr][nc]
            if symbol != "#":
                weighted_next_positions.append(
                    (self.step_score + self.rotation_score, (nr, nc), (dr, dc))
                )
        return weighted_next_positions

    def get_90_degree_rotations(
        self, unit_vector: tuple[int, int]
    ) -> tuple[tuple[int, int], tuple[int, int]]:
        r, c = unit_vector
        return ((r + 1) % 2, (c + 1) % 2), (-((r - 1) % 2), -((c - 1) % 2))


@timer
def part_one(file_path_extension: str, year: int = 2024, day: int = 16):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file_path_extension
    )
    print(f"AOC: {year}, Day {day} running with input: {file_path_extension}.txt")
    reindeer_maze = ReindeerMaze(file_path=input_file_path)
    # reindeer_maze.print_maze()
    score, path = reindeer_maze.find_path()
    # reindeer_maze.print_path(path=path)
    print(path)
    print(score)


# part_one(file_path_extension="eg")
# part_one(file_path_extension="eg2")
part_one(file_path_extension="input")


@timer
def part_two(file_path_extension: str, year: int = 2024, day: int = 16):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file_path_extension
    )
    print(
        f"AOC: {year}, Day {day} part II running with input: {file_path_extension}.txt"
    )
    reindeer_maze = ReindeerMaze(file_path=input_file_path)
    score, paths = reindeer_maze.find_paths()
    print(f"Best path score: {score}")
    print(paths[0])
    seats = set()
    for path in paths:
        seats = seats.union(path)
    print(len(seats))


# part_two(file_path_extension="eg")
# part_two(file_path_extension="eg2")
part_two(file_path_extension="input")
