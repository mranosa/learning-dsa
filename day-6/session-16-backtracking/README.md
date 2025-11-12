# Day 6, Session 16: Backtracking

## Overview

Master the art of systematic exploration and backtracking - the fundamental pattern for solving combinatorial and constraint satisfaction problems in technical interviews.

**Duration:** 3-5 hours | **Problems:** 10 (8 Medium, 2 Hard)

---

## Learning Objectives

- ✅ Understand backtracking and the decision tree model
- ✅ Master the universal backtracking template
- ✅ Solve subset, permutation, and combination problems
- ✅ Implement efficient pruning strategies
- ✅ Handle duplicate elements correctly
- ✅ Recognize when to use backtracking vs other approaches

---

## Session Flow

### 1. Videos (50 min)
- Backtracking Fundamentals (25 min)
- Decision Trees & State Space (15 min)
- Advanced Patterns (10 min)

### 2. Concept Check (10 min)
Quiz on backtracking vs recursion, decision trees, time complexity, pruning.

### 3. Tips & Tricks (10 min)
Universal template, duplicate handling, optimization techniques, TypeScript patterns.

### 4. Problems (3-4 hours)
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

### Backtracking Decision Tree
```
At each node: Make choice → Explore → Undo choice

                    []
           /         |         \
         [1]        [2]        [3]
        /  \       /  \       /  \
    [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
```

### Universal Template
```typescript
function backtrack(state, choices) {
    if (isValid(state)) {
        result.push([...state]); // Copy!
        return;
    }

    for (choice of choices) {
        if (!isValidChoice(choice)) continue; // Prune

        makeChoice(state, choice);
        backtrack(state, remainingChoices);
        undoChoice(state, choice); // Backtrack!
    }
}
```

### Problem Categories
- **Subsets:** All possible combinations (2^n)
- **Permutations:** All arrangements (n!)
- **Combinations:** Selections with constraints
- **Partitioning:** Divide into valid groups
- **Generation:** Create valid structures (parentheses, sudoku)

### Time Complexity Patterns
- **Subsets:** O(2^n × n)
- **Permutations:** O(n! × n)
- **Combinations:** O(C(n,k) × k)
- **N-Queens:** O(n!)

---

## Prerequisites

**Must know:**
- Recursion fundamentals
- Array manipulation
- Basic tree traversal concepts
- TypeScript array methods

**Nice to have:**
- DFS tree traversal
- Combinatorial math basics
- Set/Map operations

---

## Success Criteria

- [ ] Explain backtracking and decision trees confidently
- [ ] Write the universal template from memory
- [ ] Identify when to use backtracking
- [ ] Solve subset/permutation problems <20 min
- [ ] Implement pruning optimizations
- [ ] Handle duplicates correctly

---

## Resources

**Video:** LESSON.md
**Practice:** PROBLEMS.md
**Solutions:** SOLUTIONS.md
**Hints:** HINTS.md

---

## Tips

1. Watch all videos - foundation is critical
2. Draw decision trees before coding
3. Start with the universal template
4. Think about choices at each step
5. Always copy state when collecting results
6. Test pruning with small inputs
7. Review solutions even if correct

---

## Common Mistakes

- ❌ Not copying arrays when adding to results
- ❌ Forgetting to backtrack (undo changes)
- ❌ Incorrect duplicate handling without sorting
- ❌ Missing base cases or termination conditions
- ❌ Not pruning invalid branches early
- ❌ Using global state incorrectly
- ❌ Mutating input without permission

---

## What's Next

After completion:
1. 15-minute break
2. Review scores and decision trees
3. Practice drawing state spaces
4. Session 17: Heaps (Priority Queues)

Session 17 introduces heap data structures for efficient priority-based operations.

---

**Ready?** Say: `"Claude, start session 6 16"`
