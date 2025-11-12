# Problems - Session 14: 2D Dynamic Programming

10 problems in order. Use UMPIRE method.

**Targets:** Medium <25 min | Hard <40 min

---

## Problem 1: Unique Paths

**Difficulty:** Medium | **Pattern:** Grid DP
**LeetCode:** https://leetcode.com/problems/unique-paths/

### Problem

Robot at top-left of `m × n` grid. Can only move down or right. How many unique paths to bottom-right?

### Examples

```
m = 3, n = 7
Output: 28

m = 3, n = 2
Output: 3
Explanation:
1. Right → Down → Down
2. Down → Down → Right
3. Down → Right → Down
```

### Constraints

- 1 ≤ m, n ≤ 100

### Hints
- dp[i][j] = ways to reach position (i,j)
- Can only come from top or left
- Base case: first row and column all 1s

---

## Problem 2: Unique Paths II

**Difficulty:** Medium | **Pattern:** Grid DP with Obstacles
**LeetCode:** https://leetcode.com/problems/unique-paths-ii/

### Problem

Same as Unique Paths, but grid has obstacles (marked as 1). 0 = empty space. Return number of unique paths.

### Examples

```
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: One obstacle in middle

obstacleGrid = [[0,1],[0,0]]
Output: 1
```

### Constraints

- m == obstacleGrid.length
- n == obstacleGrid[i].length
- 1 ≤ m, n ≤ 100
- obstacleGrid[i][j] is 0 or 1

### Hints
- If cell has obstacle, 0 ways to reach it
- Handle first row/column carefully (obstacle blocks all after)
- Check start/end positions for obstacles

---

## Problem 3: Longest Common Subsequence

**Difficulty:** Medium | **Pattern:** String DP
**LeetCode:** https://leetcode.com/problems/longest-common-subsequence/

### Problem

Given two strings `text1` and `text2`, return length of longest common subsequence. Subsequence: characters in order but not necessarily contiguous.

### Examples

```
text1 = "abcde", text2 = "ace"
Output: 3  ("ace")

text1 = "abc", text2 = "abc"
Output: 3  ("abc")

text1 = "abc", text2 = "def"
Output: 0
```

### Constraints

- 1 ≤ text1.length, text2.length ≤ 1000
- Only lowercase English letters

### Hints
- dp[i][j] = LCS of first i chars of text1 and first j chars of text2
- If chars match: dp[i][j] = dp[i-1][j-1] + 1
- If don't match: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
- Need (m+1) × (n+1) table for empty string base case

---

## Problem 4: Edit Distance

**Difficulty:** Medium | **Pattern:** String DP
**LeetCode:** https://leetcode.com/problems/edit-distance/

### Problem

Convert `word1` to `word2` using minimum operations. Operations: insert, delete, replace a character.

### Examples

```
word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse → rorse (replace 'h' with 'r')
rorse → rose (remove 'r')
rose → ros (remove 'e')

word1 = "intention", word2 = "execution"
Output: 5
```

### Constraints

- 0 ≤ word1.length, word2.length ≤ 500
- Only lowercase English letters

### Hints
- dp[i][j] = min operations to convert word1[0..i-1] to word2[0..j-1]
- If chars match: dp[i][j] = dp[i-1][j-1]
- If don't match: 1 + min(delete, insert, replace)
- Base: dp[i][0] = i (delete all), dp[0][j] = j (insert all)

---

## Problem 5: Minimum Path Sum

**Difficulty:** Medium | **Pattern:** Grid DP
**LeetCode:** https://leetcode.com/problems/minimum-path-sum/

### Problem

Given `m × n` grid of non-negative numbers, find path from top-left to bottom-right minimizing sum. Can only move down or right.

### Examples

```
grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Path: 1→3→1→1→1

grid = [[1,2,3],[4,5,6]]
Output: 12
```

### Constraints

- m == grid.length
- n == grid[i].length
- 1 ≤ m, n ≤ 200
- 0 ≤ grid[i][j] ≤ 200

### Hints
- dp[i][j] = minimum sum to reach (i,j)
- dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
- Initialize first row/column with cumulative sums
- Can optimize to O(1) space by modifying input

---

## Problem 6: Maximal Square

**Difficulty:** Medium | **Pattern:** Grid DP
**LeetCode:** https://leetcode.com/problems/maximal-square/

### Problem

Given `m × n` binary matrix (0s and 1s), find largest square containing only 1s. Return area.

### Examples

```
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
Output: 4  (2×2 square)

matrix = [["0","1"],["1","0"]]
Output: 1

matrix = [["0"]]
Output: 0
```

### Constraints

- m == matrix.length
- n == matrix[i].length
- 1 ≤ m, n ≤ 300
- matrix[i][j] is '0' or '1'

### Hints
- dp[i][j] = side length of largest square with bottom-right at (i,j)
- If matrix[i][j] == '1': dp[i][j] = min(top, left, diagonal) + 1
- Track max side length seen
- Return maxSide × maxSide for area

---

## Problem 7: Triangle

**Difficulty:** Medium | **Pattern:** Grid DP (Irregular)
**LeetCode:** https://leetcode.com/problems/triangle/

### Problem

Given triangle array, return minimum path sum from top to bottom. Each step moves to adjacent number in row below (index i → i or i+1).

### Examples

```
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11  (2+3+5+1)

triangle = [[-10]]
Output: -10
```

### Constraints

- 1 ≤ triangle.length ≤ 200
- triangle[0].length == 1
- triangle[i].length == triangle[i-1].length + 1
- -10⁴ ≤ triangle[i][j] ≤ 10⁴

### Hints
- Work bottom-up is easier
- dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
- Start with last row, work upward
- O(n) space solution

---

## Problem 8: Interleaving String

**Difficulty:** Medium | **Pattern:** String DP
**LeetCode:** https://leetcode.com/problems/interleaving-string/

### Problem

Given `s1`, `s2`, `s3`, determine if `s3` is formed by interleaving `s1` and `s2`.

### Examples

```
s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

s1 = "", s2 = "", s3 = ""
Output: true
```

### Constraints

- 0 ≤ s1.length, s2.length ≤ 100
- 0 ≤ s3.length ≤ 200
- Lowercase English letters only

### Hints
- dp[i][j] = can first i+j chars of s3 be formed from s1[0..i-1] and s2[0..j-1]
- dp[i][j] = (dp[i-1][j] && s1[i-1]==s3[i+j-1]) || (dp[i][j-1] && s2[j-1]==s3[i+j-1])
- Check lengths: s1.length + s2.length == s3.length

---

## Problem 9: Distinct Subsequences

**Difficulty:** Hard | **Pattern:** String DP
**LeetCode:** https://leetcode.com/problems/distinct-subsequences/

### Problem

Given strings `s` and `t`, return number of distinct subsequences of `s` which equal `t`.

### Examples

```
s = "rabbbit", t = "rabbit"
Output: 3
Explanation: rabb_bit, rab_bbit, ra_bbbit

s = "babgbag", t = "bag"
Output: 5
```

### Constraints

- 1 ≤ s.length, t.length ≤ 1000
- English letters only

### Hints
- dp[i][j] = number of ways to form t[0..j-1] from s[0..i-1]
- Always can skip s[i-1]: dp[i][j] = dp[i-1][j]
- If s[i-1] == t[j-1], also add dp[i-1][j-1]
- Base: dp[i][0] = 1 (empty t can always be formed)

---

## Problem 10: Regular Expression Matching

**Difficulty:** Hard | **Pattern:** String DP
**LeetCode:** https://leetcode.com/problems/regular-expression-matching/

### Problem

Implement regex matching with '.' and '*':
- '.' matches any single character
- '*' matches zero or more of preceding element

### Examples

```
s = "aa", p = "a"
Output: false

s = "aa", p = "a*"
Output: true  (* matches multiple 'a')

s = "ab", p = ".*"
Output: true  (.* matches any string)

s = "mississippi", p = "mis*is*p*."
Output: false
```

### Constraints

- 1 ≤ s.length ≤ 20
- 1 ≤ p.length ≤ 20
- s contains only lowercase letters
- p contains lowercase, '.', '*'
- Each '*' has valid preceding character

### Hints
- dp[i][j] = s[0..i-1] matches p[0..j-1]
- If p[j-1] == '*': match 0 (dp[i][j-2]) or 1+ (dp[i-1][j] if chars match)
- If p[j-1] == '.' or matches s[i-1]: dp[i][j] = dp[i-1][j-1]
- Handle patterns like "a*" at start carefully

---

## Summary

**Total:** 10 problems (7 Medium, 3 Hard)

**Patterns:**
- Grid DP (paths, sums, squares)
- String comparison (LCS, edit distance)
- String matching (interleaving, regex)

**Complexity Targets:**
- Time: O(m×n) standard
- Space: O(m×n) → optimize to O(n)

---

**Ready?** Say: `"Claude, give me the problem"` or `"Go"`

[Solutions](./SOLUTIONS.md) | [Hints](./HINTS.md)
