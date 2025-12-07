from collections import deque, defaultdict
from pathlib import Path

from reusables import timer, INPUT_PATH


GridPoint = type(tuple[int, int])


def _parse_grid(file_path: Path):
    splitters: set[GridPoint] = set()
    s = ""
    with open(file_path, "r") as puzzle_input:
        for j, line in enumerate(puzzle_input.read().strip().splitlines()):
            for i, char in enumerate(line):
                if char == "^":
                    splitters.add((i, j))
                elif char == "S":
                    s = (i, j)
                else:
                    assert char == "."
                    continue
    # print(f"{sorted(list(splitters))=}")
    # print(f"There are {len(splitters)} splitters in total.")
    # print(f"The grid has {i+1} cols and {j+1} rows")
    # print(f"Tachyon beam starts at {s}")
    return s, splitters, i + 1, j + 1


def _dfs(
    current_position: GridPoint,
    cols: int,
    rows: int,
    splitters: set[GridPoint],
    marked_splitters: set[GridPoint] | None = None,
) -> set[GridPoint]:
    if marked_splitters is None:
        marked_splitters = set()
    x, y = current_position
    if y < 0 or y >= rows or x < 0 or x >= cols:
        assert y == rows
        return marked_splitters

    if current_position in splitters:
        if current_position not in marked_splitters:
            marked_splitters.add(current_position)
            _dfs(
                current_position=(x - 1, y),
                cols=cols,
                rows=rows,
                splitters=splitters,
                marked_splitters=marked_splitters,
            )
            _dfs(
                current_position=(x + 1, y),
                cols=cols,
                rows=rows,
                splitters=splitters,
                marked_splitters=marked_splitters,
            )
        return marked_splitters

    return _dfs(
        current_position=(x, y + 1),
        cols=cols,
        rows=rows,
        splitters=splitters,
        marked_splitters=marked_splitters,
    )


def _pprint(rows, cols, splitters, marked_splitters):
    grid = [["." for _ in range(cols)] for _ in range(rows)]
    for j in range(rows):
        for i in range(cols):
            if (i, j) in marked_splitters:
                grid[j][i] = "^"
                grid[j][i - 1] = "|"
                grid[j][i + 1] = "|"
            elif (i, j) in splitters and (i, j) not in marked_splitters:
                print(f"UNMARKED_SPLITTER: {(i,j)}")
                grid[j][i] = "^"
            elif grid[j - 1][i] == "|":
                grid[j][i] = "|"
            else:
                continue

    for r in grid:
        print("".join(r))


@timer
def part_one(file: str, day: int = 7, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    start, nodes, cols, rows = _parse_grid(file_path=input_file_path)
    hit_splitters = _dfs(current_position=start, cols=cols, rows=rows, splitters=nodes)
    # _pprint(rows, cols, nodes, hit_splitters)
    return len(hit_splitters)


# part_one(file="eg")
# part_one(file="input")


def _bfs(
    current_position: GridPoint,
    cols: int,
    rows: int,
    splitters: set[GridPoint],
) -> int:
    x, y = current_position
    q = deque([(x, y, 1)])
    total_paths = 0
    cache = defaultdict(int)
    cache[(x, y)] = 1
    while len(q) != 0:
        node = q.popleft()

        x, y, n = node
        if y >= rows - 1:
            total_paths += n
            continue

        if 0 <= x < cols and 0 <= y < rows:
            if (x, y) in splitters:
                q.append((x - 1, y, n))
                q.append((x + 1, y, n))
            else:
                q.append((x, y + 1, n))
    return total_paths


@timer
def part_two(file: str, day: int = 7, year: int = 2025):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    start, nodes, cols, rows = _parse_grid(file_path=input_file_path)
    unique_paths = _bfs(current_position=start, cols=cols, rows=rows, splitters=nodes)
    # print(f"{unique_paths=}")
    return unique_paths


part_two(file="eg")
part_two(file="input")
