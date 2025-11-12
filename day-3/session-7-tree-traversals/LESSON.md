# Lesson: Tree Traversals

---

## 📹 Video 1: Tree Fundamentals (15 min)

**"Introduction to Trees" by NeetCode**
https://www.youtube.com/watch?v=fAAZixBzIAI

**Focus on:**
- Binary tree structure
- Tree terminology (root, leaf, height, depth)
- TreeNode class definition
- When to use trees

---

## 📹 Video 2: DFS Traversals (20 min)

**"Tree Traversal Algorithms - Inorder, Preorder, Postorder" by NeetCode**
https://www.youtube.com/watch?v=fAAZixBzIAI

**Alternative:** "Binary Tree Algorithms" by freeCodeCamp
https://www.youtube.com/watch?v=fAAZixBzIAI

**Focus on:**
- Inorder (Left → Root → Right)
- Preorder (Root → Left → Right)
- Postorder (Left → Right → Root)
- Recursive vs iterative patterns

---

## 📹 Video 3: BFS Level Order Traversal (12 min)

**"Binary Tree Level Order Traversal" by NeetCode**
https://www.youtube.com/watch?v=6ZnyEApgFYg

**Focus on:**
- BFS vs DFS differences
- Queue-based implementation
- Processing nodes level by level
- When to use BFS

---

## 🌲 Tree Fundamentals

### What are Trees?

Trees are hierarchical data structures with nodes connected by edges. Each node has at most one parent (except root) and zero or more children.

**Key terminology:**
- **Root:** Top node with no parent
- **Leaf:** Node with no children
- **Height:** Longest path from node to leaf
- **Depth:** Distance from root to node
- **Binary Tree:** Each node has at most 2 children

---

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

**Example tree:**
```
    1
   / \
  2   3
 / \
4   5
```

**TypeScript:**
```typescript
const root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);
root.left.left = new TreeNode(4);
root.left.right = new TreeNode(5);
```

---

## 🌊 Depth-First Search (DFS) Traversals

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

**Example:**
```
Tree:  1          Inorder: [4, 2, 5, 1, 3]
      / \
     2   3
    / \
   4   5
```

**Complexity:**
- Time: O(n) - visit each node once
- Space: O(h) - recursion stack or explicit stack, h = height

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

    // Push right first so left is processed first (LIFO)
    if (node.right) stack.push(node.right);
    if (node.left) stack.push(node.left);
  }

  return result;
}
```

**Example:**
```
Tree:  1          Preorder: [1, 2, 4, 5, 3]
      / \
     2   3
    / \
   4   5
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

**Iterative Implementation (Reverse Preorder):**
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

**Example:**
```
Tree:  1          Postorder: [4, 5, 2, 3, 1]
      / \
     2   3
    / \
   4   5
```

**Memory Aid:** "Post" = root comes last (after children)

---

## 🌊 Breadth-First Search (BFS) - Level Order

### Level Order Traversal

**When to use:**
- Shortest path in unweighted tree
- Level-based operations
- Tree serialization by levels
- Finding nodes at specific depth

**Standard Implementation:**
```typescript
function levelOrder(root: TreeNode | null): number[][] {
  if (!root) return [];

  const result: number[][] = [];
  const queue: TreeNode[] = [root];

  while (queue.length > 0) {
    const levelSize = queue.length;
    const currentLevel: number[] = [];

    // Process all nodes at current level
    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift()!;
      currentLevel.push(node.val);

      // Add children for next level
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }

    result.push(currentLevel);
  }

  return result;
}
```

**Example:**
```
Tree:  1          Level Order: [[1], [2, 3], [4, 5]]
      / \
     2   3
    / \
   4   5
```

**Key Pattern:** Capture queue size before processing level to know how many nodes to process.

**Complexity:**
- Time: O(n) - visit each node once
- Space: O(w) - w = maximum width of tree (queue size)

---

## 🎯 Traversal Selection Guide

| Problem Type | Best Traversal | Why? |
|-------------|---------------|------|
| BST validation | Inorder | Gives sorted order |
| Find height/depth | Postorder | Need children info first |
| Serialize tree | Preorder/Level | Natural reconstruction |
| Shortest path | Level Order | Explores by distance |
| Delete tree | Postorder | Delete children first |
| Copy tree | Preorder | Create parent first |
| Level-based ops | Level Order | Direct access to levels |
| Right/left view | Level Order/DFS | Last/first node per level |

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

### Right Side View
Last node at each level:
```typescript
function rightSideView(root: TreeNode | null): number[] {
  if (!root) return [];

  const result: number[] = [];
  const queue: TreeNode[] = [root];

  while (queue.length > 0) {
    const levelSize = queue.length;

    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift()!;

      // Add only last node of level
      if (i === levelSize - 1) {
        result.push(node.val);
      }

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
  }

  return result;
}
```

---

## 🚀 Complexity Analysis

### Time Complexity
All traversals visit each node exactly once: **O(n)**

### Space Complexity

| Method | Space | Why? |
|--------|-------|------|
| Recursive DFS | O(h) | Call stack (h = height) |
| Iterative DFS | O(h) | Explicit stack |
| BFS | O(w) | Queue (w = max width) |
| Morris | O(1) | No stack/queue (advanced) |

**Tree shape matters:**
- Balanced tree: h = log(n)
- Skewed tree: h = n
- Perfect tree: w = n/2 (last level)

---

## 🎓 Interview Tips

### Common Follow-ups
1. "Can you do it iteratively?" - Always be ready
2. "What about space complexity?" - Consider tree shape
3. "Handle n-ary trees?" - Same patterns, iterate children
4. "O(1) space possible?" - Mention Morris traversal

### Edge Cases to Always Test
- `null` tree
- Single node
- Only left children (left-skewed)
- Only right children (right-skewed)
- Perfect binary tree

### Communication Tips
- "I'll use DFS because we need to process children before parent"
- "BFS would be better here since we need level-by-level processing"
- "The space complexity depends on tree shape - O(h) for balanced, O(n) for skewed"
- "Let me trace through a small example first"

---

## 🔄 Quick Reference

```typescript
// All DFS traversals in one visualization
function allDFS(root: TreeNode | null): void {
  if (!root) return;

  // PREORDER position (before recursion)
  console.log('Preorder:', root.val);

  allDFS(root.left);

  // INORDER position (between left and right)
  console.log('Inorder:', root.val);

  allDFS(root.right);

  // POSTORDER position (after recursion)
  console.log('Postorder:', root.val);
}
```

**Key Insight:** The position of processing determines the traversal type!

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **Inorder:** Left → Root → Right (BST sorted)
- **Preorder:** Root → Left → Right (Copy tree)
- **Postorder:** Left → Right → Root (Delete tree)
- **Level Order:** Level by level (BFS, use queue)
- **Recursive:** O(h) space (call stack)
- **Iterative:** O(h) DFS or O(w) BFS space

---

[Back to Session README](./README.md)
