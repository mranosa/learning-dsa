# Day 1, Session 2: Hash Maps

## Overview
Master the fundamentals of hash maps - the most powerful data structure for O(1) lookups and frequency counting.

**Duration:** 2-4 hours
**Problems:** 10 (2 Easy, 8 Medium)
**Prerequisites:** Arrays, Big O notation

---

## Learning Objectives

By the end of this session, you will:
- ✅ Understand how hash maps work internally
- ✅ Master O(1) lookup, insert, and delete operations
- ✅ Recognize when to use hash maps vs arrays
- ✅ Solve frequency counting problems efficiently
- ✅ Handle collision resolution and hash functions

---

## Session Flow

### 1. Video (20 min)
Watch the assigned video on Hash Map fundamentals and implementation.

### 2. Concept Check (10 min)
Claude will quiz you on:
- Hash function basics
- Collision resolution strategies
- Time/space complexity
- Map vs Set differences

### 3. Tips & Tricks (5 min)
Learn interview-specific insights about:
- When to use Map vs Object in TypeScript
- Common hash map patterns
- Frequency counting optimization

### 4. Problem Solving (2-3 hours)
Solve 10 carefully selected problems:
1. Contains Duplicate (Easy)
2. Valid Anagram (Easy)
3. Two Sum (Easy)
4. Group Anagrams (Medium)
5. Top K Frequent Elements (Medium)
6. Product of Array Except Self (Medium)
7. Valid Sudoku (Medium)
8. Encode and Decode Strings (Medium)
9. Longest Consecutive Sequence (Medium)
10. Subarray Sum Equals K (Medium)

---

## Key Concepts

### Hash Map Operations
- **Insert:** O(1) average, O(n) worst case
- **Lookup:** O(1) average, O(n) worst case
- **Delete:** O(1) average, O(n) worst case
- **Space:** O(n) for n elements

### TypeScript Hash Structures
- **Map<K, V>** - Preserves insertion order, any key type
- **Set<T>** - Unique values only
- **Object** - String/Symbol keys only
- **WeakMap/WeakSet** - Garbage-collectible references

### Common Patterns
- Frequency Counting
- Two Sum Pattern
- Anagram Detection
- Grouping/Categorizing
- Caching/Memoization

---

## Prerequisites

**Must know:**
- Basic array operations
- O(1) vs O(n) complexity
- Key-value pair concept

**Nice to have:**
- Understanding of hash functions
- Collision resolution basics
- Memory addressing

---

## Success Criteria

You're ready to move on when you can:
- [ ] Explain hash map internals confidently
- [ ] Choose Map vs Set vs Object appropriately
- [ ] Solve frequency counting problems quickly
- [ ] Identify hash map patterns in problems
- [ ] Handle edge cases with empty maps

---

## Resources

**Video:** See LESSON.md for link

**Readings:**
- Hash Map visualization: https://visualgo.net/en/hashtable
- TypeScript Map docs: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Master the basics first** - Frequency counting is fundamental
2. **Understand Map vs Object** - Know when to use each
3. **Draw hash tables** - Visualize collision handling
4. **Practice two-pointer with maps** - Common combo pattern
5. **Check for edge cases** - Empty map, single element
6. **Time yourself** - Hash map problems should be fast
7. **Learn the patterns** - Two Sum appears everywhere

---

## Common Mistakes

**Avoid these:**
- ❌ Using nested loops when a hash map would work
- ❌ Forgetting to handle undefined/null keys
- ❌ Not considering hash collision impact
- ❌ Using Object when Map is more appropriate
- ❌ Mutating keys after insertion (reference types)

---

## What's Next

After completing this session:
1. Take a 10-minute break
2. Review your performance scores
3. Note patterns you struggled with
4. Move to Session 3: Sliding Window

Session 3 combines arrays and hash maps for efficient window operations.

---

**Ready to start?** Say: `"Claude, start session 1 2"`