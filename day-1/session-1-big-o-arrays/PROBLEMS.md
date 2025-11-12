# Problems - Session 1: Big O & Arrays

10 problems in order. Use UMPIRE method.

**Targets:** Easy <15 min | Medium <30 min

---

## Problem 1: Two Sum ⭐ BLIND 75

**Difficulty:** Easy | **Pattern:** Hash Map
**LeetCode:** https://leetcode.com/problems/two-sum/

### Problem

Given array `nums` and integer `target`, return indices of two numbers that add up to `target`.

Exactly one solution exists. Can't use same element twice.

### Examples

```
nums = [2,7,11,15], target = 9
Output: [0,1]  (2 + 7 = 9)

nums = [3,2,4], target = 6
Output: [1,2]

nums = [3,3], target = 6
Output: [0,1]
```

### Constraints

- 2 ≤ nums.length ≤ 10⁴
- -10⁹ ≤ nums[i], target ≤ 10⁹
- One valid answer exists

### Hints
- Brute force: O(n²) nested loops
- Optimal: Hash map for O(1) lookups → O(n)
- Store value→index as you iterate

---

## Problem 2: Best Time to Buy/Sell Stock ⭐ BLIND 75

**Difficulty:** Easy | **Pattern:** Kadane's/Greedy
**LeetCode:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

### Problem

Array `prices[i]` = stock price on day i. Buy one day, sell later. Return max profit (0 if no profit possible).

### Examples

```
prices = [7,1,5,3,6,4]
Output: 5  (buy day 2 at 1, sell day 5 at 6)

prices = [7,6,4,3,1]
Output: 0  (only decreases)
```

### Constraints

- 1 ≤ prices.length ≤ 10⁵
- 0 ≤ prices[i] ≤ 10⁴

### Hints
- Must buy before selling
- Track min price seen so far
- Track max profit at each step
- One pass: O(n) time, O(1) space

---

## Problem 3: Contains Duplicate ⭐ BLIND 75

**Difficulty:** Easy | **Pattern:** Hash Set
**LeetCode:** https://leetcode.com/problems/contains-duplicate/

### Problem

Return `true` if any value appears at least twice, `false` if all distinct.

### Examples

```
nums = [1,2,3,1] → true
nums = [1,2,3,4] → false
nums = [1,1,1,3,3,4,3,2,4,2] → true
```

### Constraints

- 1 ≤ nums.length ≤ 10⁵
- -10⁹ ≤ nums[i] ≤ 10⁹

### Hints
- Use Set to track seen numbers
- If already in set → duplicate
- O(n) time, O(n) space

---

## Problem 4: Product of Array Except Self ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Prefix/Suffix
**LeetCode:** https://leetcode.com/problems/product-of-array-except-self/

### Problem

Return array where `answer[i]` = product of all elements except `nums[i]`.

Must run in O(n) time. No division operation.

### Examples

```
nums = [1,2,3,4]
Output: [24,12,8,6]

nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

### Constraints

- 2 ≤ nums.length ≤ 10⁵
- -30 ≤ nums[i] ≤ 30
- Product fits in 32-bit integer

### Follow-up
O(1) extra space? (output doesn't count)

### Hints
- Need product left × product right
- Calculate prefix products (L→R)
- Calculate suffix products (R→L)
- Optimize: reuse output array for O(1) space

---

## Problem 5: Maximum Subarray ⭐ BLIND 75

**Difficulty:** Easy | **Pattern:** Kadane's/DP
**LeetCode:** https://leetcode.com/problems/maximum-subarray/

### Problem

Find subarray with largest sum. Return sum.

Subarray = contiguous non-empty sequence.

### Examples

```
nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6  ([4,-1,2,1])

nums = [1] → 1

nums = [5,4,-1,7,8] → 23
```

### Constraints

- 1 ≤ nums.length ≤ 10⁵
- -10⁴ ≤ nums[i] ≤ 10⁴

### Follow-up
Try divide & conquer (O(n log n))

### Hints
- Kadane's: Decide to extend or start fresh
- `currentSum = max(nums[i], currentSum + nums[i])`
- Track max seen so far
- O(n) time, O(1) space

---

## Problem 6: Maximum Product Subarray ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** DP
**LeetCode:** https://leetcode.com/problems/maximum-product-subarray/

### Problem

Find subarray with largest product. Return product.

### Examples

```
nums = [2,3,-2,4]
Output: 6  ([2,3])

nums = [-2,0,-1] → 0

nums = [-2,3,-4] → 24
```

### Constraints

- 1 ≤ nums.length ≤ 2×10⁴
- -10 ≤ nums[i] ≤ 10
- Product fits in 32-bit integer

### Hints
- Multiplication is tricky: negative × negative = positive
- Track both max AND min products
- Min can become max when × negative
- Handle zero (resets products)
- O(n) time, O(1) space

---

## Problem 7: Find Min in Rotated Sorted Array ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Binary Search
**LeetCode:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

### Problem

Sorted array rotated 1 to n times. Find minimum element.

Must be O(log n).

### Examples

```
nums = [3,4,5,1,2] → 1

nums = [4,5,6,7,0,1,2] → 0

nums = [11,13,15,17] → 11  (not rotated)
```

### Constraints

- 1 ≤ n ≤ 5000
- -5000 ≤ nums[i] ≤ 5000
- All integers unique
- Array sorted and rotated 1-n times

### Hints
- Binary search with modification
- Compare mid with right element
- If nums[mid] > nums[right] → min in right half
- Otherwise → min in left half (including mid)
- O(log n) time, O(1) space

---

## Problem 8: Search in Rotated Sorted Array ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Binary Search
**LeetCode:** https://leetcode.com/problems/search-in-rotated-sorted-array/

### Problem

Sorted array rotated at pivot. Find target index. Return -1 if not found.

Must be O(log n).

### Examples

```
nums = [4,5,6,7,0,1,2], target = 0 → 4

nums = [4,5,6,7,0,1,2], target = 3 → -1

nums = [1], target = 0 → -1
```

### Constraints

- 1 ≤ nums.length ≤ 5000
- -10⁴ ≤ nums[i], target ≤ 10⁴
- All values unique
- Array rotated at pivot

### Hints
- Modified binary search
- At least one half always sorted
- Determine which half sorted
- Check if target in sorted half
- O(log n) time, O(1) space

---

## Problem 9: 3Sum ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Two Pointers
**LeetCode:** https://leetcode.com/problems/3sum/

### Problem

Return all triplets `[nums[i], nums[j], nums[k]]` where `i ≠ j ≠ k` and sum = 0.

No duplicate triplets.

### Examples

```
nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

nums = [0,1,1] → []

nums = [0,0,0] → [[0,0,0]]
```

### Constraints

- 3 ≤ nums.length ≤ 3000
- -10⁵ ≤ nums[i] ≤ 10⁵

### Hints
- Sort array first
- Fix one number, two pointers for other two (like Two Sum)
- Skip duplicates
- O(n²) time, O(1) space (excluding output)

---

## Problem 10: Container With Most Water ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Two Pointers
**LeetCode:** https://leetcode.com/problems/container-with-most-water/

### Problem

Array `height[i]` = vertical lines. Find two lines that form container holding most water.

Can't slant container.

### Examples

```
height = [1,8,6,2,5,4,8,3,7]
Output: 49  (lines at index 1 and 8)

height = [1,1] → 1
```

### Constraints

- 2 ≤ n ≤ 10⁵
- 0 ≤ height[i] ≤ 10⁴

### Hints
- Two pointers: start at both ends
- Area = min(height[left], height[right]) × width
- Move pointer with smaller height
- O(n) time, O(1) space

---

## Summary

**Total:** 10 problems (5 Easy, 5 Medium)

**Patterns:**
- Hash Map/Set
- Kadane's Algorithm
- Prefix/Suffix Arrays
- Binary Search (Rotated)
- Two Pointers

**Blind 75:** 10/75 complete (13%)

---

**Ready?** Say: `"Claude, give me the problem"` or `"Go"`

[Solutions](./SOLUTIONS.md) | [Hints](./HINTS.md)
