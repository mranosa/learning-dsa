# Session 13: 1D Dynamic Programming - Hints

## Problem 1: Climbing Stairs

### Hint Level 1 (Gentle)
Think about the last step you take to reach the top. You can either take 1 step from position n-1, or 2 steps from position n-2. What does this tell you about the total number of ways?

### Hint Level 2 (Direct)
If you know the number of ways to reach step i-1 and step i-2, you can calculate the ways to reach step i. This forms a recurrence relation: ways(i) = ways(i-1) + ways(i-2).

### Hint Level 3 (Detailed)
```
Base cases: ways(1) = 1, ways(2) = 2
For i from 3 to n:
    ways(i) = ways(i-1) + ways(i-2)

This is the Fibonacci sequence! You can solve it with:
- Recursion + memoization
- Bottom-up DP array
- Space optimization with two variables
```

---

## Problem 2: House Robber

### Hint Level 1 (Gentle)
At each house, you have two choices: rob it or skip it. If you rob house i, you can't rob house i-1, but you can add the money from house i to whatever you had from house i-2.

### Hint Level 2 (Direct)
Define dp[i] as the maximum money you can rob from houses 0 to i. For each house, compare: taking current house + dp[i-2] vs skipping current house (dp[i-1]).

### Hint Level 3 (Detailed)
```
dp[i] = max amount robbing houses 0 to i
dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])

For i from 2 to n-1:
    dp[i] = max(dp[i-1], dp[i-2] + nums[i])

You only need the last two values, so optimize to O(1) space.
```

---

## Problem 3: House Robber II

### Hint Level 1 (Gentle)
Since houses form a circle, you can't rob both the first and last house. This means you need to consider two scenarios separately.

### Hint Level 2 (Direct)
Break the problem into two linear House Robber problems:
1. Rob houses 0 to n-2 (exclude last)
2. Rob houses 1 to n-1 (exclude first)
Take the maximum of these two results.

### Hint Level 3 (Detailed)
```
def robCircular(nums):
    if len <= 2: handle edge cases

    def robLinear(start, end):
        # Standard house robber from start to end

    return max(
        robLinear(0, n-2),  # Include first, exclude last
        robLinear(1, n-1)   # Exclude first, include last
    )
```

---

## Problem 4: Coin Change

### Hint Level 1 (Gentle)
Build up the solution for larger amounts using solutions for smaller amounts. If you can make amount X with Y coins, then you can make amount X+coin with Y+1 coins.

### Hint Level 2 (Direct)
Define dp[i] as the minimum coins needed for amount i. For each amount, try using each coin and take the minimum: dp[i] = min(dp[i-coin] + 1) for all valid coins.

### Hint Level 3 (Detailed)
```
dp[0] = 0 (need 0 coins for amount 0)
dp[i] = Infinity initially

For amount from 1 to target:
    For each coin:
        if coin <= amount:
            dp[amount] = min(dp[amount], dp[amount-coin] + 1)

Return dp[target] if < Infinity, else -1
```

---

## Problem 5: Longest Increasing Subsequence

### Hint Level 1 (Gentle)
For each element, consider all previous elements that are smaller. The LIS ending at current element is 1 plus the maximum LIS ending at any of those smaller elements.

### Hint Level 2 (Direct)
Define dp[i] as the length of LIS ending at index i. For each i, check all j < i where nums[j] < nums[i], and update dp[i] = max(dp[i], dp[j] + 1).

### Hint Level 3 (Detailed)
```
O(n²) approach:
dp[i] = LIS length ending at i
Initialize all dp[i] = 1

For i from 1 to n-1:
    For j from 0 to i-1:
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

For O(n log n), maintain array of smallest tail elements.
```

---

## Problem 6: Decode Ways

### Hint Level 1 (Gentle)
At each position, you can decode either one digit (if valid) or two digits (if valid). The total ways is the sum of ways from both choices.

### Hint Level 2 (Direct)
Check if current digit forms valid single-digit code (1-9) and if current + previous form valid two-digit code (10-26). Add the corresponding previous dp values.

### Hint Level 3 (Detailed)
```
dp[i] = ways to decode s[0...i-1]
dp[0] = 1 (empty string)
dp[1] = 1 if s[0] != '0'

For i from 2 to n:
    oneDigit = s[i-1]
    if oneDigit is '1'-'9': dp[i] += dp[i-1]

    twoDigit = s[i-2:i]
    if twoDigit is '10'-'26': dp[i] += dp[i-2]
```

---

## Problem 7: Jump Game

### Hint Level 1 (Gentle)
Keep track of the furthest position you can reach. As you iterate through the array, update this maximum reach and check if you can reach the current position.

### Hint Level 2 (Direct)
Greedy approach: Track maxReach. At each position i, if i > maxReach, you can't reach this position. Otherwise, update maxReach = max(maxReach, i + nums[i]).

### Hint Level 3 (Detailed)
```
Greedy O(n):
maxReach = 0
For i from 0 to n-1:
    if i > maxReach: return false
    maxReach = max(maxReach, i + nums[i])
    if maxReach >= n-1: return true

DP O(n²):
dp[i] = can reach position i
dp[0] = true
For each i, check if any j < i can reach i
```

---

## Problem 8: Maximum Product Subarray

### Hint Level 1 (Gentle)
Negative numbers can become positive when multiplied by another negative. Keep track of both the maximum and minimum product ending at each position.

### Hint Level 2 (Direct)
At each position, the max product is either: the current number alone, current * previous max, or current * previous min (if current is negative).

### Hint Level 3 (Detailed)
```
maxSoFar = nums[0]
minSoFar = nums[0]
result = nums[0]

For i from 1 to n-1:
    temp = maxSoFar
    maxSoFar = max(nums[i], nums[i]*maxSoFar, nums[i]*minSoFar)
    minSoFar = min(nums[i], nums[i]*temp, nums[i]*minSoFar)
    result = max(result, maxSoFar)
```

---

## Problem 9: Palindromic Substrings

### Hint Level 1 (Gentle)
Every palindrome has a center. The center can be a single character (odd length) or between two characters (even length). Try expanding from each possible center.

### Hint Level 2 (Direct)
For each position i, expand around two centers: (i, i) for odd-length palindromes and (i, i+1) for even-length palindromes. Count valid palindromes during expansion.

### Hint Level 3 (Detailed)
```
Expand approach:
count = 0
For each i:
    // Odd length
    left = right = i
    while s[left] == s[right]: count++, expand

    // Even length
    left = i, right = i+1
    while s[left] == s[right]: count++, expand

DP approach:
dp[i][j] = is s[i...j] palindrome
dp[i][j] = true if s[i]==s[j] && dp[i+1][j-1]
```

---

## Problem 10: Longest Palindromic Substring

### Hint Level 1 (Gentle)
Similar to counting palindromic substrings, but track the longest one found. You can either expand from centers or use dynamic programming.

### Hint Level 2 (Direct)
Expand from each center and keep track of the start position and length of the longest palindrome found. Remember to check both odd and even length palindromes.

### Hint Level 3 (Detailed)
```
Expand approach:
start = 0, maxLen = 0

For each center i:
    // Check odd length
    expand(i, i)
    // Check even length
    expand(i, i+1)

function expand(left, right):
    while s[left] == s[right]:
        if right-left+1 > maxLen:
            update start and maxLen
        expand outward

Return s[start:start+maxLen]
```

---

## General DP Tips

1. **Start with brute force** - Understand the problem first
2. **Identify state** - What parameters define a subproblem?
3. **Write recurrence** - How to compute from subproblems?
4. **Handle base cases** - What are the smallest subproblems?
5. **Optimize space** - Can you use rolling variables?

Remember: If stuck, try working through a small example by hand!