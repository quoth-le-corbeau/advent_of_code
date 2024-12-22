from typing import Dict, Any

import pytest


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
