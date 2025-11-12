# Lesson: 2D Dynamic Programming

---

## 📹 Video 1: 2D DP Fundamentals (15 min)

**"2D Dynamic Programming Introduction" by NeetCode**
https://www.youtube.com/watch?v=cJ24x7lLies

**Focus on:**
- What makes a problem 2D DP
- State representation with two variables
- Building DP tables
- Base case initialization

---

## 📹 Video 2: Grid Traversal (12 min)

**"Unique Paths Explanation" by NeetCode**
https://www.youtube.com/watch?v=IlEsdxuD4lY

**Focus on:**
- Grid path counting
- Coming from top/left only
- Path sum optimization
- Space optimization tricks

---

## 📹 Video 3: String DP Patterns (18 min)

**"Longest Common Subsequence" by NeetCode**
https://www.youtube.com/watch?v=Ua0GhsJSlWM

**Focus on:**
- Comparing two strings
- Match vs mismatch cases
- Building LCS table
- Understanding diagonal transitions

---

## 📹 Video 4: Edit Distance (20 min)

**"Edit Distance (Levenshtein)" by NeetCode**
https://www.youtube.com/watch?v=XYi2-LPrwm4

**Focus on:**
- Insert, delete, replace operations
- Choosing minimum cost
- String transformation
- Space optimization

---

## 📹 Video 5: Regular Expression Matching (25 min)

**"Regular Expression Matching" by NeetCode**
https://www.youtube.com/watch?v=l3K8lrAOmU0

**Focus on:**
- Handling wildcards (. and *)
- Star matches 0 or more
- Complex state transitions
- Edge case handling

---

## 🎯 2D DP: Core Patterns

### Pattern 1: Grid Traversal

Used when: Path counting, min/max path problems.

```typescript
// Grid path counting
function uniquePaths(m: number, n: number): number {
  const dp: number[][] = Array(m).fill(0).map(() => Array(n).fill(1));

  // Base: First row and column all 1s (only one way)
  // Already filled with 1s above

  // Fill table
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = dp[i-1][j] + dp[i][j-1];
    }
  }

  return dp[m-1][n-1];
}
```

**Time:** O(m×n) | **Space:** O(m×n)

**Key:** Can reach cell from top or left. Sum both ways.

---

### Pattern 2: Minimum Path Sum

```typescript
function minPathSum(grid: number[][]): number {
  const m = grid.length;
  const n = grid[0].length;
  const dp: number[][] = Array(m).fill(0).map(() => Array(n).fill(0));

  // Base cases
  dp[0][0] = grid[0][0];

  // First column
  for (let i = 1; i < m; i++) {
    dp[i][0] = dp[i-1][0] + grid[i][0];
  }

  // First row
  for (let j = 1; j < n; j++) {
    dp[0][j] = dp[0][j-1] + grid[0][j];
  }

  // Fill table
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
    }
  }

  return dp[m-1][n-1];
}
```

**Time:** O(m×n) | **Space:** O(m×n)

**Key:** Choose min cost from top/left, add current cell.

---

### Pattern 3: String Comparison (LCS)

**📹 Review:** [LCS video above](https://www.youtube.com/watch?v=Ua0GhsJSlWM) (~18 min)

Used when: Finding common subsequences, comparing strings.

```typescript
function longestCommonSubsequence(text1: string, text2: string): number {
  const m = text1.length;
  const n = text2.length;
  // Extra row/col for empty string
  const dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (text1[i-1] === text2[j-1]) {
        // Match: extend LCS
        dp[i][j] = dp[i-1][j-1] + 1;
      } else {
        // No match: take max of excluding one char
        dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
      }
    }
  }

  return dp[m][n];
}
```

**Time:** O(m×n) | **Space:** O(m×n)

**Key:** Match → diagonal + 1. No match → max(top, left).

---

### Pattern 4: Edit Distance

**📹 Review:** [Edit Distance video above](https://www.youtube.com/watch?v=XYi2-LPrwm4) (~20 min)

Used when: String transformation, minimum operations.

```typescript
function editDistance(word1: string, word2: string): number {
  const m = word1.length;
  const n = word2.length;
  const dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

  // Base: empty string conversions
  for (let i = 0; i <= m; i++) dp[i][0] = i;  // Delete all
  for (let j = 0; j <= n; j++) dp[0][j] = j;  // Insert all

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (word1[i-1] === word2[j-1]) {
        dp[i][j] = dp[i-1][j-1];  // No operation
      } else {
        dp[i][j] = 1 + Math.min(
          dp[i-1][j],    // Delete
          dp[i][j-1],    // Insert
          dp[i-1][j-1]   // Replace
        );
      }
    }
  }

  return dp[m][n];
}
```

**Time:** O(m×n) | **Space:** O(m×n)

**Key:** Three operations. Take minimum cost + 1.

---

## 🧩 Creating 2D Arrays in TypeScript

### Method 1: Fill + Map (Recommended)

```typescript
const dp: number[][] = Array(m).fill(0).map(() => Array(n).fill(0));
```

**Why map?** `fill()` creates references to same array!

```typescript
// ❌ WRONG - all rows reference same array!
const wrong = Array(3).fill(Array(3).fill(0));
wrong[0][0] = 1;  // Changes ALL rows!

// ✅ CORRECT - each row is new array
const correct = Array(3).fill(0).map(() => Array(3).fill(0));
correct[0][0] = 1;  // Only first row changes
```

---

### Method 2: Nested Loops

```typescript
const dp: number[][] = [];
for (let i = 0; i < m; i++) {
  dp[i] = new Array(n).fill(0);
}
```

---

### Method 3: Array.from

```typescript
const dp = Array.from({ length: m }, () => Array(n).fill(0));
```

---

## 💡 Space Optimization Techniques

### Technique 1: Rolling Array (Two Rows)

**Before:** O(m×n) space
```typescript
const dp: number[][] = Array(m).fill(0).map(() => Array(n).fill(0));
```

**After:** O(n) space
```typescript
let prev = new Array(n).fill(0);
let curr = new Array(n).fill(0);

for (let i = 0; i < m; i++) {
  for (let j = 0; j < n; j++) {
    curr[j] = /* calculate using prev */;
  }
  [prev, curr] = [curr, prev];  // Swap
}
```

**When to use:** Need values from previous row only.

---

### Technique 2: Single Array

```typescript
const dp: number[] = new Array(n).fill(1);

for (let i = 1; i < m; i++) {
  for (let j = 1; j < n; j++) {
    dp[j] = dp[j] + dp[j-1];
  }
}
```

**When to use:** Can overwrite as you go left-to-right.

---

### Technique 3: In-Place Modification

```typescript
function minPathSum(grid: number[][]): number {
  const m = grid.length, n = grid[0].length;

  for (let i = 1; i < m; i++) grid[i][0] += grid[i-1][0];
  for (let j = 1; j < n; j++) grid[0][j] += grid[0][j-1];

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      grid[i][j] += Math.min(grid[i-1][j], grid[i][j-1]);
    }
  }

  return grid[m-1][n-1];
}
```

**Time:** O(m×n) | **Space:** O(1)

**When to use:** Allowed to modify input.

---

## 📊 Complexity Analysis

### Common 2D DP Complexities

| Approach | Time | Space | Example |
|----------|------|-------|---------|
| Standard 2D DP | O(m×n) | O(m×n) | Full DP table |
| Rolling array | O(m×n) | O(n) | Two rows only |
| Single array | O(m×n) | O(n) | One row only |
| In-place | O(m×n) | O(1) | Modify input |

---

## 🎯 State Definition Guide

### Grid Problems

```typescript
// dp[i][j] = number of paths to reach (i, j)
// dp[i][j] = minimum cost to reach (i, j)
// dp[i][j] = maximum value at (i, j)
```

**Base:** First row/column based on problem.

---

### String Problems

```typescript
// dp[i][j] = LCS of s1[0..i-1] and s2[0..j-1]
// dp[i][j] = edit distance for s1[0..i-1] to s2[0..j-1]
// dp[i][j] = true if s1[0..i-1] matches pattern s2[0..j-1]
```

**Base:** Row/column 0 for empty string.

---

## 🔧 TypeScript 2D Array Helpers

```typescript
// Check if position valid
function isValid(row: number, col: number, m: number, n: number): boolean {
  return row >= 0 && row < m && col >= 0 && col < n;
}

// Get value with default
function getValue(dp: number[][], i: number, j: number, defaultVal = 0): number {
  if (i < 0 || j < 0) return defaultVal;
  return dp[i][j];
}

// Print DP table (debugging)
function printDP(dp: number[][]): void {
  console.log('DP Table:');
  for (const row of dp) {
    console.log(row.map(x => x.toString().padStart(4)).join(' '));
  }
}

// Clone 2D array
function clone2D(arr: number[][]): number[][] {
  return arr.map(row => [...row]);
}
```

---

## 💡 Interview Tips

### Communication Strategy

**Say this:**
- "I'll use 2D DP where dp[i][j] represents..."
- "Base cases are first row and column..."
- "Recurrence relation: if match, take diagonal + 1..."
- "Time is O(m×n) for filling table, space O(m×n) but can optimize to O(n)"

**Show thinking:**
- "Let me draw the DP table for small example"
- "I'll trace through (0,0) to (2,2)"
- "I can optimize space by keeping only previous row"

---

### Common Follow-ups

**Q:** "Can you optimize space?"
**A:** "Yes, we only need previous row. Use rolling array for O(n) space."

**Q:** "Can you print the actual path/LCS?"
**A:** "Yes, backtrack from dp[m][n] to dp[0][0] following decisions."

**Q:** "What if grid is very large?"
**A:** "Consider space optimization. Maybe process in chunks. Depends on constraints."

---

## 🐛 Common Bugs and Fixes

### Bug 1: Off-by-One

```typescript
// ❌ Wrong
for (let i = 0; i <= m; i++)  // Should be < m for 0-indexed

// ✅ Correct
for (let i = 0; i < m; i++)    // For dp[m][n]
for (let i = 1; i <= m; i++)   // For dp[m+1][n+1] (string problems)
```

---

### Bug 2: Base Case

```typescript
// ❌ Wrong - forgot first row/column
dp[0][0] = grid[0][0];
// Missing initialization!

// ✅ Correct
dp[0][0] = grid[0][0];
for (let i = 1; i < m; i++) dp[i][0] = dp[i-1][0] + grid[i][0];
for (let j = 1; j < n; j++) dp[0][j] = dp[0][j-1] + grid[0][j];
```

---

### Bug 3: Index Confusion

```typescript
// When dp is (m+1) × (n+1) for strings
if (text1[i-1] === text2[j-1])  // ✅ Correct - array is 0-indexed
if (text1[i] === text2[j])      // ❌ Wrong - would skip first char
```

**Rule:** If `dp` has size (m+1)×(n+1), access string at `[i-1]` and `[j-1]`.

---

### Bug 4: Fill Array Reference

```typescript
// ❌ WRONG - creates references to SAME array
const dp = Array(m).fill(Array(n).fill(0));

// ✅ CORRECT - creates NEW array for each row
const dp = Array(m).fill(0).map(() => Array(n).fill(0));
```

---

## 📈 Pattern Recognition

### How to Know It's 2D DP

**Grid/Matrix:**
- "Find paths from top-left to bottom-right"
- "Minimum/maximum path sum"
- "Count ways to reach destination"

**Two Strings:**
- "Longest common subsequence"
- "Edit distance"
- "String matching/interleaving"

**Two Variables:**
- "First i items and capacity j"
- "Position i with state j"

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **Grid DP:** dp[i][j] = f(top, left)
- **String DP:** Match → diagonal+1, No match → max(top, left)
- **Edit Distance:** min(insert, delete, replace) + 1
- **Space:** Can usually optimize to O(n)

**Complexity Targets:**
- Time: O(m×n) is expected
- Space: O(m×n) standard, O(n) optimized, O(1) in-place

---

[Back to Session README](./README.md)
