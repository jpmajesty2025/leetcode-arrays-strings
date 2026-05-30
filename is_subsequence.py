'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
'''
def is_subsequence(s, t):
    '''
    Check if string s is a subsequence of string t.
    Time complexity: O(n) where n is the length of t.
    Space complexity: O(1) since we only use a few pointers.
    '''
    i = j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)