# Lesson: Knapsack Dynamic Programming

---

## 📹 Video 1: 0/1 Knapsack Fundamentals (15 min)

**"0/1 Knapsack - Dynamic Programming" by NeetCode**
https://www.youtube.com/watch?v=gdT3N7QGqWQ

**Focus on:**
- The fundamental include/exclude decision
- How to build the DP table
- State transitions and recurrence relation
- When each item can only be used once

---

## 📹 Video 2: Unbounded Knapsack Pattern (15 min)

**"Coin Change - Dynamic Programming Unbounded Knapsack" by NeetCode**
https://www.youtube.com/watch?v=H9bfqozjoqs

**Focus on:**
- Difference from 0/1 knapsack
- When items can be reused
- Loop direction and why it matters
- Counting combinations vs permutations

---

## 📹 Video 3: Subset Sum & Variations (15 min)

**"Partition Equal Subset Sum - Dynamic Programming" by NeetCode**
https://www.youtube.com/watch?v=IsvocB5BJhw

**Focus on:**
- Recognizing subset sum pattern
- Transform problems to subset sum
- Boolean DP arrays
- Common variations

---

## 📹 Video 4: Space Optimization Techniques (15 min)

**"DP Space Optimization" by Abdul Bari**
https://www.youtube.com/watch?v=L_0pf5ySAq8

**Alternative - NeetCode on Space Optimization:**
https://www.youtube.com/watch?v=ndYuf38-qs4

**Focus on:**
- Rolling array technique
- 2D to 1D optimization
- When to iterate backwards
- Trade-offs in space optimization

---

## 🎯 Knapsack Pattern - Core Concepts

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

## 🔑 0/1 Knapsack - The Foundation

### Definition

**0/1 Knapsack:** Choose items to maximize value within weight limit. Each item used at most once.

### Why "0/1"?

- **0** = Don't take the item
- **1** = Take the item
- **Binary choice** at each step

### Recursive Approach

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

**Key points:**
- Each item considered once
- Move to next item (i + 1) in both branches
- Binary decision tree

---

### Tabulation Approach (2D)

```typescript
function knapsackDP(weights: number[], values: number[], W: number): number {
    const n = weights.length;
    const dp: number[][] = Array(n + 1).fill(null)
        .map(() => Array(W + 1).fill(0));

    // dp[i][w] = max value using first i items with capacity w

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

**Time:** O(n × W) | **Space:** O(n × W)

---

### Space Optimized (1D) - Critical!

```typescript
function knapsackOptimized(weights: number[], values: number[], W: number): number {
    const dp: number[] = new Array(W + 1).fill(0);

    for (let i = 0; i < weights.length; i++) {
        // BACKWARDS iteration prevents reusing same item
        for (let w = W; w >= weights[i]; w--) {
            dp[w] = Math.max(dp[w], values[i] + dp[w - weights[i]]);
        }
    }

    return dp[W];
}
```

**Time:** O(n × W) | **Space:** O(W)

**Critical:** Backwards iteration is key for 0/1 knapsack!

---

## 🔄 Unbounded Knapsack - Infinite Items

### Definition

**Unbounded Knapsack:** Items can be used multiple times. No limit on quantity.

### Example: Coin Change

```typescript
function coinChange(coins: number[], amount: number): number {
    const dp: number[] = new Array(amount + 1).fill(Infinity);
    dp[0] = 0;

    for (const coin of coins) {
        // FORWARD iteration allows reuse
        for (let i = coin; i <= amount; i++) {
            dp[i] = Math.min(dp[i], dp[i - coin] + 1);
        }
    }

    return dp[amount] === Infinity ? -1 : dp[amount];
}
```

**Time:** O(n × amount) | **Space:** O(amount)

---

## ⚖️ 0/1 vs Unbounded - The Key Difference

### Loop Direction Comparison

```typescript
// 0/1 Knapsack: BACKWARDS (no reuse)
for (const item of items) {
    for (let w = W; w >= weight[item]; w--) {
        dp[w] = Math.max(dp[w], dp[w - weight[item]] + value[item]);
    }
}

// Unbounded Knapsack: FORWARDS (allow reuse)
for (const item of items) {
    for (let w = weight[item]; w <= W; w++) {
        dp[w] = Math.max(dp[w], dp[w - weight[item]] + value[item]);
    }
}
```

### Why This Matters

**Backwards (0/1):**
- Uses old values from previous iteration
- Item cannot be reused
- Each item counted once

**Forwards (Unbounded):**
- Uses updated values from current iteration
- Item can be reused
- Item can be counted multiple times

### Visual Example

```
Item: weight=2, value=3, Capacity=5

Backwards (0/1):
w=5: uses dp[3] from previous iteration
w=3: uses dp[1] from previous iteration
→ Item used once

Forwards (Unbounded):
w=2: updates dp[2]
w=4: uses updated dp[2], item used twice!
→ Item can be reused
```

---

## 🎯 Subset Sum - Classic Pattern

### Problem

Can we select elements that sum to target?

### Key Insight

This is 0/1 knapsack where all values = weights.

```typescript
function canPartition(nums: number[]): boolean {
    const sum = nums.reduce((a, b) => a + b, 0);
    if (sum % 2 !== 0) return false;

    const target = sum / 2;
    const dp: boolean[] = new Array(target + 1).fill(false);
    dp[0] = true; // empty subset sums to 0

    for (const num of nums) {
        // Backwards for 0/1 (use each number once)
        for (let j = target; j >= num; j--) {
            dp[j] = dp[j] || dp[j - num];
        }
    }

    return dp[target];
}
```

**Time:** O(n × sum) | **Space:** O(sum)

---

## 🔢 Counting: Combinations vs Permutations

### Combinations (Order Doesn't Matter)

```typescript
function coinChange2(coins: number[], amount: number): number {
    const dp: number[] = new Array(amount + 1).fill(0);
    dp[0] = 1;

    // OUTER loop: coins (ensures combinations)
    for (const coin of coins) {
        for (let i = coin; i <= amount; i++) {
            dp[i] += dp[i - coin];
        }
    }

    return dp[amount];
}
```

**Result:** [1,2] and [2,1] counted once

---

### Permutations (Order Matters)

```typescript
function combinationSum4(nums: number[], target: number): number {
    const dp: number[] = new Array(target + 1).fill(0);
    dp[0] = 1;

    // OUTER loop: targets (ensures permutations)
    for (let i = 1; i <= target; i++) {
        for (const num of nums) {
            if (i >= num) {
                dp[i] += dp[i - num];
            }
        }
    }

    return dp[target];
}
```

**Result:** [1,2] and [2,1] counted separately

---

## 🎯 Pattern Recognition Guide

### When to Use Knapsack?

Look for these keywords:
- "Select items with constraint"
- "Partition into subsets"
- "Can you make target sum?"
- "Maximum/minimum with capacity"
- "Choose or not choose"
- "Equal sum subsets"

### Identify the Variation

```
"Each item used once" → 0/1 Knapsack
"Unlimited items" → Unbounded Knapsack
"Count ways to make sum" → Subset Sum
"Split equally" → Partition Problem
"Different order matters" → Permutations
```

---

## 🧠 State Design Strategies

### Basic States

```typescript
// 2D: Using first i items, can achieve value j
dp[i][j] = boolean or number

// 1D Space Optimized: Can achieve value j
dp[j] = boolean or number
```

### Advanced States

```typescript
// Multi-dimensional constraints
dp[i][j][k] = boolean // i items, j weight, k count

// Bitmask for subset selection
dp[mask][sum] = boolean // mask tracks selected items
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
1. Empty array → return 0 or false
2. Target = 0 → usually true (empty subset)
3. Single element → check if equals target
4. All same elements → calculate based on count
5. Negative numbers → check if allowed
6. Very large targets → optimize or return impossible

---

## 🔍 Debug Checklist

If your solution fails:
- [ ] Check DP array initialization (especially dp[0])
- [ ] Verify iteration direction (forward vs backward)
- [ ] Confirm index bounds (i-1 vs i)
- [ ] Test with minimal examples (n=1, n=2)
- [ ] Print DP table for small inputs
- [ ] Check for integer overflow
- [ ] Verify 0/1 vs unbounded decision

---

## 📝 Templates to Memorize

### 0/1 Knapsack Template

```typescript
function knapsack01(items: number[], capacity: number): number {
    const dp = new Array(capacity + 1).fill(0);

    for (const item of items) {
        // Backward for 0/1 (use once)
        for (let c = capacity; c >= item; c--) {
            dp[c] = Math.max(dp[c], dp[c - item] + value(item));
        }
    }

    return dp[capacity];
}
```

### Unbounded Knapsack Template

```typescript
function knapsackUnbounded(items: number[], capacity: number): number {
    const dp = new Array(capacity + 1).fill(0);

    for (const item of items) {
        // Forward for unbounded (reuse)
        for (let c = item; c <= capacity; c++) {
            dp[c] = Math.max(dp[c], dp[c - item] + value(item));
        }
    }

    return dp[capacity];
}
```

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

        // Iterate backwards for both dimensions (0/1)
        for (let i = m; i >= zeros; i--) {
            for (let j = n; j >= ones; j--) {
                dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j - ones] + 1);
            }
        }
    }

    return dp[m][n];
}
```

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **0/1 Knapsack:** Iterate backwards, no reuse
- **Unbounded:** Iterate forwards, allow reuse
- **Subset Sum:** Boolean DP, can we reach target?
- **Combinations:** Outer loop on items
- **Permutations:** Outer loop on targets

---

[Back to Session README](./README.md)
