from reusables import dict_parametrize
from advent_2019.day_10.solutions import _gcd, _get_unit_vector


@dict_parametrize(
    {
        "simple_case": {"x": 4, "y": 6, "expected_gcd": 2},
        "simple_case_negative": {"x": -4, "y": 6, "expected_gcd": 2},
        "coprime": {"x": 4, "y": 9, "expected_gcd": 1},
        "very_divisible": {"x": 36, "y": 48, "expected_gcd": 12},
    }
)
def test__gcd(x, y, expected_gcd):
    assert _gcd(x, y) == expected_gcd


@dict_parametrize(
    {
        "already_unit_vector_close": {
            "from_": (3, 7),
            "to_": (2, 5),
            "expected_unit_vector": (-1, -2),
        },
        "already_unit_vector_far": {
            "from_": (13, 17),
            "to_": (22, 21),
            "expected_unit_vector": (9, 4),
        },
        "simple_reduction": {
            "from_": (7, 3),
            "to_": (9, 7),
            "expected_unit_vector": (1, 2),
        },
    }
)
def test__get_unit_vector(from_, to_, expected_unit_vector):
    assert _get_unit_vector(from_, to_) == expected_unit_vector
