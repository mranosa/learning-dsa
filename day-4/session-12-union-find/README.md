# Day 4, Session 12: Union-Find

## Overview

Master Union-Find (Disjoint Set Union) - a powerful data structure for connectivity problems, cycle detection, and component tracking.

**Duration:** 2-4 hours | **Problems:** 10 (All Medium)

---

## Learning Objectives

- ✅ Understand Union-Find data structure
- ✅ Implement path compression optimization
- ✅ Master union by rank technique
- ✅ Solve connectivity problems efficiently
- ✅ Detect cycles in undirected graphs

---

## Session Flow

### 1. Videos (55 min)
- Union-Find Fundamentals (14 min)
- Deep Dive with Abdul Bari (25 min)
- Advanced Applications (16 min)

### 2. Concept Check (10 min)
Quiz on find/union operations, path compression, complexity analysis.

### 3. Tips & Tricks (5 min)
When to use Union-Find, template memorization, interview communication.

### 4. Problems (2-3 hours)
1. Number of Provinces (Medium)
2. Graph Valid Tree (Medium)
3. Number of Connected Components (Medium)
4. Redundant Connection (Medium)
5. Accounts Merge (Medium)
6. Most Stones Removed (Medium)
7. Number of Operations to Make Network Connected (Medium)
8. Satisfiability of Equality Equations (Medium)
9. Smallest String With Swaps (Medium)
10. Evaluate Division (Medium)

---

## Key Concepts

### Union-Find Operations
- **Find(x)** - Get root of element x: O(α(n))
- **Union(x, y)** - Merge sets: O(α(n))
- **Connected(x, y)** - Check connectivity: O(α(n))
- **Components** - Count distinct groups: O(1)

### Optimizations
- **Path Compression** - Flatten tree during find
- **Union by Rank** - Keep trees balanced
- **Combined** - Nearly O(1) operations

### Time Complexity
- **Without optimization:** O(n) per operation
- **With both optimizations:** O(α(n)) ≈ O(1)

Where α(n) is inverse Ackermann (practically constant).

### Patterns
- Connected Components
- Cycle Detection
- Group Merging
- Component Optimization
- Minimum Spanning Tree

---

## Prerequisites

**Must know:**
- Array operations
- Basic graph concepts
- Recursion basics

**Nice to have:**
- Tree structures
- DFS/BFS traversal

---

## Success Criteria

- [ ] Implement Union-Find with both optimizations
- [ ] Explain path compression clearly
- [ ] Solve Medium problems <25 min
- [ ] Recognize Union-Find patterns
- [ ] Choose Union-Find vs DFS appropriately

---

## Resources

**Videos:** LESSON.md (55 min total)
**Practice:** PROBLEMS.md
**Solutions:** SOLUTIONS.md
**Hints:** HINTS.md

---

## Tips

1. Memorize the template - it's reusable
2. Always implement BOTH optimizations
3. Draw the tree structure
4. Track component count carefully
5. Use union return value for cycle detection
6. Practice explaining α(n) complexity
7. Review after each problem

---

## Common Mistakes

- ❌ Forgetting path compression
- ❌ Not using union by rank
- ❌ Incorrect component counting
- ❌ Index off-by-one (0 vs 1-indexed)
- ❌ Not checking if already connected

---

## What's Next

After completion:
1. 10-minute break
2. Review challenging problems
3. Note patterns learned
4. Session 13: 1D Dynamic Programming

Session 13 introduces dynamic programming with 1D problems, building optimization intuition.

---

**Ready?** Say: `"Claude, start session 4 12"`
