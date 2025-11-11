# Union-Find Hints

## 1. Number of Provinces

### Hint 1 (Gentle)
Think of this as counting disconnected groups in a graph. Each province is a connected component.

### Hint 2 (Directed)
Use Union-Find to merge cities that are directly connected. The final number of components is your answer.

### Hint 3 (Detailed)
1. Initialize Union-Find with n cities
2. For each pair (i, j) where isConnected[i][j] = 1, union(i, j)
3. Return the number of distinct components
4. Remember the matrix is symmetric, so process only upper triangle

---

## 2. Graph Valid Tree

### Hint 1 (Gentle)
A valid tree has two properties: it's connected (one component) and has no cycles. Also, a tree with n nodes has exactly n-1 edges.

### Hint 2 (Directed)
First check if edges.length === n-1. Then use Union-Find to detect cycles - if union returns false, there's a cycle.

### Hint 3 (Detailed)
1. If edges.length !== n-1, return false immediately
2. Initialize Union-Find with n nodes
3. For each edge, try to union the nodes
4. If union fails (nodes already connected), it's a cycle - return false
5. After processing all edges, check components === 1

---

## 3. Number of Connected Components

### Hint 1 (Gentle)
This is the most straightforward Union-Find problem. Just count how many separate groups exist after processing all edges.

### Hint 2 (Directed)
Union all connected nodes, then return the component count. The Union-Find structure tracks this automatically.

### Hint 3 (Detailed)
1. Initialize Union-Find with n nodes (components = n)
2. For each edge [u, v], call union(u, v)
3. Each successful union decreases component count by 1
4. Return the final component count

---

## 4. Redundant Connection

### Hint 1 (Gentle)
The redundant edge is the one that creates a cycle when added. Process edges in order and find which one connects already-connected nodes.

### Hint 2 (Directed)
Use Union-Find to track connectivity. When you try to union two nodes that are already connected, that edge is redundant.

### Hint 3 (Detailed)
1. Initialize Union-Find with n+1 size (nodes are 1-indexed)
2. Process edges in the given order
3. For each edge [u, v]:
   - If find(u) === find(v), this edge creates a cycle
   - Return this edge immediately
4. Otherwise, union(u, v) and continue

---

## 5. Accounts Merge

### Hint 1 (Gentle)
Think of each account as a node. If two accounts share an email, they belong to the same person and should be merged.

### Hint 2 (Directed)
Map each email to its first seen account index. When an email appears in another account, union those accounts.

### Hint 3 (Detailed)
1. Create emailToAccount map and emailToName map
2. For each account i:
   - For each email in account:
     - If email seen before, union(i, previousAccount)
     - Otherwise, map email to account i
3. Group emails by their root account (using find)
4. Sort emails in each group and format output

---

## 6. Most Stones Removed

### Hint 1 (Gentle)
Stones in the same row or column can be connected. The maximum stones you can remove equals total stones minus the number of connected components.

### Hint 2 (Directed)
Union stones that share rows or columns. Use the row and column indices as nodes in Union-Find. Be careful to avoid index collision.

### Hint 3 (Detailed)
1. For each stone at [x, y]:
   - Union row x with column y
   - Use ~y (bitwise NOT) for columns to avoid collision with rows
2. Count unique components (each component needs one stone to remain)
3. Return stones.length - componentCount
4. Use a Map-based Union-Find since indices can be large

---

## 7. Number of Operations to Make Network Connected

### Hint 1 (Gentle)
You need to connect all components. Count how many components exist and how many extra cables you have.

### Hint 2 (Directed)
If you have k components, you need k-1 cables to connect them all. Check if you have enough cables total (need >= n-1).

### Hint 3 (Detailed)
1. First check: if connections.length < n-1, return -1
2. Use Union-Find to count components
3. Each redundant connection (union returns false) is an extra cable
4. Operations needed = components - 1
5. You already have enough cables since you checked in step 1

---

## 8. Satisfiability of Equality Equations

### Hint 1 (Gentle)
Process equality equations first to group equal variables. Then check if any inequality equations contradict these groups.

### Hint 2 (Directed)
Two-pass approach: First union all variables in "==" equations. Then verify no "!=" equation has both variables in the same group.

### Hint 3 (Detailed)
1. Initialize Union-Find for 26 letters (a-z)
2. First pass: Process only "==" equations
   - Convert characters to indices (a=0, b=1, etc.)
   - Union the two variables
3. Second pass: Process "!=" equations
   - If find(x) === find(y) for x!=y, return false
4. If all checks pass, return true

---

## 9. Smallest String With Swaps

### Hint 1 (Gentle)
If indices can be swapped (directly or indirectly), their characters can be rearranged in any order. Find groups of swappable indices.

### Hint 2 (Directed)
Use Union-Find to group indices that can swap. Within each group, sort the characters to get the lexicographically smallest arrangement.

### Hint 3 (Detailed)
1. Union all pairs of indices that can swap
2. Group indices by their root (using find)
3. For each group:
   - Collect all characters at those indices
   - Sort the characters
   - Sort the indices
   - Place sorted characters at sorted indices
4. Build and return the result string

---

## 10. Evaluate Division

### Hint 1 (Gentle)
This is about finding paths and their products in a graph. While Union-Find can work, consider if a graph traversal might be simpler.

### Hint 2 (Directed)
Build a graph where a/b = value means edge from a to b with weight value, and b to a with weight 1/value. Use DFS to find paths.

### Hint 3 (Detailed)
For Weighted Union-Find approach:
1. Maintain parent and weight arrays
2. find(x) returns root and accumulates weights
3. union(a, b, value) sets a/b = value
4. For query c/d: if same root, return weight[c]/weight[d]

For Graph DFS approach (simpler):
1. Build bidirectional graph with weights
2. For each query, DFS from numerator to denominator
3. Multiply weights along the path
4. Return -1 if no path exists

---

## General Union-Find Tips

### Pattern Recognition
- "Connected components" → Union-Find
- "Groups" or "merge" → Union-Find
- "Detect cycle" in undirected graph → Union-Find
- "Check if connected" → Union-Find

### Implementation Tips
1. Always implement both optimizations:
   - Path compression in find()
   - Union by rank in union()
2. Track component count by decrementing on successful union
3. Use union return value to detect existing connections
4. Initialize parent[i] = i for all nodes

### Common Mistakes to Avoid
1. Forgetting path compression (causes TLE)
2. Not tracking component count correctly
3. Using 0-indexed Union-Find for 1-indexed problems
4. Not handling the case where nodes are already connected