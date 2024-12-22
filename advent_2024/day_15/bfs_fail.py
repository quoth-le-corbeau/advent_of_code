def _bfs(grid: list[list[str]], start: tuple[int, int]) -> list[tuple[int, int]]:
    queue = deque([start])
    visited = {start}
    box_coordinates = [start]
    types = ["[", "]"]

    while queue:
        current = queue.popleft()
        for direction in _DIRECTION_VECTORS.values():
            next_node = current[0] + direction[0], current[1] + direction[1]
            if next_node not in visited and grid[next_node[0]][next_node[1]] in types:
                queue.append(next_node)
                visited.add(next_node)
                box_coordinates.append(next_node)

    return box_coordinates
