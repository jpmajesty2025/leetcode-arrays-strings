from longest_substring_containing_only_1s import longest_substring_containing_only_1s


def test_empty_string():
    assert longest_substring_containing_only_1s("") == 0


def test_single_one():
    assert longest_substring_containing_only_1s("1") == 1


def test_single_zero():
    assert longest_substring_containing_only_1s("0") == 1


def test_all_ones():
    assert longest_substring_containing_only_1s("11111") == 5


def test_all_zeros():
    assert longest_substring_containing_only_1s("00000") == 1


def test_one_zero_in_string():
    assert longest_substring_containing_only_1s("11011") == 5


def test_classic_example():
    assert longest_substring_containing_only_1s("1101100111") == 5


def test_best_window_at_start():
    assert longest_substring_containing_only_1s("11100") == 4


def test_best_window_at_end():
    assert longest_substring_containing_only_1s("00111") == 4


def test_best_window_in_middle():
    assert longest_substring_containing_only_1s("001110011") == 4


def test_adjacent_zeros():
    assert longest_substring_containing_only_1s("1100111") == 4


def test_alternating():
    assert longest_substring_containing_only_1s("10101") == 3


def test_zero_at_start():
    assert longest_substring_containing_only_1s("0111") == 4


def test_zero_at_end():
    assert longest_substring_containing_only_1s("1110") == 4


def test_two_zeros_no_ones_between():
    assert longest_substring_containing_only_1s("0110") == 3


def test_two_adjacent_zeros_only():
    assert longest_substring_containing_only_1s("00") == 1
