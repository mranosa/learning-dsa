# Hints - Session 11: Graph BFS

Progressive hints for 10 problems. Struggling is part of learning.

---

## Problem 1: Rotting Oranges

### Level 1
This is a "spreading" problem. Think about how rot spreads from multiple sources simultaneously each minute.

### Level 2
Use multi-source BFS. Start with all initially rotten oranges in queue. Process level by level where each level = 1 minute.

### Level 3
```typescript
const queue: [number, number][] = [];
let fresh = 0;

// Add all rotten oranges to queue, count fresh
for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
        if (grid[i][j] === 2) queue.push([i, j]);
        else if (grid[i][j] === 1) fresh++;
    }
}

let minutes = 0;
const directions = [[0,1], [1,0], [0,-1], [-1,0]];

while (queue.length > 0 && fresh > 0) {
    const size = queue.length;
    for (let i = 0; i < size; i++) {
        const [row, col] = queue.shift()!;
        for (const [dx, dy] of directions) {
            const newRow = row + dx;
            const newCol = col + dy;
            if (newRow >= 0 && newRow < m &&
                newCol >= 0 && newCol < n &&
                grid[newRow][newCol] === 1) {
                grid[newRow][newCol] = 2;
                fresh--;
                queue.push([newRow, newCol]);
            }
        }
    }
    minutes++;
}

return fresh === 0 ? minutes : -1;
```

---

## Problem 2: Course Schedule

### Level 1
Detect cycle in directed graph. If cycle exists in prerequisites, can't complete all courses.

### Level 2
Use topological sort with Kahn's algorithm. Track in-degrees and process nodes with 0 in-degree.

### Level 3
```typescript
const graph = new Map<number, number[]>();
const inDegree = new Array(numCourses).fill(0);

for (const [course, prereq] of prerequisites) {
    if (!graph.has(prereq)) graph.set(prereq, []);
    graph.get(prereq)!.push(course);
    inDegree[course]++;
}

const queue: number[] = [];
for (let i = 0; i < numCourses; i++) {
    if (inDegree[i] === 0) queue.push(i);
}

let processed = 0;
while (queue.length > 0) {
    const node = queue.shift()!;
    processed++;
    for (const neighbor of graph.get(node) || []) {
        inDegree[neighbor]--;
        if (inDegree[neighbor] === 0) queue.push(neighbor);
    }
}

return processed === numCourses;
```

---

## Problem 3: Course Schedule II

### Level 1
Similar to Course Schedule I, but return actual ordering instead of boolean.

### Level 2
Use Kahn's algorithm and track order as you process nodes. Processing order is your answer.

### Level 3
```typescript
const graph = new Map<number, number[]>();
const inDegree = new Array(numCourses).fill(0);

for (const [course, prereq] of prerequisites) {
    if (!graph.has(prereq)) graph.set(prereq, []);
    graph.get(prereq)!.push(course);
    inDegree[course]++;
}

const queue: number[] = [];
for (let i = 0; i < numCourses; i++) {
    if (inDegree[i] === 0) queue.push(i);
}

const result: number[] = [];
while (queue.length > 0) {
    const node = queue.shift()!;
    result.push(node);
    for (const neighbor of graph.get(node) || []) {
        inDegree[neighbor]--;
        if (inDegree[neighbor] === 0) queue.push(neighbor);
    }
}

return result.length === numCourses ? result : [];
```

---

## Problem 4: Shortest Path in Binary Matrix

### Level 1
BFS finds shortest paths. This problem allows 8-directional movement (includes diagonals).

### Level 2
Start BFS from (0,0) and try to reach (n-1, n-1). Track distance as you explore.

### Level 3
```typescript
if (grid[0][0] === 1 || grid[n-1][n-1] === 1) return -1;

const directions = [
    [0,1], [1,0], [0,-1], [-1,0],
    [1,1], [1,-1], [-1,1], [-1,-1]
];

const queue: [number, number, number][] = [[0, 0, 1]];
const visited = new Set<string>(['0,0']);

while (queue.length > 0) {
    const [row, col, dist] = queue.shift()!;
    if (row === n-1 && col === n-1) return dist;

    for (const [dx, dy] of directions) {
        const newRow = row + dx;
        const newCol = col + dy;
        const key = `${newRow},${newCol}`;

        if (newRow >= 0 && newRow < n &&
            newCol >= 0 && newCol < n &&
            grid[newRow][newCol] === 0 &&
            !visited.has(key)) {
            visited.add(key);
            queue.push([newRow, newCol, dist + 1]);
        }
    }
}

return -1;
```

---

## Problem 5: Walls and Gates

### Level 1
Instead of BFS from each room to find nearest gate, reverse the problem.

### Level 2
Start BFS from all gates simultaneously. First time you reach a room is shortest distance.

### Level 3
```typescript
const m = rooms.length, n = rooms[0].length;
const queue: [number, number][] = [];

// Add all gates to queue
for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
        if (rooms[i][j] === 0) queue.push([i, j]);
    }
}

const directions = [[0,1], [1,0], [0,-1], [-1,0]];

while (queue.length > 0) {
    const [row, col] = queue.shift()!;

    for (const [dx, dy] of directions) {
        const newRow = row + dx;
        const newCol = col + dy;

        if (newRow >= 0 && newRow < m &&
            newCol >= 0 && newCol < n &&
            rooms[newRow][newCol] === INF) {
            rooms[newRow][newCol] = rooms[row][col] + 1;
            queue.push([newRow, newCol]);
        }
    }
}
```

---

## Problem 6: Word Ladder

### Level 1
Think of words as nodes in graph. Edges exist between words differing by one letter.

### Level 2
Use BFS to find shortest transformation. Use pattern matching ("h*t") for efficient neighbor lookup.

### Level 3
```typescript
if (!wordList.includes(endWord)) return 0;

// Build pattern map
const patterns = new Map<string, string[]>();
for (const word of wordList) {
    for (let i = 0; i < word.length; i++) {
        const pattern = word.slice(0, i) + '*' + word.slice(i + 1);
        if (!patterns.has(pattern)) patterns.set(pattern, []);
        patterns.get(pattern)!.push(word);
    }
}

const queue: [string, number][] = [[beginWord, 1]];
const visited = new Set<string>([beginWord]);

while (queue.length > 0) {
    const [word, level] = queue.shift()!;
    if (word === endWord) return level;

    for (let i = 0; i < word.length; i++) {
        const pattern = word.slice(0, i) + '*' + word.slice(i + 1);
        for (const neighbor of patterns.get(pattern) || []) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push([neighbor, level + 1]);
            }
        }
    }
}

return 0;
```

---

## Problem 7: 01 Matrix

### Level 1
Similar to Walls and Gates - start from all 0s and spread outward.

### Level 2
Multi-source BFS from all cells containing 0. Each level increases distance by 1.

### Level 3
```typescript
const m = mat.length, n = mat[0].length;
const queue: [number, number][] = [];
const visited = new Set<string>();

// Add all 0s to queue
for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
        if (mat[i][j] === 0) {
            queue.push([i, j]);
            visited.add(`${i},${j}`);
        }
    }
}

const directions = [[0,1], [1,0], [0,-1], [-1,0]];

while (queue.length > 0) {
    const [row, col] = queue.shift()!;

    for (const [dx, dy] of directions) {
        const newRow = row + dx;
        const newCol = col + dy;
        const key = `${newRow},${newCol}`;

        if (newRow >= 0 && newRow < m &&
            newCol >= 0 && newCol < n &&
            !visited.has(key)) {
            mat[newRow][newCol] = mat[row][col] + 1;
            visited.add(key);
            queue.push([newRow, newCol]);
        }
    }
}

return mat;
```

---

## Problem 8: Open the Lock

### Level 1
Each lock state is a node. Moving one wheel creates edge to new state.

### Level 2
BFS from "0000" to target. Each state has 8 neighbors (4 wheels × 2 directions).

### Level 3
```typescript
const dead = new Set(deadends);
if (dead.has("0000")) return -1;

const queue: [string, number][] = [["0000", 0]];
const visited = new Set<string>(["0000"]);

const getNeighbors = (state: string): string[] => {
    const neighbors: string[] = [];
    for (let i = 0; i < 4; i++) {
        const digit = parseInt(state[i]);
        const up = (digit + 1) % 10;
        const down = (digit + 9) % 10;
        neighbors.push(state.slice(0, i) + up + state.slice(i + 1));
        neighbors.push(state.slice(0, i) + down + state.slice(i + 1));
    }
    return neighbors;
};

while (queue.length > 0) {
    const [state, turns] = queue.shift()!;
    if (state === target) return turns;

    for (const neighbor of getNeighbors(state)) {
        if (!visited.has(neighbor) && !dead.has(neighbor)) {
            visited.add(neighbor);
            queue.push([neighbor, turns + 1]);
        }
    }
}

return -1;
```

---

## Problem 9: Minimum Knight Moves

### Level 1
Knight moves form graph. BFS finds minimum number of moves.

### Level 2
Use symmetry (abs values) to optimize. Be careful with boundary conditions.

### Level 3
```typescript
const directions = [
    [2,1], [1,2], [-1,2], [-2,1],
    [-2,-1], [-1,-2], [1,-2], [2,-1]
];

const queue: [number, number, number][] = [[0, 0, 0]];
const visited = new Set<string>(['0,0']);
x = Math.abs(x);
y = Math.abs(y);

while (queue.length > 0) {
    const [row, col, steps] = queue.shift()!;
    if (row === x && col === y) return steps;

    for (const [dx, dy] of directions) {
        const newRow = row + dx;
        const newCol = col + dy;
        const key = `${newRow},${newCol}`;

        if (!visited.has(key) && newRow >= -2 && newCol >= -2) {
            visited.add(key);
            queue.push([newRow, newCol, steps + 1]);
        }
    }
}

return -1;
```

---

## Problem 10: Shortest Bridge

### Level 1
Find one island first, then find shortest path to other island.

### Level 2
Use DFS to identify first island, then BFS from all cells of that island to find second.

### Level 3
```typescript
const n = grid.length;
const queue: [number, number][] = [];
let found = false;

// DFS to find and mark first island
const dfs = (row: number, col: number) => {
    if (row < 0 || row >= n || col < 0 || col >= n ||
        grid[row][col] !== 1) return;

    grid[row][col] = 2;
    queue.push([row, col]);

    dfs(row + 1, col);
    dfs(row - 1, col);
    dfs(row, col + 1);
    dfs(row, col - 1);
};

// Find first island
for (let i = 0; i < n && !found; i++) {
    for (let j = 0; j < n && !found; j++) {
        if (grid[i][j] === 1) {
            dfs(i, j);
            found = true;
        }
    }
}

// BFS to second island
const directions = [[0,1], [1,0], [0,-1], [-1,0]];
let steps = 0;

while (queue.length > 0) {
    const size = queue.length;
    for (let i = 0; i < size; i++) {
        const [row, col] = queue.shift()!;

        for (const [dx, dy] of directions) {
            const newRow = row + dx;
            const newCol = col + dy;

            if (newRow >= 0 && newRow < n &&
                newCol >= 0 && newCol < n) {
                if (grid[newRow][newCol] === 1) return steps;
                if (grid[newRow][newCol] === 0) {
                    grid[newRow][newCol] = 2;
                    queue.push([newRow, newCol]);
                }
            }
        }
    }
    steps++;
}

return steps;
```

---

## Pattern Hints

**"Spreading/infection"** → Multi-source BFS

**"Prerequisites/dependencies"** → Topological Sort

**"Shortest path/minimum steps"** → BFS

**"Level by level"** → BFS with level tracking

**"State transformation"** → State space BFS

---

## Using Hints Effectively

1. Try 10+ min before Level 1
2. Try 5+ min after each hint
3. If use Level 3, mark for review and retry similar later
4. Don't feel bad - hints are for learning

Goal: Learn pattern, not just solve one problem.

---

[Back to Problems](./PROBLEMS.md) | [Back to Solutions](./SOLUTIONS.md)
