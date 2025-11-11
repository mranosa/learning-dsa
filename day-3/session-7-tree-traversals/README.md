# Day 3, Session 7: Tree Traversals

## Overview
Master the fundamental tree traversal patterns - the foundation of all tree-based interview problems.

**Duration:** 3-5 hours
**Problems:** 10 (4 Easy, 5 Medium, 1 Hard)
**Prerequisites:** Basic tree structure understanding, recursion

---

## Learning Objectives

By the end of this session, you will:
- ✅ Master all four primary traversal methods (Inorder, Preorder, Postorder, Level Order)
- ✅ Understand recursive vs iterative implementations
- ✅ Recognize when to use BFS vs DFS
- ✅ Handle special traversal patterns (zigzag, vertical, right view)
- ✅ Apply traversals to solve complex tree problems

---

## Session Flow

### 1. Video (25 min)
Watch the assigned videos on tree traversal techniques.

### 2. Concept Check (10 min)
Claude will quiz you on:
- DFS traversal orders
- BFS vs DFS trade-offs
- Recursive vs iterative approaches
- Space complexity of each method

### 3. Tips & Tricks (5 min)
Learn interview-specific insights about:
- When to use each traversal type
- Common traversal patterns
- TypeScript tree implementation gotchas

### 4. Problem Solving (3-4 hours)
Solve 10 carefully selected problems:
1. Binary Tree Inorder Traversal (Easy)
2. Binary Tree Preorder Traversal (Easy)
3. Binary Tree Postorder Traversal (Easy)
4. Binary Tree Level Order Traversal (Medium)
5. Binary Tree Zigzag Level Order Traversal (Medium)
6. Binary Tree Right Side View (Medium)
7. Average of Levels in Binary Tree (Easy)
8. N-ary Tree Level Order Traversal (Medium)
9. Vertical Order Traversal of a Binary Tree (Hard)
10. Binary Tree Level Order Traversal II (Medium)

---

## Key Concepts

### DFS Traversals (Depth-First Search)
- **Inorder** (Left → Root → Right) - BST sorted order
- **Preorder** (Root → Left → Right) - Tree copying/serialization
- **Postorder** (Left → Right → Root) - Tree deletion/cleanup

### BFS Traversal (Breadth-First Search)
- **Level Order** - Process nodes level by level
- Uses queue data structure
- Good for shortest path, level-based operations

### Implementation Approaches
- **Recursive:** Natural for DFS, clean code, O(h) call stack
- **Iterative:** Explicit stack/queue, no recursion limit
- **Morris Traversal:** O(1) space but modifies tree temporarily

### Common Patterns
- Level-by-level processing
- Zigzag/spiral traversal
- Vertical order traversal
- Boundary/view problems

---

## Prerequisites

**Must know:**
- Tree node structure and pointers
- Basic recursion concepts
- Queue and stack operations

**Nice to have:**
- Understanding of tree height and depth
- Experience with recursive thinking
- Familiarity with BFS/DFS concepts

---

## Success Criteria

You're ready to move on when you can:
- [ ] Implement all traversals both recursively and iteratively
- [ ] Choose the right traversal for a given problem
- [ ] Solve Easy traversal problems in <10 min
- [ ] Handle edge cases (empty tree, single node)
- [ ] Analyze space complexity correctly

---

## Resources

**Videos:** See LESSON.md for links

**Readings:**
- Tree Traversal Visualization: https://www.cs.usfca.edu/~galles/visualization/BTree.html
- TypeScript tree utilities: TYPESCRIPT-LEETCODE.md

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Draw the tree** - Visualize before coding
2. **Trace through small examples** - Single node, two nodes, three nodes
3. **Master recursive first** - Then learn iterative
4. **Understand the pattern** - Don't memorize code
5. **Practice switching** - Between traversal types
6. **Consider space complexity** - Recursion uses O(h) stack
7. **Test edge cases** - Empty tree, skewed tree

---

## Common Mistakes

**Avoid these:**
- ❌ Confusing traversal orders (especially inorder vs preorder)
- ❌ Forgetting to handle null/undefined nodes
- ❌ Using wrong data structure (stack vs queue)
- ❌ Not considering recursion stack space in complexity
- ❌ Modifying tree without permission

---

## What's Next

After completing this session:
1. Take a 10-minute break
2. Review your performance scores
3. Note patterns you struggled with
4. Move to Session 8: Tree Construction

Session 8 builds on traversals by teaching you to construct and modify trees.

---

**Ready to start?** Say: `"Claude, start session 3 7"`