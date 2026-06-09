'''
You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements
in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero,
which means losing its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

Full example:
Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
Output: [-1,-1,-1,5,4,4,-1,-1,-1]
Explanation:
- avg[0], avg[1], and avg[2] are -1 because there are less than k elements before each index.
- The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37.
  Using integer division, avg[3] = 37 / 7 = 5.
- For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4.
- For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4.
- avg[6], avg[7], and avg[8] are -1 because there are less than k elements after each index.
'''


def k_radius_avg(nums: list[int], k: int) -> list[int]:
    """Return k-radius averages for each index, using -1 where the window is invalid.

    A valid window centered at index i includes elements from i-k to i+k (inclusive),
    so the window length is (2k + 1). When fewer than k elements exist on either side,
    the corresponding result is -1.

    Division uses truncation toward zero (via int(total / window_len)).
    """
    result: list[int] = [-1] * len(nums)
    window_len = 2 * k + 1

    if len(nums) < window_len:
        return result

    running_sum = sum(nums[:window_len])

    # Truncate toward zero (robust for negative totals too).
    result[k] = int(running_sum / window_len)

    for i in range(k + 1, len(nums) - k):
        running_sum -= nums[i - k - 1]
        running_sum += nums[i + k]
        result[i] = int(running_sum / window_len)

    return result
