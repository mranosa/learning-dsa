# Heap & Priority Queue Problems

## Problem 1: Kth Largest Element in an Array
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

Note that it is the `kth` largest element in sorted order, not the `kth` distinct element.

```typescript
function findKthLargest(nums: number[], k: number): number {
    // Your code here
}
```

**Examples:**
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

---

## Problem 2: Top K Frequent Elements
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

```typescript
function topKFrequent(nums: number[], k: number): number[] {
    // Your code here
}
```

**Examples:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
```

---

## Problem 3: Find Median from Data Stream
**Difficulty:** Hard
**LeetCode:** https://leetcode.com/problems/find-median-from-data-stream/

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

Implement the MedianFinder class:
- `MedianFinder()` initializes the object.
- `void addNum(int num)` adds the integer num from the data stream.
- `double findMedian()` returns the median of all elements so far.

```typescript
class MedianFinder {
    constructor() {
        // Your code here
    }

    addNum(num: number): void {
        // Your code here
    }

    findMedian(): number {
        // Your code here
    }
}
```

**Example:**
```
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

---

## Problem 4: Merge K Sorted Lists
**Difficulty:** Hard
**LeetCode:** https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of `k` linked-lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

```typescript
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    // Your code here
}
```

**Examples:**
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Input: lists = []
Output: []

Input: lists = [[]]
Output: []
```

---

## Problem 5: Task Scheduler
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/task-scheduler/

Given a characters array `tasks`, representing tasks that need to be done, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

There is a non-negative integer `n` that represents the cooldown period between two same tasks (the same letter in the array).

Return the least number of units of time that the CPU will need to finish all the given tasks.

```typescript
function leastInterval(tasks: string[], n: number): number {
    // Your code here
}
```

**Examples:**
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: All tasks can be done without idle time.
```

---

## Problem 6: Kth Smallest Element in a Sorted Matrix
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Given an `n x n` matrix where each of the rows and columns is sorted in ascending order, return the `kth` smallest element in the matrix.

Note that it is the `kth` smallest element in sorted order, not the `kth` distinct element.

```typescript
function kthSmallest(matrix: number[][], k: number): number {
    // Your code here
}
```

**Examples:**
```
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: Elements in sorted order: [1,5,9,10,11,12,13,13,15]

Input: matrix = [[-5]], k = 1
Output: -5
```

---

## Problem 7: K Closest Points to Origin
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/k-closest-points-to-origin/

Given an array of points where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)² + (y1 - y2)²).

You may return the answer in any order.

```typescript
function kClosest(points: number[][], k: number): number[][] {
    // Your code here
}
```

**Examples:**
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation: Distance of [1,3] is sqrt(10). Distance of [-2,2] is sqrt(8).

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
```

---

## Problem 8: Reorganize String
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/reorganize-string/

Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same.

Return any possible rearrangement of `s` or return `""` if not possible.

```typescript
function reorganizeString(s: string): string {
    // Your code here
}
```

**Examples:**
```
Input: s = "aab"
Output: "aba"

Input: s = "aaab"
Output: ""
```

---

## Problem 9: Ugly Number II
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/ugly-number-ii/

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer `n`, return the `nth` ugly number.

```typescript
function nthUglyNumber(n: number): number {
    // Your code here
}
```

**Examples:**
```
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] are the first 10 ugly numbers.

Input: n = 1
Output: 1
Explanation: 1 is typically treated as an ugly number.
```

---

## Problem 10: Find K Pairs with Smallest Sums
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

You are given two integer arrays `nums1` and `nums2` sorted in ascending order and an integer `k`.

Define a pair `(u, v)` which consists of one element from the first array and one element from the second array.

Return the `k` pairs `(u1, v1), (u2, v2), ..., (uk, vk)` with the smallest sums.

```typescript
function kSmallestPairs(nums1: number[], nums2: number[], k: number): number[][] {
    // Your code here
}
```

**Examples:**
```
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are: [1,2], [1,4], [1,6]

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
```

---

## Approach Tips

### General Strategy:
1. **Identify the pattern** - K elements? Streaming? Priority-based?
2. **Choose heap type** - Min-heap for smallest K, max-heap for largest K
3. **Consider custom comparator** - For complex objects or custom ordering
4. **Think about heap size** - Fixed size K or variable?
5. **Handle edge cases** - Empty input, k > array length, duplicates

### Common Techniques:
- **Min heap of size K** for K-th largest
- **Max heap of size K** for K-th smallest
- **Two heaps** for median tracking
- **Priority queue** for merge operations
- **Frequency counting** before heap operations

---

## Complexity Requirements

Most heap problems expect:
- **Time:** O(n log k) or O(n log n)
- **Space:** O(k) or O(n)

Where sorting would be O(n log n) time, heaps often achieve O(n log k) when k << n.

---

## Problem Solving Strategy

### Before You Start:
1. **Understand the problem** - Read it twice if needed
2. **Identify the pattern** - Is it a K-element problem? Streaming? Priority-based?
3. **Choose your approach** - Heap type, size constraints, custom comparator
4. **Consider edge cases** - Empty input, k > n, duplicates
5. **Plan your solution** - Pseudocode first, then implement

### During Implementation:
1. **Start simple** - Get a working solution first
2. **Test as you go** - Use the examples provided
3. **Optimize later** - Working code before optimal code
4. **Debug systematically** - Print heap state if needed
5. **Time yourself** - Aim for 20-25 minutes per medium problem

### After Solving:
1. **Verify complexity** - Does it match expectations?
2. **Check edge cases** - Test with extreme inputs
3. **Compare approaches** - Is there a better way?
4. **Review solutions** - Learn from optimal approaches
5. **Note patterns** - What can you apply to similar problems?

---

## Interview Tips

### Communication:
- **Think aloud** - Share your thought process
- **Ask questions** - Clarify requirements
- **Explain trade-offs** - Space vs time, simplicity vs optimization
- **Draw diagrams** - Visualize heap structure
- **Test thoroughly** - Walk through examples

### Common Questions to Ask:
1. "Can I modify the input array?"
2. "How should I handle duplicates?"
3. "What if k is larger than the array size?"
4. "Should I optimize for time or space?"
5. "Can I use built-in heap libraries?"

### Red Flags to Avoid:
- Don't jump to code immediately
- Don't ignore edge cases
- Don't forget to analyze complexity
- Don't use brute force without mentioning better approaches
- Don't give up if the optimal solution isn't obvious

---

## Additional Practice Resources

### Similar Problems on LeetCode:
1. **Last Stone Weight** (Easy) - LC 1046
2. **Kth Largest Element in a Stream** (Easy) - LC 703
3. **Sort Characters By Frequency** (Medium) - LC 451
4. **IPO** (Hard) - LC 502
5. **Sliding Window Median** (Hard) - LC 480

### Heap Variations:
1. **Indexed Priority Queue** - For updating priorities
2. **Binomial Heap** - For merge operations
3. **Fibonacci Heap** - For decrease-key operations
4. **D-ary Heap** - For cache optimization
5. **Leftist Heap** - For functional programming

### Real-World Applications:
1. **Task Scheduling** - CPU scheduling, job queues
2. **Event Simulation** - Discrete event simulation
3. **Path Finding** - Dijkstra's algorithm, A* search
4. **Data Compression** - Huffman coding
5. **Load Balancing** - Server request handling

---

## Quick Reference

### Heap Operations Cheat Sheet:
```typescript
// Min Heap Operations
insert(val)     // O(log n) - Add element
extractMin()    // O(log n) - Remove minimum
peekMin()       // O(1)     - View minimum
heapify(arr)    // O(n)     - Build heap
size()          // O(1)     - Get size
isEmpty()       // O(1)     - Check empty

// Index Formulas (0-indexed)
parent(i) = Math.floor((i - 1) / 2)
leftChild(i) = 2 * i + 1
rightChild(i) = 2 * i + 2

// When to use Min vs Max Heap
K largest  → Min heap of size K
K smallest → Max heap of size K
Median     → Max heap (left) + Min heap (right)
```

### TypeScript Priority Queue Template:
```typescript
class PriorityQueue<T> {
    private heap: T[] = [];
    constructor(private compare: (a: T, b: T) => number) {}

    push(val: T): void { /* ... */ }
    pop(): T | undefined { /* ... */ }
    peek(): T | undefined { return this.heap[0]; }
    size(): number { return this.heap.length; }
    isEmpty(): boolean { return this.heap.length === 0; }
}
```

---

## Progress Tracking

### Session Goals:
- [ ] Complete video watching
- [ ] Pass concept check
- [ ] Solve 3 Easy/Medium problems
- [ ] Attempt 1 Hard problem
- [ ] Review all solutions

### Skill Checkpoints:
- [ ] Can implement heap from scratch
- [ ] Understand heap vs sorting trade-offs
- [ ] Recognize K-element patterns
- [ ] Handle streaming data problems
- [ ] Apply two-heap technique

### Time Benchmarks:
- Easy problems: 10-15 minutes
- Medium problems: 15-25 minutes
- Hard problems: 25-35 minutes
- Implementation from scratch: 10 minutes

---

## Final Thoughts

Heaps are powerful for priority-based operations and K-element problems. Master the patterns in these 10 problems, and you'll handle most heap questions confidently.

Remember: It's not about memorizing solutions, but understanding when and why to use heaps. The efficiency gains for K-element problems (O(n log k) vs O(n log n)) can be the difference between an optimal and suboptimal solution.

---

**Ready to solve?** Start with the hints in HINTS.md if needed!