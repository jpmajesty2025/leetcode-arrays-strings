'''
 Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k.
'''
def longest_subarray_with_sum_leq_k(nums, k):
    left = 0
    current = 0
    answer = 0
    for right in range(len(nums)):
        current += nums[right]
        while current > k:
            current -= nums[left]
            left += 1
        answer = max(answer, right - left + 1)
    return answer