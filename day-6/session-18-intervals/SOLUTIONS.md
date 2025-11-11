# Solutions: Interval Problems

## Problem 1: Meeting Rooms

### Approach 1: Sort and Check Adjacent
```typescript
function canAttendMeetings(intervals: number[][]): boolean {
    if (intervals.length <= 1) return true;

    // Sort by start time
    intervals.sort((a, b) => a[0] - b[0]);

    // Check if any adjacent meetings overlap
    for (let i = 1; i < intervals.length; i++) {
        if (intervals[i][0] < intervals[i - 1][1]) {
            return false;  // Overlap found
        }
    }

    return true;
}
```

**Complexity:**
- Time: O(n log n) for sorting
- Space: O(1) or O(n) depending on sort implementation

### Approach 2: Brute Force (Less Efficient)
```typescript
function canAttendMeetingsBrute(intervals: number[][]): boolean {
    // Check every pair of meetings
    for (let i = 0; i < intervals.length; i++) {
        for (let j = i + 1; j < intervals.length; j++) {
            // Check if intervals i and j overlap
            if (Math.max(intervals[i][0], intervals[j][0]) <
                Math.min(intervals[i][1], intervals[j][1])) {
                return false;
            }
        }
    }
    return true;
}
```

**Complexity:**
- Time: O(n²) for checking all pairs
- Space: O(1)

---

## Problem 2: Merge Intervals

### Approach 1: Sort and Merge
```typescript
function merge(intervals: number[][]): number[][] {
    if (intervals.length <= 1) return intervals;

    // Sort by start time
    intervals.sort((a, b) => a[0] - b[0]);

    const merged: number[][] = [intervals[0]];

    for (let i = 1; i < intervals.length; i++) {
        const lastMerged = merged[merged.length - 1];
        const current = intervals[i];

        if (current[0] <= lastMerged[1]) {
            // Overlapping - extend the last merged interval
            lastMerged[1] = Math.max(lastMerged[1], current[1]);
        } else {
            // Non-overlapping - add as new interval
            merged.push(current);
        }
    }

    return merged;
}
```

**Complexity:**
- Time: O(n log n) for sorting + O(n) for merging
- Space: O(n) for result array

### Approach 2: Using Connected Components (Alternative)
```typescript
function mergeUsingGraph(intervals: number[][]): number[][] {
    const n = intervals.length;
    const graph: Map<number, number[]> = new Map();

    // Build overlap graph
    for (let i = 0; i < n; i++) {
        graph.set(i, []);
    }

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (overlap(intervals[i], intervals[j])) {
                graph.get(i)!.push(j);
                graph.get(j)!.push(i);
            }
        }
    }

    // Find connected components and merge
    const visited = new Set<number>();
    const result: number[][] = [];

    for (let i = 0; i < n; i++) {
        if (!visited.has(i)) {
            const component: number[] = [];
            dfs(i, graph, visited, component);

            // Merge all intervals in component
            let [minStart, maxEnd] = intervals[component[0]];
            for (const idx of component) {
                minStart = Math.min(minStart, intervals[idx][0]);
                maxEnd = Math.max(maxEnd, intervals[idx][1]);
            }
            result.push([minStart, maxEnd]);
        }
    }

    result.sort((a, b) => a[0] - b[0]);
    return result;
}

function overlap(a: number[], b: number[]): boolean {
    return Math.max(a[0], b[0]) <= Math.min(a[1], b[1]);
}

function dfs(node: number, graph: Map<number, number[]>,
             visited: Set<number>, component: number[]): void {
    visited.add(node);
    component.push(node);
    for (const neighbor of graph.get(node)!) {
        if (!visited.has(neighbor)) {
            dfs(neighbor, graph, visited, component);
        }
    }
}
```

**Complexity:**
- Time: O(n²) for building graph + O(n) for DFS
- Space: O(n²) for graph

---

## Problem 3: Insert Interval

### Approach 1: Linear Scan
```typescript
function insert(intervals: number[][], newInterval: number[]): number[][] {
    const result: number[][] = [];
    let i = 0;
    const n = intervals.length;

    // Add all intervals before newInterval
    while (i < n && intervals[i][1] < newInterval[0]) {
        result.push(intervals[i]);
        i++;
    }

    // Merge overlapping intervals with newInterval
    while (i < n && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
        newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
        i++;
    }
    result.push(newInterval);

    // Add remaining intervals
    while (i < n) {
        result.push(intervals[i]);
        i++;
    }

    return result;
}
```

**Complexity:**
- Time: O(n) single pass
- Space: O(n) for result

### Approach 2: Binary Search for Position
```typescript
function insertBinarySearch(intervals: number[][], newInterval: number[]): number[][] {
    if (intervals.length === 0) return [newInterval];

    // Find insertion position using binary search
    let left = 0, right = intervals.length;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (intervals[mid][0] < newInterval[0]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    // Insert at position
    intervals.splice(left, 0, newInterval);

    // Now merge overlapping intervals
    return merge(intervals);
}
```

**Complexity:**
- Time: O(log n) for binary search + O(n log n) for merge
- Space: O(n) for result

---

## Problem 4: Non-overlapping Intervals

### Approach 1: Greedy by End Time
```typescript
function eraseOverlapIntervals(intervals: number[][]): number {
    if (intervals.length <= 1) return 0;

    // Sort by end time (greedy: keep intervals that end earliest)
    intervals.sort((a, b) => a[1] - b[1]);

    let count = 0;
    let prevEnd = intervals[0][1];

    for (let i = 1; i < intervals.length; i++) {
        if (intervals[i][0] < prevEnd) {
            // Overlap - remove current interval
            count++;
        } else {
            // No overlap - update end
            prevEnd = intervals[i][1];
        }
    }

    return count;
}
```

**Complexity:**
- Time: O(n log n) for sorting
- Space: O(1)

### Approach 2: Dynamic Programming (Less Efficient)
```typescript
function eraseOverlapIntervalsDP(intervals: number[][]): number {
    if (intervals.length <= 1) return 0;

    intervals.sort((a, b) => a[0] - b[0]);
    const n = intervals.length;

    // dp[i] = max number of non-overlapping intervals ending at i
    const dp = new Array(n).fill(1);

    for (let i = 1; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (intervals[j][1] <= intervals[i][0]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
    }

    return n - Math.max(...dp);
}
```

**Complexity:**
- Time: O(n²) for DP
- Space: O(n) for DP array

---

## Problem 5: Meeting Rooms II

### Approach 1: Priority Queue (Min Heap)
```typescript
class MinHeap {
    private heap: number[] = [];

    push(val: number): void {
        this.heap.push(val);
        this.bubbleUp();
    }

    pop(): number | undefined {
        if (this.heap.length === 0) return undefined;
        if (this.heap.length === 1) return this.heap.pop();

        const min = this.heap[0];
        this.heap[0] = this.heap.pop()!;
        this.bubbleDown();
        return min;
    }

    peek(): number | undefined {
        return this.heap[0];
    }

    get size(): number {
        return this.heap.length;
    }

    private bubbleUp(): void {
        let index = this.heap.length - 1;
        while (index > 0) {
            const parentIndex = Math.floor((index - 1) / 2);
            if (this.heap[parentIndex] <= this.heap[index]) break;
            [this.heap[parentIndex], this.heap[index]] =
                [this.heap[index], this.heap[parentIndex]];
            index = parentIndex;
        }
    }

    private bubbleDown(): void {
        let index = 0;
        while (true) {
            const leftChild = 2 * index + 1;
            const rightChild = 2 * index + 2;
            let smallest = index;

            if (leftChild < this.heap.length &&
                this.heap[leftChild] < this.heap[smallest]) {
                smallest = leftChild;
            }
            if (rightChild < this.heap.length &&
                this.heap[rightChild] < this.heap[smallest]) {
                smallest = rightChild;
            }

            if (smallest === index) break;

            [this.heap[index], this.heap[smallest]] =
                [this.heap[smallest], this.heap[index]];
            index = smallest;
        }
    }
}

function minMeetingRooms(intervals: number[][]): number {
    if (intervals.length === 0) return 0;

    // Sort by start time
    intervals.sort((a, b) => a[0] - b[0]);

    // Min heap to track end times of meetings
    const heap = new MinHeap();
    heap.push(intervals[0][1]);

    for (let i = 1; i < intervals.length; i++) {
        // If earliest ending meeting has ended, reuse room
        if (intervals[i][0] >= heap.peek()!) {
            heap.pop();
        }
        heap.push(intervals[i][1]);
    }

    return heap.size;
}
```

**Complexity:**
- Time: O(n log n) for sorting and heap operations
- Space: O(n) for heap

### Approach 2: Chronological Ordering (Line Sweep)
```typescript
function minMeetingRoomsLineSweep(intervals: number[][]): number {
    const events: [number, number][] = [];

    for (const [start, end] of intervals) {
        events.push([start, 1]);   // Meeting starts
        events.push([end, -1]);     // Meeting ends
    }

    // Sort events; if times are equal, process ends before starts
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

**Complexity:**
- Time: O(n log n) for sorting
- Space: O(n) for events array

---

## Problem 6: Minimum Number of Arrows to Burst Balloons

### Approach 1: Greedy by End Position
```typescript
function findMinArrowShots(points: number[][]): number {
    if (points.length === 0) return 0;

    // Sort by end position
    points.sort((a, b) => a[1] - b[1]);

    let arrows = 1;
    let currentEnd = points[0][1];

    for (let i = 1; i < points.length; i++) {
        // If balloon starts after current arrow position
        if (points[i][0] > currentEnd) {
            arrows++;
            currentEnd = points[i][1];
        }
    }

    return arrows;
}
```

**Complexity:**
- Time: O(n log n) for sorting
- Space: O(1)

### Approach 2: Activity Selection Variant
```typescript
function findMinArrowShotsActivity(points: number[][]): number {
    if (points.length === 0) return 0;

    // Sort by start position
    points.sort((a, b) => a[0] - b[0]);

    let arrows = 1;
    let currentEnd = points[0][1];

    for (let i = 1; i < points.length; i++) {
        if (points[i][0] <= currentEnd) {
            // Overlapping - update end to minimum
            currentEnd = Math.min(currentEnd, points[i][1]);
        } else {
            // Non-overlapping - need new arrow
            arrows++;
            currentEnd = points[i][1];
        }
    }

    return arrows;
}
```

**Complexity:**
- Time: O(n log n) for sorting
- Space: O(1)

---

## Problem 7: Interval List Intersections

### Approach 1: Two Pointers
```typescript
function intervalIntersection(firstList: number[][], secondList: number[][]): number[][] {
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

**Complexity:**
- Time: O(n + m) where n and m are list lengths
- Space: O(min(n, m)) for result

### Approach 2: Merge and Find Overlaps
```typescript
function intervalIntersectionMerge(firstList: number[][], secondList: number[][]): number[][] {
    const merged: Array<[number, number, number]> = [];  // [start, end, listId]

    // Merge both lists with identifiers
    for (const interval of firstList) {
        merged.push([interval[0], interval[1], 0]);
    }
    for (const interval of secondList) {
        merged.push([interval[0], interval[1], 1]);
    }

    merged.sort((a, b) => a[0] - b[0]);

    const result: number[][] = [];
    const active: Array<[number, number]> = [[], []];

    for (const [start, end, listId] of merged) {
        // Check intersection with other list's active intervals
        const otherId = 1 - listId;
        for (const other of active[otherId]) {
            const intersectStart = Math.max(start, other[0]);
            const intersectEnd = Math.min(end, other[1]);
            if (intersectStart <= intersectEnd) {
                result.push([intersectStart, intersectEnd]);
            }
        }

        // Update active intervals
        active[listId] = active[listId].filter(interval => interval[1] >= start);
        active[listId].push([start, end]);
    }

    return result;
}
```

**Complexity:**
- Time: O((n + m) log (n + m)) for sorting
- Space: O(n + m) for merged array

---

## Problem 8: My Calendar I

### Approach 1: Linear Search
```typescript
class MyCalendar {
    private events: number[][] = [];

    book(start: number, end: number): boolean {
        // Check if new event overlaps with any existing event
        for (const [s, e] of this.events) {
            if (Math.max(start, s) < Math.min(end, e)) {
                return false;  // Overlap found
            }
        }

        this.events.push([start, end]);
        return true;
    }
}
```

**Complexity:**
- Time: O(n) per booking where n is number of events
- Space: O(n) for storing events

### Approach 2: Binary Search Tree (Optimized)
```typescript
class TreeNode {
    start: number;
    end: number;
    left: TreeNode | null = null;
    right: TreeNode | null = null;

    constructor(start: number, end: number) {
        this.start = start;
        this.end = end;
    }
}

class MyCalendarBST {
    private root: TreeNode | null = null;

    book(start: number, end: number): boolean {
        if (!this.root) {
            this.root = new TreeNode(start, end);
            return true;
        }

        return this.insert(this.root, start, end);
    }

    private insert(node: TreeNode, start: number, end: number): boolean {
        if (start >= node.end) {
            // Go right
            if (!node.right) {
                node.right = new TreeNode(start, end);
                return true;
            }
            return this.insert(node.right, start, end);
        } else if (end <= node.start) {
            // Go left
            if (!node.left) {
                node.left = new TreeNode(start, end);
                return true;
            }
            return this.insert(node.left, start, end);
        }

        // Overlap
        return false;
    }
}
```

**Complexity:**
- Time: O(log n) average, O(n) worst case per booking
- Space: O(n) for tree

---

## Problem 9: Remove Covered Intervals

### Approach 1: Sort and Track
```typescript
function removeCoveredIntervals(intervals: number[][]): number {
    // Sort by start ascending, then by end descending
    intervals.sort((a, b) => {
        if (a[0] === b[0]) {
            return b[1] - a[1];  // Larger intervals first if same start
        }
        return a[0] - b[0];
    });

    let count = 0;
    let prevEnd = 0;

    for (const [start, end] of intervals) {
        // If current interval is not covered by previous
        if (end > prevEnd) {
            count++;
            prevEnd = end;
        }
    }

    return count;
}
```

**Complexity:**
- Time: O(n log n) for sorting
- Space: O(1)

### Approach 2: Check All Pairs
```typescript
function removeCoveredIntervalsNaive(intervals: number[][]): number {
    let remaining = intervals.length;

    for (let i = 0; i < intervals.length; i++) {
        for (let j = 0; j < intervals.length; j++) {
            if (i !== j && covers(intervals[j], intervals[i])) {
                remaining--;
                break;
            }
        }
    }

    return remaining;
}

function covers(a: number[], b: number[]): boolean {
    return a[0] <= b[0] && a[1] >= b[1];
}
```

**Complexity:**
- Time: O(n²) for checking all pairs
- Space: O(1)

---

## Problem 10: Employee Free Time

### Approach 1: Merge All Intervals
```typescript
function employeeFreeTime(schedule: number[][][]): number[][] {
    // Flatten all intervals
    const allIntervals: number[][] = [];
    for (const employee of schedule) {
        for (const interval of employee) {
            allIntervals.push(interval);
        }
    }

    if (allIntervals.length === 0) return [];

    // Sort by start time
    allIntervals.sort((a, b) => a[0] - b[0]);

    // Merge overlapping intervals
    const merged: number[][] = [allIntervals[0]];

    for (let i = 1; i < allIntervals.length; i++) {
        const last = merged[merged.length - 1];
        const current = allIntervals[i];

        if (current[0] <= last[1]) {
            last[1] = Math.max(last[1], current[1]);
        } else {
            merged.push(current);
        }
    }

    // Find gaps between merged intervals
    const freeTime: number[][] = [];
    for (let i = 1; i < merged.length; i++) {
        freeTime.push([merged[i - 1][1], merged[i][0]]);
    }

    return freeTime;
}
```

**Complexity:**
- Time: O(n log n) where n is total number of intervals
- Space: O(n) for merged intervals

### Approach 2: Priority Queue
```typescript
function employeeFreeTimeHeap(schedule: number[][][]): number[][] {
    const pq = new MinHeap<[number, number, number, number]>(); // [start, end, empIndex, intIndex]

    // Add first interval from each employee
    for (let i = 0; i < schedule.length; i++) {
        if (schedule[i].length > 0) {
            pq.push([schedule[i][0][0], schedule[i][0][1], i, 0]);
        }
    }

    const result: number[][] = [];
    let prevEnd = pq.peek()![1];

    while (pq.size > 0) {
        const [start, end, empIndex, intIndex] = pq.pop()!;

        if (start > prevEnd) {
            result.push([prevEnd, start]);
        }

        prevEnd = Math.max(prevEnd, end);

        // Add next interval from same employee
        if (intIndex + 1 < schedule[empIndex].length) {
            const next = schedule[empIndex][intIndex + 1];
            pq.push([next[0], next[1], empIndex, intIndex + 1]);
        }
    }

    return result;
}
```

**Complexity:**
- Time: O(n log k) where k is number of employees
- Space: O(k) for heap