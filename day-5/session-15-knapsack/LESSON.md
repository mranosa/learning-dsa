# Lesson: Knapsack Dynamic Programming

## 📹 Video Assignment (25 minutes)

**Primary Video:**
"0/1 Knapsack - Dynamic Programming" by NeetCode
https://www.youtube.com/watch?v=gdT3N7QGqWQ

**Alternative Videos** (for different perspectives):
- "Knapsack Problem Explained" by Abdul Bari (15 min): https://www.youtube.com/watch?v=kvyShbFVaY8
- "DP Playlist - Knapsack Problems" by take U forward: https://www.youtube.com/watch?v=GqOmJHQZivw

**What to focus on:**
- The fundamental include/exclude decision
- How to build the DP table
- Space optimization techniques
- Recognizing knapsack variations

---

## 📚 Knapsack Pattern - Core Concepts

### What is the Knapsack Problem?

The knapsack problem asks: Given items with weights and values, what's the maximum value you can carry in a knapsack of limited capacity?

**Key insight:** Every item presents a binary choice - take it or leave it. This creates a decision tree that DP can optimize.

### The Three Main Variations

```
1. 0/1 Knapsack: Each item used at most once
2. Unbounded Knapsack: Items can be reused infinitely
3. Bounded Knapsack: Each item has limited quantity
```

**Pattern recognition:**
- "Partition array" → 0/1 Knapsack
- "Coin change" → Unbounded Knapsack
- "Limited supply" → Bounded Knapsack

---

### 0/1 Knapsack - The Classic Pattern

**Definition:** Choose items to maximize value within weight limit.

**Recursive Approach:**
```typescript
function knapsack(weights: number[], values: number[], W: number): number {
    const n = weights.length;

    function dp(i: number, w: number): number {
        // Base case: no items or no capacity
        if (i === n || w === 0) return 0;

        // Can't include current item
        if (weights[i] > w) {
            return dp(i + 1, w);
        }

        // Max of include vs exclude
        const include = values[i] + dp(i + 1, w - weights[i]);
        const exclude = dp(i + 1, w);

        return Math.max(include, exclude);
    }

    return dp(0, W);
}
```

**Tabulation Approach:**
```typescript
function knapsackDP(weights: number[], values: number[], W: number): number {
    const n = weights.length;
    const dp: number[][] = Array(n + 1).fill(null)
        .map(() => Array(W + 1).fill(0));

    for (let i = 1; i <= n; i++) {
        for (let w = 1; w <= W; w++) {
            if (weights[i - 1] <= w) {
                dp[i][w] = Math.max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]], // include
                    dp[i - 1][w] // exclude
                );
            } else {
                dp[i][w] = dp[i - 1][w]; // can't include
            }
        }
    }

    return dp[n][W];
}
```

**Space Optimized (1D Array):**
```typescript
function knapsackOptimized(weights: number[], values: number[], W: number): number {
    const dp: number[] = new Array(W + 1).fill(0);

    for (let i = 0; i < weights.length; i++) {
        // Iterate backwards to avoid using updated values
        for (let w = W; w >= weights[i]; w--) {
            dp[w] = Math.max(dp[w], values[i] + dp[w - weights[i]]);
        }
    }

    return dp[W];
}
```

---

### Subset Sum - A Key Variation

**Problem:** Can we select elements that sum to target?

**Key insight:** This is knapsack where all values = weights.

```typescript
function canPartition(nums: number[]): boolean {
    const sum = nums.reduce((a, b) => a + b, 0);
    if (sum % 2 !== 0) return false;

    const target = sum / 2;
    const dp: boolean[] = new Array(target + 1).fill(false);
    dp[0] = true; // empty subset sums to 0

    for (const num of nums) {
        // Iterate backwards to avoid reusing same element
        for (let j = target; j >= num; j--) {
            dp[j] = dp[j] || dp[j - num];
        }
    }

    return dp[target];
}
```

---

### Unbounded Knapsack - Coin Change Pattern

**Problem:** Items can be used multiple times.

```typescript
function coinChange(coins: number[], amount: number): number {
    const dp: number[] = new Array(amount + 1).fill(Infinity);
    dp[0] = 0;

    for (const coin of coins) {
        // Forward iteration allows reuse
        for (let i = coin; i <= amount; i++) {
            dp[i] = Math.min(dp[i], dp[i - coin] + 1);
        }
    }

    return dp[amount] === Infinity ? -1 : dp[amount];
}
```

**Key difference:** Forward vs backward iteration determines reuse!

---

## 🎯 Pattern Recognition Guide

### When to Use Knapsack?

Look for these keywords:
- "Select items with constraint"
- "Partition into subsets"
- "Can you make target sum?"
- "Maximum/minimum with capacity"
- "Choose or not choose"

### State Design Strategies

**Basic States:**
- `dp[i][j]` = using first i items, achieve value j
- `dp[j]` = can we achieve value j (space optimized)

**Advanced States:**
- `dp[i][j][k]` = first i items, sum j, count k
- `dp[mask][sum]` = bitmask for selected items

### Common Transformations

**Target Sum → Subset Sum:**
```typescript
// Target Sum: assign + or - to make target
// Transform: Find subset with sum = (total + target) / 2
function findTargetSumWays(nums: number[], target: number): number {
    const sum = nums.reduce((a, b) => a + b, 0);
    if ((sum + target) % 2 !== 0 || sum < Math.abs(target)) {
        return 0;
    }

    const newTarget = (sum + target) / 2;
    // Now count subsets with sum = newTarget
}
```

---

## 💡 Interview Tips

### Quick Complexity Analysis

**Time Complexity:**
- 0/1 Knapsack: O(n × W) where n = items, W = capacity
- Subset Sum: O(n × sum)
- Coin Change: O(n × amount)

**Space Complexity:**
- 2D DP: O(n × W)
- 1D optimized: O(W)
- Recursive + memo: O(n × W) + call stack

### Common Edge Cases

Always test:
1. Empty array
2. Target = 0
3. Single element
4. All same elements
5. Negative numbers (if allowed)
6. Very large targets

### Optimization Techniques

1. **Rolling Array:** Use two 1D arrays instead of 2D
2. **In-place:** Modify input if allowed
3. **Early termination:** Stop if target reached
4. **Pruning:** Skip impossible states

---

## 🔍 Debug Checklist

If your solution fails:
- [ ] Check DP array initialization (especially dp[0])
- [ ] Verify iteration direction (forward vs backward)
- [ ] Confirm index bounds (i-1 vs i)
- [ ] Test with minimal examples (n=1, n=2)
- [ ] Print DP table for small inputs
- [ ] Check for integer overflow

---

## 📝 Template to Memorize

```typescript
// 0/1 Knapsack Template
function knapsackPattern(items: number[], capacity: number): number {
    const dp = new Array(capacity + 1).fill(0);

    for (const item of items) {
        // Backward for 0/1 (use once)
        for (let c = capacity; c >= item; c--) {
            dp[c] = Math.max(dp[c], dp[c - item] + value(item));
        }
        // Forward for unbounded (reuse)
        // for (let c = item; c <= capacity; c++) {
        //     dp[c] = Math.max(dp[c], dp[c - item] + value(item));
        // }
    }

    return dp[capacity];
}
```

Remember: Direction determines reusability!

---

## 🚀 Advanced Patterns

### Multi-Dimensional Knapsack

Sometimes you need multiple constraints:

```typescript
// Example: Ones and Zeroes
function findMaxForm(strs: string[], m: number, n: number): number {
    const dp: number[][] = Array(m + 1).fill(null)
        .map(() => Array(n + 1).fill(0));

    for (const str of strs) {
        const zeros = (str.match(/0/g) || []).length;
        const ones = (str.match(/1/g) || []).length;

        // Iterate backwards for both dimensions
        for (let i = m; i >= zeros; i--) {
            for (let j = n; j >= ones; j--) {
                dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j - ones] + 1);
            }
        }
    }

    return dp[m][n];
}
```

### State Compression with Bitmask

For small n (≤20), use bitmask for subset selection:

```typescript
function canPartitionKSubsets(nums: number[], k: number): boolean {
    const sum = nums.reduce((a, b) => a + b, 0);
    if (sum % k !== 0) return false;

    const target = sum / k;
    const n = nums.length;
    const memo = new Map<string, boolean>();

    function dp(mask: number, currentSum: number): boolean {
        const key = `${mask},${currentSum}`;
        if (memo.has(key)) return memo.get(key)!;

        if (mask === (1 << n) - 1) return true;

        for (let i = 0; i < n; i++) {
            if (mask & (1 << i)) continue;

            const newSum = currentSum + nums[i];
            if (newSum > target) continue;

            const newMask = mask | (1 << i);
            const nextSum = newSum === target ? 0 : newSum;

            if (dp(newMask, nextSum)) {
                memo.set(key, true);
                return true;
            }
        }

        memo.set(key, false);
        return false;
    }

    return dp(0, 0);
}
```

---

## Ready to Practice!

You now have the tools to solve any knapsack problem. Remember:
1. Identify the variation (0/1, unbounded, subset)
2. Design your state representation
3. Write recursive solution first
4. Convert to tabulation
5. Optimize space if possible

Start with Problem 1 in PROBLEMS.md!