import time
import pathlib
import heapq
from typing import List, Tuple, Optional


def _get_start_end(grid) -> tuple[tuple[int, int], tuple[int, int]]:
    start_ = None
    end_ = None
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "S":
                start_ = r, c
            if col == "E":
                end_ = r, c
    if start_ is None or end_ is None:
        raise ValueError("No start or end found")
    return start_, end_


def _get_path_score(path: list[tuple[int, int]]) -> int:
    turn_count = 0
    total_forward_steps = len(path) - 1
    current_direction = "east"
    for i in range(2, len(path)):
        next_direction = _get_current_direction(path[i], path[i - 1])
        if next_direction != current_direction:
            turn_count += 1
            current_direction = next_direction

    return turn_count * 1000 + total_forward_steps


def _get_current_direction(node, prev):
    if node[0] == prev[0]:
        if node[1] - prev[1] == 1:
            return "east"
        else:
            assert node[1] - prev[1] == -1
            return "west"
    else:
        assert node[0] != prev[0]
        if node[0] - prev[0] == 1:
            return "south"
        else:
            assert node[0] - prev[0] == -1
            return "north"


# this returns the shortest path using only manhattan heuristic (not part of solution)
def _a_star(
    grid: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]
) -> List[Tuple[int, int]]:
    row_count = len(grid)
    col_count = len(grid[0])

    def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    pq = []
    heapq.heappush(pq, (0, start, [start]))

    visited = set()
    visited.add(start)

    while pq:
        cost, current, path = heapq.heappop(pq)

        if current == end:
            return path

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = current[0] + dr, current[1] + dc

            if (
                0 <= nr < row_count
                and 0 <= nc < col_count
                and (grid[nr][nc] == "." or (nr, nc) == end)
            ):
                neighbor = (nr, nc)
                if neighbor not in visited:
                    visited.add(neighbor)
                    # Priority: path cost + heuristic estimate to goal
                    priority = cost + 1 + heuristic(neighbor, end)
                    heapq.heappush(pq, (priority, neighbor, path + [neighbor]))

    return []


# this returns the best path according to the turn minimization rule
def _a_star_minimize_turns(
    grid: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]
) -> Optional[List[Tuple[int, int]]]:
    row_count = len(grid)
    col_count = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (up, down, left, right)
    direction_labels = ["up", "down", "left", "right"]

    def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    pq = []
    heapq.heappush(pq, (0, 0, start, None, [start]))
    visited = {}

    while pq:
        priority, cost, current, current_direction, path = heapq.heappop(pq)

        if current == end:
            return path

        if current in visited and visited[current] <= cost:
            continue
        visited[current] = cost

        for i, (dr, dc) in enumerate(directions):
            nr, nc = current[0] + dr, current[1] + dc
            next_direction = direction_labels[i]

            if (
                0 <= nr < row_count
                and 0 <= nc < col_count
                and (grid[nr][nc] == "." or (nr, nc) == end)
            ):
                turn_penalty = (
                    1000
                    if current_direction and current_direction != next_direction
                    else 0
                )
                next_cost = cost + 1 + turn_penalty
                next_priority = next_cost + heuristic((nr, nc), end)
                heapq.heappush(
                    pq,
                    (
                        next_priority,
                        next_cost,
                        (nr, nc),
                        next_direction,
                        path + [(nr, nc)],
                    ),
                )

    return None


def find_best_reindeer_path(file_path: str):
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        grid = [list(line) for line in puzzle_input.read().splitlines()]
        start_, end_ = _get_start_end(grid)
        # best_path = _a_star(grid=grid, start=start_, end=end_)
        best_path = _a_star_minimize_turns(grid=grid, start=start_, end=end_)
        print(f"{best_path=}")
        return _get_path_score(best_path)


start = time.perf_counter()
print(
    find_best_reindeer_path(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_16"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    find_best_reindeer_path(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_16"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
