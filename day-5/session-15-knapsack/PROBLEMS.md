# Problems - Session 15: Knapsack Dynamic Programming

Complete these 10 problems in order. Use the UMPIRE method for each.

**Target Times:**
- All Medium: <30 min each
- Focus on pattern recognition and state design

---

## Problem 1: Partition Equal Subset Sum

**Difficulty:** Medium
**Time Target:** 25-30 min
**Pattern:** 0/1 Knapsack, Subset Sum
**LeetCode:** https://leetcode.com/problems/partition-equal-subset-sum/

### Problem Statement

Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or `false` otherwise.

### Examples

```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

### Constraints

- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100

### Hints
- Total sum must be even for equal partition
- Find subset with sum = total/2
- Classic 0/1 knapsack pattern

---

## Problem 2: Target Sum

**Difficulty:** Medium
**Time Target:** 30 min
**Pattern:** 0/1 Knapsack with transformation
**LeetCode:** https://leetcode.com/problems/target-sum/

### Problem Statement

You are given an integer array `nums` and an integer `target`.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

Return the number of different expressions that you can build, which evaluates to `target`.

### Examples

```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3:
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
```

```
Input: nums = [1], target = 1
Output: 1
```

### Constraints

- 1 <= nums.length <= 20
- 0 <= nums[i] <= 1000
- 0 <= sum(nums[i]) <= 1000
- -1000 <= target <= 1000

### Hints
- Transform to subset sum problem
- P - N = target, P + N = sum → P = (sum + target) / 2
- Count subsets with sum = P

---

## Problem 3: Last Stone Weight II

**Difficulty:** Medium
**Time Target:** 30 min
**Pattern:** Partition problem, 0/1 Knapsack
**LeetCode:** https://leetcode.com/problems/last-stone-weight-ii/

### Problem Statement

You are given an array of integers `stones` where `stones[i]` is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:
- If x == y, both stones are destroyed
- If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x

At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

### Examples

```
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1]
We can combine 7 and 8 to get 1, so the array converts to [2,1,1,1]
We can combine 2 and 1 to get 1, so the array converts to [1,1,1]
We can combine 1 and 1 to get 0, so the array converts to [1], that's the optimal value.
```

```
Input: stones = [31,26,33,21,40]
Output: 5
```

### Constraints

- 1 <= stones.length <= 30
- 1 <= stones[i] <= 100

### Hints
- Minimize difference between two partitions
- Find subset closest to sum/2
- Result = total_sum - 2 * subset_sum

---

## Problem 4: Ones and Zeroes

**Difficulty:** Medium
**Time Target:** 30 min
**Pattern:** 2D Knapsack
**LeetCode:** https://leetcode.com/problems/ones-and-zeroes/

### Problem Statement

You are given an array of binary strings `strs` and two integers `m` and `n`.

Return the size of the largest subset of `strs` such that there are at most `m` 0's and `n` 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

### Examples

```
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is ["10", "0001", "1", "0"], so the answer is 4.
```

```
Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is ["0", "1"], so the answer is 2.
```

### Constraints

- 1 <= strs.length <= 600
- 1 <= strs[i].length <= 100
- strs[i] consists only of digits '0' and '1'
- 1 <= m, n <= 100

### Hints
- 2D knapsack with two constraints
- dp[i][j] = max strings with i zeros and j ones
- Iterate backwards for both dimensions

---

## Problem 5: Coin Change 2

**Difficulty:** Medium
**Time Target:** 25 min
**Pattern:** Unbounded Knapsack
**LeetCode:** https://leetcode.com/problems/coin-change-2/

### Problem Statement

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

### Examples

```
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: There are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

```
Input: amount = 3, coins = [2]
Output: 0
Explanation: The amount of 3 cannot be made up just with coins of 2.
```

### Constraints

- 1 <= coins.length <= 300
- 1 <= coins[i] <= 5000
- All values in coins are unique
- 0 <= amount <= 5000

### Hints
- Unbounded knapsack (coins reusable)
- Count combinations, not permutations
- Outer loop: coins, inner loop: amounts

---

## Problem 6: Combination Sum IV

**Difficulty:** Medium
**Time Target:** 25 min
**Pattern:** Unbounded Knapsack (Permutations)
**LeetCode:** https://leetcode.com/problems/combination-sum-iv/

### Problem Statement

Given an array of distinct integers `nums` and a target integer `target`, return the number of possible combinations that add up to `target`.

The test cases are generated so that the answer can fit in a 32-bit integer.

### Examples

```
Input: nums = [1,2,3], target = 4
Output: 7
Explanation: The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
```

```
Input: nums = [9], target = 3
Output: 0
```

### Constraints

- 1 <= nums.length <= 200
- 1 <= nums[i] <= 1000
- All elements of nums are unique
- 1 <= target <= 1000

### Hints
- Count permutations, not combinations
- Outer loop: targets, inner loop: nums
- Order matters here!

---

## Problem 7: Word Break

**Difficulty:** Medium
**Time Target:** 30 min
**Pattern:** DP with String
**LeetCode:** https://leetcode.com/problems/word-break/

### Problem Statement

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

### Examples

```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
```

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

### Constraints

- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters
- All strings in wordDict are unique

### Hints
- dp[i] = can we break s[0:i]?
- Check all possible word endings at position i
- Use Set for O(1) word lookups

---

## Problem 8: Partition to K Equal Sum Subsets

**Difficulty:** Medium
**Time Target:** 35 min
**Pattern:** Backtracking + DP with Bitmask
**LeetCode:** https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

### Problem Statement

Given an integer array `nums` and an integer `k`, return `true` if it is possible to divide this array into `k` non-empty subsets whose sums are all equal.

### Examples

```
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
```

```
Input: nums = [1,2,3,4], k = 3
Output: false
```

### Constraints

- 1 <= k <= nums.length <= 16
- 1 <= nums[i] <= 10^4
- The frequency of each element is in the range [1, 4]

### Hints
- Total sum must be divisible by k
- Use bitmask to track used elements
- Backtrack with memoization

---

## Problem 9: Shopping Offers

**Difficulty:** Medium
**Time Target:** 35 min
**Pattern:** Multi-dimensional Knapsack
**LeetCode:** https://leetcode.com/problems/shopping-offers/

### Problem Statement

In LeetCode Store, there are `n` items to sell. Each item has a price. However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

You are given an integer array `price` where `price[i]` is the price of the ith item, and an integer array `needs` where `needs[i]` is the number of pieces of the ith item you want to buy.

You are also given an array `special` where `special[i]` is of size `n + 1` where `special[i][j]` is the number of pieces of the jth item in the ith offer and `special[i][n]` (i.e., the last integer in the array) is the price of the ith offer.

Return the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers.

### Examples

```
Input: price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
Output: 14
Explanation: There are two kinds of items, A and B. Their prices are $2 and $5 respectively.
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B.
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
```

### Constraints

- n == price.length == needs.length
- 1 <= n <= 6
- 0 <= price[i], needs[i] <= 10
- 1 <= special.length <= 100
- special[i].length == n + 1
- 0 <= special[i][j] <= 50

### Hints
- Try all combinations of special offers
- Use memoization with needs as key
- Prune invalid offers early

---

## Problem 10: Minimum Cost For Tickets

**Difficulty:** Medium
**Time Target:** 30 min
**Pattern:** DP with choices
**LeetCode:** https://leetcode.com/problems/minimum-cost-for-tickets/

### Problem Statement

You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array `days`. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:
- a 1-day pass is sold for `costs[0]` dollars
- a 7-day pass is sold for `costs[1]` dollars
- a 30-day pass is sold for `costs[2]` dollars

The passes allow that many days of consecutive travel.

Return the minimum number of dollars you need to travel every day in the given list of days.

### Examples

```
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
```

```
Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.
```

### Constraints

- 1 <= days.length <= 365
- 1 <= days[i] <= 365
- days is in strictly increasing order
- costs.length == 3
- 1 <= costs[i] <= 1000

### Hints
- dp[i] = min cost to cover all days up to i
- For each day, try all three pass options
- Use set for O(1) travel day lookups