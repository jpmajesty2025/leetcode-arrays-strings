from answer_queries import answer_queries


def test_example_case():
    nums = [1, 6, 3, 2, 7, 2]
    queries = [[0, 3], [2, 5], [2, 4]]
    limit = 13
    assert answer_queries(nums, queries, limit) == [True, False, True]


def test_single_element_queries():
    nums = [5, 1, 4]
    queries = [[0, 0], [1, 1], [2, 2]]
    assert answer_queries(nums, queries, 5) == [False, True, True]


def test_full_range_and_subranges():
    nums = [2, 2, 2, 2]
    queries = [[0, 3], [1, 2], [0, 1]]
    assert answer_queries(nums, queries, 7) == [False, True, True]


def test_limit_is_strictly_less_than():
    nums = [3, 1, 2]
    queries = [[0, 2], [1, 2]]
    # sums are 6 and 3, and comparison is "< limit" (not "<=")
    assert answer_queries(nums, queries, 6) == [False, True]


def test_negative_numbers():
    nums = [4, -2, -1, 3]
    queries = [[0, 2], [1, 3], [2, 2]]
    # sums are 1, 0, -1
    assert answer_queries(nums, queries, 1) == [False, True, True]


def test_empty_queries_returns_empty_list():
    nums = [1, 2, 3]
    queries = []
    assert answer_queries(nums, queries, 10) == []
