# BST Solutions

## 1. Search in a BST

### Approach 1: Recursive
```typescript
function searchBST(root: TreeNode | null, val: number): TreeNode | null {
    // Base case: null or found
    if (!root || root.val === val) {
        return root;
    }

    // Use BST property to decide direction
    if (val < root.val) {
        return searchBST(root.left, val);
    } else {
        return searchBST(root.right, val);
    }
}

// Time: O(h) where h is height of tree
// Space: O(h) for recursion stack
```

### Approach 2: Iterative (Space Optimized)
```typescript
function searchBST(root: TreeNode | null, val: number): TreeNode | null {
    let current = root;

    while (current) {
        if (current.val === val) {
            return current;
        } else if (val < current.val) {
            current = current.left;
        } else {
            current = current.right;
        }
    }

    return null;
}

// Time: O(h)
// Space: O(1)
```

---

## 2. Validate Binary Search Tree

### Approach 1: Range Bounds
```typescript
function isValidBST(root: TreeNode | null): boolean {
    return validate(root, -Infinity, Infinity);
}

function validate(node: TreeNode | null, min: number, max: number): boolean {
    // Empty tree is valid
    if (!node) return true;

    // Check current node violates BST property
    if (node.val <= min || node.val >= max) {
        return false;
    }

    // Recursively validate subtrees with updated bounds
    return validate(node.left, min, node.val) &&
           validate(node.right, node.val, max);
}

// Time: O(n) - visit each node once
// Space: O(h) - recursion stack
```

### Approach 2: Inorder Traversal
```typescript
function isValidBST(root: TreeNode | null): boolean {
    let prev: number | null = null;

    function inorder(node: TreeNode | null): boolean {
        if (!node) return true;

        // Check left subtree
        if (!inorder(node.left)) return false;

        // Check current node
        if (prev !== null && node.val <= prev) {
            return false;
        }
        prev = node.val;

        // Check right subtree
        return inorder(node.right);
    }

    return inorder(root);
}

// Time: O(n)
// Space: O(h)
```

### Approach 3: Iterative with Stack
```typescript
function isValidBST(root: TreeNode | null): boolean {
    if (!root) return true;

    const stack: Array<[TreeNode, number, number]> = [];
    stack.push([root, -Infinity, Infinity]);

    while (stack.length > 0) {
        const [node, min, max] = stack.pop()!;

        if (node.val <= min || node.val >= max) {
            return false;
        }

        if (node.left) {
            stack.push([node.left, min, node.val]);
        }
        if (node.right) {
            stack.push([node.right, node.val, max]);
        }
    }

    return true;
}

// Time: O(n)
// Space: O(h)
```

---

## 3. Kth Smallest Element in a BST

### Approach 1: Inorder Traversal with Early Stop
```typescript
function kthSmallest(root: TreeNode | null, k: number): number {
    let count = 0;
    let result = -1;

    function inorder(node: TreeNode | null): void {
        if (!node || count >= k) return;

        // Process left subtree
        inorder(node.left);

        // Process current node
        count++;
        if (count === k) {
            result = node.val;
            return;
        }

        // Process right subtree
        inorder(node.right);
    }

    inorder(root);
    return result;
}

// Time: O(k) in best case, O(n) worst case
// Space: O(h)
```

### Approach 2: Iterative Inorder
```typescript
function kthSmallest(root: TreeNode | null, k: number): number {
    const stack: TreeNode[] = [];
    let current = root;
    let count = 0;

    while (current || stack.length > 0) {
        // Go to leftmost node
        while (current) {
            stack.push(current);
            current = current.left;
        }

        // Process current node
        current = stack.pop()!;
        count++;

        if (count === k) {
            return current.val;
        }

        // Move to right subtree
        current = current.right;
    }

    return -1;
}

// Time: O(k)
// Space: O(h)
```

---

## 4. Lowest Common Ancestor of a BST

### Approach 1: Recursive Using BST Property
```typescript
function lowestCommonAncestor(
    root: TreeNode | null,
    p: TreeNode,
    q: TreeNode
): TreeNode | null {
    if (!root) return null;

    // Both nodes in left subtree
    if (p.val < root.val && q.val < root.val) {
        return lowestCommonAncestor(root.left, p, q);
    }

    // Both nodes in right subtree
    if (p.val > root.val && q.val > root.val) {
        return lowestCommonAncestor(root.right, p, q);
    }

    // Nodes are on different sides or one is the root
    return root;
}

// Time: O(h)
// Space: O(h)
```

### Approach 2: Iterative
```typescript
function lowestCommonAncestor(
    root: TreeNode | null,
    p: TreeNode,
    q: TreeNode
): TreeNode | null {
    let current = root;

    while (current) {
        if (p.val < current.val && q.val < current.val) {
            current = current.left;
        } else if (p.val > current.val && q.val > current.val) {
            current = current.right;
        } else {
            return current;
        }
    }

    return null;
}

// Time: O(h)
// Space: O(1)
```

---

## 5. Insert into a BST

### Approach 1: Recursive
```typescript
function insertIntoBST(root: TreeNode | null, val: number): TreeNode | null {
    // Base case: found insertion point
    if (!root) {
        return new TreeNode(val);
    }

    // Recursively find correct position
    if (val < root.val) {
        root.left = insertIntoBST(root.left, val);
    } else {
        root.right = insertIntoBST(root.right, val);
    }

    return root;
}

// Time: O(h)
// Space: O(h)
```

### Approach 2: Iterative
```typescript
function insertIntoBST(root: TreeNode | null, val: number): TreeNode | null {
    const newNode = new TreeNode(val);

    if (!root) return newNode;

    let current = root;

    while (true) {
        if (val < current.val) {
            if (!current.left) {
                current.left = newNode;
                break;
            }
            current = current.left;
        } else {
            if (!current.right) {
                current.right = newNode;
                break;
            }
            current = current.right;
        }
    }

    return root;
}

// Time: O(h)
// Space: O(1)
```

---

## 6. Delete Node in a BST

### Complete Solution with All Cases
```typescript
function deleteNode(root: TreeNode | null, key: number): TreeNode | null {
    if (!root) return null;

    // Find the node to delete
    if (key < root.val) {
        root.left = deleteNode(root.left, key);
    } else if (key > root.val) {
        root.right = deleteNode(root.right, key);
    } else {
        // Found the node to delete

        // Case 1: Leaf node (no children)
        if (!root.left && !root.right) {
            return null;
        }

        // Case 2: Node with only one child
        if (!root.left) return root.right;
        if (!root.right) return root.left;

        // Case 3: Node with two children
        // Find inorder successor (smallest in right subtree)
        let successor = root.right;
        while (successor.left) {
            successor = successor.left;
        }

        // Replace current node's value with successor's value
        root.val = successor.val;

        // Delete the successor
        root.right = deleteNode(root.right, successor.val);
    }

    return root;
}

// Time: O(h)
// Space: O(h)
```

### Alternative: Using Predecessor Instead
```typescript
function deleteNodePredecessor(root: TreeNode | null, key: number): TreeNode | null {
    if (!root) return null;

    if (key < root.val) {
        root.left = deleteNodePredecessor(root.left, key);
    } else if (key > root.val) {
        root.right = deleteNodePredecessor(root.right, key);
    } else {
        if (!root.left && !root.right) return null;
        if (!root.left) return root.right;
        if (!root.right) return root.left;

        // Find predecessor (largest in left subtree)
        let predecessor = root.left;
        while (predecessor.right) {
            predecessor = predecessor.right;
        }

        root.val = predecessor.val;
        root.left = deleteNodePredecessor(root.left, predecessor.val);
    }

    return root;
}

// Time: O(h)
// Space: O(h)
```

---

## 7. Convert Sorted Array to BST

### Approach 1: Recursive Binary Search
```typescript
function sortedArrayToBST(nums: number[]): TreeNode | null {
    return buildBST(nums, 0, nums.length - 1);
}

function buildBST(nums: number[], left: number, right: number): TreeNode | null {
    if (left > right) return null;

    // Choose middle element as root
    const mid = Math.floor((left + right) / 2);
    const root = new TreeNode(nums[mid]);

    // Recursively build left and right subtrees
    root.left = buildBST(nums, left, mid - 1);
    root.right = buildBST(nums, mid + 1, right);

    return root;
}

// Time: O(n) - process each element once
// Space: O(log n) - recursion stack for balanced tree
```

### Approach 2: Choose Different Mid for Balance
```typescript
function sortedArrayToBST(nums: number[]): TreeNode | null {
    return buildBST(nums, 0, nums.length - 1);
}

function buildBST(nums: number[], left: number, right: number): TreeNode | null {
    if (left > right) return null;

    // Alternative: always choose left middle for consistency
    const mid = left + Math.floor((right - left) / 2);
    // Or: always choose right middle
    // const mid = left + Math.ceil((right - left) / 2);

    const root = new TreeNode(nums[mid]);
    root.left = buildBST(nums, left, mid - 1);
    root.right = buildBST(nums, mid + 1, right);

    return root;
}

// Time: O(n)
// Space: O(log n)
```

---

## 8. Two Sum IV - Input is a BST

### Approach 1: HashSet with Any Traversal
```typescript
function findTarget(root: TreeNode | null, k: number): boolean {
    const seen = new Set<number>();

    function dfs(node: TreeNode | null): boolean {
        if (!node) return false;

        // Check if complement exists
        if (seen.has(k - node.val)) {
            return true;
        }

        seen.add(node.val);

        return dfs(node.left) || dfs(node.right);
    }

    return dfs(root);
}

// Time: O(n)
// Space: O(n)
```

### Approach 2: Two Pointers on Sorted Array
```typescript
function findTarget(root: TreeNode | null, k: number): boolean {
    const sorted: number[] = [];

    // Get sorted array via inorder traversal
    function inorder(node: TreeNode | null): void {
        if (!node) return;
        inorder(node.left);
        sorted.push(node.val);
        inorder(node.right);
    }

    inorder(root);

    // Two pointers on sorted array
    let left = 0, right = sorted.length - 1;

    while (left < right) {
        const sum = sorted[left] + sorted[right];
        if (sum === k) return true;
        if (sum < k) left++;
        else right--;
    }

    return false;
}

// Time: O(n)
// Space: O(n)
```

### Approach 3: BST Iterator (Advanced)
```typescript
class BSTIterator {
    private stack: TreeNode[] = [];
    private reverse: boolean;

    constructor(root: TreeNode | null, reverse: boolean = false) {
        this.reverse = reverse;
        this.pushAll(root);
    }

    next(): number {
        const node = this.stack.pop()!;
        this.pushAll(this.reverse ? node.left : node.right);
        return node.val;
    }

    hasNext(): boolean {
        return this.stack.length > 0;
    }

    private pushAll(node: TreeNode | null): void {
        while (node) {
            this.stack.push(node);
            node = this.reverse ? node.right : node.left;
        }
    }
}

function findTarget(root: TreeNode | null, k: number): boolean {
    if (!root) return false;

    const leftIter = new BSTIterator(root, false);
    const rightIter = new BSTIterator(root, true);

    let left = leftIter.next();
    let right = rightIter.next();

    while (left < right) {
        const sum = left + right;
        if (sum === k) return true;
        if (sum < k) left = leftIter.next();
        else right = rightIter.next();
    }

    return false;
}

// Time: O(n)
// Space: O(h)
```

---

## 9. Serialize and Deserialize BST

### Approach 1: Preorder Traversal
```typescript
class Codec {
    // Serialize using preorder traversal
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

    // Deserialize using BST property
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

// Time: O(n) for both operations
// Space: O(n) for serialized string, O(h) for recursion
```

### Approach 2: Postorder Traversal
```typescript
class Codec {
    serialize(root: TreeNode | null): string {
        const result: number[] = [];

        function postorder(node: TreeNode | null): void {
            if (!node) return;
            postorder(node.left);
            postorder(node.right);
            result.push(node.val);
        }

        postorder(root);
        return result.join(',');
    }

    deserialize(data: string): TreeNode | null {
        if (!data) return null;

        const values = data.split(',').map(Number);

        function buildBST(min: number, max: number): TreeNode | null {
            if (values.length === 0) return null;

            const val = values[values.length - 1];
            if (val < min || val > max) return null;

            values.pop();
            const root = new TreeNode(val);
            // Build right first (reverse of postorder)
            root.right = buildBST(val, max);
            root.left = buildBST(min, val);

            return root;
        }

        return buildBST(-Infinity, Infinity);
    }
}

// Time: O(n)
// Space: O(n)
```

---

## 10. Recover Binary Search Tree

### Approach 1: Inorder Traversal with Array
```typescript
function recoverTree(root: TreeNode | null): void {
    const inorder: TreeNode[] = [];

    // Get inorder traversal
    function traverse(node: TreeNode | null): void {
        if (!node) return;
        traverse(node.left);
        inorder.push(node);
        traverse(node.right);
    }

    traverse(root);

    // Find two swapped nodes
    let first: TreeNode | null = null;
    let second: TreeNode | null = null;

    for (let i = 0; i < inorder.length - 1; i++) {
        if (inorder[i].val > inorder[i + 1].val) {
            if (!first) {
                first = inorder[i];
                second = inorder[i + 1];
            } else {
                second = inorder[i + 1];
            }
        }
    }

    // Swap values
    if (first && second) {
        [first.val, second.val] = [second.val, first.val];
    }
}

// Time: O(n)
// Space: O(n)
```

### Approach 2: Morris Traversal (O(1) Space)
```typescript
function recoverTree(root: TreeNode | null): void {
    let first: TreeNode | null = null;
    let second: TreeNode | null = null;
    let prev: TreeNode | null = null;
    let current = root;

    // Morris inorder traversal
    while (current) {
        if (!current.left) {
            // Process current node
            if (prev && prev.val > current.val) {
                if (!first) {
                    first = prev;
                    second = current;
                } else {
                    second = current;
                }
            }
            prev = current;
            current = current.right;
        } else {
            // Find inorder predecessor
            let predecessor = current.left;
            while (predecessor.right && predecessor.right !== current) {
                predecessor = predecessor.right;
            }

            if (!predecessor.right) {
                // Create thread
                predecessor.right = current;
                current = current.left;
            } else {
                // Process current node
                if (prev && prev.val > current.val) {
                    if (!first) {
                        first = prev;
                        second = current;
                    } else {
                        second = current;
                    }
                }
                prev = current;

                // Remove thread
                predecessor.right = null;
                current = current.right;
            }
        }
    }

    // Swap values
    if (first && second) {
        [first.val, second.val] = [second.val, first.val];
    }
}

// Time: O(n)
// Space: O(1) - true constant space!
```