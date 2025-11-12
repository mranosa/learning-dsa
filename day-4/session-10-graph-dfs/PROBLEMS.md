# Problems - Session 10: Graph DFS

10 problems in order. Use UMPIRE method.

**Targets:** Easy <15 min | Medium <30 min

---

## Problem 1: Number of Islands ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Grid DFS
**LeetCode:** https://leetcode.com/problems/number-of-islands/

### Problem

Given `m × n` 2D binary grid representing map of '1's (land) and '0's (water), return number of islands.

Island = surrounded by water, formed by connecting adjacent lands horizontally or vertically. All four edges surrounded by water.

### Examples

```
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

### Constraints

- m, n ≤ 300
- grid[i][j] is '0' or '1'

### Hints
- Each island is a connected component
- DFS to explore entire island when found
- Mark visited cells (modify grid or use Set)
- Count how many DFS calls needed

---

## Problem 2: Clone Graph ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Graph DFS
**LeetCode:** https://leetcode.com/problems/clone-graph/

### Problem

Given reference of node in connected undirected graph, return deep copy (clone) of the graph.

Each node contains value (int) and list of neighbors.

```typescript
class Node {
    val: number;
    neighbors: Node[];
}
```

### Examples

```
adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

Explanation: 4 nodes in graph.
Node 1: connects to 2, 4
Node 2: connects to 1, 3
Node 3: connects to 2, 4
Node 4: connects to 1, 3
```

### Constraints

- Nodes: 0 to 100
- 1 ≤ Node.val ≤ 100
- Unique values
- No repeated edges or self-loops
- Graph is connected

### Hints
- Use HashMap: original → clone
- Prevents duplicate clones
- Handles cycles
- If seen before, return existing clone

---

## Problem 3: Max Area of Island ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Grid DFS
**LeetCode:** https://leetcode.com/problems/max-area-of-island/

### Problem

Given `m × n` binary matrix `grid`. Island = group of 1's connected 4-directionally.

Area of island = number of cells with value 1 in island.

Return maximum area. If no island, return 0.

### Examples

```
grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6

grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

### Constraints

- m, n ≤ 50
- grid[i][j] is 0 or 1

### Hints
- Similar to Number of Islands
- DFS returns area count
- Area = 1 (current) + sum of 4 directions
- Track maximum area found

---

## Problem 4: Pacific Atlantic Water Flow ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Multi-source DFS
**LeetCode:** https://leetcode.com/problems/pacific-atlantic-water-flow/

### Problem

`m × n` rectangular island borders Pacific Ocean and Atlantic Ocean.

- Pacific: left and top edges
- Atlantic: right and bottom edges

Given `heights[r][c]` = height above sea level at (r, c).

Rain water flows to neighboring cells (N, S, E, W) if neighbor height ≤ current height. Water flows from any cell adjacent to ocean into ocean.

Return coordinates where rain water can flow to BOTH Pacific and Atlantic oceans.

### Examples

```
heights = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

### Constraints

- m, n ≤ 200
- 0 ≤ heights[i][j] ≤ 10⁵

### Hints
- Think backwards: from ocean to cells
- DFS from Pacific borders (top, left)
- DFS from Atlantic borders (bottom, right)
- Answer = intersection of both sets
- When going backwards: can move to cell if height ≥ current

---

## Problem 5: Surrounded Regions ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Border DFS
**LeetCode:** https://leetcode.com/problems/surrounded-regions/

### Problem

Given `m × n` matrix `board` containing 'X' and 'O', capture all regions 4-directionally surrounded by 'X'.

Region captured by flipping all 'O's into 'X's in that surrounded region.

### Examples

```
board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]
Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]

Explanation: Surrounded regions not on border.
O on bottom is on border, so not captured.
```

### Constraints

- m, n ≤ 200
- board[i][j] is 'X' or 'O'

### Hints
- O's on border or connected to border cannot be surrounded
- DFS from all border O's, mark as "safe"
- Convert remaining O's to X's
- Convert safe marks back to O's

---

## Problem 6: Flood Fill

**Difficulty:** Easy | **Pattern:** Grid DFS
**LeetCode:** https://leetcode.com/problems/flood-fill/

### Problem

Image = `m × n` integer grid `image[i][j]` = pixel value.

Given three integers `sr`, `sc`, and `newColor`. Perform flood fill starting from pixel `image[sr][sc]`.

Flood fill: Consider starting pixel + any pixels connected 4-directionally of same color as starting pixel, and so on. Replace color of all with `newColor`.

### Examples

```
image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
```

### Constraints

- m, n ≤ 50
- 0 ≤ image[i][j], newColor < 2¹⁶

### Hints
- Basic DFS problem
- Edge case: if newColor == originalColor → infinite loop
- Store original color first
- DFS changes all connected pixels with original color

---

## Problem 7: Number of Connected Components in Undirected Graph

**Difficulty:** Medium | **Pattern:** Connected Components
**LeetCode:** https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/ (Premium)

### Problem

Graph of `n` nodes. Given integer `n` and array `edges` where `edges[i] = [ai, bi]` indicates edge between ai and bi.

Return number of connected components in graph.

### Examples

```
n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Explanation: Nodes 0,1,2 connected. Nodes 3,4 connected.

n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
Explanation: All nodes connected.
```

### Constraints

- 1 ≤ n ≤ 2000
- 0 ≤ edges.length ≤ 5000
- edges[i].length == 2
- 0 ≤ ai, bi < n
- ai ≠ bi
- No duplicate edges

### Hints
- Build adjacency list from edges
- Track visited set
- For each unvisited node, start DFS and increment counter
- DFS marks all reachable nodes as visited

---

## Problem 8: Word Search ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** DFS + Backtracking
**LeetCode:** https://leetcode.com/problems/word-search/

### Problem

Given `m × n` grid `board` and string `word`, return `true` if `word` exists in grid.

Word constructed from sequentially adjacent cells (horizontal/vertical). Same letter cell cannot be used more than once.

### Examples

```
board = [
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
], word = "ABCCED"
Output: true

board = [
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
], word = "SEE"
Output: true

board = [
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
], word = "ABCB"
Output: false
```

### Constraints

- m, n ≤ 6
- 1 ≤ word.length ≤ 15
- board and word contain only lowercase and uppercase English letters

### Hints
- Try starting from each cell matching first character
- Use backtracking: mark visited during exploration, unmark when backtracking
- Track index in word
- Temporarily mark cell as visited (e.g., change to '#')

---

## Problem 9: All Paths From Source to Target

**Difficulty:** Medium | **Pattern:** Path Enumeration
**LeetCode:** https://leetcode.com/problems/all-paths-from-source-to-target/

### Problem

Given directed acyclic graph (DAG) of `n` nodes labeled 0 to n-1, find all possible paths from node 0 to node n-1. Return in any order.

Graph given as: `graph[i]` = list of all nodes you can visit from node i (directed edge from i to graph[i][j]).

### Examples

```
graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: Two paths: 0 → 1 → 3 and 0 → 2 → 3

graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
```

### Constraints

- n ≤ 15
- 0 ≤ graph[i][j] < n
- All graph[i][j] unique
- Input is DAG (no cycles)

### Hints
- Path enumeration problem
- No visited set needed (DAG = no cycles)
- Build path during traversal
- Copy path when adding to result
- Backtrack after exploring

---

## Problem 10: Detect Cycle in Undirected Graph

**Difficulty:** Medium | **Pattern:** Cycle Detection
**LeetCode:** Similar to https://leetcode.com/problems/graph-valid-tree/ (Premium)

### Problem

Given `n` nodes labeled 0 to n-1 and list of undirected edges (each edge = pair of nodes), check if graph contains cycle.

### Examples

```
n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: false
Explanation: Valid tree, no cycles.

n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: true
Explanation: Cycle: 1 → 2 → 3 → 1

n = 4, edges = [[0,1],[2,3]]
Output: false
Explanation: Two disconnected components, no cycle.
```

### Constraints

- 1 ≤ n ≤ 2000
- 0 ≤ edges.length ≤ 5000

### Hints
- Build adjacency list
- Use DFS with parent tracking
- If visit node that's already visited AND not parent → cycle
- Check all disconnected components

---

## Summary

**Total:** 10 problems (1 Easy, 9 Medium)

**Patterns:**
- Grid Traversal (4-directional)
- Connected Components
- Cycle Detection
- Path Finding
- Backtracking

**Blind 75:** 6/75 problems (8%)

**Solving Order:**
1. Flood Fill (Easy - warmup)
2. Number of Islands (classic)
3. Max Area of Island (variant)
4. Clone Graph (graph structure)
5. Connected Components (counting)
6. Detect Cycle (parent tracking)
7. Surrounded Regions (border DFS)
8. Pacific Atlantic (multi-source)
9. Word Search (backtracking)
10. All Paths (path enumeration)

---

**Ready?** Say: `"Claude, give me the problem"` or `"Go"`

[Solutions](./SOLUTIONS.md) | [Hints](./HINTS.md)
