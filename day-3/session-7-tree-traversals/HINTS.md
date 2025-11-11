# Hints - Session 7: Tree Traversals

Progressive hints for all 10 problems. Use sparingly - struggling is part of learning!

---

## Problem 1: Binary Tree Inorder Traversal

### Hint Level 1 (Gentle Nudge)
Remember the order: Left → Root → Right. For the iterative approach, think about how you can simulate the recursion stack manually.

### Hint Level 2 (More Direct)
For iterative: Use a stack and a pointer. Keep going left and pushing nodes onto the stack. When you can't go left anymore, pop from stack, process that node, then go right.

### Hint Level 3 (Step-by-Step)
Complete iterative algorithm:
1. Initialize empty `stack` and `current = root`
2. While `current` exists OR stack not empty:
   - While `current` exists: push to stack, go left
   - Pop from stack, add value to result
   - Set `current = popped.right`

---

## Problem 2: Binary Tree Preorder Traversal

### Hint Level 1
Preorder means process the root BEFORE its children. For iterative, you'll process nodes as soon as you encounter them.

### Hint Level 2
Use a stack. Process node immediately when popped. Push right child first, then left child (so left is processed first due to LIFO).

### Hint Level 3
```typescript
const stack = [root];
while (stack.length > 0) {
  const node = stack.pop();
  result.push(node.val);
  if (node.right) stack.push(node.right);
  if (node.left) stack.push(node.left);
}
```

---

## Problem 3: Binary Tree Postorder Traversal

### Hint Level 1
Postorder is tricky iteratively. Think: what's the reverse of postorder? Can you modify another traversal and reverse the result?

### Hint Level 2
Postorder (L→R→Root) reversed is (Root→R→L). This is like preorder but visiting right before left! Do modified preorder and reverse.

### Hint Level 3
Do preorder but visit right child before left. Add values to front of result (or reverse at end):
```typescript
stack.push(root);
while (stack.length) {
  const node = stack.pop();
  result.unshift(node.val); // Add to front
  if (node.left) stack.push(node.left);
  if (node.right) stack.push(node.right);
}
```

---

## Problem 4: Binary Tree Level Order Traversal

### Hint Level 1
BFS uses a queue, not a stack. Process all nodes at the current level before moving to the next level.

### Hint Level 2
Key insight: Before processing each level, record the queue size. That's how many nodes are in the current level. Process exactly that many nodes.

### Hint Level 3
Algorithm:
1. Queue starts with [root]
2. While queue not empty:
   - `levelSize = queue.length`
   - Create empty `currentLevel` array
   - Loop `levelSize` times:
     - Dequeue node, add value to `currentLevel`
     - Enqueue left and right children if they exist
   - Add `currentLevel` to result

---

## Problem 5: Binary Tree Zigzag Level Order Traversal

### Hint Level 1
This is level order with alternating direction. Use a boolean flag to track whether you're going left-to-right or right-to-left.

### Hint Level 2
Two approaches:
1. Add to current level array differently based on direction (push vs unshift)
2. Always add normally but reverse alternate levels

### Hint Level 3
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

### Hint Level 1
You want the rightmost node at each level. This is a level order traversal variant. When would you see a node from the right side?

### Hint Level 2
BFS approach: In level order traversal, the LAST node of each level is what you see from the right. Only add that node to result.

### Hint Level 3
In the level processing loop:
```typescript
for (let i = 0; i < levelSize; i++) {
  const node = queue.shift();
  if (i === levelSize - 1) { // Last node in level
    result.push(node.val);
  }
  // Add children as normal
}
```

---

## Problem 7: Average of Levels in Binary Tree

### Hint Level 1
Level order traversal, but instead of collecting all values, calculate the sum and count for each level.

### Hint Level 2
For each level, sum all node values and divide by the number of nodes in that level (which you already know from levelSize).

### Hint Level 3
```typescript
const levelSize = queue.length;
let levelSum = 0;
for (let i = 0; i < levelSize; i++) {
  const node = queue.shift();
  levelSum += node.val;
  // Add children
}
result.push(levelSum / levelSize);
```

---

## Problem 8: N-ary Tree Level Order Traversal

### Hint Level 1
Same as binary tree level order, but instead of left/right children, you have a children array.

### Hint Level 2
When adding children to queue, iterate through the entire children array instead of just checking left/right.

### Hint Level 3
Replace this binary tree pattern:
```typescript
if (node.left) queue.push(node.left);
if (node.right) queue.push(node.right);
```
With this n-ary pattern:
```typescript
for (const child of node.children) {
  queue.push(child);
}
```

---

## Problem 9: Vertical Order Traversal of a Binary Tree

### Hint Level 1
Assign coordinates to each node: (row, col). Root is at (0, 0). Left child is at (row+1, col-1), right child is at (row+1, col+1).

### Hint Level 2
Use a Map to group nodes by column. Within each column, sort by row, then by value if they're in the same row. Use BFS or DFS to traverse and collect coordinates.

### Hint Level 3
Data structure and algorithm:
1. `Map<col, Array<[row, value]>>`
2. BFS with queue containing `[node, row, col]`
3. Group nodes by column in the map
4. For each column from min to max:
   - Sort by row, then value
   - Extract just values for result

---

## Problem 10: Binary Tree Level Order Traversal II

### Hint Level 1
This is regular level order traversal but bottom-up. The easiest approach is to do normal level order then reverse.

### Hint Level 2
Two options:
1. Do normal level order and call `result.reverse()` at the end
2. Use `result.unshift(currentLevel)` to add each level to the beginning

### Hint Level 3
Simplest solution - just add one line:
```typescript
// Do normal level order traversal...
// Then before returning:
return result.reverse();
```
Or during traversal:
```typescript
result.unshift(currentLevel); // Instead of push
```