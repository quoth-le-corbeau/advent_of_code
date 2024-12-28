from pathlib import Path
import heapq

from reusables import timer, INPUT_PATH

"""
Reindeer Maze Part I

parse input into mutable grid
use a_star with turn-minimizing heuristic to find best path
calculate the score of the best path 

Note: it would be nicer to get the score within the search algo!

"""


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


def _a_star_minimize_turns(
    grid: list[list[str]], start: tuple[int, int], end: tuple[int, int]
) -> list[tuple[int, int]]:
    row_count = len(grid)
    col_count = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (up, down, left, right)
    direction_labels = ["up", "down", "left", "right"]

    def heuristic(a: tuple[int, int], b: tuple[int, int]) -> int:
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
    return []


def find_best_reindeer_path(file_path: Path):
    with open(Path(__file__).resolve().parents[2] / file_path, "r") as puzzle_input:
        grid = [list(line) for line in puzzle_input.read().splitlines()]
        start_, end_ = _get_start_end(grid)
        best_path = _a_star_minimize_turns(grid=grid, start=start_, end=end_)
        return _get_path_score(best_path)


@timer
def part_one(file: str, year: int = 2024, day: int = 16) -> None:
    input_file_path = INPUT_PATH.format(year=year, day=day, file=file)
    print(find_best_reindeer_path(file_path=input_file_path))
    print(f"solution ran with file: {file}.txt")


part_one(file="eg")
part_one(file="eg2")
part_one(file="input")
