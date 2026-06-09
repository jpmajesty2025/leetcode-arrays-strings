# Prefix Sum vs Running Sum: sometimes pre-processing is optional (and even suboptimal)

A follow-up to the last post that introduced prefix sums for arrays.

## Problem
Count the number of ways to split an array `nums` into `left` and `right` such that:

**sum(left) >= sum(right)**

Assumptions:
- `left` may be empty
- `right` must be non-empty
- `sum([]) = 0`

Define split position `k` as:
- `left = nums[:k]`
- `right = nums[k:]`
- valid `k` values: `0..n-1` (so `right` is never empty)

This is a range-sum flavored problem, so prefix sums are a valid approach—but not always the best one.

---

## Solution I: use a prefix-sum array

Build prefix sums first:

- `prefix[i] = nums[0] + ... + nums[i]`
- `total_sum = prefix[-1]`

Handle `k = 0` (empty left) separately:
- `count = int(0 >= total_sum)`

Then scan remaining split points (`k = 1..n-1`):
- `left_sum = prefix[k - 1]`
- `right_sum = total_sum - left_sum`
- `count += int(left_sum >= right_sum)`

### Complexity
- Build prefix: **O(n)** time, **O(n)** space
- Scan split points: **O(n)** time
- Total: **O(n)** time, **O(n)** space

---

## Solution II: running sum (no prefix array)

Use:
- `total_sum = sum(nums)` (one-time calculation)
- running `left_sum` while scanning split points

Initialize:
- `count = int(0 >= total_sum)` for `k = 0`

For `k = 1..n-1`:
- `left_sum += nums[k - 1]`
- `right_sum = total_sum - left_sum`
- `count += int(left_sum >= right_sum)`

### Complexity
- `sum(nums)`: **O(n)** time, **O(1)** extra space
- Scan split points: **O(n)** time, **O(1)** extra space
- Total: **O(n)** time, **O(1)** extra space

---

## Efficiency takeaway

Both solutions are **O(n)** time, so no asymptotic time is lost by dropping prefix storage.

### `sum(nums)` vs `build_prefix_sum(nums)`
- Both are **O(n)** time
- `build_prefix_sum(nums)` stores `n` cumulative values → **O(n)** space
- `sum(nums)` keeps only one accumulator → **O(1)** extra space

In practice, the running-sum version is often faster too (less allocation and less Python-level work), but exact speedups depend on data size and runtime.

For very large numeric workloads, NumPy can be much faster than pure Python loops—especially when data is already in `ndarray` form.

So the main win of Solution II is:
1. **Space reduction**: O(n) → O(1)
2. Often a **constant-factor runtime improvement**

---

## Rule of thumb
Use prefix sums when you need many arbitrary range-sum queries (`x..y`) answered quickly.

If one pass with running totals is enough, a full prefix array is usually unnecessary overhead.

#LearningInPublic #python #algorithms #datastructures #leetcode #prefixsum #optimization #softwareengineering
