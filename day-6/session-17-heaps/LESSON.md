# Heaps & Priority Queues - Complete Guide

## Video Resource
**NeetCode - Heap / Priority Queue Explained:** https://www.youtube.com/watch?v=HqPJF2L5h9U

Watch this 15-minute video for visual understanding of heap operations.

---

## What is a Heap?

A **heap** is a specialized tree-based data structure that satisfies the heap property:
- **Max Heap:** Parent >= all children
- **Min Heap:** Parent <= all children

### Key Properties
1. **Complete Binary Tree** - All levels filled except possibly the last
2. **Heap Property** - Parent-child relationship maintained
3. **Array Representation** - Efficient storage and access

---

## Array Representation

```typescript
// For 0-indexed array:
parent(i) = Math.floor((i - 1) / 2)
leftChild(i) = 2 * i + 1
rightChild(i) = 2 * i + 2

// Example heap: [10, 7, 8, 5, 2, 6, 3]
//       10
//      /  \
//     7    8
//    / \  / \
//   5  2 6  3
```

---

## Core Operations

### 1. Insert (Push) - O(log n)
```typescript
class MinHeap {
    private heap: number[] = [];

    push(val: number): void {
        this.heap.push(val);
        this.bubbleUp(this.heap.length - 1);
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
}
```

### 2. Extract Min/Max (Pop) - O(log n)
```typescript
pop(): number | undefined {
    if (this.heap.length === 0) return undefined;
    if (this.heap.length === 1) return this.heap.pop();

    const min = this.heap[0];
    this.heap[0] = this.heap.pop()!;
    this.bubbleDown(0);

    return min;
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
```

### 3. Peek - O(1)
```typescript
peek(): number | undefined {
    return this.heap[0];
}
```

### 4. Heapify - O(n)
Build heap from array efficiently:
```typescript
heapify(arr: number[]): void {
    this.heap = [...arr];
    // Start from last non-leaf node
    for (let i = Math.floor(arr.length / 2) - 1; i >= 0; i--) {
        this.bubbleDown(i);
    }
}
```

---

## Priority Queue with Custom Comparator

```typescript
class PriorityQueue<T> {
    private heap: T[] = [];
    private compare: (a: T, b: T) => number;

    constructor(compareFn: (a: T, b: T) => number) {
        this.compare = compareFn;
    }

    push(val: T): void {
        this.heap.push(val);
        this.bubbleUp(this.heap.length - 1);
    }

    private bubbleUp(index: number): void {
        while (index > 0) {
            const parentIdx = Math.floor((index - 1) / 2);
            if (this.compare(this.heap[parentIdx], this.heap[index]) <= 0) {
                break;
            }
            [this.heap[parentIdx], this.heap[index]] =
            [this.heap[index], this.heap[parentIdx]];
            index = parentIdx;
        }
    }

    // Similar pop, bubbleDown methods...
}
```

---

## Common Patterns

### Pattern 1: K-th Largest/Smallest
Use a heap of size K:
```typescript
function findKthLargest(nums: number[], k: number): number {
    // Min heap of size k for k-th largest
    const minHeap = new MinHeap();

    for (const num of nums) {
        minHeap.push(num);
        if (minHeap.size() > k) {
            minHeap.pop();
        }
    }

    return minHeap.peek()!;
}
```

### Pattern 2: Top K Elements
```typescript
function topKFrequent(nums: number[], k: number): number[] {
    // Count frequencies
    const freq = new Map<number, number>();
    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    // Min heap based on frequency
    const minHeap = new PriorityQueue<[number, number]>(
        (a, b) => a[1] - b[1]  // Compare by frequency
    );

    for (const [num, count] of freq) {
        minHeap.push([num, count]);
        if (minHeap.size() > k) {
            minHeap.pop();
        }
    }

    return minHeap.toArray().map(([num]) => num);
}
```

### Pattern 3: Two Heaps (Median)
```typescript
class MedianFinder {
    private maxHeap: PriorityQueue<number>;  // Left half
    private minHeap: PriorityQueue<number>;  // Right half

    constructor() {
        // Max heap for smaller half
        this.maxHeap = new PriorityQueue((a, b) => b - a);
        // Min heap for larger half
        this.minHeap = new PriorityQueue((a, b) => a - b);
    }

    addNum(num: number): void {
        // Always add to max heap first
        this.maxHeap.push(num);

        // Balance the heaps
        if (this.maxHeap.size() > this.minHeap.size() + 1) {
            this.minHeap.push(this.maxHeap.pop()!);
        }

        // Maintain invariant: max heap top <= min heap top
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

### Pattern 4: Merge K Sorted
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

---

## Time & Space Complexity

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Insert | O(log n) | O(1) | Bubble up |
| Extract | O(log n) | O(1) | Bubble down |
| Peek | O(1) | O(1) | Top element |
| Heapify | O(n) | O(1) | Bottom-up build |
| Delete | O(log n) | O(1) | Find + bubble |
| Search | O(n) | O(1) | Not optimized |

---

## When to Use Heaps

### Use Heaps When:
- Finding K largest/smallest elements
- Processing elements by priority
- Maintaining running median
- Merging sorted sequences
- Scheduling tasks by priority

### Don't Use Heaps When:
- Need sorted order (use sorting)
- Frequent searches by value
- Need to access middle elements
- Small, fixed-size data

---

## TypeScript Implementation Tips

```typescript
// Using built-in sort as priority queue
class SimpleHeap {
    private data: number[] = [];

    push(val: number): void {
        this.data.push(val);
        this.data.sort((a, b) => a - b);  // O(n log n) - inefficient!
    }

    pop(): number | undefined {
        return this.data.shift();  // O(n) - inefficient!
    }
}

// Better: Implement proper heap or use library
// npm install @datastructures-js/priority-queue
```

---

## Interview Tips

1. **Clarify heap type** - Min or max? Custom comparator?
2. **Consider K** - Many problems involve K elements
3. **Think streaming** - Heaps excel at online algorithms
4. **Two heaps trick** - For median and balanced partitions
5. **Implementation choice** - Library vs custom implementation

---

## Practice Problems

Start with these patterns:
1. **Basic K-element** - Kth Largest Element
2. **Frequency-based** - Top K Frequent Elements
3. **Streaming** - Find Median from Data Stream
4. **Merge** - Merge K Sorted Lists
5. **Scheduling** - Task Scheduler

Master each pattern before moving to the next!

---

## Advanced Topics

### Binary Heap Variants

#### D-ary Heap
Instead of binary (2 children), use D children:
```typescript
// For D-ary heap
parent(i) = Math.floor((i + D - 2) / D)
kthChild(i, k) = D * i + k - D + 2  // k ∈ [1, D]

// Benefits:
// - Shallower tree (log_D n height)
// - Better cache locality for large D
// - Faster decrease-key operations
```

#### Indexed Priority Queue
Maintain element positions for O(log n) updates:
```typescript
class IndexedPQ<T> {
    private heap: T[] = [];
    private indexMap: Map<T, number> = new Map();

    update(oldVal: T, newVal: T): void {
        const index = this.indexMap.get(oldVal);
        if (index !== undefined) {
            this.heap[index] = newVal;
            this.indexMap.delete(oldVal);
            this.indexMap.set(newVal, index);
            // Bubble up or down as needed
            this.heapify(index);
        }
    }
}
```

---

## Common Interview Follow-ups

### "What if we need to update priorities?"
Use an indexed heap or map to track positions.

### "How would you handle ties?"
Add a secondary comparison or timestamp:
```typescript
compare(a, b) {
    if (a.priority !== b.priority) {
        return a.priority - b.priority;
    }
    return a.timestamp - b.timestamp;
}
```

### "Can you make this thread-safe?"
Add locks or use lock-free algorithms:
```typescript
class ThreadSafeHeap {
    private mutex = new Mutex();

    async push(val: number): Promise<void> {
        await this.mutex.lock();
        try {
            // Heap operations
        } finally {
            this.mutex.unlock();
        }
    }
}
```

### "How would you persist this?"
Serialize the array representation:
```typescript
save(): string {
    return JSON.stringify(this.heap);
}

load(data: string): void {
    this.heap = JSON.parse(data);
    // Validate heap property
}
```

---

## Real-World Implementation

### Production-Ready Priority Queue
```typescript
class PriorityQueue<T> {
    private heap: T[] = [];
    private compare: (a: T, b: T) => number;
    private positions: Map<T, number> = new Map();

    constructor(
        compareFn: (a: T, b: T) => number,
        initialValues?: T[]
    ) {
        this.compare = compareFn;
        if (initialValues) {
            this.heapify(initialValues);
        }
    }

    push(val: T): void {
        this.heap.push(val);
        const index = this.heap.length - 1;
        this.positions.set(val, index);
        this.bubbleUp(index);
    }

    pop(): T | undefined {
        if (this.heap.length === 0) return undefined;
        if (this.heap.length === 1) {
            const val = this.heap.pop()!;
            this.positions.delete(val);
            return val;
        }

        const result = this.heap[0];
        this.positions.delete(result);

        const last = this.heap.pop()!;
        this.heap[0] = last;
        this.positions.set(last, 0);
        this.bubbleDown(0);

        return result;
    }

    peek(): T | undefined {
        return this.heap[0];
    }

    size(): number {
        return this.heap.length;
    }

    isEmpty(): boolean {
        return this.heap.length === 0;
    }

    contains(val: T): boolean {
        return this.positions.has(val);
    }

    remove(val: T): boolean {
        const index = this.positions.get(val);
        if (index === undefined) return false;

        this.positions.delete(val);

        if (index === this.heap.length - 1) {
            this.heap.pop();
            return true;
        }

        const last = this.heap.pop()!;
        this.heap[index] = last;
        this.positions.set(last, index);

        // Heapify at index
        const parentIdx = Math.floor((index - 1) / 2);
        if (index > 0 && this.compare(this.heap[index], this.heap[parentIdx]) < 0) {
            this.bubbleUp(index);
        } else {
            this.bubbleDown(index);
        }

        return true;
    }

    private bubbleUp(index: number): void {
        while (index > 0) {
            const parentIdx = Math.floor((index - 1) / 2);
            if (this.compare(this.heap[parentIdx], this.heap[index]) <= 0) break;

            this.swap(index, parentIdx);
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

            this.swap(index, minIndex);
            index = minIndex;
        }
    }

    private swap(i: number, j: number): void {
        [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
        this.positions.set(this.heap[i], i);
        this.positions.set(this.heap[j], j);
    }

    private heapify(arr: T[]): void {
        this.heap = [...arr];
        for (let i = 0; i < this.heap.length; i++) {
            this.positions.set(this.heap[i], i);
        }
        for (let i = Math.floor(this.heap.length / 2) - 1; i >= 0; i--) {
            this.bubbleDown(i);
        }
    }
}
```

---

**Ready to practice?** Start with Problem 1 in PROBLEMS.md