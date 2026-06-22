from max_vowels_in_substrng_of_given_len import max_vowels


def test_example_1():
    assert max_vowels("abciiidef", 3) == 3


def test_example_2():
    assert max_vowels("aeiou", 2) == 2


def test_example_3():
    assert max_vowels("leetcode", 3) == 2


def test_single_character_vowel():
    assert max_vowels("a", 1) == 1


def test_single_character_consonant():
    assert max_vowels("b", 1) == 0


def test_all_vowels():
    assert max_vowels("aaaaa", 3) == 3


def test_no_vowels():
    assert max_vowels("bcdfg", 2) == 0


def test_k_equals_full_length():
    assert max_vowels("banana", 6) == 3


def test_early_exit_when_window_reaches_k_vowels():
    assert max_vowels("zzzaeiou", 5) == 5
