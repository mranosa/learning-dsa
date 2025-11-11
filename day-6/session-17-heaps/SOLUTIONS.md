# Heap & Priority Queue Solutions

## Problem 1: Kth Largest Element in an Array

### Approach 1: Min Heap of Size K
```typescript
function findKthLargest(nums: number[], k: number): number {
    // Use min heap to keep K largest elements
    const minHeap: number[] = [];

    const bubbleUp = (index: number): void => {
        while (index > 0) {
            const parentIdx = Math.floor((index - 1) / 2);
            if (minHeap[parentIdx] <= minHeap[index]) break;
            [minHeap[parentIdx], minHeap[index]] = [minHeap[index], minHeap[parentIdx]];
            index = parentIdx;
        }
    };

    const bubbleDown = (index: number): void => {
        while (true) {
            let minIndex = index;
            const left = 2 * index + 1;
            const right = 2 * index + 2;

            if (left < minHeap.length && minHeap[left] < minHeap[minIndex]) {
                minIndex = left;
            }
            if (right < minHeap.length && minHeap[right] < minHeap[minIndex]) {
                minIndex = right;
            }

            if (minIndex === index) break;

            [minHeap[index], minHeap[minIndex]] = [minHeap[minIndex], minHeap[index]];
            index = minIndex;
        }
    };

    for (const num of nums) {
        minHeap.push(num);
        bubbleUp(minHeap.length - 1);

        if (minHeap.length > k) {
            minHeap[0] = minHeap.pop()!;
            bubbleDown(0);
        }
    }

    return minHeap[0];
}

// Time: O(n log k) - Process n elements, heap operations are O(log k)
// Space: O(k) - Heap stores at most k elements
```

### Approach 2: QuickSelect Algorithm
```typescript
function findKthLargest(nums: number[], k: number): number {
    const targetIndex = nums.length - k;

    function quickSelect(left: number, right: number): number {
        const pivot = nums[right];
        let partitionIndex = left;

        for (let i = left; i < right; i++) {
            if (nums[i] <= pivot) {
                [nums[i], nums[partitionIndex]] = [nums[partitionIndex], nums[i]];
                partitionIndex++;
            }
        }

        [nums[partitionIndex], nums[right]] = [nums[right], nums[partitionIndex]];

        if (partitionIndex === targetIndex) {
            return nums[partitionIndex];
        } else if (partitionIndex < targetIndex) {
            return quickSelect(partitionIndex + 1, right);
        } else {
            return quickSelect(left, partitionIndex - 1);
        }
    }

    return quickSelect(0, nums.length - 1);
}

// Time: O(n) average, O(n²) worst case
// Space: O(1) iterative, O(log n) recursive stack
```

---

## Problem 2: Top K Frequent Elements

### Approach 1: Min Heap with Custom Comparator
```typescript
function topKFrequent(nums: number[], k: number): number[] {
    // Count frequencies
    const freq = new Map<number, number>();
    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    // Min heap based on frequency
    const minHeap: [number, number][] = []; // [value, frequency]

    const bubbleUp = (index: number): void => {
        while (index > 0) {
            const parentIdx = Math.floor((index - 1) / 2);
            if (minHeap[parentIdx][1] <= minHeap[index][1]) break;
            [minHeap[parentIdx], minHeap[index]] = [minHeap[index], minHeap[parentIdx]];
            index = parentIdx;
        }
    };

    const bubbleDown = (index: number): void => {
        while (true) {
            let minIndex = index;
            const left = 2 * index + 1;
            const right = 2 * index + 2;

            if (left < minHeap.length && minHeap[left][1] < minHeap[minIndex][1]) {
                minIndex = left;
            }
            if (right < minHeap.length && minHeap[right][1] < minHeap[minIndex][1]) {
                minIndex = right;
            }

            if (minIndex === index) break;

            [minHeap[index], minHeap[minIndex]] = [minHeap[minIndex], minHeap[index]];
            index = minIndex;
        }
    };

    for (const [num, count] of freq) {
        minHeap.push([num, count]);
        bubbleUp(minHeap.length - 1);

        if (minHeap.length > k) {
            minHeap[0] = minHeap.pop()!;
            bubbleDown(0);
        }
    }

    return minHeap.map(([num]) => num);
}

// Time: O(n log k) - n elements, heap operations O(log k)
// Space: O(n) for frequency map + O(k) for heap
```

### Approach 2: Bucket Sort
```typescript
function topKFrequent(nums: number[], k: number): number[] {
    const freq = new Map<number, number>();
    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    // Bucket sort - index represents frequency
    const buckets: number[][] = Array(nums.length + 1).fill(null).map(() => []);

    for (const [num, count] of freq) {
        buckets[count].push(num);
    }

    const result: number[] = [];

    // Collect from highest frequency buckets
    for (let i = buckets.length - 1; i >= 0 && result.length < k; i--) {
        if (buckets[i].length > 0) {
            result.push(...buckets[i]);
        }
    }

    return result.slice(0, k);
}

// Time: O(n) - Linear scan and bucket operations
// Space: O(n) - For frequency map and buckets
```

---

## Problem 3: Find Median from Data Stream

### Approach: Two Heaps
```typescript
class MedianFinder {
    private maxHeap: number[] = []; // Left half (smaller values)
    private minHeap: number[] = []; // Right half (larger values)

    constructor() {}

    private bubbleUpMax(index: number): void {
        while (index > 0) {
            const parentIdx = Math.floor((index - 1) / 2);
            if (this.maxHeap[parentIdx] >= this.maxHeap[index]) break;
            [this.maxHeap[parentIdx], this.maxHeap[index]] =
            [this.maxHeap[index], this.maxHeap[parentIdx]];
            index = parentIdx;
        }
    }

    private bubbleDownMax(index: number): void {
        while (true) {
            let maxIndex = index;
            const left = 2 * index + 1;
            const right = 2 * index + 2;

            if (left < this.maxHeap.length &&
                this.maxHeap[left] > this.maxHeap[maxIndex]) {
                maxIndex = left;
            }
            if (right < this.maxHeap.length &&
                this.maxHeap[right] > this.maxHeap[maxIndex]) {
                maxIndex = right;
            }

            if (maxIndex === index) break;

            [this.maxHeap[index], this.maxHeap[maxIndex]] =
            [this.maxHeap[maxIndex], this.maxHeap[index]];
            index = maxIndex;
        }
    }

    private bubbleUpMin(index: number): void {
        while (index > 0) {
            const parentIdx = Math.floor((index - 1) / 2);
            if (this.minHeap[parentIdx] <= this.minHeap[index]) break;
            [this.minHeap[parentIdx], this.minHeap[index]] =
            [this.minHeap[index], this.minHeap[parentIdx]];
            index = parentIdx;
        }
    }

    private bubbleDownMin(index: number): void {
        while (true) {
            let minIndex = index;
            const left = 2 * index + 1;
            const right = 2 * index + 2;

            if (left < this.minHeap.length &&
                this.minHeap[left] < this.minHeap[minIndex]) {
                minIndex = left;
            }
            if (right < this.minHeap.length &&
                this.minHeap[right] < this.minHeap[minIndex]) {
                minIndex = right;
            }

            if (minIndex === index) break;

            [this.minHeap[index], this.minHeap[minIndex]] =
            [this.minHeap[minIndex], this.minHeap[index]];
            index = minIndex;
        }
    }

    addNum(num: number): void {
        // Add to max heap first
        this.maxHeap.push(num);
        this.bubbleUpMax(this.maxHeap.length - 1);

        // Balance: move top of max heap to min heap if needed
        if (this.maxHeap.length > this.minHeap.length + 1) {
            const val = this.maxHeap[0];
            this.maxHeap[0] = this.maxHeap.pop()!;
            if (this.maxHeap.length > 0) this.bubbleDownMax(0);

            this.minHeap.push(val);
            this.bubbleUpMin(this.minHeap.length - 1);
        }

        // Maintain invariant: max heap top <= min heap top
        if (this.minHeap.length > 0 && this.maxHeap.length > 0 &&
            this.maxHeap[0] > this.minHeap[0]) {
            // Swap tops
            const temp = this.maxHeap[0];
            this.maxHeap[0] = this.minHeap[0];
            this.minHeap[0] = temp;

            this.bubbleDownMax(0);
            this.bubbleDownMin(0);
        }
    }

    findMedian(): number {
        if (this.maxHeap.length > this.minHeap.length) {
            return this.maxHeap[0];
        }
        return (this.maxHeap[0] + this.minHeap[0]) / 2;
    }
}

// Time: addNum O(log n), findMedian O(1)
// Space: O(n) for storing all numbers
```

---

## Problem 4: Merge K Sorted Lists

### Approach: Min Heap
```typescript
class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
}

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    if (lists.length === 0) return null;

    // Min heap of nodes
    const minHeap: ListNode[] = [];

    const bubbleUp = (index: number): void => {
        while (index > 0) {
            const parentIdx = Math.floor((index - 1) / 2);
            if (minHeap[parentIdx].val <= minHeap[index].val) break;
            [minHeap[parentIdx], minHeap[index]] = [minHeap[index], minHeap[parentIdx]];
            index = parentIdx;
        }
    };

    const bubbleDown = (index: number): void => {
        while (true) {
            let minIndex = index;
            const left = 2 * index + 1;
            const right = 2 * index + 2;

            if (left < minHeap.length && minHeap[left].val < minHeap[minIndex].val) {
                minIndex = left;
            }
            if (right < minHeap.length && minHeap[right].val < minHeap[minIndex].val) {
                minIndex = right;
            }

            if (minIndex === index) break;

            [minHeap[index], minHeap[minIndex]] = [minHeap[minIndex], minHeap[index]];
            index = minIndex;
        }
    };

    // Add first node from each list
    for (const head of lists) {
        if (head) {
            minHeap.push(head);
            bubbleUp(minHeap.length - 1);
        }
    }

    const dummy = new ListNode(0);
    let curr = dummy;

    while (minHeap.length > 0) {
        // Extract minimum
        const node = minHeap[0];
        if (minHeap.length === 1) {
            minHeap.pop();
        } else {
            minHeap[0] = minHeap.pop()!;
            bubbleDown(0);
        }

        curr.next = node;
        curr = curr.next;

        // Add next node from same list
        if (node.next) {
            minHeap.push(node.next);
            bubbleUp(minHeap.length - 1);
        }
    }

    return dummy.next;
}

// Time: O(n*k*log k) where n is average list length, k is number of lists
// Space: O(k) for heap
```

---

## Problem 5: Task Scheduler

### Approach: Max Heap + Queue
```typescript
function leastInterval(tasks: string[], n: number): number {
    // Count task frequencies
    const freq = new Map<string, number>();
    for (const task of tasks) {
        freq.set(task, (freq.get(task) || 0) + 1);
    }

    // Max heap based on frequency
    const maxHeap: number[] = Array.from(freq.values());
    maxHeap.sort((a, b) => b - a);

    let time = 0;
    const queue: [number, number][] = []; // [count, availableTime]

    while (maxHeap.length > 0 || queue.length > 0) {
        time++;

        // Check if any task in queue is ready
        if (queue.length > 0 && queue[0][1] === time) {
            const [count] = queue.shift()!;
            maxHeap.push(count);
            maxHeap.sort((a, b) => b - a);
        }

        if (maxHeap.length > 0) {
            const count = maxHeap.shift()! - 1;
            if (count > 0) {
                queue.push([count, time + n + 1]);
            }
        }
    }

    return time;
}

// Time: O(n * m) where m is number of unique tasks
// Space: O(m) for frequency counting
```

---

## Problem 6: Kth Smallest Element in a Sorted Matrix

### Approach: Min Heap with Matrix Traversal
```typescript
function kthSmallest(matrix: number[][], k: number): number {
    const n = matrix.length;
    const minHeap: [number, number, number][] = []; // [value, row, col]
    const visited = new Set<string>();

    const bubbleUp = (index: number): void => {
        while (index > 0) {
            const parentIdx = Math.floor((index - 1) / 2);
            if (minHeap[parentIdx][0] <= minHeap[index][0]) break;
            [minHeap[parentIdx], minHeap[index]] = [minHeap[index], minHeap[parentIdx]];
            index = parentIdx;
        }
    };

    const bubbleDown = (index: number): void => {
        while (true) {
            let minIndex = index;
            const left = 2 * index + 1;
            const right = 2 * index + 2;

            if (left < minHeap.length && minHeap[left][0] < minHeap[minIndex][0]) {
                minIndex = left;
            }
            if (right < minHeap.length && minHeap[right][0] < minHeap[minIndex][0]) {
                minIndex = right;
            }

            if (minIndex === index) break;

            [minHeap[index], minHeap[minIndex]] = [minHeap[minIndex], minHeap[index]];
            index = minIndex;
        }
    };

    // Start with top-left element
    minHeap.push([matrix[0][0], 0, 0]);
    visited.add('0,0');

    let result = 0;

    for (let count = 0; count < k; count++) {
        // Extract minimum
        const [val, row, col] = minHeap[0];
        result = val;

        if (minHeap.length === 1) {
            minHeap.pop();
        } else {
            minHeap[0] = minHeap.pop()!;
            bubbleDown(0);
        }

        // Add adjacent elements
        if (row + 1 < n && !visited.has(`${row + 1},${col}`)) {
            minHeap.push([matrix[row + 1][col], row + 1, col]);
            bubbleUp(minHeap.length - 1);
            visited.add(`${row + 1},${col}`);
        }

        if (col + 1 < n && !visited.has(`${row},${col + 1}`)) {
            minHeap.push([matrix[row][col + 1], row, col + 1]);
            bubbleUp(minHeap.length - 1);
            visited.add(`${row},${col + 1}`);
        }
    }

    return result;
}

// Time: O(k log min(k, n²)) - Extract k elements from heap
// Space: O(min(k, n²)) - Heap and visited set size
```

---

## Problem 7: K Closest Points to Origin

### Approach: Max Heap of Size K
```typescript
function kClosest(points: number[][], k: number): number[][] {
    // Max heap based on distance (squared to avoid sqrt)
    const maxHeap: [number, number[]][] = []; // [distance², point]

    const getDistance = (point: number[]): number => {
        return point[0] * point[0] + point[1] * point[1];
    };

    const bubbleUp = (index: number): void => {
        while (index > 0) {
            const parentIdx = Math.floor((index - 1) / 2);
            if (maxHeap[parentIdx][0] >= maxHeap[index][0]) break;
            [maxHeap[parentIdx], maxHeap[index]] = [maxHeap[index], maxHeap[parentIdx]];
            index = parentIdx;
        }
    };

    const bubbleDown = (index: number): void => {
        while (true) {
            let maxIndex = index;
            const left = 2 * index + 1;
            const right = 2 * index + 2;

            if (left < maxHeap.length && maxHeap[left][0] > maxHeap[maxIndex][0]) {
                maxIndex = left;
            }
            if (right < maxHeap.length && maxHeap[right][0] > maxHeap[maxIndex][0]) {
                maxIndex = right;
            }

            if (maxIndex === index) break;

            [maxHeap[index], maxHeap[maxIndex]] = [maxHeap[maxIndex], maxHeap[index]];
            index = maxIndex;
        }
    };

    for (const point of points) {
        const dist = getDistance(point);
        maxHeap.push([dist, point]);
        bubbleUp(maxHeap.length - 1);

        if (maxHeap.length > k) {
            maxHeap[0] = maxHeap.pop()!;
            bubbleDown(0);
        }
    }

    return maxHeap.map(([_, point]) => point);
}

// Time: O(n log k) - Process n points with heap of size k
// Space: O(k) - Heap stores k points
```

---

## Problem 8: Reorganize String

### Approach: Max Heap with Greedy Placement
```typescript
function reorganizeString(s: string): string {
    // Count character frequencies
    const freq = new Map<string, number>();
    for (const char of s) {
        freq.set(char, (freq.get(char) || 0) + 1);
    }

    // Check if reorganization is possible
    const maxFreq = Math.max(...freq.values());
    if (maxFreq > Math.ceil(s.length / 2)) {
        return "";
    }

    // Max heap based on frequency
    const maxHeap: [string, number][] = Array.from(freq.entries());
    maxHeap.sort((a, b) => b[1] - a[1]);

    const result: string[] = [];
    let prevChar: string | null = null;
    let prevCount = 0;

    while (maxHeap.length > 0 || prevCount > 0) {
        // If no available characters but have previous, impossible
        if (maxHeap.length === 0 && prevCount > 0) {
            return "";
        }

        // Get most frequent character
        const [char, count] = maxHeap.shift()!;
        result.push(char);

        // Add previous character back if it still has count
        if (prevCount > 0) {
            maxHeap.push([prevChar!, prevCount]);
            maxHeap.sort((a, b) => b[1] - a[1]);
        }

        // Update previous
        prevChar = char;
        prevCount = count - 1;
    }

    return result.join('');
}

// Time: O(n log 26) = O(n) - At most 26 unique characters
// Space: O(1) - Constant space for 26 characters
```

---

## Problem 9: Ugly Number II

### Approach 1: Min Heap
```typescript
function nthUglyNumber(n: number): number {
    const minHeap: number[] = [1];
    const seen = new Set<number>([1]);

    const bubbleUp = (index: number): void => {
        while (index > 0) {
            const parentIdx = Math.floor((index - 1) / 2);
            if (minHeap[parentIdx] <= minHeap[index]) break;
            [minHeap[parentIdx], minHeap[index]] = [minHeap[index], minHeap[parentIdx]];
            index = parentIdx;
        }
    };

    const bubbleDown = (index: number): void => {
        while (true) {
            let minIndex = index;
            const left = 2 * index + 1;
            const right = 2 * index + 2;

            if (left < minHeap.length && minHeap[left] < minHeap[minIndex]) {
                minIndex = left;
            }
            if (right < minHeap.length && minHeap[right] < minHeap[minIndex]) {
                minIndex = right;
            }

            if (minIndex === index) break;

            [minHeap[index], minHeap[minIndex]] = [minHeap[minIndex], minHeap[index]];
            index = minIndex;
        }
    };

    let ugly = 0;

    for (let i = 0; i < n; i++) {
        // Extract minimum
        ugly = minHeap[0];
        if (minHeap.length === 1) {
            minHeap.pop();
        } else {
            minHeap[0] = minHeap.pop()!;
            bubbleDown(0);
        }

        // Generate new ugly numbers
        for (const factor of [2, 3, 5]) {
            const newUgly = ugly * factor;
            if (!seen.has(newUgly)) {
                seen.add(newUgly);
                minHeap.push(newUgly);
                bubbleUp(minHeap.length - 1);
            }
        }
    }

    return ugly;
}

// Time: O(n log n) - Extract n numbers, heap can grow to size n
// Space: O(n) - Heap and set storage
```

### Approach 2: Dynamic Programming (More Efficient)
```typescript
function nthUglyNumber(n: number): number {
    const ugly = [1];
    let p2 = 0, p3 = 0, p5 = 0;

    for (let i = 1; i < n; i++) {
        const next2 = ugly[p2] * 2;
        const next3 = ugly[p3] * 3;
        const next5 = ugly[p5] * 5;

        const nextUgly = Math.min(next2, next3, next5);
        ugly.push(nextUgly);

        if (nextUgly === next2) p2++;
        if (nextUgly === next3) p3++;
        if (nextUgly === next5) p5++;
    }

    return ugly[n - 1];
}

// Time: O(n) - Single pass to generate n numbers
// Space: O(n) - Store n ugly numbers
```

---

## Problem 10: Find K Pairs with Smallest Sums

### Approach: Min Heap with Smart Exploration
```typescript
function kSmallestPairs(nums1: number[], nums2: number[], k: number): number[][] {
    if (nums1.length === 0 || nums2.length === 0) return [];

    const result: number[][] = [];
    const minHeap: [number, number, number][] = []; // [sum, i, j]
    const visited = new Set<string>();

    const bubbleUp = (index: number): void => {
        while (index > 0) {
            const parentIdx = Math.floor((index - 1) / 2);
            if (minHeap[parentIdx][0] <= minHeap[index][0]) break;
            [minHeap[parentIdx], minHeap[index]] = [minHeap[index], minHeap[parentIdx]];
            index = parentIdx;
        }
    };

    const bubbleDown = (index: number): void => {
        while (true) {
            let minIndex = index;
            const left = 2 * index + 1;
            const right = 2 * index + 2;

            if (left < minHeap.length && minHeap[left][0] < minHeap[minIndex][0]) {
                minIndex = left;
            }
            if (right < minHeap.length && minHeap[right][0] < minHeap[minIndex][0]) {
                minIndex = right;
            }

            if (minIndex === index) break;

            [minHeap[index], minHeap[minIndex]] = [minHeap[minIndex], minHeap[index]];
            index = minIndex;
        }
    };

    // Start with the smallest pair
    minHeap.push([nums1[0] + nums2[0], 0, 0]);
    visited.add('0,0');

    while (result.length < k && minHeap.length > 0) {
        // Extract minimum
        const [sum, i, j] = minHeap[0];
        result.push([nums1[i], nums2[j]]);

        if (minHeap.length === 1) {
            minHeap.pop();
        } else {
            minHeap[0] = minHeap.pop()!;
            bubbleDown(0);
        }

        // Add next candidates
        if (i + 1 < nums1.length && !visited.has(`${i + 1},${j}`)) {
            minHeap.push([nums1[i + 1] + nums2[j], i + 1, j]);
            bubbleUp(minHeap.length - 1);
            visited.add(`${i + 1},${j}`);
        }

        if (j + 1 < nums2.length && !visited.has(`${i},${j + 1}`)) {
            minHeap.push([nums1[i] + nums2[j + 1], i, j + 1]);
            bubbleUp(minHeap.length - 1);
            visited.add(`${i},${j + 1}`);
        }
    }

    return result;
}

// Time: O(k log k) - Extract k pairs, heap size bounded by k
// Space: O(k) - Heap and visited set size bounded by k
```

---

## Key Takeaways

### Pattern Recognition:
1. **K-element problems** → Heap of size K
2. **Streaming median** → Two heaps (max + min)
3. **Merge sorted** → Min heap of current elements
4. **Priority scheduling** → Max heap by frequency/priority
5. **Matrix traversal** → Min heap with coordinates

### Implementation Tips:
1. **Choose correct heap type** - Min for K largest, Max for K smallest
2. **Maintain heap size** - Pop when exceeding K
3. **Handle duplicates** - Use Set for visited tracking
4. **Custom comparators** - For complex objects
5. **Array representation** - Parent at (i-1)/2, children at 2i+1 and 2i+2

### Complexity Analysis:
- **Building heap:** O(n) with heapify, O(n log n) with insertions
- **K operations:** O(k log n) or O(k log k) depending on heap size
- **Space optimization:** Keep heap at size K when possible

---

**Ready for practice?** These solutions demonstrate multiple approaches - try implementing them yourself first!