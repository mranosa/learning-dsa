# Day 4, Session 10: Graph DFS

## Overview

Master Depth-First Search for graphs - fundamental traversal pattern for countless interview problems.

**Duration:** 3-4 hours | **Problems:** 10 (1 Easy, 9 Medium)

---

## Learning Objectives

- ✅ Understand graph representations
- ✅ Master DFS traversal (recursive/iterative)
- ✅ Handle visited tracking for cycles
- ✅ Solve grid traversal problems
- ✅ Implement connected components

---

## Session Flow

### 1. Videos (47 min)
- Graph Fundamentals (15 min)
- DFS Algorithm & Patterns (20 min)
- Grid Traversal Techniques (12 min)

### 2. Concept Check (10 min)
Quiz on graph representations, DFS vs BFS, time/space complexity.

### 3. Tips & Tricks (5 min)
Visited sets, grid patterns, when to use DFS.

### 4. Problems (3-4 hours)
1. Number of Islands (Medium)
2. Clone Graph (Medium)
3. Max Area of Island (Medium)
4. Pacific Atlantic Water Flow (Medium)
5. Surrounded Regions (Medium)
6. Flood Fill (Easy)
7. Number of Connected Components (Medium)
8. Word Search (Medium)
9. All Paths Source to Target (Medium)
10. Detect Cycle in Undirected Graph (Medium)

---

## Key Concepts

### Graph Representations
- **Adjacency List:** Map<number, number[]>
- **Adjacency Matrix:** boolean[][]
- **Grid as Graph:** 2D array with implicit edges

### DFS Complexity
- **Time:** O(V + E) for graphs, O(m × n) for grids
- **Space:** O(V) for visited set + stack
- **Recursive:** Call stack uses O(V) space

### Common Patterns
- Grid Traversal (4-directional)
- Connected Components
- Cycle Detection
- Path Finding

---

## Prerequisites

**Must know:**
- Recursion fundamentals
- Basic data structures (arrays, sets, maps)
- 2D array manipulation

---

## Success Criteria

- [ ] Explain DFS clearly
- [ ] Identify when to use DFS vs BFS
- [ ] Handle cycles with visited sets
- [ ] Solve grid problems confidently
- [ ] Implement recursive and iterative DFS

---

## Resources

**Video:** LESSON.md
**Practice:** PROBLEMS.md
**Solutions:** SOLUTIONS.md
**Hints:** HINTS.md

---

## Tips

1. Draw the graph - visualize first
2. Always use visited set
3. Practice grid traversal patterns
4. Handle boundary conditions
5. Think aloud - explain your approach
6. Time yourself (Medium: <30 min)
7. Review solutions even if correct

---

## Common Mistakes

- ❌ Forgetting visited set (infinite loops)
- ❌ Modifying input without permission
- ❌ Missing disconnected components
- ❌ Off-by-one in grid boundaries
- ❌ Not handling empty graph

---

## What's Next

After completion:
1. 10-minute break
2. Review scores
3. Note difficult patterns
4. Session 11: Graph BFS

Session 11 covers Breadth-First Search for shortest path problems.

---

**Ready?** Say: `"Claude, start session 4 10"`
