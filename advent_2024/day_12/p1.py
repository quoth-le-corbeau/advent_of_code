import time
import pathlib

"""
Garden Groups Part I



"""


def get_garden_group_price(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip()
        plant_types = set(lines)
        garden_groups = {type: 0 for type in plant_types if type != "\n"}

        print(f"{garden_groups=}")
        grid = [line for line in lines.split("\n")]
        print(f"{grid=}")


start = time.perf_counter()
print(
    get_garden_group_price(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_12"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

# start = time.perf_counter()
# print(get_garden_group_price(str((pathlib.Path(__file__).resolve().parents[2] / "my_inputs/2024/day_12" / "input.txt"))))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
