import pytest
from typing import Dict, Any

from advent_2024.day_17.p1 import Computer


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


@dict_parametrize(
    {
        "adv": {
            "registers": (0, 0, 9),
            "op_code": 2,
            "operand": 6,
            "expected_registers": (0, 1, 9),
            "expected_output": None,
        },
        "bxl": {
            "registers": (0, 29, 0),
            "op_code": 1,
            "operand": 7,
            "expected_registers": (0, 26, 0),
            "expected_output": None,
        },
    }
)
def test_computer(registers, op_code, operand, expected_registers, expected_output):
    computer = Computer(
        register_A=registers[0], register_B=registers[1], register_C=registers[2]
    )
    computer.instruction_map[op_code](operand)
    assert (
        computer.register_A,
        computer.register_B,
        computer.register_C,
    ) == expected_registers
    if expected_output is not None:
        assert computer.output == expected_output
