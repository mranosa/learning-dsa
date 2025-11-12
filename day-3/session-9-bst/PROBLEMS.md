# Problems - Session 9: Binary Search Trees

10 problems in order. Use UMPIRE method.

**Targets:** Easy <15 min | Medium <25 min

---

## Problem 1: Search in a BST

**Difficulty:** Easy | **Pattern:** BST Navigation
**LeetCode:** https://leetcode.com/problems/search-in-a-binary-search-tree/

### Problem

Given root of BST and integer `val`, find node where `node.val === val`. Return subtree rooted at that node. Return null if not found.

### Examples

```
root = [4,2,7,1,3], val = 2
Output: [2,1,3]

root = [4,2,7,1,3], val = 5
Output: null
```

### Constraints

- 1 <= Node count <= 5000
- 1 <= Node.val <= 10^7
- root is a BST
- 1 <= val <= 10^7

### Hints
- Use BST property to eliminate half
- If val < root.val, search left only
- Iterative solution uses O(1) space

---

## Problem 2: Validate Binary Search Tree

**Difficulty:** Medium | **Pattern:** Range Validation
**LeetCode:** https://leetcode.com/problems/validate-binary-search-tree/

### Problem

Given root of binary tree, determine if it's a valid BST.

Valid BST:
- Left subtree nodes < node value
- Right subtree nodes > node value
- Both subtrees are also valid BSTs

### Examples

```
root = [2,1,3]
Output: true

root = [5,1,4,null,null,3,6]
Output: false  (4 < 5, but 3 < 5 breaks property)
```

### Constraints

- 1 <= Node count <= 10^4
- -2^31 <= Node.val <= 2^31 - 1

### Hints
- Can't just compare with immediate children
- Use range (min, max) for each node
- Alternative: inorder gives sorted sequence

---

## Problem 3: Kth Smallest Element in BST

**Difficulty:** Medium | **Pattern:** Inorder Traversal
**LeetCode:** https://leetcode.com/problems/kth-smallest-element-in-a-bst/

### Problem

Given root of BST and integer `k`, return kth smallest value (1-indexed).

### Examples

```
root = [3,1,4,null,2], k = 1
Output: 1

root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

### Constraints

- n nodes in tree
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

### Follow-up
If BST modified often and need kth frequently, how optimize?

### Hints
- Inorder traversal gives sorted sequence
- Use counter, stop at kth node
- Can optimize to O(k) time

---

## Problem 4: Lowest Common Ancestor of BST

**Difficulty:** Medium | **Pattern:** BST Navigation
**LeetCode:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

### Problem

Given BST, find lowest common ancestor (LCA) of two nodes p and q.

LCA: lowest node that has both p and q as descendants (node can be descendant of itself).

### Examples

```
root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6

root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
```

### Constraints

- 2 <= Node count <= 10^5
- -10^9 <= Node.val <= 10^9
- All values unique
- p != q
- p and q exist in BST

### Hints
- Use BST property to navigate
- If both < root, go left
- If both > root, go right
- Otherwise, root is LCA

---

## Problem 5: Insert into a BST

**Difficulty:** Medium | **Pattern:** BST Construction
**LeetCode:** https://leetcode.com/problems/insert-into-a-binary-search-tree/

### Problem

Given BST root and value to insert, return BST root after insertion. New value doesn't exist in BST. Multiple valid answers possible.

### Examples

```
root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]

root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
```

### Constraints

- 0 <= Node count <= 10^4
- -10^8 <= Node.val <= 10^8
- All values unique
- -10^8 <= val <= 10^8
- val doesn't exist in BST

### Hints
- New nodes inserted as leaves
- Navigate like search
- Insert at first null position

---

## Problem 6: Delete Node in a BST

**Difficulty:** Medium | **Pattern:** BST Modification
**LeetCode:** https://leetcode.com/problems/delete-node-in-a-bst/

### Problem

Given BST root and key, delete node with given key. Return root (possibly updated).

### Examples

```
root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]

root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
```

### Constraints

- 0 <= Node count <= 10^4
- -10^5 <= Node.val <= 10^5
- Each value unique
- root is valid BST
- -10^5 <= key <= 10^5

### Hints
- Three cases: leaf, one child, two children
- Two children: replace with successor/predecessor
- Successor: min of right subtree
- Then recursively delete successor

---

## Problem 7: Convert Sorted Array to BST

**Difficulty:** Easy | **Pattern:** BST Construction
**LeetCode:** https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

### Problem

Given sorted integer array, convert to height-balanced BST.

Height-balanced: depth of two subtrees never differs by more than 1.

### Examples

```
nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]

nums = [1,3]
Output: [3,1] or [1,null,3]
```

### Constraints

- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums sorted in strictly increasing order

### Hints
- Middle element as root ensures balance
- Recursively build left and right
- O(n) time, O(log n) space

---

## Problem 8: Two Sum IV - Input is BST

**Difficulty:** Easy | **Pattern:** BST + Hash
**LeetCode:** https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

### Problem

Given BST root and integer `k`, return true if two elements exist in BST that sum to `k`.

### Examples

```
root = [5,3,6,2,4,null,7], k = 9
Output: true  (3 + 6 = 9)

root = [5,3,6,2,4,null,7], k = 28
Output: false
```

### Constraints

- 1 <= Node count <= 10^4
- -10^4 <= Node.val <= 10^4
- root is valid BST
- -10^5 <= k <= 10^5

### Hints
- HashSet approach: O(n) time, O(n) space
- Or inorder to sorted array + two pointers
- BST iterator for O(h) space (advanced)

---

## Problem 9: Serialize and Deserialize BST

**Difficulty:** Medium | **Pattern:** BST Serialization
**LeetCode:** https://leetcode.com/problems/serialize-and-deserialize-bst/

### Problem

Design algorithm to serialize and deserialize BST. Encoded string should be compact as possible.

### Examples

```
root = [2,1,3]
Output: [2,1,3]

root = []
Output: []
```

### Constraints

- 0 <= Node count <= 10^4
- 0 <= Node.val <= 10^4
- Input is guaranteed BST

### Hints
- Preorder traversal for serialization
- Use BST property for deserialization
- No need for null markers
- Track min/max bounds during rebuild

---

## Problem 10: Inorder Successor in BST

**Difficulty:** Medium | **Pattern:** BST Navigation
**LeetCode:** https://leetcode.com/problems/inorder-successor-in-bst/

### Problem

Given BST and node, find inorder successor. Successor is node with smallest value greater than current node.

### Examples

```
root = [2,1,3], p = 1
Output: 2

root = [5,3,6,2,4,null,null,1], p = 6
Output: null
```

### Constraints

- Number of nodes in range [1, 10^4]
- -10^5 <= Node.val <= 10^5
- All values unique

### Hints
- If node has right child: successor is min of right
- If no right child: successor is ancestor where we last turned left
- Can solve in O(h) time without parent pointers

---

## Summary

**Total:** 10 problems (3 Easy, 7 Medium)

**Patterns:**
- BST Navigation
- Range Validation
- Inorder Traversal
- BST Construction/Modification
- BST Serialization

**Key Techniques:**
- Use BST property to eliminate half
- Inorder gives sorted sequence
- Range bounds for validation
- Successor/predecessor patterns

---

**Ready?** Say: `"Claude, give me the problem"` or `"Go"`

[Solutions](./SOLUTIONS.md) | [Hints](./HINTS.md)
