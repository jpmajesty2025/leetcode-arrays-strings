import pytest

from max_avg_subarry_1 import max_avg_subarray


def test_example_case():
    assert max_avg_subarray([1, 12, -5, -6, 50, 3], 4) == pytest.approx(12.75)


def test_all_negative_numbers():
    assert max_avg_subarray([-1, -12, -5, -6, -50, -3], 2) == pytest.approx(-5.5)


def test_k_equals_one():
    assert max_avg_subarray([5, -2, 7, 1], 1) == pytest.approx(7.0)


def test_k_equals_length_of_array():
    assert max_avg_subarray([2, 4, 6, 8], 4) == pytest.approx(5.0)


def test_mixed_numbers_matches_bruteforce_result():
    nums = [7, -3, 10, -2, 6, -1, 4]
    k = 3
    expected = max(sum(nums[i : i + k]) / k for i in range(len(nums) - k + 1))
    assert max_avg_subarray(nums, k) == pytest.approx(expected)


def test_raises_when_k_is_zero():
    with pytest.raises(ValueError):
        max_avg_subarray([1, 2, 3], 0)


def test_raises_when_k_is_negative():
    with pytest.raises(ValueError):
        max_avg_subarray([1, 2, 3], -1)


def test_raises_when_k_greater_than_len_nums():
    with pytest.raises(ValueError):
        max_avg_subarray([1, 2, 3], 4)
