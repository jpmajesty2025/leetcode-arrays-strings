'''
Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.
'''
def max_subarray_sum_fixed_k(nums, k):
    if k <= 0:
        raise ValueError("k must be a positive integer")
    
    if k > len(nums):
        return 0
    
    left = answer = current = 0
    for right in range(0,k):
        current += nums[right]
    answer = current
    
    for right in range(k,len(nums)):
        current += nums[right]
        current -= nums[left]
        left += 1
        answer = max(answer, current)
    return answer