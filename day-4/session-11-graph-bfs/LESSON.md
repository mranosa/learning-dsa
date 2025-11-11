# Lesson: Graph BFS & Topological Sort

## 📹 Video Assignments (25 minutes)

**Primary Videos:**
1. "Graph Algorithms for Technical Interviews - BFS" by NeetCode
   https://www.youtube.com/watch?v=bTtm2ky7I3Y

2. "Topological Sort - Kahn's Algorithm" by NeetCode
   https://www.youtube.com/watch?v=Akt3glAwyfY

**Alternative Videos** (if you need different explanations):
- "BFS Graph Algorithm" by Abdul Bari (15 min): https://www.youtube.com/watch?v=pcKY4hjwrYg
- "Topological Sort Algorithm" by William Fiset (10 min): https://www.youtube.com/watch?v=eL-KzMXSXXI

**What to focus on:**
- Why BFS uses a queue (FIFO property)
- Level-order traversal concept
- Shortest path in unweighted graphs
- Topological ordering and dependencies

---

## 📚 Graph BFS - Core Concepts

### What is BFS in Graphs?

Breadth-First Search explores a graph level by level, visiting all nodes at distance k before visiting nodes at distance k+1. It's like **ripples in a pond** - spreading outward uniformly.

**Key Properties:**
- Guarantees shortest path in unweighted graphs
- Explores systematically layer by layer
- Uses a queue for node processing order
- Perfect for "minimum steps" problems

### Basic BFS Template

```typescript
function bfs(graph: Map<number, number[]>, start: number): void {
    const queue: number[] = [start];
    const visited = new Set<number>([start]);

    while (queue.length > 0) {
        const node = queue.shift()!;

        // Process current node
        console.log(`Visiting node: ${node}`);

        // Add unvisited neighbors
        for (const neighbor of graph.get(node) || []) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor);
            }
        }
    }
}
```

**Critical:** Mark as visited BEFORE adding to queue to prevent duplicates!

---

### BFS with Level Tracking

Many problems require knowing the distance/level of each node:

```typescript
function bfsWithLevels(graph: Map<number, number[]>, start: number): Map<number, number> {
    const queue: [number, number][] = [[start, 0]];
    const visited = new Set<number>([start]);
    const distances = new Map<number, number>();

    while (queue.length > 0) {
        const [node, level] = queue.shift()!;
        distances.set(node, level);

        for (const neighbor of graph.get(node) || []) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push([neighbor, level + 1]);
            }
        }
    }

    return distances;
}
```

---

### Multi-Source BFS

Start BFS from multiple sources simultaneously - perfect for "spreading" problems:

```typescript
function multiSourceBFS(
    graph: Map<number, number[]>,
    sources: number[]
): Map<number, number> {
    const queue: [number, number][] = [];
    const visited = new Set<number>();
    const distances = new Map<number, number>();

    // Initialize all sources
    for (const source of sources) {
        queue.push([source, 0]);
        visited.add(source);
    }

    while (queue.length > 0) {
        const [node, dist] = queue.shift()!;
        distances.set(node, dist);

        for (const neighbor of graph.get(node) || []) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push([neighbor, dist + 1]);
            }
        }
    }

    return distances;
}
```

**Use cases:** Rotting oranges, multiple fire sources, zombie infection

---

## 🎯 Matrix BFS Patterns

### 4-Directional BFS

```typescript
function matrixBFS(grid: number[][]): number[][] {
    const m = grid.length, n = grid[0].length;
    const distances: number[][] = Array(m).fill(0).map(() => Array(n).fill(-1));
    const queue: [number, number, number][] = [];
    const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];

    // Find starting points (e.g., all 0s)
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 0) {
                queue.push([i, j, 0]);
                distances[i][j] = 0;
            }
        }
    }

    while (queue.length > 0) {
        const [row, col, dist] = queue.shift()!;

        for (const [dx, dy] of directions) {
            const newRow = row + dx;
            const newCol = col + dy;

            if (newRow >= 0 && newRow < m &&
                newCol >= 0 && newCol < n &&
                distances[newRow][newCol] === -1) {

                distances[newRow][newCol] = dist + 1;
                queue.push([newRow, newCol, dist + 1]);
            }
        }
    }

    return distances;
}
```

### 8-Directional BFS

Add diagonal movements:

```typescript
const directions = [
    [0, 1], [1, 0], [0, -1], [-1, 0],  // Cardinal
    [1, 1], [1, -1], [-1, 1], [-1, -1]  // Diagonal
];
```

---

## 📊 Topological Sort (Kahn's Algorithm)

### What is Topological Sort?

A linear ordering of vertices in a Directed Acyclic Graph (DAG) where for every edge u→v, u comes before v in the ordering.

**Real-world examples:**
- Course prerequisites
- Build dependencies
- Task scheduling

### Kahn's Algorithm Implementation

```typescript
function topologicalSort(numCourses: number, prerequisites: number[][]): number[] {
    // Build adjacency list and in-degree count
    const graph = new Map<number, number[]>();
    const inDegree = new Array(numCourses).fill(0);

    for (const [course, prereq] of prerequisites) {
        if (!graph.has(prereq)) graph.set(prereq, []);
        graph.get(prereq)!.push(course);
        inDegree[course]++;
    }

    // Initialize queue with nodes having 0 in-degree
    const queue: number[] = [];
    for (let i = 0; i < numCourses; i++) {
        if (inDegree[i] === 0) {
            queue.push(i);
        }
    }

    const result: number[] = [];

    while (queue.length > 0) {
        const node = queue.shift()!;
        result.push(node);

        // Process neighbors
        for (const neighbor of graph.get(node) || []) {
            inDegree[neighbor]--;
            if (inDegree[neighbor] === 0) {
                queue.push(neighbor);
            }
        }
    }

    // Check for cycles
    return result.length === numCourses ? result : [];
}
```

**Key insight:** If we can't process all nodes, there's a cycle!

---

## 🚀 Advanced Techniques

### Bidirectional BFS

Search from both start and end, meeting in the middle:

```typescript
function bidirectionalBFS(
    graph: Map<string, string[]>,
    start: string,
    end: string
): number {
    if (start === end) return 0;

    let beginSet = new Set([start]);
    let endSet = new Set([end]);
    const visited = new Set<string>();
    let steps = 0;

    while (beginSet.size > 0 && endSet.size > 0) {
        // Always expand the smaller set
        if (beginSet.size > endSet.size) {
            [beginSet, endSet] = [endSet, beginSet];
        }

        const nextSet = new Set<string>();

        for (const word of beginSet) {
            if (endSet.has(word)) return steps;

            for (const neighbor of graph.get(word) || []) {
                if (!visited.has(neighbor)) {
                    visited.add(neighbor);
                    nextSet.add(neighbor);
                }
            }
        }

        beginSet = nextSet;
        steps++;
    }

    return -1;
}
```

**Optimization:** Reduces search space from O(b^d) to O(b^(d/2))

---

## 💡 Problem-Solving Strategies

### When to Use BFS

Choose BFS when you need:
- ✅ Shortest path in unweighted graph
- ✅ Level-order traversal
- ✅ All nodes at distance k
- ✅ Minimum steps/transformations
- ✅ Process by layers/levels

### When NOT to Use BFS

Avoid BFS for:
- ❌ Weighted shortest paths (use Dijkstra)
- ❌ All paths enumeration (use DFS)
- ❌ Deep recursion patterns (use DFS)
- ❌ Memory-constrained problems (BFS uses more memory)

---

## 🎯 Interview Tips

### Communication Points

1. **Clarify the graph type:**
   - "Is this directed or undirected?"
   - "Can there be cycles?"
   - "Are edges weighted?"

2. **Discuss complexity:**
   - "BFS visits each node and edge once: O(V + E)"
   - "Space complexity is O(V) for the queue and visited set"

3. **Handle edge cases:**
   - Empty graph
   - Disconnected components
   - Single node
   - No valid path

### Common Follow-ups

- "Can you optimize this?" → Consider bidirectional BFS
- "What if edges have weights?" → Switch to Dijkstra's algorithm
- "How to find the actual path?" → Track parent pointers
- "What about negative weights?" → Need Bellman-Ford

---

## 📝 Quick Reference

### BFS vs DFS Comparison

| Aspect | BFS | DFS |
|--------|-----|-----|
| Data Structure | Queue | Stack/Recursion |
| Space | O(width) | O(height) |
| Shortest Path | ✅ Yes (unweighted) | ❌ No |
| Complete | ✅ Yes | ❌ Can get stuck |
| Use Case | Level-order, shortest path | All paths, backtracking |

### Complexity Cheat Sheet

| Pattern | Time | Space |
|---------|------|-------|
| Basic BFS | O(V + E) | O(V) |
| Matrix BFS | O(m × n) | O(m × n) |
| Multi-source BFS | O(V + E) | O(V) |
| Bidirectional BFS | O(b^(d/2)) | O(b^(d/2)) |
| Topological Sort | O(V + E) | O(V) |

---

**Ready to solve problems?** Check PROBLEMS.md for today's challenges!