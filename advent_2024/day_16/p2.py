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


def _a_star_all_paths(
    grid: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]
) -> List[List[Tuple[int, int]]]:
    row_count = len(grid)
    col_count = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    direction_labels = ["up", "down", "left", "right"]

    def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    pq = []
    heapq.heappush(pq, (0, 0, start, None, [start]))  # Initial direction is None
    visited = {}
    all_best_paths = []
    min_cost = float("inf")

    while pq:
        priority, cost, current, current_direction, path = heapq.heappop(pq)

        if current == end:
            if cost < min_cost:
                min_cost = cost
                all_best_paths = [path]
            elif cost == min_cost:
                all_best_paths.append(path)
            continue

        if current in visited and visited[current] < cost:
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
                # Determine turn penalty
                turn_penalty = (
                    1
                    if current_direction and current_direction != next_direction
                    else 0
                )
                next_cost = cost + 1 + turn_penalty
                next_priority = next_cost + heuristic((nr, nc), end)

                if (nr, nc) not in visited or visited[(nr, nc)] >= next_cost:
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

    return all_best_paths


def find_best_seat(file_path: str):
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        grid = [list(line) for line in puzzle_input.read().splitlines()]
        start_, end_ = _get_start_end(grid)
        # best_path = _a_star(grid=grid, start=start_, end=end_)
        best_paths = _a_star_all_paths(grid=grid, start=start_, end=end_)
        all_tiles_on_best_paths = set()
        for path in best_paths:
            all_tiles_on_best_paths |= set(path)
        return len(all_tiles_on_best_paths)


timer_start = time.perf_counter()
print(
    find_best_seat(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_16"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    find_best_seat(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_16"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
