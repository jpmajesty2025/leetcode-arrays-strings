'''
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Example: nums = [-3,2,-3,4,2]
return startValue = 5 since smallest prefix sum is -4 so we need at least 5 to get the step by step sum to be never less than 1.
'''
def min_start_value(nums):
    min_sum = 0
    step_sum = 0
    for num in nums:
        step_sum += num
        min_sum = min(min_sum, step_sum)
    return 1 - min_sum