# Hints - Session 15: Knapsack Dynamic Programming

Progressive hints for 10 problems. Struggling is part of learning.

---

## Problem 1: Partition Equal Subset Sum

### Level 1
What data structure tracks achievable sums? Need to check "can we reach target/2?"

### Level 2
Hash map or boolean DP array. For each number, update what sums are achievable. If sum is odd, impossible. Target = sum/2.

### Level 3
```typescript
const sum = nums.reduce((a, b) => a + b, 0);
if (sum % 2 !== 0) return false;

const target = sum / 2;
const dp = new Array(target + 1).fill(false);
dp[0] = true;

for (const num of nums) {
    // Backwards to avoid reusing same element
    for (let j = target; j >= num; j--) {
        dp[j] = dp[j] || dp[j - num];
    }
}
```

---

## Problem 2: Target Sum

### Level 1
Let P = sum of positive, N = sum of negative. You have P - N = target and P + N = total. Can you solve for P?

### Level 2
From P - N = target and P + N = sum: 2P = target + sum → P = (target + sum) / 2. Count subsets with sum = P.

### Level 3
```typescript
const sum = nums.reduce((a, b) => a + b, 0);
if ((target + sum) % 2 !== 0 || sum < Math.abs(target)) return 0;

const positiveSum = (target + sum) / 2;
const dp = new Array(positiveSum + 1).fill(0);
dp[0] = 1;

for (const num of nums) {
    for (let j = positiveSum; j >= num; j--) {
        dp[j] += dp[j - num];
    }
}
```

---

## Problem 3: Last Stone Weight II

### Level 1
The final weight is the difference between two groups. You want to minimize |group1 - group2|. Think partitioning.

### Level 2
Find a subset with sum as close to total_sum/2 as possible. Result = total_sum - 2 × subset_sum.

### Level 3
```typescript
const sum = stones.reduce((a, b) => a + b, 0);
const target = Math.floor(sum / 2);

const dp = new Array(target + 1).fill(false);
dp[0] = true;

for (const stone of stones) {
    for (let j = target; j >= stone; j--) {
        dp[j] = dp[j] || dp[j - stone];
    }
}

// Find largest achievable sum
for (let j = target; j >= 0; j--) {
    if (dp[j]) return sum - 2 * j;
}
```

---

## Problem 4: Ones and Zeroes

### Level 1
You have two constraints: m zeros and n ones. Each string "costs" some zeros and ones. This is 2D knapsack.

### Level 2
dp[i][j] = max strings with at most i zeros and j ones. For each string, decide include or exclude. Iterate backwards for both dimensions.

### Level 3
```typescript
const dp = Array(m + 1).fill(null)
    .map(() => Array(n + 1).fill(0));

for (const str of strs) {
    const zeros = (str.match(/0/g) || []).length;
    const ones = str.length - zeros;

    // Backwards to avoid reuse
    for (let i = m; i >= zeros; i--) {
        for (let j = n; j >= ones; j--) {
            dp[i][j] = Math.max(
                dp[i][j],
                dp[i - zeros][j - ones] + 1
            );
        }
    }
}
```

---

## Problem 5: Coin Change 2

### Level 1
This is unbounded knapsack (coins are reusable). You're counting combinations, not permutations. Order doesn't matter.

### Level 2
Outer loop: coins, Inner loop: amounts. This ensures combinations. Forward iteration allows coin reuse.

### Level 3
```typescript
const dp = new Array(amount + 1).fill(0);
dp[0] = 1;

// Process each coin type
for (const coin of coins) {
    // Forward for reuse
    for (let i = coin; i <= amount; i++) {
        dp[i] += dp[i - coin];
    }
}
```

---

## Problem 6: Combination Sum IV

### Level 1
This counts permutations, not combinations. Order matters: [1,2] and [2,1] are different. Loop order is opposite of Coin Change 2.

### Level 2
Outer loop: targets, Inner loop: nums. This ensures permutations. Each position tries all possible numbers.

### Level 3
```typescript
const dp = new Array(target + 1).fill(0);
dp[0] = 1;

// Build up each target value
for (let i = 1; i <= target; i++) {
    // Try each number at this position
    for (const num of nums) {
        if (i >= num) {
            dp[i] += dp[i - num];
        }
    }
}
```

---

## Problem 7: Word Break

### Level 1
dp[i] represents if s[0:i] can be segmented. For each position, check all possible word endings. Use Set for O(1) lookups.

### Level 2
For position i, check all j < i. If dp[j] is true and s[j:i] is a word, then dp[i] = true. Start with dp[0] = true.

### Level 3
```typescript
const wordSet = new Set(wordDict);
const dp = new Array(s.length + 1).fill(false);
dp[0] = true;

for (let i = 1; i <= s.length; i++) {
    for (let j = 0; j < i; j++) {
        if (dp[j] && wordSet.has(s.substring(j, i))) {
            dp[i] = true;
            break;
        }
    }
}
```

---

## Problem 8: Partition to K Equal Sum Subsets

### Level 1
First check if total sum is divisible by k. Each subset should have sum = total/k. Use bitmask to track which elements are used.

### Level 2
Use backtracking with memoization. State: (mask, currentSum) where mask tracks used elements. When currentSum reaches target, reset to 0.

### Level 3
```typescript
const sum = nums.reduce((a, b) => a + b, 0);
if (sum % k !== 0) return false;
const target = sum / k;

function dp(mask: number, currentSum: number): boolean {
    if (mask === (1 << n) - 1) return true;

    for (let i = 0; i < n; i++) {
        if (mask & (1 << i)) continue;

        const newSum = currentSum + nums[i];
        if (newSum > target) continue;

        const nextSum = newSum === target ? 0 : newSum;
        if (dp(mask | (1 << i), nextSum)) return true;
    }
    return false;
}
```

---

## Problem 9: Shopping Offers

### Level 1
This is a variation of knapsack with special offers. State is the current needs array. Try both: use an offer or buy individually.

### Level 2
DFS with memoization using needs as key. For each state, calculate base cost (buy individually). Try each valid offer and recurse.

### Level 3
```typescript
function dp(needs: number[]): number {
    const key = needs.join(',');
    if (memo.has(key)) return memo.get(key)!;

    // Base cost: buy individually
    let minCost = 0;
    for (let i = 0; i < price.length; i++) {
        minCost += price[i] * needs[i];
    }

    // Try each offer
    for (const offer of special) {
        const newNeeds = [...needs];
        let valid = true;

        for (let i = 0; i < price.length; i++) {
            newNeeds[i] -= offer[i];
            if (newNeeds[i] < 0) {
                valid = false;
                break;
            }
        }

        if (valid) {
            minCost = Math.min(minCost, offer[price.length] + dp(newNeeds));
        }
    }
    return minCost;
}
```

---

## Problem 10: Minimum Cost For Tickets

### Level 1
For each travel day, you have 3 choices of passes. dp[i] = minimum cost to cover all days up to day i. Only update cost on actual travel days.

### Level 2
Create a set of travel days for O(1) lookup. For each day, try: 1-day, 7-day, and 30-day passes. Look back 1, 7, or 30 days.

### Level 3
```typescript
const lastDay = days[days.length - 1];
const travelDays = new Set(days);
const dp = new Array(lastDay + 1).fill(0);

for (let i = 1; i <= lastDay; i++) {
    if (!travelDays.has(i)) {
        dp[i] = dp[i - 1];
    } else {
        const oneDayPass = dp[i - 1] + costs[0];
        const sevenDayPass = dp[Math.max(0, i - 7)] + costs[1];
        const thirtyDayPass = dp[Math.max(0, i - 30)] + costs[2];

        dp[i] = Math.min(oneDayPass, sevenDayPass, thirtyDayPass);
    }
}
```

---

## Pattern Hints

**"Partition array equally"** → Subset Sum (target = sum/2)

**"Count ways to make sum"** → Unbounded Knapsack (combinations)

**"Different order matters"** → Permutations (outer loop on targets)

**"Multiple constraints"** → Multi-dimensional DP

**"Limited choices"** → Bitmask DP

---

## Using Hints Effectively

1. Try 10+ min before Level 1
2. Try 5+ min after each hint
3. If use Level 3, mark for review
4. Don't feel bad - hints are for learning

Goal: Learn pattern, not just solve one problem.

---

[Back to Problems](./PROBLEMS.md) | [Back to Solutions](./SOLUTIONS.md)
