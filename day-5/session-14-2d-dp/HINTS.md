# Hints - Session 14: 2D Dynamic Programming

Progressive hints for 10 problems. Struggle first - it builds understanding.

---

## Problem 1: Unique Paths

### Level 1
How many ways can you reach any cell? Where can you come from?

### Level 2
Can only arrive from top or left. dp[i][j] = paths from (i-1,j) + paths from (i,j-1).

### Level 3
```typescript
const dp: number[][] = Array(m).fill(0).map(() => Array(n).fill(1));
for (let i = 1; i < m; i++) {
  for (let j = 1; j < n; j++) {
    dp[i][j] = dp[i-1][j] + dp[i][j-1];
  }
}
```

---

## Problem 2: Unique Paths II

### Level 1
Same as Unique Paths, but some cells blocked. What happens at obstacle?

### Level 2
If obstacle at (i,j), dp[i][j] = 0. Careful with first row/column - once blocked, all after blocked.

### Level 3
```typescript
if (obstacleGrid[i][j] === 1) {
  dp[i][j] = 0;
} else {
  dp[i][j] = dp[i-1][j] + dp[i][j-1];
}
// First row: dp[0][j] = obstacleGrid[0][j] === 1 ? 0 : dp[0][j-1]
```

---

## Problem 3: Longest Common Subsequence

### Level 1
When characters match vs don't match - what happens to LCS?

### Level 2
Match: extend LCS by 1 (diagonal + 1). No match: take max of excluding one char.

### Level 3
```typescript
const dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));
if (text1[i-1] === text2[j-1]) {
  dp[i][j] = dp[i-1][j-1] + 1;
} else {
  dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
}
```

---

## Problem 4: Edit Distance

### Level 1
Three operations: insert, delete, replace. How does each change the problem?

### Level 2
If match, no operation needed. If not, try all 3 and take minimum + 1.

### Level 3
```typescript
if (word1[i-1] === word2[j-1]) {
  dp[i][j] = dp[i-1][j-1];
} else {
  dp[i][j] = 1 + Math.min(
    dp[i-1][j],    // Delete
    dp[i][j-1],    // Insert
    dp[i-1][j-1]   // Replace
  );
}
// Base: dp[i][0] = i, dp[0][j] = j
```

---

## Problem 5: Minimum Path Sum

### Level 1
At each cell, what's the minimum cost to reach it? Where can you come from?

### Level 2
Come from top or left. Choose minimum path and add current cell value.

### Level 3
```typescript
dp[0][0] = grid[0][0];
// First row/col with cumulative sums
for (let i = 1; i < m; i++) dp[i][0] = dp[i-1][0] + grid[i][0];
for (let j = 1; j < n; j++) dp[0][j] = dp[0][j-1] + grid[0][j];
// Fill table
dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
```

---

## Problem 6: Maximal Square

### Level 1
For each '1', what's the largest square with this as bottom-right corner?

### Level 2
Check three neighbors: top, left, diagonal. Take minimum and add 1.

### Level 3
```typescript
if (matrix[i][j] === '1') {
  if (i === 0 || j === 0) {
    dp[i][j] = 1;
  } else {
    dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1;
  }
  maxSide = Math.max(maxSide, dp[i][j]);
}
return maxSide * maxSide;
```

---

## Problem 7: Triangle

### Level 1
Top-down or bottom-up? Which is cleaner for irregular grid?

### Level 2
Bottom-up is easier. For each position, choose min of two adjacent positions below.

### Level 3
```typescript
const dp = [...triangle[n-1]];  // Start with last row
for (let i = n - 2; i >= 0; i--) {
  for (let j = 0; j <= i; j++) {
    dp[j] = Math.min(dp[j], dp[j+1]) + triangle[i][j];
  }
}
return dp[0];
```

---

## Problem 8: Interleaving String

### Level 1
At each step, choosing from s1 or s2. Must match s3. What's the state?

### Level 2
dp[i][j] = can first i+j chars of s3 be formed from s1[0..i-1] and s2[0..j-1]?

### Level 3
```typescript
if (m + n !== s3.length) return false;
const k = i + j - 1;  // Position in s3
dp[i][j] = (dp[i-1][j] && s1[i-1] === s3[k]) ||
           (dp[i][j-1] && s2[j-1] === s3[k]);
```

---

## Problem 9: Distinct Subsequences

### Level 1
For each character in s, two choices: use it to match t, or skip it.

### Level 2
Always can skip: dp[i][j] = dp[i-1][j]. If match, also add using match: += dp[i-1][j-1].

### Level 3
```typescript
dp[i][0] = 1;  // Empty t can always be formed
dp[i][j] = dp[i-1][j];  // Skip s[i-1]
if (s[i-1] === t[j-1]) {
  dp[i][j] += dp[i-1][j-1];  // Use match
}
```

---

## Problem 10: Regular Expression Matching

### Level 1
Star matches 0 or more. Try both: match 0, or match 1+ if chars compatible.

### Level 2
If p[j-1] === '*': try 0 matches (dp[i][j-2]) or 1+ matches (dp[i-1][j] if chars match).

### Level 3
```typescript
if (p[j-1] === '*') {
  dp[i][j] = dp[i][j-2];  // Match 0
  if (p[j-2] === '.' || p[j-2] === s[i-1]) {
    dp[i][j] = dp[i][j] || dp[i-1][j];  // Match 1+
  }
} else if (p[j-1] === '.' || p[j-1] === s[i-1]) {
  dp[i][j] = dp[i-1][j-1];
}
```

---

## Pattern Recognition Hints

### Grid Problems
- "Paths from top-left to bottom-right" → Grid DP
- "Can only move down/right" → dp[i][j] from top/left
- "Minimum/maximum path sum" → min/max of neighbors

### String Problems
- "Two strings" + "longest/shortest" → 2D DP
- "Common subsequence" → Match: diagonal+1, No match: max(top, left)
- "Edit distance" → Match: diagonal, No match: 1+min(3 ops)
- "Pattern matching" → Consider wildcards specially

### State Definition
- Grid: dp[i][j] = result at position (i, j)
- Strings: dp[i][j] = result for first i and j characters
- Extra row/col for empty string base case

---

## Common Mistakes

### Off-by-One
```typescript
// ❌ Wrong
for (let i = 0; i <= m; i++)  // Should be < m

// ✅ Correct
for (let i = 0; i < m; i++)    // Grid problems
for (let i = 1; i <= m; i++)   // String problems with (m+1)×(n+1)
```

### Array Reference Bug
```typescript
// ❌ WRONG - creates references to SAME array!
const dp = Array(m).fill(Array(n).fill(0));

// ✅ CORRECT
const dp = Array(m).fill(0).map(() => Array(n).fill(0));
```

### Index Confusion
```typescript
// When dp is (m+1) × (n+1)
if (text1[i-1] === text2[j-1])  // ✅ Access at i-1, j-1
if (text1[i] === text2[j])      // ❌ Would skip first char
```

### Forgot Base Cases
```typescript
// ❌ Missing initialization
dp[0][0] = grid[0][0];
// Need first row/col too!

// ✅ Complete base cases
dp[0][0] = grid[0][0];
for (let i = 1; i < m; i++) dp[i][0] = dp[i-1][0] + grid[i][0];
for (let j = 1; j < n; j++) dp[0][j] = dp[0][j-1] + grid[0][j];
```

---

## Using Hints Effectively

1. **Try 15+ min before Level 1**
   - Draw DP table on paper
   - Trace through small example
   - Think about state definition

2. **Try 10+ min after each hint**
   - Don't jump to next hint too quickly
   - Understand WHY the hint works

3. **If use Level 3, retry later**
   - Mark problem for review
   - Try similar problems
   - Goal is pattern recognition, not memorization

4. **Don't feel bad**
   - 2D DP is challenging
   - Hints are learning tools
   - Understanding > speed at this stage

---

## Quick Reference

**Grid DP:**
- State: dp[i][j] = value at (i,j)
- Base: First row/column
- Transition: From top/left

**String DP:**
- State: dp[i][j] = result for s1[0..i-1], s2[0..j-1]
- Size: (m+1) × (n+1)
- Match: Usually diagonal
- No match: Usually max/min of top/left

**Complexity:**
- Time: O(m×n) for filling table
- Space: O(m×n) standard, O(n) optimized, O(1) in-place

---

[Back to Problems](./PROBLEMS.md) | [Back to Solutions](./SOLUTIONS.md)
