# Day 5, Session 13: 1D Dynamic Programming

## Overview

Master dynamic programming fundamentals with single-dimensional states. Essential pattern for optimization problems.

**Duration:** 3-5 hours | **Problems:** 10 (1 Easy, 9 Medium)

---

## Learning Objectives

- ✅ Understand DP core principles
- ✅ Master memoization vs tabulation
- ✅ Identify overlapping subproblems
- ✅ Define state transitions
- ✅ Optimize space complexity

---

## Session Flow

### 1. Videos (55 min)
- Dynamic Programming Fundamentals (25 min)
- Memoization vs Tabulation (15 min)
- 1D DP Patterns (15 min)

### 2. Concept Check (10 min)
Quiz on DP principles, overlapping subproblems, optimal substructure, state transitions.

### 3. Tips & Tricks (5 min)
DP problem identification, state definition, space optimization techniques.

### 4. Problems (3-4 hours)
1. Climbing Stairs (Easy)
2. House Robber (Medium)
3. House Robber II (Medium)
4. Coin Change (Medium)
5. Longest Increasing Subsequence (Medium)
6. Decode Ways (Medium)
7. Jump Game (Medium)
8. Maximum Product Subarray (Medium)
9. Palindromic Substrings (Medium)
10. Longest Palindromic Substring (Medium)

---

## Key Concepts

### DP Principles
- **Overlapping Subproblems** - Same problems solved repeatedly
- **Optimal Substructure** - Optimal solution contains optimal sub-solutions
- **Memoization (Top-Down)** - Recursive with cache
- **Tabulation (Bottom-Up)** - Iterative with table
- **State Definition** - What uniquely defines a subproblem

### Common 1D Patterns
- **Linear Sequence** - dp[i] from dp[i-1], dp[i-2]
- **Decision Making** - Include/exclude element
- **Optimization** - Min/max over choices
- **Counting** - Number of ways to reach state
- **Existence** - Can we reach target

### State Transition
- **Base Cases** - Starting points
- **Recurrence Relation** - Formula connecting states
- **Computation Order** - Fill DP table correctly

---

## Prerequisites

**Must know:**
- Basic recursion concepts
- Array manipulation in TypeScript
- Time/space complexity analysis

---

## Success Criteria

- [ ] Identify when to use DP
- [ ] Define state and transition correctly
- [ ] Implement both top-down and bottom-up
- [ ] Optimize space when possible
- [ ] Solve Medium DP <25 min

---

## Resources

**Video:** LESSON.md
**Practice:** PROBLEMS.md
**Solutions:** SOLUTIONS.md
**Hints:** HINTS.md

---

## Tips

1. Start with recursive solution
2. Draw recursion tree - visualize overlap
3. Define state clearly before coding
4. Write recurrence relation first
5. Handle base cases carefully
6. Test with small inputs
7. Optimize space last

---

## Common Mistakes

- ❌ Using DP when not needed
- ❌ Incorrect state definition
- ❌ Off-by-one array indexing
- ❌ Forgetting base cases
- ❌ Wrong DP array initialization

---

## What's Next

After completion:
1. 15-minute break
2. Review performance scores
3. Note struggled patterns
4. Session 14: 2D Dynamic Programming

Session 14 extends 1D concepts to two-dimensional states.

---

**Ready?** Say: `"Claude, start session 5 13"`
