import time
import pathlib
from collections import defaultdict

import common


def find_most_sleepy_strategy_2(file_path: str) -> int:
    with open(pathlib.Path(__file__).parent / file_path) as puzzle_input:
        guards_by_id = common.sleep_records_by_id(puzzle_input=puzzle_input)
        tally_dict_by_guard = defaultdict(dict)
        max_tally = 0
        guard_to_choose = 0
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
            tally_dict_by_guard[guard_id] = tally_dict
            max_key = max(tally_dict, key=tally_dict.get)
            if tally_dict[max_key] > max_tally:
                max_minute = max_key
                max_tally = tally_dict[max_key]
                guard_to_choose = guard_id
        print(
            f"Guard {guard_to_choose}: spent minute: {max_minute} asleep {max_tally} times."
        )
        return guard_to_choose * max_minute


start = time.perf_counter()
print(find_most_sleepy_strategy_2("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(find_most_sleepy_strategy_2("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
