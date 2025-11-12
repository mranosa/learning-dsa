# Hints - Session 6: Binary Search

Progressive hints for 10 problems. Struggling is part of learning.

---

## Problem 1: Binary Search

### Level 1
How do you find a word in a dictionary? You don't start at page 1. What data structure splits search space in half?

### Level 2
Two pointers: `left = 0`, `right = n-1`. Calculate mid. Compare `nums[mid]` with target. Which half can you eliminate?

### Level 3
```typescript
let left = 0, right = nums.length - 1;
while (left <= right) {
  const mid = left + Math.floor((right - left) / 2);
  if (nums[mid] === target) return mid;
  if (nums[mid] < target) left = mid + 1;
  else right = mid - 1;
}
return -1;
```

---

## Problem 2: Search Insert Position

### Level 1
Almost identical to standard binary search. What does `left` pointer represent when target not found?

### Level 2
After binary search terminates without finding target, `left` indicates insertion position. Why? All elements before `left` are < target.

### Level 3
```typescript
// Run standard binary search
// If found, return index
// If not found, return left
// At termination: elements [0...left) < target, elements [left...n) >= target
```

---

## Problem 3: First Bad Version

### Level 1
Finding first position where `isBadVersion` returns true. Think: array `[false, false, true, true]` - find leftmost true.

### Level 2
Use `left < right` template. When `isBadVersion(mid)` true, first bad at mid or before → `right = mid`. When false, first bad after → `left = mid + 1`.

### Level 3
```typescript
let left = 1, right = n;
while (left < right) {
  const mid = left + Math.floor((right - left) / 2);
  if (isBadVersion(mid)) right = mid;  // Search left including mid
  else left = mid + 1;  // Search right
}
return left;
```

---

## Problem 4: Find Minimum in Rotated Sorted Array

### Level 1
Minimum is at "inflection point" where rotation happened. Compare mid with right - what does that tell you?

### Level 2
If `nums[mid] > nums[right]`, rotation point (minimum) in right half. In normal sorted array, mid should be < right. Violation means rotation.

### Level 3
```typescript
let left = 0, right = nums.length - 1;
while (left < right) {
  const mid = Math.floor((left + right) / 2);
  if (nums[mid] > nums[right]) left = mid + 1;  // Min in right
  else right = mid;  // Min in left or at mid
}
return nums[left];
```

---

## Problem 5: Search in Rotated Sorted Array

### Level 1
At least one half always sorted. How to determine which half? Then check if target in sorted half.

### Level 2
Compare `nums[left]` with `nums[mid]`. If `nums[left] <= nums[mid]`, left half sorted. Check if target in sorted range using boundaries.

### Level 3
```typescript
// Determine sorted half:
if (nums[left] <= nums[mid]) {
  // Left sorted: check if target in [left, mid)
  if (nums[left] <= target && target < nums[mid]) right = mid - 1;
  else left = mid + 1;
} else {
  // Right sorted: check if target in (mid, right]
  if (nums[mid] < target && target <= nums[right]) left = mid + 1;
  else right = mid - 1;
}
```

---

## Problem 6: Search a 2D Matrix

### Level 1
Flatten 2D matrix to 1D - it's fully sorted. How to map 1D index to 2D coordinates?

### Level 2
For matrix with m rows, n cols: index i → row = `Math.floor(i / n)`, col = `i % n`.

### Level 3
```typescript
const m = matrix.length, n = matrix[0].length;
let left = 0, right = m * n - 1;
while (left <= right) {
  const mid = Math.floor((left + right) / 2);
  const row = Math.floor(mid / n);
  const col = mid % n;
  const value = matrix[row][col];
  // Standard binary search comparison
}
```

---

## Problem 7: Koko Eating Bananas

### Level 1
Not searching in array - searching for optimal speed. What's min and max possible speed?

### Level 2
Min speed = 1, max speed = `max(piles)`. Binary search this range. For each speed, check if can finish in h hours.

### Level 3
```typescript
// Binary search speed from 1 to max(piles)
// For each speed:
function canFinish(speed) {
  let hours = 0;
  for (pile of piles) hours += Math.ceil(pile / speed);
  return hours <= h;
}
// If canFinish(mid), try slower (right = mid)
// Else need faster (left = mid + 1)
```

---

## Problem 8: Find Peak Element

### Level 1
If on slope, which direction to find peak? What does `nums[mid] < nums[mid+1]` tell you?

### Level 2
If `nums[mid] < nums[mid+1]`, ascending slope → peak must be right. Otherwise descending → peak at mid or left.

### Level 3
```typescript
let left = 0, right = nums.length - 1;
while (left < right) {
  const mid = Math.floor((left + right) / 2);
  if (nums[mid] > nums[mid + 1]) right = mid;  // Descending
  else left = mid + 1;  // Ascending
}
return left;
```

---

## Problem 9: Time Based Key-Value Store

### Level 1
Store values with timestamps in sorted array per key. When getting, find largest timestamp ≤ requested.

### Level 2
Use `Map<string, Array<[timestamp, value]>>`. Timestamps strictly increasing → already sorted. Binary search for rightmost valid timestamp.

### Level 3
```typescript
// In get():
const values = store.get(key);
let left = 0, right = values.length - 1, result = "";
while (left <= right) {
  const mid = Math.floor((left + right) / 2);
  if (values[mid][0] <= timestamp) {
    result = values[mid][1];
    left = mid + 1;  // Look for larger valid timestamp
  } else right = mid - 1;
}
return result;
```

---

## Problem 10: Median of Two Sorted Arrays

### Level 1
Median splits combined arrays into equal halves. Can you partition both arrays so all left elements ≤ all right elements?

### Level 2
Binary search on smaller array. For partition i in nums1, calculate j in nums2 where `i + j = (m+n+1)/2`. Ensure `max(left) <= min(right)`.

### Level 3
```typescript
// Binary search on smaller array for partition
// For each partition position:
const partitionX = mid;
const partitionY = Math.floor((m + n + 1) / 2) - partitionX;
const maxLeftX = partitionX === 0 ? -Infinity : nums1[partitionX - 1];
const minRightX = partitionX === m ? Infinity : nums1[partitionX];
// Similar for Y
// Check if maxLeftX <= minRightY && maxLeftY <= minRightX
// Calculate median from partition boundaries
```

---

## Pattern Hints

**"Sorted array" + O(log n)** → Binary search (classic or modified)

**"Find minimum k such that..."** → Binary search on answer space

**"Rotated sorted array"** → Modified binary search, at least one half sorted

**"First/last occurrence"** → Binary search with `left < right` template

**"2D matrix with sorted properties"** → Flatten to 1D or binary search rows then columns

**"Peak/valley"** → Binary search on local property (slope)

---

## Using Hints Effectively

1. Try 10+ min before Level 1
2. Try 5+ min after each hint
3. If use Level 3, mark for review and retry later
4. Don't feel bad - hints are for learning

Goal: Learn pattern, not just solve one problem.

---

## Common Mistakes

**Infinite loops:** Ensure pointers always move
- ❌ `left = mid` when `mid === left`
- ✅ `left = mid + 1`

**Off-by-one:** Be consistent with inclusive/exclusive bounds
- Template 1: `[left, right]` with `left <= right`
- Template 2: `[left, right)` with `left < right`

**Overflow:** Use `left + (right - left) / 2`

**Edge cases:** Test empty, single element, target at boundaries

---

[Back to Problems](./PROBLEMS.md) | [Back to Solutions](./SOLUTIONS.md)
