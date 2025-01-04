from pathlib import Path

# from math import ceil, log10

from reusables import timer, INPUT_PATH


class PlutonianPebbles:
    def __init__(self, file_path: str):
        with open(
            file=Path(__file__).resolve().parents[2] / file_path, mode="r"
        ) as puzzle_input:
            self.stones = list(map(int, puzzle_input.read().strip().split(" ")))

    def count_the_blinking_stones(self, stone: int, blinks: int, memo=None) -> int:
        if memo is None:
            memo = {}
        if blinks == 0:
            return 1
        if (stone, blinks) in memo:
            return memo[(stone, blinks)]
        # power_of_ten = ceil(log10(stone)) if stone > 0 else None
        if stone == 0:
            result = self.count_the_blinking_stones(
                stone=1, blinks=blinks - 1, memo=memo
            )
        # elif power_of_ten and power_of_ten > 0 and power_of_ten % 2 == 0:
        elif len(str(stone)) % 2 == 0:
            result = self.count_the_blinking_stones(
                stone=int(str(stone)[: len(str(stone)) // 2]),
                blinks=blinks - 1,
                memo=memo,
            ) + self.count_the_blinking_stones(
                stone=int(str(stone)[len(str(stone)) // 2 :]),
                blinks=blinks - 1,
                memo=memo,
            )
        else:
            result = self.count_the_blinking_stones(
                stone=(stone * 2024), blinks=blinks - 1, memo=memo
            )
        memo[(stone, blinks)] = result
        return result


@timer
def part_one(file: str):
    input_file_path = INPUT_PATH.format(file=file, year=2024, day=11)
    plutonian_pebbles = PlutonianPebbles(file_path=input_file_path)
    print(
        sum(
            plutonian_pebbles.count_the_blinking_stones(stone=stone, blinks=25)
            for stone in plutonian_pebbles.stones
        )
    )


# part_one("eg")
part_one("input")


@timer
def part_two(file: str):
    input_file_path = INPUT_PATH.format(file=file, year=2024, day=11)
    plutonian_pebbles = PlutonianPebbles(file_path=input_file_path)
    print(
        sum(
            plutonian_pebbles.count_the_blinking_stones(stone=stone, blinks=75)
            for stone in plutonian_pebbles.stones
        )
    )


# part_two("eg")
part_two("input")
