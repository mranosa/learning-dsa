# Solutions - Session 15: Knapsack Dynamic Programming

## Problem 1: Partition Equal Subset Sum

### Approach 1: Recursive with Memoization

```typescript
function canPartition(nums: number[]): boolean {
    const sum = nums.reduce((a, b) => a + b, 0);

    // If sum is odd, we can't partition equally
    if (sum % 2 !== 0) return false;

    const target = sum / 2;
    const n = nums.length;
    const memo = new Map<string, boolean>();

    function dp(index: number, currentSum: number): boolean {
        // Base cases
        if (currentSum === target) return true;
        if (index >= n || currentSum > target) return false;

        const key = `${index},${currentSum}`;
        if (memo.has(key)) return memo.get(key)!;

        // Include current element or skip it
        const result = dp(index + 1, currentSum + nums[index]) ||
                      dp(index + 1, currentSum);

        memo.set(key, result);
        return result;
    }

    return dp(0, 0);
}

// Time: O(n × sum/2), Space: O(n × sum/2)
```

### Approach 2: Bottom-up DP (2D)

```typescript
function canPartition(nums: number[]): boolean {
    const sum = nums.reduce((a, b) => a + b, 0);

    if (sum % 2 !== 0) return false;

    const target = sum / 2;
    const n = nums.length;

    // dp[i][j] = can we make sum j using first i elements
    const dp: boolean[][] = Array(n + 1).fill(null)
        .map(() => Array(target + 1).fill(false));

    // Base case: empty subset sums to 0
    for (let i = 0; i <= n; i++) {
        dp[i][0] = true;
    }

    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= target; j++) {
            // Exclude current element
            dp[i][j] = dp[i - 1][j];

            // Include current element if possible
            if (j >= nums[i - 1]) {
                dp[i][j] = dp[i][j] || dp[i - 1][j - nums[i - 1]];
            }
        }
    }

    return dp[n][target];
}

// Time: O(n × sum/2), Space: O(n × sum/2)
```

### Approach 3: Space Optimized DP (1D)

```typescript
function canPartition(nums: number[]): boolean {
    const sum = nums.reduce((a, b) => a + b, 0);

    if (sum % 2 !== 0) return false;

    const target = sum / 2;
    const dp: boolean[] = new Array(target + 1).fill(false);
    dp[0] = true;

    for (const num of nums) {
        // Iterate backwards to avoid using updated values
        for (let j = target; j >= num; j--) {
            dp[j] = dp[j] || dp[j - num];
        }
    }

    return dp[target];
}

// Time: O(n × sum/2), Space: O(sum/2)
```

---

## Problem 2: Target Sum

### Approach 1: Transform to Subset Sum

```typescript
function findTargetSumWays(nums: number[], target: number): number {
    const sum = nums.reduce((a, b) => a + b, 0);

    // P - N = target, P + N = sum
    // 2P = target + sum → P = (target + sum) / 2

    if ((target + sum) % 2 !== 0 || sum < Math.abs(target)) {
        return 0;
    }

    const positiveSum = (target + sum) / 2;

    // Count subsets with sum = positiveSum
    const dp: number[] = new Array(positiveSum + 1).fill(0);
    dp[0] = 1; // Empty subset

    for (const num of nums) {
        for (let j = positiveSum; j >= num; j--) {
            dp[j] += dp[j - num];
        }
    }

    return dp[positiveSum];
}

// Time: O(n × sum), Space: O(sum)
```

### Approach 2: Direct DP with Offset

```typescript
function findTargetSumWays(nums: number[], target: number): number {
    const sum = nums.reduce((a, b) => a + b, 0);

    if (sum < Math.abs(target)) return 0;

    // Use offset to handle negative indices
    const offset = sum;
    const dp: number[] = new Array(2 * sum + 1).fill(0);
    dp[offset] = 1; // Start at sum = 0

    for (const num of nums) {
        const next: number[] = new Array(2 * sum + 1).fill(0);

        for (let s = -sum; s <= sum; s++) {
            if (dp[s + offset] === 0) continue;

            // Add current number
            if (s + num <= sum) {
                next[s + num + offset] += dp[s + offset];
            }

            // Subtract current number
            if (s - num >= -sum) {
                next[s - num + offset] += dp[s + offset];
            }
        }

        dp.splice(0, dp.length, ...next);
    }

    return dp[target + offset];
}

// Time: O(n × sum), Space: O(sum)
```

---

## Problem 3: Last Stone Weight II

### Approach 1: Minimize Partition Difference

```typescript
function lastStoneWeightII(stones: number[]): number {
    const sum = stones.reduce((a, b) => a + b, 0);
    const target = Math.floor(sum / 2);

    // Find the maximum sum we can achieve that's <= target
    const dp: boolean[] = new Array(target + 1).fill(false);
    dp[0] = true;

    for (const stone of stones) {
        for (let j = target; j >= stone; j--) {
            dp[j] = dp[j] || dp[j - stone];
        }
    }

    // Find the largest sum <= target that's achievable
    for (let j = target; j >= 0; j--) {
        if (dp[j]) {
            // One partition has sum j, other has sum - j
            return sum - 2 * j;
        }
    }

    return sum;
}

// Time: O(n × sum), Space: O(sum)
```

### Approach 2: DP with Actual Sums

```typescript
function lastStoneWeightII(stones: number[]): number {
    const sum = stones.reduce((a, b) => a + b, 0);

    // Track all possible sums
    let dp = new Set<number>([0]);

    for (const stone of stones) {
        const next = new Set<number>();

        for (const s of dp) {
            next.add(s + stone);
            next.add(Math.abs(s - stone));
        }

        dp = next;
    }

    return Math.min(...dp);
}

// Time: O(n × sum), Space: O(sum)
```

---

## Problem 4: Ones and Zeroes

### Approach 1: 2D Knapsack

```typescript
function findMaxForm(strs: string[], m: number, n: number): number {
    // dp[i][j] = max strings with at most i zeros and j ones
    const dp: number[][] = Array(m + 1).fill(null)
        .map(() => Array(n + 1).fill(0));

    for (const str of strs) {
        const zeros = (str.match(/0/g) || []).length;
        const ones = str.length - zeros;

        // Iterate backwards to avoid reusing same string
        for (let i = m; i >= zeros; i--) {
            for (let j = n; j >= ones; j--) {
                dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j - ones] + 1);
            }
        }
    }

    return dp[m][n];
}

// Time: O(L × m × n) where L = strs.length, Space: O(m × n)
```

### Approach 2: 3D DP (Less Optimized)

```typescript
function findMaxForm(strs: string[], m: number, n: number): number {
    const len = strs.length;

    // dp[k][i][j] = max strings from first k strings with i zeros, j ones
    const dp: number[][][] = Array(len + 1).fill(null)
        .map(() => Array(m + 1).fill(null)
            .map(() => Array(n + 1).fill(0)));

    for (let k = 1; k <= len; k++) {
        const str = strs[k - 1];
        const zeros = (str.match(/0/g) || []).length;
        const ones = str.length - zeros;

        for (let i = 0; i <= m; i++) {
            for (let j = 0; j <= n; j++) {
                // Don't take current string
                dp[k][i][j] = dp[k - 1][i][j];

                // Take current string if possible
                if (i >= zeros && j >= ones) {
                    dp[k][i][j] = Math.max(
                        dp[k][i][j],
                        dp[k - 1][i - zeros][j - ones] + 1
                    );
                }
            }
        }
    }

    return dp[len][m][n];
}

// Time: O(L × m × n), Space: O(L × m × n)
```

---

## Problem 5: Coin Change 2

### Approach 1: Unbounded Knapsack (Combinations)

```typescript
function change(amount: number, coins: number[]): number {
    const dp: number[] = new Array(amount + 1).fill(0);
    dp[0] = 1; // One way to make 0: use no coins

    // Outer loop: coins (ensures combinations, not permutations)
    for (const coin of coins) {
        // Inner loop: amounts (forward iteration for unbounded)
        for (let i = coin; i <= amount; i++) {
            dp[i] += dp[i - coin];
        }
    }

    return dp[amount];
}

// Time: O(n × amount), Space: O(amount)
```

### Approach 2: 2D DP

```typescript
function change(amount: number, coins: number[]): number {
    const n = coins.length;

    // dp[i][j] = ways to make amount j using first i coins
    const dp: number[][] = Array(n + 1).fill(null)
        .map(() => Array(amount + 1).fill(0));

    // Base case: one way to make 0
    for (let i = 0; i <= n; i++) {
        dp[i][0] = 1;
    }

    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= amount; j++) {
            // Don't use current coin
            dp[i][j] = dp[i - 1][j];

            // Use current coin (can reuse)
            if (j >= coins[i - 1]) {
                dp[i][j] += dp[i][j - coins[i - 1]];
            }
        }
    }

    return dp[n][amount];
}

// Time: O(n × amount), Space: O(n × amount)
```

---

## Problem 6: Combination Sum IV

### Approach 1: DP for Permutations

```typescript
function combinationSum4(nums: number[], target: number): number {
    const dp: number[] = new Array(target + 1).fill(0);
    dp[0] = 1; // One way to make 0: empty combination

    // Outer loop: targets (ensures permutations)
    for (let i = 1; i <= target; i++) {
        // Inner loop: nums
        for (const num of nums) {
            if (i >= num) {
                dp[i] += dp[i - num];
            }
        }
    }

    return dp[target];
}

// Time: O(target × n), Space: O(target)
```

### Approach 2: Recursive with Memoization

```typescript
function combinationSum4(nums: number[], target: number): number {
    const memo = new Map<number, number>();

    function dp(remaining: number): number {
        if (remaining === 0) return 1;
        if (remaining < 0) return 0;

        if (memo.has(remaining)) {
            return memo.get(remaining)!;
        }

        let count = 0;
        for (const num of nums) {
            count += dp(remaining - num);
        }

        memo.set(remaining, count);
        return count;
    }

    return dp(target);
}

// Time: O(target × n), Space: O(target)
```

---

## Problem 7: Word Break

### Approach 1: DP with Set

```typescript
function wordBreak(s: string, wordDict: string[]): boolean {
    const n = s.length;
    const wordSet = new Set(wordDict);

    // dp[i] = can we break s[0:i]?
    const dp: boolean[] = new Array(n + 1).fill(false);
    dp[0] = true; // Empty string

    for (let i = 1; i <= n; i++) {
        for (let j = 0; j < i; j++) {
            if (dp[j] && wordSet.has(s.substring(j, i))) {
                dp[i] = true;
                break;
            }
        }
    }

    return dp[n];
}

// Time: O(n² × m) where m = avg word length, Space: O(n)
```

### Approach 2: BFS

```typescript
function wordBreak(s: string, wordDict: string[]): boolean {
    const wordSet = new Set(wordDict);
    const visited = new Set<number>();
    const queue: number[] = [0];

    while (queue.length > 0) {
        const start = queue.shift()!;

        if (start === s.length) return true;

        if (visited.has(start)) continue;
        visited.add(start);

        for (let end = start + 1; end <= s.length; end++) {
            if (wordSet.has(s.substring(start, end))) {
                queue.push(end);
            }
        }
    }

    return false;
}

// Time: O(n³), Space: O(n)
```

---

## Problem 8: Partition to K Equal Sum Subsets

### Approach 1: Backtracking with Bitmask

```typescript
function canPartitionKSubsets(nums: number[], k: number): boolean {
    const sum = nums.reduce((a, b) => a + b, 0);

    if (sum % k !== 0) return false;

    const target = sum / k;
    const n = nums.length;
    const memo = new Map<number, boolean>();

    // Sort descending for pruning
    nums.sort((a, b) => b - a);

    if (nums[0] > target) return false;

    function dp(mask: number, currentSum: number): boolean {
        if (mask === (1 << n) - 1) return true;

        if (memo.has(mask)) return memo.get(mask)!;

        for (let i = 0; i < n; i++) {
            if (mask & (1 << i)) continue;

            const newSum = currentSum + nums[i];
            if (newSum > target) continue;

            const newMask = mask | (1 << i);
            const nextSum = newSum === target ? 0 : newSum;

            if (dp(newMask, nextSum)) {
                memo.set(mask, true);
                return true;
            }
        }

        memo.set(mask, false);
        return false;
    }

    return dp(0, 0);
}

// Time: O(n × 2^n), Space: O(2^n)
```

---

## Problem 9: Shopping Offers

### Approach 1: DFS with Memoization

```typescript
function shoppingOffers(price: number[], special: number[][], needs: number[]): number {
    const memo = new Map<string, number>();

    function dp(currentNeeds: number[]): number {
        const key = currentNeeds.join(',');

        if (memo.has(key)) return memo.get(key)!;

        // Base cost: buy all items individually
        let minCost = 0;
        for (let i = 0; i < price.length; i++) {
            minCost += price[i] * currentNeeds[i];
        }

        // Try each special offer
        for (const offer of special) {
            const newNeeds = [...currentNeeds];
            let valid = true;

            // Check if we can use this offer
            for (let i = 0; i < price.length; i++) {
                newNeeds[i] -= offer[i];
                if (newNeeds[i] < 0) {
                    valid = false;
                    break;
                }
            }

            if (valid) {
                const offerPrice = offer[offer.length - 1];
                minCost = Math.min(minCost, offerPrice + dp(newNeeds));
            }
        }

        memo.set(key, minCost);
        return minCost;
    }

    return dp(needs);
}

// Time: O(n^m × k) where n=items, m=max need, k=offers
// Space: O(n^m)
```

---

## Problem 10: Minimum Cost For Tickets

### Approach 1: DP by Days

```typescript
function mincostTickets(days: number[], costs: number[]): number {
    const lastDay = days[days.length - 1];
    const travelDays = new Set(days);

    // dp[i] = min cost to cover all travel days up to day i
    const dp: number[] = new Array(lastDay + 1).fill(0);

    for (let i = 1; i <= lastDay; i++) {
        if (!travelDays.has(i)) {
            // Not a travel day, cost stays same
            dp[i] = dp[i - 1];
        } else {
            // Try all three pass options
            const oneDayPass = dp[i - 1] + costs[0];
            const sevenDayPass = dp[Math.max(0, i - 7)] + costs[1];
            const thirtyDayPass = dp[Math.max(0, i - 30)] + costs[2];

            dp[i] = Math.min(oneDayPass, sevenDayPass, thirtyDayPass);
        }
    }

    return dp[lastDay];
}

// Time: O(last_day), Space: O(last_day)
```

### Approach 2: DP by Travel Days

```typescript
function mincostTickets(days: number[], costs: number[]): number {
    const n = days.length;

    // dp[i] = min cost to cover travel from day i onwards
    const dp: number[] = new Array(n + 1).fill(0);

    for (let i = n - 1; i >= 0; i--) {
        // Option 1: Buy 1-day pass
        let j = i;
        while (j < n && days[j] < days[i] + 1) j++;
        const oneDayPass = costs[0] + dp[j];

        // Option 2: Buy 7-day pass
        while (j < n && days[j] < days[i] + 7) j++;
        const sevenDayPass = costs[1] + dp[j];

        // Option 3: Buy 30-day pass
        while (j < n && days[j] < days[i] + 30) j++;
        const thirtyDayPass = costs[2] + dp[j];

        dp[i] = Math.min(oneDayPass, sevenDayPass, thirtyDayPass);
    }

    return dp[0];
}

// Time: O(n), Space: O(n)
```