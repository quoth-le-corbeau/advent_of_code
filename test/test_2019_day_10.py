from reusables import dict_parametrize
from advent_2019.day_10.solutions import _get_vectors, NESW_UNIT_VECTORS


@dict_parametrize(
    {
        "3_rows_4_cols_middle_right": {
            # . . . .
            # . . x .
            # . . . .
            "rows": 3,
            "columns": 4,
            "point": (2, 1),
            "expected_vectors": NESW_UNIT_VECTORS.union(
                {
                    (1, -1),
                    (1, 1),
                    (-1, 1),
                    (-1, -1),
                    (-2, -1),
                    (-2, 1),
                }
            ),
        },
        "4_rows_4_cols_middle_top_right": {
            # . . . .
            # . . x .
            # . . . .
            # . . . .
            "rows": 4,
            "columns": 4,
            "point": (2, 1),
            "expected_vectors": NESW_UNIT_VECTORS.union(
                {
                    (1, -1),
                    (1, 1),
                    (1, 2),
                    (-1, 1),
                    (-1, 2),
                    (-1, -1),
                    (-2, -1),
                    (-2, 1),
                    (-2, 2),
                }
            ),
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
                (1, 0),
                (0, 1),
                (1, 1),
                (2, 1),
                (2, 2),
                (2, 3),
                (3, 1),
                (3, 2),
                (3, 3),
                (1, 2),
                (1, 3),
            },
        },
    }
)
def test__get_vectors(point, rows, columns, expected_vectors):
    assert sorted(list(_get_vectors(point=point, rows=rows, cols=columns))) == list(
        sorted(expected_vectors)
    )
