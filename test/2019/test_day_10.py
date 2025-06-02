from reusables import dict_parametrize
from advent_2019.day_10.solutions import _get_vectors


@dict_parametrize(
    {
        "3_rows_4_cols_middle_right": {
            # . . . .
            # . . x .
            # . . . .
            "rows": 3,
            "columns": 4,
            "point": (2, 1),
            "expected_vectors": {
                (0, -1),  # N
                (1, -1),  # NE
                (1, 0),  # E
                (0, 1),  # S
                (-1, 0),  # W
                (1, 1),  # SE
                (-1, 1),  # SW
                (-1, -1),  # NW
                (-2, -1),  # WNW
                (-2, 1),  # WSW
            },
        },
        "3_rows_4_cols_furthest_from_origin": {
            # . . . .
            # . . . .
            # . . . x
            "rows": 3,
            "columns": 4,
            "point": (3, 2),
            "expected_vectors": {
                (0, -1),  # N
                (-1, 0),  # W
                (-1, -1),  # NW
                (-1, -2),  # NNW
                (-2, -1),  # WNW
                (-3, -1),  # WNW
                (-3, -2),  # WNW
            },
        },
        "4_rows_4_cols_middle_top_right": {
            # . . . .
            # . . x .
            # . . . .
            # . . . .
            "rows": 4,
            "columns": 4,
            "point": (2, 1),
            "expected_vectors": {
                (0, -1),  # N
                (1, 0),  # E
                (0, 1),  # S
                (-1, 0),  # W
                (1, -1),  # NE
                (1, 1),  # SE
                (1, 2),  # SSE
                (-1, 1),  # SW
                (-1, 2),  # SSW
                (-1, -1),  # NW
                (-2, -1),  # WNW
                (-2, 1),  # WSW
            },
        },
        "4_rows_5_cols_middle_top_right": {
            # . . . . .
            # . . x . .
            # . . . . .
            # . . . . .
            "rows": 4,
            "columns": 5,
            "point": (2, 1),
            "expected_vectors": {
                (0, -1),
                (1, 0),
                (0, 1),
                (-1, 0),
                (1, -1),
                (1, 1),
                (1, 2),
                (-1, 1),
                (-1, 2),
                (-1, -1),
                (-2, -1),
                (-2, 1),
                (2, 1),
                (2, -1),
            },
        },
        "4_rows_4_cols_middle_origin": {
            # x . . .
            # . . . .
            # . . . .
            # . . . .
            "rows": 4,
            "columns": 4,
            "point": (0, 0),
            "expected_vectors": {
                (1, 0),  # E
                (0, 1),  # S
                (1, 1),  # SE
                (1, 2),
                (1, 3),
                (2, 1),
                (2, 3),
                (3, 1),
                (3, 2),
            },
        },
    }
)
def test__get_vectors(point, rows, columns, expected_vectors):
    assert sorted(list(_get_vectors(point=point, rows=rows, cols=columns))) == list(
        sorted(expected_vectors)
    )
