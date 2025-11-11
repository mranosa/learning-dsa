# Binary Search Trees (BST) - Learning Guide

## Introduction

Binary Search Trees are the foundation of many advanced data structures and algorithms. They provide O(log n) operations when balanced, making them essential for efficient data management.

---

## Video Lesson

### Primary Video (MUST WATCH)
**NeetCode - Binary Search Trees Explained**
- Link: https://www.youtube.com/watch?v=bOjKxTUpUho
- Duration: 15 minutes
- Topics: BST properties, operations, complexity

### Supplementary Videos
1. **BST Operations Deep Dive**
   - Focus on insertion and deletion
   - Understand all deletion cases

2. **BST vs Hash Table**
   - When to use each
   - Trade-offs in real applications

---

## Core Concepts

### 1. BST Definition

A Binary Search Tree is a binary tree where:
```typescript
// For every node:
// - All values in left subtree < node.val
// - All values in right subtree > node.val

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val: number = 0) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}
```

### 2. BST Properties

**Invariant:** The BST property must hold for ALL nodes, not just the root.

```typescript
// Valid BST
    5
   / \
  3   8
 / \ / \
1  4 7  9

// Invalid BST (4 is not less than root 5's ancestor)
    5
   / \
  3   8
 / \ / \
1  6 7  9  // 6 > 5, breaks BST property
```

### 3. Inorder Traversal

**Key Insight:** Inorder traversal of a BST gives sorted order.

```typescript
function inorderTraversal(root: TreeNode | null): number[] {
    const result: number[] = [];

    function inorder(node: TreeNode | null): void {
        if (!node) return;

        inorder(node.left);   // Process left
        result.push(node.val); // Process root
        inorder(node.right);  // Process right
    }

    inorder(root);
    return result; // Returns sorted array!
}
```

---

## Essential Operations

### 1. Search - O(h)

```typescript
function searchBST(root: TreeNode | null, val: number): TreeNode | null {
    // Base case
    if (!root || root.val === val) return root;

    // BST property guides search
    if (val < root.val) {
        return searchBST(root.left, val);
    } else {
        return searchBST(root.right, val);
    }
}

// Iterative version (often preferred)
function searchBSTIterative(root: TreeNode | null, val: number): TreeNode | null {
    let current = root;

    while (current) {
        if (val === current.val) return current;
        current = val < current.val ? current.left : current.right;
    }

    return null;
}
```

### 2. Insert - O(h)

```typescript
function insertIntoBST(root: TreeNode | null, val: number): TreeNode {
    // Empty tree
    if (!root) return new TreeNode(val);

    // Recursive insert maintaining BST property
    if (val < root.val) {
        root.left = insertIntoBST(root.left, val);
    } else {
        root.right = insertIntoBST(root.right, val);
    }

    return root;
}
```

### 3. Delete - O(h)

The most complex operation with three cases:

```typescript
function deleteNode(root: TreeNode | null, key: number): TreeNode | null {
    if (!root) return null;

    // Find the node
    if (key < root.val) {
        root.left = deleteNode(root.left, key);
    } else if (key > root.val) {
        root.right = deleteNode(root.right, key);
    } else {
        // Found the node to delete

        // Case 1: Leaf node
        if (!root.left && !root.right) return null;

        // Case 2: One child
        if (!root.left) return root.right;
        if (!root.right) return root.left;

        // Case 3: Two children
        // Find inorder successor (min in right subtree)
        let minNode = root.right;
        while (minNode.left) {
            minNode = minNode.left;
        }

        // Replace value with successor
        root.val = minNode.val;

        // Delete successor
        root.right = deleteNode(root.right, minNode.val);
    }

    return root;
}
```

### 4. Find Min/Max - O(h)

```typescript
function findMin(root: TreeNode): number {
    while (root.left) {
        root = root.left;
    }
    return root.val;
}

function findMax(root: TreeNode): number {
    while (root.right) {
        root = root.right;
    }
    return root.val;
}
```

---

## Advanced Patterns

### 1. Range Validation

Use min/max bounds to validate BST:

```typescript
function isValidBST(root: TreeNode | null): boolean {
    return validate(root, -Infinity, Infinity);
}

function validate(
    node: TreeNode | null,
    min: number,
    max: number
): boolean {
    if (!node) return true;

    if (node.val <= min || node.val >= max) {
        return false;
    }

    return validate(node.left, min, node.val) &&
           validate(node.right, node.val, max);
}
```

### 2. Kth Smallest Element

Use inorder traversal property:

```typescript
function kthSmallest(root: TreeNode | null, k: number): number {
    let count = 0;
    let result = 0;

    function inorder(node: TreeNode | null): void {
        if (!node || count >= k) return;

        inorder(node.left);

        count++;
        if (count === k) {
            result = node.val;
            return;
        }

        inorder(node.right);
    }

    inorder(root);
    return result;
}
```

### 3. LCA in BST

Leverage BST property for efficiency:

```typescript
function lowestCommonAncestor(
    root: TreeNode,
    p: TreeNode,
    q: TreeNode
): TreeNode {
    // Both on left
    if (p.val < root.val && q.val < root.val) {
        return lowestCommonAncestor(root.left!, p, q);
    }

    // Both on right
    if (p.val > root.val && q.val > root.val) {
        return lowestCommonAncestor(root.right!, p, q);
    }

    // Split or one is root
    return root;
}
```

---

## Interview Tips

### Pattern Recognition

1. **"Sorted" mentioned?** → Think BST inorder
2. **"Kth element"?** → Inorder traversal with counter
3. **"Range queries"?** → BST navigation
4. **"Validate structure"?** → Range bounds approach

### Time Complexity Analysis

| Operation | Balanced BST | Skewed BST |
|-----------|-------------|------------|
| Search    | O(log n)    | O(n)       |
| Insert    | O(log n)    | O(n)       |
| Delete    | O(log n)    | O(n)       |
| Min/Max   | O(log n)    | O(n)       |

### Space Complexity

- Recursive approaches: O(h) call stack
- Iterative approaches: O(1) auxiliary space
- Height h = O(log n) balanced, O(n) worst case

---

## Common Pitfalls

### 1. Validation Mistakes

```typescript
// WRONG: Only checks immediate parent
function wrongValidation(root: TreeNode): boolean {
    if (!root) return true;

    if (root.left && root.left.val >= root.val) return false;
    if (root.right && root.right.val <= root.val) return false;

    return wrongValidation(root.left) && wrongValidation(root.right);
}

// This fails for:
//     10
//    /  \
//   5    15
//  / \
// 3   20  // 20 > 10, breaks BST property!
```

### 2. Modification Without Permission

Always ask: "Can I modify the tree structure?"

### 3. Integer Overflow

When using Integer.MAX_VALUE/MIN_VALUE as bounds, be careful with edge values.

---

## Practice Progression

1. **Start with:** Search, validation
2. **Then try:** Insert, kth smallest
3. **Advanced:** Delete, serialize/deserialize
4. **Challenge:** Recover BST, optimize operations

---

## Real-World Applications

- **Database Indexes:** B-trees are generalized BSTs
- **File Systems:** Directory structures
- **Priority Queues:** Via balanced BSTs
- **Autocomplete:** Combined with tries
- **Range Queries:** Efficient min/max in range

---

## Quick Reference

```typescript
// BST Template
class BST {
    root: TreeNode | null = null;

    search(val: number): boolean {
        // O(h) time, O(1) space iterative
    }

    insert(val: number): void {
        // O(h) time, O(h) space recursive
    }

    delete(val: number): void {
        // O(h) time, O(h) space
        // 3 cases: leaf, 1 child, 2 children
    }

    validate(): boolean {
        // Use range bounds: O(n) time, O(h) space
    }

    kthSmallest(k: number): number {
        // Inorder traversal: O(k) time
    }
}
```

**Ready to solve problems?** Open PROBLEMS.md!