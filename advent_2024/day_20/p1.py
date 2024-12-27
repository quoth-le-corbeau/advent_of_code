import time
import pathlib
from collections import deque

from typing_extensions import Self

"""
Race Condition Part I

create the initial grid
run a bfs to calculate the normal number of picoseconds
list the positions of all the walls that are not at the edge and 

"""


class RaceTrack:
    def __init__(
        self,
        grid: list[list[str]],
    ):
        self.grid = grid
        self._walls = []

    @classmethod
    def parse_file(cls, file_path: pathlib.Path) -> Self:
        with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
            return cls(
                grid=[list(line) for line in puzzle_input.read().strip().splitlines()]
            )

    def get_start_end(self) -> tuple[tuple[int, int], tuple[int, int]]:
        s = None
        e = None
        for r, row in enumerate(self.grid):
            for c, col in enumerate(row):
                if col == "S":
                    s = r, c
                elif col == "E":
                    e = r, c
        if s is None or e is None:
            raise ValueError
        return s, e

    def get_shortest_route_and_picos(self) -> tuple[list[tuple[int, int]], int]:
        s, e = self.get_start_end()
        queue = deque([[s]])
        visited = {s}
        while queue:
            path = queue.popleft()
            current = path[-1]
            if current == e:
                return path, len(path) - 1

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = current[0] + dr, current[1] + dc
                if (
                    0 <= nr < len(self.grid) - 1
                    and 0 <= nc < len(self.grid[0]) - 1
                    and self.grid[nr][nc] != "#"
                    and (nr, nc) not in visited
                ):
                    queue.append(path + [(nr, nc)])
                    visited.add((nr, nc))
        raise ValueError

    def get_race_track_walls(self) -> list[tuple[int, int]]:
        s, e = self.get_start_end()
        queue = deque([[s]])
        visited = {s}
        walls = []
        while queue:
            path = queue.popleft()
            current = path[-1]
            if current == e:
                return walls

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = current[0] + dr, current[1] + dc
                if 0 <= nr < len(self.grid) - 1 and 0 <= nc < len(self.grid[0]) - 1:
                    if self.grid[nr][nc] != "#" and (nr, nc) not in visited:
                        queue.append(path + [(nr, nc)])
                        visited.add((nr, nc))
                    elif self.grid[nr][nc] == "#":
                        walls.append((nr, nc))
        raise ValueError

    def get_cheats(self, saved_picos: int):
        walls = self.get_race_track_walls()
        picos = self.get_shortest_route_and_picos()[1]
        cheats = []
        for wall in walls:
            self.grid[wall[0]][wall[1]] = "."
            try:
                cheat_path = self.get_shortest_route_and_picos()
            except ValueError:
                continue
            if picos - cheat_path[1] >= saved_picos:
                cheats.append(cheats)
            self.grid[wall[0]][wall[1]] = "#"
        return len(cheats)

    def pprint(self):
        for line in self.grid:
            print("".join(line))


def count_100_saving_cheats(file_path: pathlib.Path):
    race_track = RaceTrack.parse_file(file_path=file_path)
    # race_track.pprint()
    return race_track.get_cheats(saved_picos=100)


timer_start = time.perf_counter()
print(
    count_100_saving_cheats(
        file_path=pathlib.Path(__file__).resolve().parents[2]
        / "my_inputs/2024/day_20"
        / "eg.txt"
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

# timer_start = time.perf_counter()
# print(
#    count_100_saving_cheats(
#        file_path=pathlib.Path(__file__).resolve().parents[2]
#        / "my_inputs/2024/day_20"
#        / "input.txt"
#    )
# )
# print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
