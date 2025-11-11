# BST Problems

## Problem Order
1. Search in a BST (Easy) - Warm-up
2. Validate Binary Search Tree (Medium) - Core concept
3. Kth Smallest Element in a BST (Medium) - Use BST property
4. Lowest Common Ancestor of a BST (Medium) - BST navigation
5. Insert into a BST (Medium) - Basic operation
6. Delete Node in a BST (Medium) - Complex operation
7. Convert Sorted Array to BST (Easy) - Construction
8. Two Sum IV - Input is a BST (Easy) - Creative use
9. Serialize and Deserialize BST (Medium) - Advanced
10. Recover Binary Search Tree (Hard) - Challenge

---

## 1. Search in a BST
**Difficulty:** Easy
**Time:** 10 minutes
**LeetCode:** [700](https://leetcode.com/problems/search-in-a-binary-search-tree/)

### Problem Statement
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

### Examples
```
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Input: root = [4,2,7,1,3], val = 5
Output: []
```

### Constraints
- The number of nodes in the tree is in the range [1, 5000]
- 1 <= Node.val <= 10^7
- root is a binary search tree
- 1 <= val <= 10^7

---

## 2. Validate Binary Search Tree
**Difficulty:** Medium
**Time:** 20 minutes
**LeetCode:** [98](https://leetcode.com/problems/validate-binary-search-tree/)

### Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

### Examples
```
Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

### Constraints
- The number of nodes in the tree is in the range [1, 10^4]
- -2^31 <= Node.val <= 2^31 - 1

---

## 3. Kth Smallest Element in a BST
**Difficulty:** Medium
**Time:** 20 minutes
**LeetCode:** [230](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

### Problem Statement
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

### Examples
```
Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

### Constraints
- The number of nodes in the tree is n
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

### Follow up
If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

---

## 4. Lowest Common Ancestor of a BST
**Difficulty:** Medium
**Time:** 15 minutes
**LeetCode:** [235](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

### Problem Statement
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)."

### Examples
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself.
```

### Constraints
- The number of nodes in the tree is in the range [2, 10^5]
- -10^9 <= Node.val <= 10^9
- All Node.val are unique
- p != q
- p and q will exist in the BST

---

## 5. Insert into a BST
**Difficulty:** Medium
**Time:** 15 minutes
**LeetCode:** [701](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

### Problem Statement
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

### Examples
```
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is [5,2,7,1,3,null,4]

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
```

### Constraints
- The number of nodes in the tree will be in the range [0, 10^4]
- -10^8 <= Node.val <= 10^8
- All the values Node.val are unique
- -10^8 <= val <= 10^8
- It's guaranteed that val does not exist in the original BST

---

## 6. Delete Node in a BST
**Difficulty:** Medium
**Time:** 25 minutes
**LeetCode:** [450](https://leetcode.com/problems/delete-node-in-a-bst/)

### Problem Statement
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
1. Search for a node to remove
2. If the node is found, delete the node

### Examples
```
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7].
Another valid answer is [5,2,6,null,4,null,7].

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
```

### Constraints
- The number of nodes in the tree is in the range [0, 10^4]
- -10^5 <= Node.val <= 10^5
- Each node has a unique value
- root is a valid binary search tree
- -10^5 <= key <= 10^5

---

## 7. Convert Sorted Array to BST
**Difficulty:** Easy
**Time:** 15 minutes
**LeetCode:** [108](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

### Problem Statement
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

### Examples
```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted.

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both valid.
```

### Constraints
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in a strictly increasing order

---

## 8. Two Sum IV - Input is a BST
**Difficulty:** Easy
**Time:** 15 minutes
**LeetCode:** [653](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)

### Problem Statement
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

### Examples
```
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
```

### Constraints
- The number of nodes in the tree is in the range [1, 10^4]
- -10^4 <= Node.val <= 10^4
- root is guaranteed to be a valid binary search tree
- -10^5 <= k <= 10^5

---

## 9. Serialize and Deserialize BST
**Difficulty:** Medium
**Time:** 30 minutes
**LeetCode:** [449](https://leetcode.com/problems/serialize-and-deserialize-bst/)

### Problem Statement
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

### Examples
```
Input: root = [2,1,3]
Output: [2,1,3]

Input: root = []
Output: []
```

### Constraints
- The number of nodes in the tree is in the range [0, 10^4]
- 0 <= Node.val <= 10^4
- The input tree is guaranteed to be a binary search tree

---

## 10. Recover Binary Search Tree
**Difficulty:** Hard
**Time:** 35 minutes
**LeetCode:** [99](https://leetcode.com/problems/recover-binary-search-tree/)

### Problem Statement
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

### Examples
```
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
```

### Constraints
- The number of nodes in the tree is in the range [2, 1000]
- -2^31 <= Node.val <= 2^31 - 1

### Follow up
A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?

---

## Problem-Solving Strategy

### For BST Problems:
1. **Always consider the BST property** - Can eliminate half the tree
2. **Inorder traversal gives sorted order** - Useful for many problems
3. **Use range bounds for validation** - Track min/max values
4. **Think recursively first** - Then optimize to iterative if needed
5. **Draw examples** - Visualize tree operations

### Time Management:
- Easy: 10-15 minutes each
- Medium: 15-25 minutes each
- Hard: 30-35 minutes

### If stuck:
1. Review BST properties in LESSON.md
2. Check HINTS.md for progressive hints
3. Draw the tree and trace through manually
4. Consider both recursive and iterative approaches