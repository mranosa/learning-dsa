# 2D Dynamic Programming - Complete Guide

## Introduction

2D Dynamic Programming extends the concepts of 1D DP to problems involving two dimensions or two variables. These problems often involve grids, matrices, or comparing two sequences.

---

## Core Concepts

### What is 2D DP?

2D DP problems have states that depend on two variables:
- **Grid problems:** dp[row][col] = optimal solution at position (row, col)
- **String problems:** dp[i][j] = result for first i chars of string1 and first j chars of string2
- **Interval problems:** dp[left][right] = optimal solution for range [left, right]

### Key Characteristics

1. **Optimal Substructure:** Solution can be built from smaller subproblems
2. **Overlapping Subproblems:** Same subproblems appear multiple times
3. **Two-dimensional State:** Need two variables to uniquely identify a state

---

## Video Resources

### Essential Videos (Watch First)

1. **2D Dynamic Programming Introduction** (15 min)
   - NeetCode: https://www.youtube.com/watch?v=cJ24x7lLies
   - Covers grid traversal and basic patterns

2. **Unique Paths Explanation** (12 min)
   - NeetCode: https://www.youtube.com/watch?v=IlEsdxuD4lY
   - Foundation for grid DP problems

3. **Longest Common Subsequence** (18 min)
   - NeetCode: https://www.youtube.com/watch?v=Ua0GhsJSlWM
   - Classic string DP pattern

### Advanced Topics

4. **Edit Distance (Levenshtein)** (20 min)
   - NeetCode: https://www.youtube.com/watch?v=XYi2-LPrwm4
   - Important for string comparison

5. **Regular Expression Matching** (25 min)
   - NeetCode: https://www.youtube.com/watch?v=l3K8lrAOmU0
   - Complex pattern matching

---

## Common Patterns

### 1. Grid Traversal Pattern

```typescript
function gridDP(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const dp: number[][] = Array(m).fill(0).map(() => Array(n).fill(0));

    // Base case: Initialize first row and column
    dp[0][0] = grid[0][0];

    for (let i = 1; i < m; i++) {
        dp[i][0] = dp[i-1][0] + grid[i][0];
    }

    for (let j = 1; j < n; j++) {
        dp[0][j] = dp[0][j-1] + grid[0][j];
    }

    // Fill the DP table
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
        }
    }

    return dp[m-1][n-1];
}
```

### 2. String Comparison Pattern

```typescript
function stringDP(s1: string, s2: string): number {
    const m = s1.length;
    const n = s2.length;
    const dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

    // Base cases
    for (let i = 0; i <= m; i++) dp[i][0] = 0;
    for (let j = 0; j <= n; j++) dp[0][j] = 0;

    // Fill the DP table
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (s1[i-1] === s2[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }

    return dp[m][n];
}
```

### 3. Space Optimization Pattern

```typescript
function optimizedDP(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;

    // Use only two rows instead of full matrix
    let prev = new Array(n).fill(0);
    let curr = new Array(n).fill(0);

    // Initialize first row
    prev[0] = grid[0][0];
    for (let j = 1; j < n; j++) {
        prev[j] = prev[j-1] + grid[0][j];
    }

    // Process remaining rows
    for (let i = 1; i < m; i++) {
        curr[0] = prev[0] + grid[i][0];
        for (let j = 1; j < n; j++) {
            curr[j] = Math.min(prev[j], curr[j-1]) + grid[i][j];
        }
        [prev, curr] = [curr, prev];
    }

    return prev[n-1];
}
```

---

## Problem-Specific Techniques

### Path Counting Problems
- Initialize dp[0][0] = 1 (one way to start)
- dp[i][j] = dp[i-1][j] + dp[i][j-1] (sum of ways from top and left)

### Minimum/Maximum Path Problems
- Initialize first row and column with cumulative sums
- dp[i][j] = min/max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

### String Matching Problems
- Extra row/column for empty string
- Diagonal transition for character match
- Consider all three directions (delete, insert, replace)

### Pattern Matching Problems
- Handle wildcards specially
- Consider multiple previous states
- May need to look back multiple positions

---

## TypeScript Tips

### Creating 2D Arrays

```typescript
// Method 1: Fill with map
const dp: number[][] = Array(m).fill(0).map(() => Array(n).fill(0));

// Method 2: Nested loops
const dp: number[][] = [];
for (let i = 0; i < m; i++) {
    dp[i] = new Array(n).fill(0);
}

// Method 3: For boolean arrays
const visited: boolean[][] = Array(m).fill(false).map(() => Array(n).fill(false));
```

### Common Helper Functions

```typescript
// Check if position is valid
function isValid(row: number, col: number, m: number, n: number): boolean {
    return row >= 0 && row < m && col >= 0 && col < n;
}

// Get value with default
function getValue(dp: number[][], i: number, j: number, defaultVal: number = 0): number {
    if (i < 0 || j < 0 || i >= dp.length || j >= dp[0].length) {
        return defaultVal;
    }
    return dp[i][j];
}
```

---

## Interview Tips

### Communication Strategy

1. **Clarify the problem:**
   - "Is the grid always rectangular?"
   - "Can we modify the input?"
   - "Are there negative values?"

2. **Explain your approach:**
   - "I'll use a 2D DP table where dp[i][j] represents..."
   - "The recurrence relation is..."
   - "Base cases are..."

3. **Discuss optimization:**
   - "We can optimize space from O(m*n) to O(n)"
   - "If we only need the final result, we don't need to store the entire table"

### Common Follow-ups

- "Can you optimize the space complexity?"
- "Can you print the actual path/solution, not just the value?"
- "What if the grid is very large?"
- "Can you solve it with recursion + memoization instead?"

---

## Debugging 2D DP

### Print the DP Table

```typescript
function printDP(dp: number[][]): void {
    for (const row of dp) {
        console.log(row.map(x => x.toString().padStart(3)).join(' '));
    }
}
```

### Common Issues

1. **Off-by-one errors:** Check if you need m+1 or m rows
2. **Base case initialization:** Ensure all necessary cells are initialized
3. **Index confusion:** Be clear about what dp[i][j] represents
4. **Direction of filling:** Some problems require reverse order

---

## Practice Strategy

### Beginner (Start Here)
1. Unique Paths - Basic grid traversal
2. Minimum Path Sum - Path optimization
3. Triangle - Different grid shape

### Intermediate
4. Longest Common Subsequence - String comparison
5. Edit Distance - Classic DP
6. Maximal Square - Area optimization

### Advanced
7. Interleaving String - Complex string matching
8. Distinct Subsequences - Counting patterns
9. Regular Expression Matching - Pattern matching

### Order of Study
1. Grid problems first (easier to visualize)
2. String problems next (build on concepts)
3. Complex patterns last (combine techniques)

---

## Key Takeaways

1. **2D DP extends 1D concepts** - Same principles, more dimensions
2. **Visualization helps** - Draw the table and trace through
3. **Space can often be optimized** - Don't always need full matrix
4. **Practice standard patterns** - Grid, string, interval
5. **Base cases are critical** - Many bugs come from incorrect initialization

---

## Next Steps

After watching the videos and understanding these concepts:
1. Start with Problem 1 (Unique Paths) in PROBLEMS.md
2. Try to solve it yourself first
3. Use HINTS.md if stuck
4. Review SOLUTIONS.md for optimization ideas
5. Practice with Claude using INTERVIEWER-SCRIPT.md

Remember: Understanding the pattern is more important than memorizing solutions!