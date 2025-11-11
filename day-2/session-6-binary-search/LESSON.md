# Lesson: Binary Search

## 📹 Video Assignment (25 minutes)

**Primary Video:**
"Binary Search - Ultimate Guide" by NeetCode
https://www.youtube.com/watch?v=s4DPM8ct1pI

**Alternative Videos** (if you need different explanations):
- "Binary Search Algorithm" by CS Dojo (17 min): https://www.youtube.com/watch?v=6ysjqCUv3K4
- "Binary Search Tutorial" by Errichto (20 min): https://www.youtube.com/watch?v=GU7DpgHINWQ

**What to focus on:**
- Understanding the divide-and-conquer approach
- Loop invariants and termination conditions
- Different templates and when to use each
- Common pitfalls and edge cases

---

## 📚 Binary Search - Core Concepts

### What is Binary Search?

Binary search is an efficient algorithm for finding a target value in a **sorted** array by repeatedly dividing the search interval in half. If the value is less than the item in the middle, it searches the left half; otherwise, it searches the right half.

**Key insight:** By eliminating half of the remaining elements at each step, we achieve O(log n) time complexity.

### Why Binary Search Matters

**Real-world applications:**
- Database indexing (B-trees)
- Git bisect for finding bugs
- Load balancing and resource allocation
- Finding roots of equations
- Optimization problems

---

## The Mathematics Behind Binary Search

### Time Complexity Analysis

Starting with n elements:
- After 1 comparison: n/2 elements remain
- After 2 comparisons: n/4 elements remain
- After k comparisons: n/(2^k) elements remain

We stop when n/(2^k) = 1, solving for k:
- 2^k = n
- k = log₂(n)

**Therefore:** Binary search has O(log n) time complexity.

### Space Complexity

- **Iterative:** O(1) - only uses a few variables
- **Recursive:** O(log n) - call stack depth

---

## Binary Search Templates

### Template 1: Classic Binary Search

**Use when:** Finding exact match in sorted array

```typescript
function binarySearch(nums: number[], target: number): number {
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

**Key points:**
- Condition: `left <= right`
- Search space: `[left, right]`
- Termination: `left > right`

### Template 2: Find Leftmost/First Position

**Use when:** Finding first occurrence or insertion point

```typescript
function findFirst(nums: number[], target: number): number {
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

**Key points:**
- Condition: `left < right`
- Search space: `[left, right)`
- Termination: `left === right`

### Template 3: Find Rightmost/Last Position

**Use when:** Finding last occurrence

```typescript
function findLast(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length;

    while (left < right) {
        const mid = left + Math.floor((right - left) / 2);

        if (nums[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left - 1;
}
```

---

## Advanced Patterns

### 1. Binary Search on Answer Space

Instead of searching in an array, search for an answer in a range.

**Example:** Finding square root

```typescript
function sqrt(x: number): number {
    let left = 0;
    let right = x;
    let result = 0;

    while (left <= right) {
        const mid = left + Math.floor((right - left) / 2);

        if (mid * mid <= x) {
            result = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return result;
}
```

### 2. Rotated Sorted Array

Handle arrays that are sorted but rotated.

**Key insight:** At least one half is always sorted.

```typescript
function searchRotated(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        const mid = left + Math.floor((right - left) / 2);

        if (nums[mid] === target) return mid;

        // Check which half is sorted
        if (nums[left] <= nums[mid]) {
            // Left half is sorted
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {
            // Right half is sorted
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

### 3. Search in 2D Matrix

Treat 2D matrix as 1D sorted array.

```typescript
function searchMatrix(matrix: number[][], target: number): boolean {
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

---

## Common Pitfalls and Solutions

### 1. Integer Overflow

**Problem:** `(left + right) / 2` can overflow

**Solution:** Use `left + (right - left) / 2`

### 2. Infinite Loops

**Problem:** Incorrect pointer updates

**Solution:** Ensure pointers always move toward termination

### 3. Off-by-One Errors

**Problem:** Wrong boundaries or conditions

**Solution:** Be clear about inclusive vs exclusive ranges

### 4. Handling Duplicates

**Problem:** Multiple occurrences of target

**Solution:** Use appropriate template for first/last occurrence

---

## Decision Tree for Binary Search Problems

```
Is the array sorted?
├── Yes
│   ├── Finding exact value? → Template 1
│   ├── Finding first/last occurrence? → Template 2/3
│   └── Array is rotated? → Modified binary search
└── No
    └── Can we define a monotonic property?
        ├── Yes → Binary search on answer space
        └── No → Binary search not applicable
```

---

## Practice Problems by Pattern

### Classic Binary Search
- Binary Search (Easy)
- Search Insert Position (Easy)
- First Bad Version (Easy)

### Rotated Arrays
- Search in Rotated Sorted Array (Medium)
- Find Minimum in Rotated Sorted Array (Medium)

### Binary Search on Answer
- Koko Eating Bananas (Medium)
- Sqrt(x) (Easy)

### Advanced Applications
- Time Based Key-Value Store (Medium)
- Median of Two Sorted Arrays (Hard)

---

## TypeScript-Specific Tips

### 1. Avoid Number Precision Issues

```typescript
// Good - using Math.floor
const mid = left + Math.floor((right - left) / 2);

// Bad - truncation might not work as expected
const mid = left + ~~((right - left) / 2);
```

### 2. Type Safety

```typescript
function binarySearch<T>(
    arr: T[],
    target: T,
    compareFn: (a: T, b: T) => number
): number {
    // Implementation with custom comparison
}
```

### 3. Handling undefined/null

```typescript
function search(nums: number[] | null | undefined, target: number): number {
    if (!nums || nums.length === 0) return -1;
    // Continue with binary search
}
```

---

## Interview Tips

### 1. Clarifying Questions
- Is the array sorted?
- Are there duplicates?
- What should I return if not found?
- Can I modify the input?

### 2. Edge Cases to Test
- Empty array
- Single element
- Target not in array
- Target at boundaries
- All elements are the same

### 3. Optimization Discussion
- Time: O(log n) vs O(n) linear search
- Space: Iterative O(1) vs Recursive O(log n)
- When binary search is overkill (small arrays)

### 4. Follow-up Questions
- "What if the array is not sorted?"
- "How would you handle duplicates?"
- "Can you make it generic for any type?"
- "What about finding k closest elements?"

---

## Summary

Binary search is more than just searching in a sorted array. It's a problem-solving technique that applies to any scenario where you can eliminate half of the possibilities at each step. Master the templates, understand the invariants, and practice recognizing when to apply binary search even when it's not obvious.

**Key takeaways:**
1. Always verify the array is sorted (or has monotonic property)
2. Choose the right template for your use case
3. Be careful with boundaries and off-by-one errors
4. Consider binary search for optimization problems
5. Practice until the pattern becomes second nature

---

## Next Steps

1. Complete the concept check with Claude
2. Work through the problems in order
3. Use hints only when stuck for 10+ minutes
4. Review solutions even if you solved it
5. Try to recognize patterns across problems

Ready? Let's start with Problem 1: Binary Search!