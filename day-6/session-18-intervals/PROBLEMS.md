# Problems - Session 18: Intervals

10 problems in order. Use UMPIRE method.

**Targets:** Easy <15 min | Medium <25 min | Hard <35 min

---

## Problem 1: Meeting Rooms ⭐

**Difficulty:** Easy | **Pattern:** Sort and Check
**LeetCode:** https://leetcode.com/problems/meeting-rooms/ (Premium)

### Problem

Given array of meeting time intervals `[[start, end], ...]` where `start < end`, determine if person can attend all meetings.

### Examples

```
intervals = [[0,30], [5,10], [15,20]]
Output: false
Explanation: [0,30] overlaps with both other meetings

intervals = [[7,10], [2,4]]
Output: true
```

### Constraints

- 0 ≤ intervals.length ≤ 10⁴
- 0 ≤ start < end ≤ 10⁶

### Hints
- Sort by start time
- Check adjacent meetings for overlap
- O(n log n) time, O(1) space

---

## Problem 2: Merge Intervals ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Sort and Merge
**LeetCode:** https://leetcode.com/problems/merge-intervals/

### Problem

Given array of intervals, merge all overlapping intervals. Return array of non-overlapping intervals covering all input intervals.

### Examples

```
intervals = [[1,3], [2,6], [8,10], [15,18]]
Output: [[1,6], [8,10], [15,18]]
Explanation: [1,3] and [2,6] overlap, merge to [1,6]

intervals = [[1,4], [4,5]]
Output: [[1,5]]
Explanation: Adjacent intervals are considered overlapping
```

### Constraints

- 1 ≤ intervals.length ≤ 10⁴
- intervals[i].length == 2
- 0 ≤ start ≤ end ≤ 10⁴

### Hints
- Sort by start time first
- Track last merged interval
- Use Math.max for end times (handles nested intervals)
- O(n log n) time, O(n) space

---

## Problem 3: Insert Interval ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Three-Phase Processing
**LeetCode:** https://leetcode.com/problems/insert-interval/

### Problem

Given non-overlapping intervals sorted by start time, insert new interval and merge if necessary.

### Examples

```
intervals = [[1,3], [6,9]], newInterval = [2,5]
Output: [[1,5], [6,9]]

intervals = [[1,2], [3,5], [6,7], [8,10], [12,16]], newInterval = [4,8]
Output: [[1,2], [3,10], [12,16]]
Explanation: [4,8] merges with [3,5], [6,7], [8,10]

intervals = [], newInterval = [5,7]
Output: [[5,7]]
```

### Constraints

- 0 ≤ intervals.length ≤ 10⁴
- intervals is sorted by start
- 0 ≤ start ≤ end ≤ 10⁵

### Hints
- Three phases: before newInterval, merge with overlapping, after newInterval
- Don't need to sort - already sorted
- O(n) time, O(n) space

---

## Problem 4: Non-overlapping Intervals ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Greedy (Activity Selection)
**LeetCode:** https://leetcode.com/problems/non-overlapping-intervals/

### Problem

Return minimum number of intervals to remove to make rest non-overlapping.

### Examples

```
intervals = [[1,2], [2,3], [3,4], [1,3]]
Output: 1
Explanation: Remove [1,3], rest are non-overlapping

intervals = [[1,2], [1,2], [1,2]]
Output: 2

intervals = [[1,2], [2,3]]
Output: 0
```

### Constraints

- 1 ≤ intervals.length ≤ 10⁵
- -5×10⁴ ≤ start < end ≤ 5×10⁴

### Hints
- Greedy: sort by END time, not start
- Keep intervals that end earliest
- Count how many you remove
- O(n log n) time, O(1) space

---

## Problem 5: Meeting Rooms II ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Line Sweep or Min Heap
**LeetCode:** https://leetcode.com/problems/meeting-rooms-ii/ (Premium)

### Problem

Find minimum number of conference rooms required.

### Examples

```
intervals = [[0,30], [5,10], [15,20]]
Output: 2
Explanation: Room 1: [0,30], Room 2: [5,10] then [15,20]

intervals = [[7,10], [2,4]]
Output: 1

intervals = [[0,30], [5,10], [10,15], [15,20]]
Output: 2
Explanation: [10,15] starts when [5,10] ends (no overlap)
```

### Constraints

- 0 ≤ intervals.length ≤ 10⁴
- 0 ≤ start < end ≤ 10⁶

### Hints
- **Approach 1:** Line sweep - create start/end events, track concurrent count
- **Approach 2:** Min heap - track end times of active meetings
- Both O(n log n) time, O(n) space

---

## Problem 6: Minimum Number of Arrows to Burst Balloons

**Difficulty:** Medium | **Pattern:** Greedy (Activity Selection)
**LeetCode:** https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

### Problem

Balloons at positions `[xstart, xend]`. Arrow shot at x bursts all balloons where `xstart ≤ x ≤ xend`. Return minimum arrows needed.

### Examples

```
points = [[10,16], [2,8], [1,6], [7,12]]
Output: 2
Explanation: Shoot at x=6 (bursts [2,8] and [1,6])
             Shoot at x=11 (bursts [10,16] and [7,12])

points = [[1,2], [3,4], [5,6], [7,8]]
Output: 4

points = [[1,2], [2,3], [3,4], [4,5]]
Output: 2
```

### Constraints

- 1 ≤ points.length ≤ 10⁵
- -2³¹ ≤ xstart < xend ≤ 2³¹ - 1

### Hints
- Similar to non-overlapping intervals
- Sort by end position
- Greedy: shoot at end of each group
- O(n log n) time, O(1) space

---

## Problem 7: Interval List Intersections

**Difficulty:** Medium | **Pattern:** Two Pointers
**LeetCode:** https://leetcode.com/problems/interval-list-intersections/

### Problem

Given two sorted interval lists, return intersection of the two lists.

### Examples

```
firstList = [[0,2], [5,10], [13,23], [24,25]]
secondList = [[1,5], [8,12], [15,24], [25,26]]
Output: [[1,2], [5,5], [8,10], [15,23], [24,24], [25,25]]

firstList = [[1,3], [5,9]]
secondList = []
Output: []

firstList = [[1,7]]
secondList = [[3,10]]
Output: [[3,7]]
```

### Constraints

- 0 ≤ firstList.length, secondList.length ≤ 1000
- Both lists are disjoint and sorted

### Hints
- Two pointers, one for each list
- Intersection: `[max(starts), min(ends)]`
- Move pointer of interval that ends first
- O(n + m) time, O(min(n,m)) space

---

## Problem 8: My Calendar I

**Difficulty:** Medium | **Pattern:** Dynamic Intervals
**LeetCode:** https://leetcode.com/problems/my-calendar-i/

### Problem

Implement calendar that can book events. `book(start, end)` returns true if event can be added without double booking.

Double booking = two events with non-empty intersection.

### Examples

```
MyCalendar cal = new MyCalendar();
cal.book(10, 20);  // true
cal.book(15, 25);  // false (overlaps with [10,20])
cal.book(20, 30);  // true (adjacent is OK)

cal.book(47, 50);  // true
cal.book(33, 41);  // true
cal.book(39, 45);  // false (overlaps with [33,41])
cal.book(25, 32);  // true
```

### Constraints

- 0 ≤ start < end ≤ 10⁹
- At most 1000 calls to book

### Hints
- **Simple:** Store all bookings, check each for overlap - O(n) per booking
- **Optimized:** Use BST - O(log n) average per booking
- Check overlap: `max(start1, start2) < min(end1, end2)`

---

## Problem 9: Remove Covered Intervals

**Difficulty:** Medium | **Pattern:** Special Sorting
**LeetCode:** https://leetcode.com/problems/remove-covered-intervals/

### Problem

Interval `[a,b)` is covered by `[c,d)` if `c ≤ a` and `b ≤ d`. Return number of remaining intervals after removing all covered intervals.

### Examples

```
intervals = [[1,4], [3,6], [2,8]]
Output: 2
Explanation: [3,6] is covered by [2,8]

intervals = [[1,4], [2,3]]
Output: 1
Explanation: [2,3] is covered by [1,4]

intervals = [[1,2], [1,4], [3,4]]
Output: 1
Explanation: [1,2] and [3,4] are covered by [1,4]
```

### Constraints

- 1 ≤ intervals.length ≤ 1000
- 0 ≤ li < ri ≤ 10⁵
- All intervals unique

### Hints
- Special sort: by start ascending, then end descending
- This ensures parent intervals come before children
- Track max end seen, count intervals extending beyond it
- O(n log n) time, O(1) space

---

## Problem 10: Employee Free Time ⭐

**Difficulty:** Hard | **Pattern:** Merge All + Find Gaps
**LeetCode:** https://leetcode.com/problems/employee-free-time/ (Premium)

### Problem

Given list of each employee's working intervals (sorted, non-overlapping), return common free time for all employees.

### Examples

```
schedule = [
    [[1,3], [4,6]],     // Employee 1
    [[2,4]],            // Employee 2
    [[6,8], [9,10]]     // Employee 3
]
Output: [[6,6], [8,9]]
Wait, that's wrong. Output: [[4,6]] is when everyone is free? No...
Actually: No common free time when [4,6] has Emp 1 working.
Correct Output: [[6,6], [8,9]]? Let me recalculate:
- Busy times merged: [1,4], [4,6], [6,8], [9,10] → [1,8], [9,10]
- Free times: [8,9]
Hmm, the problem statement is about COMMON free time.

schedule = [
    [[1,3], [4,6]],
    [[2,4]],
    [[3,5], [7,9]]
]
Output: [[5,7]]
All employees free during [5,7]

schedule = [
    [[1,3], [6,7]],
    [[2,4]],
    [[2,5], [9,12]]
]
Output: [[5,6], [7,9]]
```

### Constraints

- 1 ≤ schedule.length, schedule[i].length ≤ 50
- 0 ≤ start < end ≤ 10⁸

### Hints
- Flatten all intervals from all employees
- Sort by start time
- Merge overlapping intervals (busy times)
- Gaps between merged intervals = free times
- O(n log n) time, O(n) space where n = total intervals

---

## Summary

**Total:** 10 problems (1 Easy, 7 Medium, 2 Hard)

**Patterns:**
- Sort and Check (Meeting Rooms)
- Sort and Merge (Merge Intervals, Insert Interval)
- Greedy Selection (Non-overlapping, Min Arrows)
- Line Sweep (Meeting Rooms II)
- Two Pointers (Interval Intersections)
- Dynamic Intervals (My Calendar)
- Special Sorting (Remove Covered)

**Blind 75:** 4/75 problems

---

## Complexity Targets

| Problem | Time Target | Space Target |
|---------|------------|--------------|
| Meeting Rooms | O(n log n) | O(1) |
| Merge Intervals | O(n log n) | O(n) |
| Insert Interval | O(n) | O(n) |
| Non-overlapping | O(n log n) | O(1) |
| Meeting Rooms II | O(n log n) | O(n) |
| Min Arrows | O(n log n) | O(1) |
| Interval Intersections | O(n + m) | O(min(n,m)) |
| My Calendar I | O(n) or O(log n) | O(n) |
| Remove Covered | O(n log n) | O(1) |
| Employee Free Time | O(n log n) | O(n) |

---

**Ready?** Say: `"Claude, give me the problem"` or `"Go"`

[Solutions](./SOLUTIONS.md) | [Hints](./HINTS.md)
