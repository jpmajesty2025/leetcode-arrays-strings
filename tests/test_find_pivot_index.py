from find_pivot_index import pivot_index


def test_example_1():
    assert pivot_index([1, 7, 3, 6, 5, 6]) == 3


def test_example_2():
    assert pivot_index([1, 2, 3]) == -1


def test_example_3():
    assert pivot_index([2, 1, -1]) == 0


def test_pivot_at_last_index():
    assert pivot_index([-1, -1, 0, 1, 1, 0]) == 5


def test_all_zeros_leftmost_pivot_returned():
    assert pivot_index([0, 0, 0, 0]) == 0


def test_single_element_array():
    assert pivot_index([10]) == 0


def test_negative_values_with_middle_pivot():
    assert pivot_index([-2, 5, -3, 0]) == 3
