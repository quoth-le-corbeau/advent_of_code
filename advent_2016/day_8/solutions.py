from pathlib import Path

from reusables import timer, INPUT_PATH

SCREEN_SIZE = (50, 6)
EG_SCREEN_SIZE = (7, 3)


def _parse_instructions(file_path: Path) -> list[str]:
    with open(file_path, "r") as puzzle_input:
        return puzzle_input.read().strip().splitlines()


def _pprint_grid(
    pixel_map: dict[tuple[int, int], bool], screen_size: tuple[int, int]
) -> None:
    # grid = [["."] * screen_size[0]] * screen_size[1] # note this means each row is a copy!
    grid = [["."] * screen_size[0] for _ in range(screen_size[1])]
    for position, pixel in pixel_map.items():
        i, j = position
        if pixel:
            grid[j][i] = "#"
        pass
    for row in grid:
        print(" ".join(row))
    print("=========")


@timer
def part_one(
    file: str, screen_size: tuple[int, int], day: int = 8, year: int = 2016
) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    instructions = _parse_instructions(file_path=input_file_path)
    pixel_map: dict[tuple[int, int], bool] = {
        (i, j): False for j in range(screen_size[1]) for i in range(screen_size[0])
    }
    for instruction in instructions:
        if instruction[:4] == "rect":
            i, j = tuple(map(int, instruction.split(" ")[1].split("x")))
            for r in range(j):
                for c in range(i):
                    pixel_map[c, r] = True
            _pprint_grid(pixel_map=pixel_map, screen_size=screen_size)
        elif instruction.split(" ")[1] == "column":
            col = int(instruction.split(" ")[2].split("=")[1])
            by_ = int(instruction.split(" ")[-1])
            positions = [k for k, v in pixel_map.items() if k[0] == col and v]
            mapped_positions = [
                (p[0], ((p[1] + by_) % screen_size[1])) for p in positions
            ]
            for mapped_position in mapped_positions:
                pixel_map[mapped_position] = True
            for position in positions:
                if position not in mapped_positions:
                    pixel_map[position] = False
            _pprint_grid(pixel_map=pixel_map, screen_size=screen_size)

        elif instruction.split(" ")[1] == "row":
            row = int(instruction.split(" ")[2].split("=")[1])
            by_ = int(instruction.split(" ")[-1])
            positions = [k for k, v in pixel_map.items() if k[1] == row and v]
            mapped_positions = [
                (((p[0] + by_) % screen_size[0]), p[1]) for p in positions
            ]
            for mapped_position in mapped_positions:
                pixel_map[mapped_position] = True
            for position in positions:
                if position not in mapped_positions:
                    pixel_map[position] = False
            _pprint_grid(pixel_map=pixel_map, screen_size=screen_size)

        else:
            raise ValueError(f"Unknown instruction: {instruction}. Abort!")

    pixel_positions = [k for k, v in pixel_map.items() if v]
    return len(pixel_positions)


part_one(file="eg", screen_size=EG_SCREEN_SIZE)
part_one(file="input", screen_size=SCREEN_SIZE)


@timer
def part_two(file: str, day: int = 8, year: int = 2016):
    # RURCEOEIL
    pass
