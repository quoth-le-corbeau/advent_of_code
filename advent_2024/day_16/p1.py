import heapq
from collections import deque
from typing import TypeAlias
from pathlib import Path
from reusables import timer, INPUT_PATH

GridPoint: TypeAlias = tuple[int, int]
Vector: TypeAlias = tuple[int, int]


class RaceCourse:
    def __init__(
        self,
        tracks: list[GridPoint],
        seats: list[GridPoint],
        start_: GridPoint,
        end_: GridPoint,
        row_count: int,
        col_count: int,
    ):
        self.start_ = start_
        self.end_ = end_
        self.seats = seats
        self.tracks = tracks
        self.row_count = row_count
        self.col_count = col_count
        self._turn_penalty = 1000
        self._directions = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

    def get_best_path(self) -> list[GridPoint]:
        pq = []
        heapq.heappush(pq, (0, [self.start_], "E"))
        visited = dict()

        while len(pq) > 0:
            turn_count, path, last_direction = heapq.heappop(pq)
            current = path[-1]

            if current == self.end_:
                return path
            if current in visited and visited[current] <= turn_count:
                continue
            visited[current] = turn_count

            for direction, (dr, dc) in self._directions.items():
                nr, nc = current[0] + dr, current[1] + dc
                next_grid_point = (nr, nc)
                if (
                    0 <= nr < self.row_count
                    and 0 <= nc < self.col_count
                    and (nr, nc) not in self.seats
                ):
                    is_turn = last_direction != direction
                    new_turn_count = turn_count + (1 if is_turn else 0)
                    heapq.heappush(
                        pq, (new_turn_count, path + [next_grid_point], direction)
                    )
        raise ValueError

    def get_best_path_score(self) -> int:
        best_path = self.get_best_path()
        self.pprint(path=best_path)
        print(f"{best_path=}")
        turn_count = 0
        return len(best_path) + self._turn_penalty * turn_count

    def pprint(self, path: list[GridPoint]) -> None:
        grid = [["."] * self.col_count] * self.row_count
        print(grid)
        for track in self.tracks:
            grid[track[0]][track[1]] = "."
        for seat in self.seats:
            grid[seat[0]][seat[1]] = "#"
        for point in path:
            grid[point[0]][1] = "^"
        grid[self.start_[0]][self.start_[1]] = "S"
        grid[self.end_[0]][self.end_[1]] = "E"
        for line in grid:
            print("".join(line))


def _parse_race_track(
    puzzle_input,
) -> tuple[GridPoint, GridPoint, list[GridPoint], list[GridPoint], int, int]:
    start_ = None
    end_ = None
    seats = []
    tracks = []
    row_count = -1
    col_count = -1
    for r, row in enumerate(lines := puzzle_input.read().splitlines()[1:-1]):
        row_count += 1
        col_count = len(row)
        for c, col in enumerate(row):
            if col == "S":
                start_ = r, c
            elif col == "E":
                end_ = r, c
            elif col == "#":
                seats.append((r, c))
            else:
                assert col == "."
                tracks.append((r, c))
    if row_count == -1 or col_count == -1:
        raise ValueError
    return start_, end_, seats, tracks, row_count, col_count


def get_lowest_race_course_score(file_path: str) -> int:
    with open(Path(__file__).resolve().parents[2] / file_path, "r") as puzzle_input:
        start_, end_, seats, tracks, row_count, col_count = _parse_race_track(
            puzzle_input
        )
    racecourse = RaceCourse(
        start_=start_,
        end_=end_,
        seats=seats,
        tracks=tracks,
        row_count=row_count,
        col_count=col_count,
    )
    return racecourse.get_best_path_score()


@timer
def part_one(file: str, year: int = 2024, day: int = 16) -> None:
    input_file_path = INPUT_PATH.format(year=year, day=day, file=file)
    print(get_lowest_race_course_score(file_path=input_file_path))
    print(f"solution ran with file: {file}.txt")


part_one(file="eg")
part_one(file="eg2")
# part_one(file="input")
