# Day 6, Session 16: Backtracking

## Overview
Master the art of systematic exploration and backtracking - the key pattern for solving combinatorial problems in interviews.

**Duration:** 3-5 hours
**Problems:** 10 (8 Medium, 2 Hard)
**Prerequisites:** Recursion, arrays, basic tree concepts

---

## Learning Objectives

By the end of this session, you will:
- ✅ Understand the backtracking decision tree model
- ✅ Master the backtracking template for all problems
- ✅ Solve subset, permutation, and combination problems
- ✅ Implement efficient pruning strategies
- ✅ Handle duplicate elements in backtracking

---

## Session Flow

### 1. Video (25 min)
Watch the assigned video on Backtracking fundamentals and patterns.

### 2. Concept Check (10 min)
Claude will quiz you on:
- Backtracking vs brute force
- Decision tree visualization
- State space pruning
- Time complexity analysis

### 3. Tips & Tricks (10 min)
Learn interview-specific insights about:
- The universal backtracking template
- When to use index vs element tracking
- Handling duplicates efficiently
- Common pruning techniques

### 4. Problem Solving (3-4 hours)
Solve 10 carefully selected problems:
1. Subsets (Medium)
2. Subsets II (Medium - with duplicates)
3. Permutations (Medium)
4. Permutations II (Medium - with duplicates)
5. Combination Sum (Medium - unlimited use)
6. Combination Sum II (Medium - single use)
7. Letter Combinations of a Phone Number (Medium)
8. Palindrome Partitioning (Medium)
9. Generate Parentheses (Medium)
10. N-Queens (Hard - classic backtracking)

---

## Key Concepts

### Backtracking Template
```typescript
function backtrack(state, choices, result) {
    if (isValid(state)) {
        result.push(copy(state));
        return;
    }

    for (choice of choices) {
        makeChoice(state, choice);
        backtrack(state, remainingChoices, result);
        undoChoice(state, choice);
    }
}
```

### Problem Categories
- **Subsets:** All possible combinations
- **Permutations:** All arrangements
- **Combinations:** Selections with constraints
- **Partitioning:** Dividing into valid groups
- **Generation:** Creating valid structures

### Time Complexity Patterns
- **Subsets:** O(2ⁿ × n)
- **Permutations:** O(n! × n)
- **Combinations:** O(2ⁿ) to O(n!)
- **N-Queens:** O(n!)

---

## Prerequisites

**Must know:**
- Recursion fundamentals
- Array manipulation
- Basic tree traversal concepts
- Set/Map operations

**Nice to have:**
- DFS tree traversal
- Combinatorial math basics
- Pruning strategies

---

## Success Criteria

You're ready to move on when you can:
- [ ] Write the backtracking template from memory
- [ ] Visualize the decision tree for any problem
- [ ] Identify when to use backtracking
- [ ] Implement pruning to optimize solutions
- [ ] Handle duplicates correctly

---

## Resources

**Video:** See LESSON.md for link

**Readings:**
- Backtracking Patterns: LESSON.md
- Template variations: SOLUTIONS.md

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Draw the decision tree** - Visualize before coding
2. **Start with the template** - Adapt it to each problem
3. **Think about choices** - What decisions at each step?
4. **Track state carefully** - Know what to pass down
5. **Practice pruning** - Identify invalid branches early
6. **Handle base cases** - When to collect results
7. **Debug systematically** - Print decision tree if stuck

---

## Common Mistakes

**Avoid these:**
- ❌ Not copying state when adding to results
- ❌ Forgetting to backtrack (undo changes)
- ❌ Incorrect duplicate handling with sorting
- ❌ Missing base cases or termination conditions
- ❌ Using global variables incorrectly

---

## What's Next

After completing this session:
1. Take a 15-minute break
2. Review your performance scores
3. Practice drawing decision trees
4. Move to Session 17: Dynamic Programming II

Session 17 builds on backtracking by adding memoization for overlapping subproblems.

---

**Ready to start?** Say: `"Claude, start session 6 16"`