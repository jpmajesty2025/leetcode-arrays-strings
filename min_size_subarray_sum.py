'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is 
greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
'''
def min_subarray_len(target: int, nums: list[int]) -> int:
    """Return the minimal length of a contiguous subarray with sum >= target."""
    left = 0
    window_sum = 0
    best_len = float('inf')

    for right, value in enumerate(nums):
        window_sum += value

        while window_sum >= target:
            best_len = min(best_len, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return best_len if best_len != float('inf') else 0