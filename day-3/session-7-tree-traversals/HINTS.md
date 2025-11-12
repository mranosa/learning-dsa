# Hints - Session 7: Tree Traversals

Progressive hints for 10 problems. Struggling is part of learning.

---

## Problem 1: Binary Tree Inorder Traversal

### Level 1
Inorder: Left → Root → Right. Iterative: simulate recursion with stack.

### Level 2
Use stack and pointer. Keep going left, push nodes. When can't go left, pop, process, go right.

### Level 3
```typescript
const stack: TreeNode[] = [];
let current = root;
while (current || stack.length > 0) {
  while (current) {
    stack.push(current);
    current = current.left;
  }
  current = stack.pop()!;
  result.push(current.val);
  current = current.right;
}
```

---

## Problem 2: Binary Tree Preorder Traversal

### Level 1
Preorder: Root → Left → Right. Process node immediately when encountered.

### Level 2
Use stack. Process node when popped. Push right first, then left (LIFO).

### Level 3
```typescript
const stack = [root];
while (stack.length > 0) {
  const node = stack.pop()!;
  result.push(node.val);
  if (node.right) stack.push(node.right);
  if (node.left) stack.push(node.left);
}
```

---

## Problem 3: Binary Tree Postorder Traversal

### Level 1
Postorder is tricky. What's reverse of postorder? Modified preorder!

### Level 2
Postorder (L→R→Root) reversed is (Root→R→L). Do modified preorder, reverse result.

### Level 3
```typescript
stack.push(root);
while (stack.length) {
  const node = stack.pop()!;
  result.unshift(node.val); // Add to front
  if (node.left) stack.push(node.left);
  if (node.right) stack.push(node.right);
}
```

---

## Problem 4: Binary Tree Level Order Traversal

### Level 1
BFS uses queue. Process all nodes at current level before next.

### Level 2
Key: Capture `queue.length` before processing level. That's how many nodes in current level.

### Level 3
```typescript
const queue = [root];
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
```

---

## Problem 5: Binary Tree Zigzag Level Order Traversal

### Level 1
Level order with alternating direction. Use boolean flag.

### Level 2
Two approaches:
1. Add differently based on direction (push vs unshift)
2. Always add normally, reverse alternate levels

### Level 3
```typescript
let leftToRight = true;
// In level processing:
if (leftToRight) {
  currentLevel.push(node.val);
} else {
  currentLevel.unshift(node.val);
}
// After level:
leftToRight = !leftToRight;
```

---

## Problem 6: Binary Tree Right Side View

### Level 1
Want rightmost node at each level. Level order variant.

### Level 2
BFS: Last node of each level is visible from right. Only add that to result.

### Level 3
```typescript
for (let i = 0; i < levelSize; i++) {
  const node = queue.shift()!;
  if (i === levelSize - 1) { // Last node
    result.push(node.val);
  }
  // Add children
}
```

---

## Problem 7: Average of Levels in Binary Tree

### Level 1
Level order, but calculate sum and count per level.

### Level 2
For each level, sum all values, divide by number of nodes (levelSize).

### Level 3
```typescript
const levelSize = queue.length;
let levelSum = 0;
for (let i = 0; i < levelSize; i++) {
  const node = queue.shift()!;
  levelSum += node.val;
  // Add children
}
result.push(levelSum / levelSize);
```

---

## Problem 8: N-ary Tree Level Order Traversal

### Level 1
Same as binary tree level order, but children array instead of left/right.

### Level 2
When adding children, iterate through children array.

### Level 3
Replace:
```typescript
if (node.left) queue.push(node.left);
if (node.right) queue.push(node.right);
```
With:
```typescript
for (const child of node.children) {
  queue.push(child);
}
```

---

## Problem 9: Vertical Order Traversal of a Binary Tree

### Level 1
Assign (row, col) to each node. Root at (0, 0). Left child (row+1, col-1), right (row+1, col+1).

### Level 2
Use Map to group by column. Within each column, sort by row then value.

### Level 3
```typescript
// Map<col, Array<[row, value]>>
const columnTable = new Map<number, [number, number][]>();
// BFS with [node, row, col]
const queue: [TreeNode, number, number][] = [[root, 0, 0]];
// Group by column
// Sort each column by row, then value
nodes.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);
```

---

## Problem 10: Binary Tree Level Order Traversal II

### Level 1
Regular level order, but bottom-up. Easiest: reverse result.

### Level 2
Two options:
1. Normal level order, call `result.reverse()` at end
2. Use `result.unshift(currentLevel)` to add at beginning

### Level 3
```typescript
// Option 1: Reverse at end
return result.reverse();

// Option 2: Insert at beginning
result.unshift(currentLevel); // Instead of push
```

---

## Pattern Hints

**"Level order"** → BFS with queue, capture levelSize

**"Right/left view"** → Last/first node per level

**"Zigzag"** → Alternate direction flag

**"Vertical"** → Track coordinates, group by column

**"Inorder BST"** → Gives sorted order

**"Postorder"** → Process children before parent

---

## Using Hints Effectively

1. Try 10+ min before Level 1
2. Try 5+ min after each hint
3. If use Level 3, mark for review
4. Don't feel bad - hints aid learning

Goal: Learn pattern, not just solve one problem.

---

[Back to Problems](./PROBLEMS.md) | [Back to Solutions](./SOLUTIONS.md)
