# Session 13: 1D Dynamic Programming - Problems

## Problem 1: Climbing Stairs [Easy]
**LeetCode:** https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Example 1:**
```
Input: n = 2
Output: 2
Explanation: Two ways to climb to the top:
1. 1 step + 1 step
2. 2 steps
```

**Example 2:**
```
Input: n = 3
Output: 3
Explanation: Three ways to climb to the top:
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

**Constraints:**
- 1 <= n <= 45

---

## Problem 2: House Robber [Medium]
**LeetCode:** https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

**Example 1:**
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total = 1 + 3 = 4
```

**Example 2:**
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total = 2 + 9 + 1 = 12
```

**Constraints:**
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

---

## Problem 3: House Robber II [Medium]
**LeetCode:** https://leetcode.com/problems/house-robber-ii/

All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

**Example 1:**
```
Input: nums = [2,3,2]
Output: 3
Explanation: Cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
```

**Example 2:**
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total = 1 + 3 = 4
```

**Example 3:**
```
Input: nums = [1,2,3]
Output: 3
```

**Constraints:**
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

---

## Problem 4: Coin Change [Medium]
**LeetCode:** https://leetcode.com/problems/coin-change/

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

**Example 1:**
```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

**Example 2:**
```
Input: coins = [2], amount = 3
Output: -1
```

**Example 3:**
```
Input: coins = [1], amount = 0
Output: 0
```

**Constraints:**
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2³¹ - 1
- 0 <= amount <= 10⁴

---

## Problem 5: Longest Increasing Subsequence [Medium]
**LeetCode:** https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

**Example 1:**
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

**Example 2:**
```
Input: nums = [0,1,0,3,2,3]
Output: 4
```

**Example 3:**
```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

**Constraints:**
- 1 <= nums.length <= 2500
- -10⁴ <= nums[i] <= 10⁴

---

## Problem 6: Decode Ways [Medium]
**LeetCode:** https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z can be encoded into numbers using the following mapping:
- 'A' -> "1"
- 'B' -> "2"
- ...
- 'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways).

Given a string `s` containing only digits, return the number of ways to decode it.

**Example 1:**
```
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```

**Example 2:**
```
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

**Example 3:**
```
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero.
```

**Constraints:**
- 1 <= s.length <= 100
- s contains only digits and may contain leading zero(s).

---

## Problem 7: Jump Game [Medium]
**LeetCode:** https://leetcode.com/problems/jump-game/

You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

**Example 1:**
```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**
```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

**Constraints:**
- 1 <= nums.length <= 10⁴
- 0 <= nums[i] <= 10⁵

---

## Problem 8: Maximum Product Subarray [Medium]
**LeetCode:** https://leetcode.com/problems/maximum-product-subarray/

Given an integer array `nums`, find a subarray that has the largest product, and return the product.

**Example 1:**
```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

**Example 2:**
```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

**Constraints:**
- 1 <= nums.length <= 2 * 10⁴
- -10 <= nums[i] <= 10
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

---

## Problem 9: Palindromic Substrings [Medium]
**LeetCode:** https://leetcode.com/problems/palindromic-substrings/

Given a string `s`, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

**Example 1:**
```
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

**Example 2:**
```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

**Constraints:**
- 1 <= s.length <= 1000
- s consists of lowercase English letters.

---

## Problem 10: Longest Palindromic Substring [Medium]
**LeetCode:** https://leetcode.com/problems/longest-palindromic-substring/

Given a string `s`, return the longest palindromic substring in `s`.

**Example 1:**
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

**Example 2:**
```
Input: s = "cbbd"
Output: "bb"
```

**Constraints:**
- 1 <= s.length <= 1000
- s consist of only digits and English letters.

---

## Problem Solving Order

**Recommended sequence:**
1. Start with **Climbing Stairs** - Classic fibonacci-like DP
2. Then **House Robber** - Decision making pattern
3. Try **House Robber II** - Circular constraint handling
4. Solve **Coin Change** - Optimization with choices
5. Attempt **Longest Increasing Subsequence** - Classic subsequence DP
6. Work on **Decode Ways** - Counting with constraints
7. Try **Jump Game** - Reachability problem
8. Solve **Maximum Product Subarray** - Track min and max
9. Attempt **Palindromic Substrings** - Expand around center
10. Finish with **Longest Palindromic Substring** - Similar but track longest

---

## Key Patterns to Practice

1. **Linear Recurrence:** Problems 1, 2, 3
2. **Optimization with Choices:** Problems 4, 5
3. **Counting Valid Ways:** Problems 1, 6
4. **Reachability/Possibility:** Problem 7
5. **Tracking Multiple States:** Problem 8
6. **String DP with Expansion:** Problems 9, 10

---

## Time Guidelines

- Easy problems: 15-20 minutes
- Medium problems: 20-30 minutes
- If stuck for >10 minutes on approach, check hints
- If stuck for >30 minutes total, review solution

Remember: Understanding the pattern is more important than solving quickly!