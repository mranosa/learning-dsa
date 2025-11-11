# TypeScript Code Templates

Ready-to-use templates for common patterns. Copy and adapt these for your solutions.

---

## Table of Contents
1. [Tree Traversals](#tree-traversals)
2. [Graph Traversals](#graph-traversals)
3. [Binary Search](#binary-search)
4. [Sliding Window](#sliding-window)
5. [Two Pointers](#two-pointers)
6. [Dynamic Programming](#dynamic-programming)
7. [Backtracking](#backtracking)
8. [Union-Find](#union-find)

---

## Tree Traversals

### Tree Node Definition
```typescript
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;

  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}
```

### DFS - Inorder (Recursive)
```typescript
function inorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];

  function dfs(node: TreeNode | null): void {
    if (!node) return;

    dfs(node.left);       // Left
    result.push(node.val); // Root
    dfs(node.right);      // Right
  }

  dfs(root);
  return result;
}
```

### DFS - Preorder (Recursive)
```typescript
function preorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];

  function dfs(node: TreeNode | null): void {
    if (!node) return;

    result.push(node.val); // Root
    dfs(node.left);        // Left
    dfs(node.right);       // Right
  }

  dfs(root);
  return result;
}
```

### DFS - Postorder (Recursive)
```typescript
function postorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];

  function dfs(node: TreeNode | null): void {
    if (!node) return;

    dfs(node.left);        // Left
    dfs(node.right);       // Right
    result.push(node.val); // Root
  }

  dfs(root);
  return result;
}
```

### DFS - Iterative (using Stack)
```typescript
function inorderIterative(root: TreeNode | null): number[] {
  const result: number[] = [];
  const stack: TreeNode[] = [];
  let current = root;

  while (current || stack.length > 0) {
    // Go to leftmost node
    while (current) {
      stack.push(current);
      current = current.left;
    }

    // Process node
    current = stack.pop()!;
    result.push(current.val);

    // Go to right subtree
    current = current.right;
  }

  return result;
}
```

### BFS - Level Order
```typescript
function levelOrder(root: TreeNode | null): number[][] {
  if (!root) return [];

  const result: number[][] = [];
  const queue: TreeNode[] = [root];

  while (queue.length > 0) {
    const levelSize = queue.length;
    const currentLevel: number[] = [];

    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift()!;
      currentLevel.push(node.val);

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }

    result.push(currentLevel);
  }

  return result;
}
```

### Tree DFS with Path
```typescript
function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
  function dfs(node: TreeNode | null, currentSum: number): boolean {
    if (!node) return false;

    currentSum += node.val;

    // Leaf node - check if path sum equals target
    if (!node.left && !node.right) {
      return currentSum === targetSum;
    }

    // Recurse on children
    return dfs(node.left, currentSum) || dfs(node.right, currentSum);
  }

  return dfs(root, 0);
}
```

---

## Graph Traversals

### Graph Representation
```typescript
// Adjacency list
type Graph = Map<number, number[]>;

function buildGraph(edges: number[][]): Graph {
  const graph = new Map<number, number[]>();

  for (const [u, v] of edges) {
    if (!graph.has(u)) graph.set(u, []);
    if (!graph.has(v)) graph.set(v, []);

    graph.get(u)!.push(v);
    graph.get(v)!.push(u); // Remove for directed graph
  }

  return graph;
}
```

### Graph DFS (Recursive)
```typescript
function dfs(
  node: number,
  graph: Graph,
  visited: Set<number>
): void {
  visited.add(node);
  console.log(node); // Process node

  for (const neighbor of graph.get(node) || []) {
    if (!visited.has(neighbor)) {
      dfs(neighbor, graph, visited);
    }
  }
}

// Usage
const visited = new Set<number>();
dfs(startNode, graph, visited);
```

### Graph DFS (Iterative)
```typescript
function dfsIterative(start: number, graph: Graph): number[] {
  const visited = new Set<number>();
  const stack: number[] = [start];
  const result: number[] = [];

  while (stack.length > 0) {
    const node = stack.pop()!;

    if (visited.has(node)) continue;

    visited.add(node);
    result.push(node);

    // Add neighbors in reverse order for same result as recursive
    const neighbors = graph.get(node) || [];
    for (let i = neighbors.length - 1; i >= 0; i--) {
      if (!visited.has(neighbors[i])) {
        stack.push(neighbors[i]);
      }
    }
  }

  return result;
}
```

### Graph BFS
```typescript
function bfs(start: number, graph: Graph): number[] {
  const visited = new Set<number>();
  const queue: number[] = [start];
  const result: number[] = [];

  visited.add(start);

  while (queue.length > 0) {
    const node = queue.shift()!;
    result.push(node);

    for (const neighbor of graph.get(node) || []) {
      if (!visited.has(neighbor)) {
        visited.add(neighbor);
        queue.push(neighbor);
      }
    }
  }

  return result;
}
```

### Connected Components (DFS)
```typescript
function countComponents(n: number, edges: number[][]): number {
  const graph = buildGraph(edges);
  const visited = new Set<number>();
  let count = 0;

  function dfs(node: number): void {
    visited.add(node);
    for (const neighbor of graph.get(node) || []) {
      if (!visited.has(neighbor)) {
        dfs(neighbor);
      }
    }
  }

  for (let i = 0; i < n; i++) {
    if (!visited.has(i)) {
      dfs(i);
      count++;
    }
  }

  return count;
}
```

### Cycle Detection (Undirected Graph)
```typescript
function hasCycle(graph: Graph): boolean {
  const visited = new Set<number>();

  function dfs(node: number, parent: number): boolean {
    visited.add(node);

    for (const neighbor of graph.get(node) || []) {
      if (!visited.has(neighbor)) {
        if (dfs(neighbor, node)) return true;
      } else if (neighbor !== parent) {
        return true; // Cycle found
      }
    }

    return false;
  }

  for (const node of graph.keys()) {
    if (!visited.has(node)) {
      if (dfs(node, -1)) return true;
    }
  }

  return false;
}
```

---

## Binary Search

### Classic Binary Search
```typescript
function binarySearch(arr: number[], target: number): number {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] === target) {
      return mid;
    } else if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1; // Not found
}
```

### Lower Bound (First element >= target)
```typescript
function lowerBound(arr: number[], target: number): number {
  let left = 0;
  let right = arr.length;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  return left;
}
```

### Upper Bound (First element > target)
```typescript
function upperBound(arr: number[], target: number): number {
  let left = 0;
  let right = arr.length;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] <= target) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  return left;
}
```

### Search in Rotated Sorted Array
```typescript
function search(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (nums[mid] === target) return mid;

    // Left half is sorted
    if (nums[left] <= nums[mid]) {
      if (nums[left] <= target && target < nums[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
    // Right half is sorted
    else {
      if (nums[mid] < target && target <= nums[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }

  return -1;
}
```

---

## Sliding Window

### Fixed Size Window
```typescript
function maxSumSubarray(arr: number[], k: number): number {
  if (arr.length < k) return -1;

  // Calculate sum of first window
  let windowSum = 0;
  for (let i = 0; i < k; i++) {
    windowSum += arr[i];
  }

  let maxSum = windowSum;

  // Slide the window
  for (let i = k; i < arr.length; i++) {
    windowSum = windowSum - arr[i - k] + arr[i];
    maxSum = Math.max(maxSum, windowSum);
  }

  return maxSum;
}
```

### Variable Size Window
```typescript
function lengthOfLongestSubstring(s: string): number {
  const seen = new Set<string>();
  let left = 0;
  let maxLen = 0;

  for (let right = 0; right < s.length; right++) {
    // Shrink window while duplicate exists
    while (seen.has(s[right])) {
      seen.delete(s[left]);
      left++;
    }

    seen.add(s[right]);
    maxLen = Math.max(maxLen, right - left + 1);
  }

  return maxLen;
}
```

### Sliding Window with Frequency Map
```typescript
function minWindow(s: string, t: string): string {
  if (t.length > s.length) return '';

  // Build frequency map for t
  const required = new Map<string, number>();
  for (const char of t) {
    required.set(char, (required.get(char) || 0) + 1);
  }

  let left = 0;
  let right = 0;
  let formed = 0;
  const requiredCount = required.size;

  const windowCounts = new Map<string, number>();
  let result = [Infinity, 0, 0]; // [length, left, right]

  while (right < s.length) {
    // Expand window
    const char = s[right];
    windowCounts.set(char, (windowCounts.get(char) || 0) + 1);

    if (required.has(char) && windowCounts.get(char) === required.get(char)) {
      formed++;
    }

    // Contract window
    while (left <= right && formed === requiredCount) {
      const char = s[left];

      // Update result
      if (right - left + 1 < result[0]) {
        result = [right - left + 1, left, right];
      }

      // Shrink
      windowCounts.set(char, windowCounts.get(char)! - 1);
      if (required.has(char) && windowCounts.get(char)! < required.get(char)!) {
        formed--;
      }

      left++;
    }

    right++;
  }

  return result[0] === Infinity ? '' : s.substring(result[1], result[2] + 1);
}
```

---

## Two Pointers

### Opposite Ends
```typescript
function twoSum(numbers: number[], target: number): number[] {
  let left = 0;
  let right = numbers.length - 1;

  while (left < right) {
    const sum = numbers[left] + numbers[right];

    if (sum === target) {
      return [left, right];
    } else if (sum < target) {
      left++;
    } else {
      right--;
    }
  }

  return [-1, -1];
}
```

### Fast & Slow Pointers (Floyd's Cycle Detection)
```typescript
function hasCycle(head: ListNode | null): boolean {
  if (!head) return false;

  let slow: ListNode | null = head;
  let fast: ListNode | null = head;

  while (fast && fast.next) {
    slow = slow!.next;
    fast = fast.next.next;

    if (slow === fast) {
      return true; // Cycle detected
    }
  }

  return false;
}
```

### Remove Duplicates (Same Direction)
```typescript
function removeDuplicates(nums: number[]): number {
  if (nums.length === 0) return 0;

  let slow = 0;

  for (let fast = 1; fast < nums.length; fast++) {
    if (nums[fast] !== nums[slow]) {
      slow++;
      nums[slow] = nums[fast];
    }
  }

  return slow + 1;
}
```

---

## Dynamic Programming

### 1D DP - Top Down (Memoization)
```typescript
function fib(n: number): number {
  const memo = new Map<number, number>();

  function dp(n: number): number {
    if (n <= 1) return n;
    if (memo.has(n)) return memo.get(n)!;

    const result = dp(n - 1) + dp(n - 2);
    memo.set(n, result);
    return result;
  }

  return dp(n);
}
```

### 1D DP - Bottom Up (Tabulation)
```typescript
function fib(n: number): number {
  if (n <= 1) return n;

  const dp: number[] = new Array(n + 1);
  dp[0] = 0;
  dp[1] = 1;

  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
}
```

### 1D DP - Space Optimized
```typescript
function fib(n: number): number {
  if (n <= 1) return n;

  let prev2 = 0;
  let prev1 = 1;

  for (let i = 2; i <= n; i++) {
    const current = prev1 + prev2;
    prev2 = prev1;
    prev1 = current;
  }

  return prev1;
}
```

### 2D DP - Bottom Up
```typescript
function uniquePaths(m: number, n: number): number {
  // Create 2D DP array
  const dp: number[][] = Array.from(
    {length: m},
    () => new Array(n).fill(1)
  );

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    }
  }

  return dp[m - 1][n - 1];
}
```

### 2D DP - Space Optimized (1D array)
```typescript
function uniquePaths(m: number, n: number): number {
  let dp = new Array(n).fill(1);

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[j] = dp[j] + dp[j - 1];
    }
  }

  return dp[n - 1];
}
```

---

## Backtracking

### Subsets
```typescript
function subsets(nums: number[]): number[][] {
  const result: number[][] = [];

  function backtrack(start: number, path: number[]): void {
    result.push([...path]); // Add current subset

    for (let i = start; i < nums.length; i++) {
      path.push(nums[i]);        // Choose
      backtrack(i + 1, path);    // Explore
      path.pop();                // Unchoose (backtrack)
    }
  }

  backtrack(0, []);
  return result;
}
```

### Permutations
```typescript
function permute(nums: number[]): number[][] {
  const result: number[][] = [];

  function backtrack(path: number[], remaining: number[]): void {
    if (remaining.length === 0) {
      result.push([...path]);
      return;
    }

    for (let i = 0; i < remaining.length; i++) {
      const newPath = [...path, remaining[i]];
      const newRemaining = [...remaining.slice(0, i), ...remaining.slice(i + 1)];
      backtrack(newPath, newRemaining);
    }
  }

  backtrack([], nums);
  return result;
}
```

### Combination Sum
```typescript
function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];

  function backtrack(start: number, path: number[], sum: number): void {
    if (sum === target) {
      result.push([...path]);
      return;
    }

    if (sum > target) return; // Prune

    for (let i = start; i < candidates.length; i++) {
      path.push(candidates[i]);
      backtrack(i, path, sum + candidates[i]); // i not i+1 (can reuse)
      path.pop();
    }
  }

  backtrack(0, [], 0);
  return result;
}
```

---

## Union-Find

### Union-Find (Disjoint Set) Template
```typescript
class UnionFind {
  private parent: number[];
  private rank: number[];

  constructor(size: number) {
    this.parent = Array.from({length: size}, (_, i) => i);
    this.rank = new Array(size).fill(0);
  }

  find(x: number): number {
    // Path compression
    if (this.parent[x] !== x) {
      this.parent[x] = this.find(this.parent[x]);
    }
    return this.parent[x];
  }

  union(x: number, y: number): boolean {
    const rootX = this.find(x);
    const rootY = this.find(y);

    if (rootX === rootY) return false; // Already connected

    // Union by rank
    if (this.rank[rootX] < this.rank[rootY]) {
      this.parent[rootX] = rootY;
    } else if (this.rank[rootX] > this.rank[rootY]) {
      this.parent[rootY] = rootX;
    } else {
      this.parent[rootY] = rootX;
      this.rank[rootX]++;
    }

    return true;
  }

  connected(x: number, y: number): boolean {
    return this.find(x) === this.find(y);
  }
}

// Usage
const uf = new UnionFind(n);
uf.union(0, 1);
uf.union(1, 2);
console.log(uf.connected(0, 2)); // true
```

---

## Helper Functions

### Deep Copy 2D Array
```typescript
function deepCopy<T>(arr: T[][]): T[][] {
  return arr.map(row => [...row]);
}
```

### Generate All Directions
```typescript
// 4 directions (up, right, down, left)
const DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]];

// 8 directions (including diagonals)
const DIRECTIONS_8 = [
  [-1, -1], [-1, 0], [-1, 1],
  [0, -1],           [0, 1],
  [1, -1],  [1, 0],  [1, 1]
];
```

### Check Valid Coordinates
```typescript
function isValid(row: number, col: number, rows: number, cols: number): boolean {
  return row >= 0 && row < rows && col >= 0 && col < cols;
}
```

---

[Back to README](./README.md)
