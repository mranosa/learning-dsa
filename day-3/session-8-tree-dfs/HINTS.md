# Hints - Session 8: Tree DFS

Progressive hints for 10 problems. Struggling is part of learning.

---

## Problem 1: Maximum Depth of Binary Tree

### Level 1
What's the relationship between a tree's depth and its subtrees' depths?

### Level 2
Depth = 1 (current node) + max depth of subtrees. Base case: empty tree has depth 0.

### Level 3
```typescript
if (!root) return 0;
const leftDepth = maxDepth(root.left);
const rightDepth = maxDepth(root.right);
return 1 + Math.max(leftDepth, rightDepth);
```

---

## Problem 2: Same Tree

### Level 1
Two trees same if roots match AND subtrees match. What are base cases?

### Level 2
Check three things:
1. Both null? (same)
2. One null? (different)
3. Values match? Then check subtrees

### Level 3
```typescript
if (!p && !q) return true;
if (!p || !q) return false;
return p.val === q.val &&
       isSameTree(p.left, q.left) &&
       isSameTree(p.right, q.right);
```

---

## Problem 3: Invert Binary Tree

### Level 1
To invert, swap left and right children at every node. How to do recursively?

### Level 2
At each node: swap children, then recursively invert both subtrees.

### Level 3
```typescript
if (!root) return null;
const temp = root.left;
root.left = root.right;
root.right = temp;
invertTree(root.left);
invertTree(root.right);
return root;
```

---

## Problem 4: Symmetric Tree

### Level 1
Tree symmetric if left subtree mirrors right subtree. Need helper to compare two subtrees.

### Level 2
Helper `isMirror(left, right)` checks:
- Left's left mirrors right's right
- Left's right mirrors right's left

### Level 3
```typescript
function isMirror(left, right) {
  if (!left && !right) return true;
  if (!left || !right) return false;
  return left.val === right.val &&
         isMirror(left.left, right.right) &&
         isMirror(left.right, right.left);
}
// Call: isMirror(root.left, root.right)
```

---

## Problem 5: Diameter of Binary Tree

### Level 1
Diameter at node = left height + right height. But max diameter might not pass through root!

### Level 2
Calculate height recursively, but at each node also check diameter through that node. Track global max.

### Level 3
```typescript
let maxDiameter = 0;
function height(node) {
  if (!node) return 0;
  const leftHeight = height(node.left);
  const rightHeight = height(node.right);
  maxDiameter = Math.max(maxDiameter, leftHeight + rightHeight);
  return 1 + Math.max(leftHeight, rightHeight);
}
```

---

## Problem 6: Balanced Binary Tree

### Level 1
Balanced if for every node, height difference between subtrees ≤ 1. Check while calculating height?

### Level 2
Use -1 as sentinel for "not balanced". If any subtree returns -1, propagate up immediately.

### Level 3
```typescript
function checkHeight(node) {
  if (!node) return 0;
  const left = checkHeight(node.left);
  if (left === -1) return -1;
  const right = checkHeight(node.right);
  if (right === -1) return -1;
  if (Math.abs(left - right) > 1) return -1;
  return Math.max(left, right) + 1;
}
// Balanced if checkHeight(root) !== -1
```

---

## Problem 7: Lowest Common Ancestor

### Level 1
If p and q in different subtrees of current node, then current node is LCA. How to check which subtree contains a node?

### Level 2
Recursively search for p and q. If found at current, return it. If left returns non-null AND right returns non-null, current is LCA.

### Level 3
```typescript
if (!root) return null;
if (root === p || root === q) return root;
const left = LCA(root.left, p, q);
const right = LCA(root.right, p, q);
if (left && right) return root;  // Found LCA
return left || right;
```

---

## Problem 8: Path Sum

### Level 1
Subtract current node's value from target as you go down. What check at leaf?

### Level 2
At leaf (no children), check if remaining sum equals node's value. For non-leaf, check both subtrees.

### Level 3
```typescript
if (!root) return false;
if (!root.left && !root.right) {
  return root.val === targetSum;
}
const remaining = targetSum - root.val;
return hasPathSum(root.left, remaining) ||
       hasPathSum(root.right, remaining);
```

---

## Problem 9: Path Sum II

### Level 1
Use backtracking to track current path. When valid path found at leaf, add copy to results. Don't forget to backtrack!

### Level 2
Maintain `currentPath` array. Push going down, pop backtracking. When valid path found, add copy (not reference!).

### Level 3
```typescript
function dfs(node, remainingSum, currentPath, result) {
  if (!node) return;
  currentPath.push(node.val);
  if (!node.left && !node.right && node.val === remainingSum) {
    result.push([...currentPath]);  // Copy!
  } else {
    dfs(node.left, remainingSum - node.val, currentPath, result);
    dfs(node.right, remainingSum - node.val, currentPath, result);
  }
  currentPath.pop();  // Backtrack
}
```

---

## Problem 10: Binary Tree Maximum Path Sum

### Level 1
At each node, calculate max path through that node. Can include node and both subtrees. Track global max.

### Level 2
For each node, need two values:
1. Max path sum through node (can use both subtrees)
2. Max gain if path continues through parent (only one subtree)
Negative paths can be ignored (use 0).

### Level 3
```typescript
let maxSum = -Infinity;
function maxGain(node) {
  if (!node) return 0;
  const leftGain = Math.max(0, maxGain(node.left));
  const rightGain = Math.max(0, maxGain(node.right));
  const currentMax = node.val + leftGain + rightGain;
  maxSum = Math.max(maxSum, currentMax);
  return node.val + Math.max(leftGain, rightGain);
}
```

---

## Pattern Hints

**"Calculate tree property"** → Recursive DFS, combine subtree results

**"Check tree property"** → Recursive with early termination (-1 sentinel)

**"Find in tree"** → Post-order traversal, bubble up results

**"Root-to-leaf path"** → Top-down or backtracking with path tracking

**"Any path in tree"** → Bottom-up with global max

---

## Using Hints Effectively

1. Try 10+ min before Level 1
2. Try 5+ min after each hint
3. If use Level 3, mark for review
4. Don't feel bad - hints are for learning

Goal: Learn pattern, not just solve one problem.

---

[Back to Problems](./PROBLEMS.md) | [Back to Solutions](./SOLUTIONS.md)
