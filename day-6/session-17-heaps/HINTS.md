# Hints - Session 17: Heaps & Priority Queues

Progressive hints for 10 problems. Struggling is part of learning.

---

## Problem 1: Kth Largest Element

### Level 1
What data structure maintains K largest elements efficiently? Think about what gets removed.

### Level 2
Min heap of size K. Keep K largest, root is K-th largest. Why min? We remove smallest of K largest.

### Level 3
```typescript
const minHeap: number[] = [];
for (const num of nums) {
  minHeap.push(num);
  bubbleUp(minHeap.length - 1);
  if (minHeap.length > k) {
    minHeap[0] = minHeap.pop()!;
    bubbleDown(0);
  }
}
return minHeap[0];
```

---

## Problem 2: Top K Frequent Elements

### Level 1
Two-step problem: count frequencies, then find top K. What structure tracks K best?

### Level 2
Map for frequencies. Min heap of size K comparing by frequency. Remove least frequent when size > K.

### Level 3
```typescript
const freq = new Map();
for (const num of nums) freq.set(num, (freq.get(num) || 0) + 1);

const minHeap: [number, number][] = []; // [value, freq]
for (const [num, count] of freq) {
  minHeap.push([num, count]);
  bubbleUp(minHeap.length - 1);
  if (minHeap.length > k) {
    minHeap[0] = minHeap.pop()!;
    bubbleDown(0);
  }
}
```

---

## Problem 3: Find Median from Data Stream

### Level 1
How to maintain two halves of data? Think about accessing middle elements efficiently.

### Level 2
Two heaps: max heap (smaller half), min heap (larger half). Balance sizes. Median from top(s).

### Level 3
```typescript
class MedianFinder {
  maxHeap: number[] = []; // left half
  minHeap: number[] = []; // right half

  addNum(num: number): void {
    this.maxHeap.push(num);
    this.bubbleUpMax(this.maxHeap.length - 1);

    // Balance sizes
    if (this.maxHeap.length > this.minHeap.length + 1) {
      const val = this.maxHeap[0];
      this.maxHeap[0] = this.maxHeap.pop()!;
      this.bubbleDownMax(0);
      this.minHeap.push(val);
      this.bubbleUpMin(this.minHeap.length - 1);
    }

    // Maintain: max top <= min top
    if (this.minHeap.length && this.maxHeap[0] > this.minHeap[0]) {
      [this.maxHeap[0], this.minHeap[0]] = [this.minHeap[0], this.maxHeap[0]];
      this.bubbleDownMax(0);
      this.bubbleDownMin(0);
    }
  }

  findMedian(): number {
    if (this.maxHeap.length > this.minHeap.length) return this.maxHeap[0];
    return (this.maxHeap[0] + this.minHeap[0]) / 2;
  }
}
```

---

## Problem 4: Merge K Sorted Lists

### Level 1
Need smallest element across K lists at any time. What tracks minimum efficiently?

### Level 2
Min heap with one node from each list. Extract min, add to result, push next from same list.

### Level 3
```typescript
const minHeap: ListNode[] = [];
for (const head of lists) {
  if (head) {
    minHeap.push(head);
    bubbleUp(minHeap.length - 1);
  }
}

const dummy = new ListNode(0);
let curr = dummy;

while (minHeap.length > 0) {
  const node = minHeap[0];
  minHeap[0] = minHeap.pop()!;
  if (minHeap.length) bubbleDown(0);

  curr.next = node;
  curr = curr.next;

  if (node.next) {
    minHeap.push(node.next);
    bubbleUp(minHeap.length - 1);
  }
}
```

---

## Problem 5: Task Scheduler

### Level 1
High frequency tasks determine minimum time. Need to pick highest frequency available.

### Level 2
Max heap for frequencies. Queue for cooling tasks with available time. Simulate time.

### Level 3
```typescript
const freq = new Map();
for (const task of tasks) freq.set(task, (freq.get(task) || 0) + 1);

const maxHeap = Array.from(freq.values()).sort((a, b) => b - a);
const queue: [number, number][] = []; // [count, availableTime]
let time = 0;

while (maxHeap.length || queue.length) {
  time++;

  if (queue.length && queue[0][1] === time) {
    maxHeap.push(queue.shift()![0]);
    maxHeap.sort((a, b) => b - a);
  }

  if (maxHeap.length) {
    const count = maxHeap.shift()! - 1;
    if (count > 0) queue.push([count, time + n + 1]);
  }
}
```

---

## Problem 6: Kth Smallest in Matrix

### Level 1
Matrix sorted row and column. How to explore elements in sorted order?

### Level 2
Min heap starting with [0,0]. Extract K times. When extract [i,j], add [i+1,j] and [i,j+1].

### Level 3
```typescript
const minHeap: [number, number, number][] = [[matrix[0][0], 0, 0]];
const visited = new Set(['0,0']);

for (let count = 0; count < k; count++) {
  const [val, row, col] = minHeap[0];
  if (count === k - 1) return val;

  minHeap[0] = minHeap.pop()!;
  bubbleDown(0);

  if (row + 1 < n && !visited.has(`${row + 1},${col}`)) {
    minHeap.push([matrix[row + 1][col], row + 1, col]);
    visited.add(`${row + 1},${col}`);
    bubbleUp(minHeap.length - 1);
  }

  if (col + 1 < n && !visited.has(`${row},${col + 1}`)) {
    minHeap.push([matrix[row][col + 1], row, col + 1]);
    visited.add(`${row},${col + 1}`);
    bubbleUp(minHeap.length - 1);
  }
}
```

---

## Problem 7: K Closest Points

### Level 1
Don't need actual distance, what's sufficient? Think about what gets removed.

### Level 2
Squared distance (x² + y²) for comparison. Max heap of size K by distance.

### Level 3
```typescript
const maxHeap: [number, number[]][] = []; // [distance, point]

for (const point of points) {
  const dist = point[0] ** 2 + point[1] ** 2;
  maxHeap.push([dist, point]);
  bubbleUp(minHeap.length - 1);

  if (maxHeap.length > k) {
    maxHeap[0] = maxHeap.pop()!;
    bubbleDown(0);
  }
}

return maxHeap.map(([_, point]) => point);
```

---

## Problem 8: Reorganize String

### Level 1
What's max frequency for reorganization to be possible? How to place characters?

### Level 2
If any freq > (n+1)/2, impossible. Max heap by frequency. Take two most frequent alternately.

### Level 3
```typescript
const freq = new Map();
for (const char of s) freq.set(char, (freq.get(char) || 0) + 1);

const maxHeap = Array.from(freq.entries()).sort((a, b) => b[1] - a[1]);

if (maxHeap[0][1] > Math.ceil(s.length / 2)) return "";

const result: string[] = [];

while (maxHeap.length > 1) {
  const [char1, count1] = maxHeap.shift()!;
  const [char2, count2] = maxHeap.shift()!;

  result.push(char1, char2);

  if (count1 > 1) maxHeap.push([char1, count1 - 1]);
  if (count2 > 1) maxHeap.push([char2, count2 - 1]);

  maxHeap.sort((a, b) => b[1] - a[1]);
}

if (maxHeap.length) result.push(maxHeap[0][0]);
```

---

## Problem 9: Ugly Number II

### Level 1
Each ugly = previous ugly × 2, 3, or 5. How to generate in order?

### Level 2
Min heap. Start with 1. Multiply by 2,3,5 and add. Use Set for duplicates.

### Level 3
```typescript
const minHeap = [1];
const seen = new Set([1]);

for (let count = 0; count < n - 1; count++) {
  const ugly = minHeap[0];
  minHeap[0] = minHeap.pop()!;
  if (minHeap.length) bubbleDown(0);

  for (const factor of [2, 3, 5]) {
    const next = ugly * factor;
    if (!seen.has(next)) {
      seen.add(next);
      minHeap.push(next);
      bubbleUp(minHeap.length - 1);
    }
  }
}

return minHeap[0];
```

---

## Problem 10: K Pairs with Smallest Sums

### Level 1
Arrays sorted. Which pairs to consider first?

### Level 2
Min heap starting with [0,0]. Heap stores [sum, i, j]. When extract [i,j], add [i+1,j] and [i,j+1].

### Level 3
```typescript
const minHeap: [number, number, number][] = [[nums1[0] + nums2[0], 0, 0]];
const visited = new Set(['0,0']);
const result: number[][] = [];

while (result.length < k && minHeap.length) {
  const [sum, i, j] = minHeap[0];
  minHeap[0] = minHeap.pop()!;
  if (minHeap.length) bubbleDown(0);

  result.push([nums1[i], nums2[j]]);

  if (i + 1 < nums1.length && !visited.has(`${i + 1},${j}`)) {
    minHeap.push([nums1[i + 1] + nums2[j], i + 1, j]);
    visited.add(`${i + 1},${j}`);
    bubbleUp(minHeap.length - 1);
  }

  if (j + 1 < nums2.length && !visited.has(`${i},${j + 1}`)) {
    minHeap.push([nums1[i] + nums2[j + 1], i, j + 1]);
    visited.add(`${i},${j + 1}`);
    bubbleUp(minHeap.length - 1);
  }
}
```

---

## Pattern Hints

**"K largest"** → Min heap of size K (remove smallest)

**"K smallest"** → Max heap of size K (remove largest)

**"Median/middle"** → Two heaps (max + min)

**"Merge K sorted"** → Min heap of heads

**"Priority/scheduling"** → Max heap by priority

**"Generate sequence"** → Min heap with generation logic

---

## Using Hints Effectively

1. Try 10+ min before Level 1
2. Try 5+ min after each hint
3. If use Level 3, mark for review
4. Learn the pattern, not just the solution

Goal: Recognize when to use heaps instantly.

---

[Back to Problems](./PROBLEMS.md) | [Solutions](./SOLUTIONS.md)
