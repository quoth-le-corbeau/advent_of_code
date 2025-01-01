from pathlib import Path
import heapq


from reusables import timer, INPUT_PATH

"""
Reindeer Maze Part II

parse input into mutable grid
use modified a_star with turn-minimizing heuristic to find best paths and scores
(thus improving on part I but finding more paths)
discard the scores and instead find the union of all points in all best paths
return the length of the union

"""

_ROTATION_COST = 1000
_STEP_COST = 1


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


def _print_path(path: list[tuple[int, int]], grid: list[list[str]], file: str) -> None:
    count = 0
    for point in path:
        r, c = point
        grid[r][c] = "O"
        count += 1
    print(f"Path with {count} steps for {file} --------------------")
    for line in grid:
        print("".join(line))


def _get_possible_rotations(
    vector: tuple[int, int]
) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    return the two direction vectors of the possible 90° turns
    N,S <-> E,W
    """
    r, c = vector
    return ((r + 1) % 2, (c + 1) % 2), (-((r - 1) % 2), -((c - 1) % 2))


def _look_in_possible_directions(
    position: tuple[int, int], direction: tuple[int, int], grid: list[list[str]]
) -> list[tuple[int, tuple[int, int], tuple[int, int]]]:
    weighted_grid_points = []
    dr, dc = direction
    nr, nc = position[0] + dr, position[1] + dc
    symbol = grid[nr][nc]
    if symbol != "#":
        assert symbol in ["S", "E", "."]
        weighted_grid_points.append((_STEP_COST, (nr, nc), direction))
    for possible_rotation in _get_possible_rotations(vector=direction):
        dr, dc = possible_rotation
        nr, nc = position[0] + dr, position[1] + dc
        symbol = grid[nr][nc]
        if symbol != "#":
            assert symbol in ["S", "E", "."]
            weighted_grid_points.append(
                (_ROTATION_COST + _STEP_COST, (nr, nc), (dr, dc))
            )
    return weighted_grid_points


def _find_paths(
    grid: list[list[str]],
    start: tuple[int, int],
    end: tuple[int, int],
    start_direction: tuple[int, int],
) -> tuple[int, list[list[tuple[int, int]]]]:
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, start_direction, [start]))
    best_score = float("inf")
    paths = []
    visited = {}
    while len(priority_queue) > 0:
        cost, current, direction, path = heapq.heappop(priority_queue)
        visited[current] = cost
        if current == end:
            if cost <= best_score:
                best_score = cost
                paths.append(path)
            else:
                return best_score, paths
        for move_cost, next_position, next_direction in _look_in_possible_directions(
            position=current, direction=direction, grid=grid
        ):
            if (
                cost + move_cost
                <= visited.get(next_position, float("inf")) + _ROTATION_COST
            ):
                heapq.heappush(
                    priority_queue,
                    (
                        cost + move_cost,
                        next_position,
                        next_direction,
                        path + [next_position],
                    ),
                )

    return best_score, paths


def find_best_possible_seat_count(file_path: Path):
    with open(Path(__file__).resolve().parents[2] / file_path, "r") as puzzle_input:
        grid = [list(line) for line in puzzle_input.read().splitlines()]
        start_, end_ = _get_start_end(grid)
        cost, paths = _find_paths(
            grid=grid, start=start_, end=end_, start_direction=(0, 1)
        )
        print(f"score: {cost}")
        seats = set()
        for path in paths:
            seats = seats.union(path)
        return len(seats)


@timer
def part_two(file: str, year: int = 2024, day: int = 16) -> None:
    input_file_path = INPUT_PATH.format(year=year, day=day, file=file)
    print(find_best_possible_seat_count(file_path=input_file_path))
    print(f"solution ran with file: {file}.txt")


part_two(file="eg")
# part_two(file="eg2")
part_two(file="input")
