from reverse_only_letters import reverse_only_letters


def test_example_1():
    assert reverse_only_letters("ab-cd") == "dc-ba"


def test_example_2():
    assert reverse_only_letters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"


def test_example_3():
    assert reverse_only_letters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"


def test_all_letters():
    assert reverse_only_letters("AbCd") == "dCbA"


def test_no_letters():
    assert reverse_only_letters("123-+=") == "123-+="


def test_single_character():
    assert reverse_only_letters("Z") == "Z"
