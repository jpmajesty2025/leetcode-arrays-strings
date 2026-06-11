# K-Radius Averages: Prefix Sum is valid… but specs are the real story

## The problem in one line (with more detail below)
For each index `i`, compute the average of the window `nums[i-k : i+k+1]`.  
If that full window doesn’t exist, return `-1` at that index.

---

## Prefix sum vs sliding window

LeetCode hints at using a prefix sum. That’s valid, but let's compare:

- Prefix approach: **O(n)** time, **O(n)** space  
- Sliding window approach: **O(n)** time, **O(1)** extra space

It's optimally fast. But for a fixed-width moving window, sliding window is the leaner tool. This is another case where prefix sum is a useful concept, and a good teaching tool, but not the most memory-efficient implementation. Indeed, part of why it is a good teaching tool is that it is not automatically the best tool for the job.

---

## The deeper issue: integer division semantics

The prompt says to use integer division to compute an average and further states that the quotient should **truncate toward zero**. For instance, for a 2-radius, suppose some subarray sums to 19. The avarage is 19/5 = 3.8 which truncates to 3.

That phrase 'truncate toward zero' matters more than it looks.

For positive values, floor and truncation are identical.  
For negatives, they diverge:

- `-5 / 3 = -1.666...`
- **truncate toward 0** -> bump up to `-1`
- **floor** -> drop down to `-2`

In Python:
- `int(-5 / 3) == -1`  ✅ truncate-toward-zero
- `-5 // 3 == -2`      ✅ floor-division (different behavior)

If your implementation silently uses `//` while your spec says truncate toward zero, you can be wrong on negative cases. For this problem, there is an explicit constraint: `nums[i] >= 0`. In that case, all window sums are nonnegative and both rules coincide.

Still, encoding the **stated rule** is good engineering because it...
- Matches the spec exactly
- Survives future constraint changes
- Avoids subtle bugs when reused elsewhere

---

## Takeaway
Algorithm discussions often focus only on Big-O.  
But correctness also depends on **semantic contracts**:
- how division rounds,
- what “valid window” means,
- whether edge cases are defined explicitly.

**Integer division isn’t one thing. Specs are part of the algorithm.**

#LearningInPublic #python #algorithms #leetcode #prefixsum #slidingwindow #softwareengineering #codinginterview #problemSolving
