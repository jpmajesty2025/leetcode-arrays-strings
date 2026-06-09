'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
'''
from in_place_string_reversal import reverse_string

def reverse_words(s: str) -> str:
    """Reverse characters in each word while preserving word order and spaces."""
    rev_sentence: list[str] = []
    sentence_split = s.split(' ')
    for word in sentence_split:
        char_list = list(word)
        reverse_string(char_list)
        rev_word = ''.join(char_list)
        rev_sentence.append(rev_word)
    return ' '.join(rev_sentence)


def reverseWords(s: str) -> str:
    """LeetCode-compatible wrapper."""
    return reverse_words(s)