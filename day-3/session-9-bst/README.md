# Day 3, Session 9: Binary Search Trees (BST)

## Overview
Master the fundamental tree data structure that enables efficient searching, insertion, and deletion operations.

**Duration:** 3-5 hours
**Problems:** 10 (3 Easy, 6 Medium, 1 Hard)
**Prerequisites:** Basic tree traversal, recursion concepts

---

## Learning Objectives

By the end of this session, you will:
- ✅ Understand BST properties and invariants
- ✅ Implement BST operations (search, insert, delete)
- ✅ Validate BST structure efficiently
- ✅ Solve BST-specific problems using properties
- ✅ Convert between BST and other data structures

---

## Session Flow

### 1. Video (25 min)
Watch the assigned video on Binary Search Tree fundamentals and operations.

### 2. Concept Check (10 min)
Claude will quiz you on:
- BST property (left < root < right)
- Inorder traversal produces sorted sequence
- Time complexity of operations
- Balanced vs unbalanced BST

### 3. Tips & Tricks (5 min)
Learn interview-specific insights about:
- Using BST properties to optimize solutions
- When to use iterative vs recursive approaches
- Common BST patterns in interviews

### 4. Problem Solving (3-4 hours)
Solve 10 carefully selected problems:
1. Search in a BST (Easy)
2. Validate Binary Search Tree (Medium)
3. Kth Smallest Element in a BST (Medium)
4. Lowest Common Ancestor of a BST (Medium)
5. Insert into a BST (Medium)
6. Delete Node in a BST (Medium)
7. Convert Sorted Array to BST (Easy)
8. Two Sum IV - Input is a BST (Easy)
9. Serialize and Deserialize BST (Medium)
10. Recover Binary Search Tree (Hard)

---

## Key Concepts

### BST Properties
- **Left subtree:** All values < root
- **Right subtree:** All values > root
- **Recursive property:** Each subtree is also a BST
- **Inorder traversal:** Gives sorted sequence
- **No duplicates:** Standard BST has unique values

### BST Operations Complexity
- **Search:** O(h) where h = height
- **Insert:** O(h)
- **Delete:** O(h)
- **Min/Max:** O(h)
- **Balanced BST:** h = O(log n)
- **Skewed BST:** h = O(n)

### Common Patterns
- Inorder traversal for sorted access
- Range validation using min/max bounds
- Successor/predecessor finding
- BST construction from sorted data
- Two-pointer on BST (using sorted property)

---

## Prerequisites

**Must know:**
- Binary tree traversals (inorder, preorder, postorder)
- Recursion fundamentals
- Tree node structure in TypeScript

**Nice to have:**
- Understanding of balanced trees
- Iterator pattern knowledge
- Serialization concepts

---

## Success Criteria

You're ready to move on when you can:
- [ ] Validate if a tree is a BST efficiently
- [ ] Implement all basic BST operations
- [ ] Find kth smallest/largest element
- [ ] Convert between BST and arrays
- [ ] Handle BST deletion cases correctly

---

## Resources

**Video:** See LESSON.md for link

**Readings:**
- BST Visualization: https://visualgo.net/en/bst
- TypeScript tree patterns: TYPESCRIPT-LEETCODE.md

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Draw the tree** - Visualize operations step by step
2. **Use BST property** - Many problems become easier
3. **Consider edge cases** - Single node, skewed tree
4. **Practice inorder traversal** - It's used frequently
5. **Understand deletion** - Most complex BST operation
6. **Try both approaches** - Recursive and iterative
7. **Watch for overflow** - When dealing with ranges

---

## Common Mistakes

**Avoid these:**
- ❌ Forgetting to check both subtrees for BST validation
- ❌ Using node values instead of subtree min/max
- ❌ Not handling null nodes in recursion
- ❌ Modifying tree structure without permission
- ❌ Assuming balanced tree when not specified

---

## What's Next

After completing this session:
1. Take a 15-minute break
2. Review your performance scores
3. Note patterns you struggled with
4. Move to Session 10: Tries

Session 10 introduces prefix trees for efficient string operations.

---

**Ready to start?** Say: `"Claude, start session 3 9"`