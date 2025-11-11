# Hints: Interval Problems

## Problem 1: Meeting Rooms

### Hint 1 (Gentle nudge)
Think about what it means for two meetings to conflict. When do two time intervals overlap?

### Hint 2 (Bigger hint)
Sort the meetings by start time. Once sorted, you only need to check adjacent meetings for conflicts. Why is this sufficient?

### Hint 3 (Detailed approach)
1. Sort intervals by start time: `intervals.sort((a, b) => a[0] - b[0])`
2. For each adjacent pair, check if the first meeting ends after the second starts
3. If `intervals[i-1][1] > intervals[i][0]`, there's a conflict
4. Return false if any conflict found, true otherwise

---

## Problem 2: Merge Intervals

### Hint 1 (Gentle nudge)
If you sort the intervals by start time, what property do overlapping intervals have? How can you detect when two intervals should be merged?

### Hint 2 (Bigger hint)
After sorting, iterate through intervals. Keep track of the "current" merged interval. When does the current interval need to be extended vs. when do you start a new interval?

### Hint 3 (Detailed approach)
1. Sort by start time
2. Initialize result with first interval
3. For each subsequent interval:
   - If it overlaps with last result interval (start <= lastEnd), extend the last interval
   - Use `Math.max(lastEnd, currentEnd)` to handle nested intervals
   - If no overlap, add as new interval
4. Key insight: After sorting, all intervals that need merging will be consecutive

---

## Problem 3: Insert Interval

### Hint 1 (Gentle nudge)
The intervals are already sorted. Think about three phases: intervals before the new one, intervals that overlap with the new one, and intervals after.

### Hint 2 (Bigger hint)
Process intervals in three groups:
1. All intervals that end before newInterval starts (add directly)
2. All intervals that overlap with newInterval (merge them)
3. All remaining intervals (add directly)

### Hint 3 (Detailed approach)
1. Add all intervals where `interval[1] < newInterval[0]`
2. Merge phase: while `interval[0] <= newInterval[1]`:
   - Update newInterval: `[min(starts), max(ends)]`
3. Add the merged newInterval
4. Add all remaining intervals
5. This is a single-pass O(n) solution

---

## Problem 4: Non-overlapping Intervals

### Hint 1 (Gentle nudge)
This is a classic "activity selection" problem. Think greedily: which intervals should you keep to maximize the number of non-overlapping intervals?

### Hint 2 (Bigger hint)
Sort by end time, not start time! Always keep the interval that ends earliest. Why does this greedy approach work?

### Hint 3 (Detailed approach)
1. Sort intervals by end time: `intervals.sort((a, b) => a[1] - b[1])`
2. Keep track of the end time of the last kept interval
3. For each interval:
   - If it starts before the last kept interval ends, remove it (count++)
   - Otherwise, update the end time to this interval's end
4. Return the count of removed intervals

---

## Problem 5: Meeting Rooms II

### Hint 1 (Gentle nudge)
You need to track how many meetings are happening at the same time. What data structure can help you keep track of when rooms become available?

### Hint 2 (Bigger hint)
Use a min heap to track end times of ongoing meetings. When a new meeting starts, check if any room is free (earliest end time). Alternative: Think of this as events - meeting starts and ends.

### Hint 3 (Detailed approach)
**Approach 1 (Min Heap):**
1. Sort by start time
2. Use min heap for end times
3. For each meeting, if it starts after the earliest ending meeting, reuse that room
4. Heap size = number of rooms needed

**Approach 2 (Line Sweep):**
1. Create start and end events
2. Sort all events by time
3. Track current rooms needed
4. Maximum rooms = answer

---

## Problem 6: Minimum Number of Arrows to Burst Balloons

### Hint 1 (Gentle nudge)
This is similar to the activity selection problem. Think about where to place arrows optimally to burst multiple balloons.

### Hint 2 (Bigger hint)
Sort balloons by end position. Greedily shoot arrows at the end position of balloons. When do you need a new arrow?

### Hint 3 (Detailed approach)
1. Sort by end position: `points.sort((a, b) => a[1] - b[1])`
2. First arrow at `points[0][1]`
3. For each balloon:
   - If it starts after current arrow position, need new arrow
   - Place new arrow at this balloon's end
4. Count the arrows used
5. Greedy works because shooting at end position covers maximum overlap

---

## Problem 7: Interval List Intersections

### Hint 1 (Gentle nudge)
Use two pointers, one for each list. How do you find the intersection of two intervals? When do you advance each pointer?

### Hint 2 (Bigger hint)
Intersection of [a1, a2] and [b1, b2] is [max(a1, b1), min(a2, b2)] if valid. Advance the pointer of the interval that ends first.

### Hint 3 (Detailed approach)
1. Use two pointers i and j
2. While both lists have intervals:
   - Find intersection: `[max(starts), min(ends)]`
   - If start <= end, it's a valid intersection
   - Advance pointer of interval that ends first
3. Key insight: Can't skip intervals because lists are disjoint and sorted

---

## Problem 8: My Calendar I

### Hint 1 (Gentle nudge)
For each new booking, check if it overlaps with any existing booking. How do you check if two intervals overlap?

### Hint 2 (Bigger hint)
Two events [a1, a2) and [b1, b2) overlap if `max(a1, b1) < min(a2, b2)`. Store all successful bookings.

### Hint 3 (Detailed approach)
**Simple approach:**
1. Keep list of booked events
2. For each new booking, check against all existing
3. If no overlap, add to list

**Optimized (BST):**
1. Use BST where each node is an interval
2. Navigate tree based on interval relationships
3. Insert if no overlap found
4. O(log n) average case

---

## Problem 9: Remove Covered Intervals

### Hint 1 (Gentle nudge)
An interval [a, b] is covered by [c, d] if c <= a and b <= d. How should you sort to make detection easier?

### Hint 2 (Bigger hint)
Sort by start ascending, but if starts are equal, sort by end descending. This ensures larger intervals come first when they share a start point.

### Hint 3 (Detailed approach)
1. Sort: `intervals.sort((a, b) => a[0] - b[0] || b[1] - a[1])`
2. Track the rightmost end seen so far
3. For each interval:
   - If its end > rightmost end, it's not covered (count it)
   - Update rightmost end if needed
4. The special sorting ensures parent intervals are processed before their covered children

---

## Problem 10: Employee Free Time

### Hint 1 (Gentle nudge)
First, find all the time periods when at least one employee is working. The gaps between these periods are when everyone is free.

### Hint 2 (Bigger hint)
Merge all employee schedules into one sorted list. Then merge overlapping intervals. The gaps between merged intervals are the free times.

### Hint 3 (Detailed approach)
1. Collect all intervals from all employees
2. Sort by start time
3. Merge overlapping intervals:
   - This gives you all times when someone is working
4. Find gaps between consecutive merged intervals:
   - Gap = `[merged[i-1][1], merged[i][0]]`
5. Return these gaps as free time

**Alternative with Priority Queue:**
- Use heap to efficiently process intervals in order
- Track overall busy time while processing
- More efficient for large number of employees

---

## General Tips for Interval Problems

### Pattern Recognition
1. **Sorting is usually the first step** - By start or end depending on problem
2. **Overlap detection** - `max(start1, start2) < min(end1, end2)`
3. **Greedy often works** - Especially for optimization problems
4. **Draw it out** - Visualizing on a timeline helps immensely

### Common Techniques
- **Sort by start**: For merging, grouping
- **Sort by end**: For activity selection, greedy algorithms
- **Line sweep**: For counting concurrent events
- **Two pointers**: For comparing two sorted lists
- **Priority Queue**: For dynamic interval management

### Edge Cases to Check
- Empty input
- Single interval
- All intervals overlapping
- No intervals overlapping
- Adjacent intervals (touching but not overlapping)
- Nested intervals (one completely contains another)
- Same start/end times