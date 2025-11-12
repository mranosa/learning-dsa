# Lesson: Graph DFS (Depth-First Search)

---

## 📹 Video 1: Graph Fundamentals (15 min)

**"Graph Data Structure & Algorithms #1" by WilliamFiset**
https://www.youtube.com/watch?v=tWVWeAqZ0WU

**Alternative:** "Graphs for Beginners" by CS Dojo
https://www.youtube.com/watch?v=gXgEDyodOJU

**Focus on:**
- Graph representations (adjacency list vs matrix)
- Graph terminology (vertices, edges, directed/undirected)
- When to use graphs vs trees
- TypeScript graph structures

---

## 📹 Video 2: DFS Algorithm & Patterns (20 min)

**"Graph Algorithms for Technical Interviews" by NeetCode**
https://www.youtube.com/watch?v=tWVWeAqZ0WU

**Alternative:** "DFS Algorithm Explained" by Back to Back SWE
https://www.youtube.com/watch?v=7fujbpJ0LB4

**Focus on:**
- DFS traversal order (depth-first vs breadth-first)
- Recursive vs iterative implementation
- Visited set pattern
- Time/space complexity analysis

---

## 📹 Video 3: Grid Traversal Techniques (12 min)

**"Number of Islands - DFS - Leetcode 200" by NeetCode**
https://www.youtube.com/watch?v=pV2kpPD66nE

**Alternative:** "Graph DFS Patterns" by Kevin Naughton Jr
https://www.youtube.com/watch?v=W9F8fDQj7Ok

**Focus on:**
- Grid as implicit graph
- 4-directional traversal pattern
- Boundary checking
- Marking visited cells

---

## 🎯 Graph Representations

### What is a Graph?

A graph is a data structure consisting of:
- **Vertices (nodes):** The entities
- **Edges:** Connections between vertices

**Types:**
- **Directed:** Edges have direction (A → B)
- **Undirected:** Edges are bidirectional (A ↔ B)
- **Weighted:** Edges have values
- **Unweighted:** All edges equal

---

### Representation 1: Adjacency List

Most common and efficient for sparse graphs.

```typescript
// Using Map (most flexible)
type Graph = Map<number, number[]>;

const graph = new Map<number, number[]>();
graph.set(0, [1, 2]);
graph.set(1, [0, 3]);
graph.set(2, [0, 3]);
graph.set(3, [1, 2]);

// Using array (when nodes are 0 to n-1)
const graphArray: number[][] = [
    [1, 2],    // Node 0 connects to 1, 2
    [0, 3],    // Node 1 connects to 0, 3
    [0, 3],    // Node 2 connects to 0, 3
    [1, 2]     // Node 3 connects to 1, 2
];

// Building from edge list
function buildGraph(n: number, edges: number[][]): Map<number, number[]> {
    const graph = new Map<number, number[]>();

    // Initialize all nodes
    for (let i = 0; i < n; i++) {
        graph.set(i, []);
    }

    // Add edges (undirected)
    for (const [a, b] of edges) {
        graph.get(a)!.push(b);
        graph.get(b)!.push(a); // Remove for directed
    }

    return graph;
}
```

**Time:** O(1) to add edge, O(V + E) space
**Best for:** Sparse graphs, most interview problems

---

### Representation 2: Adjacency Matrix

2D array where matrix[i][j] indicates edge from i to j.

```typescript
// Boolean matrix
const matrix: boolean[][] = [
    [false, true, true, false],  // Node 0 → 1, 2
    [true, false, false, true],   // Node 1 → 0, 3
    [true, false, false, true],   // Node 2 → 0, 3
    [false, true, true, false]    // Node 3 → 1, 2
];

// Weighted matrix
const weighted: number[][] = [
    [0, 5, 3, 0],    // Distance from 0
    [5, 0, 0, 7],    // Distance from 1
    [3, 0, 0, 2],    // Distance from 2
    [0, 7, 2, 0]     // Distance from 3
];

// Building from edges
function buildMatrix(n: number, edges: number[][]): boolean[][] {
    const matrix: boolean[][] = Array(n).fill(null)
        .map(() => Array(n).fill(false));

    for (const [a, b] of edges) {
        matrix[a][b] = true;
        matrix[b][a] = true; // Undirected
    }

    return matrix;
}
```

**Time:** O(1) to check edge, O(V²) space
**Best for:** Dense graphs, quick edge lookup

---

### Representation 3: Grid as Graph

2D array where cells are nodes, edges are implicit.

```typescript
// Grid (each cell is a node)
const grid: number[][] = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
];

// 4-directional neighbors
const directions = [
    [0, 1],   // right
    [1, 0],   // down
    [0, -1],  // left
    [-1, 0]   // up
];

// 8-directional (includes diagonals)
const directions8 = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1],           [0, 1],
    [1, -1],  [1, 0],  [1, 1]
];

// Check if cell is valid
function isValid(grid: number[][], row: number, col: number): boolean {
    return row >= 0 && row < grid.length &&
           col >= 0 && col < grid[0].length;
}
```

**Best for:** Grid-based problems (islands, paths, etc)

---

## 🚀 DFS Algorithm

### What is DFS?

Depth-First Search explores as far as possible along each branch before backtracking.

**Key insight:** Uses a **stack** (recursive call stack or explicit stack).

**DFS Order:** Go deep before going wide.
```
    1
   / \
  2   3
 / \
4   5

DFS: 1 → 2 → 4 → 5 → 3
```

---

### Recursive DFS (Most Common)

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

// Usage
const graph = new Map<number, number[]>([
    [0, [1, 2]],
    [1, [0, 3]],
    [2, [0, 3]],
    [3, [1, 2]]
]);
dfsRecursive(graph, 0);
```

**Time:** O(V + E) | **Space:** O(V) for visited + O(V) call stack

---

### Iterative DFS

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

        // Add neighbors to stack
        const neighbors = graph.get(node) || [];
        for (const neighbor of neighbors) {
            if (!visited.has(neighbor)) {
                stack.push(neighbor);
            }
        }
    }
}
```

**Time:** O(V + E) | **Space:** O(V)

**When to use:** Deep graphs (avoid stack overflow), need specific order.

---

## 🧩 Common DFS Patterns

### Pattern 1: Grid Traversal (4-directional)

Used for: Number of Islands, Flood Fill, Max Area

```typescript
function dfsGrid(grid: number[][], row: number, col: number): void {
    // Boundary check
    if (row < 0 || row >= grid.length ||
        col < 0 || col >= grid[0].length) {
        return;
    }

    // Check if valid cell (water or visited)
    if (grid[row][col] === 0) return;

    // Mark as visited
    grid[row][col] = 0;

    // Explore 4 directions
    dfsGrid(grid, row + 1, col);  // down
    dfsGrid(grid, row - 1, col);  // up
    dfsGrid(grid, row, col + 1);  // right
    dfsGrid(grid, row, col - 1);  // left
}

// Count islands
function numIslands(grid: string[][]): number {
    let count = 0;

    for (let row = 0; row < grid.length; row++) {
        for (let col = 0; col < grid[0].length; col++) {
            if (grid[row][col] === '1') {
                dfsGrid(grid, row, col);
                count++;
            }
        }
    }

    return count;
}
```

**Key points:**
- Check boundaries first
- Mark visited (modify grid or use Set)
- Explore all 4 directions

---

### Pattern 2: Connected Components

Used for: Count components, find groups

```typescript
function countComponents(n: number, edges: number[][]): number {
    // Build graph
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

    function dfs(node: number): void {
        visited.add(node);
        for (const neighbor of graph.get(node)!) {
            if (!visited.has(neighbor)) {
                dfs(neighbor);
            }
        }
    }

    // Start DFS from each unvisited node
    for (let i = 0; i < n; i++) {
        if (!visited.has(i)) {
            dfs(i);
            components++;
        }
    }

    return components;
}
```

**Pattern:** DFS from each unvisited node, increment counter.

---

### Pattern 3: Cycle Detection

Used for: Validate tree, dependency checking

```typescript
function hasCycle(n: number, edges: number[][]): boolean {
    // Build graph
    const graph = new Map<number, number[]>();
    for (let i = 0; i < n; i++) {
        graph.set(i, []);
    }
    for (const [a, b] of edges) {
        graph.get(a)!.push(b);
        graph.get(b)!.push(a);
    }

    const visited = new Set<number>();

    function dfs(node: number, parent: number): boolean {
        visited.add(node);

        for (const neighbor of graph.get(node)!) {
            if (!visited.has(neighbor)) {
                if (dfs(neighbor, node)) return true;
            } else if (neighbor !== parent) {
                return true; // Found cycle
            }
        }
        return false;
    }

    // Check all components
    for (let i = 0; i < n; i++) {
        if (!visited.has(i)) {
            if (dfs(i, -1)) return true;
        }
    }
    return false;
}
```

**Key insight:** If visiting a node that's already visited and it's NOT the parent, found cycle.

---

### Pattern 4: Path Finding

Used for: All paths, find path

```typescript
function allPathsSourceTarget(graph: number[][]): number[][] {
    const result: number[][] = [];
    const target = graph.length - 1;

    function dfs(node: number, path: number[]): void {
        path.push(node);

        // Reached target
        if (node === target) {
            result.push([...path]); // Copy path
        } else {
            // Explore neighbors
            for (const neighbor of graph[node]) {
                dfs(neighbor, path);
            }
        }

        path.pop(); // Backtrack
    }

    dfs(0, []);
    return result;
}
```

**Key points:**
- Track current path
- Copy path when adding to result
- Backtrack after exploring

---

## 📊 Complexity Analysis

### Time Complexity

| Operation | Adjacency List | Adjacency Matrix | Grid |
|-----------|---------------|------------------|------|
| DFS Traversal | O(V + E) | O(V²) | O(m × n) |
| Add Edge | O(1) | O(1) | N/A |
| Check Edge | O(E/V) avg | O(1) | O(1) |
| Space | O(V + E) | O(V²) | O(m × n) |

**Where:**
- V = number of vertices (nodes)
- E = number of edges
- m × n = grid dimensions

---

### Space Complexity

**Recursive DFS:**
- Visited set: O(V)
- Call stack: O(V) worst case (linear graph)
- Total: O(V)

**Iterative DFS:**
- Visited set: O(V)
- Explicit stack: O(V)
- Total: O(V)

**Grid DFS:**
- Call stack: O(m × n) worst case (all cells connected)
- If modifying grid in-place: O(1) extra space
- If using visited set: O(m × n)

---

## 💡 DFS vs BFS

### Use DFS when:
- Finding ANY valid path
- Exploring all paths
- Detecting cycles
- Topological sort
- Connected components
- Tree traversal (pre/in/post-order)
- Memory constrained (DFS uses less memory)

### Use BFS when:
- Finding SHORTEST path (unweighted)
- Level-order traversal
- Minimum steps/distance
- Closest/nearest problems
- Need to explore by layers

---

## 🔨 Interview Tips

### Clarifying Questions

Always ask:
- "Is the graph directed or undirected?"
- "Can there be self-loops or multiple edges?"
- "Are there disconnected components?"
- "Can I modify the input?"
- "What should I return for empty graph?"

---

### Edge Cases

Test these:
```typescript
// Empty graph
graph = new Map()

// Single node
graph = new Map([[0, []]])

// Disconnected components
graph = new Map([
    [0, [1]],
    [1, [0]],
    [2, [3]],
    [3, [2]]
])

// Self-loop
graph = new Map([[0, [0]]])

// No edges
graph = new Map([[0, []], [1, []], [2, []]])
```

---

### Common Mistakes & Fixes

**Mistake 1: Forgetting visited set**
```typescript
// ❌ Wrong - infinite loop
function dfs(node: number) {
    for (const neighbor of graph.get(node)!) {
        dfs(neighbor); // Revisits nodes!
    }
}

// ✅ Correct
function dfs(node: number, visited: Set<number>) {
    visited.add(node);
    for (const neighbor of graph.get(node)!) {
        if (!visited.has(neighbor)) {
            dfs(neighbor, visited);
        }
    }
}
```

**Mistake 2: Modifying while iterating**
```typescript
// ❌ Wrong
for (const [node, neighbors] of graph) {
    graph.set(node, []); // Don't modify during iteration
}

// ✅ Correct
const toUpdate = [];
for (const [node, neighbors] of graph) {
    toUpdate.push(node);
}
for (const node of toUpdate) {
    graph.set(node, []);
}
```

**Mistake 3: Grid boundary errors**
```typescript
// ❌ Wrong - index out of bounds
function dfs(grid: number[][], row: number, col: number) {
    grid[row][col] = 0; // Crashes if out of bounds
    dfs(grid, row + 1, col);
}

// ✅ Correct
function dfs(grid: number[][], row: number, col: number) {
    if (row < 0 || row >= grid.length ||
        col < 0 || col >= grid[0].length) {
        return;
    }
    if (grid[row][col] === 0) return;
    grid[row][col] = 0;
    dfs(grid, row + 1, col);
}
```

---

## 🎯 TypeScript-Specific Tips

### Type Definitions

```typescript
// Graph with number nodes
type Graph = Map<number, number[]>;

// Weighted graph
type WeightedGraph = Map<number, [number, number][]>; // [neighbor, weight]

// String nodes
type StringGraph = Map<string, string[]>;

// Grid cell
type Cell = [number, number];
```

### Null Safety

```typescript
// ❌ Might crash
const neighbors = graph.get(node);
for (const n of neighbors) { ... } // neighbors might be undefined

// ✅ Safe
const neighbors = graph.get(node) || [];
for (const n of neighbors) { ... }

// ✅ Also safe
const neighbors = graph.get(node);
if (neighbors) {
    for (const n of neighbors) { ... }
}
```

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **DFS:** Stack (recursive or explicit)
- **Time:** O(V + E) for graphs, O(m × n) for grids
- **Space:** O(V) for visited set + stack
- **Pattern:** Visited set, explore deep, backtrack

**Grid Template:**
```typescript
function dfs(grid: number[][], row: number, col: number) {
    if (row < 0 || row >= grid.length ||
        col < 0 || col >= grid[0].length ||
        grid[row][col] === 0) return;

    grid[row][col] = 0;
    dfs(grid, row + 1, col);
    dfs(grid, row - 1, col);
    dfs(grid, row, col + 1);
    dfs(grid, row, col - 1);
}
```

---

[Back to Session README](./README.md)
