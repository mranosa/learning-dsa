# Union-Find - Study Notes

## Core Template

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
            this.parent[x] = this.find(this.parent[x]);
        }
        return this.parent[x];
    }

    union(x: number, y: number): boolean {
        const rootX = this.find(x);
        const rootY = this.find(y);

        if (rootX === rootY) return false;

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

## Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Find | O(α(n)) ≈ O(1) | O(1) |
| Union | O(α(n)) ≈ O(1) | O(1) |
| Connected | O(α(n)) ≈ O(1) | O(1) |
| Space total | - | O(n) |

## Common Patterns

### 1. Count Components
```typescript
function countComponents(n: number, edges: number[][]): number {
    const uf = new UnionFind(n);
    for (const [u, v] of edges) {
        uf.union(u, v);
    }
    return uf.getComponents();
}
```

### 2. Detect Cycle
```typescript
function hasCycle(edges: number[][]): boolean {
    const uf = new UnionFind(n);
    for (const [u, v] of edges) {
        if (uf.connected(u, v)) return true;
        uf.union(u, v);
    }
    return false;
}
```

### 3. Valid Tree
```typescript
function validTree(n: number, edges: number[][]): boolean {
    if (edges.length !== n - 1) return false;

    const uf = new UnionFind(n);
    for (const [u, v] of edges) {
        if (!uf.union(u, v)) return false;
    }

    return uf.getComponents() === 1;
}
```

## Key Insights

1. **Path Compression**: Makes every node point directly to root during find
2. **Union by Rank**: Keeps trees balanced by attaching shorter tree under taller
3. **Component Tracking**: Decrement count on successful union
4. **Cycle Detection**: If union returns false, edge creates cycle
5. **Return Values**: Use union's boolean return to detect existing connections

## When to Use

✅ **Use Union-Find:**
- Connected components
- Cycle detection (undirected)
- Group merging
- Dynamic connectivity
- Minimum spanning tree

❌ **Don't Use:**
- Directed graphs (needs modification)
- Need actual paths
- Need to disconnect
- Shortest paths

## Interview Checklist

- [ ] Implement both optimizations (path compression + union by rank)
- [ ] Track component count correctly
- [ ] Handle 0-indexed vs 1-indexed nodes
- [ ] Check for cycles when needed
- [ ] Return boolean from union for cycle detection
- [ ] Initialize parent[i] = i for all nodes

## Common Mistakes

1. ❌ Forgetting path compression
2. ❌ Not using union by rank
3. ❌ Wrong component counting
4. ❌ Index off-by-one errors
5. ❌ Not checking if already connected

## Quick Tips

- Draw the forest structure
- Test with 2-3 unions to verify
- Always analyze as O(α(n)) ≈ O(1)
- Say "disjoint set union" to sound technical
- Mention both optimizations explicitly
