# Session 14: 2D Dynamic Programming Solutions

## Problem 1: Unique Paths

### Approach 1: Dynamic Programming (Bottom-up)
```typescript
function uniquePaths(m: number, n: number): number {
    // Create DP table
    const dp: number[][] = Array(m).fill(0).map(() => Array(n).fill(0));

    // Base case: First row and column have only one way to reach
    for (let i = 0; i < m; i++) dp[i][0] = 1;
    for (let j = 0; j < n; j++) dp[0][j] = 1;

    // Fill the DP table
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            // Can reach current cell from top or left
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
        }
    }

    return dp[m-1][n-1];
}
```
**Time Complexity:** O(m × n)
**Space Complexity:** O(m × n)

### Approach 2: Space Optimized DP
```typescript
function uniquePathsOptimized(m: number, n: number): number {
    // Only need previous row to calculate current row
    const dp: number[] = new Array(n).fill(1);

    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            dp[j] = dp[j] + dp[j-1];
        }
    }

    return dp[n-1];
}
```
**Time Complexity:** O(m × n)
**Space Complexity:** O(n)

### Approach 3: Math (Combinatorics)
```typescript
function uniquePathsMath(m: number, n: number): number {
    // Total moves: (m-1) down + (n-1) right = m + n - 2
    // Choose (m-1) positions for down moves: C(m+n-2, m-1)
    const totalMoves = m + n - 2;
    const downMoves = m - 1;

    let result = 1;
    for (let i = 1; i <= downMoves; i++) {
        result = result * (totalMoves - downMoves + i) / i;
    }

    return Math.round(result);
}
```
**Time Complexity:** O(min(m, n))
**Space Complexity:** O(1)

---

## Problem 2: Unique Paths II

### Approach 1: Dynamic Programming
```typescript
function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
    const m = obstacleGrid.length;
    const n = obstacleGrid[0].length;

    // If start or end is blocked, return 0
    if (obstacleGrid[0][0] === 1 || obstacleGrid[m-1][n-1] === 1) {
        return 0;
    }

    const dp: number[][] = Array(m).fill(0).map(() => Array(n).fill(0));
    dp[0][0] = 1;

    // Initialize first column
    for (let i = 1; i < m; i++) {
        dp[i][0] = obstacleGrid[i][0] === 1 ? 0 : dp[i-1][0];
    }

    // Initialize first row
    for (let j = 1; j < n; j++) {
        dp[0][j] = obstacleGrid[0][j] === 1 ? 0 : dp[0][j-1];
    }

    // Fill the DP table
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
**Time Complexity:** O(m × n)
**Space Complexity:** O(m × n)

### Approach 2: Space Optimized
```typescript
function uniquePathsWithObstaclesOptimized(obstacleGrid: number[][]): number {
    const n = obstacleGrid[0].length;
    const dp: number[] = new Array(n).fill(0);
    dp[0] = 1;

    for (const row of obstacleGrid) {
        for (let j = 0; j < n; j++) {
            if (row[j] === 1) {
                dp[j] = 0;
            } else if (j > 0) {
                dp[j] = dp[j] + dp[j-1];
            }
        }
    }

    return dp[n-1];
}
```
**Time Complexity:** O(m × n)
**Space Complexity:** O(n)

---

## Problem 3: Longest Common Subsequence

### Approach 1: 2D Dynamic Programming
```typescript
function longestCommonSubsequence(text1: string, text2: string): number {
    const m = text1.length;
    const n = text2.length;
    const dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (text1[i-1] === text2[j-1]) {
                // Characters match, extend the LCS
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                // Take max of excluding one character from either string
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }

    return dp[m][n];
}
```
**Time Complexity:** O(m × n)
**Space Complexity:** O(m × n)

### Approach 2: Space Optimized
```typescript
function longestCommonSubsequenceOptimized(text1: string, text2: string): number {
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
**Time Complexity:** O(m × n)
**Space Complexity:** O(min(m, n))

---

## Problem 4: Edit Distance

### Approach 1: Dynamic Programming
```typescript
function minDistance(word1: string, word2: string): number {
    const m = word1.length;
    const n = word2.length;
    const dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

    // Base cases: converting to/from empty string
    for (let i = 0; i <= m; i++) dp[i][0] = i;
    for (let j = 0; j <= n; j++) dp[0][j] = j;

    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (word1[i-1] === word2[j-1]) {
                // Characters match, no operation needed
                dp[i][j] = dp[i-1][j-1];
            } else {
                // Min of three operations
                dp[i][j] = 1 + Math.min(
                    dp[i-1][j],    // Delete from word1
                    dp[i][j-1],    // Insert to word1
                    dp[i-1][j-1]   // Replace in word1
                );
            }
        }
    }

    return dp[m][n];
}
```
**Time Complexity:** O(m × n)
**Space Complexity:** O(m × n)

### Approach 2: Space Optimized
```typescript
function minDistanceOptimized(word1: string, word2: string): number {
    const n = word2.length;
    let prev = Array.from({length: n + 1}, (_, i) => i);
    let curr = new Array(n + 1).fill(0);

    for (let i = 1; i <= word1.length; i++) {
        curr[0] = i;
        for (let j = 1; j <= n; j++) {
            if (word1[i-1] === word2[j-1]) {
                curr[j] = prev[j-1];
            } else {
                curr[j] = 1 + Math.min(prev[j], curr[j-1], prev[j-1]);
            }
        }
        [prev, curr] = [curr, prev];
    }

    return prev[n];
}
```
**Time Complexity:** O(m × n)
**Space Complexity:** O(n)

---

## Problem 5: Minimum Path Sum

### Approach 1: Dynamic Programming
```typescript
function minPathSum(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const dp: number[][] = Array(m).fill(0).map(() => Array(n).fill(0));

    // Initialize starting point
    dp[0][0] = grid[0][0];

    // Initialize first column
    for (let i = 1; i < m; i++) {
        dp[i][0] = dp[i-1][0] + grid[i][0];
    }

    // Initialize first row
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
**Time Complexity:** O(m × n)
**Space Complexity:** O(m × n)

### Approach 2: In-place Modification
```typescript
function minPathSumInPlace(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;

    // Modify first column
    for (let i = 1; i < m; i++) {
        grid[i][0] += grid[i-1][0];
    }

    // Modify first row
    for (let j = 1; j < n; j++) {
        grid[0][j] += grid[0][j-1];
    }

    // Fill the rest
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            grid[i][j] += Math.min(grid[i-1][j], grid[i][j-1]);
        }
    }

    return grid[m-1][n-1];
}
```
**Time Complexity:** O(m × n)
**Space Complexity:** O(1)

---

## Problem 6: Maximal Square

### Approach: Dynamic Programming
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
                    // Edge cells can only form 1x1 square
                    dp[i][j] = 1;
                } else {
                    // Min of three neighbors + 1
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
**Time Complexity:** O(m × n)
**Space Complexity:** O(m × n)

---

## Problem 7: Triangle

### Approach 1: Top-Down DP
```typescript
function minimumTotal(triangle: number[][]): number {
    const n = triangle.length;
    const dp: number[][] = [];

    // Initialize with first element
    dp[0] = [triangle[0][0]];

    for (let i = 1; i < n; i++) {
        dp[i] = new Array(triangle[i].length);
        for (let j = 0; j < triangle[i].length; j++) {
            if (j === 0) {
                // Leftmost element
                dp[i][j] = dp[i-1][j] + triangle[i][j];
            } else if (j === triangle[i].length - 1) {
                // Rightmost element
                dp[i][j] = dp[i-1][j-1] + triangle[i][j];
            } else {
                // Middle elements
                dp[i][j] = Math.min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j];
            }
        }
    }

    return Math.min(...dp[n-1]);
}
```
**Time Complexity:** O(n²)
**Space Complexity:** O(n²)

### Approach 2: Bottom-Up (Space Optimized)
```typescript
function minimumTotalOptimized(triangle: number[][]): number {
    const n = triangle.length;
    // Start from the bottom row
    const dp = [...triangle[n-1]];

    // Move upwards
    for (let i = n - 2; i >= 0; i--) {
        for (let j = 0; j <= i; j++) {
            dp[j] = Math.min(dp[j], dp[j+1]) + triangle[i][j];
        }
    }

    return dp[0];
}
```
**Time Complexity:** O(n²)
**Space Complexity:** O(n)

---

## Problem 8: Interleaving String

### Approach: 2D Dynamic Programming
```typescript
function isInterleave(s1: string, s2: string, s3: string): boolean {
    const m = s1.length;
    const n = s2.length;

    if (m + n !== s3.length) return false;

    const dp: boolean[][] = Array(m + 1).fill(false)
        .map(() => Array(n + 1).fill(false));

    dp[0][0] = true;

    // Initialize first column (using only s1)
    for (let i = 1; i <= m; i++) {
        dp[i][0] = dp[i-1][0] && s1[i-1] === s3[i-1];
    }

    // Initialize first row (using only s2)
    for (let j = 1; j <= n; j++) {
        dp[0][j] = dp[0][j-1] && s2[j-1] === s3[j-1];
    }

    // Fill the DP table
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            const k = i + j - 1; // Index in s3
            // Check if we can use s1[i-1] or s2[j-1]
            dp[i][j] = (dp[i-1][j] && s1[i-1] === s3[k]) ||
                      (dp[i][j-1] && s2[j-1] === s3[k]);
        }
    }

    return dp[m][n];
}
```
**Time Complexity:** O(m × n)
**Space Complexity:** O(m × n)

---

## Problem 9: Distinct Subsequences

### Approach: Dynamic Programming
```typescript
function numDistinct(s: string, t: string): number {
    const m = s.length;
    const n = t.length;
    const dp: number[][] = Array(m + 1).fill(0)
        .map(() => Array(n + 1).fill(0));

    // Empty t can be formed from any s by deleting all chars
    for (let i = 0; i <= m; i++) {
        dp[i][0] = 1;
    }

    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            // Always can skip current character in s
            dp[i][j] = dp[i-1][j];

            // If characters match, add the count of using this match
            if (s[i-1] === t[j-1]) {
                dp[i][j] += dp[i-1][j-1];
            }
        }
    }

    return dp[m][n];
}
```
**Time Complexity:** O(m × n)
**Space Complexity:** O(m × n)

---

## Problem 10: Regular Expression Matching

### Approach: Dynamic Programming
```typescript
function isMatch(s: string, p: string): boolean {
    const m = s.length;
    const n = p.length;
    const dp: boolean[][] = Array(m + 1).fill(false)
        .map(() => Array(n + 1).fill(false));

    // Empty pattern matches empty string
    dp[0][0] = true;

    // Handle patterns like a*, a*b*, a*b*c*
    for (let j = 2; j <= n; j += 2) {
        if (p[j-1] === '*') {
            dp[0][j] = dp[0][j-2];
        }
    }

    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (p[j-1] === '*') {
                // Star can match 0 or more of preceding element
                dp[i][j] = dp[i][j-2]; // Match 0 occurrences

                // Check if we can match 1 or more occurrences
                if (p[j-2] === '.' || p[j-2] === s[i-1]) {
                    dp[i][j] = dp[i][j] || dp[i-1][j];
                }
            } else if (p[j-1] === '.' || p[j-1] === s[i-1]) {
                // Direct match or dot match
                dp[i][j] = dp[i-1][j-1];
            }
        }
    }

    return dp[m][n];
}
```
**Time Complexity:** O(m × n)
**Space Complexity:** O(m × n)