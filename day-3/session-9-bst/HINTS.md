# Hints - Session 9: Binary Search Trees

Progressive hints for 10 problems. Struggling is part of learning.

---

## Problem 1: Search in a BST

### Level 1
What property allows BST to eliminate half the tree at each step?

### Level 2
Compare target with current node. If target < node.val, search left only. If target > node.val, search right only.

### Level 3
```typescript
let current = root;
while (current) {
  if (val === current.val) return current;
  current = val < current.val ? current.left : current.right;
}
```

---

## Problem 2: Validate Binary Search Tree

### Level 1
Common mistake: only checking immediate children. Consider tree [10,5,15,null,null,12]. Node 12 satisfies 12 < 15 but violates 12 > 10. Need to track valid range for each node.

### Level 2
Each node must be within (min, max) range based on ancestors. Left child gets (min, parent.val), right child gets (parent.val, max).

### Level 3
```typescript
function validate(node: TreeNode | null, min: number, max: number): boolean {
  if (!node) return true;
  if (node.val <= min || node.val >= max) return false;
  return validate(node.left, min, node.val) &&
         validate(node.right, node.val, max);
}
```

---

## Problem 3: Kth Smallest Element in BST

### Level 1
What traversal gives sorted sequence in BST? How to find kth element in sorted sequence?

### Level 2
Inorder traversal (left, root, right) visits nodes in sorted order. Keep counter, return when counter reaches k.

### Level 3
```typescript
let count = 0, result = 0;
function inorder(node: TreeNode | null): void {
  if (!node || count >= k) return;
  inorder(node.left);
  count++;
  if (count === k) result = node.val;
  inorder(node.right);
}
```

---

## Problem 4: Lowest Common Ancestor of BST

### Level 1
If both p and q less than current node, where must LCA be? If both greater? What if they're on different sides?

### Level 2
Use BST property: if both < root, LCA in left; if both > root, LCA in right; otherwise root is LCA.

### Level 3
```typescript
while (current) {
  if (p.val < current.val && q.val < current.val) {
    current = current.left;
  } else if (p.val > current.val && q.val > current.val) {
    current = current.right;
  } else {
    return current; // Split point
  }
}
```

---

## Problem 5: Insert into a BST

### Level 1
New nodes always inserted as leaves. Where would value be if you searched for it? That's insertion point.

### Level 2
Navigate like search. When reaching null (where value would be), create new node there.

### Level 3
```typescript
let current = root;
while (true) {
  if (val < current.val) {
    if (!current.left) { current.left = new TreeNode(val); break; }
    current = current.left;
  } else {
    if (!current.right) { current.right = new TreeNode(val); break; }
    current = current.right;
  }
}
```

---

## Problem 6: Delete Node in a BST

### Level 1
Three cases: leaf (0 children), one child, two children. Which case needs special handling?

### Level 2
Two children: replace with inorder successor (min of right subtree) or predecessor (max of left). Copy value, then delete successor/predecessor.

### Level 3
```typescript
// Find node, then:
if (!root.left && !root.right) return null; // Leaf
if (!root.left) return root.right; // One child
if (!root.right) return root.left;

// Two children
let min = root.right;
while (min.left) min = min.left;
root.val = min.val;
root.right = deleteNode(root.right, min.val);
```

---

## Problem 7: Convert Sorted Array to BST

### Level 1
For balance, need equal elements on each side. Which element as root achieves this?

### Level 2
Use middle element as root. Recursively build left from left half, right from right half.

### Level 3
```typescript
function buildBST(left: number, right: number): TreeNode | null {
  if (left > right) return null;
  const mid = Math.floor((left + right) / 2);
  const root = new TreeNode(nums[mid]);
  root.left = buildBST(left, mid - 1);
  root.right = buildBST(mid + 1, right);
  return root;
}
```

---

## Problem 8: Two Sum IV - Input is BST

### Level 1
Could use HashSet like regular two sum. Or leverage BST property for sorted access?

### Level 2
Method 1: HashSet while traversing. Method 2: Inorder to sorted array, then two pointers.

### Level 3
```typescript
// Method 1: HashSet
const seen = new Set<number>();
function dfs(node: TreeNode | null): boolean {
  if (!node) return false;
  if (seen.has(k - node.val)) return true;
  seen.add(node.val);
  return dfs(node.left) || dfs(node.right);
}
```

---

## Problem 9: Serialize and Deserialize BST

### Level 1
Unlike general tree, BST can be reconstructed from preorder alone (no null markers needed). Why?

### Level 2
Serialize: preorder traversal. Deserialize: use BST property with min/max bounds to place each value.

### Level 3
```typescript
// Serialize: preorder
// Deserialize:
let index = 0;
function build(min: number, max: number): TreeNode | null {
  if (index >= values.length) return null;
  const val = values[index];
  if (val < min || val > max) return null;
  index++;
  const root = new TreeNode(val);
  root.left = build(min, val);
  root.right = build(val, max);
  return root;
}
```

---

## Problem 10: Inorder Successor in BST

### Level 1
Two cases: node has right child, or doesn't. What's successor in each case?

### Level 2
If right child exists: successor is min of right subtree. Otherwise: successor is ancestor where we last turned left.

### Level 3
```typescript
let successor: TreeNode | null = null;
let current = root;
while (current) {
  if (p.val < current.val) {
    successor = current; // Potential successor
    current = current.left;
  } else {
    current = current.right;
  }
}
return successor;
```

---

## Pattern Recognition

**Problem mentions:**
- "Sorted" or "kth" → Inorder traversal
- "Validate BST" → Range bounds (min, max)
- "Search" or "find" → Use BST property to eliminate half
- "Insert" or "delete" → Navigate to leaf/node, handle cases
- "Serialize" → Preorder + BST property

**Quick checks:**
- BST property must hold for ALL nodes, not just children
- Inorder gives sorted sequence
- O(h) operations use BST property
- Balanced: h = log n, Skewed: h = n

---

## Using Hints Effectively

1. Try 10+ min before Level 1
2. Try 5+ min after each hint
3. If use Level 3, mark for review
4. Don't feel bad - hints are for learning

Goal: Learn pattern, not just solve one problem.

---

[Back to Problems](./PROBLEMS.md) | [Back to Solutions](./SOLUTIONS.md)
