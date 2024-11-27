from typing import List, TextIO, Dict
import pendulum
from collections import defaultdict
import re


def sleep_records_by_id(
    puzzle_input: TextIO,
) -> Dict[int, List[pendulum.DateTime]]:
    records = sorted(puzzle_input.read().splitlines())
    guards_by_id = defaultdict(list)
    for i, record in enumerate(sorted(records)):
        guard_number_match = re.search(r"Guard #(\d+) begins shift", record)
        if guard_number_match is not None:
            guard_id = int(guard_number_match.group(1))
            look_ahead = 1
            while (
                i + look_ahead < len(records) and "Guard" not in records[i + look_ahead]
            ):
                line = records[i + look_ahead]
                dt = pendulum.parse(re.search(r"\[(.*?)]", line).group(1))
                if "falls asleep" in line:
                    guards_by_id[guard_id].append(dt)
                elif "wakes up" in line:
                    guards_by_id[guard_id].append(dt)
                else:
                    raise ValueError(f"unexpected record: {line}")
                look_ahead += 1
    return guards_by_id
