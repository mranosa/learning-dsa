# Solutions - Session 13: 1D Dynamic Programming

TypeScript solutions with complexity analysis.

---

## Problem 1: Climbing Stairs

### Approach 1: Top-Down Memoization

```typescript
function climbStairs(n: number): number {
  const memo = new Map<number, number>();

  function dp(i: number): number {
    if (i <= 2) return i;
    if (memo.has(i)) return memo.get(i)!;

    const ways = dp(i - 1) + dp(i - 2);
    memo.set(i, ways);
    return ways;
  }

  return dp(n);
}
```

**Time:** O(n) | **Space:** O(n) memo + stack

**Key:** Recursive with cache - only computes needed states.

---

### Approach 2: Bottom-Up Tabulation

```typescript
function climbStairs(n: number): number {
  if (n <= 2) return n;

  const dp = new Array(n + 1);
  dp[1] = 1;
  dp[2] = 2;

  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
}
```

**Time:** O(n) | **Space:** O(n) DP array

**Key:** Build up from base cases - iterative approach.

---

### Approach 3: Space Optimized (Optimal) ✅

```typescript
function climbStairs(n: number): number {
  if (n <= 2) return n;

  let prev2 = 1;
  let prev1 = 2;

  for (let i = 3; i <= n; i++) {
    const curr = prev1 + prev2;
    prev2 = prev1;
    prev1 = curr;
  }

  return prev1;
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** Only need two previous values - rolling variables.

**Say:** "Classic Fibonacci pattern. Start with tabulation O(n) space, then optimize to O(1) using rolling variables since we only need two previous states."

---

## Problem 2: House Robber

### Approach 1: Top-Down Memoization

```typescript
function rob(nums: number[]): number {
  const n = nums.length;
  const memo = new Map<number, number>();

  function dp(i: number): number {
    if (i >= n) return 0;
    if (memo.has(i)) return memo.get(i)!;

    // Rob current OR skip
    const robCurrent = nums[i] + dp(i + 2);
    const skipCurrent = dp(i + 1);

    const maxMoney = Math.max(robCurrent, skipCurrent);
    memo.set(i, maxMoney);
    return maxMoney;
  }

  return dp(0);
}
```

**Time:** O(n) | **Space:** O(n) memo + stack

---

### Approach 2: Bottom-Up Tabulation

```typescript
function rob(nums: number[]): number {
  const n = nums.length;
  if (n === 0) return 0;
  if (n === 1) return nums[0];

  const dp = new Array(n);
  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);

  for (let i = 2; i < n; i++) {
    dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
  }

  return dp[n - 1];
}
```

**Time:** O(n) | **Space:** O(n) DP array

---

### Approach 3: Space Optimized (Optimal) ✅

```typescript
function rob(nums: number[]): number {
  let prev2 = 0;
  let prev1 = 0;

  for (const num of nums) {
    const curr = Math.max(prev1, prev2 + num);
    prev2 = prev1;
    prev1 = curr;
  }

  return prev1;
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** At each house, choose max of (rob it + prev2) OR (skip it, take prev1).

**Say:** "Decision making pattern - at each step, max of including or excluding current element. Only need two previous states for O(1) space."

---

## Problem 3: House Robber II

### Solution: Two Pass (Optimal) ✅

```typescript
function rob(nums: number[]): number {
  const n = nums.length;
  if (n === 0) return 0;
  if (n === 1) return nums[0];
  if (n === 2) return Math.max(nums[0], nums[1]);

  function robLinear(start: number, end: number): number {
    let prev2 = 0;
    let prev1 = 0;

    for (let i = start; i <= end; i++) {
      const curr = Math.max(prev1, prev2 + nums[i]);
      prev2 = prev1;
      prev1 = curr;
    }

    return prev1;
  }

  // Can't rob both first and last
  return Math.max(
    robLinear(0, n - 2),  // Include first, exclude last
    robLinear(1, n - 1)   // Exclude first, include last
  );
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** Circular constraint - can't rob both ends. Run House Robber twice: once excluding last, once excluding first.

**Say:** "Circular arrangement means first and last are adjacent. Break into two linear subproblems: rob houses 0 to n-2, or rob houses 1 to n-1. Take maximum."

---

## Problem 4: Coin Change

### Approach 1: Top-Down Memoization

```typescript
function coinChange(coins: number[], amount: number): number {
  const memo = new Map<number, number>();

  function dp(remaining: number): number {
    if (remaining === 0) return 0;
    if (remaining < 0) return -1;
    if (memo.has(remaining)) return memo.get(remaining)!;

    let minCoins = Infinity;

    for (const coin of coins) {
      const result = dp(remaining - coin);
      if (result !== -1) {
        minCoins = Math.min(minCoins, result + 1);
      }
    }

    const answer = minCoins === Infinity ? -1 : minCoins;
    memo.set(remaining, answer);
    return answer;
  }

  return dp(amount);
}
```

**Time:** O(amount × coins) | **Space:** O(amount) memo + stack

---

### Approach 2: Bottom-Up Tabulation (Optimal) ✅

```typescript
function coinChange(coins: number[], amount: number): number {
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
}
```

**Time:** O(amount × coins) | **Space:** O(amount)

**Key:** For each amount, try each coin and take minimum. Initialize dp[0] = 0, others = Infinity.

**Say:** "Classic optimization DP. For each amount, try all coins and take minimum. dp[i] = min(dp[i-coin] + 1) across all coins. Initialize with Infinity to detect impossible cases."

---

## Problem 5: Longest Increasing Subsequence

### Approach 1: Dynamic Programming O(n²)

```typescript
function lengthOfLIS(nums: number[]): number {
  const n = nums.length;
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
}
```

**Time:** O(n²) | **Space:** O(n)

**Key:** dp[i] = LIS ending at i. Check all j < i where nums[j] < nums[i].

---

### Approach 2: Binary Search (Optimal) ✅

```typescript
function lengthOfLIS(nums: number[]): number {
  const tails: number[] = [];

  for (const num of nums) {
    let left = 0;
    let right = tails.length;

    // Binary search for insertion position
    while (left < right) {
      const mid = Math.floor((left + right) / 2);
      if (tails[mid] < num) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }

    if (left === tails.length) {
      tails.push(num);
    } else {
      tails[left] = num;
    }
  }

  return tails.length;
}
```

**Time:** O(n log n) | **Space:** O(n)

**Key:** Maintain array of smallest tail elements for each length. Binary search to find replacement position.

**Say:** "O(n²) DP solution: for each position, check all previous smaller elements. Follow-up O(n log n): maintain array of smallest tails, use binary search for insertion."

---

## Problem 6: Decode Ways

### Approach 1: Top-Down Memoization

```typescript
function numDecodings(s: string): number {
  const memo = new Map<number, number>();

  function dp(i: number): number {
    if (i === s.length) return 1;
    if (s[i] === '0') return 0;
    if (memo.has(i)) return memo.get(i)!;

    let ways = dp(i + 1); // Single digit

    // Two digits
    if (i + 1 < s.length) {
      const twoDigit = parseInt(s.substring(i, i + 2));
      if (twoDigit <= 26) {
        ways += dp(i + 2);
      }
    }

    memo.set(i, ways);
    return ways;
  }

  return dp(0);
}
```

**Time:** O(n) | **Space:** O(n) memo + stack

---

### Approach 2: Bottom-Up Tabulation

```typescript
function numDecodings(s: string): number {
  const n = s.length;
  if (n === 0 || s[0] === '0') return 0;

  const dp = new Array(n + 1).fill(0);
  dp[0] = 1;
  dp[1] = 1;

  for (let i = 2; i <= n; i++) {
    // Single digit
    if (s[i - 1] !== '0') {
      dp[i] += dp[i - 1];
    }

    // Two digits
    const twoDigit = parseInt(s.substring(i - 2, i));
    if (twoDigit >= 10 && twoDigit <= 26) {
      dp[i] += dp[i - 2];
    }
  }

  return dp[n];
}
```

**Time:** O(n) | **Space:** O(n)

---

### Approach 3: Space Optimized (Optimal) ✅

```typescript
function numDecodings(s: string): number {
  if (s[0] === '0') return 0;

  const n = s.length;
  let prev2 = 1, prev1 = 1;

  for (let i = 1; i < n; i++) {
    let curr = 0;

    // Single digit
    if (s[i] !== '0') {
      curr += prev1;
    }

    // Two digits
    const twoDigit = parseInt(s.substring(i - 1, i + 1));
    if (twoDigit >= 10 && twoDigit <= 26) {
      curr += prev2;
    }

    prev2 = prev1;
    prev1 = curr;
  }

  return prev1;
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** Count ways by checking valid single-digit (1-9) and two-digit (10-26) decodings. Watch for '0'!

**Say:** "Counting pattern - ways to decode position i is sum of ways using single digit (if valid 1-9) plus ways using two digits (if valid 10-26). Careful with leading zeros."

---

## Problem 7: Jump Game

### Approach 1: Dynamic Programming

```typescript
function canJump(nums: number[]): boolean {
  const n = nums.length;
  const dp = new Array(n).fill(false);
  dp[0] = true;

  for (let i = 1; i < n; i++) {
    for (let j = i - 1; j >= 0; j--) {
      if (dp[j] && j + nums[j] >= i) {
        dp[i] = true;
        break;
      }
    }
  }

  return dp[n - 1];
}
```

**Time:** O(n²) | **Space:** O(n)

---

### Approach 2: Greedy (Optimal) ✅

```typescript
function canJump(nums: number[]): boolean {
  let maxReach = 0;

  for (let i = 0; i < nums.length; i++) {
    if (i > maxReach) return false;
    maxReach = Math.max(maxReach, i + nums[i]);
    if (maxReach >= nums.length - 1) return true;
  }

  return true;
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** Track furthest reachable position. If current position > maxReach, can't reach it.

**Say:** "Greedy works here - track maximum reachable position. If we reach index where i > maxReach, we're stuck. O(n) time, O(1) space beats DP O(n²)."

---

## Problem 8: Maximum Product Subarray

### Solution: Track Min and Max (Optimal) ✅

```typescript
function maxProduct(nums: number[]): number {
  let maxSoFar = nums[0];
  let minSoFar = nums[0];
  let result = nums[0];

  for (let i = 1; i < nums.length; i++) {
    const tempMax = maxSoFar;

    maxSoFar = Math.max(
      nums[i],
      nums[i] * maxSoFar,
      nums[i] * minSoFar
    );

    minSoFar = Math.min(
      nums[i],
      nums[i] * tempMax,
      nums[i] * minSoFar
    );

    result = Math.max(result, maxSoFar);
  }

  return result;
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** Negative × negative = positive! Track both max AND min. When multiply by negative, min becomes max.

**Say:** "Track both max and min products - negative times negative gives positive, so min can become max. At each step: either start fresh with current number, or multiply by previous max/min."

---

## Problem 9: Palindromic Substrings

### Approach 1: Expand Around Centers (Optimal) ✅

```typescript
function countSubstrings(s: string): number {
  let count = 0;

  function expandAroundCenter(left: number, right: number): void {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      count++;
      left--;
      right++;
    }
  }

  for (let i = 0; i < s.length; i++) {
    expandAroundCenter(i, i);     // Odd length palindromes
    expandAroundCenter(i, i + 1); // Even length palindromes
  }

  return count;
}
```

**Time:** O(n²) | **Space:** O(1)

**Key:** Expand from each center. Check both odd-length (i, i) and even-length (i, i+1).

---

### Approach 2: Dynamic Programming

```typescript
function countSubstrings(s: string): number {
  const n = s.length;
  const dp: boolean[][] = Array(n).fill(0).map(() => Array(n).fill(false));
  let count = 0;

  // Every single character is a palindrome
  for (let i = 0; i < n; i++) {
    dp[i][i] = true;
    count++;
  }

  // Check for two-character palindromes
  for (let i = 0; i < n - 1; i++) {
    if (s[i] === s[i + 1]) {
      dp[i][i + 1] = true;
      count++;
    }
  }

  // Check for palindromes of length 3 or more
  for (let len = 3; len <= n; len++) {
    for (let i = 0; i <= n - len; i++) {
      const j = i + len - 1;
      if (s[i] === s[j] && dp[i + 1][j - 1]) {
        dp[i][j] = true;
        count++;
      }
    }
  }

  return count;
}
```

**Time:** O(n²) | **Space:** O(n²)

**Say:** "Expand from center approach is better - O(1) space vs O(n²) DP. For each position, expand outward checking both odd and even length palindromes."

---

## Problem 10: Longest Palindromic Substring

### Approach 1: Expand Around Centers (Optimal) ✅

```typescript
function longestPalindrome(s: string): string {
  let start = 0;
  let maxLen = 0;

  function expandAroundCenter(left: number, right: number): void {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      const currentLen = right - left + 1;
      if (currentLen > maxLen) {
        start = left;
        maxLen = currentLen;
      }
      left--;
      right++;
    }
  }

  for (let i = 0; i < s.length; i++) {
    expandAroundCenter(i, i);     // Odd length
    expandAroundCenter(i, i + 1); // Even length
  }

  return s.substring(start, start + maxLen);
}
```

**Time:** O(n²) | **Space:** O(1)

**Key:** Similar to counting, but track longest. Expand from each center, update start and maxLen when longer palindrome found.

---

### Approach 2: Dynamic Programming

```typescript
function longestPalindrome(s: string): string {
  const n = s.length;
  const dp: boolean[][] = Array(n).fill(0).map(() => Array(n).fill(false));
  let start = 0;
  let maxLen = 1;

  // All single characters are palindromes
  for (let i = 0; i < n; i++) {
    dp[i][i] = true;
  }

  // Check two-character substrings
  for (let i = 0; i < n - 1; i++) {
    if (s[i] === s[i + 1]) {
      dp[i][i + 1] = true;
      start = i;
      maxLen = 2;
    }
  }

  // Check substrings of length 3 or more
  for (let len = 3; len <= n; len++) {
    for (let i = 0; i <= n - len; i++) {
      const j = i + len - 1;
      if (s[i] === s[j] && dp[i + 1][j - 1]) {
        dp[i][j] = true;
        start = i;
        maxLen = len;
      }
    }
  }

  return s.substring(start, start + maxLen);
}
```

**Time:** O(n²) | **Space:** O(n²)

**Say:** "Expand from center is optimal - O(1) space. For each position, expand both odd and even length palindromes, tracking longest found. Return substring using start and maxLen."

---

## Pattern Summary

### Linear Sequence (Problems 1)
- Fibonacci-like: dp[i] = dp[i-1] + dp[i-2]
- Optimize with rolling variables

### Decision Making (Problems 2, 3)
- Include or exclude current element
- dp[i] = max(skip, take + dp[i-k])
- Space optimize with prev variables

### Optimization (Problems 4, 5)
- Try all choices, take min/max
- Coin Change: dp[i] = min(dp[i-coin] + 1)
- LIS: check all previous smaller elements

### Counting (Problem 6)
- Sum ways from all valid previous states
- Check single and double digit decodings
- Watch for invalid cases (leading zeros)

### Reachability (Problem 7)
- Greedy often better than DP
- Track maximum reachable position
- O(n) time, O(1) space

### Track Multiple States (Problem 8)
- Keep both min and max
- Negative × negative = positive
- Update both in each iteration

### Expand from Center (Problems 9, 10)
- Check all possible centers
- Both odd (i, i) and even (i, i+1)
- O(n²) time, O(1) space

---

[Back to Problems](./PROBLEMS.md) | [Back to README](./README.md)
