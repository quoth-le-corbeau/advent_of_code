import time
import pathlib


class Rectangle:
    def __init__(
        self, rectangle_id: int, origin_x: int, origin_y: int, width: int, height: int
    ):
        self.rectangle_id = rectangle_id
        self.x0 = origin_x
        self.y0 = origin_y
        self.x1 = origin_x + width - 1
        self.y1 = origin_y + height - 1

    def no_overlap(self, other) -> bool:
        return (
            self.x1 < other.x0
            or self.x0 > other.x1
            or self.y1 < other.y0
            or self.y0 > other.y1
        )


def find_non_overlapping(file_path: str):
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        rectangles = []
        for line in puzzle_input.read().splitlines():
            parsed = line.replace(" ", "").split("@")
            id = int(parsed[0][1:])
            rectangle_descriptors = list(
                map(int, parsed[1].replace(":", ",").replace("x", ",").split(","))
            )
            rectangles.append(
                Rectangle(
                    rectangle_id=id,
                    origin_x=rectangle_descriptors[0],
                    origin_y=rectangle_descriptors[1],
                    width=rectangle_descriptors[2],
                    height=rectangle_descriptors[3],
                )
            )
        for i, rectangle in enumerate(rectangles):
            if all(
                [
                    rectangle.no_overlap(other_rectangle)
                    for other_rectangle in rectangles[0:i] + rectangles[i + 1 :]
                ]
            ):
                return rectangle.rectangle_id
            else:
                continue
        else:
            raise RuntimeError(f"No non-overlapping rectangles in {file_path}")


start = time.perf_counter()
print(
    find_non_overlapping(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2018/day_3"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    find_non_overlapping(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2018/day_3"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
