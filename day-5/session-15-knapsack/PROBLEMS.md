# Problems - Session 15: Knapsack Dynamic Programming

Complete these 10 problems in order. Use the UMPIRE method for each.

**Target Times:** All Medium <30 min each

---

## Problem 1: Partition Equal Subset Sum

**Difficulty:** Medium | **Pattern:** 0/1 Knapsack, Subset Sum
**LeetCode:** https://leetcode.com/problems/partition-equal-subset-sum/

### Problem

Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal.

### Examples

```
nums = [1,5,11,5]
Output: true
Explanation: [1, 5, 5] and [11]

nums = [1,2,3,5]
Output: false
```

### Constraints

- 1 ≤ nums.length ≤ 200
- 1 ≤ nums[i] ≤ 100

### Hints
- Total sum must be even
- Find subset with sum = total/2
- Classic 0/1 knapsack (use each element once)

---

## Problem 2: Target Sum

**Difficulty:** Medium | **Pattern:** 0/1 Knapsack with transformation
**LeetCode:** https://leetcode.com/problems/target-sum/

### Problem

You are given an integer array `nums` and an integer `target`. You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

Return the number of different expressions that evaluate to `target`.

### Examples

```
nums = [1,1,1,1,1], target = 3
Output: 5
Explanation:
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

nums = [1], target = 1
Output: 1
```

### Constraints

- 1 ≤ nums.length ≤ 20
- 0 ≤ nums[i] ≤ 1000
- -1000 ≤ target ≤ 1000

### Hints
- Transform: P - N = target, P + N = sum → P = (sum + target) / 2
- Count subsets with sum = P

---

## Problem 3: Last Stone Weight II

**Difficulty:** Medium | **Pattern:** Partition problem, 0/1 Knapsack
**LeetCode:** https://leetcode.com/problems/last-stone-weight-ii/

### Problem

You are given an array of integers `stones` where `stones[i]` is the weight of the ith stone. We smash two stones together. If x ≤ y: if x == y, both destroyed; if x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

Return the smallest possible weight of the left stone.

### Examples

```
stones = [2,7,4,1,8,1]
Output: 1

stones = [31,26,33,21,40]
Output: 5
```

### Constraints

- 1 ≤ stones.length ≤ 30
- 1 ≤ stones[i] ≤ 100

### Hints
- Minimize difference between two partitions
- Find subset closest to sum/2
- Result = total_sum - 2 × subset_sum

---

## Problem 4: Ones and Zeroes

**Difficulty:** Medium | **Pattern:** 2D Knapsack
**LeetCode:** https://leetcode.com/problems/ones-and-zeroes/

### Problem

You are given an array of binary strings `strs` and two integers `m` and `n`. Return the size of the largest subset of `strs` such that there are at most `m` 0's and `n` 1's in the subset.

### Examples

```
strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: ["10", "0001", "1", "0"]

strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: ["0", "1"]
```

### Constraints

- 1 ≤ strs.length ≤ 600
- 1 ≤ strs[i].length ≤ 100
- 1 ≤ m, n ≤ 100

### Hints
- 2D knapsack with two constraints
- dp[i][j] = max strings with i zeros and j ones
- Iterate backwards for both dimensions

---

## Problem 5: Coin Change 2

**Difficulty:** Medium | **Pattern:** Unbounded Knapsack
**LeetCode:** https://leetcode.com/problems/coin-change-2/

### Problem

You are given an integer array `coins` and an integer `amount`. Return the number of combinations that make up that amount. Assume infinite coins of each kind.

### Examples

```
amount = 5, coins = [1,2,5]
Output: 4
Explanation: 5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1

amount = 3, coins = [2]
Output: 0
```

### Constraints

- 1 ≤ coins.length ≤ 300
- 1 ≤ coins[i] ≤ 5000
- 0 ≤ amount ≤ 5000

### Hints
- Unbounded knapsack (coins reusable)
- Count combinations, not permutations
- Outer loop: coins, inner loop: amounts

---

## Problem 6: Combination Sum IV

**Difficulty:** Medium | **Pattern:** Unbounded Knapsack (Permutations)
**LeetCode:** https://leetcode.com/problems/combination-sum-iv/

### Problem

Given an array of distinct integers `nums` and a target integer `target`, return the number of possible combinations that add up to `target`. Different sequences are counted as different combinations.

### Examples

```
nums = [1,2,3], target = 4
Output: 7
Explanation: (1,1,1,1), (1,1,2), (1,2,1), (1,3), (2,1,1), (2,2), (3,1)

nums = [9], target = 3
Output: 0
```

### Constraints

- 1 ≤ nums.length ≤ 200
- 1 ≤ nums[i] ≤ 1000
- 1 ≤ target ≤ 1000

### Hints
- Count permutations, not combinations
- Outer loop: targets, inner loop: nums
- Order matters here!

---

## Problem 7: Word Break

**Difficulty:** Medium | **Pattern:** DP with String
**LeetCode:** https://leetcode.com/problems/word-break/

### Problem

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of dictionary words. Same word can be reused.

### Examples

```
s = "leetcode", wordDict = ["leet","code"]
Output: true

s = "applepenapple", wordDict = ["apple","pen"]
Output: true

s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

### Constraints

- 1 ≤ s.length ≤ 300
- 1 ≤ wordDict.length ≤ 1000
- All strings in wordDict are unique

### Hints
- dp[i] = can we break s[0:i]?
- Check all possible word endings at position i
- Use Set for O(1) word lookups

---

## Problem 8: Partition to K Equal Sum Subsets

**Difficulty:** Medium | **Pattern:** Backtracking + DP with Bitmask
**LeetCode:** https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

### Problem

Given an integer array `nums` and an integer `k`, return `true` if it is possible to divide this array into `k` non-empty subsets whose sums are all equal.

### Examples

```
nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: [5], [1,4], [2,3], [2,3]

nums = [1,2,3,4], k = 3
Output: false
```

### Constraints

- 1 ≤ k ≤ nums.length ≤ 16
- 1 ≤ nums[i] ≤ 10^4

### Hints
- Total sum must be divisible by k
- Use bitmask to track used elements
- Backtrack with memoization

---

## Problem 9: Shopping Offers

**Difficulty:** Medium | **Pattern:** Multi-dimensional Knapsack
**LeetCode:** https://leetcode.com/problems/shopping-offers/

### Problem

In LeetCode Store, there are `n` items to sell. Each item has a price. However, there are some special offers. Return the lowest price you have to pay for exactly certain items as given.

### Examples

```
price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
Output: 14
Explanation: Buy offer 2 (1A + 2B for $10) and 2A separately ($4)
```

### Constraints

- n == price.length == needs.length
- 1 ≤ n ≤ 6
- 0 ≤ price[i], needs[i] ≤ 10

### Hints
- Try all combinations of special offers
- Use memoization with needs as key
- Prune invalid offers early

---

## Problem 10: Minimum Cost For Tickets

**Difficulty:** Medium | **Pattern:** DP with choices
**LeetCode:** https://leetcode.com/problems/minimum-cost-for-tickets/

### Problem

You have planned some train traveling one year in advance. The days are given as an integer array `days`. Train tickets are sold in 1-day, 7-day, and 30-day passes. Return the minimum number of dollars you need to travel.

### Examples

```
days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11

days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
```

### Constraints

- 1 ≤ days.length ≤ 365
- 1 ≤ days[i] ≤ 365
- days is in strictly increasing order
- costs.length == 3

### Hints
- dp[i] = min cost to cover all days up to i
- For each day, try all three pass options
- Use set for O(1) travel day lookups

---

## Summary

**Total:** 10 problems (All Medium)

**Patterns:**
- 0/1 Knapsack
- Unbounded Knapsack
- Subset Sum
- Multi-dimensional DP
- Combinations vs Permutations

---

**Ready?** Say: `"Claude, give me the problem"` or `"Go"`

[Solutions](./SOLUTIONS.md) | [Hints](./HINTS.md)
