# Problems - Session 13: 1D Dynamic Programming

10 problems in order. Use UMPIRE method.

**Targets:** Easy <20 min | Medium <30 min

---

## Problem 1: Climbing Stairs ⭐ BLIND 75

**Difficulty:** Easy | **Pattern:** Linear Sequence DP
**LeetCode:** https://leetcode.com/problems/climbing-stairs/

### Problem

You are climbing a staircase with `n` steps. Each time you can climb 1 or 2 steps. In how many distinct ways can you climb to the top?

### Examples

```
Input: n = 2
Output: 2
Explanation:
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation:
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Input: n = 5
Output: 8
```

### Constraints

- 1 ≤ n ≤ 45

### Hints
- Think about the last step: came from n-1 or n-2
- Recurrence: ways(n) = ways(n-1) + ways(n-2)
- This is Fibonacci!
- Can optimize to O(1) space

---

## Problem 2: House Robber ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Decision Making DP
**LeetCode:** https://leetcode.com/problems/house-robber/

### Problem

You're a robber planning to rob houses. Each house has money, but adjacent houses have connected security systems. Return max money without alerting police.

### Examples

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (1) + house 3 (3) = 4

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (2) + house 3 (9) + house 5 (1) = 12

Input: nums = [5,3,4,11,2]
Output: 16
```

### Constraints

- 1 ≤ nums.length ≤ 100
- 0 ≤ nums[i] ≤ 400

### Hints
- At each house: rob it OR skip it
- If rob house i: add nums[i] + max from i-2
- If skip: take max from i-1
- dp[i] = max(dp[i-1], dp[i-2] + nums[i])

---

## Problem 3: House Robber II ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Decision Making + Circular
**LeetCode:** https://leetcode.com/problems/house-robber-ii/

### Problem

Same as House Robber, but houses are arranged in a circle (first and last are adjacent). Return max money without alerting police.

### Examples

```
Input: nums = [2,3,2]
Output: 3
Explanation: Can't rob house 1 and 3 (adjacent in circle)

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (1) + house 3 (3) = 4

Input: nums = [1,2,3]
Output: 3
```

### Constraints

- 1 ≤ nums.length ≤ 100
- 0 ≤ nums[i] ≤ 1000

### Hints
- Can't rob both first and last house
- Two scenarios: rob houses 0..n-2 OR 1..n-1
- Use House Robber solution twice
- Take max of both scenarios

---

## Problem 4: Coin Change ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Optimization DP
**LeetCode:** https://leetcode.com/problems/coin-change/

### Problem

Given `coins` array and `amount`, return fewest coins to make up amount. If impossible, return -1. Infinite supply of each coin.

### Examples

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0

Input: coins = [1,2,5], amount = 100
Output: 20
Explanation: 100 = 5×20
```

### Constraints

- 1 ≤ coins.length ≤ 12
- 1 ≤ coins[i] ≤ 2³¹ - 1
- 0 ≤ amount ≤ 10⁴

### Hints
- dp[i] = min coins to make amount i
- Try each coin: dp[i] = min(dp[i-coin] + 1)
- Initialize dp[0] = 0, others = Infinity
- O(amount × coins) time

---

## Problem 5: Longest Increasing Subsequence ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Subsequence DP
**LeetCode:** https://leetcode.com/problems/longest-increasing-subsequence/

### Problem

Given integer array `nums`, return length of longest strictly increasing subsequence.

### Examples

```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: [2,3,7,101] (length 4)

Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: [0,1,2,3]

Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

### Constraints

- 1 ≤ nums.length ≤ 2500
- -10⁴ ≤ nums[i] ≤ 10⁴

### Follow-up
Can you solve in O(n log n)?

### Hints
- dp[i] = LIS length ending at index i
- For each i, check all j < i where nums[j] < nums[i]
- dp[i] = max(dp[i], dp[j] + 1)
- O(n²) time, or O(n log n) with binary search

---

## Problem 6: Decode Ways ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Counting DP
**LeetCode:** https://leetcode.com/problems/decode-ways/

### Problem

A-Z encoded as "1"-"26". Given digits string `s`, return number of ways to decode it.

### Examples

```
Input: s = "12"
Output: 2
Explanation: "AB" (1,2) or "L" (12)

Input: s = "226"
Output: 3
Explanation: "BZ" (2,26), "VF" (22,6), or "BBF" (2,2,6)

Input: s = "06"
Output: 0
Explanation: "06" invalid (leading zero)

Input: s = "11106"
Output: 2
```

### Constraints

- 1 ≤ s.length ≤ 100
- s contains only digits, may have leading zeros

### Hints
- dp[i] = ways to decode s[0..i-1]
- Check single digit (1-9) and double digit (10-26)
- If s[i] valid: add dp[i-1]
- If s[i-1:i+1] valid: add dp[i-2]
- Watch out for '0'!

---

## Problem 7: Jump Game ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Reachability
**LeetCode:** https://leetcode.com/problems/jump-game/

### Problem

Array `nums` where each element = max jump length. Start at index 0. Return true if can reach last index.

### Examples

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step (index 0→1), then 3 steps (1→4)

Input: nums = [3,2,1,0,4]
Output: false
Explanation: Always arrive at index 3 (max jump = 0)

Input: nums = [0]
Output: true
Explanation: Already at last index
```

### Constraints

- 1 ≤ nums.length ≤ 10⁴
- 0 ≤ nums[i] ≤ 10⁵

### Hints
- Track furthest reachable position
- Greedy: maxReach = max(maxReach, i + nums[i])
- If i > maxReach, can't reach position i
- O(n) time, O(1) space (greedy better than DP here)

---

## Problem 8: Maximum Product Subarray ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Track Min/Max
**LeetCode:** https://leetcode.com/problems/maximum-product-subarray/

### Problem

Find contiguous subarray with largest product. Return the product.

### Examples

```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has product 6

Input: nums = [-2,0,-1]
Output: 0

Input: nums = [-2,3,-4]
Output: 24
Explanation: [-2,3,-4] = 24
```

### Constraints

- 1 ≤ nums.length ≤ 2×10⁴
- -10 ≤ nums[i] ≤ 10
- Product fits in 32-bit integer

### Hints
- Negative × negative = positive!
- Track both maxProduct and minProduct
- When multiply by negative, swap max/min
- maxProd = max(num, num×maxProd, num×minProd)
- O(n) time, O(1) space

---

## Problem 9: Palindromic Substrings ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Expand from Center
**LeetCode:** https://leetcode.com/problems/palindromic-substrings/

### Problem

Return number of palindromic substrings in string `s`.

### Examples

```
Input: s = "abc"
Output: 3
Explanation: "a", "b", "c"

Input: s = "aaa"
Output: 6
Explanation: "a", "a", "a", "aa", "aa", "aaa"

Input: s = "racecar"
Output: 10
```

### Constraints

- 1 ≤ s.length ≤ 1000
- s consists of lowercase English letters

### Hints
- Every palindrome has a center
- Expand from each center: (i, i) and (i, i+1)
- Count palindromes while expanding
- O(n²) time, O(1) space
- Alternative: DP with O(n²) space

---

## Problem 10: Longest Palindromic Substring ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Expand from Center
**LeetCode:** https://leetcode.com/problems/longest-palindromic-substring/

### Problem

Return the longest palindromic substring in `s`.

### Examples

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" also valid

Input: s = "cbbd"
Output: "bb"

Input: s = "racecar"
Output: "racecar"
```

### Constraints

- 1 ≤ s.length ≤ 1000
- s consist of digits and English letters

### Hints
- Similar to counting palindromes
- Expand from each center
- Track start and maxLength
- Check both odd (i, i) and even (i, i+1) centers
- O(n²) time, O(1) space

---

## Summary

**Total:** 10 problems (1 Easy, 9 Medium)

**Patterns:**
- Linear Sequence (Fibonacci-like)
- Decision Making (Include/Exclude)
- Optimization (Min/Max)
- Counting Ways
- Reachability
- Tracking Multiple States
- Expand from Center

**Blind 75:** 10/75 complete (13%)

---

## Problem-Solving Tips

### DP Problem Recognition
- Keywords: "maximum", "minimum", "count ways", "longest"
- Look for overlapping subproblems
- Check if greedy doesn't work

### State Definition
- What parameters uniquely define subproblem?
- What does dp[i] represent?

### Recurrence Relation
- How to compute current state from previous?
- What choices do you have at each step?

### Implementation Order
1. Define state clearly
2. Write recurrence relation
3. Identify base cases
4. Code bottom-up or top-down
5. Test with examples
6. Optimize space if needed

---

**Ready?** Say: `"Claude, give me the problem"` or `"Go"`

[Solutions](./SOLUTIONS.md) | [Hints](./HINTS.md)
