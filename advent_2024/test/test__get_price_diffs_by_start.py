from advent_2024.day_22.p2 import _get_price_diffs_by_start
from advent_2024.test.utility import dict_parametrize


@dict_parametrize(
    {
        "easy_as": {
            "secret_starts": [123],
            "_limit": 9,
            "expected_dict": {
                123: {
                    "bananas": [3, 0, 6, 5, 4, 4, 6, 4, 4, 2],
                    "diffs": [-3, 6, -1, -1, 0, 2, -2, 0, -2],
                }
            },
        }
    }
)
def test__get_price_diffs_by_start(secret_starts, _limit, expected_dict):
    assert (
        _get_price_diffs_by_start(secret_starts=secret_starts, _limit=_limit)
        == expected_dict
    )
