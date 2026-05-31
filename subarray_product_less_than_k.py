'''
Given an array of positive integers nums and an integer k, return the number of subarrays where the product 
of all the elements in the subarray is strictly less than k.
'''
def subarray_product_lt_k(nums, k):
    if k <= 1:
        return 0
    left = answer = 0
    product = 1
    for right in range(len(nums)):
        product *= nums[right]
        while product >= k:
            product //= nums[left]
            left += 1
        answer += right - left + 1
    return answer