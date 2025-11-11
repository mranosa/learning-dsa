# Session 14: 2D Dynamic Programming Hints

## Problem 1: Unique Paths

### Hint 1 (Gentle)
Think about how many ways you can reach any cell in the grid. Can you only arrive at a cell from specific directions?

### Hint 2 (Direct)
You can only reach a cell from the top or left. So the number of ways to reach cell (i,j) equals the sum of ways to reach (i-1,j) and (i,j-1).

### Hint 3 (Detailed)
Create a 2D DP table where dp[i][j] represents the number of unique paths to reach cell (i,j). Initialize the first row and column to 1 (only one way to reach those cells). Then fill the table using: dp[i][j] = dp[i-1][j] + dp[i][j-1].

---

## Problem 2: Unique Paths II

### Hint 1 (Gentle)
This is similar to Unique Paths, but now some cells are blocked. How does this affect the number of paths?

### Hint 2 (Direct)
If a cell has an obstacle, there are 0 ways to reach it. Otherwise, apply the same logic as Unique Paths: sum the ways from top and left.

### Hint 3 (Detailed)
Initialize dp[0][0] = 1 if no obstacle. For the first row and column, propagate the value only if there's no obstacle (once blocked, all subsequent cells in that row/column are unreachable). For other cells: if obstacle, dp[i][j] = 0; else dp[i][j] = dp[i-1][j] + dp[i][j-1].

---

## Problem 3: Longest Common Subsequence

### Hint 1 (Gentle)
Compare characters from both strings one by one. What happens when characters match vs when they don't?

### Hint 2 (Direct)
When characters match, you extend the LCS by 1. When they don't, you take the maximum LCS by excluding one character from either string.

### Hint 3 (Detailed)
Create dp[i][j] representing LCS of first i characters of text1 and first j characters of text2. If text1[i-1] == text2[j-1], then dp[i][j] = dp[i-1][j-1] + 1. Otherwise, dp[i][j] = max(dp[i-1][j], dp[i][j-1]). Initialize with 0s for empty strings.

---

## Problem 4: Edit Distance

### Hint 1 (Gentle)
You have three operations: insert, delete, replace. Think about how each operation changes the problem size.

### Hint 2 (Direct)
For each position, if characters match, no operation needed. If they don't, try all three operations and take the minimum cost.

### Hint 3 (Detailed)
dp[i][j] = minimum operations to convert first i chars of word1 to first j chars of word2. If word1[i-1] == word2[j-1], dp[i][j] = dp[i-1][j-1]. Otherwise, dp[i][j] = 1 + min(dp[i-1][j] for delete, dp[i][j-1] for insert, dp[i-1][j-1] for replace). Base cases: dp[i][0] = i, dp[0][j] = j.

---

## Problem 5: Minimum Path Sum

### Hint 1 (Gentle)
At each cell, you want the minimum sum to reach it. From which directions can you arrive at a cell?

### Hint 2 (Direct)
You can only come from top or left. Choose the path with minimum sum and add the current cell's value.

### Hint 3 (Detailed)
dp[i][j] = minimum sum to reach cell (i,j). Initialize dp[0][0] = grid[0][0]. For first row: dp[0][j] = dp[0][j-1] + grid[0][j]. For first column: dp[i][0] = dp[i-1][0] + grid[i][0]. For others: dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j].

---

## Problem 6: Maximal Square

### Hint 1 (Gentle)
For each cell with '1', think about the largest square that can have this cell as the bottom-right corner.

### Hint 2 (Direct)
The side length of the square ending at (i,j) depends on the squares ending at (i-1,j), (i,j-1), and (i-1,j-1). Take the minimum and add 1.

### Hint 3 (Detailed)
dp[i][j] = side length of largest square with bottom-right at (i,j). If matrix[i][j] == '1': dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1. Track the maximum side length seen. Return maxSide * maxSide for the area.

---

## Problem 7: Triangle

### Hint 1 (Gentle)
Start from the top and work your way down, or start from the bottom and work your way up. Which might be easier?

### Hint 2 (Direct)
Working bottom-up is often cleaner. For each element, choose the minimum of the two possible paths from the row below.

### Hint 3 (Detailed)
Start with dp = triangle's last row. Work upwards: for each row i from n-2 to 0, for each position j: dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]. The answer is dp[0]. This approach uses O(n) space instead of O(n²).

---

## Problem 8: Interleaving String

### Hint 1 (Gentle)
At each step, you're choosing to take a character from either s1 or s2. The choice must match the corresponding character in s3.

### Hint 2 (Direct)
dp[i][j] represents whether first i characters of s1 and first j characters of s2 can form first i+j characters of s3.

### Hint 3 (Detailed)
dp[i][j] = true if s3[0...i+j-1] can be formed by interleaving s1[0...i-1] and s2[0...j-1]. Transition: dp[i][j] = (dp[i-1][j] && s1[i-1] == s3[i+j-1]) || (dp[i][j-1] && s2[j-1] == s3[i+j-1]). Base: dp[0][0] = true.

---

## Problem 9: Distinct Subsequences

### Hint 1 (Gentle)
For each character in s, you have two choices: use it to match the current character in t, or skip it.

### Hint 2 (Direct)
dp[i][j] = number of distinct subsequences of s[0...i-1] that equal t[0...j-1]. You always have the option to skip s[i-1].

### Hint 3 (Detailed)
If s[i-1] == t[j-1], you can either use this match (dp[i-1][j-1]) or skip it (dp[i-1][j]). So dp[i][j] = dp[i-1][j-1] + dp[i-1][j]. If they don't match, dp[i][j] = dp[i-1][j]. Base: dp[i][0] = 1 (empty t can always be formed).

---

## Problem 10: Regular Expression Matching

### Hint 1 (Gentle)
The '*' is tricky - it can match 0 or more of the preceding character. Think about both cases separately.

### Hint 2 (Direct)
For '*', check two cases: matching 0 occurrences (skip pattern[j-1] and '*'), or matching 1+ occurrences (if preceding char matches, check dp[i-1][j]).

### Hint 3 (Detailed)
dp[i][j] = true if s[0...i-1] matches p[0...j-1]. If p[j-1] == '*': check 0 matches (dp[i][j-2]) or 1+ matches (if p[j-2] matches s[i-1], check dp[i-1][j]). If p[j-1] is regular char or '.': check if it matches s[i-1] and dp[i-1][j-1]. Handle edge cases carefully!

---

## General 2D DP Tips

### Recognizing 2D DP Problems
- Two strings/arrays being compared
- Grid/matrix traversal
- Problems with two changing parameters
- Subproblems depend on two indices

### Building the Solution
1. Define what dp[i][j] represents clearly
2. Identify base cases (usually edges or corners)
3. Find the recurrence relation
4. Determine the filling order
5. Return the appropriate cell (usually dp[m][n] or dp[m-1][n-1])

### Common Mistakes to Avoid
- Off-by-one errors with indices
- Incorrect base case initialization
- Wrong filling order
- Forgetting to handle empty strings/arrays
- Not considering all possible transitions