# Day 2, Session 6: Binary Search

## Overview

Master O(log n) searching - the foundation for efficient algorithms.

**Duration:** 2-4 hours | **Problems:** 10 (3 Easy, 6 Medium, 1 Hard)

---

## Learning Objectives

- ✅ Understand binary search fundamentals
- ✅ Master iterative and recursive implementations
- ✅ Apply binary search to rotated arrays
- ✅ Recognize binary search on answer space
- ✅ Handle edge cases and off-by-one errors

---

## Session Flow

### 1. Videos (47 min)
- Binary Search Fundamentals (15 min)
- Rotated Arrays & Variations (18 min)
- Binary Search on Answer Space (14 min)

### 2. Concept Check (10 min)
Quiz on binary search invariants, templates, edge cases.

### 3. Tips & Tricks (5 min)
Common pitfalls, template selection, overflow prevention.

### 4. Problems (2-3 hours)
1. Binary Search (Easy)
2. Search Insert Position (Easy)
3. First Bad Version (Easy)
4. Find Minimum in Rotated Sorted Array (Medium)
5. Search in Rotated Sorted Array (Medium)
6. Search a 2D Matrix (Medium)
7. Koko Eating Bananas (Medium)
8. Find Peak Element (Medium)
9. Time Based Key-Value Store (Medium)
10. Median of Two Sorted Arrays (Hard)

---

## Key Concepts

### Complexity
- **Time:** O(log n) - halve search space each step
- **Space:** O(1) iterative, O(log n) recursive
- **Requirement:** Sorted array or monotonic property

### Templates
- **Template 1:** `while (left <= right)` - exact match
- **Template 2:** `while (left < right)` - first/last position
- **Template 3:** Binary search on answer space

### Patterns
- Classic binary search
- Rotated sorted arrays
- Binary search on answer space
- 2D matrix search
- Finding boundaries

---

## Prerequisites

**Must know:**
- Array operations in TypeScript
- While loops, basic recursion
- Understanding of sorted order

---

## Success Criteria

- [ ] Implement binary search bug-free from memory
- [ ] Choose correct template for problem type
- [ ] Handle edge cases (empty, single element)
- [ ] Apply to non-obvious problems
- [ ] Explain invariants and complexity

---

## Resources

**Video:** LESSON.md
**Practice:** PROBLEMS.md
**Solutions:** SOLUTIONS.md
**Hints:** HINTS.md

---

## Tips

1. Watch all videos - patterns are critical
2. Master the templates
3. Draw the search space
4. Test boundaries carefully
5. Use UMPIRE method
6. Think aloud during problems
7. Review solutions even if correct

---

## Common Mistakes

- ❌ Using `(left + right) / 2` (overflow risk)
- ❌ Wrong loop condition (`<=` vs `<`)
- ❌ Off-by-one errors
- ❌ Not handling empty arrays
- ❌ Infinite loops from bad pointer updates
- ❌ Missing that problem needs binary search

---

## What's Next

After completion:
1. 10-minute break
2. Review scores
3. Note action items
4. Session 7: Tree Traversals

Session 7 builds on binary search with tree structures and recursive patterns.

---

**Ready?** Say: `"Claude, start session 2 6"`
