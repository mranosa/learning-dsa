# Solutions - Session 8: Tree DFS

TypeScript solutions with complexity analysis.

---

## Problem 1: Maximum Depth of Binary Tree

### Approach: Recursive DFS (Optimal) ✅

```typescript
function maxDepth(root: TreeNode | null): number {
  if (!root) return 0;
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}
```

**Time:** O(n) | **Space:** O(h)

**Key:** Depth = 1 + max of subtree depths.

**Say:** "Recursive DFS visits each node once. Base case null returns 0. Combine subtree results with 1 plus max. Space is O(h) for recursion stack where h is height."

---

## Problem 2: Same Tree

### Approach: Recursive Comparison ✅

```typescript
function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
  // Both null - same
  if (!p && !q) return true;

  // One null - different
  if (!p || !q) return false;

  // Check current and recurse
  return p.val === q.val &&
         isSameTree(p.left, q.left) &&
         isSameTree(p.right, q.right);
}
```

**Time:** O(min(n, m)) | **Space:** O(min(h1, h2))

**Key:** Trees same if roots match AND subtrees match.

**Say:** "Check structural equality first, then value equality. Short-circuit with && stops early on mismatch."

---

## Problem 3: Invert Binary Tree

### Approach: Recursive Swap ✅

```typescript
function invertTree(root: TreeNode | null): TreeNode | null {
  if (!root) return null;

  // Swap children
  const temp = root.left;
  root.left = root.right;
  root.right = temp;

  // Recursively invert subtrees
  invertTree(root.left);
  invertTree(root.right);

  return root;
}
```

**Time:** O(n) | **Space:** O(h)

**Key:** Swap at each node, then recurse.

**Say:** "Famous interview question. Swap children before or after recursion - both work. O(n) time to visit all nodes."

---

## Problem 4: Symmetric Tree

### Approach: Recursive Helper ✅

```typescript
function isSymmetric(root: TreeNode | null): boolean {
  if (!root) return true;

  function isMirror(left: TreeNode | null, right: TreeNode | null): boolean {
    if (!left && !right) return true;
    if (!left || !right) return false;

    return left.val === right.val &&
           isMirror(left.left, right.right) &&
           isMirror(left.right, right.left);
  }

  return isMirror(root.left, root.right);
}
```

**Time:** O(n) | **Space:** O(h)

**Key:** For symmetry, left's left mirrors right's right (and vice versa).

**Say:** "Helper function compares subtrees in mirror fashion. Left child of left subtree should equal right child of right subtree."

---

## Problem 5: Diameter of Binary Tree

### Approach: Height with Global Max ✅

```typescript
function diameterOfBinaryTree(root: TreeNode | null): number {
  let maxDiameter = 0;

  function height(node: TreeNode | null): number {
    if (!node) return 0;

    const leftHeight = height(node.left);
    const rightHeight = height(node.right);

    // Update max diameter
    maxDiameter = Math.max(maxDiameter, leftHeight + rightHeight);

    // Return height
    return 1 + Math.max(leftHeight, rightHeight);
  }

  height(root);
  return maxDiameter;
}
```

**Time:** O(n) | **Space:** O(h)

**Key:** Diameter at node = left height + right height. Track global max.

**Say:** "Diameter may not pass through root, so check at every node. Calculate height while tracking max diameter. Diameter is edges not nodes, so leftHeight + rightHeight."

---

## Problem 6: Balanced Binary Tree

### Approach: Bottom-Up with -1 Sentinel ✅

```typescript
function isBalanced(root: TreeNode | null): boolean {
  function checkHeight(node: TreeNode | null): number {
    if (!node) return 0;

    const leftHeight = checkHeight(node.left);
    if (leftHeight === -1) return -1;

    const rightHeight = checkHeight(node.right);
    if (rightHeight === -1) return -1;

    if (Math.abs(leftHeight - rightHeight) > 1) {
      return -1;
    }

    return Math.max(leftHeight, rightHeight) + 1;
  }

  return checkHeight(root) !== -1;
}
```

**Time:** O(n) | **Space:** O(h)

**Key:** Use -1 as sentinel for imbalance. Early termination.

**Say:** "Bottom-up approach calculates height while checking balance. Use -1 to signal imbalance and stop early. Single pass instead of naive O(n²)."

---

## Problem 7: Lowest Common Ancestor

### Approach: Post-Order Search ✅

```typescript
function lowestCommonAncestor(
  root: TreeNode | null,
  p: TreeNode,
  q: TreeNode
): TreeNode | null {
  if (!root) return null;
  if (root === p || root === q) return root;

  const left = lowestCommonAncestor(root.left, p, q);
  const right = lowestCommonAncestor(root.right, p, q);

  // Both in different subtrees
  if (left && right) return root;

  // Return whichever found something
  return left || right;
}
```

**Time:** O(n) | **Space:** O(h)

**Key:** If p and q in different subtrees, current is LCA.

**Say:** "Post-order traversal bubbles up results. If current node is p or q, return it. If both subtrees return non-null, current is LCA where paths diverge."

---

## Problem 8: Path Sum

### Approach: Recursive DFS ✅

```typescript
function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
  if (!root) return false;

  // Check leaf
  if (!root.left && !root.right) {
    return root.val === targetSum;
  }

  // Check subtrees
  const remainingSum = targetSum - root.val;
  return hasPathSum(root.left, remainingSum) ||
         hasPathSum(root.right, remainingSum);
}
```

**Time:** O(n) | **Space:** O(h)

**Key:** Subtract current from target going down. Check at leaf.

**Say:** "Must be root-to-leaf path, not any path. Subtract from target rather than accumulating. Short-circuit with || when path found."

---

## Problem 9: Path Sum II

### Approach: DFS with Backtracking ✅

```typescript
function pathSum(root: TreeNode | null, targetSum: number): number[][] {
  const result: number[][] = [];
  const currentPath: number[] = [];

  function dfs(node: TreeNode | null, remainingSum: number): void {
    if (!node) return;

    currentPath.push(node.val);

    if (!node.left && !node.right && node.val === remainingSum) {
      result.push([...currentPath]);  // Copy!
    } else {
      dfs(node.left, remainingSum - node.val);
      dfs(node.right, remainingSum - node.val);
    }

    currentPath.pop();  // Backtrack
  }

  dfs(root, targetSum);
  return result;
}
```

**Time:** O(n²) worst case | **Space:** O(n)

**Key:** Backtrack to maintain path. Copy array when adding to result.

**Say:** "Must copy array when adding to result - JavaScript arrays are references. Backtrack by popping after exploring both subtrees. Check leaf AND target sum."

---

## Problem 10: Binary Tree Maximum Path Sum

### Approach: Post-Order with Global Max ✅

```typescript
function maxPathSum(root: TreeNode | null): number {
  let maxSum = -Infinity;

  function maxGain(node: TreeNode | null): number {
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

  maxGain(root);
  return maxSum;
}
```

**Time:** O(n) | **Space:** O(h)

**Key Insights:**
1. At each node, max path = node.val + left + right
2. When returning to parent, can only use one branch
3. Negative paths can be ignored (take 0)
4. Track global max separately

**Say:** "Track global max separately from return value. Return value is max gain for paths continuing upward. Current max includes both subtrees, return includes only one. Use Math.max(0, gain) to exclude negative paths."

---

## Pattern Summary

### Basic DFS (Problems 1, 2, 8)
- Recursively visit nodes
- Combine subtree results
- O(n) time, O(h) space

### Tree Modification (Problem 3)
- Swap/modify at each node
- Recurse on children
- In-place or return new structure

### Tree Comparison (Problems 2, 4)
- Helper functions for symmetry/equality
- Check structure AND values
- Early termination on mismatch

### Properties with Global State (Problems 5, 6, 10)
- Use global variable for tree-wide property
- Calculate one thing, track another
- -1 sentinel for early termination

### Path Problems (Problems 8, 9)
- Top-down: pass remaining target
- Backtracking: maintain current path
- Must reach leaf for root-to-leaf paths

### Search Problems (Problem 7)
- Post-order to bubble up results
- Check current before recursing
- Combine left and right results

---

[Back to Problems](./PROBLEMS.md) | [Back to README](./README.md)
