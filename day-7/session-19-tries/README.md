# Day 7, Session 19: Tries (Prefix Trees)

## Overview
Master the art of efficient string manipulation and prefix searching with Trie data structures - essential for autocomplete, spell checkers, and word games.

**Duration:** 3-4 hours
**Problems:** 10 (0 Easy, 5 Medium, 5 Hard)
**Prerequisites:** Trees, DFS/BFS, String manipulation

---

## Learning Objectives

By the end of this session, you will:
- ✅ Understand Trie data structure fundamentals
- ✅ Implement Tries from scratch with insert, search, and startsWith
- ✅ Master wildcard and pattern matching in Tries
- ✅ Solve complex word search and dictionary problems
- ✅ Optimize string operations using prefix trees

---

## Session Flow

### 1. Video (25 min)
Watch the assigned video on Trie data structures and prefix tree applications.

### 2. Concept Check (10 min)
Claude will quiz you on:
- Trie node structure
- Time complexity of operations
- Space optimization techniques
- Common Trie applications

### 3. Tips & Tricks (5 min)
Learn interview-specific insights about:
- When to use Tries vs HashMaps
- Space optimization with compressed Tries
- TypeScript implementation patterns

### 4. Problem Solving (3-4 hours)
Solve 10 carefully selected problems:
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

### Trie Structure
- **Node:** Contains children map and isEnd flag
- **Root:** Empty node as starting point
- **Path:** Represents a string from root to node
- **Prefix:** Common starting substring
- **Suffix:** Common ending substring

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

You're ready to move on when you can:
- [ ] Implement a basic Trie from scratch
- [ ] Handle wildcard pattern matching
- [ ] Optimize space usage in Tries
- [ ] Solve Medium Trie problems in <25 min
- [ ] Identify when Tries outperform HashMaps

---

## Resources

**Video:** See LESSON.md for link

**Readings:**
- Trie visualization: https://visualgo.net/en/suffixarray
- TypeScript patterns: TYPESCRIPT-LEETCODE.md

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Draw the Trie** - Visualize the structure for clarity
2. **Consider space tradeoffs** - Tries can be memory intensive
3. **Use Map vs Array** - Map for sparse, Array for dense alphabets
4. **Handle edge cases** - Empty strings, single characters
5. **Practice DFS traversal** - Essential for word collection
6. **Time yourself** - Hard problems need efficiency
7. **Think about optimization** - Pruning and early termination

---

## Common Mistakes

**Avoid these:**
- ❌ Forgetting to mark word endings with isEnd flag
- ❌ Not handling empty string inputs
- ❌ Inefficient wildcard matching without pruning
- ❌ Using recursion without proper base cases
- ❌ Not cleaning up nodes during deletion

---

## What's Next

After completing this session:
1. Take a 15-minute break
2. Review your performance scores
3. Note patterns you struggled with
4. Move to Session 20: Bit Manipulation

Session 20 introduces bit manipulation techniques for efficient problem solving.

---

**Ready to start?** Say: `"Claude, start session 7 19"`