# Session 13: 1D Dynamic Programming - Learning Material

## Video Resource

**NeetCode - Dynamic Programming Explained**
https://www.youtube.com/watch?v=73r3KWiEvyk

Watch from 0:00 to 25:00 for core concepts. This video covers:
- What is Dynamic Programming
- When to use DP
- Top-down vs Bottom-up approaches
- Common 1D DP patterns
- Space optimization techniques

---

## Core Concepts

### 1. What is Dynamic Programming?

Dynamic Programming is an algorithmic technique for solving optimization problems by breaking them down into simpler subproblems and storing the results to avoid redundant calculations.

**Key Requirements:**
1. **Overlapping Subproblems:** Same subproblems appear multiple times
2. **Optimal Substructure:** Optimal solution contains optimal sub-solutions

### 2. DP vs Other Approaches

```typescript
// Recursive (Exponential - O(2^n))
function fibRecursive(n: number): number {
    if (n <= 1) return n;
    return fibRecursive(n - 1) + fibRecursive(n - 2);
}

// Top-Down DP with Memoization (O(n))
function fibMemo(n: number, memo: Map<number, number> = new Map()): number {
    if (n <= 1) return n;
    if (memo.has(n)) return memo.get(n)!;

    const result = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);
    memo.set(n, result);
    return result;
}

// Bottom-Up DP (O(n))
function fibDP(n: number): number {
    if (n <= 1) return n;
    const dp = new Array(n + 1);
    dp[0] = 0;
    dp[1] = 1;

    for (let i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
}

// Space-Optimized (O(1))
function fibOptimized(n: number): number {
    if (n <= 1) return n;
    let prev2 = 0, prev1 = 1;

    for (let i = 2; i <= n; i++) {
        const curr = prev1 + prev2;
        prev2 = prev1;
        prev1 = curr;
    }
    return prev1;
}
```

---

## Common 1D DP Patterns

### Pattern 1: Linear Sequence
Problems where dp[i] depends on previous elements in sequence.

**Example: Climbing Stairs**
```typescript
// dp[i] = number of ways to reach step i
// dp[i] = dp[i-1] + dp[i-2]
```

### Pattern 2: Decision Making
At each step, make a choice (include/exclude).

**Example: House Robber**
```typescript
// dp[i] = max money robbing up to house i
// dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

### Pattern 3: Optimization
Find minimum/maximum over all choices.

**Example: Coin Change**
```typescript
// dp[i] = minimum coins to make amount i
// dp[i] = min(dp[i-coin] + 1) for all coins
```

### Pattern 4: Counting
Count number of ways to achieve something.

**Example: Decode Ways**
```typescript
// dp[i] = number of ways to decode up to index i
// dp[i] = dp[i-1] + (valid two-digit ? dp[i-2] : 0)
```

### Pattern 5: Existence
Check if something is possible.

**Example: Jump Game**
```typescript
// dp[i] = can we reach index i?
// dp[i] = any(dp[j] && j + nums[j] >= i) for j < i
```

---

## State Definition Strategy

### 1. Identify What Changes
What parameters vary as you solve subproblems?

### 2. Define State Meaning
What does dp[i] represent?

### 3. Write Recurrence Relation
How to compute dp[i] from previous states?

### 4. Identify Base Cases
What are the smallest subproblems?

### 5. Determine Computation Order
In what order should we fill the DP table?

---

## Implementation Templates

### Top-Down Template (Memoization)
```typescript
function solveMemo(n: number): number {
    const memo = new Map<number, number>();

    function dp(i: number): number {
        // Base cases
        if (i <= 0) return baseValue;

        // Check memo
        if (memo.has(i)) return memo.get(i)!;

        // Compute result
        let result = 0;
        // Recurrence relation
        result = /* compute from dp(i-1), dp(i-2), etc. */

        // Store and return
        memo.set(i, result);
        return result;
    }

    return dp(n);
}
```

### Bottom-Up Template (Tabulation)
```typescript
function solveDP(n: number): number {
    // Edge cases
    if (n <= 0) return baseValue;

    // Initialize DP array
    const dp = new Array(n + 1);

    // Base cases
    dp[0] = baseValue0;
    dp[1] = baseValue1;

    // Fill DP table
    for (let i = 2; i <= n; i++) {
        // Recurrence relation
        dp[i] = /* compute from dp[i-1], dp[i-2], etc. */
    }

    return dp[n];
}
```

### Space-Optimized Template
```typescript
function solveOptimized(n: number): number {
    // Edge cases
    if (n <= 0) return baseValue;

    // Only keep necessary previous states
    let prev2 = baseValue0;
    let prev1 = baseValue1;

    for (let i = 2; i <= n; i++) {
        const curr = /* compute from prev1, prev2 */
        prev2 = prev1;
        prev1 = curr;
    }

    return prev1;
}
```

---

## Problem-Specific Techniques

### 1. Subsequence Problems
Track state based on whether current element is included.

### 2. Substring Problems
Often need to check all possible centers or endings.

### 3. Decision Problems
Model as choosing best option at each step.

### 4. Counting Problems
Sum up ways from all valid previous states.

### 5. Game Theory Problems
Consider optimal play from both players.

---

## Debugging DP Solutions

### Common Issues and Fixes

1. **Wrong Answer**
   - Check base cases
   - Verify recurrence relation
   - Print DP table for small inputs

2. **Runtime Error**
   - Check array bounds
   - Initialize all necessary values
   - Handle edge cases

3. **Time Limit Exceeded**
   - Ensure memoization is working
   - Check for infinite recursion
   - Optimize unnecessary computations

4. **Memory Limit Exceeded**
   - Use space optimization
   - Clear unnecessary data
   - Consider iterative over recursive

---

## Practice Strategy

### Phase 1: Understanding
1. Solve recursively first
2. Identify overlapping subproblems
3. Add memoization

### Phase 2: Optimization
1. Convert to bottom-up
2. Optimize space complexity
3. Simplify code

### Phase 3: Pattern Recognition
1. Categorize problem type
2. Apply standard template
3. Customize for specific requirements

---

## Interview Tips

### 1. Problem Recognition
- Look for keywords: "optimal", "maximum", "minimum", "count ways"
- Check if greedy doesn't work
- Identify if subproblems overlap

### 2. Communication
- Explain why DP is needed
- Define state clearly
- Write recurrence before coding
- Discuss space optimization

### 3. Time Management
- Start with brute force (5 min)
- Optimize with DP (15 min)
- Code solution (15 min)
- Test and debug (10 min)

### 4. Common Follow-ups
- "Can you optimize space?"
- "What if input is very large?"
- "Can you solve it iteratively?"
- "Print the actual solution, not just the value"

---

## Next Steps

After watching the video and reading this material:
1. Work through the problems in order
2. Try multiple approaches for each
3. Focus on pattern recognition
4. Practice explaining your thought process

Remember: DP is about building solutions from smaller solutions. Master the patterns, and complex problems become manageable!