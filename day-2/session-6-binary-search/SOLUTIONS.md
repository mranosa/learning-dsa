# Solutions - Session 6: Binary Search

TypeScript solutions with complexity analysis.

---

## Problem 1: Binary Search

### Approach: Iterative Binary Search (Optimal) ✅

```typescript
function search(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);

    if (nums[mid] === target) {
      return mid;
    } else if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1;
}
```

**Time:** O(log n) | **Space:** O(1)

**Key:** Standard binary search template. Use `left + (right - left) / 2` to prevent overflow.

**Say:** "Classic binary search with O(log n) time by eliminating half the search space each iteration. Iterative approach uses O(1) space."

---

## Problem 2: Search Insert Position

### Approach: Binary Search (Optimal) ✅

```typescript
function searchInsert(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);

    if (nums[mid] === target) {
      return mid;
    } else if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return left;
}
```

**Time:** O(log n) | **Space:** O(1)

**Key:** Standard binary search. When target not found, `left` is the insertion position. After loop terminates, all elements before `left` are < target.

**Say:** "Using binary search to find position. When not found, left pointer indicates insertion index to maintain sorted order."

---

## Problem 3: First Bad Version

### Approach: Binary Search for First True (Optimal) ✅

```typescript
var solution = function(isBadVersion: (version: number) => boolean) {
  return function(n: number): number {
    let left = 1;
    let right = n;

    while (left < right) {
      const mid = left + Math.floor((right - left) / 2);

      if (isBadVersion(mid)) {
        right = mid; // First bad at mid or before
      } else {
        left = mid + 1; // First bad after mid
      }
    }

    return left;
  };
};
```

**Time:** O(log n) | **Space:** O(1)

**Key:** Find first position where condition becomes true. Use `left < right` (not `<=`). When isBadVersion(mid) true, search left including mid.

**Say:** "Finding boundary where false becomes true. Template for finding first occurrence in sorted boolean array."

---

## Problem 4: Find Minimum in Rotated Sorted Array

### Approach: Modified Binary Search (Optimal) ✅

```typescript
function findMin(nums: number[]): number {
  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    if (nums[mid] > nums[right]) {
      // Minimum in right half
      left = mid + 1;
    } else {
      // Minimum in left half (including mid)
      right = mid;
    }
  }

  return nums[left];
}
```

**Time:** O(log n) | **Space:** O(1)

**Key:** Compare mid with right. If `nums[mid] > nums[right]`, array is rotated and minimum is in right half (inflection point). Otherwise minimum is left including mid.

**Say:** "Comparing mid with right endpoint. In sorted array, mid should be less than right. If greater, rotation happened and minimum is right."

---

## Problem 5: Search in Rotated Sorted Array

### Approach: Modified Binary Search (Optimal) ✅

```typescript
function search(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (nums[mid] === target) return mid;

    // Determine which half is sorted
    if (nums[left] <= nums[mid]) {
      // Left half sorted
      if (nums[left] <= target && target < nums[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    } else {
      // Right half sorted
      if (nums[mid] < target && target <= nums[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }

  return -1;
}
```

**Time:** O(log n) | **Space:** O(1)

**Key:** At least one half always sorted. Determine which half, check if target in that half using boundary values. If yes, search it; else search other half.

**Say:** "Identifying sorted half then checking if target lies within that range. Always have at least one monotonic half to work with."

---

## Problem 6: Search a 2D Matrix

### Approach: Treat as 1D Array (Optimal) ✅

```typescript
function searchMatrix(matrix: number[][], target: number): boolean {
  if (!matrix.length || !matrix[0].length) return false;

  const m = matrix.length;
  const n = matrix[0].length;
  let left = 0;
  let right = m * n - 1;

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);
    const row = Math.floor(mid / n);
    const col = mid % n;
    const value = matrix[row][col];

    if (value === target) return true;
    if (value < target) left = mid + 1;
    else right = mid - 1;
  }

  return false;
}
```

**Time:** O(log(m × n)) | **Space:** O(1)

**Key:** Treat 2D matrix as flattened 1D sorted array. Convert 1D index to 2D: `row = idx / cols`, `col = idx % cols`.

**Say:** "Treating matrix as single sorted array. Converting between 1D and 2D indices allows standard binary search with O(log mn) time."

---

## Problem 7: Koko Eating Bananas

### Approach: Binary Search on Answer Space (Optimal) ✅

```typescript
function minEatingSpeed(piles: number[], h: number): number {
  let left = 1;
  let right = Math.max(...piles);

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    if (canFinish(piles, mid, h)) {
      right = mid; // Try smaller speed
    } else {
      left = mid + 1; // Need faster
    }
  }

  return left;
}

function canFinish(piles: number[], speed: number, h: number): boolean {
  let hours = 0;
  for (const pile of piles) {
    hours += Math.ceil(pile / speed);
    if (hours > h) return false; // Early termination
  }
  return hours <= h;
}
```

**Time:** O(n log m) where m = max(piles) | **Space:** O(1)

**Key:** Binary search on answer (speed) not on array. Min speed = 1, max speed = max(piles). Check if speed k works, adjust range. Monotonic: if speed k works, any speed > k also works.

**Say:** "Binary searching the answer space from 1 to max pile size. For each candidate speed, checking if can finish in time. Monotonic property allows binary search."

---

## Problem 8: Find Peak Element

### Approach: Binary Search on Slope (Optimal) ✅

```typescript
function findPeakElement(nums: number[]): number {
  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    if (nums[mid] > nums[mid + 1]) {
      // Descending, peak at mid or left
      right = mid;
    } else {
      // Ascending, peak to right
      left = mid + 1;
    }
  }

  return left;
}
```

**Time:** O(log n) | **Space:** O(1)

**Key:** If `nums[mid] < nums[mid+1]`, ascending slope → peak must be right. Otherwise descending → peak at mid or left. Always move toward higher values.

**Say:** "Following the slope upward. If ascending, peak ahead. If descending, peak behind or here. Eliminates half search space each iteration."

---

## Problem 9: Time Based Key-Value Store

### Approach: HashMap + Binary Search (Optimal) ✅

```typescript
class TimeMap {
  private store: Map<string, Array<[number, string]>>;

  constructor() {
    this.store = new Map();
  }

  set(key: string, value: string, timestamp: number): void {
    if (!this.store.has(key)) {
      this.store.set(key, []);
    }
    this.store.get(key)!.push([timestamp, value]);
  }

  get(key: string, timestamp: number): string {
    if (!this.store.has(key)) return "";

    const values = this.store.get(key)!;
    let left = 0;
    let right = values.length - 1;
    let result = "";

    while (left <= right) {
      const mid = left + Math.floor((right - left) / 2);

      if (values[mid][0] <= timestamp) {
        result = values[mid][1];
        left = mid + 1; // Look for larger valid timestamp
      } else {
        right = mid - 1;
      }
    }

    return result;
  }
}
```

**Time:** set O(1), get O(log n) | **Space:** O(n)

**Key:** Store [timestamp, value] pairs per key. Timestamps strictly increasing → sorted. Binary search for largest timestamp ≤ requested.

**Say:** "Using map with sorted timestamp arrays. Binary search finds largest valid timestamp. Timestamps are strictly increasing so array naturally sorted."

---

## Problem 10: Median of Two Sorted Arrays

### Approach: Binary Search on Smaller Array (Optimal) ✅

```typescript
function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
  // Ensure nums1 is smaller
  if (nums1.length > nums2.length) {
    return findMedianSortedArrays(nums2, nums1);
  }

  const m = nums1.length;
  const n = nums2.length;
  let left = 0;
  let right = m;

  while (left <= right) {
    const partitionX = Math.floor((left + right) / 2);
    const partitionY = Math.floor((m + n + 1) / 2) - partitionX;

    const maxLeftX = partitionX === 0 ? -Infinity : nums1[partitionX - 1];
    const minRightX = partitionX === m ? Infinity : nums1[partitionX];

    const maxLeftY = partitionY === 0 ? -Infinity : nums2[partitionY - 1];
    const minRightY = partitionY === n ? Infinity : nums2[partitionY];

    if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
      // Found correct partition
      if ((m + n) % 2 === 0) {
        return (Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2;
      } else {
        return Math.max(maxLeftX, maxLeftY);
      }
    } else if (maxLeftX > minRightY) {
      right = partitionX - 1;
    } else {
      left = partitionX + 1;
    }
  }

  throw new Error("Input arrays not sorted");
}
```

**Time:** O(log(min(m, n))) | **Space:** O(1)

**Key:** Binary search on smaller array to find partition. Partition both arrays so left halves have (m+n+1)/2 elements. Ensure max(left) ≤ min(right) for valid partition. Calculate median from partition boundaries.

**Say:** "Binary searching partition point in smaller array. Calculating corresponding partition in larger array. Valid when all left elements ≤ all right elements. Median derived from partition boundaries."

---

## Pattern Summary

### Classic Binary Search (Problems 1, 2, 6)
- Standard template: `while (left <= right)`
- Return `left` when not found for insertion
- Works on flattened 2D arrays

### Boundary Finding (Problems 3, 8)
- Use `while (left < right)`
- Finding first/last occurrence
- Peak finding with slope comparison

### Modified Binary Search (Problems 4, 5)
- At least one half always sorted
- Compare with endpoints to determine sorted half
- Handle rotation/pivot points

### Binary Search on Answer Space (Problems 7)
- Search answer range, not array
- Check if answer valid (helper function)
- Monotonic property required

### Advanced Applications (Problems 9, 10)
- Binary search in data structures
- Complex partitioning logic
- Multiple array coordination

---

[Back to Problems](./PROBLEMS.md) | [Back to README](./README.md)
