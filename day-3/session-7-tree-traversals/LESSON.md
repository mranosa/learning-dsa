# Lesson: Tree Traversals

## 📹 Video Assignment (25 minutes)

**Primary Videos:**
1. "Tree Traversal Algorithms" by NeetCode (12 min)
   https://www.youtube.com/watch?v=fAAZixBzIAI

2. "Binary Tree Level Order Traversal - BFS" by NeetCode (8 min)
   https://www.youtube.com/watch?v=6ZnyEApgFYg

**Alternative Videos** (if you need different explanations):
- "Binary Tree Algorithms for Technical Interviews" by freeCodeCamp (2 hours): https://www.youtube.com/watch?v=fAAZixBzIAI
- "Tree Traversals (Inorder, Preorder, Postorder)" by Abdul Bari (18 min): https://www.youtube.com/watch?v=9RHO6jU--GU

**What to focus on:**
- Understanding DFS vs BFS conceptually
- The order of operations for each traversal
- When to use recursion vs iteration
- Common applications of each traversal type

---

## 📚 Tree Traversals - Core Concepts

### What are Tree Traversals?

Tree traversal is the process of visiting each node in a tree data structure exactly once. The order in which nodes are visited defines the traversal type.

**Key insight:** Different problems require different visiting orders. Master all patterns!

### Tree Node Structure (TypeScript)

```typescript
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;

  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
  }
}
```

---

## 🌲 Depth-First Search (DFS) Traversals

### Inorder Traversal (Left → Root → Right)

**When to use:**
- BST problems (gives sorted order)
- Finding kth smallest/largest
- Validating BST

**Recursive Implementation:**
```typescript
function inorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];

  function traverse(node: TreeNode | null): void {
    if (!node) return;

    traverse(node.left);    // Left
    result.push(node.val);  // Root
    traverse(node.right);   // Right
  }

  traverse(root);
  return result;
}
```

**Iterative Implementation:**
```typescript
function inorderIterative(root: TreeNode | null): number[] {
  const result: number[] = [];
  const stack: TreeNode[] = [];
  let current = root;

  while (current || stack.length > 0) {
    // Go to leftmost node
    while (current) {
      stack.push(current);
      current = current.left;
    }

    // Process node
    current = stack.pop()!;
    result.push(current.val);

    // Move to right
    current = current.right;
  }

  return result;
}
```

**Memory Aid:** "In" = values are "in order" for BST

---

### Preorder Traversal (Root → Left → Right)

**When to use:**
- Tree/subtree copying
- Serialization
- Prefix expression evaluation

**Recursive Implementation:**
```typescript
function preorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];

  function traverse(node: TreeNode | null): void {
    if (!node) return;

    result.push(node.val);  // Root
    traverse(node.left);    // Left
    traverse(node.right);   // Right
  }

  traverse(root);
  return result;
}
```

**Iterative Implementation:**
```typescript
function preorderIterative(root: TreeNode | null): number[] {
  if (!root) return [];

  const result: number[] = [];
  const stack: TreeNode[] = [root];

  while (stack.length > 0) {
    const node = stack.pop()!;
    result.push(node.val);

    // Push right first so left is processed first
    if (node.right) stack.push(node.right);
    if (node.left) stack.push(node.left);
  }

  return result;
}
```

**Memory Aid:** "Pre" = root comes first (before children)

---

### Postorder Traversal (Left → Right → Root)

**When to use:**
- Tree deletion (delete children first)
- Calculating heights/sizes
- Postfix expression evaluation

**Recursive Implementation:**
```typescript
function postorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];

  function traverse(node: TreeNode | null): void {
    if (!node) return;

    traverse(node.left);    // Left
    traverse(node.right);   // Right
    result.push(node.val);  // Root
  }

  traverse(root);
  return result;
}
```

**Iterative Implementation:**
```typescript
function postorderIterative(root: TreeNode | null): number[] {
  if (!root) return [];

  const result: number[] = [];
  const stack: TreeNode[] = [root];

  while (stack.length > 0) {
    const node = stack.pop()!;
    result.unshift(node.val); // Add to front

    // Push left first so right is processed first
    if (node.left) stack.push(node.left);
    if (node.right) stack.push(node.right);
  }

  return result;
}
```

**Memory Aid:** "Post" = root comes last (after children)

---

## 🌊 Breadth-First Search (BFS) - Level Order

### Level Order Traversal

**When to use:**
- Shortest path in unweighted tree
- Level-based operations
- Tree serialization by levels

**Standard Implementation:**
```typescript
function levelOrder(root: TreeNode | null): number[][] {
  if (!root) return [];

  const result: number[][] = [];
  const queue: TreeNode[] = [root];

  while (queue.length > 0) {
    const levelSize = queue.length;
    const currentLevel: number[] = [];

    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift()!;
      currentLevel.push(node.val);

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }

    result.push(currentLevel);
  }

  return result;
}
```

**Key Pattern:** Process nodes level by level using queue size

---

## 🎯 Traversal Selection Guide

| Problem Type | Best Traversal | Why? |
|-------------|---------------|------|
| BST validation | Inorder | Gives sorted order |
| Find height | Postorder | Need children info first |
| Serialize tree | Preorder/Level | Natural reconstruction |
| Shortest path | Level Order | Explores by distance |
| Delete tree | Postorder | Delete children first |
| Copy tree | Preorder | Create parent first |

---

## 💡 Advanced Patterns

### Zigzag Level Order
Alternate direction each level:
```typescript
function zigzagLevelOrder(root: TreeNode | null): number[][] {
  if (!root) return [];

  const result: number[][] = [];
  const queue: TreeNode[] = [root];
  let leftToRight = true;

  while (queue.length > 0) {
    const levelSize = queue.length;
    const level: number[] = [];

    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift()!;

      // Add based on direction
      if (leftToRight) {
        level.push(node.val);
      } else {
        level.unshift(node.val);
      }

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }

    result.push(level);
    leftToRight = !leftToRight;
  }

  return result;
}
```

### Vertical Order Traversal
Group nodes by vertical position:
```typescript
function verticalOrder(root: TreeNode | null): number[][] {
  if (!root) return [];

  const columnTable = new Map<number, number[]>();
  const queue: [TreeNode, number][] = [[root, 0]];
  let minCol = 0, maxCol = 0;

  while (queue.length > 0) {
    const [node, col] = queue.shift()!;

    if (!columnTable.has(col)) {
      columnTable.set(col, []);
    }
    columnTable.get(col)!.push(node.val);

    minCol = Math.min(minCol, col);
    maxCol = Math.max(maxCol, col);

    if (node.left) queue.push([node.left, col - 1]);
    if (node.right) queue.push([node.right, col + 1]);
  }

  const result: number[][] = [];
  for (let i = minCol; i <= maxCol; i++) {
    result.push(columnTable.get(i)!);
  }

  return result;
}
```

---

## 🚀 Performance Analysis

### Time Complexity
All traversals visit each node exactly once: **O(n)**

### Space Complexity

| Method | Space | Why? |
|--------|-------|------|
| Recursive DFS | O(h) | Call stack (h = height) |
| Iterative DFS | O(h) | Explicit stack |
| BFS | O(w) | Queue (w = max width) |
| Morris | O(1) | No stack/queue |

**Note:** For balanced tree: h = log(n), For skewed tree: h = n

---

## 🎓 Interview Tips

### Common Follow-ups
1. "Can you do it iteratively?" - Always be ready
2. "What about space complexity?" - Consider tree shape
3. "Handle n-ary trees?" - Same patterns, multiple children
4. "Morris traversal?" - Mention O(1) space trade-off

### Edge Cases to Always Test
- `null` tree
- Single node
- Only left children (left-skewed)
- Only right children (right-skewed)
- Perfect binary tree

### Communication Tips
- "I'll use DFS because..."
- "BFS would be better here since..."
- "The space complexity depends on tree shape..."
- "Let me trace through a small example..."

---

## 🔄 Quick Reference

```typescript
// All DFS in one place
function allDFS(root: TreeNode | null): void {
  if (!root) return;

  // Preorder position
  console.log(root.val);

  allDFS(root.left);

  // Inorder position
  console.log(root.val);

  allDFS(root.right);

  // Postorder position
  console.log(root.val);
}
```

Remember: The position of the processing determines the traversal type!