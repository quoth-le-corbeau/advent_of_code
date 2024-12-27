import time
import pathlib
from collections import defaultdict

from advent_2018.day_4 import common


def find_most_sleepy_strategy_1(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path) as puzzle_input:
        guards_by_id = common.sleep_records_by_id(puzzle_input=puzzle_input)
        longest_napper = 0
        longest_nap_time = 0
        tally_dict_by_guard = defaultdict(dict)
        for guard_id, timestamps in guards_by_id.items():
            tally_dict = {x: 0 for x in range(60)}
            naps = zip(timestamps[::2], timestamps[1::2])
            total_nap_time = 0
            for nap in naps:
                t1, t2 = nap
                for minute in range(t1.minute, t2.minute):
                    tally_dict[minute] += 1
                nap_time = t2.minute - t1.minute
                total_nap_time += nap_time
            if total_nap_time > longest_nap_time:
                longest_nap_time = total_nap_time
                longest_napper = guard_id
            tally_dict_by_guard[guard_id] = tally_dict
        print(
            f"guard: {longest_napper} is longest napper with: {longest_nap_time} minutes in total."
        )
        longest_napper_tally_dict = tally_dict_by_guard[longest_napper]
        most_common_minute = max(
            longest_napper_tally_dict, key=longest_napper_tally_dict.get
        )
        print(f"most common minute: {most_common_minute}")
        return longest_napper * most_common_minute


timer_start = time.perf_counter()
print(
    find_most_sleepy_strategy_1(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2018/day_4"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

timer_start = time.perf_counter()
print(
    find_most_sleepy_strategy_1(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2018/day_4"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")
