# Hints: Mixed Review - Hardest Blind 75

## Problem 1: Alien Dictionary

### Hint 1 (Gentle)
Think about how a dictionary works. When words are sorted alphabetically, what can you infer from the ordering of adjacent words?

### Hint 2 (Direct)
Compare adjacent words to find character ordering relationships. If "wrt" comes before "wrf", then 't' must come before 'f' in the alien alphabet. Build a directed graph where an edge from 'a' to 'b' means 'a' comes before 'b'.

### Hint 3 (Detailed)
1. Build a directed graph from character dependencies
2. Use topological sort to find valid ordering
3. Watch for cycles (impossible ordering)
4. Handle edge case: "abc" before "ab" is invalid

---

## Problem 2: Serialize and Deserialize Binary Tree

### Hint 1 (Gentle)
You need a way to represent the tree structure as a string. How can you encode both the values and the tree structure?

### Hint 2 (Direct)
Use a tree traversal (pre-order, in-order, or level-order) and include markers for null nodes. Pre-order is often easiest because you process the root first.

### Hint 3 (Detailed)
1. Serialize: Pre-order traverse, use "null" for empty nodes
2. Deserialize: Use recursion or queue to rebuild
3. Example: [1,2,3,null,null,4,5] → "1,2,null,null,3,4,null,null,5,null,null"
4. Keep an index pointer when deserializing

---

## Problem 3: Longest Increasing Path in a Matrix

### Hint 1 (Gentle)
This is a graph problem in disguise. Each cell can connect to its neighbors if they have larger values. What's the longest path in this graph?

### Hint 2 (Direct)
Use DFS from each cell to find the longest increasing path starting from that cell. But this would be O(m*n)² - how can you optimize repeated calculations?

### Hint 3 (Detailed)
1. Use memoization: cache the longest path from each cell
2. DFS with memo: if memo[i][j] exists, return it
3. For each cell, try all 4 directions where value increases
4. Time complexity reduces to O(m*n) with memoization

---

## Problem 4: Maximum Profit in Job Scheduling

### Hint 1 (Gentle)
This is a weighted interval scheduling problem. For each job, you have two choices: take it or skip it. How do you track the maximum profit?

### Hint 2 (Direct)
Sort jobs by end time. For each job, find the maximum profit including this job (current profit + best profit before this job starts) versus excluding it (best profit so far).

### Hint 3 (Detailed)
1. Sort jobs by end time
2. DP[i] = max profit using jobs 0...i
3. For job i: find latest non-overlapping job j using binary search
4. DP[i] = max(DP[i-1], profit[i] + DP[j])
5. Binary search on end times for efficiency

---

## Problem 5: Reverse Nodes in k-Group

### Hint 1 (Gentle)
Break the problem down: first figure out how to reverse exactly k nodes, then figure out how to apply this to the entire list.

### Hint 2 (Direct)
Use a dummy head to simplify edge cases. For each group of k nodes, reverse them and connect to the previous group. Keep track of the tail of the previous group.

### Hint 3 (Detailed)
1. Count total nodes first
2. Use dummy node before head
3. For each k-group:
   - Save the first node (will become last)
   - Reverse k nodes using pointer manipulation
   - Connect to previous group
4. Move to next group, update pointers

---

## Problem 6: Minimum Window Subsequence

### Hint 1 (Gentle)
Unlike substring problems, subsequence allows gaps. Start by finding any valid subsequence, then try to minimize the window.

### Hint 2 (Direct)
Use two pointers: forward scan to find a subsequence, then backward scan to tighten the window. The backward scan ensures you find the minimum window ending at the current position.

### Hint 3 (Detailed)
1. Forward scan: match all characters of s2 in s1
2. Backward scan: from the end match position, go back to find the tightest start
3. Record this window if it's smaller
4. Continue from next position after the found start
5. Time: O(|s1| * |s2|)

---

## Problem 7: Wildcard Matching

### Hint 1 (Gentle)
'?' matches exactly one character, '*' matches zero or more. How would you handle these different wildcards differently?

### Hint 2 (Direct)
Use DP where dp[i][j] represents whether s[0...i-1] matches p[0...j-1]. For '*', it can match empty (dp[i][j-1]) or one/more characters (dp[i-1][j]).

### Hint 3 (Detailed)
1. DP table: dp[i][j] = s[0:i] matches p[0:j]
2. Base: dp[0][0] = true, handle leading '*' in pattern
3. If p[j] = '*': dp[i][j] = dp[i-1][j] || dp[i][j-1]
4. If p[j] = '?' or equals s[i]: dp[i][j] = dp[i-1][j-1]
5. Result: dp[m][n]

---

## Problem 8: Burst Balloons

### Hint 1 (Gentle)
The key insight: instead of thinking about which balloon to burst first, think about which balloon to burst last in a subarray.

### Hint 2 (Direct)
Use interval DP. For each subarray [left, right], try bursting each balloon k last. The coins gained = nums[left-1] * nums[k] * nums[right+1] plus the coins from the left and right subarrays.

### Hint 3 (Detailed)
1. Add dummy balloons with value 1 at both ends
2. dp[left][right] = max coins bursting balloons in [left, right]
3. For each interval length, for each starting position:
   - Try each balloon k as the last to burst
   - Coins = balloons[left-1] * balloons[k] * balloons[right+1]
   - Plus dp[left][k-1] + dp[k+1][right]
4. Build up from smaller to larger intervals

---

## Problem 9: Distinct Subsequences

### Hint 1 (Gentle)
For each character in s, you can either use it to match the current character in t, or skip it. How many ways can you form t?

### Hint 2 (Direct)
Use DP where dp[i][j] = number of ways to form t[0...j-1] from s[0...i-1]. If s[i-1] == t[j-1], you can either use or skip s[i-1].

### Hint 3 (Detailed)
1. dp[i][j] = ways to form t[0:j] from s[0:i]
2. Base: dp[i][0] = 1 (empty t)
3. Transition:
   - Always: dp[i][j] = dp[i-1][j] (skip s[i])
   - If s[i] == t[j]: dp[i][j] += dp[i-1][j-1] (use s[i])
4. Result: dp[m][n]
5. Can optimize to O(n) space using 1D array

---

## Problem 10: Basic Calculator III

### Hint 1 (Gentle)
This problem requires handling operator precedence: parentheses first, then multiplication/division, then addition/subtraction. How would you parse such an expression?

### Hint 2 (Direct)
Use recursive descent parsing with three levels: expression (handles +/-), term (handles */÷), and factor (handles parentheses and numbers). Each level handles its operators and delegates to the next level for higher precedence.

### Hint 3 (Detailed)
1. Expression level: handles + and -, calls term()
2. Term level: handles * and /, calls factor()
3. Factor level: handles () by calling expression() recursively, or returns number
4. Process left-to-right at each level
5. For parentheses: skip '(', recursively evaluate, skip ')'
6. Use index pointer to track position in string

---

## General Problem-Solving Strategy

1. **Understand deeply** - Read problem 2-3 times
2. **Find the pattern** - What technique applies?
3. **Start simple** - Brute force first
4. **Optimize** - Apply the right data structure/algorithm
5. **Handle edges** - Empty inputs, single elements, cycles
6. **Test thoroughly** - Use examples and create your own

Remember: These are hard problems. It's normal to struggle. Focus on understanding the approach even if implementation is challenging!