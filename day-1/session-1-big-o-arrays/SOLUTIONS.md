# Solutions - Session 1: Big O & Arrays

TypeScript solutions with complexity analysis.

---

## Problem 1: Two Sum

### Approach 1: Brute Force

```typescript
function twoSum(nums: number[], target: number): number[] {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) return [i, j];
    }
  }
  return [];
}
```

**Time:** O(n²) | **Space:** O(1)
**Why not optimal:** Checking every pair is slow.

---

### Approach 2: Hash Map (Optimal) ✅

```typescript
function twoSum(nums: number[], target: number): number[] {
  const seen = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (seen.has(complement)) return [seen.get(complement)!, i];
    seen.set(nums[i], i);
  }

  return [];
}
```

**Time:** O(n) | **Space:** O(n)

**Key:** Trade space for time - hash map gives O(1) lookups vs O(n) array search.

**Say:** "Using hash map to avoid O(n²) nested loops. Trading O(n) space for O(n) time."

---

## Problem 2: Best Time to Buy/Sell Stock

```typescript
function maxProfit(prices: number[]): number {
  if (prices.length === 0) return 0;

  let minPrice = prices[0];
  let maxProfit = 0;

  for (let i = 1; i < prices.length; i++) {
    maxProfit = Math.max(maxProfit, prices[i] - minPrice);
    minPrice = Math.min(minPrice, prices[i]);
  }

  return maxProfit;
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** Track min price so far. At each day, calculate profit if selling today.

**Say:** "Track minimum price and maximum profit in single pass. Similar to Kadane's algorithm."

---

## Problem 3: Contains Duplicate

```typescript
function containsDuplicate(nums: number[]): boolean {
  const seen = new Set<number>();

  for (const num of nums) {
    if (seen.has(num)) return true;
    seen.add(num);
  }

  return false;
}
```

**Time:** O(n) | **Space:** O(n)

**Alternative one-liner:**
```typescript
function containsDuplicate(nums: number[]): boolean {
  return nums.length !== new Set(nums).size;
}
```

**Key:** Use Set to track seen values.

---

## Problem 4: Product of Array Except Self

### Approach 1: Prefix & Suffix Arrays

```typescript
function productExceptSelf(nums: number[]): number[] {
  const n = nums.length;
  const result: number[] = new Array(n);

  const prefix: number[] = new Array(n);
  prefix[0] = 1;
  for (let i = 1; i < n; i++) {
    prefix[i] = prefix[i - 1] * nums[i - 1];
  }

  const suffix: number[] = new Array(n);
  suffix[n - 1] = 1;
  for (let i = n - 2; i >= 0; i--) {
    suffix[i] = suffix[i + 1] * nums[i + 1];
  }

  for (let i = 0; i < n; i++) {
    result[i] = prefix[i] * suffix[i];
  }

  return result;
}
```

**Time:** O(n) | **Space:** O(n)

---

### Approach 2: Space Optimized (Optimal) ✅

```typescript
function productExceptSelf(nums: number[]): number[] {
  const n = nums.length;
  const result: number[] = new Array(n);

  // Store prefix in result
  result[0] = 1;
  for (let i = 1; i < n; i++) {
    result[i] = result[i - 1] * nums[i - 1];
  }

  // Multiply by suffix on the fly
  let suffixProduct = 1;
  for (let i = n - 1; i >= 0; i--) {
    result[i] *= suffixProduct;
    suffixProduct *= nums[i];
  }

  return result;
}
```

**Time:** O(n) | **Space:** O(1) (excluding output)

**Key:** For each position, need product left × product right. Build prefix in result, then multiply by suffix in reverse pass.

**Say:** "Calculate prefix products left-to-right, then multiply by suffix right-to-left. Reusing output array achieves O(1) space."

---

## Problem 5: Maximum Subarray (Kadane's)

```typescript
function maxSubArray(nums: number[]): number {
  let maxSum = nums[0];
  let currentSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    currentSum = Math.max(nums[i], currentSum + nums[i]);
    maxSum = Math.max(maxSum, currentSum);
  }

  return maxSum;
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** At each position, decide: extend current subarray or start fresh. If `currentSum + nums[i] < nums[i]`, start fresh.

**Say:** "Kadane's algorithm - decide whether to extend current subarray or start new one. If adding current element makes sum worse than element alone, start fresh."

---

## Problem 6: Maximum Product Subarray

```typescript
function maxProduct(nums: number[]): number {
  let maxProd = nums[0];
  let currentMax = nums[0];
  let currentMin = nums[0];

  for (let i = 1; i < nums.length; i++) {
    const num = nums[i];

    // Swap max/min if num is negative
    if (num < 0) {
      [currentMax, currentMin] = [currentMin, currentMax];
    }

    currentMax = Math.max(num, currentMax * num);
    currentMin = Math.min(num, currentMin * num);
    maxProd = Math.max(maxProd, currentMax);
  }

  return maxProd;
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** Track both max AND min. Negative × negative = positive, so min can become max when multiplied by negative. Zero resets everything.

---

## Problem 7: Find Min in Rotated Sorted Array

```typescript
function findMin(nums: number[]): number {
  let left = 0;
  let right = nums.length - 1;

  if (nums[left] < nums[right]) return nums[left];

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    if (nums[mid] > nums[right]) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  return nums[left];
}
```

**Time:** O(log n) | **Space:** O(1)

**Key:** Compare mid with right. If `nums[mid] > nums[right]`, inflection point (minimum) is in right half. Otherwise left half (including mid).

---

## Problem 8: Search in Rotated Sorted Array

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

**Key:** At least one half is always sorted. Determine which half, check if target is in that half. If yes, search it; if no, search other half.

---

## Problem 9: 3Sum

```typescript
function threeSum(nums: number[]): number[][] {
  const result: number[][] = [];
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let left = i + 1;
    let right = nums.length - 1;
    const target = -nums[i];

    while (left < right) {
      const sum = nums[left] + nums[right];

      if (sum === target) {
        result.push([nums[i], nums[left], nums[right]]);

        while (left < right && nums[left] === nums[left + 1]) left++;
        while (left < right && nums[right] === nums[right - 1]) right--;

        left++;
        right--;
      } else if (sum < target) {
        left++;
      } else {
        right--;
      }
    }
  }

  return result;
}
```

**Time:** O(n²) | **Space:** O(1) (excluding output)

**Key:** Fix one number, use two pointers for other two (reduces to 2Sum). Sort first to enable pointers and handle duplicates. Skip duplicates to avoid duplicate triplets.

---

## Problem 10: Container With Most Water

```typescript
function maxArea(height: number[]): number {
  let maxWater = 0;
  let left = 0;
  let right = height.length - 1;

  while (left < right) {
    const width = right - left;
    const minHeight = Math.min(height[left], height[right]);
    const area = width * minHeight;

    maxWater = Math.max(maxWater, area);

    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return maxWater;
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** Start with widest container. Area = min(height[left], height[right]) × width. Move pointer with smaller height - might find taller line. Moving taller pointer only decreases both dimensions.

**Say:** "Starting with maximum width, move inward. Moving shorter line's pointer gives chance to find taller line. Moving taller pointer would decrease both dimensions."

---

## Pattern Summary

### Hash Map/Set (Problems 1, 3)
- Use for O(1) lookups
- Trade space for time
- Common in "find pair" or "check existence"

### Kadane's (Problems 5, 6)
- Track current and global optimum
- Decide at each step: extend or restart
- Max/min subarray problems

### Two Pointers (Problems 9, 10)
- Start at ends or same position
- Move based on condition
- O(n) time, O(1) space
- Usually requires sorted array

### Binary Search on Rotated Array (Problems 7, 8)
- At least one half always sorted
- Determine which half
- Compare mid with endpoints

### Prefix/Suffix (Problem 4)
- Calculate cumulative products/sums
- "All except current" problems

---

[Back to Problems](./PROBLEMS.md) | [Back to README](./README.md)
