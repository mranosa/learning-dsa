# Day 7, Session 19: Tries (Prefix Trees)

## Overview

Master efficient string manipulation and prefix searching with Trie data structures - essential for autocomplete, spell checkers, and word games.

**Duration:** 3-4 hours | **Problems:** 10 (0 Easy, 5 Medium, 5 Hard)

---

## Learning Objectives

- ✅ Understand Trie data structure and node structure
- ✅ Implement Tries from scratch with insert, search, and startsWith
- ✅ Master wildcard and pattern matching in Tries
- ✅ Solve complex word search and dictionary problems
- ✅ Optimize string operations using prefix trees

---

## Session Flow

### 1. Videos (40 min)
- Trie Implementation & Fundamentals (20 min)
- Trie Advanced Patterns (20 min)

### 2. Concept Check (10 min)
Quiz on Trie node structure, operations, time complexity, applications.

### 3. Tips & Tricks (5 min)
When to use Tries vs HashMaps, space optimization, TypeScript patterns.

### 4. Problems (3-4 hours)
1. Implement Trie (Prefix Tree) (Medium)
2. Design Add and Search Words Data Structure (Medium)
3. Word Search II (Hard)
4. Longest Word in Dictionary (Medium)
5. Replace Words (Medium)
6. Implement Magic Dictionary (Medium)
7. Prefix and Suffix Search (Hard)
8. Word Squares (Hard)
9. Concatenated Words (Hard)
10. Stream of Characters (Hard)

---

## Key Concepts

### Trie Node Structure
- **Node:** Contains children map and isEnd flag
- **Root:** Empty node as starting point
- **Path:** Represents a string from root to node
- **Children:** Map or array of child nodes

### Trie Operations
- **Insert:** O(m) where m is word length
- **Search:** O(m) exact match
- **StartsWith:** O(p) where p is prefix length
- **Delete:** O(m) with cleanup
- **Space:** O(ALPHABET_SIZE × N × M)

### Common Patterns
- Wildcard matching (. matches any char)
- DFS/BFS traversal for word collection
- Pruning for optimization
- Multiple Trie combination
- Reverse Trie for suffix search

---

## Prerequisites

**Must know:**
- Tree data structure basics
- DFS and BFS traversal
- HashMap/Object manipulation
- Recursion and backtracking

**Nice to have:**
- Dynamic programming basics
- String manipulation techniques
- Space complexity analysis

---

## Success Criteria

- [ ] Implement a basic Trie from scratch
- [ ] Handle wildcard pattern matching
- [ ] Optimize space usage in Tries
- [ ] Solve Medium Trie problems in <25 min
- [ ] Identify when Tries outperform HashMaps

---

## Resources

**Video:** LESSON.md
**Practice:** PROBLEMS.md
**Solutions:** SOLUTIONS.md
**Hints:** HINTS.md

---

## Tips

1. Draw the Trie - visualize the structure
2. Consider space tradeoffs - Tries can be memory intensive
3. Use Map vs Array - Map for sparse, Array for dense alphabets
4. Handle edge cases - empty strings, single characters
5. Practice DFS traversal - essential for word collection
6. Time yourself - Hard problems need efficiency
7. Think about optimization - pruning and early termination

---

## Common Mistakes

- ❌ Forgetting to mark word endings with isEnd flag
- ❌ Not handling empty string inputs
- ❌ Inefficient wildcard matching without pruning
- ❌ Using recursion without proper base cases
- ❌ Not cleaning up nodes during deletion

---

## What's Next

After completion:
1. 10-minute break
2. Review scores
3. Note weak patterns
4. Session 20: Bit Manipulation

Session 20 introduces bit manipulation techniques for efficient problem solving.

---

**Ready?** Say: `"Claude, start session 7 19"`
