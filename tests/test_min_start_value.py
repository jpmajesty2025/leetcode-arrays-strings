from min_start_value import min_start_value


def test_example_case():
    nums = [-3, 2, -3, 4, 2]
    assert min_start_value(nums) == 5


def test_all_positive_numbers():
    nums = [1, 2, 3]
    assert min_start_value(nums) == 1


def test_empty_array():
    nums = []
    assert min_start_value(nums) == 1


def test_min_prefix_hits_zero():
    nums = [-1, 1, -1, 1]
    assert min_start_value(nums) == 2


def test_single_negative():
    nums = [-10]
    assert min_start_value(nums) == 11


def test_single_positive():
    nums = [7]
    assert min_start_value(nums) == 1


def test_large_dip_then_recovery():
    nums = [-2, -3, 10]
    assert min_start_value(nums) == 6
