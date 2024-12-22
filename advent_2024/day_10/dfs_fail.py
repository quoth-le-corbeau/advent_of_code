from collections import defaultdict


def find_paths_dfs(grid):
    rows = len(grid)
    cols = len(grid[0])

    grid = [[int(x) for x in row] for row in grid]

    zeros = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]
    nines = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 9]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(current, end, visited, path, all_paths):
        if current == end:
            all_paths.append(path[:])
            return

        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] - grid[current[0]][current[1]] == 1:
                    next_pos = (nr, nc)
                    if next_pos not in visited:
                        visited.add(next_pos)
                        path.append(next_pos)
                        dfs(next_pos, end, visited, path, all_paths)
                        path.pop()
                        visited.remove(next_pos)

    all_paths_result = defaultdict(list)
    for zero in zeros:
        for nine in nines:
            visited = set([zero])
            path = [zero]
            all_paths = []
            dfs(zero, nine, visited, path, all_paths)
            if all_paths:
                all_paths_result[zero].append((nine, all_paths))
    print(f"{all_paths_result=}")
    return all_paths_result


GRID = [
    "89010123",
    "78121874",
    "87430965",
    "96549874",
    "45678903",
    "32019012",
    "01329801",
    "10456732",
]
GRID = []

paths = find_paths_dfs(GRID)
# for start, endpoints in paths.items():
#     print(f"From {start}:")
#     for end, all_paths in endpoints:
#         print(f"  To {end}: Paths = {all_paths}")
# trail_ratings =
# for key, value in paths.items():
print(f"{paths[(0, 2)]=}")
total = 0
for trailhead, paths in paths.items():
    for path in paths:
        total += len(path[1])
print(total)
