# Day 6, Session 17: Heaps & Priority Queues

## Overview

Master efficient priority-based operations using heaps - essential for K-element problems, scheduling, and streaming data.

**Duration:** 3-4 hours | **Problems:** 10 (7 Medium, 3 Hard)

---

## Learning Objectives

- ✅ Understand heap structure and properties
- ✅ Implement min-heap and max-heap operations
- ✅ Master K-element patterns
- ✅ Apply two-heap technique for medians
- ✅ Solve merge and priority problems

---

## Session Flow

### 1. Videos (40 min)
- Heap Fundamentals (15 min)
- Min Heap vs Max Heap (10 min)
- Priority Queue Patterns (15 min)

### 2. Concept Check (10 min)
Quiz on heap properties, operations, time complexity, pattern recognition.

### 3. Tips & Tricks (5 min)
When to use heaps, min vs max selection, K-element patterns, TypeScript implementation.

### 4. Problems (2.5-3.5 hours)
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
- **Heap Invariant** - Parent >= children (max) or Parent <= children (min)
- **Array Representation** - Parent at i, children at 2i+1, 2i+2
- **Height** - O(log n) for n elements

### Heap Operations
- **Insert:** O(log n) - bubble up
- **Extract Min/Max:** O(log n) - bubble down
- **Peek:** O(1) - top element
- **Heapify:** O(n) - build from array
- **Delete:** O(log n) - replace and bubble

### Patterns
- K-th largest/smallest (min heap of size K)
- Top K elements (heap of size K)
- Median tracking (two heaps)
- Merge K sorted (min heap of heads)
- Priority scheduling (max heap by priority)

---

## Prerequisites

**Must know:**
- Array manipulation in TypeScript
- Basic sorting concepts
- Tree structure basics

---

## Success Criteria

- [ ] Explain heap properties confidently
- [ ] Implement basic heap operations
- [ ] Identify K-element patterns instantly
- [ ] Choose correct heap type (min vs max)
- [ ] Solve Medium problems <25 min

---

## Resources

**Video:** LESSON.md
**Practice:** PROBLEMS.md
**Solutions:** SOLUTIONS.md
**Hints:** HINTS.md

---

## Tips

1. Watch all videos - heap operations are foundational
2. Do concept check - reveals confusion on min/max
3. Draw the tree structure for clarity
4. K largest = MIN heap (counterintuitive!)
5. Practice heap implementation from scratch
6. Use UMPIRE method
7. Time yourself

---

## Common Mistakes

- ❌ Confusing min-heap with max-heap
- ❌ Wrong index calculations (parent/child)
- ❌ Using max heap for K largest (should be min!)
- ❌ Not maintaining heap size K
- ❌ Sorting when heap is more efficient
- ❌ Forgetting heap property after operations

---

## What's Next

After completion:
1. 15-minute break
2. Review heap operation complexity
3. Practice implementing heap from scratch
4. Session 18: Graphs - BFS

Session 18 builds on queue concepts from heaps to explore graph traversal.

---

**Ready?** Say: `"Claude, start session 6 17"`
