# Problems - Session 3: Sliding Window

10 problems in order. Use UMPIRE method.

**Targets:** Easy <15 min | Medium <25 min

---

## Problem 1: Best Time to Buy/Sell Stock

**Difficulty:** Easy | **Pattern:** Sliding Window Variant
**LeetCode:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

### Problem

Array `prices[i]` = stock price on day i. Buy one day, sell later. Return max profit.

### Examples

```
prices = [7,1,5,3,6,4]
Output: 5  (buy at 1, sell at 6)

prices = [7,6,4,3,1]
Output: 0
```

### Constraints

- 1 ≤ prices.length ≤ 10⁵
- 0 ≤ prices[i] ≤ 10⁴

### Hints
- Track min price seen so far
- Calculate profit if selling today
- Window of size 2: buy and sell points

---

## Problem 2: Longest Substring Without Repeating Characters ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Variable-Size Window
**LeetCode:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

### Problem

Find length of longest substring without repeating characters.

### Examples

```
s = "abcabcbb" → 3  ("abc")
s = "bbbbb" → 1  ("b")
s = "pwwkew" → 3  ("wke")
s = "" → 0
```

### Constraints

- 0 ≤ s.length ≤ 5×10⁴
- s consists of English letters, digits, symbols, spaces

### Hints
- Use Set to track characters in window
- Expand with right, contract when duplicate
- Each element visited at most twice

---

## Problem 3: Longest Repeating Character Replacement ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Variable-Size + Frequency
**LeetCode:** https://leetcode.com/problems/longest-repeating-character-replacement/

### Problem

Change up to k characters to any uppercase letter. Return length of longest substring with same letter.

### Examples

```
s = "ABAB", k = 2 → 4
s = "AABABBA", k = 1 → 4
```

### Constraints

- 1 ≤ s.length ≤ 10⁵
- 0 ≤ k ≤ s.length
- s is uppercase letters only

### Hints
- Valid window: windowSize - maxFreq ≤ k
- Track character frequencies
- Don't decrease maxFreq when sliding

---

## Problem 4: Permutation in String ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Fixed-Size Window
**LeetCode:** https://leetcode.com/problems/permutation-in-string/

### Problem

Return true if s2 contains a permutation of s1.

### Examples

```
s1 = "ab", s2 = "eidbaooo" → true
s1 = "ab", s2 = "eidboaoo" → false
s1 = "adc", s2 = "dcda" → true
```

### Constraints

- 1 ≤ s1.length, s2.length ≤ 10⁴
- Lowercase English letters only

### Hints
- Fixed window of size s1.length
- Compare character frequencies
- Use array[26] for O(1) comparison

---

## Problem 5: Minimum Window Substring ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Variable-Size Window
**LeetCode:** https://leetcode.com/problems/minimum-window-substring/

### Problem

Find minimum window substring of s containing all characters in t (including duplicates).

### Examples

```
s = "ADOBECODEBANC", t = "ABC" → "BANC"
s = "a", t = "a" → "a"
s = "a", t = "aa" → ""
```

### Constraints

- 1 ≤ s.length, t.length ≤ 10⁵
- s and t are English letters (mixed case)

### Hints
- Track "have" vs "need" character counts
- Expand to include all, contract to minimize
- Use two Maps

---

## Problem 6: Maximum Sum of Distinct Subarrays

**Difficulty:** Medium | **Pattern:** Fixed-Size + Frequency
**LeetCode:** https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

### Problem

Find max sum of subarray size k with all distinct elements.

### Examples

```
nums = [1,5,4,2,9,9,9], k = 3 → 15
nums = [4,4,4], k = 3 → 0
nums = [1,2,3,4,5], k = 2 → 9
```

### Constraints

- 1 ≤ k ≤ nums.length ≤ 10⁵
- 1 ≤ nums[i] ≤ 10⁵

### Hints
- Fixed window of size k
- Valid when map.size === k
- Track sum and frequencies

---

## Problem 7: Fruit Into Baskets

**Difficulty:** Medium | **Pattern:** Variable-Size Window
**LeetCode:** https://leetcode.com/problems/fruit-into-baskets/

### Problem

Collect max fruits. Rules: 2 baskets, one fruit type per basket, pick from every tree when moving right.

### Examples

```
fruits = [1,2,1] → 3
fruits = [0,1,2,2] → 3
fruits = [1,2,3,2,2] → 4
```

### Constraints

- 1 ≤ fruits.length ≤ 10⁵
- 0 ≤ fruits[i] < fruits.length

### Hints
- "Longest subarray with ≤2 distinct elements"
- Contract when map.size > 2
- Use Map for fruit counts

---

## Problem 8: Longest Substring with At Most K Distinct

**Difficulty:** Medium | **Pattern:** Variable-Size Window
**LeetCode:** https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

### Problem

Return length of longest substring with at most k distinct characters.

### Examples

```
s = "eceba", k = 2 → 3  ("ece")
s = "aa", k = 1 → 2  ("aa")
s = "abcde", k = 3 → 3
```

### Constraints

- 1 ≤ s.length ≤ 5×10⁴
- 0 ≤ k ≤ 50

### Hints
- Track character frequencies with Map
- Contract when map.size > k
- Update result before contracting

---

## Problem 9: Minimum Size Subarray Sum

**Difficulty:** Medium | **Pattern:** Variable-Size Window
**LeetCode:** https://leetcode.com/problems/minimum-size-subarray-sum/

### Problem

Return minimal length of subarray with sum ≥ target.

### Examples

```
target = 7, nums = [2,3,1,2,4,3] → 2
target = 4, nums = [1,4,4] → 1
target = 11, nums = [1,1,1,1,1,1,1,1] → 0
```

### Constraints

- 1 ≤ target ≤ 10⁹
- 1 ≤ nums.length ≤ 10⁵
- 1 ≤ nums[i] ≤ 10⁴

### Hints
- Expand to reach target
- Contract to find minimum
- All positive: greedy contraction works

---

## Problem 10: Sliding Window Maximum

**Difficulty:** Medium | **Pattern:** Fixed-Size + Deque
**LeetCode:** https://leetcode.com/problems/sliding-window-maximum/

### Problem

Return max for each window of size k.

### Examples

```
nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

nums = [1], k = 1 → [1]
```

### Constraints

- 1 ≤ nums.length ≤ 10⁵
- -10⁴ ≤ nums[i] ≤ 10⁴
- 1 ≤ k ≤ nums.length

### Hints
- Monotonic decreasing deque
- Store indices, not values
- Remove indices outside window

---

## Summary

**Total:** 10 problems (1 Easy, 9 Medium)

**Patterns:**
- Fixed-size window
- Variable-size (expand-contract)
- Frequency counting
- Monotonic deque

**Blind 75:** 4/75 complete

---

**Ready?** Say: `"Claude, give me the problem"` or `"Go"`

[Solutions](./SOLUTIONS.md) | [Hints](./HINTS.md)
