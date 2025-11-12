# Lesson: Heaps & Priority Queues

---

## 📹 Video 1: Heap Fundamentals (15 min)

**"Heap / Priority Queue - Full Course" by NeetCode**
https://www.youtube.com/watch?v=HqPJF2L5h9U

**Focus on:**
- Complete binary tree structure
- Heap property (min vs max)
- Array representation
- Parent/child index formulas

---

## 📹 Video 2: Min Heap vs Max Heap (10 min)

**"Min Heap and Max Heap Implementation" by Abdul Bari**
https://www.youtube.com/watch?v=HqPJF2L5h9U

**Alternative - Interactive Visualization:**
https://visualgo.net/en/heap

**Focus on:**
- Differences between min and max heaps
- When to use each type
- Bubble up vs bubble down operations
- Building heaps from arrays

---

## 📹 Video 3: Priority Queue Patterns (15 min)

**"Top K Elements Pattern" by NeetCode**
https://www.youtube.com/watch?v=hOjcdrqMoQ8

**Alternative:**
https://www.youtube.com/watch?v=XEmy13g1Qxc

**Focus on:**
- K-element problems
- Two-heap technique
- Merge patterns
- When heaps beat sorting

---

## 🎯 Heap Fundamentals

### What is a Heap?

A heap is a **complete binary tree** that satisfies the **heap property**:
- **Min Heap:** Parent <= all children (smallest at root)
- **Max Heap:** Parent >= all children (largest at root)

```typescript
// Min Heap Example
//       1
//      / \
//     3   2
//    / \ / \
//   7  5 6  4

// Array: [1, 3, 2, 7, 5, 6, 4]
// Parent of i: Math.floor((i - 1) / 2)
// Left child:  2 * i + 1
// Right child: 2 * i + 2
```

---

### Why Use Heaps?

**Problem:** Find K largest elements in array.

**Naive:** Sort array O(n log n), take first K.
**Better:** Use min heap of size K - O(n log K).

When K << n, this is much faster!

---

## 🏗️ Heap Implementation

### Creating Arrays for Heaps

```typescript
// Initialize empty heap
const minHeap: number[] = [];

// With initial capacity (optimization)
const minHeap: number[] = new Array(10);
let size = 0;

// From existing array (needs heapify)
const minHeap = [...arr];
heapify(minHeap);
```

---

### Index Formulas (Critical!)

```typescript
// For 0-indexed arrays:
function parent(i: number): number {
  return Math.floor((i - 1) / 2);
}

function leftChild(i: number): number {
  return 2 * i + 1;
}

function rightChild(i: number): number {
  return 2 * i + 2;
}

// Example with index 3:
// parent(3) = floor((3-1)/2) = 1
// leftChild(3) = 2*3 + 1 = 7
// rightChild(3) = 2*3 + 2 = 8
```

---

## 🔧 Core Heap Operations

### Operation 1: Insert (Push) - O(log n)

Add element at end, then bubble up to restore heap property.

```typescript
function push(heap: number[], val: number): void {
  // Add to end
  heap.push(val);

  // Bubble up from last position
  bubbleUp(heap, heap.length - 1);
}

function bubbleUp(heap: number[], index: number): void {
  while (index > 0) {
    const parentIdx = Math.floor((index - 1) / 2);

    // Min heap: stop if parent <= current
    if (heap[parentIdx] <= heap[index]) break;

    // Swap with parent
    [heap[parentIdx], heap[index]] = [heap[index], heap[parentIdx]];
    index = parentIdx;
  }
}
```

**Visual:**
```
Insert 1 into [3, 5, 4, 7, 6]:
   3              3              1
  / \            / \            / \
 5   4    →     5   4    →     5   3
/ \            / \ /          / \ / \
7  6          7  6 1         7  6 4

Bubble up: 1 < 4, swap → 1 < 3, swap → done
```

---

### Operation 2: Extract Min (Pop) - O(log n)

Remove root, replace with last element, bubble down.

```typescript
function pop(heap: number[]): number | undefined {
  if (heap.length === 0) return undefined;
  if (heap.length === 1) return heap.pop();

  // Save root (minimum)
  const min = heap[0];

  // Move last to root
  heap[0] = heap.pop()!;

  // Bubble down from root
  bubbleDown(heap, 0);

  return min;
}

function bubbleDown(heap: number[], index: number): void {
  while (true) {
    let minIndex = index;
    const left = 2 * index + 1;
    const right = 2 * index + 2;

    // Check left child
    if (left < heap.length && heap[left] < heap[minIndex]) {
      minIndex = left;
    }

    // Check right child
    if (right < heap.length && heap[right] < heap[minIndex]) {
      minIndex = right;
    }

    // If no change, done
    if (minIndex === index) break;

    // Swap with smaller child
    [heap[index], heap[minIndex]] = [heap[minIndex], heap[index]];
    index = minIndex;
  }
}
```

**Visual:**
```
Extract from [1, 3, 2, 7, 5, 6, 4]:
   1              4              2
  / \            / \            / \
 3   2    →     3   2    →     3   4
/ \ / \        / \            / \ /
7  5 6  4     7  5 6         7  5 6

Move 4 to root → bubble down: 4 > 2, swap → done
```

---

### Operation 3: Peek - O(1)

```typescript
function peek(heap: number[]): number | undefined {
  return heap[0];
}
```

---

### Operation 4: Heapify - O(n)

Build heap from unsorted array efficiently.

```typescript
function heapify(arr: number[]): void {
  // Start from last non-leaf node
  const startIdx = Math.floor(arr.length / 2) - 1;

  // Bubble down from each internal node
  for (let i = startIdx; i >= 0; i--) {
    bubbleDown(arr, i);
  }
}

// Why O(n) not O(n log n)?
// Most nodes are near bottom (small bubble down)
// Mathematical proof: sum of heights = O(n)
```

---

## 🎭 Min Heap vs Max Heap

### Min Heap Implementation

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
      const parentIdx = Math.floor((index - 1) / 2);
      if (this.heap[parentIdx] <= this.heap[index]) break;
      [this.heap[parentIdx], this.heap[index]] =
        [this.heap[index], this.heap[parentIdx]];
      index = parentIdx;
    }
  }

  private bubbleDown(index: number): void {
    while (true) {
      let minIndex = index;
      const left = 2 * index + 1;
      const right = 2 * index + 2;

      if (left < this.heap.length &&
          this.heap[left] < this.heap[minIndex]) {
        minIndex = left;
      }

      if (right < this.heap.length &&
          this.heap[right] < this.heap[minIndex]) {
        minIndex = right;
      }

      if (minIndex === index) break;

      [this.heap[index], this.heap[minIndex]] =
        [this.heap[minIndex], this.heap[index]];
      index = minIndex;
    }
  }
}
```

---

### Max Heap Implementation

```typescript
class MaxHeap {
  private heap: number[] = [];

  push(val: number): void {
    this.heap.push(val);
    this.bubbleUp(this.heap.length - 1);
  }

  pop(): number | undefined {
    if (this.heap.length === 0) return undefined;
    if (this.heap.length === 1) return this.heap.pop();

    const max = this.heap[0];
    this.heap[0] = this.heap.pop()!;
    this.bubbleDown(0);
    return max;
  }

  peek(): number | undefined {
    return this.heap[0];
  }

  private bubbleUp(index: number): void {
    while (index > 0) {
      const parentIdx = Math.floor((index - 1) / 2);
      // ONLY DIFFERENCE: >= instead of <=
      if (this.heap[parentIdx] >= this.heap[index]) break;
      [this.heap[parentIdx], this.heap[index]] =
        [this.heap[index], this.heap[parentIdx]];
      index = parentIdx;
    }
  }

  private bubbleDown(index: number): void {
    while (true) {
      let maxIndex = index;
      const left = 2 * index + 1;
      const right = 2 * index + 2;

      // ONLY DIFFERENCE: > instead of <
      if (left < this.heap.length &&
          this.heap[left] > this.heap[maxIndex]) {
        maxIndex = left;
      }

      if (right < this.heap.length &&
          this.heap[right] > this.heap[maxIndex]) {
        maxIndex = right;
      }

      if (maxIndex === index) break;

      [this.heap[index], this.heap[maxIndex]] =
        [this.heap[maxIndex], this.heap[index]];
      index = maxIndex;
    }
  }
}
```

---

### When to Use Which?

```typescript
// K LARGEST elements → MIN heap of size K
// Why? We remove smallest of the K largest
function kLargest(nums: number[], k: number): number[] {
  const minHeap = new MinHeap();
  for (const num of nums) {
    minHeap.push(num);
    if (minHeap.size() > k) minHeap.pop(); // Remove smallest
  }
  return minHeap.toArray();
}

// K SMALLEST elements → MAX heap of size K
// Why? We remove largest of the K smallest
function kSmallest(nums: number[], k: number): number[] {
  const maxHeap = new MaxHeap();
  for (const num of nums) {
    maxHeap.push(num);
    if (maxHeap.size() > k) maxHeap.pop(); // Remove largest
  }
  return maxHeap.toArray();
}
```

**Critical insight:** Think about what you're REMOVING, not keeping!

---

## 📊 Heap Complexity

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Insert | O(log n) | O(1) | Bubble up height |
| Extract | O(log n) | O(1) | Bubble down height |
| Peek | O(1) | O(1) | Just return root |
| Heapify | O(n) | O(1) | Build from array |
| Search | O(n) | O(1) | Not optimized for search |

**Height of heap:** O(log n) for n elements

---

## 🧩 Common Heap Patterns

### Pattern 1: K-th Largest/Smallest

**Problem:** Find Kth largest in array.
**Solution:** Min heap of size K.

```typescript
function findKthLargest(nums: number[], k: number): number {
  const minHeap = new MinHeap();

  for (const num of nums) {
    minHeap.push(num);
    if (minHeap.size() > k) {
      minHeap.pop(); // Remove smallest
    }
  }

  return minHeap.peek()!;
}
```

**Time:** O(n log k) | **Space:** O(k)

**Why this works:**
- Keep K largest elements in heap
- Smallest of K largest is at root
- That's the Kth largest overall!

---

### Pattern 2: Top K Frequent Elements

**Problem:** Most frequent K elements.
**Solution:** Count frequencies, min heap of size K by frequency.

```typescript
function topKFrequent(nums: number[], k: number): number[] {
  // Count frequencies
  const freq = new Map<number, number>();
  for (const num of nums) {
    freq.set(num, (freq.get(num) || 0) + 1);
  }

  // Min heap comparing by frequency
  const minHeap = new PriorityQueue<[number, number]>(
    (a, b) => a[1] - b[1]  // Compare frequencies
  );

  for (const [num, count] of freq) {
    minHeap.push([num, count]);
    if (minHeap.size() > k) {
      minHeap.pop(); // Remove least frequent
    }
  }

  return minHeap.toArray().map(([num]) => num);
}
```

**Time:** O(n log k) | **Space:** O(n)

---

### Pattern 3: Two Heaps (Median)

**Problem:** Find median of data stream.
**Solution:** Max heap for left half, min heap for right half.

```typescript
class MedianFinder {
  private maxHeap: MaxHeap; // Smaller half
  private minHeap: MinHeap; // Larger half

  constructor() {
    this.maxHeap = new MaxHeap();
    this.minHeap = new MinHeap();
  }

  addNum(num: number): void {
    // Add to max heap first
    this.maxHeap.push(num);

    // Balance: move max heap top to min heap
    if (this.maxHeap.size() > this.minHeap.size() + 1) {
      this.minHeap.push(this.maxHeap.pop()!);
    }

    // Maintain: all in max <= all in min
    if (this.minHeap.size() > 0 &&
        this.maxHeap.peek()! > this.minHeap.peek()!) {
      const temp = this.maxHeap.pop()!;
      this.maxHeap.push(this.minHeap.pop()!);
      this.minHeap.push(temp);
    }
  }

  findMedian(): number {
    if (this.maxHeap.size() > this.minHeap.size()) {
      return this.maxHeap.peek()!;
    }
    return (this.maxHeap.peek()! + this.minHeap.peek()!) / 2;
  }
}
```

**Time:** addNum O(log n), findMedian O(1) | **Space:** O(n)

---

### Pattern 4: Merge K Sorted

**Problem:** Merge K sorted lists.
**Solution:** Min heap with one element from each list.

```typescript
function mergeKLists(lists: ListNode[]): ListNode | null {
  const minHeap = new PriorityQueue<ListNode>(
    (a, b) => a.val - b.val
  );

  // Add first node from each list
  for (const head of lists) {
    if (head) minHeap.push(head);
  }

  const dummy = new ListNode(0);
  let curr = dummy;

  while (minHeap.size() > 0) {
    const node = minHeap.pop()!;
    curr.next = node;
    curr = curr.next;

    if (node.next) {
      minHeap.push(node.next);
    }
  }

  return dummy.next;
}
```

**Time:** O(n log k) where n = total nodes, k = lists | **Space:** O(k)

---

## 💡 Interview Tips

### Heap Type Selection

**Quick rules:**
- K largest → Min heap of size K
- K smallest → Max heap of size K
- Running median → Two heaps (max + min)
- Merge sorted → Min heap
- Priority scheduling → Max heap

**Say this:**
- "I'll use a min heap of size K to track the K largest elements. This gives O(n log k) instead of O(n log n) sorting."
- "For median, I'll maintain two heaps: max heap for smaller half, min heap for larger half."
- "Heap is better than sorting here because we only need K elements, not full sort."

---

### Complexity Analysis

```typescript
// ❌ Wrong approach
nums.sort((a, b) => a - b);  // O(n log n)
return nums.slice(-k);        // Get K largest

// ✅ Better with heap
const minHeap = new MinHeap();
for (const num of nums) {     // O(n log k)
  minHeap.push(num);
  if (minHeap.size() > k) minHeap.pop();
}
```

When k << n, O(n log k) << O(n log n)!

---

### TypeScript Implementation

```typescript
// Generic Priority Queue with custom comparator
class PriorityQueue<T> {
  private heap: T[] = [];

  constructor(
    private compare: (a: T, b: T) => number
  ) {}

  push(val: T): void {
    this.heap.push(val);
    this.bubbleUp(this.heap.length - 1);
  }

  pop(): T | undefined {
    if (this.heap.length === 0) return undefined;
    if (this.heap.length === 1) return this.heap.pop();

    const result = this.heap[0];
    this.heap[0] = this.heap.pop()!;
    this.bubbleDown(0);
    return result;
  }

  peek(): T | undefined {
    return this.heap[0];
  }

  size(): number {
    return this.heap.length;
  }

  private bubbleUp(index: number): void {
    while (index > 0) {
      const parentIdx = Math.floor((index - 1) / 2);
      if (this.compare(this.heap[parentIdx], this.heap[index]) <= 0) break;
      [this.heap[parentIdx], this.heap[index]] =
        [this.heap[index], this.heap[parentIdx]];
      index = parentIdx;
    }
  }

  private bubbleDown(index: number): void {
    while (true) {
      let minIndex = index;
      const left = 2 * index + 1;
      const right = 2 * index + 2;

      if (left < this.heap.length &&
          this.compare(this.heap[left], this.heap[minIndex]) < 0) {
        minIndex = left;
      }

      if (right < this.heap.length &&
          this.compare(this.heap[right], this.heap[minIndex]) < 0) {
        minIndex = right;
      }

      if (minIndex === index) break;

      [this.heap[index], this.heap[minIndex]] =
        [this.heap[minIndex], this.heap[index]];
      index = minIndex;
    }
  }
}

// Usage:
const minHeap = new PriorityQueue<number>((a, b) => a - b);
const maxHeap = new PriorityQueue<number>((a, b) => b - a);
const customHeap = new PriorityQueue<[number, number]>(
  (a, b) => a[1] - b[1]  // Compare by second element
);
```

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **Insert:** O(log n) - bubble up
- **Extract:** O(log n) - bubble down
- **Peek:** O(1) - root element
- **K largest:** Min heap of size K
- **K smallest:** Max heap of size K
- **Median:** Two heaps (max + min)

---

[Back to Session README](./README.md)
