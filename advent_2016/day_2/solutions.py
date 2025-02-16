from pathlib import Path

from reusables import timer, INPUT_PATH


class BathroomButtons:
    def __init__(self, file_path: Path):
        with open(file=file_path, mode="r") as instructions_lines:
            self.instructions = instructions_lines.read().splitlines()
            self.directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
            self.keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            self.keypad_2 = [
                [None, None, 1, None, None],
                [None, 2, 3, 4, None],
                [5, 6, 7, 8, 9],
                [None, "A", "B", "C", None],
                [None, None, "D", None, None],
            ]
            self.position = (1, 1)
            self.position_2 = (2, 0)

    def find_code(self) -> str:
        code = []
        for instruction in self.instructions:
            for move in instruction:
                dr, dc = self.directions[move]
                nr, nc = self.position[0] + dr, self.position[1] + dc
                if 0 <= nr < len(self.keypad) and 0 <= nc < len(self.keypad[0]):
                    self.position = nr, nc
                else:
                    continue
            code.append(self.keypad[self.position[0]][self.position[1]])
        return "".join([str(c) for c in code])

    def find_code_2(self) -> str:
        code = []
        for instruction in self.instructions:
            for move in instruction:
                dr, dc = self.directions[move]
                nr, nc = self.position_2[0] + dr, self.position_2[1] + dc
                if (
                    0 <= nr < len(self.keypad_2)
                    and 0 <= nc < len(self.keypad_2[0])
                    and self.keypad_2[nr][nc] is not None
                ):
                    self.position_2 = nr, nc
                else:
                    continue
            code.append(self.keypad_2[self.position_2[0]][self.position_2[1]])
        return "".join([str(c) for c in code])


@timer
def part_one(file: str, day: int = 2, year: int = 2016) -> str:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    bathroom_button = BathroomButtons(file_path=input_file_path)
    return bathroom_button.find_code()


# part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 2, year: int = 2016):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    bathroom_button = BathroomButtons(file_path=input_file_path)
    return bathroom_button.find_code_2()


# part_two(file="eg")
part_two(file="input")
