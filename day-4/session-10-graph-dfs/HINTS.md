# Hints: Graph DFS

## Problem 1: Number of Islands

### Hint Level 1 (Gentle nudge)
Think of each island as a connected component in a graph. How can you explore all land cells connected to a starting point?

### Hint Level 2 (Directed guidance)
Use DFS to explore each island completely. When you find a '1', increment your island count and use DFS to mark all connected '1's as visited. You can either:
- Modify the grid in-place (change '1' to '0')
- Use a separate visited set

### Hint Level 3 (Detailed approach)
```typescript
// Pseudocode structure:
function numIslands(grid):
    islands = 0

    for each cell in grid:
        if cell is '1':
            islands++
            dfs(cell) // Mark entire island as visited

    return islands

function dfs(row, col):
    // Base case: out of bounds or water
    if invalid: return

    // Mark as visited
    grid[row][col] = '0'

    // Explore 4 directions
    dfs(row+1, col), dfs(row-1, col), dfs(row, col+1), dfs(row, col-1)
```

---

## Problem 2: Clone Graph

### Hint Level 1 (Gentle nudge)
You need to create a deep copy. Think about how to avoid infinite loops when the graph has cycles. What data structure can help you track already cloned nodes?

### Hint Level 2 (Directed guidance)
Use a HashMap to map original nodes to their clones. This serves two purposes:
1. Avoid creating duplicate clones
2. Handle cycles in the graph

When you encounter a node, check if it's already cloned. If yes, return the clone; if no, create a new clone and recursively clone its neighbors.

### Hint Level 3 (Detailed approach)
```typescript
// Use a Map to track cloned nodes
const cloned = new Map<Node, Node>();

function dfs(node):
    // Already cloned? Return the clone
    if (cloned.has(node)):
        return cloned.get(node)

    // Create clone
    clone = new Node(node.val)
    cloned.set(node, clone)

    // Clone all neighbors
    for neighbor in node.neighbors:
        clone.neighbors.push(dfs(neighbor))

    return clone
```

---

## Problem 3: Max Area of Island

### Hint Level 1 (Gentle nudge)
This is similar to Number of Islands, but instead of just counting islands, you need to track the size of each island. How can you modify the DFS to return the area?

### Hint Level 2 (Directed guidance)
Make your DFS function return the area of the island it explores. The area is:
- 1 (for current cell) + area from exploring all 4 directions
- 0 if the cell is water or out of bounds

Keep track of the maximum area found across all islands.

### Hint Level 3 (Detailed approach)
```typescript
function maxAreaOfIsland(grid):
    maxArea = 0

    for each cell in grid:
        if cell is 1:
            area = dfs(row, col)
            maxArea = max(maxArea, area)

    return maxArea

function dfs(row, col):
    if out of bounds or water:
        return 0

    grid[row][col] = 0  // Mark as visited

    area = 1  // Current cell
    area += dfs(row+1, col)  // Add area from each direction
    area += dfs(row-1, col)
    area += dfs(row, col+1)
    area += dfs(row, col-1)

    return area
```

---

## Problem 4: Pacific Atlantic Water Flow

### Hint Level 1 (Gentle nudge)
Instead of checking from each cell if water can reach both oceans, think backwards: which cells can be reached FROM each ocean? Water flows from higher to equal/lower heights.

### Hint Level 2 (Directed guidance)
Run DFS from all Pacific border cells (top row and left column) to find all cells reachable from Pacific. Do the same for Atlantic (bottom row and right column). The answer is cells that appear in both sets.

When doing DFS from ocean, you can move to a neighbor if its height is >= current height (water flows uphill when going backwards).

### Hint Level 3 (Detailed approach)
```typescript
// Two separate DFS explorations
pacific = new Set()
atlantic = new Set()

// DFS from Pacific borders
for each cell in top row: dfs(cell, pacific)
for each cell in left column: dfs(cell, pacific)

// DFS from Atlantic borders
for each cell in bottom row: dfs(cell, atlantic)
for each cell in right column: dfs(cell, atlantic)

// Find intersection
result = []
for each cell:
    if cell in pacific AND atlantic:
        result.push(cell)

// DFS function
function dfs(row, col, visited, prevHeight):
    if out of bounds or visited or height < prevHeight:
        return
    visited.add(cell)
    // Explore 4 directions with current height
```

---

## Problem 5: Surrounded Regions

### Hint Level 1 (Gentle nudge)
O's that are on the border or connected to the border cannot be surrounded. How can you identify and protect these O's before flipping the rest?

### Hint Level 2 (Directed guidance)
1. Run DFS from all border O's and mark them as "safe" (use a temporary marker like 'S')
2. After marking all safe O's, iterate through the board:
   - Change remaining O's to X's (these are surrounded)
   - Change S's back to O's (these are safe)

### Hint Level 3 (Detailed approach)
```typescript
// Step 1: Mark border-connected O's as safe
for each border cell:
    if cell is 'O':
        dfs(cell)  // Changes O to S

function dfs(row, col):
    if out of bounds or not 'O': return
    board[row][col] = 'S'  // Mark as safe
    // Explore 4 directions

// Step 2: Final pass
for each cell:
    if cell is 'O': change to 'X'  // Surrounded
    if cell is 'S': change to 'O'  // Safe
```

---

## Problem 6: Flood Fill

### Hint Level 1 (Gentle nudge)
This is a straightforward DFS problem. Start from the given pixel and change all connected pixels of the same color to the new color.

### Hint Level 2 (Directed guidance)
Be careful of one edge case: if the new color is the same as the original color, you don't need to do anything (and you'd get infinite recursion if you tried).

Store the original color, then use DFS to change all connected pixels with that color to the new color.

### Hint Level 3 (Detailed approach)
```typescript
function floodFill(image, sr, sc, newColor):
    originalColor = image[sr][sc]

    // Edge case: same color
    if originalColor == newColor: return image

    dfs(sr, sc)
    return image

function dfs(row, col):
    if out of bounds or image[row][col] != originalColor:
        return

    image[row][col] = newColor
    // Explore 4 directions
```

---

## Problem 7: Number of Connected Components

### Hint Level 1 (Gentle nudge)
Build an adjacency list from the edges, then count how many times you need to start a new DFS to visit all nodes.

### Hint Level 2 (Directed guidance)
1. Create an adjacency list representation of the graph
2. Keep a visited set
3. For each unvisited node, start a DFS and increment component count
4. The DFS should mark all reachable nodes as visited

### Hint Level 3 (Detailed approach)
```typescript
// Build adjacency list
graph = new Map()
for i from 0 to n-1:
    graph[i] = []
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

### Hint Level 1 (Gentle nudge)
Try starting from each cell that matches the first character of the word. Use backtracking - mark cells as visited during exploration, then unmark them when backtracking.

### Hint Level 2 (Directed guidance)
Use DFS with an index parameter tracking your position in the word. At each step:
1. Check if current cell matches word[index]
2. Temporarily mark the cell as visited (e.g., change to '#')
3. Explore 4 directions with index+1
4. Restore the original value (backtrack)

### Hint Level 3 (Detailed approach)
```typescript
function exist(board, word):
    for each cell:
        if dfs(row, col, 0): return true
    return false

function dfs(row, col, index):
    if index == word.length: return true  // Found word
    if out of bounds or board[row][col] != word[index]: return false

    // Temporarily mark as visited
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

### Hint Level 1 (Gentle nudge)
This is a path enumeration problem. Use DFS to explore all paths from node 0 to node n-1. Since it's a DAG, you don't need to worry about cycles.

### Hint Level 2 (Directed guidance)
Build the current path as you traverse. When you reach the target node, add the current path to your result. Remember to:
- Add the current node to the path before exploring
- Remove it after exploring (backtracking)
- Or create a new path array for each recursive call

### Hint Level 3 (Detailed approach)
```typescript
function allPaths(graph):
    result = []
    target = graph.length - 1

    function dfs(node, path):
        path.push(node)

        if node == target:
            result.push([...path])  // Found a path
        else:
            for neighbor in graph[node]:
                dfs(neighbor, path)

        path.pop()  // Backtrack

    dfs(0, [])
    return result
```

---

## Problem 10: Detect Cycle in Undirected Graph

### Hint Level 1 (Gentle nudge)
In an undirected graph, a cycle exists if you visit a node that's already been visited AND it's not the parent of the current node.

### Hint Level 2 (Directed guidance)
Build an adjacency list, then use DFS with parent tracking:
- If you encounter an unvisited neighbor, continue DFS
- If you encounter a visited neighbor that's not your parent, you found a cycle
- Check all disconnected components

### Hint Level 3 (Detailed approach)
```typescript
// Build adjacency list
graph = buildGraph(n, edges)
visited = new Set()

function dfs(node, parent):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor, node):  // Found cycle in subtree
                return true
        else if neighbor != parent:  // Back edge (cycle)
            return true

    return false

// Check all components
for i from 0 to n-1:
    if i not in visited:
        if dfs(i, -1): return true

return false
```