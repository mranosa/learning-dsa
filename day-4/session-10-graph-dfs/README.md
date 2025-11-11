# Day 4, Session 10: Graph DFS

## Overview
Master Depth-First Search in graphs - one of the most fundamental graph traversal patterns that appears in countless interview problems.

**Duration:** 3-4 hours
**Problems:** 10 (1 Easy, 9 Medium)
**Prerequisites:** Basic understanding of recursion and tree traversal

---

## Learning Objectives

By the end of this session, you will:
- ✅ Understand graph representations (adjacency list, matrix)
- ✅ Master DFS traversal patterns
- ✅ Handle visited nodes to avoid cycles
- ✅ Solve connected component problems
- ✅ Implement path finding algorithms

---

## Session Flow

### 1. Video (25 min)
Watch the assigned video on Graph DFS fundamentals and common patterns.

### 2. Concept Check (10 min)
Claude will quiz you on:
- Graph representations
- DFS vs BFS
- Visited set pattern
- Time/space complexity

### 3. Tips & Tricks (5 min)
Learn interview-specific insights about:
- When to use DFS vs BFS
- Grid traversal patterns
- Cycle detection techniques

### 4. Problem Solving (3-4 hours)
Solve 10 carefully selected problems:
1. Number of Islands (Medium)
2. Clone Graph (Medium)
3. Max Area of Island (Medium)
4. Pacific Atlantic Water Flow (Medium)
5. Surrounded Regions (Medium)
6. Flood Fill (Easy)
7. Number of Connected Components in Graph (Medium)
8. Word Search (Medium)
9. All Paths From Source to Target (Medium)
10. Detect Cycle in Undirected Graph (Medium)

---

## Key Concepts

### Graph Representations
- **Adjacency List:** Map<number, number[]> or number[][]
- **Adjacency Matrix:** boolean[][] or number[][]
- **Grid as Graph:** 2D array treated as implicit graph

### DFS Patterns
- **Recursive DFS:** Function calls manage the stack
- **Iterative DFS:** Explicit stack for traversal
- **Visited Set:** Track processed nodes
- **Path Building:** Track current path for solutions

### Common Applications
- Connected Components
- Cycle Detection
- Path Finding
- Grid Traversal (4 or 8 directions)

---

## Prerequisites

**Must know:**
- Recursion fundamentals
- Basic data structures (arrays, sets, maps)
- Tree traversal (helpful but not required)

**Nice to have:**
- Understanding of graph theory basics
- Experience with 2D arrays
- Tree DFS patterns

---

## Success Criteria

You're ready to move on when you can:
- [ ] Explain DFS traversal clearly
- [ ] Identify when to use DFS vs BFS
- [ ] Handle cycles with visited sets
- [ ] Solve grid traversal problems confidently
- [ ] Implement both recursive and iterative DFS

---

## Resources

**Video:** See LESSON.md for link

**Readings:**
- Graph representations guide
- DFS visualization tools

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Draw the graph** - Visualize before coding
2. **Start with base cases** - Handle null/empty inputs
3. **Use visited sets** - Prevent infinite loops
4. **Practice grid traversal** - Very common in interviews
5. **Consider edge cases** - Disconnected graphs, single node
6. **Time yourself** - Medium problems in 25-30 min
7. **Compare approaches** - Recursive vs iterative

---

## Common Mistakes

**Avoid these:**
- ❌ Forgetting to mark nodes as visited
- ❌ Modifying input without asking permission
- ❌ Not handling disconnected components
- ❌ Using wrong data structure (stack vs queue)
- ❌ Off-by-one errors in grid boundaries

---

## Grid Traversal Pattern

Most common DFS pattern in interviews:

```typescript
const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]; // 4-directional

function dfs(grid: number[][], row: number, col: number): void {
    // Base cases
    if (row < 0 || row >= grid.length ||
        col < 0 || col >= grid[0].length ||
        grid[row][col] === 0) {
        return;
    }

    // Mark visited
    grid[row][col] = 0;

    // Explore neighbors
    for (const [dr, dc] of directions) {
        dfs(grid, row + dr, col + dc);
    }
}
```

---

## What's Next

After completing this session:
1. Take a 10-minute break
2. Review your performance scores
3. Note patterns you struggled with
4. Move to Session 11: Graph BFS

Session 11 explores Breadth-First Search for shortest path problems.

---

**Ready to start?** Say: `"Claude, start session 4 10"`