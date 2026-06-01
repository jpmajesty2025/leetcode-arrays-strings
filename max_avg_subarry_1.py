'''
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.
'''
def max_avg_subarray(nums, k):
    if k <= 0 or k > len(nums):
        raise ValueError("k must be a positive integer and <= len(nums)")

    max_sum = current_sum = sum(nums[:k])
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, current_sum)
    return max_sum/k