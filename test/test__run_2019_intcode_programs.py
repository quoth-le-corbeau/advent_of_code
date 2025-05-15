from advent_2019.day_2.solutions import _run
from reusables import dict_parametrize


@dict_parametrize(
    {
        "case_1": {"program": [1, 0, 0, 0, 99], "expected_output": [2, 0, 0, 0, 99]},
        "case_2": {"program": [2, 3, 0, 3, 99], "expected_output": [2, 3, 0, 6, 99]},
        "case_3": {
            "program": [2, 4, 4, 5, 99, 0],
            "expected_output": [2, 4, 4, 5, 99, 9801],
        },
        "case_4": {
            "program": [1, 1, 1, 4, 99, 5, 6, 0, 99],
            "expected_output": [30, 1, 1, 4, 2, 5, 6, 0, 99],
        },
        "example_input": {
            "program": [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
            "expected_output": [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
        },
    }
)
def test__run(program, expected_output):
    assert _run(program) == expected_output
