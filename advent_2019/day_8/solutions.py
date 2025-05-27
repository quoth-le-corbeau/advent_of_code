from pathlib import Path

from reusables import timer, INPUT_PATH

_PIXELS_WIDE = 25
_PIXELS_HIGH = 6
_LAYER_SIZE = _PIXELS_WIDE * _PIXELS_HIGH


def _parse(file_path: Path):
    with open(file_path, "r") as puzzle_input:
        return puzzle_input.read().strip()


@timer
def part_one(file: str, day: int = 8, year: int = 2019, layer_size: int = _LAYER_SIZE):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )

    layers = _get_layers(
        pixels=_parse(file_path=input_file_path), layer_size=layer_size
    )
    least_zeros_layer = min(layers, key=lambda x: x.count("0"))
    return least_zeros_layer.count("1") * least_zeros_layer.count("2")


def _get_layers(pixels: str, layer_size: int) -> list[str]:
    i = 0
    layers = []
    while i <= len(pixels) - layer_size:
        layers.append(pixels[i : i + layer_size])
        i += layer_size
    return layers


part_one(file="eg", layer_size=6)
part_one(file="input")


@timer
def part_two(file: str, day: int = 8, year: int = 2019):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )


# part_two(file="eg")
# part_two(file="input")
