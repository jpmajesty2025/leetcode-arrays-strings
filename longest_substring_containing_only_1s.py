'''
You are given a binary string s (a string containing only "0" and "1"). 
You may choose up to one "0" and flip it to a "1". 
What is the length of the longest substring achievable that contains only "1"?
Note: this is the same as finding the longest substring containing at most one "0",
a typical sliding window problem.
'''
def longest_substring_containing_only_1s(s):
    left = zeros = answer = 0
    for right in range(len(s)):
        if s[right] == '0':
            zeros += 1
        while zeros > 1:
            if s[left] == '0':
                zeros -= 1
            left += 1
        answer = max(answer, right - left + 1)
    return answer