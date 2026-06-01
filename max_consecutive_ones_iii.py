'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
Equivalent to finding the longest subarray with at most k zeros.
'''
def max_consecutive_ones_iii(nums, k):
    if k < 0:
        raise ValueError("k must be a positive integer")
    
    left = answer = zeros = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros +=1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        
        answer = max(answer, right-left+1)
    
    return answer