# Day 5, Session 15: Knapsack Dynamic Programming

## Overview
Master the knapsack pattern - one of the most fundamental and frequently tested DP patterns in technical interviews.

**Duration:** 3-4 hours
**Problems:** 10 (All Medium)
**Prerequisites:** Basic DP understanding, 1D/2D DP experience

---

## Learning Objectives

By the end of this session, you will:
- ✅ Master the 0/1 knapsack pattern
- ✅ Understand unbounded knapsack variations
- ✅ Recognize subset sum problems
- ✅ Apply knapsack to partition problems
- ✅ Optimize space complexity using rolling arrays

---

## Session Flow

### 1. Video (25 min)
Watch the assigned video on Knapsack DP fundamentals.

### 2. Concept Check (10 min)
Claude will quiz you on:
- 0/1 vs Unbounded knapsack
- Subset sum pattern
- State representation
- Space optimization techniques

### 3. Tips & Tricks (5 min)
Learn interview-specific insights about:
- When to use knapsack pattern
- Common state transitions
- TypeScript DP optimizations

### 4. Problem Solving (3-4 hours)
Solve 10 carefully selected problems:
1. Partition Equal Subset Sum (Medium)
2. Target Sum (Medium)
3. Last Stone Weight II (Medium)
4. Ones and Zeroes (Medium)
5. Coin Change 2 (Medium)
6. Combination Sum IV (Medium)
7. Word Break (Medium)
8. Partition to K Equal Sum Subsets (Medium)
9. Shopping Offers (Medium)
10. Minimum Cost For Tickets (Medium)

---

## Key Concepts

### Knapsack Variations
- **0/1 Knapsack** - Each item used once
- **Unbounded Knapsack** - Items can be reused
- **Subset Sum** - Can we reach target sum?
- **Partition Problem** - Split into equal subsets

### DP State Design
- **dp[i][j]** - Using first i items, can we achieve j?
- **dp[j]** - Can we achieve sum j? (space optimized)
- **dp[i][j][k]** - Multi-dimensional for complex constraints

### Common Patterns
- Include/Exclude decisions
- Rolling array optimization
- Counting combinations vs permutations
- Target sum transformations

---

## Prerequisites

**Must know:**
- Basic DP concepts (memoization, tabulation)
- 1D and 2D array manipulation
- Recursion and state transitions

**Nice to have:**
- Experience with subset problems
- Understanding of space optimization
- Bitmasking basics (for some problems)

---

## Success Criteria

You're ready to move on when you can:
- [ ] Identify knapsack pattern immediately
- [ ] Design correct DP state representation
- [ ] Implement both recursive and iterative solutions
- [ ] Optimize space complexity when possible
- [ ] Handle variations (counting, optimization, decision)

---

## Resources

**Video:** See LESSON.md for link

**Readings:**
- Knapsack Problem Wiki: https://en.wikipedia.org/wiki/Knapsack_problem
- DP Patterns: https://leetcode.com/discuss/study-guide/458695/

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Understand the pattern first** - Don't memorize solutions
2. **Draw the DP table** - Visualize state transitions
3. **Start with recursive** - Then convert to iterative
4. **Test with small inputs** - Verify your logic
5. **Look for optimizations** - Can you reduce space?
6. **Practice state design** - It's the hardest part
7. **Time yourself** - Knapsack should be <30 min

---

## Common Mistakes

**Avoid these:**
- ❌ Confusing 0/1 with unbounded knapsack
- ❌ Wrong initialization of DP array
- ❌ Off-by-one errors in array bounds
- ❌ Not handling edge cases (empty array, zero target)
- ❌ Forgetting to consider negative numbers

---

## What's Next

After completing this session:
1. Take a 15-minute break
2. Review your performance scores
3. Note patterns you struggled with
4. Move to Session 16: String DP

Session 16 builds on DP concepts with string-specific patterns.

---

**Ready to start?** Say: `"Claude, start session 5 15"`