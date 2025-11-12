# Lesson: Binary Search

---

## 📹 Video 1: Binary Search Fundamentals (15 min)

**"Binary Search - Ultimate Guide" by NeetCode**
https://www.youtube.com/watch?v=s4DPM8ct1pI

**Focus on:**
- Core algorithm mechanics
- Loop invariants
- Time complexity O(log n)
- Template patterns

---

## 📹 Video 2: Rotated Arrays & Variations (18 min)

**"Binary Search - Rotated Sorted Array" by NeetCode**
https://www.youtube.com/watch?v=U8XENwh8Oy8

**Alternative:**
"Find Minimum in Rotated Sorted Array" by NeetCode
https://www.youtube.com/watch?v=nIVW4P8b1VA

**Focus on:**
- Handling rotated sorted arrays
- Finding pivot points
- Modified binary search
- When one half is always sorted

---

## 📹 Video 3: Binary Search on Answer Space (14 min)

**"Koko Eating Bananas - Binary Search" by NeetCode**
https://www.youtube.com/watch?v=U2SozAs9RzA

**Focus on:**
- Binary search on answer range
- Minimization/maximization problems
- Monotonic properties
- When to apply this pattern

---

## 🎯 Binary Search: Core Concept

### What is Binary Search?

Efficient algorithm finding target in **sorted** array by repeatedly halving search space.

**Key insight:** Eliminate half of remaining elements each step → O(log n).

### Why It Matters

**Real-world applications:**
- Database indexing
- Git bisect (finding bugs)
- Resource allocation
- Optimization problems
- Finding roots of equations

---

## 📊 Complexity Analysis

### Time Complexity

Starting with n elements:
- After 1 comparison: n/2 remain
- After 2 comparisons: n/4 remain
- After k comparisons: n/(2^k) remain

Stop when n/(2^k) = 1:
- 2^k = n
- k = log₂(n)

**Therefore:** O(log n) time

**Example:** Array of 1,000,000 elements → ~20 comparisons max!

### Space Complexity

- **Iterative:** O(1) - only variables
- **Recursive:** O(log n) - call stack

---

## 🔧 Binary Search Templates

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
- Search space: `[left, right]` (inclusive)
- Mid calculation avoids overflow
- Termination: `left > right`

**Time:** O(log n) | **Space:** O(1)

---

### Template 2: Find First/Last Position

**Use when:** Finding insertion point or first occurrence

```typescript
// Find first position >= target
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

// Find last position <= target
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

**Key points:**
- Condition: `left < right`
- Search space: `[left, right)` (right exclusive)
- Termination: `left === right`
- Used for boundaries

---

### Template 3: Binary Search on Answer Space

**Use when:** Finding minimum/maximum value satisfying condition

```typescript
// Example: Finding square root
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

**Pattern recognition:** "Find minimum k such that..." → binary search on answer

---

## 🧩 Advanced Patterns

### Pattern 1: Rotated Sorted Array

**📹 Learn:** [Search in Rotated Sorted Array](https://www.youtube.com/watch?v=U8XENwh8Oy8) by NeetCode (~12 min)

**Use when:** Sorted array rotated at unknown pivot

```typescript
function searchRotated(nums: number[], target: number): number {
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

**Key insight:** At least one half always sorted. Check which half, then if target in sorted half.

**Time:** O(log n) | **Space:** O(1)

---

### Pattern 2: Find Minimum in Rotated Array

**📹 Learn:** [Find Minimum in Rotated Sorted Array](https://www.youtube.com/watch?v=nIVW4P8b1VA) by NeetCode (~8 min)

```typescript
function findMin(nums: number[]): number {
  let left = 0;
  let right = nums.length - 1;

  // Already sorted
  if (nums[left] < nums[right]) return nums[left];

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

**Key insight:** Compare mid with right. If `nums[mid] > nums[right]`, inflection point (minimum) is right.

---

### Pattern 3: Search in 2D Matrix

**📹 Learn:** [Search a 2D Matrix](https://www.youtube.com/watch?v=Ber2pi2C0j0) by NeetCode (~10 min)

```typescript
function searchMatrix(matrix: number[][], target: number): boolean {
  const m = matrix.length;
  const n = matrix[0].length;
  let left = 0;
  let right = m * n - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
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

**Key insight:** Treat 2D matrix as flattened 1D array. Convert index: `row = idx / cols`, `col = idx % cols`.

**Time:** O(log(m × n)) | **Space:** O(1)

---

### Pattern 4: Binary Search on Answer Space

**📹 Learn:** [Koko Eating Bananas](https://www.youtube.com/watch?v=U2SozAs9RzA) by NeetCode (~14 min)

**Use when:** "Find minimum k such that condition(k) is true"

```typescript
function minEatingSpeed(piles: number[], h: number): number {
  let left = 1;
  let right = Math.max(...piles);

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    if (canFinish(piles, mid, h)) {
      right = mid; // Try smaller speed
    } else {
      left = mid + 1; // Need faster speed
    }
  }

  return left;
}

function canFinish(piles: number[], speed: number, h: number): boolean {
  let hours = 0;
  for (const pile of piles) {
    hours += Math.ceil(pile / speed);
  }
  return hours <= h;
}
```

**Key insight:** Binary search on answer (speed), not on array. Check if answer valid, adjust range.

**Time:** O(n log m) where m = max(piles) | **Space:** O(1)

---

## 💡 Common Pitfalls & Solutions

### Pitfall 1: Integer Overflow

**Problem:** `(left + right) / 2` can overflow with large numbers

```typescript
// ❌ Wrong - potential overflow
const mid = Math.floor((left + right) / 2);

// ✅ Correct - prevents overflow
const mid = left + Math.floor((right - left) / 2);
```

---

### Pitfall 2: Infinite Loops

**Problem:** Pointers don't move toward termination

```typescript
// ❌ Wrong - can cause infinite loop
while (left < right) {
  const mid = Math.floor((left + right) / 2);
  if (condition) {
    right = mid; // OK
  } else {
    left = mid; // ❌ Infinite loop if left === mid
  }
}

// ✅ Correct
while (left < right) {
  const mid = Math.floor((left + right) / 2);
  if (condition) {
    right = mid;
  } else {
    left = mid + 1; // ✅ Always moves
  }
}
```

---

### Pitfall 3: Off-by-One Errors

**Problem:** Wrong boundaries or conditions

```typescript
// Template 1: [left, right] inclusive
while (left <= right) {
  // ...
  left = mid + 1;
  right = mid - 1;
}

// Template 2: [left, right) exclusive
while (left < right) {
  // ...
  left = mid + 1;
  right = mid; // Not mid - 1!
}
```

**Rule:** Be clear about inclusive vs exclusive ranges. Test with small arrays.

---

### Pitfall 4: Wrong Template

| Problem Type | Template | Condition |
|--------------|----------|-----------|
| Exact match | 1 | `left <= right` |
| First/last occurrence | 2 | `left < right` |
| Insertion point | 2 | `left < right` |
| Min/max with condition | 2 or 3 | Depends |

---

## 🎯 Decision Tree

```
Is array sorted?
├── Yes
│   ├── Finding exact value? → Template 1
│   ├── Finding first/last? → Template 2
│   └── Array rotated? → Modified Template 1
└── No
    └── Monotonic property exists?
        ├── Yes → Binary search on answer space
        └── No → Binary search not applicable
```

---

## 📝 TypeScript-Specific Tips

### Avoid Number Precision Issues

```typescript
// ✅ Good - using Math.floor
const mid = left + Math.floor((right - left) / 2);

// ❌ Avoid bitwise (can behave unexpectedly)
const mid = left + ((right - left) >> 1);
```

### Handle Edge Cases

```typescript
function binarySearch(nums: number[] | null | undefined, target: number): number {
  // Check for invalid input
  if (!nums || nums.length === 0) return -1;

  // Single element
  if (nums.length === 1) return nums[0] === target ? 0 : -1;

  // Continue with binary search
  // ...
}
```

### Type Safety with Generics

```typescript
function binarySearch<T>(
  arr: T[],
  target: T,
  compareFn: (a: T, b: T) => number
): number {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);
    const cmp = compareFn(arr[mid], target);

    if (cmp === 0) return mid;
    if (cmp < 0) left = mid + 1;
    else right = mid - 1;
  }

  return -1;
}
```

---

## 🎤 Interview Communication

### Clarifying Questions

Always ask:
- "Is the array sorted?"
- "Are there duplicates?"
- "What should I return if not found?"
- "Can I modify the input?"
- "Any constraints on array size?"

### Explain Your Approach

**Say this:**
- "Using binary search for O(log n) time instead of O(n) linear search"
- "Choosing Template 1 for exact match since we return immediately on finding target"
- "Comparing mid with right endpoint to determine which half contains minimum"
- "Binary searching on answer space from 1 to max(array) for minimum valid speed"

### Edge Cases to Test

- Empty array `[]`
- Single element `[5]`
- Target not in array
- Target at boundaries (first/last)
- All elements same `[3,3,3,3]`
- Already sorted (no rotation)

---

## 🎯 Pattern Recognition

| Problem Hint | Pattern |
|--------------|---------|
| "O(log n) required" | Binary search |
| "Sorted array" | Classic binary search |
| "Find minimum k such that..." | Binary search on answer |
| "Rotated sorted array" | Modified binary search |
| "First/last occurrence" | Template 2 |
| "2D matrix with sorted rows" | 2D binary search |
| "Peak element" | Binary search on local property |

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **Template 1:** `while (left <= right)` - exact match
- **Template 2:** `while (left < right)` - boundaries
- **Always:** Use `left + (right - left) / 2`
- **Test:** Empty, single, boundaries

---

[Back to Session README](./README.md)
