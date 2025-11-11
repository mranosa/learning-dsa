# Solutions: Graph BFS

## Problem 1: Rotting Oranges

### Solution 1: Multi-Source BFS
```typescript
function orangesRotting(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    const queue: [number, number][] = [];
    let freshCount = 0;

    // Find all rotten oranges and count fresh ones
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 2) {
                queue.push([i, j]);
            } else if (grid[i][j] === 1) {
                freshCount++;
            }
        }
    }

    // No fresh oranges to rot
    if (freshCount === 0) return 0;

    const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    let minutes = 0;

    // BFS to rot oranges
    while (queue.length > 0 && freshCount > 0) {
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
                    freshCount--;
                    queue.push([newRow, newCol]);
                }
            }
        }

        minutes++;
    }

    return freshCount === 0 ? minutes : -1;
}

// Time: O(m × n) - visit each cell at most once
// Space: O(m × n) - worst case all cells in queue
```

---

## Problem 2: Course Schedule

### Solution 1: Topological Sort (Kahn's Algorithm)
```typescript
function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    // Build adjacency list and in-degree array
    const graph = new Map<number, number[]>();
    const inDegree = new Array(numCourses).fill(0);

    for (const [course, prereq] of prerequisites) {
        if (!graph.has(prereq)) graph.set(prereq, []);
        graph.get(prereq)!.push(course);
        inDegree[course]++;
    }

    // Find all courses with no prerequisites
    const queue: number[] = [];
    for (let i = 0; i < numCourses; i++) {
        if (inDegree[i] === 0) {
            queue.push(i);
        }
    }

    let coursesCompleted = 0;

    while (queue.length > 0) {
        const course = queue.shift()!;
        coursesCompleted++;

        // Process dependent courses
        for (const nextCourse of graph.get(course) || []) {
            inDegree[nextCourse]--;
            if (inDegree[nextCourse] === 0) {
                queue.push(nextCourse);
            }
        }
    }

    return coursesCompleted === numCourses;
}

// Time: O(V + E) where V = numCourses, E = prerequisites.length
// Space: O(V + E) for graph and queue
```

### Solution 2: DFS Cycle Detection
```typescript
function canFinishDFS(numCourses: number, prerequisites: number[][]): boolean {
    const graph = new Map<number, number[]>();

    for (const [course, prereq] of prerequisites) {
        if (!graph.has(prereq)) graph.set(prereq, []);
        graph.get(prereq)!.push(course);
    }

    const visited = new Set<number>();
    const visiting = new Set<number>();

    function hasCycle(course: number): boolean {
        if (visiting.has(course)) return true;
        if (visited.has(course)) return false;

        visiting.add(course);

        for (const next of graph.get(course) || []) {
            if (hasCycle(next)) return true;
        }

        visiting.delete(course);
        visited.add(course);
        return false;
    }

    for (let i = 0; i < numCourses; i++) {
        if (hasCycle(i)) return false;
    }

    return true;
}

// Time: O(V + E)
// Space: O(V + E)
```

---

## Problem 3: Course Schedule II

### Solution 1: Topological Sort with Order Tracking
```typescript
function findOrder(numCourses: number, prerequisites: number[][]): number[] {
    const graph = new Map<number, number[]>();
    const inDegree = new Array(numCourses).fill(0);

    for (const [course, prereq] of prerequisites) {
        if (!graph.has(prereq)) graph.set(prereq, []);
        graph.get(prereq)!.push(course);
        inDegree[course]++;
    }

    const queue: number[] = [];
    for (let i = 0; i < numCourses; i++) {
        if (inDegree[i] === 0) {
            queue.push(i);
        }
    }

    const result: number[] = [];

    while (queue.length > 0) {
        const course = queue.shift()!;
        result.push(course);

        for (const nextCourse of graph.get(course) || []) {
            inDegree[nextCourse]--;
            if (inDegree[nextCourse] === 0) {
                queue.push(nextCourse);
            }
        }
    }

    return result.length === numCourses ? result : [];
}

// Time: O(V + E)
// Space: O(V + E)
```

---

## Problem 4: Shortest Path in Binary Matrix

### Solution 1: 8-Directional BFS
```typescript
function shortestPathBinaryMatrix(grid: number[][]): number {
    const n = grid.length;

    // Check if start or end is blocked
    if (grid[0][0] === 1 || grid[n-1][n-1] === 1) return -1;

    // Single cell case
    if (n === 1) return 1;

    const directions = [
        [0, 1], [1, 0], [0, -1], [-1, 0],     // 4-directional
        [1, 1], [1, -1], [-1, 1], [-1, -1]    // diagonals
    ];

    const queue: [number, number, number][] = [[0, 0, 1]];
    const visited = new Set<string>();
    visited.add('0,0');

    while (queue.length > 0) {
        const [row, col, dist] = queue.shift()!;

        for (const [dx, dy] of directions) {
            const newRow = row + dx;
            const newCol = col + dy;
            const key = `${newRow},${newCol}`;

            if (newRow >= 0 && newRow < n &&
                newCol >= 0 && newCol < n &&
                grid[newRow][newCol] === 0 &&
                !visited.has(key)) {

                // Check if we reached the target
                if (newRow === n - 1 && newCol === n - 1) {
                    return dist + 1;
                }

                visited.add(key);
                queue.push([newRow, newCol, dist + 1]);
            }
        }
    }

    return -1;
}

// Time: O(n²) - visit each cell at most once
// Space: O(n²) - for visited set and queue
```

---

## Problem 5: Walls and Gates

### Solution 1: Multi-Source BFS from Gates
```typescript
function wallsAndGates(rooms: number[][]): void {
    const INF = 2147483647;
    const m = rooms.length;
    if (m === 0) return;
    const n = rooms[0].length;

    const queue: [number, number][] = [];

    // Find all gates
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (rooms[i][j] === 0) {
                queue.push([i, j]);
            }
        }
    }

    const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];

    while (queue.length > 0) {
        const [row, col] = queue.shift()!;

        for (const [dx, dy] of directions) {
            const newRow = row + dx;
            const newCol = col + dy;

            // If out of bounds or not an empty room, skip
            if (newRow < 0 || newRow >= m ||
                newCol < 0 || newCol >= n ||
                rooms[newRow][newCol] !== INF) {
                continue;
            }

            // Update distance
            rooms[newRow][newCol] = rooms[row][col] + 1;
            queue.push([newRow, newCol]);
        }
    }
}

// Time: O(m × n)
// Space: O(m × n) for queue in worst case
```

---

## Problem 6: Word Ladder

### Solution 1: BFS with Pattern Matching
```typescript
function ladderLength(beginWord: string, endWord: string, wordList: string[]): number {
    if (!wordList.includes(endWord)) return 0;

    // Build adjacency list using patterns
    const patternMap = new Map<string, string[]>();
    const allWords = [beginWord, ...wordList];

    for (const word of allWords) {
        for (let i = 0; i < word.length; i++) {
            const pattern = word.slice(0, i) + '*' + word.slice(i + 1);
            if (!patternMap.has(pattern)) {
                patternMap.set(pattern, []);
            }
            patternMap.get(pattern)!.push(word);
        }
    }

    const queue: [string, number][] = [[beginWord, 1]];
    const visited = new Set<string>([beginWord]);

    while (queue.length > 0) {
        const [word, level] = queue.shift()!;

        for (let i = 0; i < word.length; i++) {
            const pattern = word.slice(0, i) + '*' + word.slice(i + 1);

            for (const neighbor of patternMap.get(pattern) || []) {
                if (neighbor === endWord) {
                    return level + 1;
                }

                if (!visited.has(neighbor)) {
                    visited.add(neighbor);
                    queue.push([neighbor, level + 1]);
                }
            }
        }
    }

    return 0;
}

// Time: O(M² × N) where M = word length, N = number of words
// Space: O(M² × N)
```

### Solution 2: Bidirectional BFS
```typescript
function ladderLengthBidirectional(beginWord: string, endWord: string, wordList: string[]): number {
    if (!wordList.includes(endWord)) return 0;

    const wordSet = new Set(wordList);
    let beginSet = new Set([beginWord]);
    let endSet = new Set([endWord]);
    let visited = new Set<string>();
    let level = 1;

    while (beginSet.size > 0 && endSet.size > 0) {
        // Always expand the smaller set
        if (beginSet.size > endSet.size) {
            [beginSet, endSet] = [endSet, beginSet];
        }

        const nextSet = new Set<string>();

        for (const word of beginSet) {
            const chars = word.split('');

            for (let i = 0; i < chars.length; i++) {
                const original = chars[i];

                for (let c = 97; c <= 122; c++) {
                    chars[i] = String.fromCharCode(c);
                    const newWord = chars.join('');

                    if (endSet.has(newWord)) {
                        return level + 1;
                    }

                    if (wordSet.has(newWord) && !visited.has(newWord)) {
                        visited.add(newWord);
                        nextSet.add(newWord);
                    }
                }

                chars[i] = original;
            }
        }

        beginSet = nextSet;
        level++;
    }

    return 0;
}

// Time: O(M × N) where M = word length, N = number of words
// Space: O(M × N)
```

---

## Problem 7: 01 Matrix

### Solution 1: Multi-Source BFS from All Zeros
```typescript
function updateMatrix(mat: number[][]): number[][] {
    const m = mat.length, n = mat[0].length;
    const distances = Array(m).fill(0).map(() => Array(n).fill(-1));
    const queue: [number, number][] = [];

    // Initialize with all 0s
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (mat[i][j] === 0) {
                distances[i][j] = 0;
                queue.push([i, j]);
            }
        }
    }

    const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];

    while (queue.length > 0) {
        const [row, col] = queue.shift()!;

        for (const [dx, dy] of directions) {
            const newRow = row + dx;
            const newCol = col + dy;

            if (newRow >= 0 && newRow < m &&
                newCol >= 0 && newCol < n &&
                distances[newRow][newCol] === -1) {

                distances[newRow][newCol] = distances[row][col] + 1;
                queue.push([newRow, newCol]);
            }
        }
    }

    return distances;
}

// Time: O(m × n)
// Space: O(m × n)
```

---

## Problem 8: Open the Lock

### Solution 1: BFS State Space Exploration
```typescript
function openLock(deadends: string[], target: string): number {
    const dead = new Set(deadends);
    if (dead.has("0000")) return -1;
    if (target === "0000") return 0;

    const queue: [string, number][] = [["0000", 0]];
    const visited = new Set<string>(["0000"]);

    while (queue.length > 0) {
        const [current, turns] = queue.shift()!;

        // Try all possible next states
        for (let i = 0; i < 4; i++) {
            const digit = parseInt(current[i]);

            // Try both directions (up and down)
            for (const delta of [-1, 1]) {
                const newDigit = (digit + delta + 10) % 10;
                const newState = current.slice(0, i) + newDigit + current.slice(i + 1);

                if (newState === target) {
                    return turns + 1;
                }

                if (!dead.has(newState) && !visited.has(newState)) {
                    visited.add(newState);
                    queue.push([newState, turns + 1]);
                }
            }
        }
    }

    return -1;
}

// Time: O(10⁴ × 4 × 2) = O(10⁴) - bounded by possible states
// Space: O(10⁴) for visited set
```

---

## Problem 9: Minimum Knight Moves

### Solution 1: BFS with Pruning
```typescript
function minKnightMoves(x: number, y: number): number {
    // Use symmetry to reduce search space
    x = Math.abs(x);
    y = Math.abs(y);

    const moves = [
        [2, 1], [1, 2], [-1, 2], [-2, 1],
        [-2, -1], [-1, -2], [1, -2], [2, -1]
    ];

    const queue: [number, number, number][] = [[0, 0, 0]];
    const visited = new Set<string>(['0,0']);

    while (queue.length > 0) {
        const [curX, curY, steps] = queue.shift()!;

        if (curX === x && curY === y) {
            return steps;
        }

        for (const [dx, dy] of moves) {
            const newX = curX + dx;
            const newY = curY + dy;
            const key = `${newX},${newY}`;

            // Prune: don't go too far negative
            if (!visited.has(key) && newX >= -2 && newY >= -2) {
                visited.add(key);
                queue.push([newX, newY, steps + 1]);
            }
        }
    }

    return -1;
}

// Time: O(max(|x|, |y|)²)
// Space: O(max(|x|, |y|)²)
```

---

## Problem 10: Shortest Bridge

### Solution 1: DFS + BFS
```typescript
function shortestBridge(grid: number[][]): number {
    const n = grid.length;
    const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];

    // Find first island using DFS
    const firstIsland: [number, number][] = [];

    function dfs(row: number, col: number): void {
        if (row < 0 || row >= n || col < 0 || col >= n || grid[row][col] !== 1) {
            return;
        }

        grid[row][col] = 2; // Mark as visited
        firstIsland.push([row, col]);

        for (const [dx, dy] of directions) {
            dfs(row + dx, col + dy);
        }
    }

    // Find and mark first island
    outer: for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                dfs(i, j);
                break outer;
            }
        }
    }

    // BFS from first island to find second island
    const queue: [number, number, number][] = [];
    const visited = new Set<string>();

    for (const [row, col] of firstIsland) {
        queue.push([row, col, 0]);
        visited.add(`${row},${col}`);
    }

    while (queue.length > 0) {
        const [row, col, dist] = queue.shift()!;

        for (const [dx, dy] of directions) {
            const newRow = row + dx;
            const newCol = col + dy;
            const key = `${newRow},${newCol}`;

            if (newRow >= 0 && newRow < n &&
                newCol >= 0 && newCol < n &&
                !visited.has(key)) {

                if (grid[newRow][newCol] === 1) {
                    return dist;
                }

                visited.add(key);
                queue.push([newRow, newCol, dist + 1]);
            }
        }
    }

    return -1;
}

// Time: O(n²) - DFS + BFS both visit each cell once
// Space: O(n²) for queue and visited set
```