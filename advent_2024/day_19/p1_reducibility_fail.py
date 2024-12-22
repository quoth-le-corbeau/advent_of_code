import time
import pathlib

"""
Linen Layout - Part I

get a list of available patterns sorted by length desc
examine each design
try to reduce it to length zero by eliminating the available substrings:

    loop through sorted available:
        e.g. brwrr: bwu -> brwrr, wr -> brr, rb -> brr, br -> r, r -> <empty> 
        e.g. bggr: bwu -> bggr, wr -> bggr, rb -> bggr, br -> bggr, r -> bgg, g -> b, b -> <empty>
        e.g gbbr: bwu -> gbbr, wr -> gbbr, rb -> gbbr, br -> gb, r -> gb, b -> b, b -> <empty>
        e.g rrbgbr: bwu -> rrbgbr, wr -> rrbgbr, rb -> rgbr, br -> rg, r -> g, g -> <empty>
        impossible:
        e.g ubwu: bwu -> u, No single u!
        e.g bbrgwb: bwu -> bbrgwb, wr -> bbrgwb, rb -> bbrgwb, br -> bgwb, gb -> bgwb, g -> bwb, b -> w, No single w!


"""


def _is_fully_reducible(string: str, substrings: list[str]) -> bool:
    for substring in substrings:
        while substring in string:
            string = string.replace(substring, "")
        if len(string) == 0:
            return True
    return len(string) == 0


def count_possible_designs(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path, "r") as puzzle_input:
        lines = puzzle_input.read().split("\n\n")
        available_patterns = lines[0].strip().replace(" ", "").split(",")
        patterns = sorted(available_patterns, key=len, reverse=True)
        print(f"patterns: {patterns}")
        designs = lines[1].strip().split("\n")
        print(f"Total number of designs: {len(designs)}.")
        impossible = 0
        for design in designs:
            if not _is_fully_reducible(string=design, substrings=patterns):
                impossible += 1
        return len(designs) - impossible


start = time.perf_counter()
print(
    count_possible_designs(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_19"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(
    count_possible_designs(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_19"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
