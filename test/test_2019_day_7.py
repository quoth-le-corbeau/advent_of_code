from reusables import dict_parametrize
from advent_2019.day_7.solutions import _get_max_thrust_permutation

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
