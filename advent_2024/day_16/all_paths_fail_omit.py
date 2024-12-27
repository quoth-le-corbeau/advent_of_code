import heapq
from typing import List, Tuple


def a_star_all_best_paths_with_turn_penalty(
    grid: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]
) -> List[List[Tuple[int, int]]]:
    row_count = len(grid)
    col_count = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (up, down, left, right)
    direction_labels = ["up", "down", "left", "right"]

    # Heuristic: Manhattan distance
    def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Priority queue: (priority, cost, current_position, current_direction, path, turns)
    pq = []
    heapq.heappush(pq, (0, 0, start, None, [start], 0))  # Initial direction is None
    visited = {}
    all_best_paths = []
    min_cost = float("inf")

    while pq:
        priority, cost, current, current_direction, path, turns = heapq.heappop(pq)

        # If we reach the end, process the result
        if current == end:
            total_cost = 1000 * turns + len(path) - 1  # Calculate total cost
            if total_cost < min_cost:
                min_cost = total_cost
                all_best_paths = [path]
            elif total_cost == min_cost:
                all_best_paths.append(path)
            continue

        # Skip if this state is not promising
        if current in visited and visited[current] <= (cost, turns):
            continue
        visited[current] = (cost, turns)

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
                next_turns = turns + turn_penalty
                next_cost = cost + 1  # Each step costs 1
                next_priority = next_cost + heuristic((nr, nc), end)

                # Allow revisiting nodes if the new state is as good as or better
                if (nr, nc) not in visited or visited[(nr, nc)] >= (
                    next_cost,
                    next_turns,
                ):
                    heapq.heappush(
                        pq,
                        (
                            next_priority,
                            next_cost,
                            (nr, nc),
                            next_direction,
                            path + [(nr, nc)],
                            next_turns,
                        ),
                    )

    return all_best_paths


# Example grid and usage
grid = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", "E", "#"],
    ["#", ".", "#", ".", "#", "#", "#", ".", "#", ".", "#", "#", "#", ".", "#"],
    ["#", ".", ".", ".", ".", ".", "#", ".", "#", ".", ".", ".", "#", ".", "#"],
    ["#", ".", "#", "#", "#", ".", "#", "#", "#", "#", "#", ".", "#", ".", "#"],
    ["#", ".", "#", ".", "#", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
    ["#", ".", "#", ".", "#", "#", "#", "#", "#", ".", "#", "#", "#", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
    ["#", "#", "#", ".", "#", ".", "#", "#", "#", "#", "#", ".", "#", ".", "#"],
    ["#", ".", ".", ".", "#", ".", ".", ".", ".", ".", "#", ".", "#", ".", "#"],
    ["#", ".", "#", ".", "#", ".", "#", "#", "#", ".", "#", ".", "#", ".", "#"],
    ["#", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#", ".", "#", ".", "#"],
    ["#", ".", "#", "#", "#", ".", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
    ["#", "S", ".", ".", "#", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
]

start = (13, 1)  # 'S' coordinates
end = (1, 13)  # 'E' coordinates
paths = a_star_all_best_paths_with_turn_penalty(grid, start, end)

print(
    f"Found {len(paths)} optimal paths with total cost of {1000 * (len(paths[0]) - 1 - 7036 // 1000) + 7036 // 1000}:"
)
for path in paths:
    print(path)
