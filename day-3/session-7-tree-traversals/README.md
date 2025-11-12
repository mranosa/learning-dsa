# Day 3, Session 7: Tree Traversals

## Overview

Master tree traversal patterns - the foundation for all tree-based interview problems.

**Duration:** 2-4 hours | **Problems:** 10 (4 Easy, 6 Medium)

---

## Learning Objectives

- ✅ Master all four traversal methods (Inorder, Preorder, Postorder, Level Order)
- ✅ Understand recursive vs iterative implementations
- ✅ Recognize when to use BFS vs DFS
- ✅ Apply traversals to complex tree problems
- ✅ Analyze space complexity for each method

---

## Session Flow

### 1. Videos (47 min)
- Tree Fundamentals (15 min)
- DFS Traversals - Inorder, Preorder, Postorder (20 min)
- BFS Level Order Traversal (12 min)

### 2. Concept Check (10 min)
Quiz on traversal orders, BFS vs DFS, space complexity.

### 3. Tips & Tricks (5 min)
Traversal selection, implementation patterns, TypeScript gotchas.

### 4. Problems (2-3 hours)
1. Binary Tree Inorder Traversal (Easy)
2. Binary Tree Preorder Traversal (Easy)
3. Binary Tree Postorder Traversal (Easy)
4. Binary Tree Level Order Traversal (Medium)
5. Binary Tree Zigzag Level Order Traversal (Medium)
6. Binary Tree Right Side View (Medium)
7. Average of Levels in Binary Tree (Easy)
8. N-ary Tree Level Order Traversal (Medium)
9. Vertical Order Traversal of a Binary Tree (Medium)
10. Binary Tree Level Order Traversal II (Medium)

---

## Key Concepts

### DFS Traversals (Depth-First Search)
- **Inorder** (Left → Root → Right) - BST sorted order
- **Preorder** (Root → Left → Right) - Tree copying
- **Postorder** (Left → Right → Root) - Tree deletion

### BFS Traversal (Breadth-First Search)
- **Level Order** - Process level by level
- Uses queue data structure
- Good for shortest path, level-based operations

### Complexity
- **Time:** O(n) - visit each node once
- **Space:** O(h) DFS recursion, O(w) BFS queue
- h = height, w = max width

### Patterns
- Level-by-level processing
- Zigzag/spiral traversal
- Right/left view problems
- Vertical order grouping

---

## Prerequisites

**Must know:**
- Tree node structure (TreeNode class)
- Basic recursion
- Queue and stack operations

---

## Success Criteria

- [ ] Implement all traversals recursively and iteratively
- [ ] Choose right traversal for problem
- [ ] Solve Easy problems <10 min
- [ ] Handle edge cases (null, single node)
- [ ] Analyze space complexity correctly

---

## Resources

**Video:** LESSON.md
**Practice:** PROBLEMS.md
**Solutions:** SOLUTIONS.md
**Hints:** HINTS.md

---

## Tips

1. Watch all videos - foundation is critical
2. Do concept check - reveals gaps
3. Start with Easy problems
4. Draw trees - visualize before coding
5. Master recursive first, then iterative
6. Test edge cases
7. Review solutions even if correct

---

## Common Mistakes

- ❌ Confusing traversal orders
- ❌ Forgetting null checks
- ❌ Using wrong data structure (stack vs queue)
- ❌ Not considering recursion stack space
- ❌ Mutating tree without permission

---

## What's Next

After completion:
1. 10-minute break
2. Review scores
3. Note action items
4. Session 8: Tree Construction

Session 8 builds on traversals by teaching tree construction and modification.

---

**Ready?** Say: `"Claude, start session 3 7"`
