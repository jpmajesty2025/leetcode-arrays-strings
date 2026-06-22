from reverse_prefix_of_word import reverse_prefix


def test_example_1():
    assert reverse_prefix("abcdefd", "d") == "dcbaefd"


def test_example_2():
    assert reverse_prefix("xyxzxe", "z") == "zxyxxe"


def test_example_3():
    assert reverse_prefix("abcd", "z") == "abcd"


def test_ch_at_start():
    assert reverse_prefix("abcd", "a") == "abcd"


def test_ch_at_end():
    assert reverse_prefix("abcd", "d") == "dcba"


def test_reverses_to_first_occurrence_only():
    assert reverse_prefix("abacad", "a") == "abacad"


def test_single_character_match():
    assert reverse_prefix("z", "z") == "z"


def test_single_character_no_match():
    assert reverse_prefix("a", "z") == "a"


def test_repeated_target_character():
    assert reverse_prefix("aabbaa", "b") == "baabaa"
