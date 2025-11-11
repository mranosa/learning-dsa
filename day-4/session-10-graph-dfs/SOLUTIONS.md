# Solutions: Graph DFS

## Problem 1: Number of Islands

### Approach 1: DFS with Modification
**Time:** O(m × n) | **Space:** O(m × n) for recursion stack

```typescript
function numIslands(grid: string[][]): number {
    if (!grid || grid.length === 0) return 0;

    let islands = 0;
    const rows = grid.length;
    const cols = grid[0].length;

    function dfs(row: number, col: number): void {
        // Boundary and water check
        if (row < 0 || row >= rows || col < 0 || col >= cols || grid[row][col] === '0') {
            return;
        }

        // Mark as visited by changing to water
        grid[row][col] = '0';

        // Explore all 4 directions
        dfs(row + 1, col); // down
        dfs(row - 1, col); // up
        dfs(row, col + 1); // right
        dfs(row, col - 1); // left
    }

    // Check each cell
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            if (grid[row][col] === '1') {
                islands++;
                dfs(row, col);
            }
        }
    }

    return islands;
}
```

### Approach 2: DFS with Visited Set (Preserves Input)
**Time:** O(m × n) | **Space:** O(m × n) for visited set

```typescript
function numIslands(grid: string[][]): number {
    if (!grid || grid.length === 0) return 0;

    const rows = grid.length;
    const cols = grid[0].length;
    const visited = new Set<string>();
    let islands = 0;

    function dfs(row: number, col: number): void {
        const key = `${row},${col}`;

        if (row < 0 || row >= rows || col < 0 || col >= cols ||
            grid[row][col] === '0' || visited.has(key)) {
            return;
        }

        visited.add(key);

        // Explore 4 directions
        const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        for (const [dr, dc] of directions) {
            dfs(row + dr, col + dc);
        }
    }

    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            if (grid[row][col] === '1' && !visited.has(`${row},${col}`)) {
                islands++;
                dfs(row, col);
            }
        }
    }

    return islands;
}
```

---

## Problem 2: Clone Graph

### Approach: DFS with HashMap
**Time:** O(V + E) | **Space:** O(V) for cloned nodes

```typescript
class Node {
    val: number;
    neighbors: Node[];
    constructor(val?: number, neighbors?: Node[]) {
        this.val = (val === undefined ? 0 : val);
        this.neighbors = (neighbors === undefined ? [] : neighbors);
    }
}

function cloneGraph(node: Node | null): Node | null {
    if (!node) return null;

    const cloned = new Map<Node, Node>();

    function dfs(node: Node): Node {
        // If already cloned, return the clone
        if (cloned.has(node)) {
            return cloned.get(node)!;
        }

        // Create new node
        const clone = new Node(node.val);
        cloned.set(node, clone);

        // Clone all neighbors
        for (const neighbor of node.neighbors) {
            clone.neighbors.push(dfs(neighbor));
        }

        return clone;
    }

    return dfs(node);
}
```

### Approach 2: Iterative DFS
**Time:** O(V + E) | **Space:** O(V)

```typescript
function cloneGraph(node: Node | null): Node | null {
    if (!node) return null;

    const cloned = new Map<Node, Node>();
    const stack = [node];

    // Create clone of starting node
    cloned.set(node, new Node(node.val));

    while (stack.length > 0) {
        const current = stack.pop()!;
        const currentClone = cloned.get(current)!;

        for (const neighbor of current.neighbors) {
            if (!cloned.has(neighbor)) {
                // Create new clone
                cloned.set(neighbor, new Node(neighbor.val));
                stack.push(neighbor);
            }
            // Add to neighbors list
            currentClone.neighbors.push(cloned.get(neighbor)!);
        }
    }

    return cloned.get(node)!;
}
```

---

## Problem 3: Max Area of Island

### Approach: DFS with Area Tracking
**Time:** O(m × n) | **Space:** O(m × n) for recursion

```typescript
function maxAreaOfIsland(grid: number[][]): number {
    if (!grid || grid.length === 0) return 0;

    let maxArea = 0;
    const rows = grid.length;
    const cols = grid[0].length;

    function dfs(row: number, col: number): number {
        // Boundary and water check
        if (row < 0 || row >= rows || col < 0 || col >= cols || grid[row][col] === 0) {
            return 0;
        }

        // Mark as visited
        grid[row][col] = 0;

        // Count current cell + all connected cells
        let area = 1;
        area += dfs(row + 1, col);
        area += dfs(row - 1, col);
        area += dfs(row, col + 1);
        area += dfs(row, col - 1);

        return area;
    }

    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            if (grid[row][col] === 1) {
                const area = dfs(row, col);
                maxArea = Math.max(maxArea, area);
            }
        }
    }

    return maxArea;
}
```

---

## Problem 4: Pacific Atlantic Water Flow

### Approach: DFS from Ocean Borders
**Time:** O(m × n) | **Space:** O(m × n)

```typescript
function pacificAtlantic(heights: number[][]): number[][] {
    if (!heights || heights.length === 0) return [];

    const rows = heights.length;
    const cols = heights[0].length;
    const pacific = new Set<string>();
    const atlantic = new Set<string>();

    function dfs(row: number, col: number, visited: Set<string>, prevHeight: number): void {
        const key = `${row},${col}`;

        // Check boundaries, visited, and height constraint
        if (row < 0 || row >= rows || col < 0 || col >= cols ||
            visited.has(key) || heights[row][col] < prevHeight) {
            return;
        }

        visited.add(key);

        // Explore 4 directions
        const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        for (const [dr, dc] of directions) {
            dfs(row + dr, col + dc, visited, heights[row][col]);
        }
    }

    // DFS from Pacific borders (top and left)
    for (let col = 0; col < cols; col++) {
        dfs(0, col, pacific, -1); // top row
    }
    for (let row = 0; row < rows; row++) {
        dfs(row, 0, pacific, -1); // left column
    }

    // DFS from Atlantic borders (bottom and right)
    for (let col = 0; col < cols; col++) {
        dfs(rows - 1, col, atlantic, -1); // bottom row
    }
    for (let row = 0; row < rows; row++) {
        dfs(row, cols - 1, atlantic, -1); // right column
    }

    // Find cells that can reach both oceans
    const result: number[][] = [];
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            const key = `${row},${col}`;
            if (pacific.has(key) && atlantic.has(key)) {
                result.push([row, col]);
            }
        }
    }

    return result;
}
```

---

## Problem 5: Surrounded Regions

### Approach: DFS from Borders
**Time:** O(m × n) | **Space:** O(m × n)

```typescript
function solve(board: string[][]): void {
    if (!board || board.length === 0) return;

    const rows = board.length;
    const cols = board[0].length;

    function dfs(row: number, col: number): void {
        if (row < 0 || row >= rows || col < 0 || col >= cols || board[row][col] !== 'O') {
            return;
        }

        // Mark as safe (connected to border)
        board[row][col] = 'S';

        // Explore 4 directions
        dfs(row + 1, col);
        dfs(row - 1, col);
        dfs(row, col + 1);
        dfs(row, col - 1);
    }

    // Mark all O's connected to borders as safe
    for (let row = 0; row < rows; row++) {
        dfs(row, 0);         // left border
        dfs(row, cols - 1);  // right border
    }
    for (let col = 0; col < cols; col++) {
        dfs(0, col);         // top border
        dfs(rows - 1, col);  // bottom border
    }

    // Convert remaining O's to X's and S's back to O's
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            if (board[row][col] === 'O') {
                board[row][col] = 'X';  // Surrounded region
            } else if (board[row][col] === 'S') {
                board[row][col] = 'O';  // Safe region
            }
        }
    }
}
```

---

## Problem 6: Flood Fill

### Approach: Simple DFS
**Time:** O(m × n) | **Space:** O(m × n)

```typescript
function floodFill(image: number[][], sr: number, sc: number, newColor: number): number[][] {
    const originalColor = image[sr][sc];

    // If new color is same as original, no need to fill
    if (originalColor === newColor) return image;

    function dfs(row: number, col: number): void {
        // Check boundaries and color match
        if (row < 0 || row >= image.length ||
            col < 0 || col >= image[0].length ||
            image[row][col] !== originalColor) {
            return;
        }

        // Fill current pixel
        image[row][col] = newColor;

        // Fill adjacent pixels
        dfs(row + 1, col);
        dfs(row - 1, col);
        dfs(row, col + 1);
        dfs(row, col - 1);
    }

    dfs(sr, sc);
    return image;
}
```

---

## Problem 7: Number of Connected Components

### Approach: DFS with Adjacency List
**Time:** O(V + E) | **Space:** O(V + E)

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

    function dfs(node: number): void {
        visited.add(node);
        for (const neighbor of graph.get(node)!) {
            if (!visited.has(neighbor)) {
                dfs(neighbor);
            }
        }
    }

    // Count components
    for (let i = 0; i < n; i++) {
        if (!visited.has(i)) {
            components++;
            dfs(i);
        }
    }

    return components;
}
```

---

## Problem 8: Word Search

### Approach: DFS with Backtracking
**Time:** O(m × n × 4^L) where L is word length | **Space:** O(L)

```typescript
function exist(board: string[][], word: string): boolean {
    const rows = board.length;
    const cols = board[0].length;

    function dfs(row: number, col: number, index: number): boolean {
        // Found the word
        if (index === word.length) return true;

        // Boundary and character check
        if (row < 0 || row >= rows || col < 0 || col >= cols ||
            board[row][col] !== word[index]) {
            return false;
        }

        // Mark as visited temporarily
        const temp = board[row][col];
        board[row][col] = '#';

        // Explore 4 directions
        const found = dfs(row + 1, col, index + 1) ||
                     dfs(row - 1, col, index + 1) ||
                     dfs(row, col + 1, index + 1) ||
                     dfs(row, col - 1, index + 1);

        // Backtrack
        board[row][col] = temp;

        return found;
    }

    // Try starting from each cell
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            if (dfs(row, col, 0)) return true;
        }
    }

    return false;
}
```

---

## Problem 9: All Paths From Source to Target

### Approach: DFS with Path Building
**Time:** O(2^N × N) | **Space:** O(2^N × N)

```typescript
function allPathsSourceTarget(graph: number[][]): number[][] {
    const target = graph.length - 1;
    const result: number[][] = [];

    function dfs(node: number, path: number[]): void {
        // Add current node to path
        path.push(node);

        // If we reached target, add path to result
        if (node === target) {
            result.push([...path]);
        } else {
            // Explore neighbors
            for (const neighbor of graph[node]) {
                dfs(neighbor, path);
            }
        }

        // Backtrack
        path.pop();
    }

    dfs(0, []);
    return result;
}
```

### Approach 2: Without Backtracking
**Time:** O(2^N × N) | **Space:** O(2^N × N)

```typescript
function allPathsSourceTarget(graph: number[][]): number[][] {
    const target = graph.length - 1;
    const result: number[][] = [];

    function dfs(node: number, path: number[]): void {
        if (node === target) {
            result.push([...path, node]);
            return;
        }

        for (const neighbor of graph[node]) {
            dfs(neighbor, [...path, node]);
        }
    }

    dfs(0, []);
    return result;
}
```

---

## Problem 10: Detect Cycle in Undirected Graph

### Approach: DFS with Parent Tracking
**Time:** O(V + E) | **Space:** O(V + E)

```typescript
function hasCycle(n: number, edges: number[][]): boolean {
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

    function dfs(node: number, parent: number): boolean {
        visited.add(node);

        for (const neighbor of graph.get(node)!) {
            if (!visited.has(neighbor)) {
                // Continue DFS
                if (dfs(neighbor, node)) return true;
            } else if (neighbor !== parent) {
                // Found a cycle (visited node that's not parent)
                return true;
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

### Approach 2: Union-Find (Alternative)
**Time:** O(E × α(V)) | **Space:** O(V)

```typescript
function hasCycle(n: number, edges: number[][]): boolean {
    const parent = Array(n).fill(0).map((_, i) => i);

    function find(x: number): number {
        if (parent[x] !== x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    function union(x: number, y: number): boolean {
        const px = find(x);
        const py = find(y);

        if (px === py) return true; // Cycle detected

        parent[px] = py;
        return false;
    }

    for (const [a, b] of edges) {
        if (union(a, b)) return true;
    }

    return false;
}
```