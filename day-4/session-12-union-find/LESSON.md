# Lesson: Union-Find

---

## 📹 Video 1: Union-Find Fundamentals (14 min)

**"Union Find - NeetCode"**
https://www.youtube.com/watch?v=8f1XPm4WxGU

**Focus on:**
- What Union-Find solves
- Find and Union operations
- Path compression optimization
- Union by rank/size

---

## 📹 Video 2: Union-Find Deep Dive (25 min)

**"Disjoint Set | UNION and FIND - Abdul Bari"**
https://www.youtube.com/watch?v=wU6udHRIkcc

**Focus on:**
- Tree representation of sets
- Weighted union (union by rank)
- Path compression details
- Complexity analysis

---

## 📹 Video 3: Advanced Applications (16 min)

**"Union Find Explained - William Fiset"**
https://www.youtube.com/watch?v=ibjEGG7ylHk

**Alternative:**
https://www.youtube.com/watch?v=ayW5B2W9hfo

**Focus on:**
- Kruskal's algorithm
- Connected components
- Cycle detection
- Real-world applications

---

## 🎯 What is Union-Find?

Union-Find (also called Disjoint Set Union or DSU) is a data structure that efficiently tracks elements partitioned into disjoint (non-overlapping) sets.

### Real-World Analogy

Think of Union-Find like managing friend groups on social media:
- Initially, each person is in their own group (singleton)
- When two people become friends, their entire groups merge
- To check if two people are connected, see if they're in the same group
- Each group has a "representative" (the root)

### Core Problem

Given n elements, support these operations efficiently:
1. **Union(x, y)** - Merge the sets containing x and y
2. **Find(x)** - Determine which set contains x
3. **Connected(x, y)** - Check if x and y are in the same set

**Key insight:** We don't care about the exact structure, just connectivity!

---

## 🏗️ Basic Structure

### Parent Array Representation

```typescript
class UnionFind {
    private parent: number[];

    constructor(n: number) {
        // Each element starts as its own parent
        this.parent = Array(n).fill(0).map((_, i) => i);
    }
}
```

**Visualization:**
```
Initial state (n=5):
Elements: 0   1   2   3   4
Parent:   0   1   2   3   4  (each element is its own set)
```

Each element initially points to itself, forming singleton sets.

---

## 🔍 Find Operation

Find the root representative of the set containing element x.

### Naive Implementation

```typescript
find(x: number): number {
    // Follow parent pointers until we reach root
    while (this.parent[x] !== x) {
        x = this.parent[x];
    }
    return x;
}
```

**Visualization:**
```
Chain: 0 → 1 → 2 → 3 (root)
find(0) follows: 0 → 1 → 2 → 3 → returns 3
```

**Time Complexity:** O(n) worst case (skewed tree)

---

## 🔗 Union Operation

Merge two sets by connecting their roots.

### Naive Implementation

```typescript
union(x: number, y: number): void {
    const rootX = this.find(x);
    const rootY = this.find(y);

    if (rootX !== rootY) {
        // Make rootX point to rootY
        this.parent[rootX] = rootY;
    }
}
```

**Visualization:**
```
Before union(0, 3):
Set 1: 0 → 1 (root)
Set 2: 3 → 4 (root)

After union(0, 3):
        4 (root)
       /
      3
     /
    1
   /
  0
```

**Problem:** Can create very tall trees → slow find operations!

---

## ⚡ Optimization 1: Path Compression

**Key Idea:** During find, make every node point directly to the root.

### Implementation

```typescript
find(x: number): number {
    if (this.parent[x] !== x) {
        // Recursively find root AND update parent
        this.parent[x] = this.find(this.parent[x]);
    }
    return this.parent[x];
}
```

**Visualization:**
```
Before find(0):
0 → 1 → 2 → 3 → 4 (root)

After find(0):
0 → 4
1 → 4
2 → 4
3 → 4
4 (root)
```

**Effect:** Future finds are nearly instant!

**Alternative (Iterative):**
```typescript
find(x: number): number {
    let root = x;

    // Find root
    while (this.parent[root] !== root) {
        root = this.parent[root];
    }

    // Compress path
    while (x !== root) {
        const next = this.parent[x];
        this.parent[x] = root;
        x = next;
    }

    return root;
}
```

---

## ⚖️ Optimization 2: Union by Rank

**Key Idea:** Always attach the shorter tree under the taller tree to keep trees balanced.

### Implementation

```typescript
class UnionFind {
    private parent: number[];
    private rank: number[];  // Approximate tree height

    constructor(n: number) {
        this.parent = Array(n).fill(0).map((_, i) => i);
        this.rank = Array(n).fill(0);  // All start with rank 0
    }

    union(x: number, y: number): boolean {
        const rootX = this.find(x);
        const rootY = this.find(y);

        if (rootX === rootY) {
            return false;  // Already in same set
        }

        // Attach smaller rank tree under larger rank tree
        if (this.rank[rootX] < this.rank[rootY]) {
            this.parent[rootX] = rootY;
        } else if (this.rank[rootX] > this.rank[rootY]) {
            this.parent[rootY] = rootX;
        } else {
            // Same rank - attach either way and increment rank
            this.parent[rootY] = rootX;
            this.rank[rootX]++;
        }

        return true;
    }
}
```

**Visualization:**
```
Union by rank prevents skewed trees:

❌ Bad (without union by rank):
    5
   /
  4
 /
3
/
2
/
1    → Height 5, slow finds!

✅ Good (with union by rank):
    5
   / \
  3   4
 / \
1   2  → Height 2, fast finds!
```

**Why "rank" not "height"?** Path compression changes actual heights, but rank remains an upper bound that's simpler to maintain.

---

## 🎯 Complete Template

### Standard Union-Find Implementation

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
            this.parent[x] = this.find(this.parent[x]);  // Path compression
        }
        return this.parent[x];
    }

    union(x: number, y: number): boolean {
        const rootX = this.find(x);
        const rootY = this.find(y);

        if (rootX === rootY) {
            return false;  // Already connected
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

**Memory this template!** It's the foundation for all Union-Find problems.

---

## 📊 Time Complexity

### Without Optimizations
- Find: O(n) worst case
- Union: O(n) worst case

### With Path Compression Only
- Find: O(log n) amortized
- Union: O(log n) amortized

### With Both Optimizations
- Find: O(α(n)) ≈ O(1) amortized
- Union: O(α(n)) ≈ O(1) amortized

Where α(n) is the **inverse Ackermann function** - grows extremely slowly:
```
α(1) = 1
α(10) = 2
α(100) = 3
α(1000) = 3
α(10^80) = 4  (more atoms than in the universe!)
```

**For practical purposes: α(n) ≤ 4**, so treat it as constant!

**Space Complexity:** O(n) for parent and rank arrays

---

## 🧩 Common Problem Patterns

### Pattern 1: Count Connected Components

Count the number of separate groups in a graph.

```typescript
function countComponents(n: number, edges: number[][]): number {
    const uf = new UnionFind(n);

    for (const [u, v] of edges) {
        uf.union(u, v);
    }

    return uf.getComponents();
}
```

**Time:** O(E × α(V)) where E = edges, V = vertices

**Problems:** Number of Provinces, Connected Components in Undirected Graph

---

### Pattern 2: Detect Cycles

Check if adding an edge creates a cycle in an undirected graph.

```typescript
function hasCycle(n: number, edges: number[][]): boolean {
    const uf = new UnionFind(n);

    for (const [u, v] of edges) {
        if (uf.connected(u, v)) {
            return true;  // Already connected = cycle!
        }
        uf.union(u, v);
    }

    return false;
}
```

**Key insight:** If two nodes are already connected (same root), adding an edge between them creates a cycle.

**Problems:** Graph Valid Tree, Redundant Connection

---

### Pattern 3: Group Merging

Merge groups that share a common property.

```typescript
function mergeAccounts(accounts: string[][]): string[][] {
    const emailToAccount = new Map<string, number>();
    const uf = new UnionFind(accounts.length);

    // Union accounts sharing emails
    for (let i = 0; i < accounts.length; i++) {
        for (let j = 1; j < accounts[i].length; j++) {
            const email = accounts[i][j];

            if (emailToAccount.has(email)) {
                // Merge with existing account
                uf.union(i, emailToAccount.get(email)!);
            } else {
                emailToAccount.set(email, i);
            }
        }
    }

    // Group emails by root account
    // ... (group and format result)
}
```

**Problems:** Accounts Merge, Smallest String With Swaps

---

### Pattern 4: Component Optimization

Maximize removals by keeping one element per component.

```typescript
function maxStonesRemoved(stones: number[][]): number {
    const uf = new UnionFind();

    for (const [x, y] of stones) {
        // Union row x with column y
        // Use ~y to avoid collision with row indices
        uf.union(x, ~y);
    }

    // Can remove all except one per component
    return stones.length - uf.getComponents();
}
```

**Key insight:** In each connected component, we must keep 1 stone, but can remove all others.

**Problems:** Most Stones Removed, Number of Operations to Make Network Connected

---

## 🎓 Advanced Variations

### Weighted Union-Find

Track ratios/weights between elements (used for division problems).

```typescript
class WeightedUnionFind {
    private parent: Map<string, string>;
    private weight: Map<string, number>;  // weight[x] = x / parent[x]

    find(x: string): string {
        if (!this.parent.has(x)) {
            this.parent.set(x, x);
            this.weight.set(x, 1.0);
        }

        if (this.parent.get(x) !== x) {
            const originalParent = this.parent.get(x)!;
            this.parent.set(x, this.find(originalParent));
            // Update weight: x/root = (x/parent) * (parent/root)
            this.weight.set(x, this.weight.get(x)! * this.weight.get(originalParent)!);
        }

        return this.parent.get(x)!;
    }

    union(x: string, y: string, value: number): void {
        // x / y = value
        const rootX = this.find(x);
        const rootY = this.find(y);

        if (rootX !== rootY) {
            this.parent.set(rootX, rootY);
            // rootX / rootY = (x/y) * (y/rootY) / (x/rootX)
            this.weight.set(rootX, value * this.weight.get(y)! / this.weight.get(x)!);
        }
    }
}
```

**Problems:** Evaluate Division

---

### Union-Find with Size

Track the size of each component (alternative to rank).

```typescript
class UnionFindWithSize {
    private parent: number[];
    private size: number[];  // Number of elements in component

    constructor(n: number) {
        this.parent = Array(n).fill(0).map((_, i) => i);
        this.size = Array(n).fill(1);  // Each starts with size 1
    }

    union(x: number, y: number): void {
        const rootX = this.find(x);
        const rootY = this.find(y);

        if (rootX === rootY) return;

        // Attach smaller component to larger
        if (this.size[rootX] < this.size[rootY]) {
            this.parent[rootX] = rootY;
            this.size[rootY] += this.size[rootX];
        } else {
            this.parent[rootY] = rootX;
            this.size[rootX] += this.size[rootY];
        }
    }

    getSize(x: number): number {
        return this.size[this.find(x)];
    }
}
```

---

## 🎯 When to Use Union-Find

### Use Union-Find when you see:
- ✅ "Connected components"
- ✅ "Groups" or "clusters"
- ✅ "Merge" or "join"
- ✅ "Detect cycle" in undirected graph
- ✅ "Check connectivity" queries
- ✅ "Minimum spanning tree" (Kruskal's)
- ✅ Dynamic connectivity

### Don't use Union-Find when:
- ❌ Directed graphs (needs modification)
- ❌ Need actual paths (use BFS/DFS)
- ❌ Need to disconnect elements (Union-Find doesn't support split)
- ❌ Shortest path problems (use Dijkstra/BFS)
- ❌ Need to track edges (Union-Find only tracks nodes)

---

## 💡 Interview Tips

### What to Say

**Recognizing the pattern:**
- "This looks like a connectivity problem, I'll use Union-Find."
- "We need to track connected components dynamically, Union-Find is perfect here."
- "For cycle detection in an undirected graph, Union-Find is optimal."

**Explaining your solution:**
- "I'm implementing Union-Find with path compression and union by rank for near-constant time operations."
- "Each union operation merges two components, reducing the total count."
- "If the nodes are already connected, this edge would create a cycle."

**Analyzing complexity:**
- "With both optimizations, each operation is O(α(n)), which is effectively constant."
- "For E edges and V vertices, the total time is O(E × α(V)), practically O(E)."

### What to Draw

```
Draw the forest representation:

Initial:  0   1   2   3   4
          ↓   ↓   ↓   ↓   ↓
          0   1   2   3   4

After union(0,1):
          0
          ↓
          1   2   3   4
          ↓   ↓   ↓   ↓
          1   2   3   4

After union(2,3):
          0       2
          ↓       ↓
          1       3   4
          ↓       ↓   ↓
          1       3   4

After union(1,3):
              0
             / \
            1   2
            ↓   ↓
            3   3   4
            ↓       ↓
            3       4
```

### Common Follow-ups

**"What's the time complexity?"**
→ "O(α(n)) per operation with both optimizations, where α is the inverse Ackermann function. For all practical purposes, this is constant time."

**"Why not use DFS/BFS?"**
→ "Union-Find is better for dynamic connectivity queries. DFS requires O(V+E) per query, while Union-Find is nearly O(1). However, if we only need to check connectivity once, DFS is simpler."

**"Can you disconnect nodes?"**
→ "Standard Union-Find doesn't support disconnect. We'd need a persistent data structure or rebuild from scratch."

**"How do you handle duplicate edges?"**
→ "Union returns false if nodes are already connected, so we naturally ignore duplicates."

---

## 🎓 Implementation Variations

### Map-Based Union-Find (Unknown Size)

When you don't know the number of elements in advance:

```typescript
class DynamicUnionFind {
    private parent: Map<number, number>;
    private rank: Map<number, number>;

    find(x: number): number {
        if (!this.parent.has(x)) {
            this.parent.set(x, x);
            this.rank.set(x, 0);
        }

        if (this.parent.get(x) !== x) {
            this.parent.set(x, this.find(this.parent.get(x)!));
        }

        return this.parent.get(x)!;
    }

    union(x: number, y: number): void {
        const rootX = this.find(x);
        const rootY = this.find(y);

        if (rootX === rootY) return;

        const rankX = this.rank.get(rootX)!;
        const rankY = this.rank.get(rootY)!;

        if (rankX < rankY) {
            this.parent.set(rootX, rootY);
        } else if (rankX > rankY) {
            this.parent.set(rootY, rootX);
        } else {
            this.parent.set(rootY, rootX);
            this.rank.set(rootX, rankX + 1);
        }
    }
}
```

---

## ✅ Key Takeaways

1. **Union-Find excels at dynamic connectivity** - Use it when you need to merge groups and query connectivity efficiently.

2. **Always use both optimizations** - Path compression + union by rank give you O(α(n)) ≈ O(1) operations.

3. **Track component count** - Decrement when union succeeds, makes counting trivial.

4. **Union return value is useful** - Return false if already connected (cycle detection, counting extra edges).

5. **Initialize correctly** - Each element starts as its own parent: `parent[i] = i`.

6. **Weighted variants are tricky** - For problems like Evaluate Division, consider graph DFS as simpler alternative.

7. **Draw the trees** - Visualization helps understand merging and path compression.

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **Find with path compression:** O(α(n)) ≈ O(1)
- **Union by rank:** O(α(n)) ≈ O(1)
- **Space:** O(n) for parent and rank arrays
- **When to use:** Connectivity, grouping, cycle detection, components

---

[Back to Session README](./README.md)
