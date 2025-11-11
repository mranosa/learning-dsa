# Session 13: 1D Dynamic Programming - Solutions

## Problem 1: Climbing Stairs

### Approach 1: Top-Down DP (Memoization)
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
**Time:** O(n) - Each state computed once
**Space:** O(n) - Recursion stack + memo

### Approach 2: Bottom-Up DP
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
**Time:** O(n) - Single pass
**Space:** O(n) - DP array

### Approach 3: Space Optimized
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
**Time:** O(n) - Single pass
**Space:** O(1) - Only two variables

---

## Problem 2: House Robber

### Approach 1: Top-Down DP
```typescript
function rob(nums: number[]): number {
    const n = nums.length;
    const memo = new Map<number, number>();

    function dp(i: number): number {
        if (i >= n) return 0;
        if (memo.has(i)) return memo.get(i)!;

        // Choice: rob current house or skip it
        const robCurrent = nums[i] + dp(i + 2);
        const skipCurrent = dp(i + 1);

        const maxMoney = Math.max(robCurrent, skipCurrent);
        memo.set(i, maxMoney);
        return maxMoney;
    }

    return dp(0);
}
```
**Time:** O(n) - Each house visited once
**Space:** O(n) - Recursion stack + memo

### Approach 2: Bottom-Up DP
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
**Time:** O(n) - Single pass
**Space:** O(n) - DP array

### Approach 3: Space Optimized
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
**Time:** O(n) - Single pass
**Space:** O(1) - Only two variables

---

## Problem 3: House Robber II

### Solution: Two Pass Approach
```typescript
function rob(nums: number[]): number {
    const n = nums.length;
    if (n === 0) return 0;
    if (n === 1) return nums[0];
    if (n === 2) return Math.max(nums[0], nums[1]);

    // Helper function for linear robber
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

    // Either rob houses 0 to n-2, or houses 1 to n-1
    return Math.max(
        robLinear(0, n - 2),  // Include first, exclude last
        robLinear(1, n - 1)   // Exclude first, include last
    );
}
```
**Time:** O(n) - Two linear passes
**Space:** O(1) - Reusing helper function

---

## Problem 4: Coin Change

### Approach 1: Top-Down DP
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
**Time:** O(amount * coins.length) - Each subproblem solved once
**Space:** O(amount) - Recursion stack + memo

### Approach 2: Bottom-Up DP
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
**Time:** O(amount * coins.length) - Nested loops
**Space:** O(amount) - DP array

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
**Time:** O(n²) - Nested loops
**Space:** O(n) - DP array

### Approach 2: Binary Search O(n log n)
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

        tails[left] = num;
    }

    return tails.length;
}
```
**Time:** O(n log n) - Binary search for each element
**Space:** O(n) - Tails array

---

## Problem 6: Decode Ways

### Approach 1: Top-Down DP
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
**Time:** O(n) - Each position visited once
**Space:** O(n) - Recursion stack + memo

### Approach 2: Bottom-Up DP
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
**Time:** O(n) - Single pass
**Space:** O(n) - DP array

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
**Time:** O(n²) - Nested loops
**Space:** O(n) - DP array

### Approach 2: Greedy (Optimal)
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
**Time:** O(n) - Single pass
**Space:** O(1) - Only one variable

---

## Problem 8: Maximum Product Subarray

### Solution: Track Min and Max
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
**Time:** O(n) - Single pass
**Space:** O(1) - Only tracking min/max

---

## Problem 9: Palindromic Substrings

### Approach 1: Expand Around Centers
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
**Time:** O(n²) - Expand from each center
**Space:** O(1) - No extra space

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
**Time:** O(n²) - Fill DP table
**Space:** O(n²) - DP table

---

## Problem 10: Longest Palindromic Substring

### Approach 1: Expand Around Centers
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
**Time:** O(n²) - Expand from each center
**Space:** O(1) - No extra space

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
**Time:** O(n²) - Fill DP table
**Space:** O(n²) - DP table