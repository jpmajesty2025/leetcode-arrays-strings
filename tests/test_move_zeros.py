from move_zeros import move_zeros


def test_example_case():
    nums = [0, 1, 0, 3, 12]
    move_zeros(nums)
    assert nums == [1, 3, 12, 0, 0]


def test_single_zero():
    nums = [0]
    move_zeros(nums)
    assert nums == [0]


def test_no_zeros():
    nums = [1, 2, 3]
    move_zeros(nums)
    assert nums == [1, 2, 3]


def test_all_zeros():
    nums = [0, 0, 0, 0]
    move_zeros(nums)
    assert nums == [0, 0, 0, 0]


def test_mixed_values_with_negatives():
    nums = [4, 0, -1, 0, 0, 2, -3]
    move_zeros(nums)
    assert nums == [4, -1, 2, -3, 0, 0, 0]


def test_preserves_relative_order_of_non_zero_elements():
    nums = [0, 5, 0, 1, 0, 5, 2]
    move_zeros(nums)
    assert nums == [5, 1, 5, 2, 0, 0, 0]


def test_mutates_in_place():
    nums = [0, 1, 0, 2]
    original_id = id(nums)
    move_zeros(nums)
    assert id(nums) == original_id
    assert nums == [1, 2, 0, 0]


def test_empty_list_graceful_behavior():
    nums = []
    move_zeros(nums)
    assert nums == []
