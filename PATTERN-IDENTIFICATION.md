# Pattern Identification Guide

Master pattern recognition to solve problems in <2 minutes.

---

## Quick Decision Tree

```
START: Read problem statement
         ↓
    What's the input type?
    ┌─────┴─────┬─────────┬─────────┐
    │           │         │         │
  ARRAY      STRING    TREE      GRAPH
    │           │         │         │
    ↓           ↓         ↓         ↓
```

---

## ARRAY / STRING Patterns

### 🎯 Two Pointers
**Keywords:**
- "Find pair that sums to..."
- "Remove duplicates in-place"
- "Reverse"
- "Palindrome"
- "Sorted array"

**When to use:**
- Sorted array + searching
- Need to compare elements from both ends
- In-place requirement (O(1) space)
- Looking for pairs/triplets

**Examples:**
- Two Sum II (sorted)
- Container With Most Water
- Valid Palindrome
- Remove Duplicates from Sorted Array

**Time:** O(n) | **Space:** O(1)

---

### 🪟 Sliding Window
**Keywords:**
- "Subarray" or "substring"
- "Contiguous"
- "k consecutive elements"
- "Maximum/minimum in window"
- "Longest/shortest satisfying condition"

**When to use:**
- Need to track a continuous portion of array
- Looking for optimum in all subarrays of size k
- "Longest substring with..."
- "Maximum sum subarray of size k"

**Types:**
- **Fixed size:** Window size given (k elements)
- **Variable size:** Find optimal window size

**Examples:**
- Maximum Sum Subarray of Size K (fixed)
- Longest Substring Without Repeating Characters (variable)
- Minimum Window Substring (variable)

**Time:** O(n) | **Space:** O(1) or O(k)

---

### 📊 Prefix Sum
**Keywords:**
- "Range sum query"
- "Subarray sum equals k"
- "Sum between indices i and j"
- Multiple sum queries

**When to use:**
- Multiple range queries on same array
- Need to calculate subarray sums quickly
- Array doesn't change between queries

**Formula:**
```
prefixSum[i] = sum of elements from 0 to i
rangeSum(i, j) = prefixSum[j] - prefixSum[i-1]
```

**Examples:**
- Range Sum Query
- Subarray Sum Equals K
- Product of Array Except Self

**Time:** O(n) build, O(1) query | **Space:** O(n)

---

### 🗺️ Hash Map / Hash Set
**Keywords:**
- "Find pair/duplicate/anagram"
- "Frequency count"
- "Check if exists"
- "Group by..."
- "Count occurrences"

**When to use:**
- Need O(1) lookup
- Counting frequencies
- Checking existence
- Grouping elements
- Finding complements

**Map vs Set:**
- **Map:** Need to store key-value pairs (value→index, char→count)
- **Set:** Only need to check existence (no duplicate tracking)

**Examples:**
- Two Sum (unsorted)
- Contains Duplicate
- Valid Anagram
- Group Anagrams
- First Unique Character

**Time:** O(n) | **Space:** O(n)

---

### 🔍 Binary Search
**Keywords:**
- "Sorted array"
- "Find target"
- "First/last occurrence"
- "Find minimum/maximum"
- "Rotated sorted array"
- "Search in range"

**When to use:**
- Array is sorted (or rotated sorted)
- Need O(log n) time
- Searching for specific value
- Finding boundaries (first/last)

**Variations:**
- Classic: Find exact value
- Lower bound: First element >= target
- Upper bound: First element > target
- Rotated array: Special pivot handling

**Examples:**
- Binary Search
- Search in Rotated Sorted Array
- Find First and Last Position
- Find Peak Element

**Time:** O(log n) | **Space:** O(1)

---

## LINKED LIST Patterns

### 🐢🐇 Fast & Slow Pointers (Floyd's)
**Keywords:**
- "Detect cycle"
- "Find middle"
- "Nth node from end"
- "Palindrome linked list"

**When to use:**
- Cycle detection
- Finding middle element
- Detecting start of cycle
- Two-speed traversal needed

**Technique:**
```
slow moves 1 step
fast moves 2 steps
If fast catches slow → cycle exists
When fast reaches end → slow at middle
```

**Examples:**
- Linked List Cycle
- Find Duplicate Number (cycle detection on array)
- Middle of Linked List
- Palindrome Linked List

**Time:** O(n) | **Space:** O(1)

---

## TREE Patterns

### 🌲 Tree DFS (Depth-First Search)
**Keywords:**
- "Path from root to leaf"
- "All paths"
- "Tree depth/height"
- "Validate tree"
- "Lowest common ancestor"

**When to use:**
- Exploring all paths
- Need to go deep first
- Calculating depth/height
- Comparing subtrees
- Working with paths

**Traversals:**
- **Inorder:** Left → Root → Right (BST: sorted order)
- **Preorder:** Root → Left → Right (copying tree)
- **Postorder:** Left → Right → Root (deleting tree)

**Examples:**
- Maximum Depth of Binary Tree
- Path Sum
- Validate Binary Search Tree
- Lowest Common Ancestor
- Diameter of Binary Tree

**Time:** O(n) | **Space:** O(h) where h = height

---

### 📏 Tree BFS (Breadth-First Search)
**Keywords:**
- "Level-order traversal"
- "Level by level"
- "Minimum depth"
- "Zigzag traversal"
- "Right side view"

**When to use:**
- Process nodes level by level
- Shortest path in tree
- Level-related problems
- Need to track levels

**Technique:**
```
Use queue
Process level by level
Track level count
```

**Examples:**
- Binary Tree Level Order Traversal
- Minimum Depth of Binary Tree
- Binary Tree Right Side View
- Zigzag Level Order Traversal

**Time:** O(n) | **Space:** O(w) where w = max width

---

### 🔢 Binary Search Tree (BST)
**Keywords:**
- "Binary search tree"
- "Kth smallest/largest"
- "Validate BST"
- "In sorted order"

**When to use:**
- Tree has BST property (left < root < right)
- Need sorted order (inorder traversal)
- Searching in tree
- Finding kth element

**BST Property:**
```
All left subtree values < root
All right subtree values > root
Both subtrees are BSTs
```

**Examples:**
- Validate Binary Search Tree
- Kth Smallest Element in BST
- Lowest Common Ancestor of BST
- Serialize and Deserialize BST

**Time:** O(log n) average, O(n) worst | **Space:** O(h)

---

## GRAPH Patterns

### 🗺️ Graph DFS
**Keywords:**
- "Connected components"
- "Find all paths"
- "Cycle detection"
- "Topological sort"
- "Flood fill"

**When to use:**
- Exploring all reachable nodes
- Finding connected components
- Detecting cycles
- Path existence
- Maze solving

**Technique:**
```
Mark visited
Explore neighbors recursively
Backtrack when needed
```

**Examples:**
- Number of Islands
- Clone Graph
- Pacific Atlantic Water Flow
- Course Schedule (DFS version)

**Time:** O(V + E) | **Space:** O(V)

---

### 🎯 Graph BFS
**Keywords:**
- "Shortest path"
- "Minimum steps"
- "Level by level"
- "Distance from source"

**When to use:**
- Shortest path (unweighted graph)
- Level-based exploration
- Minimum distance
- All nodes at distance k

**Technique:**
```
Use queue
Process level by level
Track distance/level
Mark visited
```

**Examples:**
- Word Ladder
- Shortest Path in Binary Matrix
- Rotting Oranges
- Course Schedule (BFS version)

**Time:** O(V + E) | **Space:** O(V)

---

### 🔗 Union-Find (Disjoint Set)
**Keywords:**
- "Connected components"
- "Dynamic connectivity"
- "Detect cycle in undirected graph"
- "Minimum spanning tree"

**When to use:**
- Dynamic connectivity queries
- Grouping elements into sets
- Cycle detection in undirected graphs
- Network connectivity

**Operations:**
```
find(x): Find set containing x
union(x, y): Merge sets containing x and y
```

**Examples:**
- Number of Connected Components
- Graph Valid Tree
- Redundant Connection
- Accounts Merge

**Time:** O(α(n)) ≈ O(1) with path compression | **Space:** O(n)

---

## DYNAMIC PROGRAMMING Patterns

### 📈 1D DP
**Keywords:**
- "Maximum/minimum"
- "Count ways"
- "Optimize"
- "Fibonacci-like"
- "House robber"

**When to use:**
- Optimization problem
- Current decision depends on previous decisions
- Can be expressed as: `dp[i] = f(dp[i-1], dp[i-2], ...)`

**Examples:**
- Climbing Stairs
- House Robber
- Decode Ways
- Coin Change (1D)
- Longest Increasing Subsequence

**Time:** O(n) | **Space:** O(n) → O(1) with optimization

---

### 📊 2D DP
**Keywords:**
- "Grid"
- "Two sequences"
- "Longest common subsequence"
- "Edit distance"
- "Unique paths"

**When to use:**
- Two sequences to compare
- Grid traversal with constraints
- `dp[i][j]` depends on neighbors
- Two dimensions of choice

**Examples:**
- Unique Paths
- Longest Common Subsequence
- Edit Distance
- Coin Change (2D unbounded)
- Regular Expression Matching

**Time:** O(n×m) | **Space:** O(n×m) → O(min(n,m)) with optimization

---

### 🎒 Knapsack
**Keywords:**
- "Subset sum"
- "Target sum"
- "Partition"
- "Capacity constraint"

**Types:**
- **0/1 Knapsack:** Each item used once or not at all
- **Unbounded:** Can use items multiple times
- **Bounded:** Limited quantity of each item

**When to use:**
- Selecting items with constraint
- Target sum problems
- Subset selection

**Examples:**
- Partition Equal Subset Sum
- Target Sum
- Coin Change (unbounded knapsack)
- Ones and Zeroes

**Time:** O(n×capacity) | **Space:** O(n×capacity) → O(capacity)

---

## BACKTRACKING Patterns

### 🔄 Backtracking
**Keywords:**
- "All combinations"
- "All permutations"
- "Generate all"
- "All subsets"
- "N-Queens"
- "Sudoku"

**When to use:**
- Generate all possible solutions
- Explore all paths
- Constraint satisfaction
- Decision tree exploration

**Template:**
```typescript
function backtrack(path, choices) {
  if (isComplete(path)) {
    results.push([...path]);
    return;
  }

  for (const choice of choices) {
    // Make choice
    path.push(choice);

    // Explore
    backtrack(path, newChoices);

    // Undo choice (backtrack)
    path.pop();
  }
}
```

**Examples:**
- Subsets
- Permutations
- Combination Sum
- N-Queens
- Sudoku Solver

**Time:** O(2^n) or O(n!) | **Space:** O(n) recursion depth

---

## HEAP / PRIORITY QUEUE Patterns

### ⛰️ Heap
**Keywords:**
- "Top K elements"
- "Kth largest/smallest"
- "Merge K sorted"
- "Find median"

**When to use:**
- Need to maintain top K elements
- Finding kth largest/smallest
- Merging sorted lists
- Dynamic min/max queries

**Types:**
- **Min Heap:** Root is minimum
- **Max Heap:** Root is maximum

**Examples:**
- Kth Largest Element
- Top K Frequent Elements
- Merge K Sorted Lists
- Find Median from Data Stream

**Time:** O(log n) insert/delete, O(1) peek | **Space:** O(n)

---

## SPECIAL Patterns

### 🔤 Trie (Prefix Tree)
**Keywords:**
- "Prefix"
- "Dictionary"
- "Word search"
- "Autocomplete"

**When to use:**
- Prefix-based search
- Dictionary operations
- Word validation
- Autocomplete features

**Examples:**
- Implement Trie
- Word Search II
- Design Add and Search Words Data Structure

**Time:** O(m) where m = word length | **Space:** O(n×m)

---

### 🎲 Bit Manipulation
**Keywords:**
- "XOR"
- "Single number"
- "Counting bits"
- "Power of two"
- "Missing number"

**When to use:**
- Need O(1) space solution
- XOR properties useful
- Working with binary representations
- Optimization tricks

**Common Tricks:**
```
x ^ x = 0 (XOR same number = 0)
x ^ 0 = x (XOR with 0 = itself)
x & (x-1) removes rightmost 1 bit
x & -x isolates rightmost 1 bit
```

**Examples:**
- Single Number
- Number of 1 Bits
- Counting Bits
- Missing Number

**Time:** O(1) or O(n) | **Space:** O(1)

---

### 📅 Intervals
**Keywords:**
- "Merge intervals"
- "Meeting rooms"
- "Insert interval"
- "Non-overlapping"

**When to use:**
- Working with ranges/intervals
- Overlap detection
- Scheduling problems

**Technique:**
```
1. Sort intervals by start time
2. Iterate and merge/process
3. Track current interval
```

**Examples:**
- Merge Intervals
- Meeting Rooms
- Insert Interval
- Non-overlapping Intervals

**Time:** O(n log n) for sorting | **Space:** O(n)

---

## Pattern Recognition Practice

### Problem: "Find the longest substring without repeating characters"
**Analysis:**
- "substring" → contiguous → Sliding Window
- "without repeating" → track seen characters → Hash Set
- "longest" → optimize window size → Variable Sliding Window

**Answer:** Variable Sliding Window + Hash Set

---

### Problem: "Given a sorted array, find two numbers that sum to target"
**Analysis:**
- "sorted array" → Binary Search or Two Pointers
- "two numbers sum" → Two Pointers is optimal
- "find pair" → Two Pointers (opposite ends)

**Answer:** Two Pointers

---

### Problem: "Find all paths from root to leaf in a binary tree"
**Analysis:**
- "all paths" → explore all options → DFS
- "root to leaf" → tree traversal → Tree DFS
- Need to track path → Backtracking

**Answer:** Tree DFS with Backtracking

---

### Problem: "Find kth largest element in unsorted array"
**Analysis:**
- "kth largest" → top K problem → Heap
- "unsorted" → can't use binary search
- "single element" → Min Heap of size k

**Answer:** Min Heap (or QuickSelect for O(n) average)

---

## Quick Reference Table

| Problem Type | Pattern | Time | Space |
|-------------|---------|------|-------|
| Find pair in sorted array | Two Pointers | O(n) | O(1) |
| Find pair in unsorted array | Hash Map | O(n) | O(n) |
| Longest substring with K chars | Sliding Window | O(n) | O(k) |
| Range sum queries | Prefix Sum | O(1) query | O(n) |
| Search in sorted array | Binary Search | O(log n) | O(1) |
| Cycle detection | Fast & Slow Pointers | O(n) | O(1) |
| Tree paths | Tree DFS | O(n) | O(h) |
| Level-order | Tree BFS | O(n) | O(w) |
| Shortest path (unweighted) | Graph BFS | O(V+E) | O(V) |
| Connected components | DFS or Union-Find | O(V+E) | O(V) |
| Optimize over choices | Dynamic Programming | O(n²) typ | O(n²) |
| All combinations | Backtracking | O(2^n) | O(n) |
| Top K elements | Heap | O(n log k) | O(k) |
| Prefix search | Trie | O(m) | O(n×m) |

---

## Pro Tips

1. **Read the problem twice** - keywords matter!
2. **Look for these signals:**
   - "Sorted" → Binary Search or Two Pointers
   - "Subarray/Substring" → Sliding Window or Prefix Sum
   - "All combinations" → Backtracking
   - "Shortest/Minimum" → BFS or DP
   - "Maximum/Optimize" → DP or Greedy

3. **When stuck:** Think about what data structure gives you the operation you need most frequently in O(1) or O(log n)

4. **Multiple patterns:** Some problems combine patterns (e.g., Sliding Window + Hash Map)

---

[Back to README](./README.md)
