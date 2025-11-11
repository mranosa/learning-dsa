# Hints: Binary Search

## Problem 1: Binary Search

### Hint Level 1 (Gentle nudge)
Think about how you would search for a word in a dictionary. You don't start from page 1 - you open it somewhere in the middle. What happens next?

### Hint Level 2 (More specific)
Use two pointers: `left` and `right`. Calculate the middle index and compare `nums[mid]` with target. Based on the comparison, which half of the array can you eliminate?

### Hint Level 3 (Detailed approach)
```typescript
// Initialize: left = 0, right = nums.length - 1
// While left <= right:
//   1. Calculate mid = left + Math.floor((right - left) / 2)
//   2. If nums[mid] === target, return mid
//   3. If nums[mid] < target, search right half (left = mid + 1)
//   4. Otherwise, search left half (right = mid - 1)
// If loop ends without finding, return -1
```

---

## Problem 2: Search in Rotated Sorted Array

### Hint Level 1 (Gentle nudge)
Even though the array is rotated, at least one half is always sorted. How can you determine which half is sorted?

### Hint Level 2 (More specific)
Compare `nums[left]` with `nums[mid]`. If `nums[left] <= nums[mid]`, the left half is sorted. Now check if the target lies in the sorted range using boundary values.

### Hint Level 3 (Detailed approach)
```typescript
// At each step:
// 1. Check if nums[mid] === target
// 2. Determine which half is sorted:
//    - If nums[left] <= nums[mid]: left half is sorted
//    - Otherwise: right half is sorted
// 3. Check if target is in the sorted half using range check
// 4. Move to the appropriate half
```

---

## Problem 3: Find Minimum in Rotated Sorted Array

### Hint Level 1 (Gentle nudge)
The minimum element is at the "inflection point" where the rotation happened. How does the middle element compare to the rightmost element?

### Hint Level 2 (More specific)
If `nums[mid] > nums[right]`, the rotation point (and minimum) must be in the right half. Why? Because in a sorted array, mid should be less than right.

### Hint Level 3 (Detailed approach)
```typescript
// Use left < right (not left <= right)
// Compare nums[mid] with nums[right]:
//   - If nums[mid] > nums[right]: minimum is in right half (left = mid + 1)
//   - Otherwise: minimum is in left half including mid (right = mid)
// When left === right, nums[left] is the minimum
```

---

## Problem 4: Search a 2D Matrix

### Hint Level 1 (Gentle nudge)
If you "flatten" the 2D matrix into a 1D array, it would be completely sorted. How can you map a 1D index to 2D coordinates?

### Hint Level 2 (More specific)
For a matrix with m rows and n columns, index i in the flattened array corresponds to:
- Row: `Math.floor(i / n)`
- Column: `i % n`

### Hint Level 3 (Detailed approach)
```typescript
// Total elements = m * n
// Binary search from index 0 to (m * n - 1)
// For each mid index:
//   - row = Math.floor(mid / n)
//   - col = mid % n
//   - value = matrix[row][col]
// Then proceed with standard binary search comparison
```

---

## Problem 5: Koko Eating Bananas

### Hint Level 1 (Gentle nudge)
You're not searching in an array - you're searching for the optimal eating speed. What's the minimum and maximum possible eating speed?

### Hint Level 2 (More specific)
Minimum speed = 1 (eat at least 1 banana per hour). Maximum speed = max(piles) (no point eating faster than the largest pile). Binary search this range and check if each speed allows finishing within h hours.

### Hint Level 3 (Detailed approach)
```typescript
// Binary search on speed from 1 to max(piles)
// For each speed, calculate total hours needed:
//   - For each pile: hours += Math.ceil(pile / speed)
// If total hours <= h, this speed works (try slower)
// If total hours > h, need faster speed
// Keep track of minimum valid speed
```

---

## Problem 6: Find Peak Element

### Hint Level 1 (Gentle nudge)
If you're standing on a slope, which direction would you go to find a peak? Think about what `nums[mid] < nums[mid + 1]` tells you.

### Hint Level 2 (More specific)
If `nums[mid] < nums[mid + 1]`, you're on an ascending slope, so there must be a peak to the right. Otherwise, there's a peak to the left (or you're at a peak).

### Hint Level 3 (Detailed approach)
```typescript
// Use left < right (not left <= right)
// Compare nums[mid] with nums[mid + 1]:
//   - If nums[mid] > nums[mid + 1]: peak is in left half including mid (right = mid)
//   - Otherwise: peak is in right half excluding mid (left = mid + 1)
// When left === right, you've found a peak
```

---

## Problem 7: Search Insert Position

### Hint Level 1 (Gentle nudge)
This is almost identical to standard binary search. What should you return when the target is not found?

### Hint Level 2 (More specific)
When the standard binary search ends without finding the target, the `left` pointer indicates where the target should be inserted to maintain sorted order.

### Hint Level 3 (Detailed approach)
```typescript
// Run standard binary search
// If target is found, return its index
// If not found (left > right), return left
// Why left? Because at termination:
//   - All elements before left are < target
//   - All elements from left onwards are > target
```

---

## Problem 8: First Bad Version

### Hint Level 1 (Gentle nudge)
You're looking for the first position where `isBadVersion` returns true. Think of it as finding the leftmost "true" in an array of [false, false, true, true, true].

### Hint Level 2 (More specific)
When you find a bad version, you need to keep searching left to find the FIRST bad version. When you find a good version, the first bad must be to the right.

### Hint Level 3 (Detailed approach)
```typescript
// Use left < right (not left <= right)
// If isBadVersion(mid) is true:
//   - First bad is at mid or before (right = mid)
// If isBadVersion(mid) is false:
//   - First bad is after mid (left = mid + 1)
// When left === right, that's the first bad version
```

---

## Problem 9: Time Based Key-Value Store

### Hint Level 1 (Gentle nudge)
Store values with timestamps in a sorted array for each key. When getting a value, you need to find the largest timestamp that is <= the requested timestamp.

### Hint Level 2 (More specific)
Use a Map where each key maps to an array of [timestamp, value] pairs. Since timestamps are strictly increasing, the array is already sorted. Binary search to find the rightmost valid timestamp.

### Hint Level 3 (Detailed approach)
```typescript
// In set(): Add [timestamp, value] to the array for the key
// In get():
//   1. Get the array for the key
//   2. Binary search for largest timestamp <= requested timestamp
//   3. Keep track of the result whenever you find a valid timestamp
//   4. Update left = mid + 1 to look for larger valid timestamps
```

---

## Problem 10: Median of Two Sorted Arrays

### Hint Level 1 (Gentle nudge)
The median splits the combined arrays into two equal halves. Can you partition both arrays such that all elements in the left partition are <= all elements in the right partition?

### Hint Level 2 (More specific)
Binary search on the smaller array to find the correct partition. For partition position i in nums1 and j in nums2, ensure:
- `i + j = (m + n + 1) / 2`
- `max(left partition) <= min(right partition)`

### Hint Level 3 (Detailed approach)
```typescript
// Binary search on smaller array (for efficiency)
// For each partition position in smaller array:
//   1. Calculate corresponding partition in larger array
//   2. Get max of left partition and min of right partition
//   3. Check if valid partition (maxLeft <= minRight)
//   4. If valid, calculate median based on total length (odd/even)
//   5. If not valid, adjust partition position
// Handle edge cases: partition at 0 or at array end
```

---

## General Binary Search Tips

### Template Selection Guide
- **Exact match?** Use `while (left <= right)`
- **Finding boundary?** Use `while (left < right)`
- **Maximizing/Minimizing?** Keep track of best answer so far

### Common Mistakes to Avoid
1. **Infinite loops:** Make sure pointers always move
2. **Off-by-one:** Be consistent with inclusive/exclusive bounds
3. **Overflow:** Use `left + (right - left) / 2`
4. **Edge cases:** Test empty array, single element, target at boundaries

### Debugging Strategy
1. Print left, right, mid values
2. Verify your comparison logic
3. Check termination condition
4. Test with arrays of size 0, 1, 2, 3
5. Trace through with target at start, middle, end, and not present