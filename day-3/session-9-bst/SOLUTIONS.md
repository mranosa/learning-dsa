# Solutions - Session 9: Binary Search Trees

TypeScript solutions with complexity analysis.

---

## Problem 1: Search in a BST

### Approach 1: Recursive

```typescript
function searchBST(root: TreeNode | null, val: number): TreeNode | null {
  if (!root || root.val === val) return root;

  if (val < root.val) {
    return searchBST(root.left, val);
  } else {
    return searchBST(root.right, val);
  }
}
```

**Time:** O(h) | **Space:** O(h) recursion

---

### Approach 2: Iterative (Optimal) ✅

```typescript
function searchBST(root: TreeNode | null, val: number): TreeNode | null {
  let current = root;

  while (current) {
    if (val === current.val) return current;
    current = val < current.val ? current.left : current.right;
  }

  return null;
}
```

**Time:** O(h) | **Space:** O(1)

**Key:** Use BST property to eliminate half the tree at each step. Iterative saves space.

**Say:** "Leveraging BST property, we can search in O(h) time. Iterative version uses O(1) space vs O(h) for recursion."

---

## Problem 2: Validate Binary Search Tree

### Approach 1: Range Validation (Optimal) ✅

```typescript
function isValidBST(root: TreeNode | null): boolean {
  return validate(root, -Infinity, Infinity);
}

function validate(
  node: TreeNode | null,
  min: number,
  max: number
): boolean {
  if (!node) return true;

  if (node.val <= min || node.val >= max) {
    return false;
  }

  return validate(node.left, min, node.val) &&
         validate(node.right, node.val, max);
}
```

**Time:** O(n) | **Space:** O(h)

---

### Approach 2: Inorder Traversal

```typescript
function isValidBST(root: TreeNode | null): boolean {
  let prev: number | null = null;

  function inorder(node: TreeNode | null): boolean {
    if (!node) return true;

    if (!inorder(node.left)) return false;

    if (prev !== null && node.val <= prev) {
      return false;
    }
    prev = node.val;

    return inorder(node.right);
  }

  return inorder(root);
}
```

**Time:** O(n) | **Space:** O(h)

**Key:** Range validation ensures BST property holds for ALL nodes, not just immediate children. Inorder approach checks if traversal is strictly increasing.

**Say:** "Using range bounds (min, max) propagates valid range down the tree. Left child gets (min, parent.val), right gets (parent.val, max)."

---

## Problem 3: Kth Smallest Element in BST

```typescript
function kthSmallest(root: TreeNode | null, k: number): number {
  let count = 0;
  let result = 0;

  function inorder(node: TreeNode | null): void {
    if (!node || count >= k) return;

    inorder(node.left);

    count++;
    if (count === k) {
      result = node.val;
      return;
    }

    inorder(node.right);
  }

  inorder(root);
  return result;
}
```

**Time:** O(k) best case, O(n) worst | **Space:** O(h)

**Key:** Inorder traversal of BST visits nodes in sorted order. Stop at kth visit for efficiency.

**Say:** "Inorder traversal gives sorted sequence. Track counter and return value at kth position. Early termination optimizes to O(k) in best case."

---

## Problem 4: Lowest Common Ancestor of BST

### Approach 1: Recursive

```typescript
function lowestCommonAncestor(
  root: TreeNode,
  p: TreeNode,
  q: TreeNode
): TreeNode {
  if (p.val < root.val && q.val < root.val) {
    return lowestCommonAncestor(root.left!, p, q);
  }

  if (p.val > root.val && q.val > root.val) {
    return lowestCommonAncestor(root.right!, p, q);
  }

  return root;
}
```

**Time:** O(h) | **Space:** O(h)

---

### Approach 2: Iterative (Optimal) ✅

```typescript
function lowestCommonAncestor(
  root: TreeNode,
  p: TreeNode,
  q: TreeNode
): TreeNode {
  let current = root;

  while (current) {
    if (p.val < current.val && q.val < current.val) {
      current = current.left!;
    } else if (p.val > current.val && q.val > current.val) {
      current = current.right!;
    } else {
      return current;
    }
  }

  return root;
}
```

**Time:** O(h) | **Space:** O(1)

**Key:** Use BST property. If both nodes less than current, LCA is in left subtree. If both greater, LCA is in right. Otherwise, current is LCA.

---

## Problem 5: Insert into a BST

### Approach 1: Recursive

```typescript
function insertIntoBST(root: TreeNode | null, val: number): TreeNode {
  if (!root) return new TreeNode(val);

  if (val < root.val) {
    root.left = insertIntoBST(root.left, val);
  } else {
    root.right = insertIntoBST(root.right, val);
  }

  return root;
}
```

**Time:** O(h) | **Space:** O(h)

---

### Approach 2: Iterative (Optimal) ✅

```typescript
function insertIntoBST(root: TreeNode | null, val: number): TreeNode {
  if (!root) return new TreeNode(val);

  let current = root;

  while (true) {
    if (val < current.val) {
      if (!current.left) {
        current.left = new TreeNode(val);
        break;
      }
      current = current.left;
    } else {
      if (!current.right) {
        current.right = new TreeNode(val);
        break;
      }
      current = current.right;
    }
  }

  return root;
}
```

**Time:** O(h) | **Space:** O(1)

**Key:** New nodes always inserted as leaves. Navigate like search until finding null position.

---

## Problem 6: Delete Node in a BST

```typescript
function deleteNode(root: TreeNode | null, key: number): TreeNode | null {
  if (!root) return null;

  if (key < root.val) {
    root.left = deleteNode(root.left, key);
  } else if (key > root.val) {
    root.right = deleteNode(root.right, key);
  } else {
    // Found node to delete

    // Case 1: Leaf node
    if (!root.left && !root.right) return null;

    // Case 2: One child
    if (!root.left) return root.right;
    if (!root.right) return root.left;

    // Case 3: Two children
    // Find inorder successor (min in right subtree)
    let minNode = root.right;
    while (minNode.left) {
      minNode = minNode.left;
    }

    // Replace value with successor
    root.val = minNode.val;

    // Delete successor
    root.right = deleteNode(root.right, minNode.val);
  }

  return root;
}
```

**Time:** O(h) | **Space:** O(h)

**Key:** Three cases based on children count:
1. **Leaf:** Simply remove
2. **One child:** Replace with child
3. **Two children:** Replace with inorder successor, then delete successor

**Say:** "Deletion has three cases. Two children is tricky - replace node value with inorder successor (min of right subtree), then recursively delete that successor."

---

## Problem 7: Convert Sorted Array to BST

```typescript
function sortedArrayToBST(nums: number[]): TreeNode | null {
  return buildBST(0, nums.length - 1);

  function buildBST(left: number, right: number): TreeNode | null {
    if (left > right) return null;

    const mid = Math.floor((left + right) / 2);
    const root = new TreeNode(nums[mid]);

    root.left = buildBST(left, mid - 1);
    root.right = buildBST(mid + 1, right);

    return root;
  }
}
```

**Time:** O(n) | **Space:** O(log n)

**Key:** Choose middle element as root to ensure balance. Recursively build left and right subtrees from corresponding halves.

**Say:** "Using middle element as root ensures equal elements on each side, creating balanced BST. Recursively apply to left and right halves."

---

## Problem 8: Two Sum IV - Input is BST

### Approach 1: HashSet (Simple)

```typescript
function findTarget(root: TreeNode | null, k: number): boolean {
  const seen = new Set<number>();

  function dfs(node: TreeNode | null): boolean {
    if (!node) return false;

    if (seen.has(k - node.val)) return true;

    seen.add(node.val);

    return dfs(node.left) || dfs(node.right);
  }

  return dfs(root);
}
```

**Time:** O(n) | **Space:** O(n)

---

### Approach 2: Two Pointers on Sorted Array ✅

```typescript
function findTarget(root: TreeNode | null, k: number): boolean {
  const sorted: number[] = [];

  function inorder(node: TreeNode | null): void {
    if (!node) return;
    inorder(node.left);
    sorted.push(node.val);
    inorder(node.right);
  }

  inorder(root);

  let left = 0, right = sorted.length - 1;

  while (left < right) {
    const sum = sorted[left] + sorted[right];
    if (sum === k) return true;
    if (sum < k) left++;
    else right--;
  }

  return false;
}
```

**Time:** O(n) | **Space:** O(n)

**Key:** Leverage BST property - inorder gives sorted array. Then use two pointers for two sum.

---

## Problem 9: Serialize and Deserialize BST

```typescript
class Codec {
  serialize(root: TreeNode | null): string {
    const result: number[] = [];

    function preorder(node: TreeNode | null): void {
      if (!node) return;
      result.push(node.val);
      preorder(node.left);
      preorder(node.right);
    }

    preorder(root);
    return result.join(',');
  }

  deserialize(data: string): TreeNode | null {
    if (!data) return null;

    const values = data.split(',').map(Number);
    let index = 0;

    function buildBST(min: number, max: number): TreeNode | null {
      if (index >= values.length) return null;

      const val = values[index];
      if (val < min || val > max) return null;

      index++;
      const root = new TreeNode(val);
      root.left = buildBST(min, val);
      root.right = buildBST(val, max);

      return root;
    }

    return buildBST(-Infinity, Infinity);
  }
}
```

**Time:** O(n) | **Space:** O(n)

**Key:** Preorder traversal for serialization. Use BST property with range bounds for deserialization - no need for null markers unlike general trees.

**Say:** "BST property allows reconstruction from preorder alone. Use min/max bounds to determine where each value belongs without null markers."

---

## Problem 10: Inorder Successor in BST

```typescript
function inorderSuccessor(root: TreeNode | null, p: TreeNode): TreeNode | null {
  let successor: TreeNode | null = null;
  let current = root;

  while (current) {
    if (p.val < current.val) {
      // Current could be successor, go left for smaller
      successor = current;
      current = current.left;
    } else {
      // p.val >= current.val, go right
      current = current.right;
    }
  }

  return successor;
}
```

**Time:** O(h) | **Space:** O(1)

**Alternative with right subtree:**

```typescript
function inorderSuccessor(root: TreeNode | null, p: TreeNode): TreeNode | null {
  // If p has right child, successor is min of right subtree
  if (p.right) {
    let min = p.right;
    while (min.left) {
      min = min.left;
    }
    return min;
  }

  // Otherwise, find ancestor where we last turned left
  let successor: TreeNode | null = null;
  let current = root;

  while (current) {
    if (p.val < current.val) {
      successor = current;
      current = current.left;
    } else {
      current = current.right;
    }
  }

  return successor;
}
```

**Time:** O(h) | **Space:** O(1)

**Key:** Two cases:
1. If node has right child: successor is min of right subtree
2. Otherwise: successor is ancestor where we last turned left

---

## Pattern Summary

### Range Validation (Problem 2)
- Track (min, max) bounds for each node
- Left child: (min, node.val)
- Right child: (node.val, max)
- Validates BST property globally

### Inorder Traversal (Problems 3, 8)
- BST inorder gives sorted sequence
- Use for kth element, validation, two sum
- Can optimize with early termination

### BST Navigation (Problems 1, 4, 10)
- Use BST property to eliminate half
- O(h) time vs O(n) for general tree
- Iterative saves space

### BST Modification (Problems 5, 6)
- Insert: always as leaf
- Delete: three cases by children count
- Successor/predecessor for two children case

### BST Construction (Problems 7, 9)
- From sorted: use middle as root
- Serialization: preorder + BST property
- No null markers needed

---

[Back to Problems](./PROBLEMS.md) | [Back to README](./README.md)
