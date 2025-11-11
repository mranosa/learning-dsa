# Union-Find Solutions

## 1. Number of Provinces

### Approach 1: Union-Find

```typescript
function findCircleNum(isConnected: number[][]): number {
    const n = isConnected.length;
    const uf = new UnionFind(n);

    // Union connected cities
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (isConnected[i][j] === 1) {
                uf.union(i, j);
            }
        }
    }

    return uf.getComponents();
}

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

    getComponents(): number {
        return this.components;
    }
}
```

**Time Complexity:** O(n² × α(n)) where α is inverse Ackermann function
**Space Complexity:** O(n)

### Approach 2: DFS

```typescript
function findCircleNum(isConnected: number[][]): number {
    const n = isConnected.length;
    const visited = new Array(n).fill(false);
    let provinces = 0;

    const dfs = (city: number): void => {
        visited[city] = true;
        for (let neighbor = 0; neighbor < n; neighbor++) {
            if (isConnected[city][neighbor] === 1 && !visited[neighbor]) {
                dfs(neighbor);
            }
        }
    };

    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i);
            provinces++;
        }
    }

    return provinces;
}
```

**Time Complexity:** O(n²)
**Space Complexity:** O(n)

---

## 2. Graph Valid Tree

### Approach: Union-Find with Cycle Detection

```typescript
function validTree(n: number, edges: number[][]): boolean {
    // A valid tree must have exactly n-1 edges
    if (edges.length !== n - 1) return false;

    const uf = new UnionFind(n);

    // Check for cycles
    for (const [u, v] of edges) {
        if (!uf.union(u, v)) {
            return false; // Cycle detected
        }
    }

    // Check if all nodes are connected
    return uf.getComponents() === 1;
}

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

        if (rootX === rootY) {
            return false; // Already connected (cycle)
        }

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

    getComponents(): number {
        return this.components;
    }
}
```

**Time Complexity:** O(E × α(V)) where E is edges, V is vertices
**Space Complexity:** O(V)

---

## 3. Number of Connected Components

### Approach: Union-Find

```typescript
function countComponents(n: number, edges: number[][]): number {
    const uf = new UnionFind(n);

    for (const [u, v] of edges) {
        uf.union(u, v);
    }

    return uf.getComponents();
}

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

    union(x: number, y: number): void {
        const rootX = this.find(x);
        const rootY = this.find(y);

        if (rootX === rootY) return;

        if (this.rank[rootX] < this.rank[rootY]) {
            this.parent[rootX] = rootY;
        } else if (this.rank[rootX] > this.rank[rootY]) {
            this.parent[rootY] = rootX;
        } else {
            this.parent[rootY] = rootX;
            this.rank[rootX]++;
        }

        this.components--;
    }

    getComponents(): number {
        return this.components;
    }
}
```

**Time Complexity:** O(E × α(V))
**Space Complexity:** O(V)

---

## 4. Redundant Connection

### Approach: Union-Find to Find Cycle Edge

```typescript
function findRedundantConnection(edges: number[][]): number[] {
    const n = edges.length;
    const uf = new UnionFind(n + 1); // Nodes are 1-indexed

    for (const [u, v] of edges) {
        if (!uf.union(u, v)) {
            // This edge creates a cycle
            return [u, v];
        }
    }

    return []; // Should never reach here
}

class UnionFind {
    private parent: number[];
    private rank: number[];

    constructor(n: number) {
        this.parent = Array(n).fill(0).map((_, i) => i);
        this.rank = Array(n).fill(0);
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

        if (rootX === rootY) {
            return false; // Edge creates cycle
        }

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
}
```

**Time Complexity:** O(n × α(n))
**Space Complexity:** O(n)

---

## 5. Accounts Merge

### Approach: Union-Find with Email Mapping

```typescript
function accountsMerge(accounts: string[][]): string[][] {
    const emailToAccount = new Map<string, number>();
    const emailToName = new Map<string, string>();
    const n = accounts.length;
    const uf = new UnionFind(n);

    // Map emails to accounts and union accounts with common emails
    for (let i = 0; i < n; i++) {
        const name = accounts[i][0];

        for (let j = 1; j < accounts[i].length; j++) {
            const email = accounts[i][j];
            emailToName.set(email, name);

            if (emailToAccount.has(email)) {
                // This email belongs to another account, merge them
                uf.union(i, emailToAccount.get(email)!);
            } else {
                emailToAccount.set(email, i);
            }
        }
    }

    // Group emails by component root
    const components = new Map<number, string[]>();

    for (const [email, accountIdx] of emailToAccount) {
        const root = uf.find(accountIdx);
        if (!components.has(root)) {
            components.set(root, []);
        }
        components.get(root)!.push(email);
    }

    // Build result
    const result: string[][] = [];

    for (const [root, emails] of components) {
        emails.sort(); // Sort emails lexicographically
        const name = emailToName.get(emails[0])!;
        result.push([name, ...emails]);
    }

    return result;
}

class UnionFind {
    private parent: number[];
    private rank: number[];

    constructor(n: number) {
        this.parent = Array(n).fill(0).map((_, i) => i);
        this.rank = Array(n).fill(0);
    }

    find(x: number): number {
        if (this.parent[x] !== x) {
            this.parent[x] = this.find(this.parent[x]);
        }
        return this.parent[x];
    }

    union(x: number, y: number): void {
        const rootX = this.find(x);
        const rootY = this.find(y);

        if (rootX === rootY) return;

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

**Time Complexity:** O(NK log NK) where N is accounts, K is max emails per account
**Space Complexity:** O(NK)

---

## 6. Most Stones Removed

### Approach: Union-Find with Row/Column Mapping

```typescript
function removeStones(stones: number[][]): number {
    const uf = new UnionFind();

    for (const [x, y] of stones) {
        // Connect row and column indices
        // Use negative values for columns to avoid collision
        uf.union(x, ~y);
    }

    // Maximum removals = total stones - number of components
    return stones.length - uf.getComponents();
}

class UnionFind {
    private parent: Map<number, number>;
    private rank: Map<number, number>;
    private components: Set<number>;

    constructor() {
        this.parent = new Map();
        this.rank = new Map();
        this.components = new Set();
    }

    find(x: number): number {
        if (!this.parent.has(x)) {
            this.parent.set(x, x);
            this.rank.set(x, 0);
            this.components.add(x);
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
            this.components.delete(rootX);
        } else if (rankX > rankY) {
            this.parent.set(rootY, rootX);
            this.components.delete(rootY);
        } else {
            this.parent.set(rootY, rootX);
            this.rank.set(rootX, rankX + 1);
            this.components.delete(rootY);
        }
    }

    getComponents(): number {
        return this.components.size;
    }
}
```

**Time Complexity:** O(n × α(n))
**Space Complexity:** O(n)

---

## 7. Number of Operations to Make Network Connected

### Approach: Count Components and Extra Cables

```typescript
function makeConnected(n: number, connections: number[][]): number {
    // Need at least n-1 cables to connect n computers
    if (connections.length < n - 1) return -1;

    const uf = new UnionFind(n);
    let extraCables = 0;

    for (const [a, b] of connections) {
        if (!uf.union(a, b)) {
            // This cable is redundant
            extraCables++;
        }
    }

    const components = uf.getComponents();
    const cablesNeeded = components - 1;

    return cablesNeeded;
}

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

    getComponents(): number {
        return this.components;
    }
}
```

**Time Complexity:** O(E × α(V))
**Space Complexity:** O(V)

---

## 8. Satisfiability of Equality Equations

### Approach: Union Equal Variables, Check Inequalities

```typescript
function equationsPossible(equations: string[]): boolean {
    const uf = new UnionFind(26); // 26 lowercase letters

    // First pass: process all equality equations
    for (const eq of equations) {
        if (eq[1] === '=') {
            const x = eq.charCodeAt(0) - 97; // 'a' = 0
            const y = eq.charCodeAt(3) - 97;
            uf.union(x, y);
        }
    }

    // Second pass: check inequality equations
    for (const eq of equations) {
        if (eq[1] === '!') {
            const x = eq.charCodeAt(0) - 97;
            const y = eq.charCodeAt(3) - 97;

            if (uf.find(x) === uf.find(y)) {
                // Variables that should be different are in same group
                return false;
            }
        }
    }

    return true;
}

class UnionFind {
    private parent: number[];
    private rank: number[];

    constructor(n: number) {
        this.parent = Array(n).fill(0).map((_, i) => i);
        this.rank = Array(n).fill(0);
    }

    find(x: number): number {
        if (this.parent[x] !== x) {
            this.parent[x] = this.find(this.parent[x]);
        }
        return this.parent[x];
    }

    union(x: number, y: number): void {
        const rootX = this.find(x);
        const rootY = this.find(y);

        if (rootX === rootY) return;

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

**Time Complexity:** O(n × α(26)) ≈ O(n)
**Space Complexity:** O(1)

---

## 9. Smallest String With Swaps

### Approach: Group Characters by Component and Sort

```typescript
function smallestStringWithSwaps(s: string, pairs: number[][]): string {
    const n = s.length;
    const uf = new UnionFind(n);

    // Union indices that can be swapped
    for (const [i, j] of pairs) {
        uf.union(i, j);
    }

    // Group indices by component
    const components = new Map<number, number[]>();
    for (let i = 0; i < n; i++) {
        const root = uf.find(i);
        if (!components.has(root)) {
            components.set(root, []);
        }
        components.get(root)!.push(i);
    }

    // Sort characters within each component
    const result = s.split('');

    for (const indices of components.values()) {
        // Get characters at these indices
        const chars: string[] = [];
        for (const idx of indices) {
            chars.push(s[idx]);
        }

        // Sort characters
        chars.sort();

        // Sort indices to place characters in order
        indices.sort((a, b) => a - b);

        // Place sorted characters back
        for (let i = 0; i < indices.length; i++) {
            result[indices[i]] = chars[i];
        }
    }

    return result.join('');
}

class UnionFind {
    private parent: number[];
    private rank: number[];

    constructor(n: number) {
        this.parent = Array(n).fill(0).map((_, i) => i);
        this.rank = Array(n).fill(0);
    }

    find(x: number): number {
        if (this.parent[x] !== x) {
            this.parent[x] = this.find(this.parent[x]);
        }
        return this.parent[x];
    }

    union(x: number, y: number): void {
        const rootX = this.find(x);
        const rootY = this.find(y);

        if (rootX === rootY) return;

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

**Time Complexity:** O(n log n + E × α(n))
**Space Complexity:** O(n)

---

## 10. Evaluate Division

### Approach 1: Weighted Union-Find (Complex)

```typescript
function calcEquation(equations: string[][], values: number[], queries: string[][]): number[] {
    const parent = new Map<string, string>();
    const weight = new Map<string, number>();

    const find = (x: string): string => {
        if (!parent.has(x)) {
            parent.set(x, x);
            weight.set(x, 1.0);
        }

        if (parent.get(x) !== x) {
            const originalParent = parent.get(x)!;
            parent.set(x, find(originalParent));
            weight.set(x, weight.get(x)! * weight.get(originalParent)!);
        }

        return parent.get(x)!;
    };

    const union = (x: string, y: string, value: number): void => {
        const rootX = find(x);
        const rootY = find(y);

        if (rootX !== rootY) {
            parent.set(rootX, rootY);
            weight.set(rootX, value * weight.get(y)! / weight.get(x)!);
        }
    };

    // Build union-find structure
    for (let i = 0; i < equations.length; i++) {
        const [a, b] = equations[i];
        union(a, b, values[i]);
    }

    // Process queries
    const result: number[] = [];

    for (const [c, d] of queries) {
        if (!parent.has(c) || !parent.has(d)) {
            result.push(-1.0);
        } else {
            const rootC = find(c);
            const rootD = find(d);

            if (rootC !== rootD) {
                result.push(-1.0);
            } else {
                result.push(weight.get(c)! / weight.get(d)!);
            }
        }
    }

    return result;
}
```

**Time Complexity:** O((E + Q) × α(E))
**Space Complexity:** O(E)

### Approach 2: Graph DFS (Simpler)

```typescript
function calcEquation(equations: string[][], values: number[], queries: string[][]): number[] {
    const graph = new Map<string, Map<string, number>>();

    // Build graph
    for (let i = 0; i < equations.length; i++) {
        const [a, b] = equations[i];
        const value = values[i];

        if (!graph.has(a)) graph.set(a, new Map());
        if (!graph.has(b)) graph.set(b, new Map());

        graph.get(a)!.set(b, value);
        graph.get(b)!.set(a, 1 / value);
    }

    // DFS to find path value
    const dfs = (start: string, end: string, visited: Set<string>): number => {
        if (!graph.has(start) || !graph.has(end)) return -1;
        if (start === end) return 1;

        visited.add(start);

        for (const [neighbor, value] of graph.get(start)!) {
            if (!visited.has(neighbor)) {
                const result = dfs(neighbor, end, visited);
                if (result !== -1) {
                    return value * result;
                }
            }
        }

        return -1;
    };

    // Process queries
    const result: number[] = [];

    for (const [c, d] of queries) {
        result.push(dfs(c, d, new Set()));
    }

    return result;
}
```

**Time Complexity:** O(Q × (V + E))
**Space Complexity:** O(E)