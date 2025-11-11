# Lesson: Interval Problems

## Video Assignment

**Watch this video:** [Merge Intervals & Meeting Rooms - NeetCode](https://www.youtube.com/watch?v=44H3cEC2fFM)

**Duration:** 30 minutes

**Backup videos:**
- [Interval Problems Playlist](https://www.youtube.com/watch?v=Zb4eRjuPHbM)
- [Meeting Rooms Problem](https://www.youtube.com/watch?v=PaJxqZVPhbg)

---

## Core Concepts

### 1. What are Intervals?

An interval represents a range between two points:
```typescript
type Interval = [number, number]; // [start, end]

// Examples:
const meeting = [9, 11];     // 9:00 AM to 11:00 AM
const task = [1, 5];         // Time units 1 to 5
const range = [100, 200];    // Values from 100 to 200
```

**Key Properties:**
- Start point and end point
- Can be inclusive or exclusive
- May overlap with other intervals
- Can be sorted by start or end

### 2. Detecting Overlaps

Two intervals overlap if they share any common time:

```typescript
function doOverlap(a: [number, number], b: [number, number]): boolean {
    // Overlap if a starts before b ends AND b starts before a ends
    return a[0] < b[1] && b[0] < a[1];
}

// Visual representation:
// a: [1, 5]    |-----|
// b: [3, 7]        |-----|
//                  ^^^ overlap
```

**Non-overlapping conditions:**
- `a` ends before `b` starts: `a[1] <= b[0]`
- `b` ends before `a` starts: `b[1] <= a[0]`

### 3. Merging Intervals

Combining overlapping intervals into single intervals:

```typescript
function merge(intervals: number[][]): number[][] {
    if (intervals.length <= 1) return intervals;

    // Sort by start time
    intervals.sort((a, b) => a[0] - b[0]);

    const merged: number[][] = [intervals[0]];

    for (let i = 1; i < intervals.length; i++) {
        const last = merged[merged.length - 1];
        const current = intervals[i];

        if (last[1] >= current[0]) {
            // Overlapping - merge
            last[1] = Math.max(last[1], current[1]);
        } else {
            // Non-overlapping - add new
            merged.push(current);
        }
    }

    return merged;
}
```

### 4. Interval Insertion

Adding a new interval and merging if necessary:

```typescript
function insert(intervals: number[][], newInterval: number[]): number[][] {
    const result: number[][] = [];
    let i = 0;

    // Add all intervals before newInterval
    while (i < intervals.length && intervals[i][1] < newInterval[0]) {
        result.push(intervals[i]);
        i++;
    }

    // Merge overlapping intervals
    while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
        newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
        i++;
    }
    result.push(newInterval);

    // Add remaining intervals
    while (i < intervals.length) {
        result.push(intervals[i]);
        i++;
    }

    return result;
}
```

---

## Interval Patterns

### Pattern 1: Sort and Iterate

Most interval problems start with sorting:

```typescript
// Sort by start time for merging
intervals.sort((a, b) => a[0] - b[0]);

// Sort by end time for activity selection
intervals.sort((a, b) => a[1] - b[1]);
```

### Pattern 2: Greedy Selection

For finding minimum intervals to remove:

```typescript
function eraseOverlapIntervals(intervals: number[][]): number {
    if (intervals.length <= 1) return 0;

    // Sort by end time (greedy: earliest ending first)
    intervals.sort((a, b) => a[1] - b[1]);

    let count = 0;
    let prevEnd = intervals[0][1];

    for (let i = 1; i < intervals.length; i++) {
        if (intervals[i][0] < prevEnd) {
            // Overlap - remove current
            count++;
        } else {
            // No overlap - update end
            prevEnd = intervals[i][1];
        }
    }

    return count;
}
```

### Pattern 3: Line Sweep

Track events at time points:

```typescript
function minMeetingRooms(intervals: number[][]): number {
    const events: [number, number][] = [];

    for (const [start, end] of intervals) {
        events.push([start, 1]);   // Start event
        events.push([end, -1]);     // End event
    }

    // Sort by time, starts before ends if same time
    events.sort((a, b) => a[0] - b[0] || b[1] - a[1]);

    let maxRooms = 0;
    let currentRooms = 0;

    for (const [time, delta] of events) {
        currentRooms += delta;
        maxRooms = Math.max(maxRooms, currentRooms);
    }

    return maxRooms;
}
```

### Pattern 4: Priority Queue

For tracking active intervals:

```typescript
import { MinHeap } from './heap';

function minMeetingRooms(intervals: number[][]): number {
    if (!intervals.length) return 0;

    // Sort by start time
    intervals.sort((a, b) => a[0] - b[0]);

    // Min heap to track end times
    const heap = new MinHeap<number>();
    heap.push(intervals[0][1]);

    for (let i = 1; i < intervals.length; i++) {
        // If earliest ending meeting has ended
        if (intervals[i][0] >= heap.peek()) {
            heap.pop();
        }
        heap.push(intervals[i][1]);
    }

    return heap.size();
}
```

---

## Common Operations

### 1. Check if Intervals Overlap

```typescript
const overlap = (a: number[], b: number[]): boolean => {
    return Math.max(a[0], b[0]) < Math.min(a[1], b[1]);
};
```

### 2. Find Intersection

```typescript
const intersection = (a: number[], b: number[]): number[] | null => {
    const start = Math.max(a[0], b[0]);
    const end = Math.min(a[1], b[1]);
    return start < end ? [start, end] : null;
};
```

### 3. Check if Interval Covers Another

```typescript
const covers = (a: number[], b: number[]): boolean => {
    return a[0] <= b[0] && a[1] >= b[1];
};
```

### 4. Calculate Gap Between Intervals

```typescript
const gap = (a: number[], b: number[]): number => {
    // Assumes a comes before b
    return Math.max(0, b[0] - a[1]);
};
```

---

## Advanced Techniques

### 1. Interval Tree

For efficient interval queries:

```typescript
class IntervalTreeNode {
    interval: [number, number];
    max: number;  // Maximum end in subtree
    left: IntervalTreeNode | null = null;
    right: IntervalTreeNode | null = null;

    constructor(interval: [number, number]) {
        this.interval = interval;
        this.max = interval[1];
    }
}
```

### 2. Sweep Line with Events

```typescript
interface Event {
    time: number;
    type: 'start' | 'end';
    intervalId: number;
}

function processIntervals(intervals: number[][]): void {
    const events: Event[] = [];

    intervals.forEach((interval, id) => {
        events.push({ time: interval[0], type: 'start', intervalId: id });
        events.push({ time: interval[1], type: 'end', intervalId: id });
    });

    events.sort((a, b) => {
        if (a.time !== b.time) return a.time - b.time;
        return a.type === 'end' ? -1 : 1; // Ends before starts
    });

    // Process events...
}
```

### 3. Interval Scheduling

Maximum number of non-overlapping intervals:

```typescript
function intervalScheduling(intervals: number[][]): number[][] {
    // Sort by end time (greedy)
    intervals.sort((a, b) => a[1] - b[1]);

    const selected: number[][] = [];
    let lastEnd = -Infinity;

    for (const interval of intervals) {
        if (interval[0] >= lastEnd) {
            selected.push(interval);
            lastEnd = interval[1];
        }
    }

    return selected;
}
```

---

## Edge Cases to Consider

1. **Empty input:** `[]`
2. **Single interval:** `[[1, 3]]`
3. **All overlapping:** `[[1, 5], [2, 6], [3, 7]]`
4. **No overlapping:** `[[1, 2], [3, 4], [5, 6]]`
5. **Adjacent intervals:** `[[1, 2], [2, 3]]` (check boundary handling)
6. **Nested intervals:** `[[1, 10], [2, 3], [4, 5]]`
7. **Same start or end:** `[[1, 3], [1, 5]]` or `[[1, 5], [3, 5]]`
8. **Point intervals:** `[[2, 2]]`

---

## Time & Space Complexity Analysis

| Operation | Time | Space | Notes |
|-----------|------|-------|--------|
| Sort intervals | O(n log n) | O(1) or O(n) | Depends on sort implementation |
| Merge intervals | O(n log n) | O(n) | Sorting + linear scan |
| Insert interval | O(n) | O(n) | Linear scan |
| Remove overlaps | O(n log n) | O(1) | Greedy after sorting |
| Meeting rooms | O(n log n) | O(n) | Various approaches |
| Interval intersection | O(n + m) | O(min(n, m)) | Two pointer technique |

---

## Common Interview Questions

1. **"How do you handle inclusive vs exclusive intervals?"**
   - Clarify with interviewer
   - Adjust comparisons accordingly
   - Document your assumption

2. **"What if intervals can have the same start time?"**
   - Secondary sort by end time
   - Or by interval length
   - Depends on problem requirements

3. **"Can intervals be modified in place?"**
   - Ask if mutation is allowed
   - Consider space complexity trade-offs

4. **"How would you handle streaming intervals?"**
   - Discuss online algorithms
   - Interval tree for dynamic updates
   - Trade-offs of different data structures

---

## Practice Problems

Start with these in order:
1. Meeting Rooms (Easy) - Simple overlap check
2. Merge Intervals (Medium) - Fundamental operation
3. Insert Interval (Medium) - Build on merge
4. Non-overlapping Intervals (Medium) - Greedy approach
5. Meeting Rooms II (Medium) - Multiple techniques

Then advance to:
6. Minimum Number of Arrows (Medium) - Greedy variant
7. Interval List Intersections (Medium) - Two pointers
8. My Calendar I (Medium) - Dynamic intervals
9. Remove Covered Intervals (Medium) - Subset relationships
10. Employee Free Time (Hard) - Complex merging

---

**Ready for the concept check?** Say: "I watched the video"