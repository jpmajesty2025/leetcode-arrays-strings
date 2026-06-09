from reverse_words_in_a_string_iii import reverseWords


def test_example_1():
    s = "Let's take LeetCode contest"
    assert reverseWords(s) == "s'teL ekat edoCteeL tsetnoc"


def test_example_2():
    s = "Mr Ding"
    assert reverseWords(s) == "rM gniD"


def test_single_word():
    s = "Python"
    assert reverseWords(s) == "nohtyP"


def test_preserves_word_order():
    s = "ab cd ef"
    assert reverseWords(s) == "ba dc fe"


def test_numbers_and_symbols():
    s = "a1b2 !@#"
    assert reverseWords(s) == "2b1a #@!"


def test_single_character_words():
    s = "a b c"
    assert reverseWords(s) == "a b c"


def test_mixed_case():
    s = "HeLLo WoRLD"
    assert reverseWords(s) == "oLLeH DLRoW"
