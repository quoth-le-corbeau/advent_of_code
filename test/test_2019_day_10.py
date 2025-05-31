from reusables import dict_parametrize
from advent_2019.day_10.solutions import _get_vectors


@dict_parametrize(
    {
        "3_rows_4_cols_middle_right": {
            "rows": 4,
            "columns": 3,
            "row": 1,
            "column": 2,
            "expected_vectors": [()],
        }
    }
)
def test__get_vectors(rows, columns, row, column, expected_vectors):
    assert _get_vectors(y=row, x=column, rows=rows, cols=columns) == expected_vectors
