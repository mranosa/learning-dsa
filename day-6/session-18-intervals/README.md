# Day 6, Session 18: Intervals

## Overview

Master interval problems - crucial for scheduling, calendar, and resource allocation challenges in technical interviews.

**Duration:** 2-4 hours | **Problems:** 10 (1 Easy, 7 Medium, 2 Hard)

---

## Learning Objectives

- ✅ Understand interval representation and operations
- ✅ Master merge and insert patterns
- ✅ Detect overlaps efficiently
- ✅ Apply greedy algorithms to scheduling
- ✅ Solve interval problems in O(n log n) time

---

## Session Flow

### 1. Videos (30 min)
- Interval Fundamentals & Merging (15 min)
- Meeting Rooms & Scheduling (15 min)

### 2. Concept Check (10 min)
Quiz on overlap detection, sorting strategies, merge patterns.

### 3. Tips & Tricks (5 min)
Sorting strategies, overlap formulas, boundary handling, TypeScript patterns.

### 4. Problems (2-3 hours)
1. Meeting Rooms (Easy)
2. Merge Intervals (Medium)
3. Insert Interval (Medium)
4. Non-overlapping Intervals (Medium)
5. Meeting Rooms II (Medium)
6. Minimum Number of Arrows to Burst Balloons (Medium)
7. Interval List Intersections (Medium)
8. My Calendar I (Medium)
9. Remove Covered Intervals (Medium)
10. Employee Free Time (Hard)

---

## Key Concepts

### Interval Basics
- **Representation:** `[start, end]` tuples
- **Overlap:** When two intervals share time
- **Merge:** Combine overlapping intervals
- **Insert:** Add and merge new interval
- **Sort:** Usually first step (by start or end)

### Operations
- **O(1)** - Check overlap between two intervals
- **O(n log n)** - Sort intervals
- **O(n)** - Merge sorted intervals
- **O(n)** - Insert into sorted intervals

### Patterns
- Sort by start time (merging)
- Sort by end time (greedy selection)
- Line sweep (concurrent events)
- Priority queue (active intervals)

---

## Prerequisites

**Must know:**
- Array manipulation
- Sorting with comparators
- Basic greedy concepts

---

## Success Criteria

- [ ] Detect overlaps in O(1)
- [ ] Merge intervals correctly
- [ ] Handle boundary cases (adjacent intervals)
- [ ] Explain greedy strategies
- [ ] Solve Easy problems <15 min

---

## Resources

**Video:** LESSON.md
**Practice:** PROBLEMS.md
**Solutions:** SOLUTIONS.md
**Hints:** HINTS.md

---

## Tips

1. Always visualize on timeline
2. Sort first in 90% of problems
3. Master overlap formula: `max(start1, start2) < min(end1, end2)`
4. Check adjacent vs overlapping carefully
5. Use clear variable names: `prevEnd`, `currentInterval`
6. Draw examples during planning
7. Consider inclusive vs exclusive endpoints

---

## Common Mistakes

- ❌ Forgetting to sort intervals
- ❌ Wrong overlap check (`<` vs `<=`)
- ❌ Not handling adjacent intervals [1,2] and [2,3]
- ❌ Mutating input without permission
- ❌ Off-by-one errors with boundaries
- ❌ Using wrong sort key (start vs end)

---

## What's Next

After completion:
1. 10-minute break
2. Review scores
3. Practice drawing intervals
4. Session 19: Tries

Session 19 introduces prefix trees for efficient string operations.

---

**Ready?** Say: `"Claude, start session 6 18"`
