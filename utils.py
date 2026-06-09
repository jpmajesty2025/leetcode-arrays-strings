

def build_prefix_sum(nums):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    return prefix

def build_string(s):
    arr = []
    for c in s:
        arr.append(c)

    return "".join(arr)