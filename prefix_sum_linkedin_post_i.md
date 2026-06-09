# Prefix Sums: A tiny pre-processing trick that makes range-sum queries fast

If you're working with an array of numbers, one very practical idea is based on the following definitions:

- **Prefix** of an array = elements from index `0` to `i`
- **Prefix sum** at `i` = sum of elements from index `0` to `i`

So for `nums = [1, 6, 3, 2, 7, 2]`, the prefix-sum array is:

`[1, 7, 10, 12, 19, 21]`

---

## Problem
Given:
- an integer array `nums`
- `queries`, a list where each query denotes a subarry via a list of indices `[x, y]` with `x <= y`
- a `limit`

Return a boolean array where each answer is `True` if `sum(nums[x:y+1]) < limit`, else `False`.

Example:
- `nums = [1, 6, 3, 2, 7, 2]`
- `queries = [[0, 3], [2, 5], [2, 4]]`
- `limit = 13`
- Output: `[True, False, True]`

---

## A brute-force solution
For each query `[x, y]`, loop from `x` to `y` and sum the subarray.

- If there are `q` queries and average queried length is `k`, time complexity is **O(q * k)**.
- In worst case (`k ~ n`), that becomes **O(qn)**.

Sure, it works fine for this toy example, but itt scales poorly when queries are many.

---

## The slick approach using a prefix-sum optimization
Pseudocode:
```
init prefix = to nums[0]
for i = 1..nums.length - 1
    append to prefix: nums[i] + rightmost prefix value
```

Then each query requires 3 lookups. Time cost O(1):

```
subarray_sum = prefix[y] - prefix[x] + nums[x]
```

Why this formula?
- `prefix[y]` is sum `0..y`
- `prefix[x]` is sum `0..x`
- subtracting removes the left endpoint, so we add it back in with `nums[x]`

An equivalent common form to compute **subarray_sum**, with conditional logic for the edge case:
- if `x == 0`: `prefix[y]`
- else: `prefix[y] - prefix[x-1]`

### Complexity
- Build prefix: **O(n)** time, **O(n)** space
- Each query: **O(1)** time
- Total, assuming **len(queries) == q**: **O(n + q)** time, **O(n)** space

That’s a big improvement over **O(qn)** when **q** is large.

---

## Takeaway
Prefix sums are a classic **pay-once, query-fast** strategy:
- The downside:  O(n) time upfront to build the prefix sum array and O(n) of in-memory storage space to stash it
- The upside: Answer many range-sum queries in O(1) each

Great example of turning repeated work into pre-processing. 🚀

#LearningInPublic #python #algorithms #datastructures #leetcode #codinginterview #prefixsum