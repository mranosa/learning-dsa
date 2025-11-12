# Lesson: Binary Search Trees

---

## 📹 Video 1: BST Fundamentals (15 min)

**"Binary Search Tree Intro" by NeetCode**
https://www.youtube.com/watch?v=JfSdGQdAzq8

**Focus on:**
- BST definition and properties
- Left < root < right invariant
- Why BST is useful
- Time complexity analysis

---

## 📹 Video 2: BST Operations (15 min)

**"Binary Search Tree Operations" by NeetCode**
https://www.youtube.com/watch?v=bOjKxTUpUho

**Focus on:**
- Search algorithm
- Insert operation
- Delete operation (3 cases)
- Min/Max finding

---

## 📹 Video 3: BST Problem Patterns (12 min)

**"Validate Binary Search Tree" by NeetCode**
https://www.youtube.com/watch?v=s6ATEkipzow

**Alternative - BST Iterator:**
https://www.youtube.com/watch?v=RXy5RzGF5wo

**Focus on:**
- Range validation technique
- Inorder traversal pattern
- Common BST interview tricks

---

## 🎯 BST: Definition & Properties

### What is a BST?

Binary Search Tree is a binary tree with ordering property:

```typescript
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;

  constructor(val: number = 0) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

// BST Property:
// For every node:
// - All left subtree values < node.val
// - All right subtree values > node.val
// - Both subtrees are also BSTs
```

---

### Visual Example

```
Valid BST:
       8
      / \
     3   10
    / \    \
   1   6   14
      / \  /
     4  7 13

Inorder: [1, 3, 4, 6, 7, 8, 10, 13, 14] ← SORTED!
```

```
Invalid BST:
       8
      / \
     3   10
    / \    \
   1   6   14
      / \  /
     4  9 13
        ↑
    9 > 8, breaks BST property!
```

**Key Insight:** BST property must hold for ALL nodes, not just direct children.

---

## 🔧 BST Node Structure

```typescript
// Standard node definition
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

// Creating nodes
const root = new TreeNode(8);
root.left = new TreeNode(3);
root.right = new TreeNode(10);
root.left.left = new TreeNode(1);
root.left.right = new TreeNode(6);
```

---

## 📊 BST Operations

### Operation 1: Search - O(h)

**📹 Watch:** [Binary Search Tree Search](https://www.youtube.com/watch?v=JfSdGQdAzq8&t=180s) (3 min timestamp in BST intro)

```typescript
// Recursive approach
function searchBST(root: TreeNode | null, val: number): TreeNode | null {
  // Base case
  if (!root || root.val === val) return root;

  // Use BST property to guide search
  if (val < root.val) {
    return searchBST(root.left, val);
  } else {
    return searchBST(root.right, val);
  }
}

// Iterative approach (preferred - O(1) space)
function searchBSTIterative(root: TreeNode | null, val: number): TreeNode | null {
  let current = root;

  while (current) {
    if (val === current.val) return current;
    current = val < current.val ? current.left : current.right;
  }

  return null;
}
```

**Time:** O(h) | **Space:** O(1) iterative, O(h) recursive

---

### Operation 2: Insert - O(h)

**📹 Watch:** [BST Insert Operation](https://www.youtube.com/watch?v=bOjKxTUpUho&t=120s) (~4 min)

```typescript
// Recursive insertion
function insertIntoBST(root: TreeNode | null, val: number): TreeNode {
  // Base case: found insertion point
  if (!root) return new TreeNode(val);

  // Recursive insertion maintaining BST property
  if (val < root.val) {
    root.left = insertIntoBST(root.left, val);
  } else {
    root.right = insertIntoBST(root.right, val);
  }

  return root;
}

// Iterative insertion
function insertIntoBSTIterative(root: TreeNode | null, val: number): TreeNode {
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

**Time:** O(h) | **Space:** O(1) iterative, O(h) recursive

---

### Operation 3: Delete - O(h)

**📹 Watch:** [BST Delete Operation](https://www.youtube.com/watch?v=bOjKxTUpUho&t=420s) (~6 min)

Most complex BST operation with three cases:

```typescript
function deleteNode(root: TreeNode | null, key: number): TreeNode | null {
  if (!root) return null;

  // Find the node
  if (key < root.val) {
    root.left = deleteNode(root.left, key);
  } else if (key > root.val) {
    root.right = deleteNode(root.right, key);
  } else {
    // Found node to delete

    // Case 1: Leaf node (no children)
    if (!root.left && !root.right) return null;

    // Case 2: One child
    if (!root.left) return root.right;
    if (!root.right) return root.left;

    // Case 3: Two children
    // Find inorder successor (smallest in right subtree)
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

**Time:** O(h) | **Space:** O(h) for recursion

**Three Cases:**
1. **Leaf:** Simply remove
2. **One child:** Replace with child
3. **Two children:** Replace with inorder successor, then delete successor

---

### Operation 4: Find Min/Max - O(h)

```typescript
// Minimum is leftmost node
function findMin(root: TreeNode): TreeNode {
  while (root.left) {
    root = root.left;
  }
  return root;
}

// Maximum is rightmost node
function findMax(root: TreeNode): TreeNode {
  while (root.right) {
    root = root.right;
  }
  return root;
}
```

**Time:** O(h) | **Space:** O(1)

---

## 🎯 BST Time Complexity

| Operation | Balanced BST | Skewed BST | Notes |
|-----------|-------------|------------|-------|
| Search | O(log n) | O(n) | Halve search space each step |
| Insert | O(log n) | O(n) | Follow search path |
| Delete | O(log n) | O(n) | Find + restructure |
| Min/Max | O(log n) | O(n) | Go left/right to end |
| Inorder | O(n) | O(n) | Visit all nodes |

**Height matters:**
- Balanced: h = O(log n)
- Skewed (worst): h = O(n)

```
Balanced (height 3):    Skewed (height 5):
       8                      1
      / \                      \
     4   12                     2
    / \  / \                     \
   2  6 10 14                     3
                                   \
                                    4
                                     \
                                      5
```

---

## 🧩 BST Problem Patterns

### Pattern 1: Range Validation

**📹 Learn:** [Validate BST](https://www.youtube.com/watch?v=s6ATEkipzow) by NeetCode (12 min)

Used for: Validating BST structure.

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

  // Check if current node violates bounds
  if (node.val <= min || node.val >= max) {
    return false;
  }

  // Recursively validate subtrees with updated bounds
  return validate(node.left, min, node.val) &&
         validate(node.right, node.val, max);
}
```

**Key:** Track valid range (min, max) for each node. Left child inherits (min, root.val), right child inherits (root.val, max).

**Time:** O(n) | **Space:** O(h)

---

### Pattern 2: Inorder Traversal

**📹 Learn:** [Tree Traversals](https://www.youtube.com/watch?v=6oL-0TdVy28) by NeetCode (~10 min)

Used for: Kth smallest, BST to sorted array, validation.

```typescript
// Recursive inorder
function inorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];

  function inorder(node: TreeNode | null): void {
    if (!node) return;

    inorder(node.left);        // Left
    result.push(node.val);     // Root
    inorder(node.right);       // Right
  }

  inorder(root);
  return result; // Returns SORTED array for BST!
}

// Iterative inorder (using stack)
function inorderIterative(root: TreeNode | null): number[] {
  const result: number[] = [];
  const stack: TreeNode[] = [];
  let current = root;

  while (current || stack.length > 0) {
    // Go left as far as possible
    while (current) {
      stack.push(current);
      current = current.left;
    }

    // Process node
    current = stack.pop()!;
    result.push(current.val);

    // Go right
    current = current.right;
  }

  return result;
}
```

**Time:** O(n) | **Space:** O(h)

---

### Pattern 3: Kth Smallest Element

Used for: Finding kth element in sorted order.

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

**Key:** Inorder traversal visits nodes in sorted order. Stop at kth visit.

**Time:** O(k) in best case, O(n) worst | **Space:** O(h)

---

### Pattern 4: BST Navigation (LCA)

**📹 Learn:** [Lowest Common Ancestor](https://www.youtube.com/watch?v=gs2LMfuOR9k) by NeetCode (~8 min)

Used for: Finding lowest common ancestor.

```typescript
function lowestCommonAncestor(
  root: TreeNode,
  p: TreeNode,
  q: TreeNode
): TreeNode {
  // Both on left side
  if (p.val < root.val && q.val < root.val) {
    return lowestCommonAncestor(root.left!, p, q);
  }

  // Both on right side
  if (p.val > root.val && q.val > root.val) {
    return lowestCommonAncestor(root.right!, p, q);
  }

  // Split point or one equals root
  return root;
}
```

**Key:** Use BST property to determine which subtree contains LCA.

**Time:** O(h) | **Space:** O(1) iterative, O(h) recursive

---

### Pattern 5: BST Construction

Used for: Building BST from sorted array.

```typescript
function sortedArrayToBST(nums: number[]): TreeNode | null {
  if (nums.length === 0) return null;

  function buildBST(left: number, right: number): TreeNode | null {
    if (left > right) return null;

    // Middle element as root for balance
    const mid = Math.floor((left + right) / 2);
    const root = new TreeNode(nums[mid]);

    // Recursively build subtrees
    root.left = buildBST(left, mid - 1);
    root.right = buildBST(mid + 1, right);

    return root;
  }

  return buildBST(0, nums.length - 1);
}
```

**Key:** Middle element as root ensures balanced tree. Recursively build left and right halves.

**Time:** O(n) | **Space:** O(log n) for balanced recursion

---

## 💡 Interview Tips

### BST Recognition

**Problem mentions:**
- "Binary search tree" → Use BST properties
- "Sorted order" + tree → Think inorder traversal
- "Kth smallest/largest" → Inorder with counter
- "Validate tree" → Range validation
- "Find node in BST" → Binary search approach

### Quick Complexity Rules

**For BST operations:**
- Single path root to leaf: O(h) time
- Visit all nodes: O(n) time
- Recursive calls: O(h) space
- Iterative with stack: O(h) space
- Balanced tree: h = log n
- Skewed tree: h = n

**Say this:**
- "This is O(h) time where h is height. In balanced BST, h = O(log n)."
- "Using inorder traversal gives sorted sequence, so we can find kth element in O(k) time."
- "Range validation ensures BST property holds for all nodes, not just direct children."

---

### TypeScript Gotchas

```typescript
// ❌ Wrong - null pointer error
function search(root: TreeNode, val: number): TreeNode {
  if (val < root.val) {
    return search(root.left, val); // root.left might be null!
  }
}

// ✅ Correct - handle null
function search(root: TreeNode | null, val: number): TreeNode | null {
  if (!root) return null;
  if (val === root.val) return root;

  if (val < root.val) {
    return search(root.left, val);
  } else {
    return search(root.right, val);
  }
}

// ❌ Wrong - using === for nodes
if (node === p || node === q) // Compares references

// ✅ Correct - compare values
if (node.val === p.val || node.val === q.val)

// Integer bounds for validation
-Infinity / Infinity // Works for numbers
Number.MIN_SAFE_INTEGER / Number.MAX_SAFE_INTEGER // Alternative
```

---

### Common BST Patterns

| Problem Type | Pattern | Complexity |
|--------------|---------|------------|
| Search for value | BST search | O(h) |
| Validate BST | Range validation | O(n) |
| Kth smallest | Inorder with counter | O(k) |
| LCA in BST | BST navigation | O(h) |
| Build balanced BST | Use sorted array mid | O(n) |
| Two sum in BST | Inorder + two pointers | O(n) |

---

## ✅ Common Pitfalls

### Pitfall 1: Invalid BST Validation

```typescript
// ❌ WRONG: Only checks immediate children
function wrongValidation(root: TreeNode): boolean {
  if (!root) return true;

  if (root.left && root.left.val >= root.val) return false;
  if (root.right && root.right.val <= root.val) return false;

  return wrongValidation(root.left) && wrongValidation(root.right);
}

// Fails for:
//      10
//     /  \
//    5    15
//   / \
//  3   12  ← 12 > 10, breaks BST!
```

**Fix:** Use range validation with min/max bounds.

---

### Pitfall 2: Not Handling Null

```typescript
// ❌ Wrong
function insert(root: TreeNode, val: number): TreeNode {
  if (val < root.val) {
    root.left = insert(root.left, val); // root.left might be null!
  }
}

// ✅ Correct
function insert(root: TreeNode | null, val: number): TreeNode {
  if (!root) return new TreeNode(val);

  if (val < root.val) {
    root.left = insert(root.left, val);
  } else {
    root.right = insert(root.right, val);
  }

  return root;
}
```

---

### Pitfall 3: Integer Overflow in Bounds

```typescript
// ❌ Might overflow with edge values
function isValidBST(root: TreeNode | null): boolean {
  return validate(root, Number.MIN_SAFE_INTEGER, Number.MAX_SAFE_INTEGER);
}

// ✅ Use Infinity
function isValidBST(root: TreeNode | null): boolean {
  return validate(root, -Infinity, Infinity);
}
```

---

## 🎯 Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **BST property:** Left < root < right (ALL nodes)
- **Inorder traversal:** Gives sorted sequence
- **Search/Insert/Delete:** O(h) time
- **Validation:** Use range bounds (min, max)
- **Kth element:** Inorder traversal with counter

**Complexity:**
- Balanced BST: O(log n) operations
- Skewed BST: O(n) operations
- Always state which case you're analyzing

---

[Back to Session README](./README.md)
