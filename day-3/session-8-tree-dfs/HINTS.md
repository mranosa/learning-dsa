# Hints - Session 8: Tree DFS

Progressive hints for all 10 problems. Use sparingly - struggling is part of learning!

---

## Problem 1: Maximum Depth of Binary Tree

### Hint Level 1 (Gentle Nudge)
Think recursively. The depth of a tree is related to the depth of its subtrees. What's the relationship?

### Hint Level 2 (More Direct)
The depth of a tree is 1 (for the root) plus the maximum depth of its left and right subtrees. Base case: what's the depth of an empty tree?

### Hint Level 3 (Step-by-Step)
Complete algorithm:
1. If root is null, return 0 (empty tree has no depth)
2. Recursively find depth of left subtree
3. Recursively find depth of right subtree
4. Return `1 + Math.max(leftDepth, rightDepth)`

---

## Problem 2: Same Tree

### Hint Level 1
Two trees are the same if their roots have the same value AND their subtrees are the same. Think about the base cases first.

### Hint Level 2
Check three things at each step:
1. Are both nodes null? (same)
2. Is exactly one node null? (different)
3. Do values match? Then check subtrees

### Hint Level 3
```typescript
if (!p && !q) return true;  // Both null
if (!p || !q) return false;  // One null
return p.val === q.val &&
       isSameTree(p.left, q.left) &&
       isSameTree(p.right, q.right);
```

---

## Problem 3: Invert Binary Tree

### Hint Level 1
To invert a tree, you need to swap the left and right children of every node. Can you do this recursively?

### Hint Level 2
At each node: swap left and right children, then recursively invert the left subtree and right subtree.

### Hint Level 3
Algorithm:
1. If root is null, return null
2. Swap `root.left` and `root.right` (use a temp variable)
3. Recursively call `invertTree(root.left)`
4. Recursively call `invertTree(root.right)`
5. Return root

---

## Problem 4: Symmetric Tree

### Hint Level 1
A tree is symmetric if the left subtree is a mirror of the right subtree. You need a helper function that compares two subtrees.

### Hint Level 2
Create a helper `isMirror(left, right)` that checks:
- Left's left child mirrors right's right child
- Left's right child mirrors right's left child

### Hint Level 3
```typescript
function isMirror(left, right) {
  if (!left && !right) return true;
  if (!left || !right) return false;
  return left.val === right.val &&
         isMirror(left.left, right.right) &&
         isMirror(left.right, right.left);
}
// Call with isMirror(root.left, root.right)
```

---

## Problem 5: Diameter of Binary Tree

### Hint Level 1
The diameter at any node is the sum of the heights of its left and right subtrees. But the maximum diameter might not pass through the root!

### Hint Level 2
Calculate height recursively, but at each node also calculate the diameter through that node (left height + right height). Keep track of the global maximum.

### Hint Level 3
Algorithm:
1. Create a global variable `maxDiameter = 0`
2. Create recursive function `height(node)`:
   - If null, return 0
   - Get `leftHeight = height(node.left)`
   - Get `rightHeight = height(node.right)`
   - Update `maxDiameter = Math.max(maxDiameter, leftHeight + rightHeight)`
   - Return `1 + Math.max(leftHeight, rightHeight)`
3. Call height(root) and return maxDiameter

---

## Problem 6: Balanced Binary Tree

### Hint Level 1
A tree is balanced if for every node, the height difference between left and right subtrees is at most 1. Can you check this while calculating height?

### Hint Level 2
Use -1 as a sentinel value to indicate "not balanced". If any subtree returns -1, propagate it up immediately (early termination).

### Hint Level 3
```typescript
function checkHeight(node): number {
  if (!node) return 0;

  const left = checkHeight(node.left);
  if (left === -1) return -1;

  const right = checkHeight(node.right);
  if (right === -1) return -1;

  if (Math.abs(left - right) > 1) return -1;

  return Math.max(left, right) + 1;
}
// Tree is balanced if checkHeight(root) !== -1
```

---

## Problem 7: Lowest Common Ancestor

### Hint Level 1
If p and q are in different subtrees of the current node, then the current node is their LCA. How do you check which subtree contains a node?

### Hint Level 2
Recursively search for p and q. If you find p or q at current node, return it. If left subtree returns non-null AND right subtree returns non-null, current node is LCA.

### Hint Level 3
Algorithm:
1. If root is null, return null
2. If root equals p or q, return root
3. Search left: `left = LCA(root.left, p, q)`
4. Search right: `right = LCA(root.right, p, q)`
5. If both left and right are non-null, return root (found LCA)
6. Otherwise return whichever is non-null (left || right)

---

## Problem 8: Path Sum

### Hint Level 1
Subtract the current node's value from the target sum as you traverse down. What should you check when you reach a leaf?

### Hint Level 2
At a leaf node (no children), check if the remaining sum equals the node's value. For non-leaf nodes, recursively check both subtrees with the updated sum.

### Hint Level 3
```typescript
function hasPathSum(root, targetSum) {
  if (!root) return false;

  // Check leaf node
  if (!root.left && !root.right) {
    return root.val === targetSum;
  }

  // Check subtrees with remaining sum
  const remaining = targetSum - root.val;
  return hasPathSum(root.left, remaining) ||
         hasPathSum(root.right, remaining);
}
```

---

## Problem 9: Path Sum II

### Hint Level 1
Use backtracking to track the current path. When you find a valid path at a leaf, add a copy to your results. Don't forget to remove nodes from the path when backtracking!

### Hint Level 2
Maintain a `currentPath` array. Push nodes as you go down, pop when you backtrack. When you find a valid path, add a copy (not the reference!) to results.

### Hint Level 3
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

### Hint Level 1
At each node, calculate the maximum path that goes through that node. This path can include the node and both its subtrees. Keep track of the global maximum.

### Hint Level 2
For each node, you need two values:
1. Max path sum through this node (can use both subtrees)
2. Max gain if path continues through parent (can use only one subtree)

Remember: negative paths can be ignored (use 0 instead).

### Hint Level 3
```typescript
let maxSum = -Infinity;

function maxGain(node) {
  if (!node) return 0;

  // Get max from subtrees (ignore negatives)
  const leftGain = Math.max(0, maxGain(node.left));
  const rightGain = Math.max(0, maxGain(node.right));

  // Max path through this node
  const currentMax = node.val + leftGain + rightGain;
  maxSum = Math.max(maxSum, currentMax);

  // Return max gain for parent
  return node.val + Math.max(leftGain, rightGain);
}
```