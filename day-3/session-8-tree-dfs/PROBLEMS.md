# Problems - Session 8: Tree DFS

Complete these 10 problems in order. Use the UMPIRE method for each.

**Target Times:**
- Easy: <15 min
- Medium: <30 min
- Hard: <45 min

---

## Problem 1: Maximum Depth of Binary Tree

**Difficulty:** Easy
**Time Target:** 10-15 min
**Pattern:** Basic DFS
**LeetCode:** https://leetcode.com/problems/maximum-depth-of-binary-tree/

### Problem Statement

Given the `root` of a binary tree, return its maximum depth.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

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

- The number of nodes in the tree is in the range [0, 10^4]
- -100 <= Node.val <= 100

### Hints
- Think recursively: depth = 1 + max(left_depth, right_depth)
- Base case: null node has depth 0
- Can also solve iteratively with BFS

---

## Problem 2: Same Tree

**Difficulty:** Easy
**Time Target:** 10-15 min
**Pattern:** Tree Comparison
**LeetCode:** https://leetcode.com/problems/same-tree/

### Problem Statement

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

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

```
Input: p = [1,2,1], q = [1,1,2]
    1         1
   / \       / \
  2   1     1   2
Output: false
```

### Constraints

- The number of nodes in both trees is in the range [0, 100]
- -10^4 <= Node.val <= 10^4

### Hints
- Check if both nodes are null (base case)
- Check if one is null and other isn't
- Compare values and recurse on children

---

## Problem 3: Invert Binary Tree ⭐ BLIND 75

**Difficulty:** Easy
**Time Target:** 10-15 min
**Pattern:** Tree Modification
**LeetCode:** https://leetcode.com/problems/invert-binary-tree/

### Problem Statement

Given the `root` of a binary tree, invert the tree, and return its root.

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

```
Input: root = []
Output: []
```

### Constraints

- The number of nodes in the tree is in the range [0, 100]
- -100 <= Node.val <= 100

### Hints
- Swap left and right children at each node
- Can be done recursively or iteratively
- Remember to recurse after swapping

---

## Problem 4: Symmetric Tree

**Difficulty:** Easy
**Time Target:** 15-20 min
**Pattern:** Tree Comparison
**LeetCode:** https://leetcode.com/problems/symmetric-tree/

### Problem Statement

Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

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

- The number of nodes in the tree is in the range [1, 1000]
- -100 <= Node.val <= 100

### Hints
- Helper function to compare two subtrees
- Left subtree's left should match right subtree's right
- Left subtree's right should match right subtree's left

---

## Problem 5: Diameter of Binary Tree ⭐ BLIND 75

**Difficulty:** Easy
**Time Target:** 20-25 min
**Pattern:** Tree Properties
**LeetCode:** https://leetcode.com/problems/diameter-of-binary-tree/

### Problem Statement

Given the `root` of a binary tree, return the length of the **diameter** of the tree.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The **length** of a path between two nodes is represented by the number of edges between them.

### Examples

```
Input: root = [1,2,3,4,5]
        1
       / \
      2   3
     / \
    4   5
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

```
Input: root = [1,2]
    1
   /
  2
Output: 1
```

### Constraints

- The number of nodes in the tree is in the range [1, 10^4]
- -100 <= Node.val <= 100

### Hints
- At each node, diameter might pass through it
- Diameter through node = left_height + right_height
- Keep track of maximum diameter seen

---

## Problem 6: Balanced Binary Tree ⭐ BLIND 75

**Difficulty:** Easy
**Time Target:** 20-25 min
**Pattern:** Tree Properties
**LeetCode:** https://leetcode.com/problems/balanced-binary-tree/

### Problem Statement

Given a binary tree, determine if it is **height-balanced**.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

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

```
Input: root = []
Output: true
```

### Constraints

- The number of nodes in the tree is in the range [0, 5000]
- -10^4 <= Node.val <= 10^4

### Hints
- Calculate height while checking balance
- Return -1 to indicate imbalance
- Check left and right subtrees recursively

---

## Problem 7: Lowest Common Ancestor of a Binary Tree ⭐ BLIND 75

**Difficulty:** Medium
**Time Target:** 25-30 min
**Pattern:** Tree Search
**LeetCode:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

### Problem Statement

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA: "The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself)."

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
Explanation: The LCA of nodes 5 and 1 is 3.
```

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 (a node can be its own ancestor).
```

### Constraints

- The number of nodes in the tree is in the range [2, 10^5]
- -10^9 <= Node.val <= 10^9
- All Node.val are unique
- p != q
- p and q exist in the tree

### Hints
- If current node is p or q, it could be LCA
- Check if p and q are in different subtrees
- Use post-order traversal to bubble up results

---

## Problem 8: Path Sum

**Difficulty:** Easy
**Time Target:** 15-20 min
**Pattern:** Path Finding
**LeetCode:** https://leetcode.com/problems/path-sum/

### Problem Statement

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no children.

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
Explanation: Path 5 → 4 → 11 → 2 sums to 22.
```

```
Input: root = [1,2,3], targetSum = 5
    1
   / \
  2   3
Output: false
```

```
Input: root = [], targetSum = 0
Output: false
```

### Constraints

- The number of nodes in the tree is in the range [0, 5000]
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000

### Hints
- Subtract current value from target as you go down
- Check if you've reached target at a leaf node
- Must be root-to-leaf path (not just any path)

---

## Problem 9: Path Sum II

**Difficulty:** Medium
**Time Target:** 25-30 min
**Pattern:** Path Finding with Backtracking
**LeetCode:** https://leetcode.com/problems/path-sum-ii/

### Problem Statement

Given the `root` of a binary tree and an integer `targetSum`, return all **root-to-leaf** paths where the sum of the node values in the path equals `targetSum`. Each path should be returned as a list of the node values, not node references.

A **root-to-leaf** path is a path starting from the root and ending at any leaf node. A **leaf** is a node with no children.

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

```
Input: root = [1,2], targetSum = 0
Output: []
```

### Constraints

- The number of nodes in the tree is in the range [0, 5000]
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000

### Hints
- Use backtracking to track current path
- Add path to result when reaching leaf with target sum
- Remember to remove node from path when backtracking

---

## Problem 10: Binary Tree Maximum Path Sum ⭐ BLIND 75

**Difficulty:** Hard
**Time Target:** 35-45 min
**Pattern:** Tree DP
**LeetCode:** https://leetcode.com/problems/binary-tree-maximum-path-sum/

### Problem Statement

A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return the maximum **path sum** of any **non-empty** path.

### Examples

```
Input: root = [1,2,3]
    1
   / \
  2   3
Output: 6
Explanation: The optimal path is 2 → 1 → 3 with sum 2 + 1 + 3 = 6.
```

```
Input: root = [-10,9,20,null,null,15,7]
      -10
      / \
     9   20
        / \
       15  7
Output: 42
Explanation: The optimal path is 15 → 20 → 7 with sum 15 + 20 + 7 = 42.
```

### Constraints

- The number of nodes in the tree is in the range [1, 3 * 10^4]
- -1000 <= Node.val <= 1000

### Hints
- At each node, calculate max path that goes through it
- Track global maximum across all nodes
- A node can choose to include 0, 1, or 2 of its subtrees
- Negative paths can be excluded (take 0 instead)