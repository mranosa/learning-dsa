# Session 14: 2D Dynamic Programming Problems

## Problem 1: Unique Paths (Medium)
**LeetCode:** https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a `m x n` grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

### Examples:
```
Input: m = 3, n = 7
Output: 28

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are 3 ways to reach bottom-right:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

### Constraints:
- 1 <= m, n <= 100

---

## Problem 2: Unique Paths II (Medium)
**LeetCode:** https://leetcode.com/problems/unique-paths-ii/

You are given an `m x n` integer array grid. There is a robot initially located at the top-left corner. The robot can only move either down or right. The robot is trying to reach the bottom-right corner.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

### Examples:
```
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
```

### Constraints:
- m == obstacleGrid.length
- n == obstacleGrid[i].length
- 1 <= m, n <= 100
- obstacleGrid[i][j] is 0 or 1

---

## Problem 3: Longest Common Subsequence (Medium)
**LeetCode:** https://leetcode.com/problems/longest-common-subsequence/

Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

A common subsequence of two strings is a subsequence that is common to both strings.

### Examples:
```
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no common subsequence, return 0.
```

### Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters

---

## Problem 4: Edit Distance (Medium)
**LeetCode:** https://leetcode.com/problems/edit-distance/

Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

### Examples:
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

### Constraints:
- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters

---

## Problem 5: Minimum Path Sum (Medium)
**LeetCode:** https://leetcode.com/problems/minimum-path-sum/

Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

### Examples:
```
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: The path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
Explanation: The path 1 → 2 → 3 → 6 minimizes the sum.
```

### Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 200

---

## Problem 6: Maximal Square (Medium)
**LeetCode:** https://leetcode.com/problems/maximal-square/

Given an `m x n` binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

### Examples:
```
Input: matrix = [["1","0","1","0","0"],
                 ["1","0","1","1","1"],
                 ["1","1","1","1","1"],
                 ["1","0","0","1","0"]]
Output: 4
Explanation: The largest square has side length 2.

Input: matrix = [["0","1"],["1","0"]]
Output: 1

Input: matrix = [["0"]]
Output: 0
```

### Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 300
- matrix[i][j] is '0' or '1'

---

## Problem 7: Triangle (Medium)
**LeetCode:** https://leetcode.com/problems/triangle/

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

### Examples:
```
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.

Input: triangle = [[-10]]
Output: -10
```

### Constraints:
- 1 <= triangle.length <= 200
- triangle[0].length == 1
- triangle[i].length == triangle[i - 1].length + 1
- -10^4 <= triangle[i][j] <= 10^4

---

## Problem 8: Interleaving String (Medium)
**LeetCode:** https://leetcode.com/problems/interleaving-string/

Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an interleaving of `s1` and `s2`.

An interleaving of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` substrings respectively, such that:
- s = s₁ + s₂ + ... + sₙ
- t = t₁ + t₂ + ... + tₘ
- |n - m| <= 1
- The interleaving is s₁ + t₁ + s₂ + t₂ + s₃ + t₃ + ... or t₁ + s₁ + t₂ + s₂ + t₃ + s₃ + ...

### Examples:
```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Input: s1 = "", s2 = "", s3 = ""
Output: true
```

### Constraints:
- 0 <= s1.length, s2.length <= 100
- 0 <= s3.length <= 200
- s1, s2, and s3 consist of lowercase English letters

---

## Problem 9: Distinct Subsequences (Hard)
**LeetCode:** https://leetcode.com/problems/distinct-subsequences/

Given two strings `s` and `t`, return the number of distinct subsequences of `s` which equals `t`.

The test cases are generated so that the answer fits on a 32-bit signed integer.

### Examples:
```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation: There are 3 ways you can generate "rabbit" from s.
rabb_bit
rab_bbit
ra_bbbit

Input: s = "babgbag", t = "bag"
Output: 5
Explanation: There are 5 ways you can generate "bag" from s.
ba_g_bag
ba_gb_ag
b_abgb_ag
_babg_bag
_babgba_g
```

### Constraints:
- 1 <= s.length, t.length <= 1000
- s and t consist of English letters

---

## Problem 10: Regular Expression Matching (Hard)
**LeetCode:** https://leetcode.com/problems/regular-expression-matching/

Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*' where:
- '.' Matches any single character
- '*' Matches zero or more of the preceding element

The matching should cover the entire input string (not partial).

### Examples:
```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'.

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Input: s = "mississippi", p = "mis*is*p*."
Output: false
```

### Constraints:
- 1 <= s.length <= 20
- 1 <= p.length <= 20
- s contains only lowercase English letters
- p contains only lowercase English letters, '.', and '*'
- It is guaranteed for each appearance of the character '*', there will be a previous valid character to match