from pathlib import Path

from reusables import timer, INPUT_PATH

_PIXELS_WIDE = 25
_PIXELS_HIGH = 6
_LAYER_SIZE = _PIXELS_WIDE * _PIXELS_HIGH
_TEST_PIXELS_HIGH = 2
_TEST_PIXELS_WIDE = 2


def _parse(file_path: Path):
    with open(file_path, "r") as puzzle_input:
        return puzzle_input.read().strip()


def _get_unordered_layers(pixels: str, layer_size: int) -> list[str]:
    i = 0
    layers = []
    while i <= len(pixels) - layer_size:
        layers.append(pixels[i : i + layer_size])
        i += layer_size
    return layers


def _get_ordered_layers(
    pixels: str, rows: int, columns: int
) -> dict[tuple[int, int], list[str]]:
    layer_size = rows * columns
    i = 0
    grid_look_up = {(r, c): [] for r in range(rows) for c in range(columns)}
    while i <= len(pixels) - layer_size:
        layer = iter(pixels[i : i + layer_size])
        for y in range(rows):
            for x in range(columns):
                grid_look_up[(y, x)].append(next(layer))
        i += layer_size
    return grid_look_up


def _print_image(
    grid_look_up: dict[tuple[int, int], list[str]], columns: int, rows: int
) -> None:
    filtered_pixels_by_grid_position = dict()
    for grid_position, pixels in grid_look_up.items():
        for pixel in pixels:
            if pixel != "2":
                filtered_pixels_by_grid_position[grid_position] = pixel
                break
    grid = [["." for c in range(columns)] for r in range(rows)]
    for r in range(rows):
        for c in range(columns):
            grid[r][c] = filtered_pixels_by_grid_position[(r, c)]
    _print_grid(grid)


def _print_grid(grid: list[list[str]]) -> None:
    for row in grid:
        print(" ".join(row))


@timer
def part_one(file: str, day: int = 8, year: int = 2019, layer_size: int = _LAYER_SIZE):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    layers = _get_unordered_layers(
        pixels=_parse(file_path=input_file_path), layer_size=layer_size
    )
    least_zeros_layer = min(layers, key=lambda x: x.count("0"))
    return least_zeros_layer.count("1") * least_zeros_layer.count("2")


part_one(file="input")


@timer
def part_two(
    file: str,
    day: int = 8,
    year: int = 2019,
    pixels_high: int = _PIXELS_HIGH,
    pixels_wide: int = _PIXELS_WIDE,
) -> None:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    look_up = _get_ordered_layers(
        pixels=_parse(file_path=input_file_path), rows=pixels_high, columns=pixels_wide
    )
    _print_image(look_up, rows=pixels_high, columns=pixels_wide)


part_two(file="eg", pixels_high=_TEST_PIXELS_HIGH, pixels_wide=_TEST_PIXELS_WIDE)
part_two(file="input")
