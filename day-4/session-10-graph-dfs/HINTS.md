# Hints - Session 10: Graph DFS

Progressive hints for 10 problems. Struggling is part of learning.

---

## Problem 1: Number of Islands

### Level 1
Think of each island as a connected component in a graph. How can you explore all land cells connected to a starting point?

### Level 2
Use DFS to explore each island completely. When you find a '1', increment island count and use DFS to mark all connected '1's as visited. Either:
- Modify grid in-place (change '1' to '0')
- Use separate visited set

### Level 3
```typescript
// Pseudocode:
islands = 0

for each cell in grid:
    if cell is '1':
        islands++
        dfs(cell) // Mark entire island as visited

function dfs(row, col):
    if out of bounds or water: return
    grid[row][col] = '0'  // Mark visited
    dfs(row+1, col), dfs(row-1, col), dfs(row, col+1), dfs(row, col-1)
```

---

## Problem 2: Clone Graph

### Level 1
Need deep copy. How to avoid infinite loops when graph has cycles? What data structure tracks already cloned nodes?

### Level 2
Use HashMap to map original nodes to their clones. Serves two purposes:
1. Avoid creating duplicate clones
2. Handle cycles in graph

When encounter node: check if already cloned. If yes, return clone; if no, create new clone and recursively clone neighbors.

### Level 3
```typescript
const cloned = new Map<Node, Node>();

function dfs(node):
    if (cloned.has(node)): return cloned.get(node)

    clone = new Node(node.val)
    cloned.set(node, clone)

    for neighbor in node.neighbors:
        clone.neighbors.push(dfs(neighbor))

    return clone
```

---

## Problem 3: Max Area of Island

### Level 1
Similar to Number of Islands, but instead of just counting, track the size of each island. How can you modify DFS to return area?

### Level 2
Make DFS return the area of island it explores. Area is:
- 1 (for current cell) + area from exploring all 4 directions
- 0 if cell is water or out of bounds

Keep track of maximum area found.

### Level 3
```typescript
maxArea = 0

for each cell:
    if cell is 1:
        area = dfs(row, col)
        maxArea = max(maxArea, area)

function dfs(row, col):
    if out of bounds or water: return 0
    grid[row][col] = 0  // Mark visited

    area = 1  // Current cell
    area += dfs(row+1, col)
    area += dfs(row-1, col)
    area += dfs(row, col+1)
    area += dfs(row, col-1)

    return area
```

---

## Problem 4: Pacific Atlantic Water Flow

### Level 1
Instead of checking from each cell if water can reach both oceans, think backwards: which cells can be reached FROM each ocean? Water flows from higher to equal/lower heights.

### Level 2
Run DFS from all Pacific border cells (top row and left column) to find all cells reachable from Pacific. Do same for Atlantic (bottom row and right column). Answer = cells that appear in both sets.

When doing DFS from ocean, can move to neighbor if height >= current height (water flows uphill when going backwards).

### Level 3
```typescript
pacific = new Set()
atlantic = new Set()

// DFS from Pacific borders
for each cell in top row: dfs(cell, pacific)
for each cell in left column: dfs(cell, pacific)

// DFS from Atlantic borders
for each cell in bottom row: dfs(cell, atlantic)
for each cell in right column: dfs(cell, atlantic)

// Find intersection
for each cell:
    if cell in pacific AND atlantic:
        result.push(cell)

function dfs(row, col, visited, prevHeight):
    if out of bounds or visited or height < prevHeight: return
    visited.add(cell)
    // Explore 4 directions with current height
```

---

## Problem 5: Surrounded Regions

### Level 1
O's on border or connected to border cannot be surrounded. How can you identify and protect these O's before flipping the rest?

### Level 2
1. Run DFS from all border O's and mark as "safe" (use temporary marker like 'S')
2. After marking all safe O's, iterate through board:
   - Change remaining O's to X's (surrounded)
   - Change S's back to O's (safe)

### Level 3
```typescript
// Step 1: Mark border-connected O's as safe
for each border cell:
    if cell is 'O': dfs(cell)  // Changes O to S

function dfs(row, col):
    if out of bounds or not 'O': return
    board[row][col] = 'S'  // Mark safe
    // Explore 4 directions

// Step 2: Final pass
for each cell:
    if cell is 'O': change to 'X'  // Surrounded
    if cell is 'S': change to 'O'  // Safe
```

---

## Problem 6: Flood Fill

### Level 1
Straightforward DFS problem. Start from given pixel and change all connected pixels of same color to new color.

### Level 2
Be careful of edge case: if new color same as original color, don't need to do anything (and you'd get infinite recursion if you tried).

Store original color, then use DFS to change all connected pixels with that color to new color.

### Level 3
```typescript
originalColor = image[sr][sc]

// Edge case: same color
if originalColor == newColor: return image

dfs(sr, sc)

function dfs(row, col):
    if out of bounds or image[row][col] != originalColor: return

    image[row][col] = newColor
    // Explore 4 directions
```

---

## Problem 7: Number of Connected Components

### Level 1
Build adjacency list from edges, then count how many times you need to start a new DFS to visit all nodes.

### Level 2
1. Create adjacency list representation of graph
2. Keep visited set
3. For each unvisited node, start DFS and increment component count
4. DFS should mark all reachable nodes as visited

### Level 3
```typescript
// Build adjacency list
graph = new Map()
for i from 0 to n-1: graph[i] = []
for each edge [a, b]:
    graph[a].push(b)
    graph[b].push(a)

// Count components
visited = new Set()
components = 0

for i from 0 to n-1:
    if i not in visited:
        components++
        dfs(i, visited, graph)

return components
```

---

## Problem 8: Word Search

### Level 1
Try starting from each cell matching first character. Use backtracking - mark cells as visited during exploration, then unmark when backtracking.

### Level 2
Use DFS with index parameter tracking position in word. At each step:
1. Check if current cell matches word[index]
2. Temporarily mark cell as visited (change to '#')
3. Explore 4 directions with index+1
4. Restore original value (backtrack)

### Level 3
```typescript
function exist(board, word):
    for each cell:
        if dfs(row, col, 0): return true
    return false

function dfs(row, col, index):
    if index == word.length: return true  // Found word
    if out of bounds or board[row][col] != word[index]: return false

    // Temporarily mark visited
    temp = board[row][col]
    board[row][col] = '#'

    // Try all 4 directions
    found = dfs(row+1, col, index+1) ||
            dfs(row-1, col, index+1) ||
            dfs(row, col+1, index+1) ||
            dfs(row, col-1, index+1)

    // Backtrack
    board[row][col] = temp

    return found
```

---

## Problem 9: All Paths From Source to Target

### Level 1
Path enumeration problem. Use DFS to explore all paths from node 0 to node n-1. Since it's DAG, don't need to worry about cycles.

### Level 2
Build current path as you traverse. When reach target node, add current path to result. Remember to:
- Add current node to path before exploring
- Remove it after exploring (backtracking)
- Or create new path array for each recursive call

### Level 3
```typescript
result = []
target = graph.length - 1

function dfs(node, path):
    path.push(node)

    if node == target:
        result.push([...path])  // Found path
    else:
        for neighbor in graph[node]:
            dfs(neighbor, path)

    path.pop()  // Backtrack

dfs(0, [])
return result
```

---

## Problem 10: Detect Cycle in Undirected Graph

### Level 1
In undirected graph, cycle exists if you visit node that's already been visited AND it's not parent of current node.

### Level 2
Build adjacency list, then use DFS with parent tracking:
- If encounter unvisited neighbor, continue DFS
- If encounter visited neighbor that's not parent, found cycle
- Check all disconnected components

### Level 3
```typescript
// Build adjacency list
graph = buildGraph(n, edges)
visited = new Set()

function dfs(node, parent):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor, node): return true  // Found cycle in subtree
        else if neighbor != parent:  // Back edge (cycle)
            return true

    return false

// Check all components
for i from 0 to n-1:
    if i not in visited:
        if dfs(i, -1): return true

return false
```

---

## Pattern Hints

**"Count islands/components"** → DFS from each unvisited cell/node, count starts

**"Max/min area"** → DFS returns size/area, track maximum

**"Can reach both X and Y"** → Multi-source DFS from X and Y, find intersection

**"Connected to border"** → DFS from all border cells, mark as safe

**"Find all paths"** → DFS with path tracking, backtracking

**"Detect cycle"** → DFS with parent/state tracking

**"Clone/copy structure"** → DFS with HashMap to track clones

---

## Using Hints Effectively

1. Try 10+ min before Level 1
2. Try 5+ min after each hint
3. If use Level 3, mark for review and retry similar later
4. Don't feel bad - hints are for learning

Goal: Learn pattern, not just solve one problem.

---

[Back to Problems](./PROBLEMS.md) | [Back to Solutions](./SOLUTIONS.md)
