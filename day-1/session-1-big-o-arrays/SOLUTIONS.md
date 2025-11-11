# Solutions - Session 1: Big O & Arrays

Comprehensive TypeScript solutions with multiple approaches and complexity analysis.

---

## Problem 1: Two Sum

### Approach 1: Brute Force (Not Recommended)

```typescript
function twoSum(nums: number[], target: number): number[] {
  // Check every pair
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
  return []; // Should never reach (problem guarantees solution)
}
```

**Complexity:**
- Time: O(n²) - nested loops
- Space: O(1) - only variables

**Why not optimal:** Checking every pair is slow for large arrays.

---

### Approach 2: Hash Map (Optimal) ✅

```typescript
function twoSum(nums: number[], target: number): number[] {
  // Store value → index mapping
  const seen = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];

    // Check if complement exists
    if (seen.has(complement)) {
      return [seen.get(complement)!, i];
    }

    // Store current number
    seen.set(nums[i], i);
  }

  return []; // Never reached
}
```

**Complexity:**
- Time: O(n) - single loop, O(1) map operations
- Space: O(n) - hash map stores up to n elements

**Key Insight:** Trading space for time - use hash map for O(1) lookups instead of O(n) array search.

**Interview Points:**
- "I'm using a hash map to avoid the O(n²) brute force nested loops"
- "By storing values as I iterate, I can check if complement exists in O(1)"
- "This trades O(n) space for O(n) time complexity"

---

## Problem 2: Best Time to Buy and Sell Stock

### Approach: One Pass (Kadane's-like)

```typescript
function maxProfit(prices: number[]): number {
  if (prices.length === 0) return 0;

  let minPrice = prices[0];
  let maxProfit = 0;

  for (let i = 1; i < prices.length; i++) {
    // Update max profit if selling today gives better profit
    maxProfit = Math.max(maxProfit, prices[i] - minPrice);

    // Update minimum price seen so far
    minPrice = Math.min(minPrice, prices[i]);
  }

  return maxProfit;
}
```

**Complexity:**
- Time: O(n) - single pass
- Space: O(1) - only two variables

**Key Insight:**
- Must buy before selling
- Track lowest price seen so far
- At each day, calculate profit if we sold today
- Keep track of maximum profit

**Interview Points:**
- "I need to find the best buy/sell pair where buy comes before sell"
- "I'll track the minimum price and maximum profit as I scan left to right"
- "This is similar to Kadane's algorithm for max subarray"

---

## Problem 3: Contains Duplicate

### Approach: Hash Set

```typescript
function containsDuplicate(nums: number[]): boolean {
  const seen = new Set<number>();

  for (const num of nums) {
    // If already seen, we found a duplicate
    if (seen.has(num)) {
      return true;
    }

    seen.add(num);
  }

  return false;
}
```

**Complexity:**
- Time: O(n) - single pass
- Space: O(n) - set stores unique elements

**Alternative (one-liner):**
```typescript
function containsDuplicate(nums: number[]): boolean {
  return nums.length !== new Set(nums).size;
}
```

**Key Insight:** Use Set to track what we've seen. If we see it again, it's a duplicate.

---

## Problem 4: Product of Array Except Self

### Approach 1: Prefix & Suffix Arrays

```typescript
function productExceptSelf(nums: number[]): number[] {
  const n = nums.length;
  const result: number[] = new Array(n);

  // Build prefix products (product of all elements to the left)
  const prefix: number[] = new Array(n);
  prefix[0] = 1;
  for (let i = 1; i < n; i++) {
    prefix[i] = prefix[i - 1] * nums[i - 1];
  }

  // Build suffix products (product of all elements to the right)
  const suffix: number[] = new Array(n);
  suffix[n - 1] = 1;
  for (let i = n - 2; i >= 0; i--) {
    suffix[i] = suffix[i + 1] * nums[i + 1];
  }

  // Result is prefix * suffix for each position
  for (let i = 0; i < n; i++) {
    result[i] = prefix[i] * suffix[i];
  }

  return result;
}
```

**Complexity:**
- Time: O(n) - three passes
- Space: O(n) - prefix and suffix arrays

---

### Approach 2: Space Optimized (Optimal) ✅

```typescript
function productExceptSelf(nums: number[]): number[] {
  const n = nums.length;
  const result: number[] = new Array(n);

  // First pass: store prefix products in result
  result[0] = 1;
  for (let i = 1; i < n; i++) {
    result[i] = result[i - 1] * nums[i - 1];
  }

  // Second pass: multiply by suffix products on the fly
  let suffixProduct = 1;
  for (let i = n - 1; i >= 0; i--) {
    result[i] *= suffixProduct;
    suffixProduct *= nums[i];
  }

  return result;
}
```

**Complexity:**
- Time: O(n) - two passes
- Space: O(1) - not counting output array

**Key Insight:**
- For each position, need product of everything to left × everything to right
- Can build prefix products in result array
- Then multiply by suffix products in reverse pass
- Avoids extra arrays by reusing result and a variable

**Interview Points:**
- "I'll calculate prefix products left-to-right, then multiply by suffix products right-to-left"
- "This avoids division and handles zeros correctly"
- "By reusing the output array, I achieve O(1) extra space"

---

## Problem 5: Maximum Subarray (Kadane's Algorithm)

### Approach: Kadane's Algorithm

```typescript
function maxSubArray(nums: number[]): number {
  let maxSum = nums[0];
  let currentSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    // Either extend current subarray or start new one
    currentSum = Math.max(nums[i], currentSum + nums[i]);

    // Track overall maximum
    maxSum = Math.max(maxSum, currentSum);
  }

  return maxSum;
}
```

**Complexity:**
- Time: O(n) - single pass
- Space: O(1) - only two variables

**Key Insight (Kadane's Algorithm):**
- At each position, decide: continue current subarray or start fresh?
- If `currentSum + nums[i] < nums[i]`, better to start fresh
- Keep track of best sum seen so far

**Why it works:**
- If sum becomes negative, it won't help future elements
- Starting fresh from current element is better

**Interview Points:**
- "This is Kadane's algorithm - a classic DP problem"
- "At each step, I decide whether to extend the current subarray or start a new one"
- "If adding current element to previous sum makes it worse than just current element alone, I start fresh"

---

## Problem 6: Maximum Product Subarray

### Approach: Track Both Max and Min

```typescript
function maxProduct(nums: number[]): number {
  let maxProd = nums[0];
  let currentMax = nums[0];
  let currentMin = nums[0];

  for (let i = 1; i < nums.length; i++) {
    const num = nums[i];

    // If num is negative, swap max and min
    // (negative * max = new min, negative * min = new max)
    if (num < 0) {
      [currentMax, currentMin] = [currentMin, currentMax];
    }

    // Either extend current product or start fresh
    currentMax = Math.max(num, currentMax * num);
    currentMin = Math.min(num, currentMin * num);

    // Track overall maximum
    maxProd = Math.max(maxProd, currentMax);
  }

  return maxProd;
}
```

**Complexity:**
- Time: O(n) - single pass
- Space: O(1) - only variables

**Key Insight:**
- Similar to max subarray, but multiplication is trickier
- Negative × negative = positive! So track BOTH max and min
- When we see a negative number, min becomes max and vice versa
- Zero resets everything (product becomes 0)

---

## Problem 7: Find Minimum in Rotated Sorted Array

### Approach: Binary Search

```typescript
function findMin(nums: number[]): number {
  let left = 0;
  let right = nums.length - 1;

  // If not rotated, first element is minimum
  if (nums[left] < nums[right]) {
    return nums[left];
  }

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    // If mid > right, minimum must be in right half
    if (nums[mid] > nums[right]) {
      left = mid + 1;
    }
    // Otherwise, minimum is in left half (including mid)
    else {
      right = mid;
    }
  }

  return nums[left];
}
```

**Complexity:**
- Time: O(log n) - binary search
- Space: O(1) - only pointers

**Key Insight:**
- Compare mid with right endpoint (not left!)
- If nums[mid] > nums[right], inflection point is to the right
- Otherwise, minimum is to the left (could be mid itself)

---

## Problem 8: Search in Rotated Sorted Array

### Approach: Modified Binary Search

```typescript
function search(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (nums[mid] === target) return mid;

    // Determine which half is sorted
    if (nums[left] <= nums[mid]) {
      // Left half is sorted
      if (nums[left] <= target && target < nums[mid]) {
        right = mid - 1; // Target in left half
      } else {
        left = mid + 1;  // Target in right half
      }
    } else {
      // Right half is sorted
      if (nums[mid] < target && target <= nums[right]) {
        left = mid + 1;  // Target in right half
      } else {
        right = mid - 1; // Target in left half
      }
    }
  }

  return -1;
}
```

**Complexity:**
- Time: O(log n) - binary search
- Space: O(1) - only pointers

**Key Insight:**
- At least one half is always sorted
- Figure out which half is sorted
- Check if target is in the sorted half
- If yes, search that half; if no, search other half

---

## Problem 9: 3Sum

### Approach: Sort + Two Pointers

```typescript
function threeSum(nums: number[]): number[][] {
  const result: number[][] = [];
  nums.sort((a, b) => a - b); // Must sort first!

  for (let i = 0; i < nums.length - 2; i++) {
    // Skip duplicates for first number
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    // Two pointers for remaining two numbers
    let left = i + 1;
    let right = nums.length - 1;
    const target = -nums[i]; // We want nums[left] + nums[right] = target

    while (left < right) {
      const sum = nums[left] + nums[right];

      if (sum === target) {
        result.push([nums[i], nums[left], nums[right]]);

        // Skip duplicates
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

**Complexity:**
- Time: O(n²) - O(n log n) sort + O(n²) two pointers
- Space: O(1) - not counting output

**Key Insight:**
- Fix one number, use two pointers for other two (reduces to 2Sum)
- Sort first to enable two pointers and handle duplicates
- Skip duplicates to avoid duplicate triplets

---

## Problem 10: Container With Most Water

### Approach: Two Pointers

```typescript
function maxArea(height: number[]): number {
  let maxWater = 0;
  let left = 0;
  let right = height.length - 1;

  while (left < right) {
    // Calculate current area
    const width = right - left;
    const minHeight = Math.min(height[left], height[right]);
    const area = width * minHeight;

    maxWater = Math.max(maxWater, area);

    // Move pointer with smaller height (might find taller line)
    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return maxWater;
}
```

**Complexity:**
- Time: O(n) - single pass with two pointers
- Space: O(1) - only variables

**Key Insight:**
- Start with widest possible container (left=0, right=n-1)
- Area = min(height[left], height[right]) × width
- To potentially get larger area, move the pointer with smaller height
  - Why? Moving taller pointer will only decrease both width and height
  - Moving shorter pointer might find a taller line

**Interview Points:**
- "Starting with maximum width, I'll move pointers inward"
- "Moving the shorter line's pointer gives us a chance to find a taller line"
- "Moving the taller line's pointer would only decrease both dimensions"

---

## Common Patterns Summary

### Hash Map/Set Pattern (Problems 1, 3)
- Use for O(1) lookups
- Trade space for time
- Common in "find pair" or "check existence" problems

### Kadane's Pattern (Problems 5, 6)
- Track current and global optimum
- Decide at each step: extend or restart
- Works for max/min subarray problems

### Two Pointers (Problems 9, 10)
- Start at ends or same position
- Move based on condition
- O(n) time, O(1) space
- Requires sorted array (or sort first)

### Binary Search on Rotated Array (Problems 7, 8)
- At least one half is always sorted
- Figure out which half
- Compare mid with endpoints

### Prefix/Suffix (Problem 4)
- Calculate cumulative products/sums
- Useful for "all except current" problems

---

[Back to Problems](./PROBLEMS.md) | [Back to Session README](./README.md)
