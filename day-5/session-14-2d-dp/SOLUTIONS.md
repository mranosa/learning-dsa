# Solutions - Session 14: 2D Dynamic Programming

TypeScript solutions with complexity analysis.

---

## Problem 1: Unique Paths

### Approach 1: Standard 2D DP

```typescript
function uniquePaths(m: number, n: number): number {
  const dp: number[][] = Array(m).fill(0).map(() => Array(n).fill(1));

  // First row and column already filled with 1s

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = dp[i-1][j] + dp[i][j-1];
    }
  }

  return dp[m-1][n-1];
}
```

**Time:** O(m×n) | **Space:** O(m×n)

---

### Approach 2: Space Optimized (Optimal) ✅

```typescript
function uniquePaths(m: number, n: number): number {
  const dp: number[] = new Array(n).fill(1);

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[j] = dp[j] + dp[j-1];
    }
  }

  return dp[n-1];
}
```

**Time:** O(m×n) | **Space:** O(n)

**Key:** Only need previous row. Update in-place left-to-right.

**Say:** "Using 1D array since we only need previous row values. dp[j] represents paths to current position."

---

## Problem 2: Unique Paths II

```typescript
function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
  const m = obstacleGrid.length;
  const n = obstacleGrid[0].length;

  if (obstacleGrid[0][0] === 1 || obstacleGrid[m-1][n-1] === 1) {
    return 0;
  }

  const dp: number[][] = Array(m).fill(0).map(() => Array(n).fill(0));
  dp[0][0] = 1;

  // First column
  for (let i = 1; i < m; i++) {
    dp[i][0] = obstacleGrid[i][0] === 1 ? 0 : dp[i-1][0];
  }

  // First row
  for (let j = 1; j < n; j++) {
    dp[0][j] = obstacleGrid[0][j] === 1 ? 0 : dp[0][j-1];
  }

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (obstacleGrid[i][j] === 1) {
        dp[i][j] = 0;
      } else {
        dp[i][j] = dp[i-1][j] + dp[i][j-1];
      }
    }
  }

  return dp[m-1][n-1];
}
```

**Time:** O(m×n) | **Space:** O(m×n)

**Key:** Obstacle = 0 paths. Once blocked in first row/col, all after blocked.

---

## Problem 3: Longest Common Subsequence

### Approach 1: Standard 2D DP

```typescript
function longestCommonSubsequence(text1: string, text2: string): number {
  const m = text1.length;
  const n = text2.length;
  const dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (text1[i-1] === text2[j-1]) {
        dp[i][j] = dp[i-1][j-1] + 1;
      } else {
        dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
      }
    }
  }

  return dp[m][n];
}
```

**Time:** O(m×n) | **Space:** O(m×n)

---

### Approach 2: Space Optimized ✅

```typescript
function longestCommonSubsequence(text1: string, text2: string): number {
  if (text1.length < text2.length) {
    [text1, text2] = [text2, text1];
  }

  const n = text2.length;
  let prev = new Array(n + 1).fill(0);
  let curr = new Array(n + 1).fill(0);

  for (let i = 1; i <= text1.length; i++) {
    for (let j = 1; j <= n; j++) {
      if (text1[i-1] === text2[j-1]) {
        curr[j] = prev[j-1] + 1;
      } else {
        curr[j] = Math.max(prev[j], curr[j-1]);
      }
    }
    [prev, curr] = [curr, prev];
  }

  return prev[n];
}
```

**Time:** O(m×n) | **Space:** O(min(m,n))

**Key:** Match → diagonal+1. No match → max(exclude from each string).

**Say:** "LCS is classic 2D DP. If characters match, extend previous LCS. Otherwise, take max of excluding one character from either string."

---

## Problem 4: Edit Distance

### Approach: 2D DP (Optimal) ✅

```typescript
function minDistance(word1: string, word2: string): number {
  const m = word1.length;
  const n = word2.length;
  const dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

  // Base cases
  for (let i = 0; i <= m; i++) dp[i][0] = i;
  for (let j = 0; j <= n; j++) dp[0][j] = j;

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (word1[i-1] === word2[j-1]) {
        dp[i][j] = dp[i-1][j-1];
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

**Key:** Three operations - take minimum. Match = no cost.

**Say:** "Edit distance uses 3 operations. Delete moves up, insert moves left, replace moves diagonal. Take minimum + 1."

---

## Problem 5: Minimum Path Sum

### Approach 1: Standard DP

```typescript
function minPathSum(grid: number[][]): number {
  const m = grid.length;
  const n = grid[0].length;
  const dp: number[][] = Array(m).fill(0).map(() => Array(n).fill(0));

  dp[0][0] = grid[0][0];

  for (let i = 1; i < m; i++) {
    dp[i][0] = dp[i-1][0] + grid[i][0];
  }

  for (let j = 1; j < n; j++) {
    dp[0][j] = dp[0][j-1] + grid[0][j];
  }

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
    }
  }

  return dp[m-1][n-1];
}
```

**Time:** O(m×n) | **Space:** O(m×n)

---

### Approach 2: In-Place (Optimal) ✅

```typescript
function minPathSum(grid: number[][]): number {
  const m = grid.length;
  const n = grid[0].length;

  for (let i = 1; i < m; i++) {
    grid[i][0] += grid[i-1][0];
  }

  for (let j = 1; j < n; j++) {
    grid[0][j] += grid[0][j-1];
  }

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      grid[i][j] += Math.min(grid[i-1][j], grid[i][j-1]);
    }
  }

  return grid[m-1][n-1];
}
```

**Time:** O(m×n) | **Space:** O(1)

**Key:** Modify input to save space. Choose minimum path from top/left.

---

## Problem 6: Maximal Square

```typescript
function maximalSquare(matrix: string[][]): number {
  if (!matrix.length || !matrix[0].length) return 0;

  const m = matrix.length;
  const n = matrix[0].length;
  const dp: number[][] = Array(m).fill(0).map(() => Array(n).fill(0));
  let maxSide = 0;

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (matrix[i][j] === '1') {
        if (i === 0 || j === 0) {
          dp[i][j] = 1;
        } else {
          dp[i][j] = Math.min(
            dp[i-1][j],
            dp[i][j-1],
            dp[i-1][j-1]
          ) + 1;
        }
        maxSide = Math.max(maxSide, dp[i][j]);
      }
    }
  }

  return maxSide * maxSide;
}
```

**Time:** O(m×n) | **Space:** O(m×n)

**Key:** Square size at (i,j) = min of three neighbors + 1.

**Say:** "For each cell as bottom-right of square, check top, left, and diagonal. Min of those determines largest square possible here."

---

## Problem 7: Triangle

### Approach: Bottom-Up (Optimal) ✅

```typescript
function minimumTotal(triangle: number[][]): number {
  const n = triangle.length;
  const dp = [...triangle[n-1]];

  for (let i = n - 2; i >= 0; i--) {
    for (let j = 0; j <= i; j++) {
      dp[j] = Math.min(dp[j], dp[j+1]) + triangle[i][j];
    }
  }

  return dp[0];
}
```

**Time:** O(n²) | **Space:** O(n)

**Key:** Work bottom-up. At each position, choose min of two paths below.

**Say:** "Starting from bottom, work upward. For each position, choose minimum of two adjacent positions below and add current value."

---

## Problem 8: Interleaving String

```typescript
function isInterleave(s1: string, s2: string, s3: string): boolean {
  const m = s1.length;
  const n = s2.length;

  if (m + n !== s3.length) return false;

  const dp: boolean[][] = Array(m + 1).fill(false)
    .map(() => Array(n + 1).fill(false));

  dp[0][0] = true;

  for (let i = 1; i <= m; i++) {
    dp[i][0] = dp[i-1][0] && s1[i-1] === s3[i-1];
  }

  for (let j = 1; j <= n; j++) {
    dp[0][j] = dp[0][j-1] && s2[j-1] === s3[j-1];
  }

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      const k = i + j - 1;
      dp[i][j] = (dp[i-1][j] && s1[i-1] === s3[k]) ||
                 (dp[i][j-1] && s2[j-1] === s3[k]);
    }
  }

  return dp[m][n];
}
```

**Time:** O(m×n) | **Space:** O(m×n)

**Key:** Can use character from s1 or s2. Must match s3 at position i+j-1.

---

## Problem 9: Distinct Subsequences

```typescript
function numDistinct(s: string, t: string): number {
  const m = s.length;
  const n = t.length;
  const dp: number[][] = Array(m + 1).fill(0)
    .map(() => Array(n + 1).fill(0));

  for (let i = 0; i <= m; i++) {
    dp[i][0] = 1;
  }

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      dp[i][j] = dp[i-1][j];

      if (s[i-1] === t[j-1]) {
        dp[i][j] += dp[i-1][j-1];
      }
    }
  }

  return dp[m][n];
}
```

**Time:** O(m×n) | **Space:** O(m×n)

**Key:** Always can skip current char. If match, add count using match.

**Say:** "Count subsequences. Always option to skip character. If characters match, add ways using this match to ways skipping it."

---

## Problem 10: Regular Expression Matching

```typescript
function isMatch(s: string, p: string): boolean {
  const m = s.length;
  const n = p.length;
  const dp: boolean[][] = Array(m + 1).fill(false)
    .map(() => Array(n + 1).fill(false));

  dp[0][0] = true;

  for (let j = 2; j <= n; j += 2) {
    if (p[j-1] === '*') {
      dp[0][j] = dp[0][j-2];
    }
  }

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (p[j-1] === '*') {
        dp[i][j] = dp[i][j-2];

        if (p[j-2] === '.' || p[j-2] === s[i-1]) {
          dp[i][j] = dp[i][j] || dp[i-1][j];
        }
      } else if (p[j-1] === '.' || p[j-1] === s[i-1]) {
        dp[i][j] = dp[i-1][j-1];
      }
    }
  }

  return dp[m][n];
}
```

**Time:** O(m×n) | **Space:** O(m×n)

**Key:** Star matches 0 or more. '.' matches any character.

**Say:** "For '*', try matching 0 occurrences first. If preceding char matches current, also try matching 1+ occurrences."

---

## Pattern Summary

### Grid Traversal (Problems 1, 2, 5, 6, 7)
- State: dp[i][j] = result at position (i,j)
- Transition: Combine top and left (or diagonal)
- Base: First row/column
- Space: Can optimize to O(n) or O(1)

### String Comparison (Problems 3, 4, 8, 9, 10)
- State: dp[i][j] = result for s1[0..i-1] and s2[0..j-1]
- Size: (m+1) × (n+1) for empty string base
- Match: Usually dp[i-1][j-1] + something
- No match: Usually max/min of excluding one char

### Optimization Tricks
1. **Rolling array:** Keep only prev and curr rows
2. **Single array:** Update in-place when safe
3. **In-place:** Modify input when allowed
4. **Swap strings:** Process smaller dimension

---

[Back to Problems](./PROBLEMS.md) | [Back to README](./README.md)
