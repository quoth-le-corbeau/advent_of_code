import heapq


def _find_paths(
    grid: list[list[str]], start: tuple[int, int], end: tuple[int, int]
) -> list[list[tuple[int, int]]]:
    row_count = len(grid)
    col_count = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (up, down, left, right)
    direction_labels = ["up", "down", "left", "right"]

    def heuristic(a: tuple[int, int], b: tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    pq = []
    heapq.heappush(pq, (0, 0, start, None, [start]))
    visited = {}
    paths = []

    while pq:
        priority, cost, current, current_direction, path = heapq.heappop(pq)

        if current == end:
            paths.append(path)
            continue

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

    return paths


def _find_paths_only_one_with_score(
    grid: list[list[str]], start: tuple[int, int], end: tuple[int, int]
) -> list[list[tuple[int, int]]]:
    row_count = len(grid)
    col_count = len(grid[0])

    def heuristic(a: tuple[int, int], b: tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    pq = []
    heapq.heappush(
        pq, (0, start, [start])
    )  # Priority queue with (cost, current node, path)

    visited = {}  # Tracks the best score to a node
    paths = []
    min_score = float("inf")

    while pq:
        cost, current, path = heapq.heappop(pq)

        # If this path has already been processed with a lower cost, skip it
        if current in visited and visited[current] <= cost:
            continue
        visited[current] = cost

        # Calculate the score of the current path
        current_score = _get_path_score(path)

        # If current path reaches the end
        if current == end:
            if current_score <= min_score:
                min_score = current_score
                paths = [path]  # Start a new collection of best paths
            elif current_score == min_score:
                paths.append(path)
            continue

        # Explore neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = current[0] + dr, current[1] + dc

            if (
                0 <= nr < row_count
                and 0 <= nc < col_count
                and (grid[nr][nc] == "." or (nr, nc) == end)
            ):
                neighbor = (nr, nc)
                new_path = path + [neighbor]
                new_score = _get_path_score(new_path)
                priority = new_score + heuristic(neighbor, end)
                heapq.heappush(pq, (priority, neighbor, new_path))

    return paths
