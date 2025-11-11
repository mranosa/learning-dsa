# Heap & Priority Queue Hints

## Problem 1: Kth Largest Element in an Array

### Hint 1 (Gentle)
Think about what data structure efficiently maintains the K largest elements seen so far.

### Hint 2 (Direct)
Use a min heap of size K. The root will always be the Kth largest element.

### Hint 3 (Detailed)
- Create a min heap
- Add elements one by one
- When heap size exceeds K, remove the smallest (root)
- After processing all elements, the root is your answer
- This is more efficient than sorting when K << n

---

## Problem 2: Top K Frequent Elements

### Hint 1 (Gentle)
This is a two-step problem: count frequencies, then find the top K.

### Hint 2 (Direct)
Count frequencies with a Map, then use a min heap of size K based on frequency.

### Hint 3 (Detailed)
- First pass: Build frequency map
- Second pass: Use min heap comparing by frequency
- Keep heap size at K by removing minimum frequency
- Alternative: Use bucket sort since frequencies are bounded by array length

---

## Problem 3: Find Median from Data Stream

### Hint 1 (Gentle)
How can you maintain the smaller and larger halves of your data separately?

### Hint 2 (Direct)
Use two heaps: a max heap for the smaller half and a min heap for the larger half.

### Hint 3 (Detailed)
- Max heap stores smaller half (top is largest of small)
- Min heap stores larger half (top is smallest of large)
- Keep sizes balanced (differ by at most 1)
- Median is either max heap top or average of both tops
- Maintain invariant: max heap top <= min heap top

---

## Problem 4: Merge K Sorted Lists

### Hint 1 (Gentle)
You need to track the smallest element across all K lists at any time.

### Hint 2 (Direct)
Use a min heap containing one node from each list. Always take the minimum.

### Hint 3 (Detailed)
- Initialize heap with first node from each list
- Extract minimum node, add to result
- If extracted node has a next, add it to heap
- Continue until heap is empty
- Heap size never exceeds K

---

## Problem 5: Task Scheduler

### Hint 1 (Gentle)
Tasks with higher frequency determine the minimum time needed.

### Hint 2 (Direct)
Use a max heap for frequencies and a queue for cooling tasks.

### Hint 3 (Detailed)
- Count task frequencies
- Use max heap to always pick highest frequency task
- After executing, decrease count and add to cooldown queue
- Queue stores [count, available_time]
- Process queue when tasks become available
- Time progresses whether CPU is idle or not

---

## Problem 6: Kth Smallest Element in a Sorted Matrix

### Hint 1 (Gentle)
The matrix is sorted row-wise and column-wise. How can you explore elements in order?

### Hint 2 (Direct)
Use a min heap starting with matrix[0][0], then explore right and down.

### Hint 3 (Detailed)
- Start with top-left element in heap
- Extract minimum K times
- When extracting element at [i,j]:
  - Add [i+1,j] if not visited
  - Add [i,j+1] if not visited
- Use a Set to track visited cells
- Kth extraction gives the answer

---

## Problem 7: K Closest Points to Origin

### Hint 1 (Gentle)
You don't need to calculate the actual distance - what's sufficient for comparison?

### Hint 2 (Direct)
Use squared distance (x² + y²) to avoid sqrt. Use a max heap of size K.

### Hint 3 (Detailed)
- Calculate squared distance for each point
- Use max heap comparing by distance
- Keep heap size at K
- Remove farthest point when size > K
- Final heap contains K closest points
- No need for sqrt since comparing relative distances

---

## Problem 8: Reorganize String

### Hint 1 (Gentle)
What's the maximum frequency a character can have for reorganization to be possible?

### Hint 2 (Direct)
Use a max heap by frequency. Always place the most frequent character, then the second most.

### Hint 3 (Detailed)
- Count character frequencies
- If any frequency > (length + 1) / 2, return ""
- Use max heap ordered by frequency
- Take two most frequent characters each iteration
- Place them alternately
- Decrease counts and re-add to heap if > 0
- Handle last character separately if odd length

---

## Problem 9: Ugly Number II

### Hint 1 (Gentle)
Each ugly number is formed by multiplying a previous ugly number by 2, 3, or 5.

### Hint 2 (Direct)
Use a min heap to generate ugly numbers in order, avoiding duplicates.

### Hint 3 (Detailed)
- Start with 1 in heap
- Extract minimum, it's the next ugly number
- Multiply by 2, 3, 5 and add to heap
- Use a Set to avoid duplicates
- Alternative: Use three pointers for 2x, 3x, 5x sequences
- Dynamic programming approach is more efficient

---

## Problem 10: Find K Pairs with Smallest Sums

### Hint 1 (Gentle)
Since arrays are sorted, which pairs should you consider first?

### Hint 2 (Direct)
Use a min heap starting with (nums1[0], nums2[0]), then explore next candidates.

### Hint 3 (Detailed)
- Start with pair (0, 0) in heap
- Heap stores [sum, i, j] where i and j are indices
- When extracting pair (i, j):
  - Add (i+1, j) if not visited
  - Add (i, j+1) if not visited
- Use Set to track visited pairs
- Extract K pairs from heap
- Early termination when K pairs found

---

## General Heap Problem-Solving Strategy

### Step 1: Identify the Pattern
- K elements? → Heap of size K
- Streaming data? → Dynamic heap operations
- Priority ordering? → Custom comparator
- Merge sorted? → Min heap of heads

### Step 2: Choose Heap Type
- K largest → Min heap of size K
- K smallest → Max heap of size K
- Median → Two heaps (max + min)
- Merge → Min heap

### Step 3: Implementation
- Custom heap or library?
- Handle edge cases
- Track additional state if needed
- Optimize heap size when possible

### Step 4: Complexity Analysis
- Insertion: O(log k) or O(log n)
- Extraction: O(log k) or O(log n)
- Building: O(n) with heapify
- Total: Usually O(n log k)

---

## Common Pitfalls to Avoid

1. **Wrong heap type** - Min vs Max confusion
2. **Heap size** - Not maintaining size K
3. **Comparator** - Wrong comparison function
4. **Duplicates** - Not handling properly
5. **Edge cases** - Empty input, K > n
6. **Index math** - Parent/child calculations
7. **Heap invariant** - Not maintaining after operations

---

## Debugging Tips

### Common Heap Bugs:

#### 1. Index Calculation Errors
```typescript
// WRONG - Common off-by-one error
parent(i) = i / 2  // Missing floor
leftChild(i) = 2 * i  // Wrong for 0-indexed

// CORRECT
parent(i) = Math.floor((i - 1) / 2)
leftChild(i) = 2 * i + 1
rightChild(i) = 2 * i + 2
```

#### 2. Heap Property Violation
```typescript
// Debug by printing heap after each operation
console.log("Heap state:", heap);
console.log("Is valid:", isValidHeap(heap));
```

#### 3. Wrong Heap Type
```typescript
// For K largest → Use MIN heap (counterintuitive!)
// For K smallest → Use MAX heap
// Remember: We keep K elements and remove the "worst"
```

#### 4. Forgetting to Maintain Size K
```typescript
// WRONG
heap.push(element);

// CORRECT
heap.push(element);
if (heap.size() > k) {
    heap.pop();
}
```

---

## Pattern Recognition Guide

### Pattern 1: Fixed K Elements
**Problems:** Kth Largest, Top K Frequent, K Closest Points
```typescript
// Template
for (const element of input) {
    heap.push(element);
    if (heap.size() > k) heap.pop();
}
return heap.getAllElements();
```

### Pattern 2: Dynamic Median
**Problems:** Find Median from Data Stream
```typescript
// Template
maxHeap; // smaller half
minHeap; // larger half
// Maintain: maxHeap.size() >= minHeap.size()
// Maintain: maxHeap.top() <= minHeap.top()
```

### Pattern 3: Merge Multiple Sources
**Problems:** Merge K Lists, K Pairs with Smallest Sums
```typescript
// Template
heap.push(initialElements);
while (!heap.isEmpty() && result.length < k) {
    current = heap.pop();
    result.push(current);
    heap.push(nextCandidates);
}
```

### Pattern 4: Greedy with Constraints
**Problems:** Task Scheduler, Reorganize String
```typescript
// Template
while (hasWork) {
    available = getAvailable();
    best = heap.pop();
    process(best);
    updateConstraints();
}
```

---

## Time Complexity Quick Guide

### Building Heap:
- **From insertions:** O(n log n)
- **From heapify:** O(n) - Preferred!

### K Operations:
- **Maintaining size K heap:** O(n log k)
- **Extracting K elements:** O(k log n)

### Trade-offs:
- **Sorting:** O(n log n) always
- **Heap:** O(n log k) when k << n
- **QuickSelect:** O(n) average, O(n²) worst

Choose based on:
- k << n? → Use heap
- Need all sorted? → Use sorting
- Only need kth? → Use QuickSelect

---

## Visualization Techniques

### Draw the Heap:
```
       10          [10, 7, 8, 5, 2, 6, 3]
      /  \
     7    8        Index: 0  1  2  3  4  5  6
    / \  / \
   5  2 6  3       Parent of i: (i-1)/2
                   Children: 2i+1, 2i+2
```

### Trace Operations:
```
Insert 4:
[10, 7, 8, 5, 2, 6, 3] → [10, 7, 8, 5, 2, 6, 3, 4]
Bubble up from index 7:
Parent(7) = 3, arr[3] = 5 > 4, no swap
Final: [10, 7, 8, 5, 2, 6, 3, 4]
```

---

## Interview Conversation Examples

### When Asked About Approach:
"I see this is a K-element problem. I'll use a min heap of size K to maintain the K largest elements. This gives us O(n log k) time instead of O(n log n) for sorting."

### When Explaining Trade-offs:
"We could sort in O(n log n), but since we only need K elements, a heap gives us O(n log k). If K is small relative to n, this is much better."

### When Debugging:
"Let me trace through with a small example. Starting with [3,2,1], k=2. I'll maintain a min heap of size 2..."

---

## Final Study Checklist

Before moving on, ensure you can:

### Implementation:
- [ ] Code a min heap from scratch in 5 minutes
- [ ] Code a max heap from scratch in 5 minutes
- [ ] Convert between min and max heap logic
- [ ] Implement with custom comparator

### Problem Solving:
- [ ] Identify when to use heap vs other structures
- [ ] Choose correct heap type (min vs max)
- [ ] Handle edge cases properly
- [ ] Optimize for K << n scenarios

### Conceptual:
- [ ] Explain heap properties clearly
- [ ] Derive time complexities
- [ ] Justify space complexities
- [ ] Compare with alternative approaches

---

**Still stuck?** Review the LESSON.md for heap operation implementations!