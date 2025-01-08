import heapq
from collections import deque
from pathlib import Path
from typing import Optional

from tqdm import tqdm

from reusables import timer, INPUT_PATH


class RaceTrack:
    def __init__(self, file: str):
        with open(
            file=Path(__file__).resolve().parents[2] / file, mode="r"
        ) as puzzle_input:
            grid_lines = puzzle_input.read().strip().splitlines()
            self.row_count = len(grid_lines)
            self.col_count = len(grid_lines[0])
            self.barriers = set()
            self.start = ""
            self.end = ""
            for r, row in enumerate(grid_lines):
                for c, col in enumerate(row):
                    if col == "S":
                        self.start = (r, c)
                    elif col == "E":
                        self.end = (r, c)
                    elif (
                        col == "#"
                        and r != 0
                        and r != self.row_count - 1
                        and c != 0
                        and c != self.col_count - 1
                    ):
                        self.barriers.add((r, c))
                    else:
                        assert col == "." or (
                            col == "#"
                            and (
                                r == 0
                                or r == self.row_count - 1
                                or c == 0
                                or c == self.col_count - 1
                            )
                        )
            if len(self.start) == 0 or len(self.end) == 0:
                raise ValueError("No Start-End found!")
            if len(self.barriers) == 0:
                raise ValueError("No Barriers found!")

    def get_base_path(
        self, barriers: Optional[set[tuple[int, int]]] = None
    ) -> tuple[int, list[tuple[int, int]]]:
        """A star shortest path using manhattan heuristic"""

        def manhattan_heuristic(a: tuple[int, int], b: tuple[int, int]) -> int:
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        if barriers is None:
            barriers = self.barriers

        pq = []
        heapq.heappush(pq, (0, self.start, [self.start]))
        visited = set()

        while len(pq) > 0:
            score, current, path = heapq.heappop(pq)
            if current in visited:
                continue
            visited.add(current)

            if current == self.end:
                return len(path) - 1, path

            for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = current[0] + direction[0], current[1] + direction[1]
                if (
                    (nr, nc) not in barriers
                    and 0 < nr < self.row_count - 1
                    and 0 < nc < self.col_count - 1
                    and (nr, nc) not in visited
                ):
                    heapq.heappush(
                        pq,
                        (
                            score + 1 + manhattan_heuristic(current, self.end),
                            (nr, nc),
                            path + [(nr, nc)],
                        ),
                    )

        raise ValueError(f"No path from {self.start} to {self.end} found!")

    def check_all_paths(self, limit: int) -> int:
        base_score, base_path = self.get_base_path()
        all_barriers = list(self.barriers)
        scores_by_removed_barrier = {}
        for i, barrier in tqdm(
            enumerate(all_barriers), desc="Checking all paths", ncols=100
        ):
            score, path = self.get_base_path(
                barriers=set(all_barriers[:i] + all_barriers[i + 1 :])
            )
            if score <= base_score - limit and barrier not in scores_by_removed_barrier:
                scores_by_removed_barrier[barrier] = path
            else:
                continue
        # for barrier, path in scores_by_removed_barrier.items():
        #    self.print_path(path=path, removed_barrier=barrier)
        return len(scores_by_removed_barrier)

    def print_path(
        self, path: list[tuple[int, int]], removed_barrier: tuple[int, int]
    ) -> None:
        grid = [["."] * self.row_count for _ in range(self.col_count)]
        for r in range(self.row_count):
            for c in range(self.col_count):
                if (
                    (r, c) in self.barriers
                    and (r, c) != removed_barrier
                    or r == self.row_count - 1
                    or c == self.col_count - 1
                    or r == 0
                    or c == 0
                ):
                    grid[r][c] = "#"
                elif (
                    (r, c) in path
                    and (r, c) != self.start
                    and (r, c) != self.end
                    and (r, c) != removed_barrier
                ):
                    grid[r][c] = "^"
                elif (r, c) == self.start:
                    grid[r][c] = "S"
                elif (r, c) == self.end:
                    grid[r][c] = "E"
                elif (r, c) == removed_barrier:
                    grid[r][c] = "1"
                else:
                    assert grid[r][c] == "."

        for row in grid:
            print("".join(row))

    def get_cheat_paths(self, cheat_limit: int = 1):
        """Use bfs and keep track of the number of # traversed"""

        queue = deque([[self.start]])
        visited = set()
        cheat_count = 0
        paths = []

        while len(queue) > 0:
            path = queue.popleft()
            current = path[-1]

            if current == self.end:
                paths.append((len(path) - 1, path))

            for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = current[0] + direction[0], current[1] + direction[1]
                if (
                    0 < nr < self.row_count - 1
                    and 0 < nc < self.col_count - 1
                    and (nr, nc) not in visited
                ):
                    if (nr, nc) in self.barriers:
                        if cheat_count >= cheat_limit:
                            continue
                        else:
                            cheat_count += 1
                            queue.append(path + [(nr, nc)])
                            visited.add((nr, nc))
                    else:
                        queue.append(path + [(nr, nc)])
                        visited.add((nr, nc))

        return paths


@timer
def part_one(filename: str, year=2024, day=20) -> None:
    input_file = INPUT_PATH.format(file=filename, year=year, day=day)
    racetrack = RaceTrack(file=input_file)
    # print(f"{racetrack.get_base_path()=}")
    print(
        f"There are {racetrack.check_all_paths(limit=100)} cheats that save 100 picoseconds. or more"
    )


# part_one("eg")
# part_one("input")


@timer
def part_two(filename: str, year: int = 2024, day: int = 20) -> None:
    input_file = INPUT_PATH.format(file=filename, year=year, day=day)
    racetrack = RaceTrack(file=input_file)
    base_paths = racetrack.get_cheat_paths(cheat_limit=0)
    print(f"{base_paths=}")
    path_20 = racetrack.get_cheat_paths(cheat_limit=20)
    print(f"{path_20=}")


part_two("eg")
