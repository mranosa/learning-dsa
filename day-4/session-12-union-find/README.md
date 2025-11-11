# Day 4, Session 12: Union-Find

## Overview
Master the Union-Find (Disjoint Set Union) data structure - a powerful technique for solving connectivity problems and detecting cycles in graphs.

**Duration:** 3-4 hours
**Problems:** 10 (All Medium complexity)
**Prerequisites:** Basic understanding of graphs and tree concepts

---

## Learning Objectives

By the end of this session, you will:
- ✅ Understand Union-Find data structure and its operations
- ✅ Implement path compression and union by rank optimizations
- ✅ Solve graph connectivity problems efficiently
- ✅ Detect cycles in undirected graphs
- ✅ Master component counting and grouping problems

---

## Session Flow

### 1. Video (30 min)
Watch the assigned video on Union-Find fundamentals and optimizations.

### 2. Concept Check (15 min)
Claude will quiz you on:
- Union and Find operations
- Path compression technique
- Union by rank optimization
- Time complexity analysis

### 3. Tips & Tricks (10 min)
Learn interview-specific insights about:
- When to use Union-Find vs DFS/BFS
- Common Union-Find patterns
- TypeScript implementation tips

### 4. Problem Solving (2.5-3.5 hours)
Solve 10 carefully selected problems:
1. Number of Provinces (Medium - Basic connectivity)
2. Graph Valid Tree (Medium - Cycle detection)
3. Number of Connected Components (Medium - Component counting)
4. Redundant Connection (Medium - Find cycle edge)
5. Accounts Merge (Medium - Group merging)
6. Most Stones Removed (Medium - Maximum components)
7. Number of Operations to Make Network Connected (Medium - Connectivity operations)
8. Satisfiability of Equality Equations (Medium - Equation grouping)
9. Smallest String With Swaps (Medium - Component optimization)
10. Evaluate Division (Medium - Weighted Union-Find)

---

## Key Concepts

### Union-Find Operations
- **Find(x)** - Find the root parent of element x
- **Union(x, y)** - Connect components containing x and y
- **Connected(x, y)** - Check if x and y are in same component
- **Count()** - Get number of distinct components

### Optimizations
- **Path Compression** - Make each node point directly to root
- **Union by Rank** - Always attach smaller tree to larger
- **Combined Optimization** - Nearly O(1) amortized operations

### Time Complexity
- **Without optimization:** O(n) per operation
- **With path compression:** O(log n) amortized
- **With both optimizations:** O(α(n)) ≈ O(1) amortized

### Common Patterns
- Connected components counting
- Cycle detection in graphs
- Minimum spanning tree (Kruskal's)
- Dynamic connectivity queries
- Group merging problems

---

## Prerequisites

**Must know:**
- Basic graph representation (adjacency list/matrix)
- Tree structure concepts
- Set operations basics

**Nice to have:**
- DFS/BFS graph traversal
- Understanding of amortized analysis
- Basic graph theory

---

## Success Criteria

You're ready to move on when you can:
- [ ] Implement Union-Find with optimizations from memory
- [ ] Identify when Union-Find is the optimal approach
- [ ] Solve Medium Union-Find problems in <25 min
- [ ] Explain path compression and union by rank
- [ ] Apply Union-Find to various problem types

---

## Resources

**Video:** See LESSON.md for link

**Readings:**
- Union-Find visualization: https://visualgo.net/en/ufds
- Complexity analysis: https://en.wikipedia.org/wiki/Disjoint-set_data_structure

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Master the template** - Union-Find has a standard implementation
2. **Draw the forest** - Visualize component trees
3. **Count components carefully** - Track merges correctly
4. **Consider both optimizations** - They work together
5. **Practice variations** - Weighted, directional, etc.
6. **Think connectivity** - Union-Find excels at connectivity queries
7. **Compare with DFS** - Know when each is better

---

## Common Mistakes

**Avoid these:**
- ❌ Forgetting path compression in find operation
- ❌ Not using union by rank (leads to skewed trees)
- ❌ Incorrect component counting after unions
- ❌ Using Union-Find for directed graphs without modification
- ❌ Not handling self-loops or parallel edges

---

## What's Next

After completing this session:
1. Take a 15-minute break
2. Review your implementation patterns
3. Note any challenging concepts
4. Move to Session 13: 1D Dynamic Programming

Session 13 introduces dynamic programming with 1D problems, building problem-solving intuition for optimization problems.

---

**Ready to start?** Say: `"Claude, start session 4 12"`