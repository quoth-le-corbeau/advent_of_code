import time
from typing import Dict, Any
from functools import wraps

import pytest

INPUT_PATH = "my_inputs/{year}/day_{day}/{file}.txt"


def timer(func):
    @wraps(func)
    def timed_function(*args, **kwargs):
        timer_start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - timer_start
        print(result)
        print(
            f"Function '{func.__name__}' with input file {kwargs.get('file')}"
            f" executed in {elapsed_time:.4f} seconds."
        )
        return result

    return timed_function


def dict_parametrize(test_cases_by_id: Dict[str, Dict[str, Any]]):
    case_ids = list(test_cases_by_id.keys())
    test_cases = list(test_cases_by_id.values())
    sorted_args_names = sorted(test_cases[0].keys())
    args_string = ",".join(sorted_args_names)
    if len(sorted_args_names) > 1:
        parameters = [
            tuple(case[arg_name] for arg_name in sorted_args_names)
            for case in test_cases
        ]
    else:
        parameters = [case[sorted_args_names[0]] for case in test_cases]

    return pytest.mark.parametrize(args_string, parameters, ids=case_ids)
