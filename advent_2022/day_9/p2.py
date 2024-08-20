import pathlib
import time
import math


class Head:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def move(self, direction: str) -> None:
        if direction == "U":
            self.y += 1
        elif direction == "D":
            self.y -= 1
        elif direction == "R":
            self.x += 1
        elif direction == "L":
            self.x -= 1


class Tail(Head):
    def has_to_move(self, head: Head) -> bool:
        hypotenuse = self.get_hypotenuse(head)
        return hypotenuse > math.sqrt(2)

    def get_hypotenuse(self, head: Head) -> float:
        horizontal_distance = abs(self.x - head.x)
        vertical_distance = abs(self.y - head.y)
        a_sq_plus_b_sq = horizontal_distance**2 + vertical_distance**2
        return math.sqrt(a_sq_plus_b_sq)

    def follow_head(self, head: Head) -> None:
        moves_by_direction = self.get_possible_moves_by_direction(head)
        for key, value in moves_by_direction.items():
            if value is True:
                self.move(direction=key)

    def get_possible_moves_by_direction(
        self, head: Head
    ) -> dict[tuple[int, int], bool]:
        moves_by_direction = dict()
        # N E S W
        moves_by_direction[(0, 1)] = self.x == head.x and self.y - head.y == -2
        moves_by_direction[(1, 0)] = self.y == head.y and self.x - head.x == -2
        moves_by_direction[(0, -1)] = self.x == head.x and self.y - head.y == 2
        moves_by_direction[(-1, 0)] = self.y == head.y and self.x - head.x == 2
        # NE NW SE SW
        moves_by_direction[(1, 1)] = (
            (self.x - head.x == -1 and self.y - head.y == -2)
            or (self.x - head.x == -2 and self.y - head.y == -1)
            or (self.x - head.x == -2 and self.y - head.y == -2)
        )
        moves_by_direction[(-1, 1)] = (
            (self.x - head.x == 1 and self.y - head.y == -2)
            or (self.x - head.x == 2 and self.y - head.y == -1)
            or (self.x - head.x == 2 and self.y - head.y == -2)
        )
        moves_by_direction[(1, -1)] = (
            (self.x - head.x == -1 and self.y - head.y == 2)
            or (self.x - head.x == -2 and self.y - head.y == 1)
            or (self.x - head.x == -2 and self.y - head.y == 2)
        )
        moves_by_direction[(-1, -1)] = (
            (self.x - head.x == 1 and self.y - head.y == 2)
            or (self.x - head.x == 2 and self.y - head.y == 1)
            or (self.x - head.x == 2 and self.y - head.y == 2)
        )
        return moves_by_direction

    def move(self, direction: tuple[int, int]) -> None:
        self.x += direction[0]
        self.y += direction[1]


def count_tail_positions(file: str) -> int:
    instructions = _get_instructions(file=file)
    head = Head()
    tail_1 = Tail()
    tail_2 = Tail()
    tail_3 = Tail()
    tail_4 = Tail()
    tail_5 = Tail()
    tail_6 = Tail()
    tail_7 = Tail()
    tail_8 = Tail()
    tail_9 = Tail()
    positions: set[tuple[int, int]] = {(0, 0)}
    for instruction in instructions:
        spaces = 0
        direction = instruction[0]
        while spaces < instruction[1]:
            head.move(direction=direction)
            if tail_1.has_to_move(head=head):
                tail_1.follow_head(head=head)
            if tail_2.has_to_move(head=tail_1):
                tail_2.follow_head(head=tail_1)
            if tail_3.has_to_move(head=tail_2):
                tail_3.follow_head(head=tail_2)
            if tail_4.has_to_move(head=tail_3):
                tail_4.follow_head(head=tail_3)
            if tail_5.has_to_move(head=tail_4):
                tail_5.follow_head(head=tail_4)
            if tail_6.has_to_move(head=tail_5):
                tail_6.follow_head(head=tail_5)
            if tail_7.has_to_move(head=tail_6):
                tail_7.follow_head(head=tail_6)
            if tail_8.has_to_move(head=tail_7):
                tail_8.follow_head(head=tail_7)
            if tail_9.has_to_move(head=tail_8):
                tail_9.follow_head(head=tail_8)
                positions.add((tail_9.x, tail_9.y))
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
print(count_tail_positions("eg1.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(count_tail_positions("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
