from longest_subarray_with_sum_leq_k import longest_subarray_with_sum_leq_k


def test_empty_array():
    assert longest_subarray_with_sum_leq_k([], 5) == 0


def test_single_element_within_k():
    assert longest_subarray_with_sum_leq_k([3], 5) == 1


def test_single_element_equals_k():
    assert longest_subarray_with_sum_leq_k([5], 5) == 1


def test_single_element_exceeds_k():
    assert longest_subarray_with_sum_leq_k([10], 5) == 0


def test_entire_array_fits():
    assert longest_subarray_with_sum_leq_k([1, 2, 3], 6) == 3


def test_k_larger_than_total_sum():
    assert longest_subarray_with_sum_leq_k([1, 2, 3], 100) == 3


def test_k_is_zero():
    # all values are positive so no subarray can have sum <= 0
    assert longest_subarray_with_sum_leq_k([1, 2, 3], 0) == 0


def test_classic_example():
    assert longest_subarray_with_sum_leq_k([3, 1, 2, 7, 4, 2, 1, 1, 5], 8) == 4


def test_best_subarray_at_start():
    assert longest_subarray_with_sum_leq_k([1, 1, 1, 1, 5], 4) == 4


def test_best_subarray_at_end():
    assert longest_subarray_with_sum_leq_k([5, 1, 1, 1, 1], 4) == 4


def test_best_subarray_in_middle():
    assert longest_subarray_with_sum_leq_k([5, 1, 1, 1, 5], 4) == 3


def test_window_must_shrink_multiple_times():
    assert longest_subarray_with_sum_leq_k([10, 1, 10], 1) == 1


def test_all_elements_equal():
    assert longest_subarray_with_sum_leq_k([2, 2, 2, 2], 4) == 2


def test_k_equals_one_element():
    assert longest_subarray_with_sum_leq_k([3, 1, 2], 3) == 2


def test_all_elements_exceed_k():
    assert longest_subarray_with_sum_leq_k([5, 6, 7], 4) == 0
