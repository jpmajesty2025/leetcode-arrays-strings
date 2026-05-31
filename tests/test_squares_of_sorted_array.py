from squares_of_sorted_array import sorted_squares


def test_empty():
    assert sorted_squares([]) == []


def test_single_zero():
    assert sorted_squares([0]) == [0]


def test_single_positive():
    assert sorted_squares([5]) == [25]


def test_single_negative():
    assert sorted_squares([-3]) == [9]


def test_all_non_negative():
    assert sorted_squares([1, 2, 3, 4]) == [1, 4, 9, 16]


def test_all_non_positive():
    assert sorted_squares([-4, -3, -2, -1]) == [1, 4, 9, 16]


def test_all_zeros():
    assert sorted_squares([0, 0, 0]) == [0, 0, 0]


def test_mix_with_zero():
    assert sorted_squares([-2, 0, 2]) == [0, 4, 4]


def test_classic_example_1():
    assert sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]


def test_classic_example_2():
    assert sorted_squares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]


def test_symmetric_array():
    assert sorted_squares([-3, -2, 2, 3]) == [4, 4, 9, 9]


def test_longer_negative_prefix():
    assert sorted_squares([-5, -4, -3, 1, 2]) == [1, 4, 9, 16, 25]


def test_longer_positive_suffix():
    assert sorted_squares([-1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]


def test_all_same_value():
    assert sorted_squares([2, 2, 2]) == [4, 4, 4]
