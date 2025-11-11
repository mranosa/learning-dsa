# Day 3, Session 8: Tree DFS

## Overview
Master depth-first search techniques for binary trees - from basic traversals to complex path-finding algorithms.

**Duration:** 3-5 hours
**Problems:** 10 (6 Easy, 3 Medium, 1 Hard)
**Prerequisites:** Basic recursion and tree concepts

---

## Learning Objectives

By the end of this session, you will:
- ✅ Understand DFS traversal patterns (preorder, inorder, postorder)
- ✅ Master recursive tree operations
- ✅ Calculate tree properties (depth, diameter, balance)
- ✅ Solve path-based problems efficiently
- ✅ Recognize when to use DFS vs BFS for trees

---

## Session Flow

### 1. Video (30 min)
Watch the assigned video on Tree DFS and binary tree fundamentals.

### 2. Concept Check (10 min)
Claude will quiz you on:
- Tree terminology (root, leaf, height, depth)
- DFS traversal patterns
- Recursive vs iterative approaches
- Time/space complexity of tree operations

### 3. Tips & Tricks (5 min)
Learn interview-specific insights about:
- When to use each traversal type
- Common tree patterns
- Edge cases in tree problems
- TypeScript tree node definitions

### 4. Problem Solving (3-4 hours)
Solve 10 carefully selected problems:
1. Maximum Depth of Binary Tree (Easy)
2. Same Tree (Easy)
3. Invert Binary Tree (Easy)
4. Symmetric Tree (Easy)
5. Diameter of Binary Tree (Easy)
6. Balanced Binary Tree (Easy)
7. Lowest Common Ancestor of a Binary Tree (Medium)
8. Path Sum (Easy)
9. Path Sum II (Medium)
10. Binary Tree Maximum Path Sum (Hard)

---

## Key Concepts

### DFS Traversal Patterns
- **Preorder:** Root → Left → Right (top-down)
- **Inorder:** Left → Root → Right (sorted for BST)
- **Postorder:** Left → Right → Root (bottom-up)

### Tree Properties
- **Height/Depth:** Longest path from root to leaf
- **Diameter:** Longest path between any two nodes
- **Balance:** Height difference between subtrees ≤ 1

### Common Patterns
- Recursive helper functions
- Return values from subtrees
- Path tracking with backtracking
- Global variables for tree-wide properties

---

## Prerequisites

**Must know:**
- Recursion fundamentals
- Class/object syntax in TypeScript
- Basic tree terminology

**Nice to have:**
- Stack/queue operations
- Backtracking concepts
- Binary search tree properties

---

## Success Criteria

You're ready to move on when you can:
- [ ] Implement all three DFS traversals from memory
- [ ] Calculate tree height/depth recursively
- [ ] Solve Easy tree problems in <15 min
- [ ] Identify when to use bottom-up vs top-down approach
- [ ] Handle edge cases (null root, single node, skewed tree)

---

## Resources

**Video:** See LESSON.md for link

**Readings:**
- Tree Visualizer: https://www.cs.usfca.edu/~galles/visualization/BST.html
- DFS patterns: TYPESCRIPT-LEETCODE.md

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Draw the tree** - Visualize before coding
2. **Start with base cases** - null check, leaf node
3. **Think recursively** - Trust the recursion
4. **Use helper functions** - Keep main function clean
5. **Consider both subtrees** - Don't forget either side
6. **Test edge cases** - Empty tree, single node, skewed
7. **Practice traversals** - Foundation for all tree problems

---

## Common Mistakes

**Avoid these:**
- ❌ Forgetting to handle null nodes
- ❌ Off-by-one errors in height/depth calculations
- ❌ Mixing up height vs depth terminology
- ❌ Not considering negative values in path problems
- ❌ Modifying the tree when not allowed

---

## What's Next

After completing this session:
1. Take a 10-minute break
2. Review your performance scores
3. Note patterns you struggled with
4. Move to Session 9: Tree BFS

Session 9 explores breadth-first search for level-order traversal and shortest path problems.

---

**Ready to start?** Say: `"Claude, start session 3 8"`