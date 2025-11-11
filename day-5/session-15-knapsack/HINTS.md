# Hints - Session 15: Knapsack Dynamic Programming

## Problem 1: Partition Equal Subset Sum

### Hint Level 1 (Gentle)
- First check if the total sum is even
- Think about what sum each partition should have
- This is a subset sum problem in disguise

### Hint Level 2 (Direct)
- Target = total_sum / 2
- Can you find a subset that sums to target?
- Use 0/1 knapsack pattern (each element used once)

### Hint Level 3 (Detailed)
```typescript
// 1. Check if sum is even
const sum = nums.reduce((a, b) => a + b, 0);
if (sum % 2 !== 0) return false;

// 2. Find subset with sum = total/2
const target = sum / 2;
const dp = new Array(target + 1).fill(false);
dp[0] = true;

// 3. For each number, update what sums are achievable
for (const num of nums) {
    // Iterate backwards to avoid reusing same element
    for (let j = target; j >= num; j--) {
        dp[j] = dp[j] || dp[j - num];
    }
}
```

---

## Problem 2: Target Sum

### Hint Level 1 (Gentle)
- Let P = sum of positive numbers, N = sum of negative numbers
- You have P - N = target and P + N = total_sum
- Can you solve for P?

### Hint Level 2 (Direct)
- From P - N = target and P + N = sum:
- 2P = target + sum → P = (target + sum) / 2
- Count subsets with sum = P

### Hint Level 3 (Detailed)
```typescript
// 1. Transform the problem
const sum = nums.reduce((a, b) => a + b, 0);
if ((target + sum) % 2 !== 0 || sum < Math.abs(target)) return 0;

const positiveSum = (target + sum) / 2;

// 2. Count subsets with sum = positiveSum
const dp = new Array(positiveSum + 1).fill(0);
dp[0] = 1; // One way to make 0

// 3. For each number, update counts
for (const num of nums) {
    for (let j = positiveSum; j >= num; j--) {
        dp[j] += dp[j - num]; // Add ways to make j
    }
}
```

---

## Problem 3: Last Stone Weight II

### Hint Level 1 (Gentle)
- The final weight is the difference between two groups
- You want to minimize |group1 - group2|
- Think about partitioning the stones

### Hint Level 2 (Direct)
- Find a subset with sum as close to total_sum/2 as possible
- Result = total_sum - 2 × subset_sum
- Use 0/1 knapsack to find the best subset

### Hint Level 3 (Detailed)
```typescript
// 1. Find maximum subset sum <= total/2
const sum = stones.reduce((a, b) => a + b, 0);
const target = Math.floor(sum / 2);

// 2. Track achievable sums
const dp = new Array(target + 1).fill(false);
dp[0] = true;

// 3. Update achievable sums
for (const stone of stones) {
    for (let j = target; j >= stone; j--) {
        dp[j] = dp[j] || dp[j - stone];
    }
}

// 4. Find largest achievable sum
for (let j = target; j >= 0; j--) {
    if (dp[j]) return sum - 2 * j;
}
```

---

## Problem 4: Ones and Zeroes

### Hint Level 1 (Gentle)
- You have two constraints: m zeros and n ones
- Each string "costs" some zeros and ones
- This is a 2D knapsack problem

### Hint Level 2 (Direct)
- dp[i][j] = max strings with at most i zeros and j ones
- For each string, decide include or exclude
- Remember to iterate backwards for both dimensions

### Hint Level 3 (Detailed)
```typescript
// 1. Initialize 2D DP array
const dp = Array(m + 1).fill(null)
    .map(() => Array(n + 1).fill(0));

// 2. Process each string
for (const str of strs) {
    const zeros = (str.match(/0/g) || []).length;
    const ones = str.length - zeros;

    // 3. Update DP (backwards to avoid reuse)
    for (let i = m; i >= zeros; i--) {
        for (let j = n; j >= ones; j--) {
            dp[i][j] = Math.max(
                dp[i][j], // exclude
                dp[i - zeros][j - ones] + 1 // include
            );
        }
    }
}
```

---

## Problem 5: Coin Change 2

### Hint Level 1 (Gentle)
- This is unbounded knapsack (coins are reusable)
- You're counting combinations, not permutations
- Order of coins doesn't matter for combinations

### Hint Level 2 (Direct)
- Outer loop: coins, Inner loop: amounts
- This ensures combinations (not permutations)
- Forward iteration allows coin reuse

### Hint Level 3 (Detailed)
```typescript
// 1. Initialize DP
const dp = new Array(amount + 1).fill(0);
dp[0] = 1; // One way to make 0

// 2. Process each coin type
for (const coin of coins) {
    // 3. Update amounts (forward for reuse)
    for (let i = coin; i <= amount; i++) {
        dp[i] += dp[i - coin];
    }
}
// This counts: {1,2} but not {2,1}
```

---

## Problem 6: Combination Sum IV

### Hint Level 1 (Gentle)
- This counts permutations, not combinations
- Order matters: [1,2] and [2,1] are different
- Loop order is opposite of Coin Change 2

### Hint Level 2 (Direct)
- Outer loop: targets, Inner loop: nums
- This ensures permutations are counted
- Each position tries all possible numbers

### Hint Level 3 (Detailed)
```typescript
// 1. Initialize DP
const dp = new Array(target + 1).fill(0);
dp[0] = 1;

// 2. Build up each target value
for (let i = 1; i <= target; i++) {
    // 3. Try each number at this position
    for (const num of nums) {
        if (i >= num) {
            dp[i] += dp[i - num];
        }
    }
}
// This counts both: {1,2} and {2,1}
```

---

## Problem 7: Word Break

### Hint Level 1 (Gentle)
- dp[i] represents if s[0:i] can be segmented
- For each position, check all possible word endings
- Use a Set for O(1) word lookups

### Hint Level 2 (Direct)
- For position i, check all j < i
- If dp[j] is true and s[j:i] is a word, then dp[i] = true
- Start with dp[0] = true (empty string)

### Hint Level 3 (Detailed)
```typescript
// 1. Setup
const wordSet = new Set(wordDict);
const dp = new Array(s.length + 1).fill(false);
dp[0] = true;

// 2. Check each position
for (let i = 1; i <= s.length; i++) {
    // 3. Try all possible splits
    for (let j = 0; j < i; j++) {
        if (dp[j] && wordSet.has(s.substring(j, i))) {
            dp[i] = true;
            break; // Found valid segmentation
        }
    }
}
```

---

## Problem 8: Partition to K Equal Sum Subsets

### Hint Level 1 (Gentle)
- First check if total sum is divisible by k
- Each subset should have sum = total/k
- Use bitmask to track which elements are used

### Hint Level 2 (Direct)
- Use backtracking with memoization
- State: (mask, currentSum) where mask tracks used elements
- When currentSum reaches target, reset to 0

### Hint Level 3 (Detailed)
```typescript
// 1. Validate
const sum = nums.reduce((a, b) => a + b, 0);
if (sum % k !== 0) return false;
const target = sum / k;

// 2. Backtrack with bitmask
function dp(mask: number, currentSum: number): boolean {
    if (mask === (1 << n) - 1) return true; // All used

    for (let i = 0; i < n; i++) {
        if (mask & (1 << i)) continue; // Already used

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

### Hint Level 1 (Gentle)
- This is a variation of knapsack with special offers
- State is the current needs array
- Try both: use an offer or buy individually

### Hint Level 2 (Direct)
- DFS with memoization using needs as key
- For each state, calculate base cost (buy individually)
- Try each valid offer and recurse with reduced needs

### Hint Level 3 (Detailed)
```typescript
// 1. Memoized DFS
function dp(needs: number[]): number {
    const key = needs.join(',');
    if (memo.has(key)) return memo.get(key)!;

    // 2. Base cost: buy individually
    let minCost = 0;
    for (let i = 0; i < price.length; i++) {
        minCost += price[i] * needs[i];
    }

    // 3. Try each offer
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

### Hint Level 1 (Gentle)
- For each travel day, you have 3 choices of passes
- dp[i] = minimum cost to cover all days up to day i
- Only update cost on actual travel days

### Hint Level 2 (Direct)
- Create a set of travel days for O(1) lookup
- For each day, try: 1-day, 7-day, and 30-day passes
- Look back 1, 7, or 30 days for the previous cost

### Hint Level 3 (Detailed)
```typescript
// 1. Setup
const lastDay = days[days.length - 1];
const travelDays = new Set(days);
const dp = new Array(lastDay + 1).fill(0);

// 2. Process each day
for (let i = 1; i <= lastDay; i++) {
    if (!travelDays.has(i)) {
        dp[i] = dp[i - 1]; // Not traveling
    } else {
        // 3. Try all three passes
        const oneDayPass = dp[i - 1] + costs[0];
        const sevenDayPass = dp[Math.max(0, i - 7)] + costs[1];
        const thirtyDayPass = dp[Math.max(0, i - 30)] + costs[2];

        dp[i] = Math.min(oneDayPass, sevenDayPass, thirtyDayPass);
    }
}
```