# Problems - Session 7: Tree Traversals

Complete these 10 problems in order. Use the UMPIRE method for each.

**Target Times:**
- Easy: <10 min
- Medium: <25 min
- Hard: <40 min

---

## Problem 1: Binary Tree Inorder Traversal

**Difficulty:** Easy
**Time Target:** 10 min
**Pattern:** DFS - Inorder
**LeetCode:** https://leetcode.com/problems/binary-tree-inorder-traversal/

### Problem Statement

Given the `root` of a binary tree, return the inorder traversal of its nodes' values.

### Examples

```
Input: root = [1,null,2,3]
    1
     \
      2
     /
    3
Output: [1,3,2]
```

```
Input: root = []
Output: []
```

```
Input: root = [1]
Output: [1]
```

### Constraints

- The number of nodes in the tree is in the range `[0, 100]`
- `-100 <= Node.val <= 100`

### Follow-up
Recursive solution is trivial, could you do it iteratively?

### Hints
- Inorder: Left → Root → Right
- For iterative: use a stack
- Go left as far as possible, then process, then go right

---

## Problem 2: Binary Tree Preorder Traversal

**Difficulty:** Easy
**Time Target:** 10 min
**Pattern:** DFS - Preorder
**LeetCode:** https://leetcode.com/problems/binary-tree-preorder-traversal/

### Problem Statement

Given the `root` of a binary tree, return the preorder traversal of its nodes' values.

### Examples

```
Input: root = [1,null,2,3]
    1
     \
      2
     /
    3
Output: [1,2,3]
```

```
Input: root = []
Output: []
```

```
Input: root = [1]
Output: [1]
```

### Constraints

- The number of nodes in the tree is in the range `[0, 100]`
- `-100 <= Node.val <= 100`

### Follow-up
Recursive solution is trivial, could you do it iteratively?

### Hints
- Preorder: Root → Left → Right
- Process node before visiting children
- For iterative: push right child first, then left

---

## Problem 3: Binary Tree Postorder Traversal

**Difficulty:** Easy
**Time Target:** 10 min
**Pattern:** DFS - Postorder
**LeetCode:** https://leetcode.com/problems/binary-tree-postorder-traversal/

### Problem Statement

Given the `root` of a binary tree, return the postorder traversal of its nodes' values.

### Examples

```
Input: root = [1,null,2,3]
    1
     \
      2
     /
    3
Output: [3,2,1]
```

```
Input: root = []
Output: []
```

```
Input: root = [1]
Output: [1]
```

### Constraints

- The number of nodes in the tree is in the range `[0, 100]`
- `-100 <= Node.val <= 100`

### Follow-up
Recursive solution is trivial, could you do it iteratively?

### Hints
- Postorder: Left → Right → Root
- Process children before parent
- For iterative: can reverse a modified preorder

---

## Problem 4: Binary Tree Level Order Traversal

**Difficulty:** Medium
**Time Target:** 20 min
**Pattern:** BFS
**LeetCode:** https://leetcode.com/problems/binary-tree-level-order-traversal/

### Problem Statement

Given the `root` of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).

### Examples

```
Input: root = [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
Output: [[3],[9,20],[15,7]]
```

```
Input: root = [1]
Output: [[1]]
```

```
Input: root = []
Output: []
```

### Constraints

- The number of nodes in the tree is in the range `[0, 2000]`
- `-1000 <= Node.val <= 1000`

### Hints
- Use a queue for BFS
- Process nodes level by level
- Track level size to know when level ends

---

## Problem 5: Binary Tree Zigzag Level Order Traversal

**Difficulty:** Medium
**Time Target:** 25 min
**Pattern:** BFS with alternating direction
**LeetCode:** https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

### Problem Statement

Given the `root` of a binary tree, return the zigzag level order traversal of its nodes' values (i.e., from left to right, then right to left for the next level and alternate between).

### Examples

```
Input: root = [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
Output: [[3],[20,9],[15,7]]
```

```
Input: root = [1]
Output: [[1]]
```

```
Input: root = []
Output: []
```

### Constraints

- The number of nodes in the tree is in the range `[0, 2000]`
- `-100 <= Node.val <= 100`

### Hints
- Similar to level order but alternate direction
- Use a flag to track current direction
- Can reverse alternate levels or use deque

---

## Problem 6: Binary Tree Right Side View

**Difficulty:** Medium
**Time Target:** 20 min
**Pattern:** BFS/DFS - Rightmost nodes
**LeetCode:** https://leetcode.com/problems/binary-tree-right-side-view/

### Problem Statement

Given the `root` of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

### Examples

```
Input: root = [1,2,3,null,5,null,4]
    1
   / \
  2   3
   \   \
    5   4
Output: [1,3,4]
```

```
Input: root = [1,null,3]
    1
     \
      3
Output: [1,3]
```

```
Input: root = []
Output: []
```

### Constraints

- The number of nodes in the tree is in the range `[0, 100]`
- `-100 <= Node.val <= 100`

### Hints
- Last node at each level
- BFS: take last element of each level
- DFS: visit right subtree first, track depth

---

## Problem 7: Average of Levels in Binary Tree

**Difficulty:** Easy
**Time Target:** 15 min
**Pattern:** BFS - Level processing
**LeetCode:** https://leetcode.com/problems/average-of-levels-in-binary-tree/

### Problem Statement

Given the `root` of a binary tree, return the average value of the nodes on each level in the form of an array.

### Examples

```
Input: root = [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
Output: [3.00000,14.50000,11.00000]
Explanation:
Level 0: 3
Level 1: (9 + 20) / 2 = 14.5
Level 2: (15 + 7) / 2 = 11
```

```
Input: root = [3,9,20,15,7]
    3
   / \
  9  20
 / \
15  7
Output: [3.00000,14.50000,11.00000]
```

### Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`
- `-2^31 <= Node.val <= 2^31 - 1`

### Hints
- Level order traversal with sum calculation
- Track sum and count for each level
- Calculate average after processing level

---

## Problem 8: N-ary Tree Level Order Traversal

**Difficulty:** Medium
**Time Target:** 20 min
**Pattern:** BFS - N-ary tree
**LeetCode:** https://leetcode.com/problems/n-ary-tree-level-order-traversal/

### Problem Statement

Given an n-ary tree, return the level order traversal of its nodes' values.

N-ary tree input serialization is represented in their level order traversal format. Each group of children is separated by the null value.

### Examples

```
Input: root = [1,null,3,2,4,null,5,6]
      1
    / | \
   3  2  4
  / \
 5   6
Output: [[1],[3,2,4],[5,6]]
```

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
```

### Constraints

- The height of the n-ary tree is less than or equal to `1000`
- The total number of nodes is between `[0, 10^4]`

### Node Definition
```typescript
class Node {
  val: number;
  children: Node[];
  constructor(val?: number) {
    this.val = (val === undefined ? 0 : val);
    this.children = [];
  }
}
```

### Hints
- Same as binary tree but iterate through children array
- Use BFS with queue
- Process all children instead of just left/right

---

## Problem 9: Vertical Order Traversal of a Binary Tree

**Difficulty:** Hard
**Time Target:** 35 min
**Pattern:** BFS/DFS with coordinates
**LeetCode:** https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

### Problem Statement

Given the `root` of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position `(row, col)`, its left and right children will be at positions `(row + 1, col - 1)` and `(row + 1, col + 1)` respectively. The root of the tree is at `(0, 0)`.

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

### Examples

```
Input: root = [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9
Column 0: Nodes 3 and 15
Column 1: Only node 20
Column 2: Only node 7
```

```
Input: root = [1,2,3,4,5,6,7]
      1
    /   \
   2     3
  / \   / \
 4   5 6   7
Output: [[4],[2],[1,5,6],[3],[7]]
```

### Constraints

- The number of nodes in the tree is in the range `[1, 1000]`
- `0 <= Node.val <= 1000`

### Hints
- Track (row, col) for each node
- Group by column, sort by row then value
- Use Map to store column groups
- BFS or DFS both work

---

## Problem 10: Binary Tree Level Order Traversal II

**Difficulty:** Medium
**Time Target:** 20 min
**Pattern:** BFS - Bottom-up
**LeetCode:** https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

### Problem Statement

Given the `root` of a binary tree, return the bottom-up level order traversal of its nodes' values (i.e., from left to right, level by level from leaf to root).

### Examples

```
Input: root = [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
Output: [[15,7],[9,20],[3]]
```

```
Input: root = [1]
Output: [[1]]
```

```
Input: root = []
Output: []
```

### Constraints

- The number of nodes in the tree is in the range `[0, 2000]`
- `-1000 <= Node.val <= 1000`

### Hints
- Same as regular level order but reversed
- Can reverse result at end
- Or insert at beginning of result array