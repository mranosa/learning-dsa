# Lesson: Tree DFS (Depth-First Search)

## 📹 Video Assignment (30 minutes)

**Primary Video:**
"Binary Tree Algorithms for Coding Interviews" by NeetCode
https://www.youtube.com/watch?v=fAAZixBzIAI

**Alternative Videos** (if you need different explanations):
- "Tree Traversals (Inorder, Preorder, Postorder)" by NeetCode (8 min): https://www.youtube.com/watch?v=afTpieEZXck
- "Binary Trees - Introduction" by mycodeschool (15 min): https://www.youtube.com/watch?v=H5JubkIy_p8

**What to focus on:**
- Understanding tree terminology and structure
- Three types of DFS traversals
- Recursive approach to tree problems
- Time and space complexity of tree operations

---

## 📚 Tree DFS - Core Concepts

### What is a Binary Tree?

A hierarchical data structure where each node has at most two children (left and right).

**Key terminology:**
- **Root:** Top node of the tree
- **Leaf:** Node with no children
- **Height:** Length of longest path from node to leaf
- **Depth:** Length of path from root to node
- **Subtree:** A node and all its descendants

### TypeScript Tree Node Definition

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

### DFS Traversal Patterns

**The three fundamental ways to visit all nodes:**

#### 1. Preorder Traversal (Root → Left → Right)

```typescript
function preorder(root: TreeNode | null): number[] {
  if (!root) return [];

  const result: number[] = [];

  function dfs(node: TreeNode | null): void {
    if (!node) return;

    result.push(node.val);    // Process root first
    dfs(node.left);            // Then left subtree
    dfs(node.right);           // Then right subtree
  }

  dfs(root);
  return result;
}
```

**Use when:** You need to explore nodes before their subtrees (copying tree, prefix expressions)

#### 2. Inorder Traversal (Left → Root → Right)

```typescript
function inorder(root: TreeNode | null): number[] {
  if (!root) return [];

  const result: number[] = [];

  function dfs(node: TreeNode | null): void {
    if (!node) return;

    dfs(node.left);            // Process left subtree first
    result.push(node.val);     // Then root
    dfs(node.right);           // Then right subtree
  }

  dfs(root);
  return result;
}
```

**Use when:** You need sorted order in BST, evaluating expressions

#### 3. Postorder Traversal (Left → Right → Root)

```typescript
function postorder(root: TreeNode | null): number[] {
  if (!root) return [];

  const result: number[] = [];

  function dfs(node: TreeNode | null): void {
    if (!node) return;

    dfs(node.left);            // Process left subtree first
    dfs(node.right);           // Then right subtree
    result.push(node.val);     // Root last
  }

  dfs(root);
  return result;
}
```

**Use when:** You need to process children before parent (deleting nodes, postfix expressions)

---

### Recursive Pattern for Tree Problems

Most tree problems follow this template:

```typescript
function solveProblem(root: TreeNode | null): ReturnType {
  // Base case: handle null
  if (!root) return baseValue;

  // Base case: handle leaf (optional)
  if (!root.left && !root.right) {
    return leafValue;
  }

  // Recursive case: process subtrees
  const leftResult = solveProblem(root.left);
  const rightResult = solveProblem(root.right);

  // Combine results with current node
  return combine(root.val, leftResult, rightResult);
}
```

---

### Top-Down vs Bottom-Up Approaches

#### Top-Down (Preorder-like)
Pass information from parent to children:

```typescript
function topDown(node: TreeNode | null, parentInfo: any): void {
  if (!node) return;

  // Use parent info to process current node
  const currentInfo = process(node, parentInfo);

  // Pass info down to children
  topDown(node.left, currentInfo);
  topDown(node.right, currentInfo);
}
```

#### Bottom-Up (Postorder-like)
Collect information from children to parent:

```typescript
function bottomUp(node: TreeNode | null): any {
  if (!node) return null;

  // Get info from children first
  const leftInfo = bottomUp(node.left);
  const rightInfo = bottomUp(node.right);

  // Process current node using children's info
  return process(node, leftInfo, rightInfo);
}
```

---

### Common Tree Patterns

#### Pattern 1: Calculate Tree Properties

```typescript
// Height of tree
function height(root: TreeNode | null): number {
  if (!root) return 0;
  return 1 + Math.max(height(root.left), height(root.right));
}

// Number of nodes
function countNodes(root: TreeNode | null): number {
  if (!root) return 0;
  return 1 + countNodes(root.left) + countNodes(root.right);
}
```

#### Pattern 2: Check Tree Properties

```typescript
// Is tree balanced?
function isBalanced(root: TreeNode | null): boolean {
  function checkHeight(node: TreeNode | null): number {
    if (!node) return 0;

    const left = checkHeight(node.left);
    if (left === -1) return -1;  // Not balanced

    const right = checkHeight(node.right);
    if (right === -1) return -1;  // Not balanced

    if (Math.abs(left - right) > 1) return -1;  // Current node not balanced

    return Math.max(left, right) + 1;
  }

  return checkHeight(root) !== -1;
}
```

#### Pattern 3: Path Problems

```typescript
// Find all root-to-leaf paths
function allPaths(root: TreeNode | null): number[][] {
  const result: number[][] = [];

  function dfs(node: TreeNode | null, path: number[]): void {
    if (!node) return;

    path.push(node.val);

    if (!node.left && !node.right) {
      result.push([...path]);  // Found a complete path
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

---

### Complexity Analysis

**Time Complexity:**
- Visiting all nodes: O(n) where n is number of nodes
- Each node processed once in DFS

**Space Complexity:**
- Recursive call stack: O(h) where h is height
- Best case (balanced): O(log n)
- Worst case (skewed): O(n)
- Additional space for results: varies by problem

---

### Edge Cases to Always Consider

1. **Empty tree:** `root === null`
2. **Single node:** Tree with just root
3. **Leaf nodes:** Nodes with no children
4. **Skewed tree:** All nodes on one side (linked list-like)
5. **Negative values:** When calculating sums/paths
6. **Duplicate values:** When searching/comparing

---

### Tree DFS vs Tree BFS

**Use DFS when:**
- Need to explore complete paths (root-to-leaf)
- Calculate properties that depend on subtrees
- Space is a concern (O(h) vs O(w) for BFS)
- Natural recursion fits the problem

**Use BFS when:**
- Need level-by-level processing
- Finding shortest path in unweighted tree
- Need to process nodes at same depth together
- Width of tree is smaller than height

---

### Interview Tips

1. **Always start with null check** - First line of most tree functions
2. **Draw small examples** - Trees with 3-5 nodes
3. **Trace through recursion** - Step by step on paper
4. **Name helper functions clearly** - `dfsHelper`, `calculateHeight`, etc.
5. **State assumptions** - "Assuming values are unique" if relevant
6. **Consider both recursive and iterative** - But recursive usually cleaner
7. **Test with edge cases** - Empty, single node, skewed

---

### Practice Exercises

Before jumping into problems, try implementing these from scratch:

1. **All three traversals** (preorder, inorder, postorder)
2. **Tree height calculator**
3. **Node counter**
4. **Sum of all nodes**
5. **Check if value exists**

These fundamentals appear in almost every tree problem!

---

## Ready for Problems?

Now that you understand DFS patterns, let's solve real interview problems. Each builds on these core concepts!

Say **"Claude, I'm ready for problems"** to begin!