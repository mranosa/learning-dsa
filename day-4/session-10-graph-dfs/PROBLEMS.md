# Problems: Graph DFS

## Problem 1: Number of Islands
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/number-of-islands/

Given an `m x n` 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

```typescript
function numIslands(grid: string[][]): number {
    // Your code here
}

// Example 1:
// Input: grid = [
//   ["1","1","1","1","0"],
//   ["1","1","0","1","0"],
//   ["1","1","0","0","0"],
//   ["0","0","0","0","0"]
// ]
// Output: 1

// Example 2:
// Input: grid = [
//   ["1","1","0","0","0"],
//   ["1","1","0","0","0"],
//   ["0","0","1","0","0"],
//   ["0","0","0","1","1"]
// ]
// Output: 3
```

---

## Problem 2: Clone Graph
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

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
    // Your code here
}

// Example:
// Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
// Output: [[2,4],[1,3],[2,4],[1,3]]
// Explanation: There are 4 nodes in the graph.
// Node 1 has value 1 and is connected to nodes 2 and 4.
// Node 2 has value 2 and is connected to nodes 1 and 3.
// Node 3 has value 3 and is connected to nodes 2 and 4.
// Node 4 has value 4 and is connected to nodes 1 and 3.
```

---

## Problem 3: Max Area of Island
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/max-area-of-island/

You are given an `m x n` binary matrix `grid`. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in `grid`. If there is no island, return 0.

```typescript
function maxAreaOfIsland(grid: number[][]): number {
    // Your code here
}

// Example 1:
// Input: grid = [
//   [0,0,1,0,0,0,0,1,0,0,0,0,0],
//   [0,0,0,0,0,0,0,1,1,1,0,0,0],
//   [0,1,1,0,1,0,0,0,0,0,0,0,0],
//   [0,1,0,0,1,1,0,0,1,0,1,0,0],
//   [0,1,0,0,1,1,0,0,1,1,1,0,0],
//   [0,0,0,0,0,0,0,0,0,0,1,0,0],
//   [0,0,0,0,0,0,0,1,1,1,0,0,0],
//   [0,0,0,0,0,0,0,1,1,0,0,0,0]
// ]
// Output: 6
// Explanation: The answer is not 11, because the island must be connected 4-directionally.

// Example 2:
// Input: grid = [[0,0,0,0,0,0,0,0]]
// Output: 0
```

---

## Problem 4: Pacific Atlantic Water Flow
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/pacific-atlantic-water-flow/

There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates `result` where `result[i] = [ri, ci]` denotes that rain water can flow from cell `(ri, ci)` to both the Pacific and Atlantic oceans.

```typescript
function pacificAtlantic(heights: number[][]): number[][] {
    // Your code here
}

// Example:
// Input: heights = [
//   [1,2,2,3,5],
//   [3,2,3,4,4],
//   [2,4,5,3,1],
//   [6,7,1,4,5],
//   [5,1,1,2,4]
// ]
// Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
// Explanation: The cells with coordinates can flow to both oceans.
```

---

## Problem 5: Surrounded Regions
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/surrounded-regions/

Given an `m x n` matrix `board` containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

```typescript
function solve(board: string[][]): void {
    // Your code here
}

// Example:
// Input: board = [
//   ["X","X","X","X"],
//   ["X","O","O","X"],
//   ["X","X","O","X"],
//   ["X","O","X","X"]
// ]
// Output: [
//   ["X","X","X","X"],
//   ["X","X","X","X"],
//   ["X","X","X","X"],
//   ["X","O","X","X"]
// ]
// Explanation: Surrounded regions should not be on the border.
// The 'O' on the bottom is on the border, so it is not captured.
```

---

## Problem 6: Flood Fill
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/flood-fill/

An image is represented by an `m x n` integer grid `image` where `image[i][j]` represents the pixel value of the image.

You are also given three integers `sr`, `sc`, and `newColor`. You should perform a flood fill on the image starting from the pixel `image[sr][sc]`.

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with `newColor`.

Return the modified image after performing the flood fill.

```typescript
function floodFill(image: number[][], sr: number, sc: number, newColor: number): number[][] {
    // Your code here
}

// Example 1:
// Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
// Output: [[2,2,2],[2,2,0],[2,0,1]]
// Explanation: From the center of the image with position (sr, sc) = (1, 1)
// (i.e., the red pixel), all pixels connected by a path of the same color as
// the starting pixel are colored with the new color.

// Example 2:
// Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
// Output: [[2,2,2],[2,2,2]]
```

---

## Problem 7: Number of Connected Components in an Undirected Graph
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/ (Premium)

You have a graph of `n` nodes. You are given an integer `n` and an array `edges` where `edges[i] = [ai, bi]` indicates that there is an edge between `ai` and `bi` in the graph.

Return the number of connected components in the graph.

```typescript
function countComponents(n: number, edges: number[][]): number {
    // Your code here
}

// Example 1:
// Input: n = 5, edges = [[0,1],[1,2],[3,4]]
// Output: 2
// Explanation: Node 0, 1, 2 are connected. Node 3, 4 are connected.

// Example 2:
// Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
// Output: 1
// Explanation: All nodes are connected.
```

---

## Problem 8: Word Search
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/word-search/

Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

```typescript
function exist(board: string[][], word: string): boolean {
    // Your code here
}

// Example 1:
// Input: board = [
//   ["A","B","C","E"],
//   ["S","F","C","S"],
//   ["A","D","E","E"]
// ], word = "ABCCED"
// Output: true

// Example 2:
// Input: board = [
//   ["A","B","C","E"],
//   ["S","F","C","S"],
//   ["A","D","E","E"]
// ], word = "SEE"
// Output: true

// Example 3:
// Input: board = [
//   ["A","B","C","E"],
//   ["S","F","C","S"],
//   ["A","D","E","E"]
// ], word = "ABCB"
// Output: false
```

---

## Problem 9: All Paths From Source to Target
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/all-paths-from-source-to-target/

Given a directed acyclic graph (DAG) of `n` nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: `graph[i]` is a list of all nodes you can visit from node `i` (i.e., there is a directed edge from node `i` to node `graph[i][j]`).

```typescript
function allPathsSourceTarget(graph: number[][]): number[][] {
    // Your code here
}

// Example 1:
// Input: graph = [[1,2],[3],[3],[]]
// Output: [[0,1,3],[0,2,3]]
// Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

// Example 2:
// Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
// Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
```

---

## Problem 10: Detect Cycle in an Undirected Graph
**Difficulty:** Medium
**LeetCode:** Similar to https://leetcode.com/problems/graph-valid-tree/ (Premium)

Given `n` nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), check whether the graph contains a cycle.

```typescript
function hasCycle(n: number, edges: number[][]): boolean {
    // Your code here
}

// Example 1:
// Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
// Output: false
// Explanation: It's a valid tree with no cycles.

// Example 2:
// Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
// Output: true
// Explanation: There is a cycle: 1 -> 2 -> 3 -> 1

// Example 3:
// Input: n = 4, edges = [[0,1],[2,3]]
// Output: false
// Explanation: Two disconnected components, no cycle.
```

---

## Problem Order Strategy

**Suggested solving order for learning:**
1. **Start with:** Flood Fill (Easy - basic DFS)
2. **Grid basics:** Number of Islands (classic problem)
3. **Track size:** Max Area of Island (extension of islands)
4. **Graph structure:** Clone Graph (understand graph representation)
5. **Components:** Number of Connected Components
6. **Cycle detection:** Detect Cycle in Undirected Graph
7. **Boundary DFS:** Surrounded Regions
8. **Multi-source:** Pacific Atlantic Water Flow
9. **Backtracking:** Word Search
10. **Path enumeration:** All Paths From Source to Target

---

## Time Limits

- Easy problems: 15 minutes
- Medium problems: 30 minutes
- Stop and check hints if stuck for >10 minutes
- Review solution even if you solve it

Good luck!