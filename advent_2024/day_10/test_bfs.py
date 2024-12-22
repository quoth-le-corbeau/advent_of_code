from collections import deque
from typing import Optional

test_grid = [
    [8, 9, 0, 1, 0, 1, 2, 3],
    [7, 8, 1, 2, 1, 8, 7, 4],
    [8, 7, 4, 3, 0, 9, 6, 5],
    [9, 6, 5, 4, 9, 8, 7, 4],
    [4, 5, 6, 7, 8, 9, 0, 3],
    [3, 2, 0, 1, 9, 0, 1, 2],
    [0, 1, 3, 2, 9, 8, 0, 1],
    [1, 0, 4, 5, 6, 7, 3, 2],
]

first_zero = (0, 2)
first_nine = (0, 1)


def bfs(
    start: tuple[int, int], end: tuple[int, int], grid: list[list[int]]
) -> Optional[list[tuple[int, int]]]:

    return None


def test_bfs():
    assert bfs(first_zero, first_nine, test_grid) == [
        (0, 2),
        (1, 2),
        (1, 3),
        (2, 3),
        (3, 3),
        (3, 2),
        (3, 1),
        (2, 1),
        (1, 1),
        (0, 1),
    ]
