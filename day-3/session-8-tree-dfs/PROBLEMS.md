# Problems - Session 8: Tree DFS

10 problems in order. Use UMPIRE method.

**Targets:** Easy <15 min | Medium <30 min | Hard <45 min

---

## Problem 1: Maximum Depth of Binary Tree

**Difficulty:** Easy | **Pattern:** Basic DFS
**LeetCode:** https://leetcode.com/problems/maximum-depth-of-binary-tree/

### Problem

Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from root to farthest leaf.

### Examples

```
Input: root = [3,9,20,null,null,15,7]
       3
      / \
     9   20
        /  \
       15   7
Output: 3
```

```
Input: root = [1,null,2]
       1
        \
         2
Output: 2
```

```
Input: root = []
Output: 0
```

### Constraints

- Number of nodes: [0, 10^4]
- -100 <= Node.val <= 100

### Hints
- Recursively: depth = 1 + max(leftDepth, rightDepth)
- Base case: null node returns 0
- Can also solve with BFS level counting

---

## Problem 2: Same Tree

**Difficulty:** Easy | **Pattern:** Tree Comparison
**LeetCode:** https://leetcode.com/problems/same-tree/

### Problem

Given roots of two binary trees `p` and `q`, check if they are the same.

Two trees are same if structurally identical with same node values.

### Examples

```
Input: p = [1,2,3], q = [1,2,3]
    1         1
   / \       / \
  2   3     2   3
Output: true
```

```
Input: p = [1,2], q = [1,null,2]
    1         1
   /           \
  2             2
Output: false
```

### Constraints

- Number of nodes: [0, 100]
- -10^4 <= Node.val <= 10^4

### Hints
- Check if both null (base case)
- Check if one null, other not
- Compare values and recurse on children

---

## Problem 3: Invert Binary Tree ⭐ BLIND 75

**Difficulty:** Easy | **Pattern:** Tree Modification
**LeetCode:** https://leetcode.com/problems/invert-binary-tree/

### Problem

Given the `root` of a binary tree, invert the tree and return its root.

### Examples

```
Input: root = [4,2,7,1,3,6,9]
       4                4
      / \              / \
     2   7     →      7   2
    / \ / \          / \ / \
   1  3 6  9        9  6 3  1
Output: [4,7,2,9,6,3,1]
```

```
Input: root = [2,1,3]
    2         2
   / \   →   / \
  1   3     3   1
Output: [2,3,1]
```

### Constraints

- Number of nodes: [0, 100]
- -100 <= Node.val <= 100

### Hints
- Swap left and right children at each node
- Can be done recursively or iteratively
- Recurse after swapping

---

## Problem 4: Symmetric Tree

**Difficulty:** Easy | **Pattern:** Tree Comparison
**LeetCode:** https://leetcode.com/problems/symmetric-tree/

### Problem

Check if binary tree is a mirror of itself (symmetric around center).

### Examples

```
Input: root = [1,2,2,3,4,4,3]
        1
       / \
      2   2
     / \ / \
    3  4 4  3
Output: true
```

```
Input: root = [1,2,2,null,3,null,3]
        1
       / \
      2   2
       \   \
        3   3
Output: false
```

### Constraints

- Number of nodes: [1, 1000]
- -100 <= Node.val <= 100

### Hints
- Helper function to compare two subtrees
- Left's left should match right's right
- Left's right should match right's left

---

## Problem 5: Diameter of Binary Tree ⭐ BLIND 75

**Difficulty:** Easy | **Pattern:** Tree Properties
**LeetCode:** https://leetcode.com/problems/diameter-of-binary-tree/

### Problem

Return the length of the diameter of the tree.

The diameter is the length of the longest path between any two nodes. May or may not pass through root.

Length = number of edges between nodes.

### Examples

```
Input: root = [1,2,3,4,5]
        1
       / \
      2   3
     / \
    4   5
Output: 3
Explanation: Path [4,2,1,3] or [5,2,1,3]
```

```
Input: root = [1,2]
    1
   /
  2
Output: 1
```

### Constraints

- Number of nodes: [1, 10^4]
- -100 <= Node.val <= 100

### Hints
- At each node, diameter = leftHeight + rightHeight
- Diameter might not pass through root
- Keep track of maximum diameter seen

---

## Problem 6: Balanced Binary Tree ⭐ BLIND 75

**Difficulty:** Easy | **Pattern:** Tree Properties
**LeetCode:** https://leetcode.com/problems/balanced-binary-tree/

### Problem

Determine if height-balanced.

A tree is height-balanced if depth of two subtrees of every node never differs by more than one.

### Examples

```
Input: root = [3,9,20,null,null,15,7]
       3
      / \
     9   20
        /  \
       15   7
Output: true
```

```
Input: root = [1,2,2,3,3,null,null,4,4]
          1
         / \
        2   2
       / \
      3   3
     / \
    4   4
Output: false
```

### Constraints

- Number of nodes: [0, 5000]
- -10^4 <= Node.val <= 10^4

### Hints
- Calculate height while checking balance
- Return -1 to indicate imbalance
- Check left and right subtrees recursively

---

## Problem 7: Lowest Common Ancestor ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Tree Search
**LeetCode:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

### Problem

Find lowest common ancestor (LCA) of two given nodes.

LCA is the lowest node that has both `p` and `q` as descendants (node can be descendant of itself).

### Examples

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
         3
       /   \
      5     1
     / \   / \
    6   2 0   8
       / \
      7   4
Output: 3
Explanation: LCA of 5 and 1 is 3
```

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: Node can be its own ancestor
```

### Constraints

- Number of nodes: [2, 10^5]
- -10^9 <= Node.val <= 10^9
- All values unique
- p != q
- p and q exist in tree

### Hints
- If current node is p or q, it could be LCA
- Check if p and q in different subtrees
- Use post-order to bubble up results

---

## Problem 8: Path Sum

**Difficulty:** Easy | **Pattern:** Path Finding
**LeetCode:** https://leetcode.com/problems/path-sum/

### Problem

Return `true` if tree has root-to-leaf path where values sum to `targetSum`.

A leaf is a node with no children.

### Examples

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
          5
         / \
        4   8
       /   / \
      11  13  4
     / \       \
    7   2       1
Output: true
Explanation: Path 5 → 4 → 11 → 2 = 22
```

```
Input: root = [1,2,3], targetSum = 5
    1
   / \
  2   3
Output: false
```

### Constraints

- Number of nodes: [0, 5000]
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000

### Hints
- Subtract current value from target going down
- Check if reached target at leaf node
- Must be root-to-leaf (not any path)

---

## Problem 9: Path Sum II

**Difficulty:** Medium | **Pattern:** Path Finding + Backtracking
**LeetCode:** https://leetcode.com/problems/path-sum-ii/

### Problem

Return all root-to-leaf paths where sum equals `targetSum`. Return as list of node values.

A leaf is a node with no children.

### Examples

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
          5
         / \
        4   8
       /   / \
      11  13  4
     / \     / \
    7   2   5   1
Output: [[5,4,11,2],[5,8,4,5]]
```

```
Input: root = [1,2,3], targetSum = 5
Output: []
```

### Constraints

- Number of nodes: [0, 5000]
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000

### Hints
- Use backtracking to track current path
- Add path to result when reaching leaf with target
- Remove node from path when backtracking

---

## Problem 10: Binary Tree Maximum Path Sum ⭐ BLIND 75

**Difficulty:** Hard | **Pattern:** Tree DP
**LeetCode:** https://leetcode.com/problems/binary-tree-maximum-path-sum/

### Problem

A path is a sequence of nodes with edges connecting them. Node appears at most once. Path does not need to pass through root.

Path sum is sum of node values in path.

Return maximum path sum of any non-empty path.

### Examples

```
Input: root = [1,2,3]
    1
   / \
  2   3
Output: 6
Explanation: Path 2 → 1 → 3 = 6
```

```
Input: root = [-10,9,20,null,null,15,7]
      -10
      / \
     9   20
        / \
       15  7
Output: 42
Explanation: Path 15 → 20 → 7 = 42
```

### Constraints

- Number of nodes: [1, 3 × 10^4]
- -1000 <= Node.val <= 1000

### Hints
- At each node, calculate max path through it
- Track global maximum across all nodes
- Node can include 0, 1, or 2 subtrees
- Negative paths can be excluded (take 0)

---

## Summary

**Total:** 10 problems (6 Easy, 3 Medium, 1 Hard)

**Patterns:**
- Basic DFS recursion
- Tree comparison
- Tree modification
- Tree properties (height, diameter, balance)
- Path finding with backtracking

**Blind 75:** 5/75 complete (7%)

---

**Ready?** Say: `"Claude, give me the problem"` or `"Go"`

[Solutions](./SOLUTIONS.md) | [Hints](./HINTS.md)
