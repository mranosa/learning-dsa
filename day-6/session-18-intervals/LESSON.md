# Lesson: Intervals

---

## 📹 Video 1: Interval Fundamentals & Merging (15 min)

**"Merge Intervals - Leetcode 56" by NeetCode**
https://www.youtube.com/watch?v=44H3cEC2fFM

**Focus on:**
- Interval representation
- Detecting overlaps
- Sorting strategy
- Merging algorithm
- Time/space complexity

---

## 📹 Video 2: Meeting Rooms & Scheduling (15 min)

**"Meeting Rooms II - Leetcode 253" by NeetCode**
https://www.youtube.com/watch?v=FdzJmTCVyJU

**Alternative:**
https://www.youtube.com/watch?v=4MEkHeDGIl8

**Focus on:**
- Min heap approach
- Line sweep technique
- Greedy algorithm
- Activity selection
- Real-world applications

---

## 🎯 Interval Fundamentals

### What are Intervals?

An interval represents a continuous range between two points:

```typescript
type Interval = [number, number]; // [start, end]

// Examples:
const meeting = [9, 11];     // 9:00 AM to 11:00 AM
const event = [1, 5];         // Time units 1 to 5
const range = [100, 200];     // Numbers from 100 to 200
```

**Key Properties:**
- Start point and end point
- Can be inclusive or exclusive (clarify in interviews)
- May overlap with other intervals
- Can be adjacent without overlapping
- Sorting enables efficient operations

---

## 🔍 Detecting Overlaps

Two intervals overlap if they share any common time:

```typescript
// Method 1: Direct comparison
function doOverlap(a: [number, number], b: [number, number]): boolean {
    return a[0] < b[1] && b[0] < a[1];
}

// Method 2: Using max/min
function doOverlap(a: [number, number], b: [number, number]): boolean {
    return Math.max(a[0], b[0]) < Math.min(a[1], b[1]);
}

// Visual:
// a: [1, 5]    |-----|
// b: [3, 7]        |-----|
//                  ^^^ overlap

// Non-overlapping:
// a: [1, 3]    |---|
// b: [4, 6]            |---|
```

**Adjacent intervals:**
```typescript
// [1, 2] and [2, 3] - typically NOT overlapping (touching only)
// Use <= if you want to merge adjacent intervals
intervals[i][0] <= intervals[j][1]  // Merge adjacent
intervals[i][0] < intervals[j][1]   // Only overlap
```

---

## 🔧 Core Operations

### 1. Merging Intervals

Combine overlapping intervals into single intervals:

```typescript
function merge(intervals: number[][]): number[][] {
    if (intervals.length <= 1) return intervals;

    // Sort by start time - CRITICAL
    intervals.sort((a, b) => a[0] - b[0]);

    const merged: number[][] = [intervals[0]];

    for (let i = 1; i < intervals.length; i++) {
        const last = merged[merged.length - 1];
        const current = intervals[i];

        if (current[0] <= last[1]) {
            // Overlapping - extend last interval
            last[1] = Math.max(last[1], current[1]);
        } else {
            // Non-overlapping - add new interval
            merged.push(current);
        }
    }

    return merged;
}
```

**Time:** O(n log n) | **Space:** O(n)

**Key insight:** After sorting by start time, overlapping intervals are consecutive.

---

### 2. Inserting Interval

Add new interval and merge if necessary:

```typescript
function insert(intervals: number[][], newInterval: number[]): number[][] {
    const result: number[][] = [];
    let i = 0;

    // Phase 1: Add all intervals before newInterval
    while (i < intervals.length && intervals[i][1] < newInterval[0]) {
        result.push(intervals[i]);
        i++;
    }

    // Phase 2: Merge overlapping intervals with newInterval
    while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
        newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
        i++;
    }
    result.push(newInterval);

    // Phase 3: Add remaining intervals
    while (i < intervals.length) {
        result.push(intervals[i]);
        i++;
    }

    return result;
}
```

**Time:** O(n) | **Space:** O(n)

**Key insight:** Three phases - before, during overlap, after.

---

### 3. Finding Intersection

Find common intervals between two lists:

```typescript
function intersection(a: number[], b: number[]): number[] | null {
    const start = Math.max(a[0], b[0]);
    const end = Math.min(a[1], b[1]);
    return start < end ? [start, end] : null;
}

// Example:
intersection([1, 5], [3, 7])  // [3, 5]
intersection([1, 3], [4, 6])  // null
```

---

## 🧩 Common Patterns

### Pattern 1: Sort by Start Time

**Use when:** Merging, grouping, sequential processing

```typescript
intervals.sort((a, b) => a[0] - b[0]);
```

**Problems:**
- Merge Intervals
- Insert Interval
- Meeting Rooms
- Employee Free Time

---

### Pattern 2: Sort by End Time (Greedy)

**Use when:** Activity selection, optimization, minimum removals

```typescript
intervals.sort((a, b) => a[1] - b[1]);
```

**Why it works:** Choosing intervals that end earliest leaves maximum room for future intervals.

```typescript
function eraseOverlapIntervals(intervals: number[][]): number {
    if (intervals.length <= 1) return 0;

    // Sort by end time
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

**Problems:**
- Non-overlapping Intervals
- Minimum Arrows to Burst Balloons

---

### Pattern 3: Line Sweep

**Use when:** Counting concurrent events, tracking active intervals

```typescript
function minMeetingRooms(intervals: number[][]): number {
    const events: [number, number][] = [];

    for (const [start, end] of intervals) {
        events.push([start, 1]);   // Start event: +1 room
        events.push([end, -1]);    // End event: -1 room
    }

    // Sort by time; if equal, ends before starts
    events.sort((a, b) => a[0] - b[0] || a[1] - b[1]);

    let maxRooms = 0;
    let currentRooms = 0;

    for (const [time, delta] of events) {
        currentRooms += delta;
        maxRooms = Math.max(maxRooms, currentRooms);
    }

    return maxRooms;
}
```

**Time:** O(n log n) | **Space:** O(n)

**Problems:**
- Meeting Rooms II
- Number of Flowers in Bloom

---

### Pattern 4: Two Pointers

**Use when:** Comparing two sorted interval lists

```typescript
function intervalIntersection(
    firstList: number[][],
    secondList: number[][]
): number[][] {
    const result: number[][] = [];
    let i = 0, j = 0;

    while (i < firstList.length && j < secondList.length) {
        // Find intersection
        const start = Math.max(firstList[i][0], secondList[j][0]);
        const end = Math.min(firstList[i][1], secondList[j][1]);

        if (start <= end) {
            result.push([start, end]);
        }

        // Move pointer for interval that ends first
        if (firstList[i][1] < secondList[j][1]) {
            i++;
        } else {
            j++;
        }
    }

    return result;
}
```

**Time:** O(n + m) | **Space:** O(min(n, m))

---

## 📊 Complexity Analysis

### Time Complexities

| Operation | Complexity | Notes |
|-----------|-----------|-------|
| Sort intervals | O(n log n) | Usually required first step |
| Merge sorted | O(n) | Linear scan after sorting |
| Insert interval | O(n) | Already sorted input |
| Check overlap | O(1) | Simple comparison |
| Find all overlaps | O(n²) | Check every pair |

### Space Complexities

| Operation | Complexity | Notes |
|-----------|-----------|-------|
| In-place merge | O(1) | Mutate input |
| New merged array | O(n) | Store result |
| Line sweep events | O(n) | Store start/end events |
| Priority queue | O(n) | Track active intervals |

---

## 💡 Interview Tips

### Always Clarify

```typescript
// 1. Inclusive or exclusive endpoints?
[1, 3] and [3, 5]  // Overlapping or adjacent?

// 2. Can intervals be modified?
// In-place vs new array affects space complexity

// 3. What about empty input?
intervals.length === 0  // Return [] or special value?

// 4. Sorted input?
// Some problems give pre-sorted intervals
```

---

### Visualize on Timeline

```
Problem: Merge [[1,3], [2,6], [8,10], [15,18]]

Timeline:
     1   3      6        10         15  18
     |---|
       |--------|
                 |--|
                            |-----|

After merge: [1,6], [8,10], [15,18]
```

---

### Common Formulas

```typescript
// Overlap check
overlap = a[0] < b[1] && b[0] < a[1]

// Intersection
intersection = [Math.max(a[0], b[0]), Math.min(a[1], b[1])]

// Coverage (a covers b)
covers = a[0] <= b[0] && a[1] >= b[1]

// Adjacent (touching but not overlapping)
adjacent = a[1] === b[0] || b[1] === a[0]

// Gap between intervals (a before b)
gap = Math.max(0, b[0] - a[1])
```

---

## 🎓 Advanced Techniques

### Priority Queue for Dynamic Intervals

```typescript
class MinHeap {
    private heap: number[] = [];

    push(val: number): void {
        this.heap.push(val);
        this.bubbleUp(this.heap.length - 1);
    }

    pop(): number | undefined {
        if (this.heap.length === 0) return undefined;
        if (this.heap.length === 1) return this.heap.pop();

        const min = this.heap[0];
        this.heap[0] = this.heap.pop()!;
        this.bubbleDown(0);
        return min;
    }

    peek(): number | undefined {
        return this.heap[0];
    }

    size(): number {
        return this.heap.length;
    }

    private bubbleUp(index: number): void {
        while (index > 0) {
            const parent = Math.floor((index - 1) / 2);
            if (this.heap[parent] <= this.heap[index]) break;
            [this.heap[parent], this.heap[index]] =
                [this.heap[index], this.heap[parent]];
            index = parent;
        }
    }

    private bubbleDown(index: number): void {
        while (true) {
            const left = 2 * index + 1;
            const right = 2 * index + 2;
            let smallest = index;

            if (left < this.heap.length &&
                this.heap[left] < this.heap[smallest]) {
                smallest = left;
            }
            if (right < this.heap.length &&
                this.heap[right] < this.heap[smallest]) {
                smallest = right;
            }

            if (smallest === index) break;

            [this.heap[index], this.heap[smallest]] =
                [this.heap[smallest], this.heap[index]];
            index = smallest;
        }
    }
}

function minMeetingRoomsHeap(intervals: number[][]): number {
    if (!intervals.length) return 0;

    intervals.sort((a, b) => a[0] - b[0]);

    const heap = new MinHeap();
    heap.push(intervals[0][1]);

    for (let i = 1; i < intervals.length; i++) {
        if (intervals[i][0] >= heap.peek()!) {
            heap.pop();  // Room freed
        }
        heap.push(intervals[i][1]);
    }

    return heap.size();
}
```

---

### Special Sorting for Covered Intervals

```typescript
// Sort by start ascending, end descending
// Ensures parent intervals come before children
intervals.sort((a, b) => {
    if (a[0] === b[0]) {
        return b[1] - a[1];  // Longer first if same start
    }
    return a[0] - b[0];
});

// Now can detect covered intervals in one pass
function removeCoveredIntervals(intervals: number[][]): number {
    intervals.sort((a, b) =>
        a[0] === b[0] ? b[1] - a[1] : a[0] - b[0]
    );

    let count = 0;
    let prevEnd = 0;

    for (const [start, end] of intervals) {
        if (end > prevEnd) {
            count++;
            prevEnd = end;
        }
    }

    return count;
}
```

---

## 🚨 Edge Cases

Always test these:

1. **Empty input:** `[]`
2. **Single interval:** `[[1, 3]]`
3. **All overlapping:** `[[1, 5], [2, 6], [3, 7]]`
4. **No overlaps:** `[[1, 2], [3, 4], [5, 6]]`
5. **Adjacent intervals:** `[[1, 2], [2, 3]]`
6. **Nested intervals:** `[[1, 10], [2, 3], [4, 5]]`
7. **Same start:** `[[1, 3], [1, 5]]`
8. **Same end:** `[[1, 5], [3, 5]]`
9. **Point intervals:** `[[2, 2]]`
10. **Unsorted input:** `[[5, 7], [1, 3], [2, 4]]`

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **Overlap:** `a[0] < b[1] && b[0] < a[1]`
- **Sort by start:** Merging problems
- **Sort by end:** Greedy problems
- **Line sweep:** Concurrent events
- **Always visualize:** Draw timeline first

**Pattern Recognition:**
- "Merge overlapping" → Sort by start, merge in one pass
- "Minimum remove" → Sort by end, greedy selection
- "How many concurrent" → Line sweep or heap
- "Two sorted lists" → Two pointers

---

[Back to Session README](./README.md)
