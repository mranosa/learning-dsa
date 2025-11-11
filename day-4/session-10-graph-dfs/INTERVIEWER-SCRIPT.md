# Interviewer Script: Graph DFS

This script helps Claude guide candidates through graph DFS problems using the UMPIRE method.

## UMPIRE Method Reminder

1. **U**nderstand - Clarify the problem
2. **M**atch - Identify patterns
3. **P**lan - Design solution
4. **I**mplement - Write code
5. **R**eview - Check solution
6. **E**valuate - Analyze complexity

---

## General Graph DFS Questions

### Initial Problem Understanding
- "Can you explain the problem in your own words?"
- "Is the graph directed or undirected?"
- "Can the graph have cycles?"
- "Are there disconnected components?"
- "Can I modify the input graph/grid?"
- "What should I return if the graph is empty?"

### Pattern Recognition
- "What graph traversal pattern do you see here?"
- "Would DFS or BFS be better for this problem? Why?"
- "How will you handle visited nodes?"
- "Do you need to track the path or just visit nodes?"

### Implementation Questions
- "How will you represent the graph?"
- "Will you use recursive or iterative DFS?"
- "How will you handle the base cases?"
- "What data structures will you need?"

---

## Problem-Specific Scripts

### Problem 1: Number of Islands

**Understand Phase:**
- "So we're counting connected components of 1's in a grid?"
- "Are diagonal connections considered adjacent?"
- "Can I modify the input grid to mark visited cells?"

**Match Phase:**
- "This is a connected components problem"
- "Each island is a connected component in the grid graph"

**Plan Phase:**
- "I'll iterate through each cell"
- "When I find a '1', I'll increment my count and use DFS to mark the entire island"
- "I can either modify the grid or use a visited set"

**Common Mistakes to Watch For:**
- Not checking grid boundaries
- Forgetting to mark cells as visited
- Including diagonal neighbors (unless specified)

**Hints if Stuck:**
- "How can you mark cells as visited?"
- "What happens when you find an unvisited '1'?"
- "Think of the grid as a graph where each cell is a node"

---

### Problem 2: Clone Graph

**Understand Phase:**
- "We need a deep copy, so changing the clone shouldn't affect the original?"
- "The graph might have cycles?"
- "Each node value is unique?"

**Match Phase:**
- "This requires graph traversal with node creation"
- "Need to handle cycles to avoid infinite loops"

**Plan Phase:**
- "I'll use a HashMap to track original → clone mappings"
- "This prevents duplicate clones and handles cycles"

**Common Mistakes to Watch For:**
- Creating duplicate clones of the same node
- Not handling cycles (infinite recursion)
- Shallow copy instead of deep copy

**Hints if Stuck:**
- "How can you track which nodes you've already cloned?"
- "What data structure maps original nodes to clones?"
- "Think about what happens when you encounter a node you've seen before"

---

### Problem 3: Max Area of Island

**Understand Phase:**
- "We're finding the largest connected component?"
- "Area is the count of connected 1's?"
- "Only horizontal and vertical connections count?"

**Match Phase:**
- "Similar to Number of Islands but tracking size"
- "DFS can return the area it explores"

**Plan Phase:**
- "DFS will return the area of the island it explores"
- "Keep track of maximum area found"

**Common Mistakes to Watch For:**
- Not accumulating area from all directions
- Forgetting to mark cells as visited
- Not handling the case of no islands (return 0)

---

### Problem 4: Pacific Atlantic Water Flow

**Understand Phase:**
- "Water flows from higher or equal heights to lower?"
- "We need cells that can reach both oceans?"
- "Pacific is top/left, Atlantic is bottom/right?"

**Match Phase:**
- "This is a multi-source DFS problem"
- "We can work backwards from the oceans"

**Plan Phase:**
- "DFS from Pacific borders to find Pacific-reachable cells"
- "DFS from Atlantic borders to find Atlantic-reachable cells"
- "Return intersection of both sets"

**Common Mistakes to Watch For:**
- Wrong flow direction (should go from low to high when working backwards)
- Not starting from all border cells
- Using wrong comparison (< vs <=)

**Hints if Stuck:**
- "What if you start from the oceans instead of each cell?"
- "Water flows uphill when traversing backwards from ocean"
- "You need two separate DFS explorations"

---

### Problem 5: Surrounded Regions

**Understand Phase:**
- "Only regions completely surrounded get flipped?"
- "Border O's can never be surrounded?"
- "We modify the board in-place?"

**Match Phase:**
- "Border-connected components stay as O"
- "Everything else becomes X"

**Plan Phase:**
- "DFS from border O's to mark safe regions"
- "Convert remaining O's to X's, safe marks back to O's"

**Common Mistakes to Watch For:**
- Trying to identify surrounded regions directly
- Not checking all four borders
- Modifying while traversing

---

### Problem 6: Flood Fill

**Understand Phase:**
- "Change all connected pixels of the same color?"
- "Only 4-directional connections?"
- "What if new color equals original color?"

**Match Phase:**
- "Basic DFS color fill"
- "Similar to paint bucket tool"

**Plan Phase:**
- "Check if colors are same (edge case)"
- "DFS to change all connected pixels"

**Common Mistakes to Watch For:**
- Infinite recursion when newColor equals original
- Not storing original color before starting
- Wrong boundary checks

---

### Problem 7: Connected Components

**Understand Phase:**
- "Count separate graph components?"
- "Nodes are labeled 0 to n-1?"
- "Undirected edges?"

**Match Phase:**
- "Standard connected components problem"
- "Need to track visited nodes"

**Plan Phase:**
- "Build adjacency list from edges"
- "DFS from each unvisited node"
- "Count number of DFS starts needed"

**Common Mistakes to Watch For:**
- Not building bidirectional edges for undirected graph
- Missing isolated nodes (no edges)
- Not initializing adjacency list for all nodes

---

### Problem 8: Word Search

**Understand Phase:**
- "Can we reuse the same cell?"
- "Only horizontal and vertical moves?"
- "Do we just return true/false or the path?"

**Match Phase:**
- "DFS with backtracking"
- "Need to track current position in word"

**Plan Phase:**
- "Try starting from each cell"
- "Mark cells as visited, then unmark (backtrack)"
- "Use index to track position in word"

**Common Mistakes to Watch For:**
- Not backtracking (unmarking cells)
- Not trying all starting positions
- Reusing cells in the same path

---

### Problem 9: All Paths Source to Target

**Understand Phase:**
- "It's a DAG so no cycles?"
- "Find ALL paths, not just one?"
- "Path from 0 to n-1?"

**Match Phase:**
- "Path enumeration with DFS"
- "No visited set needed (DAG)"

**Plan Phase:**
- "Build path during DFS"
- "Add to result when reaching target"
- "Backtrack to explore other paths"

**Common Mistakes to Watch For:**
- Not copying path when adding to result
- Forgetting to backtrack
- Including incomplete paths

---

### Problem 10: Detect Cycle

**Understand Phase:**
- "Undirected graph?"
- "Just detect if any cycle exists?"
- "Can have disconnected components?"

**Match Phase:**
- "DFS with parent tracking"
- "Cycle exists if we visit a non-parent visited node"

**Plan Phase:**
- "Track parent in DFS"
- "If neighbor is visited and not parent → cycle"
- "Check all components"

**Common Mistakes to Watch For:**
- Not tracking parent (treats all edges as cycles)
- Not checking disconnected components
- Wrong parent initialization

---

## Evaluation Criteria

### Code Quality
- Clean, readable code
- Good variable names
- Proper indentation
- Comments for complex logic

### Problem Solving
- Asks clarifying questions
- Identifies edge cases
- Systematic approach
- Tests with examples

### Communication
- Explains thought process
- Walks through approach
- Discusses trade-offs
- Analyzes complexity

### Technical Skills
- Correct DFS implementation
- Proper base cases
- Handles cycles/visited nodes
- Efficient solution

---

## Difficulty Progression

1. **Start Easy:** Flood Fill
2. **Basic Grid:** Number of Islands
3. **Grid Variant:** Max Area of Island
4. **Graph Structure:** Clone Graph, Connected Components
5. **Advanced:** Pacific Atlantic, Word Search
6. **Complex Logic:** Surrounded Regions, Cycle Detection, All Paths

---

## Time Guidelines

- Easy: 15 minutes
- Medium: 25-30 minutes
- Hard: 40-45 minutes

If candidate is stuck for >5 minutes, provide a hint.
If stuck for >10 minutes, guide toward solution.

---

## Notes for Claude

- Be encouraging but honest
- Point out good approaches
- Suggest optimizations gently
- Focus on learning, not just solving
- Celebrate progress and insights