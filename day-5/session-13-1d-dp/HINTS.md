# Hints - Session 13: 1D Dynamic Programming

Progressive hints for 10 problems. Struggling is part of learning.

---

## Problem 1: Climbing Stairs

### Level 1
How many ways to reach step n? Think about the last step - you came from n-1 (took 1 step) or n-2 (took 2 steps).

### Level 2
Recurrence relation: ways(n) = ways(n-1) + ways(n-2). This is Fibonacci! Base cases: ways(1) = 1, ways(2) = 2.

### Level 3
```typescript
// Space optimized
let prev2 = 1, prev1 = 2;
for (let i = 3; i <= n; i++) {
  const curr = prev1 + prev2;
  prev2 = prev1;
  prev1 = curr;
}
return prev1;
```

---

## Problem 2: House Robber

### Level 1
At each house: rob it OR skip it. If rob house i, can't rob i-1, but can add money from i-2.

### Level 2
Define dp[i] = max money robbing houses 0..i. Recurrence: dp[i] = max(dp[i-1], dp[i-2] + nums[i]).

### Level 3
```typescript
let prev2 = 0, prev1 = 0;
for (const num of nums) {
  const curr = Math.max(prev1, prev2 + num);
  prev2 = prev1;
  prev1 = curr;
}
return prev1;
```

---

## Problem 3: House Robber II

### Level 1
Circular arrangement - first and last houses are adjacent. Can't rob both!

### Level 2
Two scenarios: (1) Rob houses 0 to n-2 (exclude last), (2) Rob houses 1 to n-1 (exclude first). Take max.

### Level 3
```typescript
function robLinear(start, end) {
  let prev2 = 0, prev1 = 0;
  for (let i = start; i <= end; i++) {
    const curr = Math.max(prev1, prev2 + nums[i]);
    prev2 = prev1;
    prev1 = curr;
  }
  return prev1;
}
return Math.max(robLinear(0, n-2), robLinear(1, n-1));
```

---

## Problem 4: Coin Change

### Level 1
Build solution for larger amounts using smaller amounts. If can make X with Y coins, can make X+coin with Y+1 coins.

### Level 2
dp[i] = min coins for amount i. For each amount, try each coin: dp[i] = min(dp[i-coin] + 1).

### Level 3
```typescript
const dp = new Array(amount + 1).fill(Infinity);
dp[0] = 0;
for (let i = 1; i <= amount; i++) {
  for (const coin of coins) {
    if (i >= coin) {
      dp[i] = Math.min(dp[i], dp[i - coin] + 1);
    }
  }
}
return dp[amount] === Infinity ? -1 : dp[amount];
```

---

## Problem 5: Longest Increasing Subsequence

### Level 1
For each element, find longest increasing subsequence ending at that position by checking all smaller previous elements.

### Level 2
dp[i] = LIS length ending at i. For each i, check all j < i where nums[j] < nums[i]: dp[i] = max(dp[i], dp[j] + 1).

### Level 3
```typescript
// O(n²) approach
const dp = new Array(n).fill(1);
let maxLength = 1;
for (let i = 1; i < n; i++) {
  for (let j = 0; j < i; j++) {
    if (nums[j] < nums[i]) {
      dp[i] = Math.max(dp[i], dp[j] + 1);
    }
  }
  maxLength = Math.max(maxLength, dp[i]);
}
return maxLength;
```

---

## Problem 6: Decode Ways

### Level 1
At each position, can decode as single digit (1-9) or two digits (10-26). Total ways is sum of both choices.

### Level 2
dp[i] = ways to decode up to i. Check if s[i] valid single digit, add dp[i-1]. Check if s[i-1:i+1] valid double digit, add dp[i-2].

### Level 3
```typescript
if (s[0] === '0') return 0;
let prev2 = 1, prev1 = 1;
for (let i = 1; i < s.length; i++) {
  let curr = 0;
  if (s[i] !== '0') curr += prev1;  // Single digit
  const twoDigit = parseInt(s.substring(i-1, i+1));
  if (twoDigit >= 10 && twoDigit <= 26) curr += prev2;  // Two digits
  prev2 = prev1;
  prev1 = curr;
}
return prev1;
```

---

## Problem 7: Jump Game

### Level 1
Track furthest position you can reach. If current position > max reach, you're stuck.

### Level 2
Greedy: maxReach = max(maxReach, i + nums[i]). If i > maxReach at any point, return false.

### Level 3
```typescript
let maxReach = 0;
for (let i = 0; i < nums.length; i++) {
  if (i > maxReach) return false;
  maxReach = Math.max(maxReach, i + nums[i]);
  if (maxReach >= nums.length - 1) return true;
}
return true;
```

---

## Problem 8: Maximum Product Subarray

### Level 1
Negative × negative = positive! Need to track both maximum AND minimum products.

### Level 2
When multiply by negative number, min becomes max and vice versa. Track both maxProd and minProd.

### Level 3
```typescript
let maxSoFar = nums[0], minSoFar = nums[0], result = nums[0];
for (let i = 1; i < nums.length; i++) {
  const tempMax = maxSoFar;
  maxSoFar = Math.max(nums[i], nums[i] * maxSoFar, nums[i] * minSoFar);
  minSoFar = Math.min(nums[i], nums[i] * tempMax, nums[i] * minSoFar);
  result = Math.max(result, maxSoFar);
}
return result;
```

---

## Problem 9: Palindromic Substrings

### Level 1
Every palindrome has a center. Expand outward from each possible center.

### Level 2
For each position i, expand from two centers: (i, i) for odd-length and (i, i+1) for even-length palindromes.

### Level 3
```typescript
let count = 0;
function expand(left, right) {
  while (left >= 0 && right < s.length && s[left] === s[right]) {
    count++;
    left--;
    right++;
  }
}
for (let i = 0; i < s.length; i++) {
  expand(i, i);      // Odd length
  expand(i, i + 1);  // Even length
}
return count;
```

---

## Problem 10: Longest Palindromic Substring

### Level 1
Similar to counting palindromes, but track the longest one found instead of counting.

### Level 2
Expand from each center, keep track of start position and maxLength when longer palindrome found.

### Level 3
```typescript
let start = 0, maxLen = 0;
function expand(left, right) {
  while (left >= 0 && right < s.length && s[left] === s[right]) {
    const len = right - left + 1;
    if (len > maxLen) {
      start = left;
      maxLen = len;
    }
    left--;
    right++;
  }
}
for (let i = 0; i < s.length; i++) {
  expand(i, i);      // Odd
  expand(i, i + 1);  // Even
}
return s.substring(start, start + maxLen);
```

---

## Pattern Recognition

**"Count ways to..."** → Counting DP, sum from valid previous states

**"Maximum/Minimum..."** → Optimization DP, try all choices

**"Can you reach..."** → Reachability, consider greedy first

**"Longest increasing..."** → Subsequence DP, check previous elements

**"Decode/partition..."** → Check valid single and multiple elements

**"Palindrome..."** → Expand from center or 2D DP

---

## Using Hints Effectively

1. Try 10+ min before Level 1
2. Try 5+ min after each hint
3. If use Level 3, mark problem for review
4. Don't feel bad - hints are for learning
5. Goal: Learn pattern, not just solve one problem

---

## DP Debugging Checklist

**Wrong Answer?**
- Check base cases carefully
- Verify recurrence relation
- Print DP table for small input
- Test edge cases (empty, single element)

**Runtime Error?**
- Check array bounds
- Initialize all values
- Handle edge cases first

**TLE?**
- Ensure memoization working
- Check for infinite loops
- Verify complexity is correct

**Space Issues?**
- Can you use rolling variables?
- Only keep necessary states
- Consider iterative vs recursive

---

[Back to Problems](./PROBLEMS.md) | [Back to Solutions](./SOLUTIONS.md)
