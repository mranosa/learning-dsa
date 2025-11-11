# Solutions - Session 8: Tree DFS

Comprehensive TypeScript solutions with multiple approaches and complexity analysis.

---

## Problem 1: Maximum Depth of Binary Tree

### Approach 1: Recursive DFS (Optimal) ✅

```typescript
function maxDepth(root: TreeNode | null): number {
  // Base case: empty tree has depth 0
  if (!root) return 0;

  // Recursive case: 1 + max of subtree depths
  const leftDepth = maxDepth(root.left);
  const rightDepth = maxDepth(root.right);

  return 1 + Math.max(leftDepth, rightDepth);
}
```

**Complexity:**
- Time: O(n) - visit every node once
- Space: O(h) - recursion stack, h is height

**Key Insight:** The depth of a tree is 1 (for current node) plus the maximum depth of its subtrees.

---

### Approach 2: Iterative BFS

```typescript
function maxDepth(root: TreeNode | null): number {
  if (!root) return 0;

  const queue: TreeNode[] = [root];
  let depth = 0;

  while (queue.length > 0) {
    const levelSize = queue.length;
    depth++;

    // Process all nodes at current level
    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift()!;
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
  }

  return depth;
}
```

**Complexity:**
- Time: O(n) - visit every node
- Space: O(w) - queue holds at most w nodes, where w is max width

**Interview Points:**
- "Recursive is more intuitive for depth calculation"
- "BFS naturally counts levels which equals max depth"
- "Space complexity differs: O(h) for DFS vs O(w) for BFS"

---

## Problem 2: Same Tree

### Approach: Recursive Comparison ✅

```typescript
function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
  // Both null - same
  if (!p && !q) return true;

  // One null, other not - different
  if (!p || !q) return false;

  // Check current values and recurse
  return p.val === q.val &&
         isSameTree(p.left, q.left) &&
         isSameTree(p.right, q.right);
}
```

**Complexity:**
- Time: O(min(n, m)) - where n and m are tree sizes
- Space: O(min(h1, h2)) - recursion depth

**Key Insight:** Trees are same if roots match AND left subtrees match AND right subtrees match.

**Interview Points:**
- "Check structural equality first (both null or both non-null)"
- "Then check value equality"
- "Short-circuit evaluation with && stops early if mismatch found"

---

## Problem 3: Invert Binary Tree

### Approach 1: Recursive (Clean) ✅

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

**Complexity:**
- Time: O(n) - visit every node
- Space: O(h) - recursion stack

---

### Approach 2: Recursive (Functional Style)

```typescript
function invertTree(root: TreeNode | null): TreeNode | null {
  if (!root) return null;

  // Invert subtrees first, then swap
  const left = invertTree(root.left);
  const right = invertTree(root.right);

  root.left = right;
  root.right = left;

  return root;
}
```

**Interview Points:**
- "Can swap before or after recursion - both work"
- "This is the problem that tripped up the Homebrew creator at Google!"
- "Simple problem but tests understanding of tree structure"

---

## Problem 4: Symmetric Tree

### Approach 1: Recursive Helper ✅

```typescript
function isSymmetric(root: TreeNode | null): boolean {
  if (!root) return true;

  function isMirror(left: TreeNode | null, right: TreeNode | null): boolean {
    // Both null - symmetric
    if (!left && !right) return true;

    // One null - not symmetric
    if (!left || !right) return false;

    // Check values and cross-compare children
    return left.val === right.val &&
           isMirror(left.left, right.right) &&
           isMirror(left.right, right.left);
  }

  return isMirror(root.left, root.right);
}
```

**Complexity:**
- Time: O(n) - visit every node
- Space: O(h) - recursion depth

**Key Insight:** For symmetry, left child of left subtree should mirror right child of right subtree.

---

### Approach 2: Iterative with Queue

```typescript
function isSymmetric(root: TreeNode | null): boolean {
  if (!root) return true;

  const queue: (TreeNode | null)[] = [root.left, root.right];

  while (queue.length > 0) {
    const left = queue.shift();
    const right = queue.shift();

    if (!left && !right) continue;
    if (!left || !right) return false;
    if (left.val !== right.val) return false;

    // Add in mirror order
    queue.push(left.left, right.right);
    queue.push(left.right, right.left);
  }

  return true;
}
```

**Interview Points:**
- "Process nodes in pairs that should be mirrors"
- "Queue maintains pairing throughout traversal"

---

## Problem 5: Diameter of Binary Tree

### Approach: Height Calculation with Global Max ✅

```typescript
function diameterOfBinaryTree(root: TreeNode | null): number {
  let maxDiameter = 0;

  function height(node: TreeNode | null): number {
    if (!node) return 0;

    // Get height of subtrees
    const leftHeight = height(node.left);
    const rightHeight = height(node.right);

    // Update max diameter (path through this node)
    maxDiameter = Math.max(maxDiameter, leftHeight + rightHeight);

    // Return height of this subtree
    return 1 + Math.max(leftHeight, rightHeight);
  }

  height(root);
  return maxDiameter;
}
```

**Complexity:**
- Time: O(n) - visit every node once
- Space: O(h) - recursion stack

**Key Insight:**
- Diameter at each node = left height + right height
- Keep global max as we calculate heights
- Don't confuse diameter (edges) with height (nodes)

**Interview Points:**
- "Diameter may not pass through root"
- "Calculate height while tracking max diameter"
- "Diameter is edges, not nodes, so it's leftHeight + rightHeight"

---

## Problem 6: Balanced Binary Tree

### Approach: Bottom-Up with Early Termination ✅

```typescript
function isBalanced(root: TreeNode | null): boolean {
  function checkHeight(node: TreeNode | null): number {
    // Empty tree is balanced with height 0
    if (!node) return 0;

    // Check left subtree
    const leftHeight = checkHeight(node.left);
    if (leftHeight === -1) return -1;  // Not balanced

    // Check right subtree
    const rightHeight = checkHeight(node.right);
    if (rightHeight === -1) return -1;  // Not balanced

    // Check current node's balance
    if (Math.abs(leftHeight - rightHeight) > 1) {
      return -1;  // Not balanced
    }

    // Return height if balanced
    return Math.max(leftHeight, rightHeight) + 1;
  }

  return checkHeight(root) !== -1;
}
```

**Complexity:**
- Time: O(n) - visit each node once
- Space: O(h) - recursion depth

**Key Insight:** Use -1 as sentinel value to indicate imbalance and stop early.

**Interview Points:**
- "Bottom-up approach calculates height while checking balance"
- "Early termination with -1 prevents unnecessary computation"
- "Single pass solution instead of naive O(n²) approach"

---

## Problem 7: Lowest Common Ancestor

### Approach: Recursive Search ✅

```typescript
function lowestCommonAncestor(
  root: TreeNode | null,
  p: TreeNode,
  q: TreeNode
): TreeNode | null {
  // Base cases
  if (!root) return null;
  if (root === p || root === q) return root;

  // Search in subtrees
  const left = lowestCommonAncestor(root.left, p, q);
  const right = lowestCommonAncestor(root.right, p, q);

  // If both found in different subtrees, current is LCA
  if (left && right) return root;

  // Otherwise, return whichever side found something
  return left || right;
}
```

**Complexity:**
- Time: O(n) - worst case visit all nodes
- Space: O(h) - recursion stack

**Key Insight:**
- If p and q are in different subtrees, current node is LCA
- If both in same subtree, LCA is in that subtree
- Post-order traversal bubbles up the result

**Interview Points:**
- "If current node is p or q, it could be the LCA"
- "LCA is where paths to p and q diverge"
- "Post-order ensures we check children before deciding"

---

## Problem 8: Path Sum

### Approach: Recursive DFS ✅

```typescript
function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
  // Empty tree has no paths
  if (!root) return false;

  // Check if we've reached a leaf with target sum
  if (!root.left && !root.right) {
    return root.val === targetSum;
  }

  // Check if path exists in either subtree
  const remainingSum = targetSum - root.val;
  return hasPathSum(root.left, remainingSum) ||
         hasPathSum(root.right, remainingSum);
}
```

**Complexity:**
- Time: O(n) - might visit all nodes
- Space: O(h) - recursion depth

**Key Insight:** Subtract current value from target as we go down, check if we hit 0 at a leaf.

**Interview Points:**
- "Must be root-to-leaf path, not just any path"
- "Subtract from target rather than accumulating sum"
- "Short-circuit with || when path found"

---

## Problem 9: Path Sum II

### Approach: DFS with Backtracking ✅

```typescript
function pathSum(root: TreeNode | null, targetSum: number): number[][] {
  const result: number[][] = [];
  const currentPath: number[] = [];

  function dfs(node: TreeNode | null, remainingSum: number): void {
    if (!node) return;

    // Add current node to path
    currentPath.push(node.val);

    // Check if we've found a valid path at leaf
    if (!node.left && !node.right && node.val === remainingSum) {
      result.push([...currentPath]);  // Copy current path
    } else {
      // Continue searching in subtrees
      dfs(node.left, remainingSum - node.val);
      dfs(node.right, remainingSum - node.val);
    }

    // Backtrack: remove current node from path
    currentPath.pop();
  }

  dfs(root, targetSum);
  return result;
}
```

**Complexity:**
- Time: O(n²) - worst case n/2 leaves, each path length n/2
- Space: O(n) - recursion stack + path storage

**Key Insight:** Use backtracking to maintain current path, copy when valid path found.

**Interview Points:**
- "Must copy array when adding to result (JavaScript arrays are references)"
- "Backtrack by removing node after exploring both subtrees"
- "Check for leaf node AND target sum"

---

## Problem 10: Binary Tree Maximum Path Sum

### Approach: Post-Order DFS with Global Max ✅

```typescript
function maxPathSum(root: TreeNode | null): number {
  let maxSum = -Infinity;  // Global maximum

  function maxGain(node: TreeNode | null): number {
    if (!node) return 0;

    // Get max gain from subtrees (ignore negative paths)
    const leftGain = Math.max(0, maxGain(node.left));
    const rightGain = Math.max(0, maxGain(node.right));

    // Max path through current node
    const currentMax = node.val + leftGain + rightGain;

    // Update global maximum
    maxSum = Math.max(maxSum, currentMax);

    // Return max gain if we continue path through parent
    return node.val + Math.max(leftGain, rightGain);
  }

  maxGain(root);
  return maxSum;
}
```

**Complexity:**
- Time: O(n) - visit each node once
- Space: O(h) - recursion stack

**Key Insights:**
1. At each node, calculate max path that passes through it
2. A path through a node = node.val + left path + right path
3. When returning to parent, can only use one branch (not both)
4. Negative paths can be ignored (take 0 instead)

**Interview Points:**
- "Track global max separately from return value"
- "Return value is max gain for paths continuing upward"
- "Current max includes both subtrees, return value includes only one"
- "Use Math.max(0, gain) to exclude negative paths"

**Edge Cases to Consider:**
- All negative values (must include at least one node)
- Single node tree
- Skewed tree (essentially a linked list)