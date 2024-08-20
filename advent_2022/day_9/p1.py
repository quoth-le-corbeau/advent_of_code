import pathlib
import time
import math


class Head:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def move_and_store_last_position(self, direction: str) -> tuple[int, int]:
        last_position = self.x, self.y
        if direction == "U":
            self.y += 1
        elif direction == "D":
            self.y -= 1
        elif direction == "R":
            self.x += 1
        elif direction == "L":
            self.x -= 1
        return last_position


class Tail(Head):
    def has_to_move(self, head: Head) -> bool:
        hypotenuse = self.get_hypotenuse(head)
        return hypotenuse > math.sqrt(2)

    def get_hypotenuse(self, head: Head) -> float:
        horizontal_distance = abs(self.x - head.x)
        vertical_distance = abs(self.y - head.y)
        return math.sqrt(horizontal_distance**2 + vertical_distance**2)


def count_tail_positions(file_path: str) -> int:
    instructions = _get_instructions(file=file_path)
    head = Head()
    tail = Tail()
    positions: set[tuple[int, int]] = {(tail.x, tail.y)}
    for instruction in instructions:
        spaces = 0
        direction = instruction[0]
        while spaces < instruction[1]:
            last_head_position = head.move_and_store_last_position(direction=direction)
            if tail.has_to_move(head):
                tail.x, tail.y = last_head_position
                positions.add((tail.x, tail.y))
            spaces += 1
    return len(positions)


def _get_instructions(file: str) -> list[tuple[str, int]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        instructions = list()
        for line in lines:
            direction, spaces = line.split()
            instructions.append((direction, int(spaces)))
        return instructions


start = time.perf_counter()
print(count_tail_positions("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(count_tail_positions("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
