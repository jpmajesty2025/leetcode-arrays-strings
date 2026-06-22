from min_size_subarray_sum import min_subarray_len


def test_example_case_1():
    assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2


def test_example_case_2():
    assert min_subarray_len(4, [1, 4, 4]) == 1


def test_example_case_3_no_valid_subarray():
    assert min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0


def test_single_element_equal_to_target():
    assert min_subarray_len(5, [5]) == 1


def test_single_element_less_than_target():
    assert min_subarray_len(5, [4]) == 0


def test_full_array_required():
    assert min_subarray_len(15, [1, 2, 3, 4, 5]) == 5


def test_chooses_shortest_among_multiple_candidates():
    assert min_subarray_len(8, [1, 2, 3, 4, 2, 1, 1]) == 3


def test_empty_list_graceful_behavior():
    assert min_subarray_len(7, []) == 0
