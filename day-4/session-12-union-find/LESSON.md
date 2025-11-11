# Union-Find (Disjoint Set Union) - Complete Guide

## Video Resource

📺 **Watch:** [Union Find - NeetCode](https://www.youtube.com/watch?v=8f1XPm4WxGU)

Duration: 30 minutes

**Alternative videos:**
- [Union Find Explained - William Fiset](https://www.youtube.com/watch?v=ibjEGG7ylHk)
- [Disjoint Set Union (DSU) - Abdul Bari](https://www.youtube.com/watch?v=wU6udHRIkcc)

---

## What is Union-Find?

Union-Find (also called Disjoint Set Union or DSU) is a data structure that tracks elements partitioned into disjoint sets. It provides near-constant time operations to:
1. **Unite** two sets
2. **Find** which set an element belongs to

### Real-World Analogy

Think of Union-Find like managing friend groups in a social network:
- Initially, each person is in their own group
- When two people become friends, their groups merge
- To check if two people are connected, find if they're in the same group
- The "leader" of each group represents the entire group

---

## Core Operations

### 1. Find Operation

Determines the root/representative of a set containing element x.

```typescript
class UnionFind {
    parent: number[];

    find(x: number): number {
        // Basic find - follows parent pointers to root
        if (this.parent[x] !== x) {
            return this.find(this.parent[x]);
        }
        return x;
    }
}
```

### 2. Union Operation

Merges two sets containing elements x and y.

```typescript
union(x: number, y: number): void {
    const rootX = this.find(x);
    const rootY = this.find(y);

    if (rootX !== rootY) {
        this.parent[rootX] = rootY;
    }
}
```

### 3. Connected Check

Determines if two elements are in the same set.

```typescript
connected(x: number, y: number): boolean {
    return this.find(x) === this.find(y);
}
```

---

## Optimizations

### 1. Path Compression

During find, make every node point directly to the root.

```typescript
find(x: number): number {
    if (this.parent[x] !== x) {
        // Path compression: point directly to root
        this.parent[x] = this.find(this.parent[x]);
    }
    return this.parent[x];
}
```

**Visualization:**
```
Before:  1 → 2 → 3 → 4 (root)
After:   1 → 4
         2 → 4
         3 → 4
```

### 2. Union by Rank

Always attach the smaller tree under the larger tree.

```typescript
class UnionFind {
    parent: number[];
    rank: number[];

    union(x: number, y: number): void {
        const rootX = this.find(x);
        const rootY = this.find(y);

        if (rootX === rootY) return;

        // Attach smaller tree under larger tree
        if (this.rank[rootX] < this.rank[rootY]) {
            this.parent[rootX] = rootY;
        } else if (this.rank[rootX] > this.rank[rootY]) {
            this.parent[rootY] = rootX;
        } else {
            this.parent[rootY] = rootX;
            this.rank[rootX]++;
        }
    }
}
```

---

## Complete Implementation

### Standard Union-Find Template

```typescript
class UnionFind {
    private parent: number[];
    private rank: number[];
    private components: number;

    constructor(n: number) {
        this.parent = Array(n).fill(0).map((_, i) => i);
        this.rank = Array(n).fill(0);
        this.components = n;
    }

    find(x: number): number {
        if (this.parent[x] !== x) {
            this.parent[x] = this.find(this.parent[x]); // Path compression
        }
        return this.parent[x];
    }

    union(x: number, y: number): boolean {
        const rootX = this.find(x);
        const rootY = this.find(y);

        if (rootX === rootY) {
            return false; // Already connected
        }

        // Union by rank
        if (this.rank[rootX] < this.rank[rootY]) {
            this.parent[rootX] = rootY;
        } else if (this.rank[rootX] > this.rank[rootY]) {
            this.parent[rootY] = rootX;
        } else {
            this.parent[rootY] = rootX;
            this.rank[rootX]++;
        }

        this.components--;
        return true;
    }

    connected(x: number, y: number): boolean {
        return this.find(x) === this.find(y);
    }

    getComponents(): number {
        return this.components;
    }
}
```

---

## Time Complexity Analysis

### Without Optimizations
- Find: O(n) worst case
- Union: O(n) worst case

### With Path Compression Only
- Find: O(log n) amortized
- Union: O(log n) amortized

### With Both Optimizations
- Find: O(α(n)) ≈ O(1) amortized
- Union: O(α(n)) ≈ O(1) amortized

Where α(n) is the inverse Ackermann function, effectively constant for all practical values.

---

## Common Problem Patterns

### 1. Connected Components

Count number of disconnected groups in a graph.

```typescript
function countComponents(n: number, edges: number[][]): number {
    const uf = new UnionFind(n);

    for (const [u, v] of edges) {
        uf.union(u, v);
    }

    return uf.getComponents();
}
```

### 2. Cycle Detection

Detect if adding an edge creates a cycle.

```typescript
function hasCycle(edges: number[][]): boolean {
    const uf = new UnionFind(n);

    for (const [u, v] of edges) {
        if (uf.connected(u, v)) {
            return true; // Cycle detected
        }
        uf.union(u, v);
    }

    return false;
}
```

### 3. Minimum Spanning Tree

Used in Kruskal's algorithm.

```typescript
function kruskalMST(edges: number[][]): number {
    edges.sort((a, b) => a[2] - b[2]); // Sort by weight
    const uf = new UnionFind(n);
    let cost = 0;

    for (const [u, v, weight] of edges) {
        if (uf.union(u, v)) {
            cost += weight;
        }
    }

    return cost;
}
```

---

## When to Use Union-Find

### Use Union-Find when:
- Need to track connected components dynamically
- Detecting cycles in undirected graphs
- Grouping/merging sets of elements
- Checking connectivity between elements
- Problems mention "groups", "components", or "connections"

### Don't use Union-Find when:
- Working with directed graphs (needs modification)
- Need to find actual paths (use BFS/DFS)
- Need to disconnect elements (Union-Find doesn't support split)
- Working with weighted edges for shortest path (use Dijkstra)

---

## Advanced Variations

### 1. Weighted Union-Find

Track additional information per component.

```typescript
class WeightedUnionFind {
    private parent: number[];
    private weight: number[];

    find(x: number): number {
        if (this.parent[x] !== x) {
            const originalParent = this.parent[x];
            this.parent[x] = this.find(originalParent);
            this.weight[x] *= this.weight[originalParent];
        }
        return this.parent[x];
    }
}
```

### 2. Union-Find with Rollback

Support undo operations.

```typescript
class UnionFindWithRollback {
    private history: Array<[number, number, number]>;

    union(x: number, y: number): void {
        // Save state before union
        this.history.push([rootX, this.parent[rootX], this.rank[rootX]]);
        // Perform union...
    }

    rollback(): void {
        const [node, parent, rank] = this.history.pop()!;
        this.parent[node] = parent;
        this.rank[node] = rank;
    }
}
```

---

## Practice Problems by Pattern

### Basic Connectivity (Start here)
1. Number of Provinces (LC 547)
2. Number of Connected Components (LC 323)

### Cycle Detection
3. Graph Valid Tree (LC 261)
4. Redundant Connection (LC 684)

### Advanced Grouping
5. Accounts Merge (LC 721)
6. Smallest String With Swaps (LC 1202)

### Optimization Problems
7. Most Stones Removed (LC 947)
8. Number of Operations to Make Network Connected (LC 1319)

### Special Applications
9. Satisfiability of Equality Equations (LC 990)
10. Evaluate Division (LC 399)

---

## Key Takeaways

1. **Union-Find excels at connectivity** - Use it when you need to check if elements are connected
2. **Always use both optimizations** - Path compression + union by rank
3. **Track component count** - Decrement when union succeeds
4. **Check for existing connection** - Before union to detect cycles
5. **Initialize properly** - Each element starts as its own parent

---

## Interview Tips

### What to Say
- "I'll use Union-Find since we need to track connected components"
- "Let me implement with path compression and union by rank for optimal performance"
- "This gives us near-constant time operations"

### What to Draw
- Show the forest of trees
- Demonstrate path compression
- Illustrate union by rank

### Common Follow-ups
- "What's the time complexity?" → O(α(n)) ≈ O(1) amortized
- "Why not use DFS?" → Union-Find is better for dynamic connectivity
- "Can you disconnect nodes?" → Standard Union-Find doesn't support split

---

## Summary

Union-Find is a powerful data structure for solving connectivity problems. Master the template implementation with both optimizations, and you'll be able to tackle a wide range of graph problems efficiently. The key is recognizing when connectivity queries are the core of the problem.