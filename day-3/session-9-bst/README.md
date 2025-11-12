# Day 3, Session 9: Binary Search Trees

## Overview

Master BSTs - the foundation for efficient searching, insertion, and sorted data operations.

**Duration:** 2-4 hours | **Problems:** 10 (3 Easy, 7 Medium)

---

## Learning Objectives

- ✅ Understand BST properties and invariants
- ✅ Implement BST operations (search, insert, delete)
- ✅ Validate BST structure efficiently
- ✅ Solve problems using BST properties
- ✅ Convert between BST and arrays

---

## Session Flow

### 1. Videos (42 min)
- BST Fundamentals (15 min)
- BST Operations (15 min)
- BST Problem Patterns (12 min)

### 2. Concept Check (10 min)
Quiz on BST property, operations, complexity, validation.

### 3. Tips & Tricks (5 min)
BST patterns, recursion vs iteration, TypeScript gotchas.

### 4. Problems (2-3 hours)
1. Search in a BST (Easy)
2. Validate Binary Search Tree (Medium)
3. Kth Smallest Element in BST (Medium)
4. Lowest Common Ancestor of BST (Medium)
5. Insert into a BST (Medium)
6. Delete Node in a BST (Medium)
7. Convert Sorted Array to BST (Easy)
8. Two Sum IV - Input is BST (Easy)
9. Serialize and Deserialize BST (Medium)
10. Inorder Successor in BST (Medium)

---

## Key Concepts

### BST Properties
- **Left subtree:** All values < root
- **Right subtree:** All values > root
- **Recursive:** Each subtree is also BST
- **Inorder:** Gives sorted sequence

### BST Operations
- **Search:** O(h) where h = height
- **Insert:** O(h)
- **Delete:** O(h)
- **Min/Max:** O(h)
- **Balanced:** h = O(log n)
- **Skewed:** h = O(n)

### Patterns
- Range validation with min/max
- Inorder traversal for sorted access
- Two pointers on sorted BST
- BST construction from sorted data

---

## Prerequisites

**Must know:**
- Binary tree structure
- Tree traversals (inorder, preorder, postorder)
- Recursion fundamentals

---

## Success Criteria

- [ ] Validate BST correctly
- [ ] Implement all basic BST operations
- [ ] Find kth element in O(k) time
- [ ] Handle BST deletion cases
- [ ] Explain BST time complexity

---

## Resources

**Video:** LESSON.md
**Practice:** PROBLEMS.md
**Solutions:** SOLUTIONS.md
**Hints:** HINTS.md

---

## Tips

1. Draw trees - visualization is critical
2. Use BST property to eliminate half
3. Inorder traversal gives sorted order
4. Start recursive, optimize to iterative
5. Watch for integer overflow in bounds
6. Handle null cases carefully
7. Practice deletion - most complex

---

## Common Mistakes

- ❌ Validating only immediate children
- ❌ Forgetting BST property applies to ALL nodes
- ❌ Not handling null pointers
- ❌ Assuming balanced tree
- ❌ Using node value instead of subtree min/max

---

## What's Next

After completion:
1. 10-minute break
2. Review scores
3. Note action items
4. Session 10: Tries

Session 10 introduces prefix trees for string operations.

---

**Ready?** Say: `"Claude, start session 3 9"`
