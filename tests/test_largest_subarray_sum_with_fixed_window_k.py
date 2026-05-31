from largest_subarray_sum_with_fixed_window_k import max_subarray_sum_fixed_k


def test_mixed_values_window_size_three():
    nums = [2, 1, 5, 1, 3, 2]
    k = 3

    assert max_subarray_sum_fixed_k(nums, k) == 9


def test_k_equals_array_length():
    nums = [4, -1, 2]
    k = 3

    assert max_subarray_sum_fixed_k(nums, k) == 5


def test_k_larger_than_array_length_returns_zero():
    nums = [1, 2]
    k = 3

    assert max_subarray_sum_fixed_k(nums, k) == 0


def test_all_negative_values():
    nums = [-5, -2, -3, -4]
    k = 2

    assert max_subarray_sum_fixed_k(nums, k) == -5


def test_window_size_one_returns_max_element():
    nums = [3, -7, 8, 1]
    k = 1

    assert max_subarray_sum_fixed_k(nums, k) == 8


def test_empty_array_with_positive_k_returns_zero():
    nums = []
    k = 1

    assert max_subarray_sum_fixed_k(nums, k) == 0
