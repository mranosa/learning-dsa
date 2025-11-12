# Day 5, Session 15: Knapsack Dynamic Programming

## Overview

Master the knapsack pattern - one of the most fundamental and frequently tested DP patterns in technical interviews.

**Duration:** 3-4 hours | **Problems:** 10 (All Medium)

---

## Learning Objectives

- ✅ Master the 0/1 knapsack pattern
- ✅ Understand unbounded knapsack variations
- ✅ Recognize subset sum problems
- ✅ Apply knapsack to partition problems
- ✅ Optimize space complexity using rolling arrays

---

## Session Flow

### 1. Videos (60 min)
- 0/1 Knapsack Fundamentals (15 min)
- Unbounded Knapsack Pattern (15 min)
- Subset Sum & Variations (15 min)
- Space Optimization Techniques (15 min)

### 2. Concept Check (10 min)
Quiz on 0/1 vs unbounded, subset sum, state representation, space optimization.

### 3. Tips & Tricks (5 min)
Pattern recognition, state design, iteration direction, TypeScript DP gotchas.

### 4. Problems (3-4 hours)
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

### Knapsack Fundamentals
- **0/1 Knapsack** - Each item used at most once
- **Unbounded Knapsack** - Items can be reused infinitely
- **Bounded Knapsack** - Each item has limited quantity
- **Subset Sum** - Can we reach target sum?

### 0/1 vs Unbounded
- **0/1:** Iterate backwards, no reuse
- **Unbounded:** Iterate forwards, allow reuse
- **Key difference:** Loop direction determines reusability

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

- [ ] Identify knapsack pattern immediately
- [ ] Design correct DP state representation
- [ ] Implement both recursive and iterative solutions
- [ ] Optimize space complexity when possible
- [ ] Distinguish 0/1 from unbounded knapsack

---

## Resources

**Video:** LESSON.md
**Practice:** PROBLEMS.md
**Solutions:** SOLUTIONS.md
**Hints:** HINTS.md

---

## Tips

1. Watch all videos - pattern recognition is critical
2. Draw the DP table for visualization
3. Start with recursive, then convert to iterative
4. Test with small inputs first
5. Look for space optimization opportunities
6. Practice state design - it's the hardest part
7. Time yourself - aim for <30 min per problem

---

## Common Mistakes

- ❌ Confusing 0/1 with unbounded knapsack
- ❌ Wrong initialization of DP array
- ❌ Off-by-one errors in array bounds
- ❌ Not handling edge cases (empty array, zero target)
- ❌ Forgetting to iterate backwards for 0/1
- ❌ Mixing up combinations vs permutations

---

## What's Next

After completion:
1. 15-minute break
2. Review performance scores
3. Note patterns you struggled with
4. Session 16: String DP

Session 16 builds on DP concepts with string-specific patterns.

---

**Ready?** Say: `"Claude, start session 5 15"`
