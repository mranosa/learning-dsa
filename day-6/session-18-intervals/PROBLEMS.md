# Problems: Interval Challenges

## Problem 1: Meeting Rooms (Easy)

**LeetCode:** [252 - Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) (Premium)

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]` where `si < ei`, determine if a person could attend all meetings.

### Examples

```typescript
// Example 1:
const intervals1 = [[0, 30], [5, 10], [15, 20]];
console.log(canAttendMeetings(intervals1));
// Output: false
// Explanation: [0,30] overlaps with both [5,10] and [15,20]

// Example 2:
const intervals2 = [[7, 10], [2, 4]];
console.log(canAttendMeetings(intervals2));
// Output: true
// Explanation: No overlaps between meetings
```

### Constraints
- 0 <= intervals.length <= 10^4
- 0 <= start < end <= 10^6

### Your Task
Implement `canAttendMeetings(intervals: number[][]): boolean`

---

## Problem 2: Merge Intervals (Medium)

**LeetCode:** [56 - Merge Intervals](https://leetcode.com/problems/merge-intervals/)

Given an array of intervals where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

### Examples

```typescript
// Example 1:
const intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]];
console.log(merge(intervals1));
// Output: [[1, 6], [8, 10], [15, 18]]
// Explanation: [1,3] and [2,6] overlap, merge them into [1,6]

// Example 2:
const intervals2 = [[1, 4], [4, 5]];
console.log(merge(intervals2));
// Output: [[1, 5]]
// Explanation: Intervals [1,4] and [4,5] are considered overlapping

// Example 3:
const intervals3 = [[1, 4], [0, 4]];
console.log(merge(intervals3));
// Output: [[0, 4]]
```

### Constraints
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4

### Your Task
Implement `merge(intervals: number[][]): number[][]`

---

## Problem 3: Insert Interval (Medium)

**LeetCode:** [57 - Insert Interval](https://leetcode.com/problems/insert-interval/)

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

### Examples

```typescript
// Example 1:
const intervals1 = [[1, 3], [6, 9]];
const newInterval1 = [2, 5];
console.log(insert(intervals1, newInterval1));
// Output: [[1, 5], [6, 9]]

// Example 2:
const intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]];
const newInterval2 = [4, 8];
console.log(insert(intervals2, newInterval2));
// Output: [[1, 2], [3, 10], [12, 16]]
// Explanation: newInterval overlaps with [3,5], [6,7], [8,10]

// Example 3:
const intervals3: number[][] = [];
const newInterval3 = [5, 7];
console.log(insert(intervals3, newInterval3));
// Output: [[5, 7]]
```

### Constraints
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^5
- intervals is sorted by starti in ascending order
- newInterval.length == 2
- 0 <= start <= end <= 10^5

### Your Task
Implement `insert(intervals: number[][], newInterval: number[]): number[][]`

---

## Problem 4: Non-overlapping Intervals (Medium)

**LeetCode:** [435 - Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

Given an array of intervals `intervals` where `intervals[i] = [starti, endi]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

### Examples

```typescript
// Example 1:
const intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]];
console.log(eraseOverlapIntervals(intervals1));
// Output: 1
// Explanation: Remove [1,3] to make non-overlapping

// Example 2:
const intervals2 = [[1, 2], [1, 2], [1, 2]];
console.log(eraseOverlapIntervals(intervals2));
// Output: 2
// Explanation: Remove two [1,2] to make non-overlapping

// Example 3:
const intervals3 = [[1, 2], [2, 3]];
console.log(eraseOverlapIntervals(intervals3));
// Output: 0
// Explanation: Already non-overlapping
```

### Constraints
- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5 * 10^4 <= starti < endi <= 5 * 10^4

### Your Task
Implement `eraseOverlapIntervals(intervals: number[][]): number`

---

## Problem 5: Meeting Rooms II (Medium)

**LeetCode:** [253 - Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (Premium)

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]` where `si < ei`, find the minimum number of conference rooms required.

### Examples

```typescript
// Example 1:
const intervals1 = [[0, 30], [5, 10], [15, 20]];
console.log(minMeetingRooms(intervals1));
// Output: 2
// Explanation: Room 1: [0,30], Room 2: [5,10] and [15,20]

// Example 2:
const intervals2 = [[7, 10], [2, 4]];
console.log(minMeetingRooms(intervals2));
// Output: 1
// Explanation: One room is enough for both meetings

// Example 3:
const intervals3 = [[0, 30], [5, 10], [10, 15], [15, 20]];
console.log(minMeetingRooms(intervals3));
// Output: 2
// Explanation: [5,10] and [10,15] don't overlap (one ends when other starts)
```

### Constraints
- 0 <= intervals.length <= 10^4
- 0 <= start < end <= 10^6

### Your Task
Implement `minMeetingRooms(intervals: number[][]): number`

---

## Problem 6: Minimum Number of Arrows to Burst Balloons (Medium)

**LeetCode:** [452 - Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `points` where `points[i] = [xstart, xend]` denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Return the minimum number of arrows that must be shot to burst all balloons.

### Examples

```typescript
// Example 1:
const points1 = [[10, 16], [2, 8], [1, 6], [7, 12]];
console.log(findMinArrowShots(points1));
// Output: 2
// Explanation: Shoot at x=6 (burst [2,8] and [1,6]) and x=11 (burst [10,16] and [7,12])

// Example 2:
const points2 = [[1, 2], [3, 4], [5, 6], [7, 8]];
console.log(findMinArrowShots(points2));
// Output: 4
// Explanation: One arrow for each balloon

// Example 3:
const points3 = [[1, 2], [2, 3], [3, 4], [4, 5]];
console.log(findMinArrowShots(points3));
// Output: 2
// Explanation: Shoot at x=2 and x=4
```

### Constraints
- 1 <= points.length <= 10^5
- points[i].length == 2
- -2^31 <= xstart < xend <= 2^31 - 1

### Your Task
Implement `findMinArrowShots(points: number[][]): number`

---

## Problem 7: Interval List Intersections (Medium)

**LeetCode:** [986 - Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)

You are given two lists of closed intervals, `firstList` and `secondList`, where `firstList[i] = [starti, endi]` and `secondList[j] = [startj, endj]`. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

### Examples

```typescript
// Example 1:
const firstList1 = [[0, 2], [5, 10], [13, 23], [24, 25]];
const secondList1 = [[1, 5], [8, 12], [15, 24], [25, 26]];
console.log(intervalIntersection(firstList1, secondList1));
// Output: [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

// Example 2:
const firstList2 = [[1, 3], [5, 9]];
const secondList2: number[][] = [];
console.log(intervalIntersection(firstList2, secondList2));
// Output: []

// Example 3:
const firstList3 = [[1, 7]];
const secondList3 = [[3, 10]];
console.log(intervalIntersection(firstList3, secondList3));
// Output: [[3, 7]]
```

### Constraints
- 0 <= firstList.length, secondList.length <= 1000
- firstList.length + secondList.length >= 1
- 0 <= starti < endi <= 10^9
- endi < starti+1
- 0 <= startj < endj <= 10^9
- endj < startj+1

### Your Task
Implement `intervalIntersection(firstList: number[][], secondList: number[][]): number[][]`

---

## Problem 8: My Calendar I (Medium)

**LeetCode:** [729 - My Calendar I](https://leetcode.com/problems/my-calendar-i/)

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events).

Implement the MyCalendar class:
- `MyCalendar()` Initializes the calendar object.
- `boolean book(int start, int end)` Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

### Examples

```typescript
// Example:
const myCalendar = new MyCalendar();
console.log(myCalendar.book(10, 20)); // true
console.log(myCalendar.book(15, 25)); // false (overlaps with [10, 20])
console.log(myCalendar.book(20, 30)); // true (no overlap, adjacent is OK)

// Example 2:
const cal = new MyCalendar();
console.log(cal.book(47, 50)); // true
console.log(cal.book(33, 41)); // true
console.log(cal.book(39, 45)); // false (overlaps with [33, 41])
console.log(cal.book(33, 42)); // false (overlaps with [33, 41])
console.log(cal.book(25, 32)); // true
```

### Constraints
- 0 <= start < end <= 10^9
- At most 1000 calls will be made to book

### Your Task
Implement the `MyCalendar` class with its `book` method

---

## Problem 9: Remove Covered Intervals (Medium)

**LeetCode:** [1288 - Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/)

Given an array intervals where `intervals[i] = [li, ri]` represent the interval `[li, ri)`, remove all intervals that are covered by another interval in the list.

The interval `[a, b)` is covered by the interval `[c, d)` if and only if `c <= a` and `b <= d`.

Return the number of remaining intervals.

### Examples

```typescript
// Example 1:
const intervals1 = [[1, 4], [3, 6], [2, 8]];
console.log(removeCoveredIntervals(intervals1));
// Output: 2
// Explanation: [3,6] is covered by [2,8], so remove it

// Example 2:
const intervals2 = [[1, 4], [2, 3]];
console.log(removeCoveredIntervals(intervals2));
// Output: 1
// Explanation: [2,3] is covered by [1,4]

// Example 3:
const intervals3 = [[1, 2], [1, 4], [3, 4]];
console.log(removeCoveredIntervals(intervals3));
// Output: 1
// Explanation: [1,2] and [3,4] are covered by [1,4]
```

### Constraints
- 1 <= intervals.length <= 1000
- intervals[i].length == 2
- 0 <= li < ri <= 10^5
- All the given intervals are unique

### Your Task
Implement `removeCoveredIntervals(intervals: number[][]): number`

---

## Problem 10: Employee Free Time (Hard)

**LeetCode:** [759 - Employee Free Time](https://leetcode.com/problems/employee-free-time/) (Premium)

We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

### Examples

```typescript
// Example 1:
const schedule1 = [
    [[1, 3], [4, 6]],    // Employee 1
    [[2, 4]],            // Employee 2
    [[6, 8], [9, 10]]    // Employee 3
];
console.log(employeeFreeTime(schedule1));
// Output: [[4, 6], [8, 9]]
// Explanation: All employees are free during [4,6] and [8,9]

// Example 2:
const schedule2 = [
    [[1, 3]],
    [[2, 4]],
    [[3, 5], [7, 9]]
];
console.log(employeeFreeTime(schedule2));
// Output: [[5, 7]]
// Explanation: All employees are free during [5,7]

// Example 3:
const schedule3 = [
    [[1, 3], [6, 7]],
    [[2, 4]],
    [[2, 5], [9, 12]]
];
console.log(employeeFreeTime(schedule3));
// Output: [[5, 6], [7, 9]]
```

### Constraints
- 1 <= schedule.length, schedule[i].length <= 50
- 0 <= schedule[i][j][0] < schedule[i][j][1] <= 10^8
- schedule[i] is sorted by start time

### Your Task
Implement `employeeFreeTime(schedule: number[][][]): number[][]`

---

## Tips for All Problems

1. **Always sort first** - Most interval problems require sorted input
2. **Draw it out** - Visualize intervals on a timeline
3. **Consider edge cases** - Empty arrays, single intervals, adjacent intervals
4. **Choose the right sort** - By start for merging, by end for greedy
5. **Track key variables** - Previous end, current count, etc.
6. **Think about boundaries** - Inclusive vs exclusive endpoints
7. **Use clear variable names** - `prevEnd` not `p`, `currentInterval` not `curr`

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
| My Calendar I | O(n²) or O(n log n) | O(n) |
| Remove Covered | O(n log n) | O(1) |
| Employee Free Time | O(n log n) | O(n) |

Where n = number of intervals, m = size of second list