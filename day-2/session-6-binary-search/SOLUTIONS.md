# Solutions: Binary Search

## Problem 1: Binary Search

### Approach 1: Iterative Binary Search

```typescript
function search(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        // Prevent overflow
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

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

### Approach 2: Recursive Binary Search

```typescript
function search(nums: number[], target: number): number {
    return binarySearchRecursive(nums, target, 0, nums.length - 1);
}

function binarySearchRecursive(nums: number[], target: number, left: number, right: number): number {
    if (left > right) return -1;

    const mid = left + Math.floor((right - left) / 2);

    if (nums[mid] === target) {
        return mid;
    } else if (nums[mid] < target) {
        return binarySearchRecursive(nums, target, mid + 1, right);
    } else {
        return binarySearchRecursive(nums, target, left, mid - 1);
    }
}
```

**Time Complexity:** O(log n)
**Space Complexity:** O(log n) - recursive call stack

---

## Problem 2: Search in Rotated Sorted Array

### Approach: Modified Binary Search

```typescript
function search(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        const mid = left + Math.floor((right - left) / 2);

        // Found target
        if (nums[mid] === target) {
            return mid;
        }

        // Determine which half is sorted
        if (nums[left] <= nums[mid]) {
            // Left half is sorted
            if (nums[left] <= target && target < nums[mid]) {
                // Target is in the sorted left half
                right = mid - 1;
            } else {
                // Target is in the unsorted right half
                left = mid + 1;
            }
        } else {
            // Right half is sorted
            if (nums[mid] < target && target <= nums[right]) {
                // Target is in the sorted right half
                left = mid + 1;
            } else {
                // Target is in the unsorted left half
                right = mid - 1;
            }
        }
    }

    return -1;
}
```

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

**Key Insight:** At least one half of the array is always sorted after rotation. We can determine which half is sorted and whether the target lies in that half.

---

## Problem 3: Find Minimum in Rotated Sorted Array

### Approach 1: Binary Search for Inflection Point

```typescript
function findMin(nums: number[]): number {
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        const mid = left + Math.floor((right - left) / 2);

        // If mid element is greater than right element,
        // minimum must be in the right half
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            // Minimum is in left half (including mid)
            right = mid;
        }
    }

    return nums[left];
}
```

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

### Approach 2: Check Already Sorted First

```typescript
function findMin(nums: number[]): number {
    let left = 0;
    let right = nums.length - 1;

    // Handle case when array is not rotated
    if (nums[left] <= nums[right]) {
        return nums[left];
    }

    while (left < right) {
        const mid = left + Math.floor((right - left) / 2);

        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return nums[left];
}
```

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

---

## Problem 4: Search a 2D Matrix

### Approach 1: Treat as 1D Array

```typescript
function searchMatrix(matrix: number[][], target: number): boolean {
    if (!matrix.length || !matrix[0].length) return false;

    const m = matrix.length;
    const n = matrix[0].length;
    let left = 0;
    let right = m * n - 1;

    while (left <= right) {
        const mid = left + Math.floor((right - left) / 2);
        // Convert 1D index to 2D coordinates
        const row = Math.floor(mid / n);
        const col = mid % n;
        const value = matrix[row][col];

        if (value === target) {
            return true;
        } else if (value < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return false;
}
```

**Time Complexity:** O(log(m*n))
**Space Complexity:** O(1)

### Approach 2: Two Binary Searches

```typescript
function searchMatrix(matrix: number[][], target: number): boolean {
    if (!matrix.length || !matrix[0].length) return false;

    const m = matrix.length;
    const n = matrix[0].length;

    // Binary search to find the correct row
    let top = 0;
    let bottom = m - 1;

    while (top <= bottom) {
        const midRow = top + Math.floor((bottom - top) / 2);

        if (matrix[midRow][0] <= target && target <= matrix[midRow][n - 1]) {
            // Target might be in this row, do binary search
            return binarySearchRow(matrix[midRow], target);
        } else if (target < matrix[midRow][0]) {
            bottom = midRow - 1;
        } else {
            top = midRow + 1;
        }
    }

    return false;
}

function binarySearchRow(row: number[], target: number): boolean {
    let left = 0;
    let right = row.length - 1;

    while (left <= right) {
        const mid = left + Math.floor((right - left) / 2);
        if (row[mid] === target) return true;
        if (row[mid] < target) left = mid + 1;
        else right = mid - 1;
    }

    return false;
}
```

**Time Complexity:** O(log m + log n) = O(log(m*n))
**Space Complexity:** O(1)

---

## Problem 5: Koko Eating Bananas

### Approach: Binary Search on Answer Space

```typescript
function minEatingSpeed(piles: number[], h: number): number {
    // Binary search on eating speed
    let left = 1;
    let right = Math.max(...piles);
    let result = right;

    while (left <= right) {
        const mid = left + Math.floor((right - left) / 2);

        if (canEatAll(piles, h, mid)) {
            result = mid;
            right = mid - 1;  // Try to find smaller speed
        } else {
            left = mid + 1;   // Need faster speed
        }
    }

    return result;
}

function canEatAll(piles: number[], h: number, speed: number): boolean {
    let hoursNeeded = 0;

    for (const pile of piles) {
        // Hours needed for this pile at given speed
        hoursNeeded += Math.ceil(pile / speed);

        // Early termination
        if (hoursNeeded > h) return false;
    }

    return hoursNeeded <= h;
}
```

**Time Complexity:** O(n * log(max(piles)))
**Space Complexity:** O(1)

**Key Insight:** We're not searching in an array, but in the answer space [1, max(piles)]. Binary search works because if Koko can eat all bananas at speed k, she can also eat them at any speed > k.

---

## Problem 6: Find Peak Element

### Approach: Binary Search on Slope

```typescript
function findPeakElement(nums: number[]): number {
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        const mid = left + Math.floor((right - left) / 2);

        // Compare mid with mid + 1
        if (nums[mid] > nums[mid + 1]) {
            // Peak is in left half (including mid)
            right = mid;
        } else {
            // Peak is in right half (excluding mid)
            left = mid + 1;
        }
    }

    return left;
}
```

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

**Key Insight:** If nums[mid] < nums[mid + 1], we're on an ascending slope, so there must be a peak to the right. Otherwise, we're on a descending slope or at a peak, so the peak is to the left (or at mid).

---

## Problem 7: Search Insert Position

### Approach 1: Standard Binary Search with Modification

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

    // If not found, left is the insert position
    return left;
}
```

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

### Approach 2: Find First Position >= Target

```typescript
function searchInsert(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length;

    while (left < right) {
        const mid = left + Math.floor((right - left) / 2);

        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}
```

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

---

## Problem 8: First Bad Version

### Approach: Binary Search for First True

```typescript
/**
 * The knows API is defined in the parent class Relation.
 * isBadVersion(version: number): boolean {
 *     ...
 * };
 */

var solution = function(isBadVersion: (version: number) => boolean) {
    return function(n: number): number {
        let left = 1;
        let right = n;

        while (left < right) {
            const mid = left + Math.floor((right - left) / 2);

            if (isBadVersion(mid)) {
                // First bad version is at mid or before
                right = mid;
            } else {
                // First bad version is after mid
                left = mid + 1;
            }
        }

        return left;
    };
};
```

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

**Key Pattern:** This is a template for finding the first position where a condition becomes true in a sorted boolean array [F, F, F, T, T, T].

---

## Problem 9: Time Based Key-Value Store

### Approach: HashMap with Binary Search

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
        if (!this.store.has(key)) {
            return "";
        }

        const values = this.store.get(key)!;

        // Binary search for largest timestamp <= given timestamp
        let left = 0;
        let right = values.length - 1;
        let result = "";

        while (left <= right) {
            const mid = left + Math.floor((right - left) / 2);

            if (values[mid][0] <= timestamp) {
                result = values[mid][1];
                left = mid + 1;  // Look for a larger valid timestamp
            } else {
                right = mid - 1;
            }
        }

        return result;
    }
}
```

**Time Complexity:**
- set: O(1)
- get: O(log n) where n is the number of values for the key

**Space Complexity:** O(n) where n is total number of set operations

---

## Problem 10: Median of Two Sorted Arrays

### Approach 1: Binary Search on Smaller Array

```typescript
function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    // Ensure nums1 is the smaller array
    if (nums1.length > nums2.length) {
        return findMedianSortedArrays(nums2, nums1);
    }

    const m = nums1.length;
    const n = nums2.length;
    let left = 0;
    let right = m;

    while (left <= right) {
        const partitionX = left + Math.floor((right - left) / 2);
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
            // We are too far on right side for partitionX
            right = partitionX - 1;
        } else {
            // We are too far on left side for partitionX
            left = partitionX + 1;
        }
    }

    throw new Error("Input arrays are not sorted");
}
```

**Time Complexity:** O(log(min(m, n)))
**Space Complexity:** O(1)

### Approach 2: Find Kth Element (More Intuitive)

```typescript
function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    const total = nums1.length + nums2.length;

    if (total % 2 === 1) {
        return findKth(nums1, nums2, Math.floor(total / 2));
    } else {
        const left = findKth(nums1, nums2, Math.floor(total / 2) - 1);
        const right = findKth(nums1, nums2, Math.floor(total / 2));
        return (left + right) / 2;
    }
}

function findKth(nums1: number[], nums2: number[], k: number): number {
    // Finds the kth smallest element (0-indexed)
    const m = nums1.length;
    const n = nums2.length;

    if (m > n) {
        return findKth(nums2, nums1, k);
    }

    if (m === 0) {
        return nums2[k];
    }

    if (k === 0) {
        return Math.min(nums1[0], nums2[0]);
    }

    const i = Math.min(m, Math.floor((k + 1) / 2));
    const j = Math.floor((k + 1) / 2);

    if (nums1[i - 1] < nums2[j - 1]) {
        return findKth(nums1.slice(i), nums2, k - i);
    } else {
        return findKth(nums1, nums2.slice(j), k - j);
    }
}
```

**Time Complexity:** O(log(m + n))
**Space Complexity:** O(log(m + n)) due to recursion

---

## Common Patterns Summary

1. **Classic Binary Search:** Use when searching for exact value in sorted array
2. **Find First/Last Position:** Use different templates based on need
3. **Search in Rotated Array:** Identify which half is sorted
4. **Binary Search on Answer:** When optimizing a value within a range
5. **Peak Finding:** Use slope comparison
6. **2D to 1D Conversion:** Treat 2D matrix as flattened array

## Interview Tips

- Always handle edge cases (empty array, single element)
- Use `left + (right - left) / 2` to prevent overflow
- Be clear about inclusive vs exclusive bounds
- Test with small examples to verify logic
- Consider whether duplicates affect the solution