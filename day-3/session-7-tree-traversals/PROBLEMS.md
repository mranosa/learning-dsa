# Problems - Session 7: Tree Traversals

10 problems in order. Use UMPIRE method.

**Targets:** Easy <10 min | Medium <25 min

---

## Problem 1: Binary Tree Inorder Traversal

**Difficulty:** Easy | **Pattern:** DFS - Inorder
**LeetCode:** https://leetcode.com/problems/binary-tree-inorder-traversal/

### Problem

Given `root` of binary tree, return inorder traversal of node values.

### Examples

```
Input: root = [1,null,2,3]
    1
     \
      2
     /
    3
Output: [1,3,2]

Input: root = []
Output: []

Input: root = [1]
Output: [1]
```

### Constraints

- 0 ≤ nodes ≤ 100
- -100 ≤ Node.val ≤ 100

### Follow-up
Recursive solution is trivial, can you do it iteratively?

### Hints
- Inorder: Left → Root → Right
- Iterative: use stack
- Go left fully, process, then right

---

## Problem 2: Binary Tree Preorder Traversal

**Difficulty:** Easy | **Pattern:** DFS - Preorder
**LeetCode:** https://leetcode.com/problems/binary-tree-preorder-traversal/

### Problem

Given `root` of binary tree, return preorder traversal of node values.

### Examples

```
Input: root = [1,null,2,3]
    1
     \
      2
     /
    3
Output: [1,2,3]

Input: root = []
Output: []

Input: root = [1]
Output: [1]
```

### Constraints

- 0 ≤ nodes ≤ 100
- -100 ≤ Node.val ≤ 100

### Follow-up
Recursive solution is trivial, can you do it iteratively?

### Hints
- Preorder: Root → Left → Right
- Process node before children
- Iterative: push right first, then left

---

## Problem 3: Binary Tree Postorder Traversal

**Difficulty:** Easy | **Pattern:** DFS - Postorder
**LeetCode:** https://leetcode.com/problems/binary-tree-postorder-traversal/

### Problem

Given `root` of binary tree, return postorder traversal of node values.

### Examples

```
Input: root = [1,null,2,3]
    1
     \
      2
     /
    3
Output: [3,2,1]

Input: root = []
Output: []

Input: root = [1]
Output: [1]
```

### Constraints

- 0 ≤ nodes ≤ 100
- -100 ≤ Node.val ≤ 100

### Follow-up
Recursive solution is trivial, can you do it iteratively?

### Hints
- Postorder: Left → Right → Root
- Process children before parent
- Iterative: reverse modified preorder

---

## Problem 4: Binary Tree Level Order Traversal

**Difficulty:** Medium | **Pattern:** BFS
**LeetCode:** https://leetcode.com/problems/binary-tree-level-order-traversal/

### Problem

Given `root` of binary tree, return level order traversal (left to right, level by level).

### Examples

```
Input: root = [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
```

### Constraints

- 0 ≤ nodes ≤ 2000
- -1000 ≤ Node.val ≤ 1000

### Hints
- Use queue for BFS
- Process level by level
- Track level size to know when level ends

---

## Problem 5: Binary Tree Zigzag Level Order Traversal

**Difficulty:** Medium | **Pattern:** BFS with alternating direction
**LeetCode:** https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

### Problem

Given `root` of binary tree, return zigzag level order traversal (left to right, then right to left alternating).

### Examples

```
Input: root = [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
Output: [[3],[20,9],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
```

### Constraints

- 0 ≤ nodes ≤ 2000
- -100 ≤ Node.val ≤ 100

### Hints
- Similar to level order but alternate direction
- Use flag to track current direction
- Can reverse alternate levels or use deque

---

## Problem 6: Binary Tree Right Side View

**Difficulty:** Medium | **Pattern:** BFS/DFS - Rightmost nodes
**LeetCode:** https://leetcode.com/problems/binary-tree-right-side-view/

### Problem

Given `root` of binary tree, imagine standing on right side. Return values you can see ordered top to bottom.

### Examples

```
Input: root = [1,2,3,null,5,null,4]
    1
   / \
  2   3
   \   \
    5   4
Output: [1,3,4]

Input: root = [1,null,3]
    1
     \
      3
Output: [1,3]

Input: root = []
Output: []
```

### Constraints

- 0 ≤ nodes ≤ 100
- -100 ≤ Node.val ≤ 100

### Hints
- Last node at each level
- BFS: take last element of each level
- DFS: visit right subtree first, track depth

---

## Problem 7: Average of Levels in Binary Tree

**Difficulty:** Easy | **Pattern:** BFS - Level processing
**LeetCode:** https://leetcode.com/problems/average-of-levels-in-binary-tree/

### Problem

Given `root` of binary tree, return average value of nodes on each level as array.

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

Input: root = [3,9,20,15,7]
    3
   / \
  9  20
 / \
15  7
Output: [3.00000,14.50000,11.00000]
```

### Constraints

- 1 ≤ nodes ≤ 10⁴
- -2³¹ ≤ Node.val ≤ 2³¹ - 1

### Hints
- Level order traversal with sum
- Track sum and count for each level
- Calculate average after processing level

---

## Problem 8: N-ary Tree Level Order Traversal

**Difficulty:** Medium | **Pattern:** BFS - N-ary tree
**LeetCode:** https://leetcode.com/problems/n-ary-tree-level-order-traversal/

### Problem

Given n-ary tree, return level order traversal of node values.

### Examples

```
Input: root = [1,null,3,2,4,null,5,6]
      1
    / | \
   3  2  4
  / \
 5   6
Output: [[1],[3,2,4],[5,6]]

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
```

### Constraints

- Height ≤ 1000
- 0 ≤ nodes ≤ 10⁴

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
- Same as binary tree but children array
- Use BFS with queue
- Process all children instead of just left/right

---

## Problem 9: Vertical Order Traversal of a Binary Tree

**Difficulty:** Medium | **Pattern:** BFS/DFS with coordinates
**LeetCode:** https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

### Problem

Given `root` of binary tree, calculate vertical order traversal.

For each node at position `(row, col)`, left and right children at `(row + 1, col - 1)` and `(row + 1, col + 1)`. Root at `(0, 0)`.

Return list of top-to-bottom orderings for each column. If multiple nodes same row/col, sort by values.

### Examples

```
Input: root = [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
Output: [[9],[3,15],[20],[7]]

Input: root = [1,2,3,4,5,6,7]
      1
    /   \
   2     3
  / \   / \
 4   5 6   7
Output: [[4],[2],[1,5,6],[3],[7]]
```

### Constraints

- 1 ≤ nodes ≤ 1000
- 0 ≤ Node.val ≤ 1000

### Hints
- Track (row, col) for each node
- Group by column, sort by row then value
- Use Map to store column groups
- BFS or DFS both work

---

## Problem 10: Binary Tree Level Order Traversal II

**Difficulty:** Medium | **Pattern:** BFS - Bottom-up
**LeetCode:** https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

### Problem

Given `root` of binary tree, return bottom-up level order traversal (left to right, level by level from leaf to root).

### Examples

```
Input: root = [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
Output: [[15,7],[9,20],[3]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
```

### Constraints

- 0 ≤ nodes ≤ 2000
- -1000 ≤ Node.val ≤ 1000

### Hints
- Same as regular level order but reversed
- Can reverse result at end
- Or insert at beginning of result array

---

## Summary

**Total:** 10 problems (4 Easy, 6 Medium)

**Patterns:**
- DFS (Inorder, Preorder, Postorder)
- BFS (Level Order)
- Advanced traversals (Zigzag, Views, Vertical)

**Time:** All O(n)
**Space:** O(h) DFS, O(w) BFS

---

**Ready?** Say: `"Claude, give me the problem"` or `"Go"`

[Solutions](./SOLUTIONS.md) | [Hints](./HINTS.md)
