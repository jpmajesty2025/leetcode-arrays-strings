from get_equal_length_substrings_within_budget import equal_substring


def test_example_1():
    assert equal_substring("abcd", "bcdf", 3) == 3


def test_example_2():
    assert equal_substring("abcd", "cdef", 3) == 1


def test_example_3():
    assert equal_substring("abcd", "acde", 0) == 1


def test_zero_budget_and_no_equal_chars():
    assert equal_substring("abcd", "bcde", 0) == 0


def test_full_length_with_large_budget():
    assert equal_substring("abcd", "zzzz", 200) == 4


def test_identical_strings_with_zero_budget():
    assert equal_substring("aaaa", "aaaa", 0) == 4


def test_sliding_window_shrinks_correctly():
    assert equal_substring("abcdxyz", "bcdfxyw", 4) == 5
