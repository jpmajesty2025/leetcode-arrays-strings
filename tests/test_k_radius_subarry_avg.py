from k_radius_subarry_avg import k_radius_avg


def test_full_example_from_prompt():
    nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
    assert k_radius_avg(nums, 3) == [-1, -1, -1, 5, 4, 4, -1, -1, -1]


def test_k_zero_returns_original_values():
    nums = [5, 1, 9]
    assert k_radius_avg(nums, 0) == [5, 1, 9]


def test_array_too_short_returns_all_negative_one():
    nums = [1, 2, 3]
    assert k_radius_avg(nums, 2) == [-1, -1, -1]


def test_single_center_window():
    nums = [1, 2, 3, 4, 5]
    assert k_radius_avg(nums, 2) == [-1, -1, 3, -1, -1]


def test_negative_values_truncate_toward_zero():
    # Center window sum is -1 and window length is 3.
    # Truncating toward zero should yield 0 (not -1).
    nums = [-1, 0, 0]
    assert k_radius_avg(nums, 1) == [-1, 0, -1]
