# K-Radius Averages: Prefix Sum is valid… but specs are the real story

Working through `k_radius_subarry_avg.py` surfaced two great lessons:

1. **Prefix sum is optional here** (and often suboptimal)
2. **“Integer division” is not one universal thing**

---

## The problem (in one line)
For each index `i`, compute the average of the window `nums[i-k : i+k+1]`.  
If that full window doesn’t exist, return `-1` at that index.

---

## Prefix sum vs sliding window

LeetCode hints prefix sum for this one, and that’s absolutely valid:

- Prefix approach: **O(n)** time, **O(n)** space  
- Sliding window approach: **O(n)** time, **O(1)** extra space

For a fixed-width moving window, sliding window is the leaner tool.

So yes — this is another case where prefix sum is a useful concept, and a good teaching tool, but not the most memory-efficient implementation. Indeed, part of why it is a good teaching tool is that it is not the best tool for the job.

---

## The deeper issue: integer division semantics

The prompt says an average should use integer division that **truncates toward zero**.

That phrase matters more than it looks.

For positive values, floor and truncation look identical.  
For negatives, they diverge:

- `-5 / 3 = -1.666...`
- **truncate toward 0** ⇒ `-1`
- **floor** ⇒ `-2`

In Python:
- `int(-5 / 3) == -1`  ✅ truncate-toward-zero
- `-5 // 3 == -2`      ✅ floor-division (different behavior)

If your implementation silently uses `//` while your spec says truncate toward zero, you can be wrong on negative cases.

---

## “But nums are nonnegative in constraints — does it matter?”
If constraints guarantee `nums[i] >= 0`, then window sums are nonnegative and both rules coincide.

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
