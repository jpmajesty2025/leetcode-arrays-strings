from in_place_string_reversal import reverse_string


def test_returns_none():
    assert reverse_string(["a", "b", "c"]) is None


def test_empty_list():
    s = []
    reverse_string(s)
    assert s == []


def test_single_char():
    s = ["a"]
    reverse_string(s)
    assert s == ["a"]


def test_two_chars():
    s = ["a", "b"]
    reverse_string(s)
    assert s == ["b", "a"]


def test_odd_length():
    s = ["h", "e", "l", "l", "o"]
    reverse_string(s)
    assert s == ["o", "l", "l", "e", "h"]


def test_even_length():
    s = ["a", "b", "c", "d"]
    reverse_string(s)
    assert s == ["d", "c", "b", "a"]


def test_palindrome():
    s = ["r", "a", "c", "e", "c", "a", "r"]
    reverse_string(s)
    assert s == ["r", "a", "c", "e", "c", "a", "r"]


def test_all_same_chars():
    s = ["a", "a", "a", "a"]
    reverse_string(s)
    assert s == ["a", "a", "a", "a"]


def test_with_spaces():
    s = ["a", " ", "b"]
    reverse_string(s)
    assert s == ["b", " ", "a"]


def test_with_digits():
    s = ["1", "2", "3", "4", "5"]
    reverse_string(s)
    assert s == ["5", "4", "3", "2", "1"]


def test_mixed_case():
    s = ["H", "e", "L", "l", "O"]
    reverse_string(s)
    assert s == ["O", "l", "L", "e", "H"]
