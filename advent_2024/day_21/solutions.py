import heapq
from collections import deque, defaultdict
from pathlib import Path
from typing import Union

from reusables import INPUT_PATH, timer


BASE_PATH = Path(__file__).resolve().parents[2]
NUMERIC_KEYPAD = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    [None, 0, "A"],
]
NUMERIC_START = (3, 2)
DIRECTIONAL_KEYPAD = [
    [None, "^", "A"],
    ["<", "v", ">"],
]
DIRECTIONAL_START = (0, 2)
DIRECTION_MAP = {(-1, 0): "^", (0, -1): "<", (1, 0): "v", (0, 1): ">"}
_PART_ONE_LOOPS = 3


def _parse_input(path: Path):
    with path.open(mode="r", encoding="utf-8") as puzzle_input:
        return puzzle_input.read().strip().splitlines()


def _bfs(
    pair: tuple[tuple[int, int], tuple[int, int]], keypad: list[list[Union[int, str]]]
) -> list[tuple[int, int]]:
    start, end = pair
    queue = deque([[start]])
    visited = set()

    while len(queue) > 0:
        path = queue.popleft()
        current = path[-1]

        if current == end:
            return path

        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = current[0] + direction[0], current[1] + direction[1]
            if (
                (nr, nc) not in visited
                and (0 <= nr < len(keypad) and 0 <= nc < len(keypad[0]))
                and keypad[nr][nc] is not None
            ):
                queue.append(path + [(nr, nc)])
                visited.add((nr, nc))
    raise ValueError("No path found")


def _get_symbol_node(char: str, keypad: list[list[Union[int, str]]]) -> tuple[int, int]:
    for r, row in enumerate(keypad):
        for c, col in enumerate(row):
            if str(col) == char:
                return r, c
    raise ValueError(f"No {char} found")


def _get_corresponding_sequence(
    sequence: str, start_node: tuple[int, int], keypad: list[list[Union[int, str]]]
) -> str:
    def manhattan(node_1: tuple[int, int], node_2: tuple[int, int]) -> tuple[int, int]:
        return node_2[0] - node_1[0], node_2[1] - node_1[1]

    code_nodes = [start_node] + [
        _get_symbol_node(char=char, keypad=keypad) for char in sequence
    ]
    node_pairs = zip(code_nodes, code_nodes[1:])
    new_sequence = []
    for pair in node_pairs:
        path = _bfs(pair, keypad=keypad)
        path_pairs = zip(path, path[1:])
        for path_pair in path_pairs:
            node_1, node_2 = path_pair
            new_sequence.append(DIRECTION_MAP[manhattan(node_1, node_2)])
        new_sequence.append("A")

    optimised_sequence = _optimise_sequence(new_sequence)
    return "".join(optimised_sequence)


def _optimise_sequence(sequence: list[str]) -> list[str]:
    """analyze the sequence and make consecutive where possible"""
    result = []
    blocks = _chunk_sequence(sequence)
    for block in blocks:
        to_analyse = block[:-1]
        if "".join(to_analyse) == ">^>" or "".join(to_analyse) == "<v<":
            block[2], block[1] = block[1], block[2]
        result += block
    return result


def _chunk_sequence(sequence: list[str]) -> list[list[str]]:
    blocks = []
    i = 0
    block = []
    while i < len(sequence):
        char = sequence[i]
        if char != "A":
            block.append(char)
        else:
            block.append(char)
            blocks.append(block)
            block = []
        i += 1
    return blocks


def _get_numeric_part(code: str) -> int:
    res_str = ""
    for char in code:
        if char not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            continue
        else:
            res_str += char
    return int(res_str)


@timer
def part_one(filename: str) -> None:
    codes = _parse_input(
        path=BASE_PATH / INPUT_PATH.format(file=filename, year=2024, day=21)
    )
    final_sequences = defaultdict(str)
    for code in codes:
        next_sequence = None
        current_sequence = code
        i = 0
        while i < _PART_ONE_LOOPS:
            if i == 0:
                keypad = NUMERIC_KEYPAD
                start_node = NUMERIC_START
            else:
                keypad = DIRECTIONAL_KEYPAD
                start_node = DIRECTIONAL_START
            next_sequence = _get_corresponding_sequence(
                sequence=current_sequence, start_node=start_node, keypad=keypad
            )
            current_sequence = next_sequence
            i += 1
        final_sequences[code] = next_sequence
    print(final_sequences)
    total = 0
    for code, sequence in final_sequences.items():
        print(f"{_get_numeric_part(code)} * {len(sequence)}")
        total += len(sequence) * _get_numeric_part(code)
    print(f"part 1: {total}")


part_one(filename="eg")
part_one(filename="input")
