from num_ways_to_split_an_array_i import num_ways_to_split_an_array_i


def test_empty_array_returns_zero():
    assert num_ways_to_split_an_array_i([]) == 0


def test_single_negative_element_counts_empty_left_split():
    assert num_ways_to_split_an_array_i([-1]) == 1


def test_single_positive_element_does_not_count_empty_left_split():
    assert num_ways_to_split_an_array_i([5]) == 0


def test_example_case():
    assert num_ways_to_split_an_array_i([10, 4, -8, 7]) == 2


def test_all_zeroes():
    assert num_ways_to_split_an_array_i([0, 0, 0]) == 3


def test_mixed_values():
    assert num_ways_to_split_an_array_i([2, 3, 1, 0]) == 2
