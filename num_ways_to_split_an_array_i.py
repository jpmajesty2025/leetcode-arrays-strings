'''
Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or
equal to the sum of the second section. The second section should have at least one number.

Assumption used here: the left section may be empty, while the right section must be non-empty.
'''
from utils import build_prefix_sum


def num_ways_to_split_an_array_i(nums):
    if len(nums) == 0:
        return 0

    prefix = build_prefix_sum(nums)
    total_sum = prefix[-1]

    # Split at k = 0 => left = [], right = nums
    count = int(0 >= total_sum)

    # Splits at k = 1..len(nums)-1 (right remains non-empty)
    for i in range(len(nums) - 1):
        left_sum = prefix[i]
        right_sum = total_sum - left_sum
        count += int(left_sum >= right_sum)

    return count
