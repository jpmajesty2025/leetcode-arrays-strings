import pytest

from max_consecutive_ones_iii import max_consecutive_ones_iii


def test_example_case_1():
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    assert max_consecutive_ones_iii(nums, 2) == 6


def test_example_case_2():
    nums = [0, 0, 1, 1, 1, 0, 0]
    assert max_consecutive_ones_iii(nums, 0) == 3


def test_all_ones():
    assert max_consecutive_ones_iii([1, 1, 1, 1], 2) == 4


def test_all_zeros_with_limited_flips():
    assert max_consecutive_ones_iii([0, 0, 0, 0], 2) == 2


def test_all_zeros_with_enough_flips():
    assert max_consecutive_ones_iii([0, 0, 0, 0], 4) == 4


def test_all_zeros_with_more_than_enough_flips():
    assert max_consecutive_ones_iii([0, 0, 0, 0], 5) == 4


def test_empty_array():
    assert max_consecutive_ones_iii([], 3) == 0


def test_k_greater_than_number_of_zeros():
    assert max_consecutive_ones_iii([1, 0, 1, 1, 0, 1], 10) == 6


def test_single_zero_with_no_flips():
    assert max_consecutive_ones_iii([0], 0) == 0


def test_single_zero_with_one_flip():
    assert max_consecutive_ones_iii([0], 1) == 1


def test_raises_when_k_is_negative():
    with pytest.raises(ValueError):
        max_consecutive_ones_iii([1, 0, 1], -1)
