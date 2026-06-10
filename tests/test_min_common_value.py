from min_common_value import get_min_common_value


def test_example_1():
    assert get_min_common_value([1, 2, 3], [2, 4]) == 2


def test_example_2():
    assert get_min_common_value([1, 2, 3, 6], [2, 3, 4, 5]) == 2


def test_no_common_value():
    assert get_min_common_value([1, 3, 5], [2, 4, 6]) == -1


def test_common_value_at_start():
    assert get_min_common_value([2, 10, 20], [2, 3, 4]) == 2


def test_common_value_at_end():
    assert get_min_common_value([1, 4, 9], [2, 7, 9]) == 9


def test_duplicates_in_both_arrays():
    assert get_min_common_value([1, 2, 2, 2, 5], [2, 2, 3]) == 2


def test_multiple_common_values_returns_smallest():
    assert get_min_common_value([1, 2, 3, 7], [2, 3, 8]) == 2
