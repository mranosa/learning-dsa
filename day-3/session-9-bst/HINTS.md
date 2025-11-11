# BST Hints

## 1. Search in a BST

### Hint 1 (Gentle)
Remember the key property of BST: for any node, all values in the left subtree are smaller and all values in the right subtree are larger. How can you use this to eliminate half the tree at each step?

### Hint 2 (Direct)
At each node, compare the target value with the current node's value. If target is smaller, where should you search? If larger?

### Hint 3 (Detailed)
```typescript
// If val equals current node value -> found!
// If val < current node value -> search left subtree only
// If val > current node value -> search right subtree only
// This gives O(h) time complexity
```

---

## 2. Validate Binary Search Tree

### Hint 1 (Gentle)
A common mistake is only comparing a node with its immediate children. But what about this tree: [5, 1, 4, null, null, 3, 6]? The node 3 is less than its parent 4, but it's not less than the root 5. How can you track the valid range for each node?

### Hint 2 (Direct)
Each node must be within a certain range based on its ancestors. As you traverse left, the maximum allowed value decreases. As you traverse right, the minimum allowed value increases.

### Hint 3 (Detailed)
```typescript
// Start with range (-∞, +∞) for root
// For left child: range becomes (min, parent.val)
// For right child: range becomes (parent.val, max)
// Check if node.val is within its allowed range
// Alternative: inorder traversal should give sorted sequence
```

---

## 3. Kth Smallest Element in a BST

### Hint 1 (Gentle)
What traversal of a BST gives you elements in sorted order? Once you have a sorted sequence, finding the kth element is straightforward.

### Hint 2 (Direct)
Perform an inorder traversal (left → root → right) and keep a counter. When the counter reaches k, you've found your answer. Can you optimize to stop early?

### Hint 3 (Detailed)
```typescript
// Use inorder traversal with a counter:
// 1. Traverse left subtree
// 2. Increment counter when processing node
// 3. If counter === k, return current value
// 4. Continue to right subtree if needed
// Early termination saves time
```

---

## 4. Lowest Common Ancestor of a BST

### Hint 1 (Gentle)
Unlike a regular binary tree, BST has a special property. If both p and q are less than the current node, where must their LCA be? What if both are greater?

### Hint 2 (Direct)
The LCA is the first node where p and q diverge into different subtrees. If both are on the same side (left or right), move to that side. Otherwise, the current node is the LCA.

### Hint 3 (Detailed)
```typescript
// Three cases at each node:
// 1. Both p and q < current -> LCA is in left subtree
// 2. Both p and q > current -> LCA is in right subtree
// 3. p and q on different sides -> current is LCA
// This works in O(h) time without visiting all nodes
```

---

## 5. Insert into a BST

### Hint 1 (Gentle)
New nodes in a BST are always inserted as leaves. You never need to rearrange existing nodes. Where would a new value go if you were searching for it?

### Hint 2 (Direct)
Navigate the tree as if searching for the value. When you reach a null pointer (where the value would be if it existed), that's where you insert the new node.

### Hint 3 (Detailed)
```typescript
// Start at root:
// If val < current.val:
//   - If left child exists, go left
//   - If left is null, insert new node as left child
// If val > current.val:
//   - If right child exists, go right
//   - If right is null, insert new node as right child
```

---

## 6. Delete Node in a BST

### Hint 1 (Gentle)
Deletion has three cases based on the number of children: no children (leaf), one child, or two children. The tricky case is two children - you need a replacement that maintains BST property.

### Hint 2 (Direct)
For two children case: find either the inorder successor (smallest in right subtree) or predecessor (largest in left subtree). Replace the node's value with this, then delete the successor/predecessor.

### Hint 3 (Detailed)
```typescript
// Case 1 (leaf): Simply remove the node
// Case 2 (one child): Replace node with its child
// Case 3 (two children):
//   - Find min in right subtree (successor)
//   - Copy successor's value to current node
//   - Delete successor (which has at most 1 child)
// This maintains BST property
```

---

## 7. Convert Sorted Array to BST

### Hint 1 (Gentle)
A height-balanced BST has roughly equal number of nodes in left and right subtrees. If you have a sorted array, which element would make a good root to achieve balance?

### Hint 2 (Direct)
Choose the middle element as root. This ensures equal (±1) elements on each side. Apply this recursively to build left and right subtrees from the corresponding array portions.

### Hint 3 (Detailed)
```typescript
// For array[left...right]:
// 1. mid = (left + right) / 2
// 2. Create node with array[mid]
// 3. Left subtree from array[left...mid-1]
// 4. Right subtree from array[mid+1...right]
// Base case: left > right returns null
```

---

## 8. Two Sum IV - Input is a BST

### Hint 1 (Gentle)
You could treat this like a regular tree and use a HashSet. But can you leverage the BST property for a potentially more elegant solution?

### Hint 2 (Direct)
BST gives you sorted access via inorder traversal. Once you have a sorted array, this becomes the classic two-pointer two sum problem. Alternatively, use a HashSet while traversing.

### Hint 3 (Detailed)
```typescript
// Method 1: HashSet during any traversal
//   - Check if (k - current.val) exists in set
//   - Add current.val to set
// Method 2: Two pointers on sorted array
//   - Get sorted array via inorder
//   - Use left/right pointers to find sum
// Method 3: BST iterators (advanced)
```

---

## 9. Serialize and Deserialize BST

### Hint 1 (Gentle)
Unlike general binary trees, BST has a special property that can help reconstruction. If you know the preorder (or postorder) traversal of a BST, can you uniquely reconstruct it?

### Hint 2 (Direct)
Use preorder traversal for serialization. During deserialization, use the BST property with min/max bounds to determine where each value belongs, without needing to store null markers.

### Hint 3 (Detailed)
```typescript
// Serialize: Simple preorder traversal to string
// Deserialize with preorder:
//   - First value is root
//   - Values less than root go to left subtree
//   - Values greater than root go to right subtree
//   - Use bounds to determine where values belong
// No need for null markers unlike general trees!
```

---

## 10. Recover Binary Search Tree

### Hint 1 (Gentle)
If two nodes are swapped in a BST, the inorder traversal will have elements out of order. How many inversions (where a larger value comes before a smaller one) will there be?

### Hint 2 (Direct)
There will be either one or two inversions in the inorder sequence. If nodes are adjacent in inorder, there's one inversion. If not adjacent, there are two inversions. Find these inversions to identify the swapped nodes.

### Hint 3 (Detailed)
```typescript
// During inorder traversal, track previous node:
// First inversion: prev.val > current.val
//   - First swapped node is prev
//   - Second swapped node is current (may update)
// Second inversion (if exists):
//   - Update second swapped node to current
// After traversal, swap the values of the two nodes
// For O(1) space: Use Morris traversal
```

---

## General BST Problem-Solving Tips

### Pattern Recognition
- **"Sorted" or "ordered"** → Think inorder traversal
- **"kth smallest/largest"** → Inorder with counter
- **"Range" or "bounds"** → Track min/max values
- **"Validate"** → Check BST property with bounds
- **"Common ancestor"** → Use BST property to navigate

### Common Techniques
1. **Inorder = Sorted**: Most important BST property
2. **Range bounds**: Pass min/max to validate subtrees
3. **BST navigation**: Eliminate half at each step
4. **Successor/Predecessor**: Min of right / Max of left
5. **Morris traversal**: For O(1) space complexity

### Debugging Tips
- Draw small examples (3-5 nodes)
- Trace through your algorithm step by step
- Check edge cases: empty tree, single node, skewed tree
- Verify BST property is maintained after modifications