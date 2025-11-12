# Lesson: Graph BFS

---

## 📹 Video 1: Graph BFS Fundamentals (12 min)

**"Graph BFS Algorithm" by NeetCode**
https://www.youtube.com/watch?v=bTtm2ky7I3Y

**Focus on:**
- Queue-based traversal
- Level-order processing
- Shortest path property
- Visited tracking

---

## 📹 Video 2: Topological Sort (10 min)

**"Topological Sort - Kahn's Algorithm" by NeetCode**
https://www.youtube.com/watch?v=Akt3glAwyfY

**Focus on:**
- In-degree concept
- DAG requirements
- Cycle detection
- BFS-based approach

---

## 📹 Video 3: Alternative Explanations (Optional)

**"BFS Graph Algorithm" by Abdul Bari (15 min)**
https://www.youtube.com/watch?v=pcKY4hjwrYg

**"Topological Sort" by William Fiset (10 min)**
https://www.youtube.com/watch?v=eL-KzMXSXXI

---

## 🎯 BFS Fundamentals

### What is BFS?

Breadth-First Search explores a graph **level by level**, visiting all nodes at distance k before moving to k+1. Like ripples in a pond spreading outward.

**Key Properties:**
- Guarantees shortest path in unweighted graphs
- Uses queue for FIFO processing
- Explores systematically by layers
- Perfect for "minimum steps" problems

---

### Basic BFS Template

```typescript
function bfs(graph: Map<number, number[]>, start: number): void {
    const queue: number[] = [start];
    const visited = new Set<number>([start]);

    while (queue.length > 0) {
        const node = queue.shift()!;

        // Process node
        console.log(node);

        // Visit neighbors
        for (const neighbor of graph.get(node) || []) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);  // Mark BEFORE enqueueing!
                queue.push(neighbor);
            }
        }
    }
}
```

**Time:** O(V + E) | **Space:** O(V)

**Critical:** Mark visited BEFORE adding to queue to prevent duplicates!

---

### BFS with Level Tracking

```typescript
function bfsLevels(graph: Map<number, number[]>, start: number): Map<number, number> {
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

**Use when:** Need distance/depth information.

---

## 🔧 Common BFS Patterns

### Pattern 1: Multi-Source BFS

Start from multiple sources simultaneously - efficient for spreading problems.

```typescript
function multiSourceBFS(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    const queue: [number, number, number][] = [];
    const visited = new Set<string>();

    // Add all sources to queue
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === SOURCE) {
                queue.push([i, j, 0]);
                visited.add(`${i},${j}`);
            }
        }
    }

    const directions = [[0,1], [1,0], [0,-1], [-1,0]];

    while (queue.length > 0) {
        const [row, col, dist] = queue.shift()!;

        for (const [dx, dy] of directions) {
            const newRow = row + dx;
            const newCol = col + dy;
            const key = `${newRow},${newCol}`;

            if (newRow >= 0 && newRow < m &&
                newCol >= 0 && newCol < n &&
                !visited.has(key)) {

                visited.add(key);
                queue.push([newRow, newCol, dist + 1]);
            }
        }
    }

    return dist;
}
```

**Time:** O(m × n) | **Space:** O(m × n)

**Examples:** Rotting Oranges, Walls and Gates, 01 Matrix

---

### Pattern 2: Matrix BFS (4-Directional)

```typescript
const directions = [
    [0, 1],   // right
    [1, 0],   // down
    [0, -1],  // left
    [-1, 0]   // up
];

function matrixBFS(grid: number[][], start: [number, number]): number {
    const [startRow, startCol] = start;
    const queue: [number, number, number][] = [[startRow, startCol, 0]];
    const visited = new Set<string>([`${startRow},${startCol}`]);

    while (queue.length > 0) {
        const [row, col, dist] = queue.shift()!;

        // Check if target
        if (grid[row][col] === TARGET) return dist;

        for (const [dx, dy] of directions) {
            const newRow = row + dx;
            const newCol = col + dy;
            const key = `${newRow},${newCol}`;

            if (newRow >= 0 && newRow < grid.length &&
                newCol >= 0 && newCol < grid[0].length &&
                grid[newRow][newCol] !== WALL &&
                !visited.has(key)) {

                visited.add(key);
                queue.push([newRow, newCol, dist + 1]);
            }
        }
    }

    return -1;
}
```

---

### Pattern 3: 8-Directional BFS

```typescript
const directions = [
    [0, 1], [1, 0], [0, -1], [-1, 0],      // Cardinal
    [1, 1], [1, -1], [-1, 1], [-1, -1]     // Diagonal
];

// Use same structure as 4-directional
```

**Example:** Shortest Path in Binary Matrix

---

## 📊 Topological Sort (Kahn's Algorithm)

### What is Topological Sort?

Linear ordering of vertices in a DAG where for every edge u→v, u comes before v.

**Real-world uses:**
- Course prerequisites
- Build dependencies
- Task scheduling

**Requirements:** Only works on Directed Acyclic Graphs (no cycles!)

---

### Kahn's Algorithm Implementation

```typescript
function topologicalSort(numCourses: number, prerequisites: number[][]): number[] {
    // Build graph and in-degree
    const graph = new Map<number, number[]>();
    const inDegree = new Array(numCourses).fill(0);

    for (const [course, prereq] of prerequisites) {
        if (!graph.has(prereq)) graph.set(prereq, []);
        graph.get(prereq)!.push(course);
        inDegree[course]++;
    }

    // Queue nodes with 0 in-degree
    const queue: number[] = [];
    for (let i = 0; i < numCourses; i++) {
        if (inDegree[i] === 0) queue.push(i);
    }

    const result: number[] = [];

    while (queue.length > 0) {
        const node = queue.shift()!;
        result.push(node);

        // Reduce in-degree of neighbors
        for (const neighbor of graph.get(node) || []) {
            inDegree[neighbor]--;
            if (inDegree[neighbor] === 0) {
                queue.push(neighbor);
            }
        }
    }

    // Check for cycle
    return result.length === numCourses ? result : [];
}
```

**Time:** O(V + E) | **Space:** O(V + E)

**Key insight:** If result.length < numCourses, a cycle exists!

---

## 🚀 Advanced Patterns

### Bidirectional BFS

Search from both start and end, meeting in middle:

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
        // Always expand smaller set
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

**Time:** O(b^(d/2)) instead of O(b^d)

**Use when:** Single source-to-target problem

---

## 💡 BFS vs DFS

### When to Use BFS

| Scenario | Why BFS |
|----------|---------|
| Shortest path (unweighted) | BFS guarantees minimum distance |
| Level-order traversal | Queue processes layer by layer |
| All nodes at distance k | BFS naturally tracks levels |
| Minimum steps/transformations | First path found is shortest |
| Connected components (graph) | Either works, BFS uses more memory |

### When NOT to Use BFS

| Scenario | Use Instead |
|----------|-------------|
| Weighted shortest path | Dijkstra's algorithm |
| All paths enumeration | DFS |
| Deep recursion patterns | DFS |
| Memory constraints | DFS (less memory) |
| Topological sort | Either BFS or DFS |

---

## 🎯 Complexity Reference

| Pattern | Time | Space | Notes |
|---------|------|-------|-------|
| Basic BFS | O(V + E) | O(V) | Visit each node once |
| Matrix BFS | O(m × n) | O(m × n) | All cells |
| Multi-source BFS | O(V + E) | O(V) | Same as basic |
| Bidirectional BFS | O(b^(d/2)) | O(b^(d/2)) | Much faster! |
| Topological Sort | O(V + E) | O(V + E) | Graph + queue |

---

## 💡 Interview Tips

### Communication Points

**Say this:**
- "I'll use BFS because we need shortest path in unweighted graph"
- "Multi-source BFS is more efficient than running BFS from each source"
- "Marking visited before enqueueing prevents duplicates in queue"
- "BFS visits each vertex and edge once, so O(V + E) time"
- "For grids, that's O(m × n) since we visit each cell once"

---

### Problem Recognition

| Keyword | Approach |
|---------|----------|
| "shortest path" | BFS |
| "minimum steps" | BFS |
| "level by level" | BFS |
| "closest/nearest" | Multi-source BFS |
| "spreading" | Multi-source BFS |
| "prerequisites" | Topological Sort |
| "dependencies" | Topological Sort |

---

### Common Mistakes

- Marking visited after dequeue (causes duplicates)
- Using stack instead of queue
- Not handling disconnected graphs
- Forgetting level tracking
- Missing cycle check in topological sort

---

## 📝 Quick Reference

### BFS Template Checklist

```typescript
// Complete BFS template
function bfs(start) {
    const queue = [start];           // 1. Initialize queue
    const visited = new Set([start]); // 2. Initialize visited

    while (queue.length > 0) {        // 3. Process queue
        const node = queue.shift();   // 4. Dequeue

        // Process node here

        for (const neighbor of getNeighbors(node)) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);  // 5. Mark BEFORE enqueue
                queue.push(neighbor);   // 6. Enqueue
            }
        }
    }
}
```

---

### Level-by-Level Processing

```typescript
while (queue.length > 0) {
    const levelSize = queue.length;  // Snapshot current level

    for (let i = 0; i < levelSize; i++) {
        const node = queue.shift();
        // Process node
        // Add neighbors to queue
    }

    level++;  // Move to next level
}
```

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **BFS:** Queue, level-order, shortest path
- **Multi-source:** Start from all sources simultaneously
- **Topological:** Kahn's algorithm, check for cycles
- **Bidirectional:** Search from both ends

---

[Back to Session README](./README.md)
