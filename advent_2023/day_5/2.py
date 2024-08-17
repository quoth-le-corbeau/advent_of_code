import time
import pathlib
import bisect
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class MappingGuide:
    destination: int
    source: int
    span: int

    def __lt__(self, other):
        return self.source < other.source


def find_min_seed_range_location(file: str) -> int:
    seed_ranges, mappings = _get_seed_ranges_and_mappings(file=file)
    mapped_seed_ranges = []
    for seed_range in seed_ranges:
        mapped_seed_ranges += _trace_range_through_mappings(
            seed_range=seed_range, mappings=mappings
        )
    return min([mapped_seed_range[0] for mapped_seed_range in mapped_seed_ranges])


def _trace_range_through_mappings(
    seed_range: tuple[int, int], mappings: list[dict[str, list[float]]]
) -> list[tuple[float, float]]:
    mapped_ranges = list()
    sub_intervals = [seed_range]
    for mapping in mappings:
        new_intervals = []
        for interval in sub_intervals:
            new_intervals += _split_seed_range_over_mapping(
                mapping=mapping, seed_range=interval
            )
            sub_intervals = new_intervals
    mapped_ranges += sub_intervals
    return mapped_ranges


def _map_range_on_interval(
    mapping: dict[str, list[float]], seed_range: tuple[float, float]
) -> tuple[float, float]:
    start, end = seed_range
    index = bisect.bisect_right(mapping["sources"], start) - 1
    source = mapping["sources"][index]
    destination = mapping["destinations"][index]
    return destination + start - source, destination + end - source


def _split_seed_range_over_mapping(
    mapping: dict[str, list[float]], seed_range: tuple[float, float]
) -> list[tuple[float, float]]:
    start, end = seed_range
    end = end - 1
    start_index = bisect.bisect_right(mapping["sources"], start) - 1
    end_index = bisect.bisect_right(mapping["sources"], end) - 1
    if start_index == end_index:
        return [_map_range_on_interval(mapping=mapping, seed_range=seed_range)]
    else:
        # make intervals:
        sources_between = [
            mapping["sources"][i + 1] for i in range(start_index, end_index)
        ]
        sources_between.append(start)
        sources_between.append(end)
        new_intervals = zip(sorted(sources_between)[:-1], sorted(sources_between)[1:])
        return [
            _map_range_on_interval(mapping=mapping, seed_range=interval)
            for interval in new_intervals
        ]


def _get_seed_ranges_and_mappings(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        seeds, *blocks = puzzle_input.read().split("\n\n")
        seeds = list(map(int, seeds.split(":")[1].strip().split()))
        seed_ranges = [
            (seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)
        ]
        mappings = list()
        for block in blocks:
            mapping = _get_full_mapping(block=block)
            mappings.append(mapping)
    return seed_ranges, mappings


def _get_full_mapping(block: str) -> dict[str, list[int]]:
    guides = block.split(":")[1].strip().splitlines()
    mapping = dict()
    sources = [-1]
    destinations = [-1]
    mapping_guides = []
    for guide in guides:
        destination, source, span = [int(val) for val in guide.split()]
        mapping_guides.append(
            MappingGuide(destination=destination, source=source, span=span)
        )
    mapping = _make_full_mapping(destinations, mapping, mapping_guides, sources)
    return mapping


def _make_full_mapping(
    destinations: list[int],
    mapping: dict[str, list[int]],
    mapping_guides: list[MappingGuide],
    sources: list[int],
) -> dict[str, list[int]]:
    end_of_mapping = []
    for mapping_guide in sorted(mapping_guides):
        sources.append(mapping_guide.source)
        destinations.append(mapping_guide.destination)
        end_of_mapping.append(mapping_guide.source + mapping_guide.span)
    end_of_guides = max(end_of_mapping)
    sources.append(end_of_guides)
    destinations.append(end_of_guides)
    sources.append(math.inf)
    destinations.append(math.inf)
    mapping["sources"] = sources
    mapping["destinations"] = destinations
    return mapping


start = time.perf_counter()
print(find_min_seed_range_location("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(find_min_seed_range_location("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
