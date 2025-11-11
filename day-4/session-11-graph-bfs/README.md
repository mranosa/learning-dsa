# Day 4, Session 11: Graph BFS

## Overview
Master Breadth-First Search in graphs and topological sorting - essential patterns for level-order traversal and dependency resolution.

**Duration:** 3-5 hours
**Problems:** 10 (7 Medium, 1 Hard, 2 LC Premium)
**Prerequisites:** Graph basics, queue operations, adjacency list representation

---

## Learning Objectives

By the end of this session, you will:
- ✅ Understand BFS traversal in graphs
- ✅ Implement multi-source BFS efficiently
- ✅ Master topological sorting with Kahn's algorithm
- ✅ Solve shortest path problems in unweighted graphs
- ✅ Handle level-order graph traversal patterns

---

## Session Flow

### 1. Video (25 min)
Watch the assigned videos on Graph BFS and Topological Sort fundamentals.

### 2. Concept Check (10 min)
Claude will quiz you on:
- BFS vs DFS in graphs
- Queue-based traversal
- Topological sorting
- Shortest path properties

### 3. Tips & Tricks (5 min)
Learn interview-specific insights about:
- When to use BFS vs DFS
- Multi-source BFS patterns
- Bidirectional BFS optimization
- Cycle detection in directed graphs

### 4. Problem Solving (3-4 hours)
Solve 10 carefully selected problems:
1. Rotting Oranges (Medium - Multi-source BFS)
2. Course Schedule (Medium - Cycle Detection)
3. Course Schedule II (Medium - Topological Sort)
4. Shortest Path in Binary Matrix (Medium - 8-directional BFS)
5. Walls and Gates (Medium - Multi-source BFS)
6. Word Ladder (Hard - Transformation Graph)
7. 01 Matrix (Medium - Distance BFS)
8. Open the Lock (Medium - State Space BFS)
9. Minimum Knight Moves (Medium - Chess BFS)
10. Shortest Bridge (Medium - BFS + DFS)

---

## Key Concepts

### BFS Characteristics
- **Level-order traversal** - Process all nodes at distance k before k+1
- **Shortest path** - In unweighted graphs, BFS finds shortest paths
- **Queue-based** - FIFO ensures level-by-level processing
- **Visited tracking** - Prevents cycles and revisiting

### Common BFS Patterns
- **Single-source BFS** - Start from one node
- **Multi-source BFS** - Start from multiple nodes simultaneously
- **Bidirectional BFS** - Search from both ends
- **Level tracking** - Track distance/depth during traversal

### Topological Sort (Kahn's Algorithm)
- **In-degree tracking** - Count incoming edges
- **Queue initialization** - Start with 0 in-degree nodes
- **Process and reduce** - Remove edges, add new 0 in-degree nodes
- **Cycle detection** - If processed < total nodes, cycle exists

### Time Complexity
- **BFS Traversal:** O(V + E) where V = vertices, E = edges
- **Topological Sort:** O(V + E)
- **Shortest Path:** O(V + E) for unweighted graphs

---

## Prerequisites

**Must know:**
- Queue operations (enqueue, dequeue)
- Graph representation (adjacency list/matrix)
- Set/Map for visited tracking
- Basic graph terminology

**Nice to have:**
- DFS understanding for comparison
- Matrix traversal experience
- State space concept

---

## Success Criteria

You're ready to move on when you can:
- [ ] Implement BFS from scratch
- [ ] Apply multi-source BFS pattern
- [ ] Perform topological sort correctly
- [ ] Identify when BFS is optimal vs DFS
- [ ] Handle edge cases (cycles, disconnected components)

---

## Resources

**Videos:** See LESSON.md for links

**Readings:**
- Graph algorithms visualization: https://visualgo.net/en/dfsbfs
- Topological sort: https://www.geeksforgeeks.org/topological-sorting-kahns-algorithm/

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Draw the graph** - Visualize before coding
2. **Track levels explicitly** - Many problems need distance/depth
3. **Consider multi-source** - Often more efficient than multiple BFS
4. **Check for cycles** - Especially in directed graphs
5. **Use proper data structures** - Queue for BFS, not stack
6. **Handle disconnected graphs** - May need multiple BFS calls
7. **Optimize with bidirectional BFS** - For single source-target problems

---

## Common Mistakes

**Avoid these:**
- ❌ Using DFS when BFS gives shortest path
- ❌ Forgetting to mark visited before enqueueing
- ❌ Not handling disconnected components
- ❌ Incorrect neighbor iteration in matrices
- ❌ Missing edge cases (empty graph, single node)

---

## What's Next

After completing this session:
1. Take a 15-minute break
2. Review your performance scores
3. Note patterns that were challenging
4. Move to Session 12: Graph DFS

Session 12 explores depth-first patterns including backtracking and connected components.

---

**Ready to start?** Say: `"Claude, start session 4 11"`