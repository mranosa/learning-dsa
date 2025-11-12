# Day 4, Session 11: Graph BFS

## Overview

Master breadth-first search in graphs - essential for shortest path and level-order traversal problems.

**Duration:** 3-5 hours | **Problems:** 10 (7 Medium, 1 Hard, 2 Premium)

---

## Learning Objectives

- ✅ Understand BFS traversal in graphs
- ✅ Implement queue-based level-order traversal
- ✅ Master multi-source BFS pattern
- ✅ Apply topological sort (Kahn's algorithm)
- ✅ Solve shortest path problems

---

## Session Flow

### 1. Videos (25 min)
- Graph BFS fundamentals (12 min)
- Topological sort (10 min)
- Alternative explanations (optional)

### 2. Concept Check (10 min)
Quiz on BFS vs DFS, queue usage, shortest path, topological sort.

### 3. Tips & Tricks (5 min)
Multi-source BFS, bidirectional optimization, cycle detection.

### 4. Problems (3-4 hours)
1. Rotting Oranges (Medium)
2. Course Schedule (Medium)
3. Course Schedule II (Medium)
4. Shortest Path in Binary Matrix (Medium)
5. Walls and Gates (Medium - Premium)
6. Word Ladder (Hard)
7. 01 Matrix (Medium)
8. Open the Lock (Medium)
9. Minimum Knight Moves (Medium - Premium)
10. Shortest Bridge (Medium)

---

## Key Concepts

### BFS Properties
- **Level-order** - Process layer by layer
- **Shortest path** - In unweighted graphs
- **Queue-based** - FIFO guarantees order
- **Visited tracking** - Prevents cycles

### Common Patterns
- Single-source BFS
- Multi-source BFS
- Bidirectional BFS
- Topological sort

### Complexity
- **Time:** O(V + E) for graphs, O(m × n) for grids
- **Space:** O(V) for queue and visited set

---

## Prerequisites

**Must know:**
- Queue operations (enqueue/dequeue)
- Graph representation (adjacency list)
- Set/Map for tracking
- Matrix traversal

---

## Success Criteria

- [ ] Implement BFS from scratch
- [ ] Apply multi-source BFS
- [ ] Perform topological sort
- [ ] Identify BFS vs DFS use cases
- [ ] Handle cycles and edge cases

---

## Resources

**Videos:** LESSON.md
**Practice:** PROBLEMS.md
**Solutions:** SOLUTIONS.md
**Hints:** HINTS.md

---

## Tips

1. Draw the graph first
2. Track levels explicitly when needed
3. Consider multi-source for spreading problems
4. Use proper queue (not stack!)
5. Mark visited before enqueueing
6. Handle disconnected components
7. Consider bidirectional for optimization

---

## Common Mistakes

- ❌ Using DFS when BFS gives shortest path
- ❌ Marking visited after dequeue (causes duplicates)
- ❌ Not handling disconnected graphs
- ❌ Incorrect neighbor iteration in matrices
- ❌ Missing edge cases (empty, single node)

---

## What's Next

After completion:
1. 15-minute break
2. Review performance
3. Note challenging patterns
4. Session 12: Graph DFS

Session 12 explores depth-first patterns including backtracking and connected components.

---

**Ready?** Say: `"Claude, start session 4 11"`
