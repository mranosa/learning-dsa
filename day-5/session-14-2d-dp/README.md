# Day 5, Session 14: 2D Dynamic Programming

## Overview
Master multi-dimensional dynamic programming techniques - essential for solving complex optimization problems in technical interviews.

**Duration:** 3-5 hours
**Problems:** 10 (7 Medium, 3 Hard)
**Prerequisites:** 1D Dynamic Programming, Matrix manipulation

---

## Learning Objectives

By the end of this session, you will:
- ✅ Understand 2D DP state representation
- ✅ Build DP tables for grid-based problems
- ✅ Solve string matching and comparison problems
- ✅ Optimize space complexity in 2D DP
- ✅ Recognize when to apply 2D vs 1D DP

---

## Session Flow

### 1. Video (30 min)
Watch the assigned videos on 2D Dynamic Programming patterns.

### 2. Concept Check (15 min)
Claude will quiz you on:
- 2D state representation
- Grid traversal patterns
- String DP problems
- Space optimization techniques

### 3. Tips & Tricks (10 min)
Learn interview-specific insights about:
- Building the DP table
- Choosing state variables
- Space optimization patterns
- Common 2D DP templates

### 4. Problem Solving (3-4 hours)
Solve 10 carefully selected problems:
1. Unique Paths (Medium)
2. Unique Paths II (Medium)
3. Longest Common Subsequence (Medium)
4. Edit Distance (Medium)
5. Minimum Path Sum (Medium)
6. Maximal Square (Medium)
7. Triangle (Medium)
8. Interleaving String (Medium)
9. Distinct Subsequences (Hard)
10. Regular Expression Matching (Hard)

---

## Key Concepts

### 2D DP Patterns
- **Grid Traversal** - Path counting/optimization
- **String Matching** - LCS, Edit Distance patterns
- **Matrix Chain** - Optimal multiplication order
- **Interval DP** - Range-based subproblems
- **Game Theory** - Min-max problems

### State Definition
- **dp[i][j]** - Result for first i elements and first j elements
- **dp[row][col]** - Result at grid position (row, col)
- **dp[left][right]** - Result for interval [left, right]
- **dp[i][state]** - Result at position i with specific state

### Space Optimization
- **Rolling Array:** Use only 2 rows instead of full matrix
- **1D Optimization:** When only previous row needed
- **In-place:** Modify input when allowed

### Common Templates
- Grid path problems
- String comparison problems
- Optimal selection problems
- Pattern matching problems

---

## Prerequisites

**Must know:**
- 1D Dynamic Programming concepts
- Matrix/2D array manipulation
- Recursion with memoization
- String operations in TypeScript

**Nice to have:**
- Understanding of recurrence relations
- Graph traversal basics
- Optimization problem experience

---

## Success Criteria

You're ready to move on when you can:
- [ ] Identify 2D DP problems quickly
- [ ] Define appropriate state variables
- [ ] Build DP table correctly
- [ ] Optimize space complexity when possible
- [ ] Solve Medium 2D DP problems in <25 min

---

## Resources

**Videos:** See LESSON.md for links

**Readings:**
- Dynamic Programming Patterns: https://leetcode.com/discuss/general-discussion/458695/
- 2D DP Tutorial: https://www.geeksforgeeks.org/dynamic-programming/

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Draw the DP table** - Visualize state transitions
2. **Start with recursion** - Then optimize to DP
3. **Check base cases carefully** - Often tricky in 2D
4. **Test with small examples** - Trace through table filling
5. **Consider space optimization** - Impress interviewers
6. **Practice string problems** - Very common in interviews
7. **Master grid traversal** - Foundation for many problems

---

## Common Mistakes

**Avoid these:**
- ❌ Incorrect base case initialization
- ❌ Off-by-one errors in indices
- ❌ Confusing dp[i][j] meaning
- ❌ Not handling empty strings/arrays
- ❌ Forgetting to consider diagonal transitions

---

## What's Next

After completing this session:
1. Take a 15-minute break
2. Review your performance scores
3. Note patterns you struggled with
4. Move to Session 15: Graph Algorithms

Session 15 introduces graph traversal and shortest path algorithms.

---

**Ready to start?** Say: `"Claude, start session 5 14"`