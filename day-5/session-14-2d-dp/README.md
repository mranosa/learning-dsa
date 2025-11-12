# Day 5, Session 14: 2D Dynamic Programming

## Overview

Master multi-dimensional DP for grids, strings, and complex state problems.

**Duration:** 3-4 hours | **Problems:** 10 (7 Medium, 3 Hard)

---

## Learning Objectives

- ✅ Understand 2D DP state representation
- ✅ Build DP tables for grid problems
- ✅ Solve string comparison problems
- ✅ Optimize space from O(m×n) to O(n)
- ✅ Recognize 2D DP patterns instantly

---

## Session Flow

### 1. Videos (90 min)
- 2D DP Fundamentals (15 min)
- Grid Traversal (12 min)
- String DP Patterns (18 min)
- Edit Distance (20 min)
- Regular Expression Matching (25 min)

### 2. Concept Check (10 min)
Quiz on state definition, base cases, transitions.

### 3. Tips & Tricks (5 min)
Space optimization, index handling, common pitfalls.

### 4. Problems (2-3 hours)
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
- **Grid Traversal:** dp[i][j] = result at position (i, j)
- **String Comparison:** dp[i][j] = result for s1[0..i] and s2[0..j]
- **Interval DP:** dp[left][right] = result for range [left, right]
- **State DP:** dp[i][state] = result at position i with state

### State Definition
- **Grid:** dp[row][col] - value at grid position
- **Strings:** dp[i][j] - comparing first i and j chars
- **Intervals:** dp[L][R] - subproblem for range [L, R]

### Recurrence Relations
- **Grid paths:** dp[i][j] = f(dp[i-1][j], dp[i][j-1])
- **String match:** dp[i][j] = match ? dp[i-1][j-1] + 1 : max(dp[i-1][j], dp[i][j-1])
- **Edit distance:** dp[i][j] = 1 + min(insert, delete, replace)

### Space Optimization
- **Rolling array:** Use 2 rows instead of full matrix → O(n)
- **1D array:** When only previous row needed → O(n)
- **In-place:** Modify input when allowed → O(1)

---

## Prerequisites

**Must know:**
- 1D Dynamic Programming (Session 13)
- Array/Matrix manipulation
- String operations in TypeScript

---

## Success Criteria

- [ ] Define dp[i][j] clearly for any problem
- [ ] Identify correct base cases
- [ ] Write recurrence relations
- [ ] Optimize space when possible
- [ ] Solve Medium 2D DP <25 min

---

## Resources

**Video:** LESSON.md
**Practice:** PROBLEMS.md
**Solutions:** SOLUTIONS.md
**Hints:** HINTS.md

---

## Tips

1. Draw the DP table - visualize state transitions
2. Start with base cases - edges and corners
3. Trace through small example - verify logic
4. Check all transitions - don't miss diagonal
5. Consider space optimization - impress interviewers
6. Handle empty inputs - common edge case
7. Watch for off-by-one - dp[i][j] vs arr[i-1][j-1]

---

## Common Mistakes

- ❌ Confusing dp[i][j] meaning (indices vs counts)
- ❌ Wrong base case initialization
- ❌ Off-by-one errors in loops
- ❌ Not handling empty strings/grids
- ❌ Forgetting diagonal transitions
- ❌ Incorrect filling order

---

## What's Next

After completion:
1. 10-minute break
2. Review scores
3. Note difficult patterns
4. Session 15: Graphs

Session 15 introduces graph traversal and shortest paths.

---

**Ready?** Say: `"Claude, start session 5 14"`
