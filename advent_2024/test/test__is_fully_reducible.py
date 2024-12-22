import time
from advent_2024.test.utility import dict_parametrize
from advent_2024.day_19.p1_reducibility_fail import _is_fully_reducible
from advent_2024.day_19.p1 import _can_be_formed


_TEST_SUBSTRINGS = ["bwu", "wr", "rb", "gb", "br", "r", "b", "g"]


@dict_parametrize(
    {
        "possible_1": {
            "string": "brwrr",
            "substrings": _TEST_SUBSTRINGS,
            "expected_bool": True,
        },
        "possible_2": {
            "string": "bggr",
            "substrings": _TEST_SUBSTRINGS,
            "expected_bool": True,
        },
        "possible_3": {
            "string": "gbbr",
            "substrings": _TEST_SUBSTRINGS,
            "expected_bool": True,
        },
        "possible_4": {
            "string": "rrbgbr",
            "substrings": _TEST_SUBSTRINGS,
            "expected_bool": True,
        },
        "impossible_1": {
            "string": "ubwu",
            "substrings": _TEST_SUBSTRINGS,
            "expected_bool": False,
        },
        "impossible_2": {
            "string": "bbrgwb",
            "substrings": _TEST_SUBSTRINGS,
            "expected_bool": False,
        },
    }
)
def test__is_fully_reducible(string, substrings, expected_bool):
    assert _is_fully_reducible(string, substrings) is expected_bool


@dict_parametrize(
    {
        "possible_1": {
            "string": "brwrr",
            "substrings": _TEST_SUBSTRINGS,
            "expected_bool": True,
        },
        "possible_2": {
            "string": "bggr",
            "substrings": _TEST_SUBSTRINGS,
            "expected_bool": True,
        },
        "possible_3": {
            "string": "gbbr",
            "substrings": _TEST_SUBSTRINGS,
            "expected_bool": True,
        },
        "possible_4": {
            "string": "rrbgbr",
            "substrings": _TEST_SUBSTRINGS,
            "expected_bool": True,
        },
        "impossible_1": {
            "string": "ubwu",
            "substrings": _TEST_SUBSTRINGS,
            "expected_bool": False,
        },
        "impossible_2": {
            "string": "bbrgwb",
            "substrings": _TEST_SUBSTRINGS,
            "expected_bool": False,
        },
    }
)
def test__can_be_formed(string, substrings, expected_bool):
    assert _can_be_formed(string, substrings) is expected_bool


def fibonacci(n: int) -> int:
    if n == 2 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@dict_parametrize(
    {
        "5": {"n": 5, "expected": 5},
        "9": {"n": 9, "expected": 34},
        "36": {"n": 36, "expected": 14930352},
    }
)
def test_fibonacci(n, expected):
    start = time.perf_counter()
    assert fibonacci(n) == expected
    print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")


def fibonacci_memo(n: int, memo=None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 2 or n == 1:
        memo[n] = 1
        return 1
    else:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
        return memo[n]


@dict_parametrize(
    {
        "5": {"n": 5, "expected": 5},
        "9": {"n": 9, "expected": 34},
        "36": {"n": 36, "expected": 14930352},
        "100": {"n": 100, "expected": 354224848179261915075},
        "200": {"n": 200, "expected": 280571172992510140037611932413038677189525},
    }
)
def test_fibonacci_memo(n, expected):
    start = time.perf_counter()
    assert fibonacci_memo(n) == expected
    print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
