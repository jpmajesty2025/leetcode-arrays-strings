from is_subsequence import is_subsequence


def test_empty_s_and_t():
    assert is_subsequence("", "") is True


def test_empty_s_nonempty_t():
    assert is_subsequence("", "abc") is True


def test_nonempty_s_empty_t():
    assert is_subsequence("a", "") is False


def test_s_equals_t():
    assert is_subsequence("abc", "abc") is True


def test_basic_true():
    assert is_subsequence("ace", "abcde") is True


def test_basic_false_wrong_order():
    assert is_subsequence("aec", "abcde") is False


def test_chars_present_but_wrong_order():
    assert is_subsequence("ba", "abc") is False


def test_s_longer_than_t():
    assert is_subsequence("abcd", "abc") is False


def test_single_char_present():
    assert is_subsequence("b", "abc") is True


def test_single_char_absent():
    assert is_subsequence("d", "abc") is False


def test_s_at_start_of_t():
    assert is_subsequence("abc", "abcxyz") is True


def test_s_at_end_of_t():
    assert is_subsequence("xyz", "abcxyz") is True


def test_repeated_chars_sufficient():
    assert is_subsequence("aaa", "aaaa") is True


def test_repeated_chars_insufficient():
    assert is_subsequence("aaa", "aa") is False


def test_s_spread_across_t():
    assert is_subsequence("ace", "xaxbcyez") is True


def test_identical_single_char():
    assert is_subsequence("a", "a") is True


def test_no_common_chars():
    assert is_subsequence("xyz", "abc") is False
