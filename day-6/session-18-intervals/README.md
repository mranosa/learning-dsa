# Day 6, Session 18: Intervals

## Overview
Master interval problems - a crucial pattern that appears in scheduling, calendar, and resource allocation problems.

**Duration:** 3-5 hours
**Problems:** 10 (1 Easy, 7 Medium, 2 Hard)
**Prerequisites:** Arrays, Sorting, Greedy algorithms

---

## Learning Objectives

By the end of this session, you will:
- ✅ Understand interval representations and operations
- ✅ Master merging overlapping intervals
- ✅ Handle interval insertions and deletions
- ✅ Solve scheduling and conflict resolution problems
- ✅ Apply greedy algorithms to interval problems

---

## Session Flow

### 1. Video (30 min)
Watch the assigned video on Interval problems and sorting strategies.

### 2. Concept Check (10 min)
Claude will quiz you on:
- Interval representation
- Sorting strategies for intervals
- Overlap detection
- Greedy approach for intervals

### 3. Tips & Tricks (5 min)
Learn interview-specific insights about:
- Common interval patterns
- Sorting strategies (start vs end)
- Edge cases in interval problems
- TypeScript interval handling

### 4. Problem Solving (3-4 hours)
Solve 10 carefully selected problems:
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

### Interval Operations
- **Merge:** Combine overlapping intervals
- **Insert:** Add new interval and merge if needed
- **Remove:** Delete intervals or overlapping portions
- **Intersect:** Find common intervals
- **Count:** Track concurrent intervals

### Common Patterns
- **Sort by start time:** For merging/grouping
- **Sort by end time:** For activity selection
- **Line sweep:** Track events at time points
- **Priority queue:** For concurrent intervals
- **Greedy selection:** For optimal scheduling

### Time Complexities
- **Sorting:** O(n log n)
- **Merging:** O(n) after sorting
- **Insertion:** O(n) in sorted list
- **Interval tree:** O(log n) operations

---

## Prerequisites

**Must know:**
- Array manipulation in TypeScript
- Sorting algorithms and comparators
- Basic greedy algorithm concepts

**Nice to have:**
- Priority queue/heap understanding
- Line sweep algorithm
- Calendar/scheduling domain knowledge

---

## Success Criteria

You're ready to move on when you can:
- [ ] Detect interval overlaps efficiently
- [ ] Merge intervals in O(n log n) time
- [ ] Handle interval insertions correctly
- [ ] Apply greedy strategies to scheduling
- [ ] Solve Medium interval problems in <25 min

---

## Resources

**Video:** See LESSON.md for link

**Readings:**
- Interval algorithms guide
- Greedy scheduling strategies
- TypeScript sorting patterns

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Always consider sorting** - Most interval problems require it
2. **Draw the intervals** - Visualize overlaps and gaps
3. **Check edge cases** - Adjacent intervals, single point
4. **Think greedy** - Often optimal for interval problems
5. **Use clear variable names** - start/end, not a/b
6. **Handle boundaries carefully** - Inclusive vs exclusive
7. **Test with examples** - Use timeline visualization

---

## Common Mistakes

**Avoid these:**
- ❌ Forgetting to sort intervals first
- ❌ Wrong comparison for overlaps (< vs <=)
- ❌ Not handling adjacent intervals correctly
- ❌ Mutating input array without checking
- ❌ Off-by-one errors in interval boundaries

---

## What's Next

After completing this session:
1. Take a 15-minute break
2. Review your performance scores
3. Practice drawing interval scenarios
4. Move to Session 19: Tries

Session 19 introduces prefix trees for efficient string operations.

---

**Ready to start?** Say: `"Claude, start session 6 18"`