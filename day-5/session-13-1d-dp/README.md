# Day 5, Session 13: 1D Dynamic Programming

## Overview
Master the fundamental patterns of dynamic programming with single-dimensional states - the key to solving optimization problems efficiently.

**Duration:** 3-5 hours
**Problems:** 10 (1 Easy, 9 Medium)
**Prerequisites:** Basic recursion, memoization concepts

---

## Learning Objectives

By the end of this session, you will:
- ✅ Understand the core principles of dynamic programming
- ✅ Identify when to use DP vs other approaches
- ✅ Master bottom-up and top-down DP techniques
- ✅ Recognize common 1D DP patterns
- ✅ Optimize space complexity using state reduction

---

## Session Flow

### 1. Video (30 min)
Watch the assigned video on Dynamic Programming fundamentals and 1D DP patterns.

### 2. Concept Check (10 min)
Claude will quiz you on:
- DP vs recursion vs memoization
- Identifying overlapping subproblems
- Optimal substructure property
- State transition formulas

### 3. Tips & Tricks (5 min)
Learn interview-specific insights about:
- How to quickly identify DP problems
- Common state definitions
- Space optimization techniques

### 4. Problem Solving (3-4 hours)
Solve 10 carefully selected problems:
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

### Dynamic Programming Principles
- **Overlapping Subproblems** - Same problems solved multiple times
- **Optimal Substructure** - Optimal solution contains optimal sub-solutions
- **State Definition** - What parameters uniquely define a subproblem
- **State Transition** - How to compute state from previous states
- **Base Cases** - Starting points for computation

### Common 1D DP Patterns
- **Linear Sequence** - dp[i] depends on dp[i-1], dp[i-2], etc.
- **Decision Making** - Include/exclude current element
- **Optimization** - Min/max over all choices
- **Counting** - Number of ways to reach state
- **Existence** - Can we reach target state

### Implementation Approaches
- **Top-Down (Memoization):** Recursive with cache
- **Bottom-Up (Tabulation):** Iterative with table
- **Space-Optimized:** Using rolling variables

---

## Prerequisites

**Must know:**
- Basic recursion concepts
- Array manipulation in TypeScript
- Time/space complexity analysis

**Nice to have:**
- Mathematical recurrence relations
- Previous exposure to memoization
- Understanding of optimization problems

---

## Success Criteria

You're ready to move on when you can:
- [ ] Identify DP problems from problem statement
- [ ] Define state and transition correctly
- [ ] Implement both top-down and bottom-up solutions
- [ ] Optimize space complexity when possible
- [ ] Solve Medium DP problems in <25 min

---

## Resources

**Video:** See LESSON.md for link

**Readings:**
- DP Patterns: https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns
- State machines: TYPESCRIPT-LEETCODE.md

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Start with recursion** - Build intuition first
2. **Draw the recursion tree** - Visualize overlapping subproblems
3. **Define state clearly** - What uniquely identifies each subproblem
4. **Write recurrence relation** - Before coding
5. **Handle base cases carefully** - Common source of bugs
6. **Test with small inputs** - Trace through execution
7. **Optimize space last** - Correctness first, optimization second

---

## Common Mistakes

**Avoid these:**
- ❌ Jumping to DP without identifying if it's needed
- ❌ Incorrect state definition missing parameters
- ❌ Off-by-one errors in array indexing
- ❌ Forgetting to handle base cases
- ❌ Not initializing DP array properly

---

## What's Next

After completing this session:
1. Take a 15-minute break
2. Review your performance scores
3. Note patterns you struggled with
4. Move to Session 14: 2D Dynamic Programming

Session 14 extends these concepts to problems with two-dimensional states.

---

**Ready to start?** Say: `"Claude, start session 5 13"`