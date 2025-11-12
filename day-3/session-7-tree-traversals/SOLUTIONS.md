# Solutions - Session 7: Tree Traversals

Comprehensive TypeScript solutions with multiple approaches and complexity analysis.

---

## Problem 1: Binary Tree Inorder Traversal

### Approach 1: Recursive (Classic)

```typescript
function inorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];

  function traverse(node: TreeNode | null): void {
    if (!node) return;

    traverse(node.left);    // Visit left
    result.push(node.val);  // Process root
    traverse(node.right);   // Visit right
  }

  traverse(root);
  return result;
}
```

**Complexity:**
- Time: O(n) - visit each node once
- Space: O(h) - recursion stack, h = height

---

### Approach 2: Iterative with Stack

```typescript
function inorderTraversal(root: TreeNode | null): number[] {
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

    // Visit right
    current = current.right;
  }

  return result;
}
```

**Complexity:**
- Time: O(n)
- Space: O(h) - explicit stack

**Key Insight:** Simulate recursion. Go left fully, process node, then go right.

---

## Problem 2: Binary Tree Preorder Traversal

### Approach 1: Recursive

```typescript
function preorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];

  function traverse(node: TreeNode | null): void {
    if (!node) return;

    result.push(node.val);  // Root first
    traverse(node.left);    // Then left
    traverse(node.right);   // Then right
  }

  traverse(root);
  return result;
}
```

---

### Approach 2: Iterative with Stack

```typescript
function preorderTraversal(root: TreeNode | null): number[] {
  if (!root) return [];

  const result: number[] = [];
  const stack: TreeNode[] = [root];

  while (stack.length > 0) {
    const node = stack.pop()!;
    result.push(node.val);

    // Push right first (LIFO - left processed first)
    if (node.right) stack.push(node.right);
    if (node.left) stack.push(node.left);
  }

  return result;
}
```

**Complexity:**
- Time: O(n)
- Space: O(h)

**Key Pattern:** Process immediately, push children (right first).

---

## Problem 3: Binary Tree Postorder Traversal

### Approach 1: Recursive

```typescript
function postorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];

  function traverse(node: TreeNode | null): void {
    if (!node) return;

    traverse(node.left);    // Left first
    traverse(node.right);   // Then right
    result.push(node.val);  // Root last
  }

  traverse(root);
  return result;
}
```

---

### Approach 2: Iterative - Reverse Preorder

```typescript
function postorderTraversal(root: TreeNode | null): number[] {
  if (!root) return [];

  const result: number[] = [];
  const stack: TreeNode[] = [root];

  while (stack.length > 0) {
    const node = stack.pop()!;
    result.unshift(node.val); // Add to front

    // Push left first (right processed first)
    if (node.left) stack.push(node.left);
    if (node.right) stack.push(node.right);
  }

  return result;
}
```

**Key Insight:** Postorder is reverse of modified preorder (Root→Right→Left).

**Complexity:**
- Time: O(n)
- Space: O(h)

---

## Problem 4: Binary Tree Level Order Traversal

### Approach: BFS with Queue

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

**Complexity:**
- Time: O(n) - visit each node once
- Space: O(w) - w = maximum width

**Key Pattern:** Capture queue size to know level boundary.

---

## Problem 5: Binary Tree Zigzag Level Order Traversal

### Approach 1: BFS with Direction Flag

```typescript
function zigzagLevelOrder(root: TreeNode | null): number[][] {
  if (!root) return [];

  const result: number[][] = [];
  const queue: TreeNode[] = [root];
  let leftToRight = true;

  while (queue.length > 0) {
    const levelSize = queue.length;
    const currentLevel: number[] = [];

    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift()!;

      // Add based on direction
      if (leftToRight) {
        currentLevel.push(node.val);
      } else {
        currentLevel.unshift(node.val);
      }

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }

    result.push(currentLevel);
    leftToRight = !leftToRight;
  }

  return result;
}
```

---

### Approach 2: BFS with Reverse

```typescript
function zigzagLevelOrder(root: TreeNode | null): number[][] {
  if (!root) return [];

  const result: number[][] = [];
  let queue: TreeNode[] = [root];
  let level = 0;

  while (queue.length > 0) {
    const currentLevel: number[] = [];
    const nextQueue: TreeNode[] = [];

    for (const node of queue) {
      currentLevel.push(node.val);
      if (node.left) nextQueue.push(node.left);
      if (node.right) nextQueue.push(node.right);
    }

    // Reverse odd levels (0-indexed)
    if (level % 2 === 1) {
      currentLevel.reverse();
    }

    result.push(currentLevel);
    queue = nextQueue;
    level++;
  }

  return result;
}
```

**Complexity:**
- Time: O(n)
- Space: O(w)

---

## Problem 6: Binary Tree Right Side View

### Approach 1: BFS - Last Node Per Level

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

### Approach 2: DFS - Right First

```typescript
function rightSideView(root: TreeNode | null): number[] {
  const result: number[] = [];

  function dfs(node: TreeNode | null, depth: number): void {
    if (!node) return;

    // First node at this depth is rightmost
    if (depth === result.length) {
      result.push(node.val);
    }

    // Visit right first
    dfs(node.right, depth + 1);
    dfs(node.left, depth + 1);
  }

  dfs(root, 0);
  return result;
}
```

**Key Insight:** By visiting right first in DFS, first node at each depth is rightmost.

**Complexity:**
- Time: O(n)
- Space: O(h) DFS or O(w) BFS

---

## Problem 7: Average of Levels in Binary Tree

### Approach: BFS with Sum Calculation

```typescript
function averageOfLevels(root: TreeNode | null): number[] {
  if (!root) return [];

  const result: number[] = [];
  const queue: TreeNode[] = [root];

  while (queue.length > 0) {
    const levelSize = queue.length;
    let levelSum = 0;

    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift()!;
      levelSum += node.val;

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }

    result.push(levelSum / levelSize);
  }

  return result;
}
```

**Complexity:**
- Time: O(n)
- Space: O(w)

**Edge Case:** Handle potential overflow for large sums.

---

## Problem 8: N-ary Tree Level Order Traversal

### Approach: BFS for N-ary Tree

```typescript
class Node {
  val: number;
  children: Node[];
  constructor(val?: number) {
    this.val = (val === undefined ? 0 : val);
    this.children = [];
  }
}

function levelOrder(root: Node | null): number[][] {
  if (!root) return [];

  const result: number[][] = [];
  const queue: Node[] = [root];

  while (queue.length > 0) {
    const levelSize = queue.length;
    const currentLevel: number[] = [];

    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift()!;
      currentLevel.push(node.val);

      // Add all children
      for (const child of node.children) {
        queue.push(child);
      }
    }

    result.push(currentLevel);
  }

  return result;
}
```

**Key Difference:** Iterate through children array instead of left/right.

**Complexity:**
- Time: O(n)
- Space: O(w)

---

## Problem 9: Vertical Order Traversal of a Binary Tree

### Approach: BFS with Coordinates

```typescript
function verticalTraversal(root: TreeNode | null): number[][] {
  if (!root) return [];

  // Map: column -> list of [row, value] pairs
  const columnTable = new Map<number, [number, number][]>();
  const queue: [TreeNode, number, number][] = [[root, 0, 0]]; // [node, row, col]
  let minCol = 0, maxCol = 0;

  // BFS to collect nodes with coordinates
  while (queue.length > 0) {
    const [node, row, col] = queue.shift()!;

    if (!columnTable.has(col)) {
      columnTable.set(col, []);
    }
    columnTable.get(col)!.push([row, node.val]);

    minCol = Math.min(minCol, col);
    maxCol = Math.max(maxCol, col);

    if (node.left) queue.push([node.left, row + 1, col - 1]);
    if (node.right) queue.push([node.right, row + 1, col + 1]);
  }

  // Build result
  const result: number[][] = [];
  for (let col = minCol; col <= maxCol; col++) {
    const nodes = columnTable.get(col)!;
    // Sort by row, then by value if same row
    nodes.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);
    result.push(nodes.map(node => node[1]));
  }

  return result;
}
```

**Complexity:**
- Time: O(n log n) - due to sorting
- Space: O(n)

**Key Points:**
- Track (row, col) for each node
- Group by column
- Sort within each column by row, then value

---

## Problem 10: Binary Tree Level Order Traversal II

### Approach 1: BFS with Result Reversal

```typescript
function levelOrderBottom(root: TreeNode | null): number[][] {
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

  return result.reverse(); // Simply reverse
}
```

---

### Approach 2: Insert at Beginning

```typescript
function levelOrderBottom(root: TreeNode | null): number[][] {
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

    result.unshift(currentLevel); // Insert at beginning
  }

  return result;
}
```

**Trade-off:** `unshift` is O(n) per operation vs O(n) single reverse at end.

**Complexity:**
- Time: O(n)
- Space: O(w)

---

## Summary

### Time Complexity
All traversals: **O(n)** - visit each node once

### Space Complexity
- **Recursive DFS:** O(h) - call stack
- **Iterative DFS:** O(h) - explicit stack
- **BFS:** O(w) - queue width
- **Tree shape matters:** balanced h = log(n), skewed h = n

### Key Patterns
1. **DFS Recursive:** Natural and clean
2. **DFS Iterative:** Use stack, simulate recursion
3. **BFS:** Use queue, capture levelSize
4. **Advanced:** Track coordinates, use direction flags

### Interview Tips
- Always offer both recursive and iterative
- Discuss space complexity and tree shape
- Mention Morris traversal for O(1) space
- Handle edge cases: null, single node, skewed

---

[Back to Problems](./PROBLEMS.md) | [Back to Hints](./HINTS.md)
