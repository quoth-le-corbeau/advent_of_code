from reusables import dict_parametrize
from advent_2019.day_7.solutions import (
    _get_max_thrust_permutation,
    _get_max_thrust_permutation_feedback_mode,
)

TEST_PROG_2 = [
    3,
    23,
    3,
    24,
    1002,
    24,
    10,
    24,
    1002,
    23,
    -1,
    23,
    101,
    5,
    23,
    23,
    1,
    24,
    23,
    23,
    4,
    23,
    99,
    0,
    0,
]
TEST_PROG_3 = [
    3,
    31,
    3,
    32,
    1002,
    32,
    10,
    32,
    1001,
    31,
    -2,
    31,
    1007,
    31,
    0,
    33,
    1002,
    33,
    7,
    33,
    1,
    33,
    31,
    31,
    1,
    32,
    31,
    31,
    4,
    31,
    99,
    0,
    0,
    0,
]
TEST_FEEDBACK_PROG_1 = [
    3,
    26,
    1001,
    26,
    -4,
    26,
    3,
    27,
    1002,
    27,
    2,
    27,
    1,
    27,
    26,
    27,
    4,
    27,
    1001,
    28,
    -1,
    28,
    1005,
    28,
    6,
    99,
    0,
    0,
    5,
]
TEST_FEEDBACK_PROG_2 = [
    3,
    52,
    1001,
    52,
    -5,
    52,
    3,
    53,
    1,
    52,
    56,
    54,
    1007,
    54,
    5,
    55,
    1005,
    55,
    26,
    1001,
    54,
    -5,
    54,
    1105,
    1,
    12,
    1,
    53,
    54,
    53,
    1008,
    54,
    0,
    55,
    1001,
    55,
    1,
    55,
    2,
    53,
    55,
    53,
    4,
    53,
    1001,
    56,
    -1,
    56,
    1005,
    56,
    6,
    99,
    0,
    0,
    0,
    0,
    10,
]


@dict_parametrize(
    {
        "43210": {
            "program": [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0],
            "expected_max_thrust": 43210,
            "expected_max_thrust_phase_setting": (4, 3, 2, 1, 0),
        },
        "54321": {
            "program": TEST_PROG_2,
            "expected_max_thrust": 54321,
            "expected_max_thrust_phase_setting": (0, 1, 2, 3, 4),
        },
        "65210": {
            "program": TEST_PROG_3,
            "expected_max_thrust": 65210,
            "expected_max_thrust_phase_setting": (1, 0, 4, 3, 2),
        },
    }
)
def test__get_max_thrust_permutation(
    program, expected_max_thrust, expected_max_thrust_phase_setting
):
    max_thrust, phase_setting = _get_max_thrust_permutation(program=program)
    assert max_thrust == expected_max_thrust
    assert phase_setting == expected_max_thrust_phase_setting


@dict_parametrize(
    {
        "139629729": {
            "program": TEST_FEEDBACK_PROG_1,
            "expected_max_thrust": 139629729,
            "expected_max_thrust_phase_setting": (9, 8, 7, 6, 5),
        },
        "18216": {
            "program": TEST_FEEDBACK_PROG_2,
            "expected_max_thrust": 18216,
            "expected_max_thrust_phase_setting": (9, 7, 8, 5, 6),
        },
    }
)
def test__get_max_thrust_permutation_feedback_mode(
    program, expected_max_thrust, expected_max_thrust_phase_setting
):
    max_thrust, phase_setting = _get_max_thrust_permutation_feedback_mode(
        program=program
    )
    assert max_thrust == expected_max_thrust
    assert phase_setting == expected_max_thrust_phase_setting
