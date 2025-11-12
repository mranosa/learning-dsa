# Problems - Session 17: Heaps & Priority Queues

10 problems in order. Use UMPIRE method.

**Targets:** Medium <25 min | Hard <35 min

---

## Problem 1: Kth Largest Element in an Array

**Difficulty:** Medium | **Pattern:** K-Element (Min Heap)
**LeetCode:** https://leetcode.com/problems/kth-largest-element-in-an-array/

### Problem

Given integer array `nums` and integer `k`, return the `kth` largest element.

Note: kth largest in sorted order, not kth distinct.

### Examples

```
nums = [3,2,1,5,6,4], k = 2
Output: 5

nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

### Constraints

- 1 ≤ k ≤ nums.length ≤ 10⁵
- -10⁴ ≤ nums[i] ≤ 10⁴

### Hints
- Use min heap of size K
- Why min heap for K largest? Think about what gets removed
- O(n log k) beats O(n log n) sorting when k << n

---

## Problem 2: Top K Frequent Elements

**Difficulty:** Medium | **Pattern:** K-Element with Frequency
**LeetCode:** https://leetcode.com/problems/top-k-frequent-elements/

### Problem

Given integer array `nums` and integer `k`, return the `k` most frequent elements.

Return in any order.

### Examples

```
nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

nums = [1], k = 1
Output: [1]
```

### Constraints

- 1 ≤ nums.length ≤ 10⁵
- -10⁴ ≤ nums[i] ≤ 10⁴
- k is in range [1, number of unique elements]
- Answer is unique

### Hints
- Two steps: count frequencies, then find top K
- Min heap of size K comparing by frequency
- Alternative: bucket sort (frequencies bounded by n)

---

## Problem 3: Find Median from Data Stream

**Difficulty:** Hard | **Pattern:** Two Heaps
**LeetCode:** https://leetcode.com/problems/find-median-from-data-stream/

### Problem

Median is middle value in ordered list. If even size, median is mean of two middle values.

Implement MedianFinder:
- `MedianFinder()` - initializes object
- `void addNum(int num)` - adds integer from data stream
- `double findMedian()` - returns median of all elements

### Examples

```
MedianFinder mf = new MedianFinder();
mf.addNum(1);    // arr = [1]
mf.addNum(2);    // arr = [1, 2]
mf.findMedian(); // return 1.5
mf.addNum(3);    // arr = [1, 2, 3]
mf.findMedian(); // return 2.0
```

### Constraints

- -10⁵ ≤ num ≤ 10⁵
- At least one element before calling findMedian
- At most 5×10⁴ calls to addNum and findMedian

### Hints
- Two heaps: max heap for smaller half, min heap for larger half
- Keep sizes balanced (differ by at most 1)
- Maintain: max heap top ≤ min heap top
- Median from top(s)

---

## Problem 4: Merge K Sorted Lists

**Difficulty:** Hard | **Pattern:** Merge with Heap
**LeetCode:** https://leetcode.com/problems/merge-k-sorted-lists/

### Problem

Given array of `k` linked-lists, each sorted ascending. Merge all into one sorted list.

### Examples

```
lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

lists = []
Output: []

lists = [[]]
Output: []
```

### Constraints

- k == lists.length
- 0 ≤ k ≤ 10⁴
- 0 ≤ lists[i].length ≤ 500
- -10⁴ ≤ Node.val ≤ 10⁴
- Lists sorted ascending
- Sum of all lengths ≤ 10⁴

### Hints
- Min heap with one node from each list
- Extract min, add to result, push next node from same list
- Heap size never exceeds K
- O(n log k) where n = total nodes

---

## Problem 5: Task Scheduler

**Difficulty:** Medium | **Pattern:** Greedy with Heap
**LeetCode:** https://leetcode.com/problems/task-scheduler/

### Problem

Given array `tasks` (letters represent different tasks) and integer `n` (cooldown period).

Each task takes 1 unit. CPU can do one task or be idle. Same task must wait n intervals.

Return minimum units of time to finish all tasks.

### Examples

```
tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B

tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
```

### Constraints

- 1 ≤ tasks.length ≤ 10⁴
- tasks[i] is uppercase letter
- 0 ≤ n ≤ 100

### Hints
- Count task frequencies
- Max heap to always pick highest frequency available task
- Queue to track cooling tasks with available time
- Simulate time progression

---

## Problem 6: Kth Smallest Element in a Sorted Matrix

**Difficulty:** Medium | **Pattern:** K-Element in Matrix
**LeetCode:** https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

### Problem

Given `n x n` matrix where each row and column is sorted ascending. Return `kth` smallest element.

Note: kth smallest in sorted order, not kth distinct.

### Examples

```
matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13

matrix = [[-5]], k = 1
Output: -5
```

### Constraints

- n == matrix.length == matrix[i].length
- 1 ≤ n ≤ 300
- -10⁹ ≤ matrix[i][j] ≤ 10⁹
- Matrix sorted row-wise and column-wise
- 1 ≤ k ≤ n²

### Hints
- Min heap starting with [0,0]
- Extract min K times
- When extract [i,j], add [i+1,j] and [i,j+1] if not visited
- Track visited with Set

---

## Problem 7: K Closest Points to Origin

**Difficulty:** Medium | **Pattern:** K-Element with Distance
**LeetCode:** https://leetcode.com/problems/k-closest-points-to-origin/

### Problem

Given array `points` where `points[i] = [xi, yi]` and integer `k`, return `k` closest points to origin (0, 0).

Distance is Euclidean: √(x² + y²). Return in any order.

### Examples

```
points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]

points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
```

### Constraints

- 1 ≤ k ≤ points.length ≤ 10⁴
- -10⁴ ≤ xi, yi ≤ 10⁴

### Hints
- Use squared distance (x² + y²) - no need for sqrt
- Max heap of size K
- Remove farthest when size > K
- O(n log k)

---

## Problem 8: Reorganize String

**Difficulty:** Medium | **Pattern:** Greedy with Heap
**LeetCode:** https://leetcode.com/problems/reorganize-string/

### Problem

Given string `s`, rearrange characters so no two adjacent are the same.

Return any valid rearrangement, or `""` if impossible.

### Examples

```
s = "aab"
Output: "aba"

s = "aaab"
Output: ""
```

### Constraints

- 1 ≤ s.length ≤ 500
- s consists of lowercase letters

### Hints
- If any char frequency > (n+1)/2, impossible
- Max heap by frequency
- Take two most frequent each iteration
- Alternate placement

---

## Problem 9: Ugly Number II

**Difficulty:** Medium | **Pattern:** Generation with Heap
**LeetCode:** https://leetcode.com/problems/ugly-number-ii/

### Problem

Ugly number is positive integer whose prime factors are only 2, 3, and 5.

Given integer `n`, return `nth` ugly number.

### Examples

```
n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]

n = 1
Output: 1
```

### Constraints

- 1 ≤ n ≤ 1690

### Hints
- Each ugly number = previous ugly × 2, 3, or 5
- Min heap to generate in order
- Start with 1, multiply by 2,3,5 and add to heap
- Use Set to avoid duplicates
- Alternative: DP with three pointers

---

## Problem 10: Find K Pairs with Smallest Sums

**Difficulty:** Medium | **Pattern:** K-Element from Two Arrays
**LeetCode:** https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

### Problem

Given two integer arrays `nums1` and `nums2` sorted ascending, and integer `k`.

Define pair `(u, v)` with one element from each array.

Return `k` pairs with smallest sums.

### Examples

```
nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]

nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
```

### Constraints

- 1 ≤ nums1.length, nums2.length ≤ 10⁵
- -10⁹ ≤ nums1[i], nums2[i] ≤ 10⁹
- nums1 and nums2 sorted ascending
- 1 ≤ k ≤ 10⁴

### Hints
- Start with pair [0,0] in min heap
- Heap stores [sum, i, j]
- When extract [i,j], add [i+1,j] and [i,j+1]
- Track visited pairs

---

## Summary

**Total:** 10 problems (7 Medium, 3 Hard)

**Patterns:**
- K-Element (min/max heap of size K)
- Two Heaps (median)
- Merge with Heap
- Greedy with Priority
- Generation with Heap

**Key Operations:**
- Insert: O(log n)
- Extract: O(log n)
- Maintain size K: O(n log k)

---

**Ready?** Say: `"Claude, give me the problem"` or `"Go"`

[Solutions](./SOLUTIONS.md) | [Hints](./HINTS.md)
