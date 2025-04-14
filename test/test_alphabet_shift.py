from advent_2016.day_4.solutions import _alphabet_shift


def test_alphabet_shift(
    shift_steps: int = 343,
    input_string: str = "qzmt-zixmtkozy-ivhz",
    expected_output_string: str = "very encrypted name",
):
    assert _alphabet_shift(input_string, shift_steps) == expected_output_string
