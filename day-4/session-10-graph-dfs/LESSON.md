# Lesson: Graph DFS (Depth-First Search)

## 📹 Video Assignment (25 minutes)

**Primary Video:**
"Graph Algorithms for Technical Interviews" by NeetCode
https://www.youtube.com/watch?v=tWVWeAqZ0WU

**Alternative Videos** (if you need different explanations):
- "DFS Graph Algorithm" by Back to Back SWE (15 min): https://www.youtube.com/watch?v=7fujbpJ0LB4
- "Graph Data Structure" by CS Dojo (14 min): https://www.youtube.com/watch?v=zaBhtODEL0w

**What to focus on:**
- Graph representations (adjacency list vs matrix)
- DFS traversal pattern
- Visited set usage
- Recursive vs iterative approaches

---

## 📚 Graph DFS - Core Concepts

### What is DFS?

Depth-First Search explores as far as possible along each branch before backtracking. Think of it like exploring a maze by always taking paths to their end before trying alternatives.

**Key insight:** DFS uses a **stack** (implicit with recursion or explicit with iteration) to track the exploration path.

### Graph Representations

```typescript
// 1. Adjacency List (most common)
type Graph = Map<number, number[]>;
const graph = new Map<number, number[]>();
graph.set(0, [1, 2]);
graph.set(1, [0, 3]);

// 2. Adjacency Matrix
const matrix: boolean[][] = [
    [false, true, true, false],  // Node 0 connects to 1, 2
    [true, false, false, true],   // Node 1 connects to 0, 3
];

// 3. Grid as Graph (2D array)
const grid: number[][] = [
    [1, 1, 0],
    [0, 1, 0],
    [1, 0, 1]
];
```

---

### Basic DFS Implementation

#### Recursive DFS

```typescript
function dfsRecursive(
    graph: Map<number, number[]>,
    node: number,
    visited: Set<number> = new Set()
): void {
    // Mark as visited
    visited.add(node);
    console.log(node); // Process node

    // Visit all unvisited neighbors
    const neighbors = graph.get(node) || [];
    for (const neighbor of neighbors) {
        if (!visited.has(neighbor)) {
            dfsRecursive(graph, neighbor, visited);
        }
    }
}
```

#### Iterative DFS

```typescript
function dfsIterative(
    graph: Map<number, number[]>,
    start: number
): void {
    const visited = new Set<number>();
    const stack = [start];

    while (stack.length > 0) {
        const node = stack.pop()!;

        if (visited.has(node)) continue;
        visited.add(node);
        console.log(node); // Process node

        const neighbors = graph.get(node) || [];
        for (const neighbor of neighbors) {
            if (!visited.has(neighbor)) {
                stack.push(neighbor);
            }
        }
    }
}
```

---

## 🎯 Key Patterns

### Pattern 1: Grid Traversal

Used for island problems, flood fill, etc.

```typescript
function exploreGrid(grid: number[][], row: number, col: number): void {
    // Boundary check
    if (row < 0 || row >= grid.length ||
        col < 0 || col >= grid[0].length) {
        return;
    }

    // Check if valid cell
    if (grid[row][col] === 0) return;

    // Mark as visited
    grid[row][col] = 0;

    // Explore 4 directions
    exploreGrid(grid, row + 1, col);  // down
    exploreGrid(grid, row - 1, col);  // up
    exploreGrid(grid, row, col + 1);  // right
    exploreGrid(grid, row, col - 1);  // left
}
```

### Pattern 2: Connected Components

Count separate groups in a graph.

```typescript
function countComponents(n: number, edges: number[][]): number {
    // Build adjacency list
    const graph = new Map<number, number[]>();
    for (let i = 0; i < n; i++) {
        graph.set(i, []);
    }
    for (const [a, b] of edges) {
        graph.get(a)!.push(b);
        graph.get(b)!.push(a);
    }

    const visited = new Set<number>();
    let components = 0;

    // DFS from each unvisited node
    for (let i = 0; i < n; i++) {
        if (!visited.has(i)) {
            dfs(graph, i, visited);
            components++;
        }
    }

    return components;
}
```

### Pattern 3: Cycle Detection

Detect cycles in undirected graphs.

```typescript
function hasCycle(graph: Map<number, number[]>): boolean {
    const visited = new Set<number>();

    function dfs(node: number, parent: number): boolean {
        visited.add(node);

        for (const neighbor of graph.get(node) || []) {
            if (!visited.has(neighbor)) {
                if (dfs(neighbor, node)) return true;
            } else if (neighbor !== parent) {
                return true; // Found cycle
            }
        }
        return false;
    }

    // Check all components
    for (const node of graph.keys()) {
        if (!visited.has(node)) {
            if (dfs(node, -1)) return true;
        }
    }
    return false;
}
```

---

## 🔍 Complexity Analysis

### Time Complexity
- **General DFS:** O(V + E) where V = vertices, E = edges
- **Grid DFS:** O(m × n) where m, n are grid dimensions
- **Complete graph:** O(V²)

### Space Complexity
- **Recursive DFS:** O(V) for call stack + visited set
- **Iterative DFS:** O(V) for explicit stack + visited set
- **Grid problems:** O(m × n) worst case for call stack

---

## 🎨 Visualization

### DFS Traversal Order

```
Graph:     1 --- 2
          / \     \
         3   4     5

DFS from 1: 1 → 3 → 4 → 2 → 5
Stack evolution:
[1] → [3,4,2] → [4,2] → [2] → [5] → []
```

### Grid DFS (Number of Islands)

```
Initial:          After DFS from (0,0):
1 1 0 0 0        0 0 0 0 0
1 1 0 0 0        0 0 0 0 0
0 0 1 0 0        0 0 1 0 0
0 0 0 1 1        0 0 0 1 1

Islands found: 3
```

---

## 💡 When to Use DFS vs BFS

### Use DFS when:
- Exploring all paths
- Finding any valid solution
- Memory is a concern (DFS uses less memory)
- Working with tree/graph traversal
- Detecting cycles

### Use BFS when:
- Finding shortest path (unweighted)
- Level-order traversal
- Finding minimum steps
- Spreading outward uniformly

---

## 🔨 Interview Tips

### 1. Clarifying Questions
- "Is the graph directed or undirected?"
- "Can there be cycles?"
- "Are there disconnected components?"
- "Can I modify the input?"
- "What should I return if graph is empty?"

### 2. Edge Cases
- Empty graph
- Single node
- Disconnected components
- Self-loops
- Duplicate edges

### 3. Optimization Techniques
- **Early termination:** Return as soon as you find the answer
- **Pruning:** Skip paths that can't lead to solution
- **Memoization:** Cache results for repeated subproblems

---

## 📝 Practice Problems by Pattern

### Grid Traversal
1. Number of Islands - Count connected components
2. Max Area of Island - Track size while traversing
3. Flood Fill - Change connected region

### Path Finding
1. Word Search - Find path forming word
2. All Paths Source to Target - Enumerate all paths
3. Pacific Atlantic Water Flow - Multi-source DFS

### Graph Structure
1. Clone Graph - Deep copy with DFS
2. Connected Components - Count separate groups
3. Detect Cycle - Track visited with parent

### Advanced
1. Surrounded Regions - Boundary DFS
2. Course Schedule - Topological sort with DFS

---

## 🎯 Common Pitfalls & Solutions

### Pitfall 1: Infinite Loops
**Problem:** Forgetting visited set causes infinite recursion
**Solution:** Always track visited nodes

### Pitfall 2: Modifying During Iteration
**Problem:** Changing structure while traversing
**Solution:** Collect changes, apply after traversal

### Pitfall 3: Stack Overflow
**Problem:** Deep recursion on large graphs
**Solution:** Use iterative DFS with explicit stack

### Pitfall 4: Wrong Traversal Order
**Problem:** Processing in wrong order for the problem
**Solution:** Understand if order matters for your problem

---

## 📚 Additional Resources

- [Visualgo - Graph Traversal](https://visualgo.net/en/dfsbfs)
- [LeetCode Graph Patterns](https://leetcode.com/discuss/study-guide/1326900/)
- [Graph Algorithm Visualizer](https://www.cs.usfca.edu/~galles/visualization/DFS.html)

---

**Ready for problems?** Start with Number of Islands - the classic DFS grid problem!