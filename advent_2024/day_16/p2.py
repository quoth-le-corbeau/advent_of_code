from pathlib import Path
from collections import deque
import heapq
from reusables import timer, INPUT_PATH


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


def _print_path(path: list[tuple[int, int]], grid: list[list[str]], file: str) -> None:
    count = 0
    for point in path:
        r, c = point
        grid[r][c] = "O"
        count += 1
    print(f"Path with {count} steps for {file} --------------------")
    for line in grid:
        print("".join(line))


def _find_paths_bfs(grid, start, end):
    q = deque([[start]])
    paths = []

    while q:
        path = q.popleft()
        current = path[-1]

        # If the end point is reached, save the path
        if current == end:
            paths.append(path)
            continue

        # Explore neighbors in all four directions
        for vector in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            dr, dc = vector
            next_point = current[0] + dr, current[1] + dc
            nr, nc = next_point

            if (
                0 <= nr < len(grid)
                and 0 <= nc < len(grid[0])
                and next_point not in path  # Avoid revisiting nodes in the current path
                and (grid[nr][nc] == "." or grid[nr][nc] == "E")
            ):
                q.append(path + [next_point])

    return paths


def _find_paths(grid, start, end):
    row_count = len(grid)
    col_count = len(grid[0])

    def heuristic(path):
        # Score based on current path cost and estimated distance to the end
        return (
            _get_path_score(path)
            + abs(path[-1][0] - end[0])
            + abs(path[-1][1] - end[1])
        )

    pq = []
    heapq.heappush(pq, (0, [start]))  # Priority queue of (priority, path)
    best_score = float("inf")
    paths = []

    while pq:
        current_score, path = heapq.heappop(pq)
        current = path[-1]

        # If the end is reached, evaluate the path
        if current == end:
            final_score = _get_path_score(path)
            if final_score < best_score:
                best_score = final_score
                paths = [path]
            elif final_score == best_score:
                paths.append(path)
            continue

        # Prune paths with a cost exceeding the best score
        if current_score > best_score:
            continue

        # Explore neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = current[0] + dr, current[1] + dc
            if (
                0 <= nr < row_count
                and 0 <= nc < col_count
                and (grid[nr][nc] == "." or (nr, nc) == end)
                and (nr, nc) not in path  # Prevent cycles
            ):
                new_path = path + [(nr, nc)]
                heapq.heappush(pq, (heuristic(new_path), new_path))

    return paths


def find_best_reindeer_path(file_path: Path):
    with open(Path(__file__).resolve().parents[2] / file_path, "r") as puzzle_input:
        grid = [list(line) for line in puzzle_input.read().splitlines()]
        start_, end_ = _get_start_end(grid)
        paths = _find_paths(grid=grid, start=start_, end=end_)
        scores_by_path = {i: _get_path_score(path) for i, path in enumerate(paths)}
        min_score = min(scores_by_path.values())
        best_paths = [
            path for path in scores_by_path if scores_by_path[path] == min_score
        ]
        print(f"{len(paths)} paths found")
        seats = set()
        for i in best_paths:
            path = paths[i]
            _print_path(path=path, grid=grid, file=str(file_path))
            for point in path:
                seats.add(point)
        return len(seats)


@timer
def part_two(file: str, year: int = 2024, day: int = 16) -> None:
    input_file_path = INPUT_PATH.format(year=year, day=day, file=file)
    print(find_best_reindeer_path(file_path=input_file_path))
    print(f"solution ran with file: {file}.txt")


part_two(file="eg")
part_two(file="eg2")
part_two(file="input")
