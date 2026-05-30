from merge_sorted_arrays import merge


def test_both_empty():
    assert merge([], []) == []


def test_first_empty():
    assert merge([], [1, 2, 3]) == [1, 2, 3]


def test_second_empty():
    assert merge([1, 2, 3], []) == [1, 2, 3]


def test_interleaved_no_overlap():
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_first_entirely_before_second():
    assert merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_second_entirely_before_first():
    assert merge([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]


def test_duplicates_within_arrays():
    assert merge([1, 1, 3], [2, 2, 4]) == [1, 1, 2, 2, 3, 4]


def test_duplicates_between_arrays():
    assert merge([1, 2, 3], [1, 2, 3]) == [1, 1, 2, 2, 3, 3]


def test_duplicates_within_and_between_arrays():
    assert merge([1, 1, 1, 1, 3], [1, 1, 2, 2, 4]) == [1, 1, 1, 1, 1, 1, 2, 2, 3, 4]


def test_all_elements_identical():
    assert merge([2, 2], [2, 2]) == [2, 2, 2, 2]


def test_single_elements_different():
    assert merge([1], [2]) == [1, 2]


def test_single_elements_equal():
    assert merge([1], [1]) == [1, 1]


def test_negative_numbers():
    assert merge([-3, -1, 0], [-2, 1, 2]) == [-3, -2, -1, 0, 1, 2]


def test_mixed_positive_and_negative():
    assert merge([-2, 0, 3], [-1, 1, 4]) == [-2, -1, 0, 1, 3, 4]


def test_one_element_vs_many():
    assert merge([3], [1, 2, 4, 5]) == [1, 2, 3, 4, 5]


def test_longer_first_array():
    assert merge([1, 2, 3, 4, 5], [3]) == [1, 2, 3, 3, 4, 5]
