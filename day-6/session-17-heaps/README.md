# Day 6, Session 17: Heaps & Priority Queues

## Overview
Master the art of efficient priority-based operations using heaps - essential for system design and optimization problems.

**Duration:** 3-4 hours
**Problems:** 10 (7 Medium, 3 Hard)
**Prerequisites:** Arrays, basic sorting algorithms

---

## Learning Objectives

By the end of this session, you will:
- ✅ Understand heap data structure and its properties
- ✅ Implement min-heap and max-heap operations
- ✅ Master priority queue patterns
- ✅ Solve K-th element problems efficiently
- ✅ Handle streaming data and median finding

---

## Session Flow

### 1. Video (25 min)
Watch the assigned video on Heaps and Priority Queues fundamentals.

### 2. Concept Check (10 min)
Claude will quiz you on:
- Heap properties (complete binary tree)
- Heapify operations
- Priority queue operations
- Time complexity of heap operations

### 3. Tips & Tricks (5 min)
Learn interview-specific insights about:
- When to use min-heap vs max-heap
- K-element patterns
- Two-heap technique
- TypeScript priority queue implementation

### 4. Problem Solving (2.5-3.5 hours)
Solve 10 carefully selected problems:
1. Kth Largest Element in an Array (Medium)
2. Top K Frequent Elements (Medium)
3. Find Median from Data Stream (Hard)
4. Merge K Sorted Lists (Hard)
5. Task Scheduler (Medium)
6. Kth Smallest Element in a Sorted Matrix (Medium)
7. K Closest Points to Origin (Medium)
8. Reorganize String (Medium)
9. Ugly Number II (Medium)
10. Find K Pairs with Smallest Sums (Medium)

---

## Key Concepts

### Heap Properties
- **Complete Binary Tree** - All levels filled except possibly last
- **Heap Invariant** - Parent >= children (max-heap) or Parent <= children (min-heap)
- **Array Representation** - Parent at i, children at 2i+1 and 2i+2
- **Height** - O(log n) for n elements

### Heap Operations
- **Insert:** O(log n) - bubble up
- **Extract Min/Max:** O(log n) - bubble down
- **Peek:** O(1) - top element
- **Heapify:** O(n) - build heap from array
- **Delete:** O(log n) - replace and bubble

### Common Patterns
- K-th largest/smallest element
- Top K elements
- Median tracking (two heaps)
- Merge K sorted sequences
- Interval scheduling

---

## Prerequisites

**Must know:**
- Array manipulation in TypeScript
- Basic sorting concepts
- Tree structure basics

**Nice to have:**
- Binary tree traversal
- Understanding of complete binary trees
- Priority concepts

---

## Success Criteria

You're ready to move on when you can:
- [ ] Explain heap properties clearly
- [ ] Implement heap operations from scratch
- [ ] Identify when to use heaps vs sorting
- [ ] Solve K-element problems efficiently
- [ ] Handle streaming data problems

---

## Resources

**Video:** See LESSON.md for link

**Readings:**
- Heap Visualization: https://visualgo.net/en/heap
- Priority Queue patterns: LESSON.md

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Visualize the heap** - Draw the tree structure
2. **Master the formulas** - Parent/child indices
3. **Think about K** - Most heap problems involve K elements
4. **Consider both heaps** - Min and max have different uses
5. **Practice implementation** - Know how to code a heap
6. **Time complexity matters** - Heaps vs sorting trade-offs
7. **Handle edge cases** - Empty heap, single element

---

## Common Mistakes

**Avoid these:**
- ❌ Confusing min-heap with max-heap properties
- ❌ Wrong parent/child index calculations
- ❌ Not maintaining heap invariant after operations
- ❌ Using sorting when heap is more efficient
- ❌ Forgetting to handle duplicate elements

---

## What's Next

After completing this session:
1. Take a 15-minute break
2. Review heap operation complexities
3. Practice implementing a heap from scratch
4. Move to Session 18: Graphs - BFS

Session 18 introduces graph traversal, building on queue concepts from heaps.

---

**Ready to start?** Say: `"Claude, start session 6 17"`