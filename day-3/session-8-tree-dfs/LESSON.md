# Lesson: Tree DFS

---

## 📹 Video 1: Binary Tree Fundamentals (15 min)

**"Binary Trees - Introduction" by mycodeschool**
https://www.youtube.com/watch?v=H5JubkIy_p8

**Focus on:**
- Tree terminology (root, leaf, height, depth)
- Binary tree structure
- Node relationships
- Tree properties

---

## 📹 Video 2: DFS Traversals Explained (12 min)

**"Tree Traversals (Inorder, Preorder, Postorder)" by NeetCode**
https://www.youtube.com/watch?v=afTpieEZXck

**Focus on:**
- Preorder traversal pattern
- Inorder traversal pattern
- Postorder traversal pattern
- When to use each type

---

## 📹 Video 3: Tree Problem Patterns (18 min)

**"Binary Tree Algorithms for Coding Interviews" by NeetCode**
https://www.youtube.com/watch?v=fAAZixBzIAI

**Focus on:**
- Recursive problem solving
- Top-down vs bottom-up
- Common tree patterns
- Time/space complexity

---

## 🎯 Tree DFS: Node Definition

### TypeScript TreeNode

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

**Creating trees:**
```typescript
// Manual construction
const root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);
root.left.left = new TreeNode(4);
root.left.right = new TreeNode(5);

// Result:
//       1
//      / \
//     2   3
//    / \
//   4   5
```

---

## 🔧 DFS Traversal Patterns

### Pattern 1: Preorder (Root → Left → Right)

**📹 Learn:** Search "NeetCode preorder traversal" on YouTube (~8-10 min)

Used when: Need to explore root before subtrees (copying tree, prefix expressions).

```typescript
function preorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];

  function dfs(node: TreeNode | null): void {
    if (!node) return;

    result.push(node.val);    // Process root first
    dfs(node.left);           // Then left subtree
    dfs(node.right);          // Then right subtree
  }

  dfs(root);
  return result;
}
```

**Example:**
```
       1
      / \
     2   3
    / \
   4   5

Preorder: [1, 2, 4, 5, 3]
```

**Time:** O(n) | **Space:** O(h) where h = height

---

### Pattern 2: Inorder (Left → Root → Right)

Used when: Need sorted order in BST, evaluating expressions.

```typescript
function inorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];

  function dfs(node: TreeNode | null): void {
    if (!node) return;

    dfs(node.left);           // Process left subtree first
    result.push(node.val);    // Then root
    dfs(node.right);          // Then right subtree
  }

  dfs(root);
  return result;
}
```

**Example:**
```
       1
      / \
     2   3
    / \
   4   5

Inorder: [4, 2, 5, 1, 3]
```

**Time:** O(n) | **Space:** O(h)

---

### Pattern 3: Postorder (Left → Right → Root)

Used when: Need to process children before parent (deleting nodes, postfix expressions).

```typescript
function postorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];

  function dfs(node: TreeNode | null): void {
    if (!node) return;

    dfs(node.left);           // Process left subtree first
    dfs(node.right);          // Then right subtree
    result.push(node.val);    // Root last
  }

  dfs(root);
  return result;
}
```

**Example:**
```
       1
      / \
     2   3
    / \
   4   5

Postorder: [4, 5, 2, 3, 1]
```

**Time:** O(n) | **Space:** O(h)

---

## 🧩 Tree DFS Patterns

### Pattern 1: Calculate Tree Properties

**📹 Learn:** Search "NeetCode maximum depth binary tree" on YouTube (~8 min)

```typescript
// Height of tree
function maxDepth(root: TreeNode | null): number {
  if (!root) return 0;
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}

// Count nodes
function countNodes(root: TreeNode | null): number {
  if (!root) return 0;
  return 1 + countNodes(root.left) + countNodes(root.right);
}

// Sum of all values
function sumTree(root: TreeNode | null): number {
  if (!root) return 0;
  return root.val + sumTree(root.left) + sumTree(root.right);
}
```

**Time:** O(n) | **Space:** O(h)

---

### Pattern 2: Top-Down (Preorder-like)

**📹 Learn:** Search "NeetCode path sum" or "NeetCode tree top down" (~10 min)

Pass information from parent to children:

```typescript
// Check if path sum exists
function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
  if (!root) return false;

  // Leaf node - check if reached target
  if (!root.left && !root.right) {
    return root.val === targetSum;
  }

  // Pass remaining sum down to children
  const remaining = targetSum - root.val;
  return hasPathSum(root.left, remaining) || hasPathSum(root.right, remaining);
}
```

**Key insight:** Parent passes info (remaining sum) down to children.

**Time:** O(n) | **Space:** O(h)

---

### Pattern 3: Bottom-Up (Postorder-like)

**📹 Learn:** Search "NeetCode diameter of binary tree" on YouTube (~10 min)

Collect information from children to parent:

```typescript
// Calculate diameter
function diameterOfBinaryTree(root: TreeNode | null): number {
  let maxDiameter = 0;

  function height(node: TreeNode | null): number {
    if (!node) return 0;

    const leftHeight = height(node.left);
    const rightHeight = height(node.right);

    // Update max diameter at this node
    maxDiameter = Math.max(maxDiameter, leftHeight + rightHeight);

    // Return height for parent
    return 1 + Math.max(leftHeight, rightHeight);
  }

  height(root);
  return maxDiameter;
}
```

**Key insight:** Children return info (height) up to parent for calculation.

**Time:** O(n) | **Space:** O(h)

---

### Pattern 4: Path Tracking with Backtracking

**📹 Learn:** Search "NeetCode binary tree paths" or "NeetCode path sum II" (~12 min)

```typescript
// Find all root-to-leaf paths
function binaryTreePaths(root: TreeNode | null): string[] {
  const result: string[] = [];

  function dfs(node: TreeNode | null, path: number[]): void {
    if (!node) return;

    path.push(node.val);

    // Leaf node - add complete path
    if (!node.left && !node.right) {
      result.push(path.join('->'));
    } else {
      dfs(node.left, path);
      dfs(node.right, path);
    }

    path.pop();  // Backtrack
  }

  dfs(root, []);
  return result;
}
```

**Key insight:** Add to path going down, remove (backtrack) going back up.

**Time:** O(n) | **Space:** O(h)

---

### Pattern 5: Tree Comparison

```typescript
// Check if two trees are identical
function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
  // Both null
  if (!p && !q) return true;

  // One null, other not
  if (!p || !q) return false;

  // Values different
  if (p.val !== q.val) return false;

  // Recursively check subtrees
  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}
```

**Time:** O(n) | **Space:** O(h)

---

## 📊 Complexity Analysis

### Time Complexity

| Operation | Complexity | Why |
|-----------|------------|-----|
| Visit all nodes | O(n) | Each node visited once |
| Traversal | O(n) | Process each node once |
| Search | O(n) | Worst case check all |
| Insert BST | O(h) | Follow path to position |

### Space Complexity

| Scenario | Complexity | Notes |
|----------|------------|-------|
| Balanced tree | O(log n) | Height = log n |
| Skewed tree | O(n) | Height = n (like linked list) |
| Additional storage | Varies | Result arrays, etc. |

**h = height of tree**
- Best case (balanced): h = log n
- Worst case (skewed): h = n

---

## 💡 Interview Tips

### Recursive Pattern Template

```typescript
function solveTree(root: TreeNode | null): ReturnType {
  // Base case: handle null
  if (!root) return baseValue;

  // Base case: handle leaf (optional)
  if (!root.left && !root.right) {
    return leafValue;
  }

  // Recursive case: process subtrees
  const leftResult = solveTree(root.left);
  const rightResult = solveTree(root.right);

  // Combine results
  return combine(root.val, leftResult, rightResult);
}
```

---

### Edge Cases to Consider

```typescript
// 1. Empty tree
root === null

// 2. Single node
root !== null && !root.left && !root.right

// 3. Left-skewed tree
//     1
//    /
//   2
//  /
// 3

// 4. Right-skewed tree
// 1
//  \
//   2
//    \
//     3

// 5. Negative values
//      1
//     / \
//   -2   3

// 6. All same values
//     5
//    / \
//   5   5
```

---

### Common Mistakes

```typescript
// ❌ Wrong - forgetting null check
function maxDepth(root: TreeNode | null): number {
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
  // Crashes on null!
}

// ✅ Correct - null check first
function maxDepth(root: TreeNode | null): number {
  if (!root) return 0;
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}

// ❌ Wrong - confusing height vs depth
// Height: distance from node to deepest leaf
// Depth: distance from root to node

// ❌ Wrong - not considering path must end at leaf
function hasPathSum(root: TreeNode | null, sum: number): boolean {
  if (!root) return false;
  if (root.val === sum) return true;  // Wrong! Must reach leaf
  // ...
}

// ✅ Correct - check leaf condition
function hasPathSum(root: TreeNode | null, sum: number): boolean {
  if (!root) return false;
  if (!root.left && !root.right) {  // Leaf check
    return root.val === sum;
  }
  // ...
}
```

---

### When to Use DFS vs BFS

**Use DFS when:**
- Exploring complete root-to-leaf paths
- Calculating tree properties (height, diameter)
- Space is concern (O(h) vs O(w) for BFS)
- Problem naturally recursive

**Use BFS when:**
- Level-by-level processing
- Shortest path in unweighted tree
- Processing nodes at same depth
- Width < height

---

### Interview Communication

**Say this:**
- "I'll use DFS with recursion since we need complete paths from root to leaf."
- "Base case is null node returns 0, then recursively calculate for both subtrees."
- "This is O(n) time to visit all nodes, O(h) space for recursion stack."
- "Helper function tracks path and backtracks to explore all routes."

**Draw examples:**
```
"Let me trace through with a small example:
       3
      / \
     9   20
        /  \
       15   7

maxDepth(3):
  leftHeight = maxDepth(9) = 1
  rightHeight = maxDepth(20) = 2
  return 1 + max(1, 2) = 3"
```

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **Preorder:** Root → Left → Right
- **Inorder:** Left → Root → Right
- **Postorder:** Left → Right → Root
- **Time:** O(n) visit all nodes
- **Space:** O(h) recursion stack

**Fundamental operations to know:**
1. Three traversals
2. Tree height
3. Node count
4. Path sum check

---

[Back to Session README](./README.md)
