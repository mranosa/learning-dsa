# Hints - Session 1: Big O & Arrays

Progressive hints for 10 problems. Struggling is part of learning.

---

## Problem 1: Two Sum

### Level 1
What data structure gives O(1) lookup? Need to check "does complement exist?"

### Level 2
Hash map stores numbers seen. For each number, calculate `complement = target - current`. If complement exists in map, found pair.

### Level 3
```typescript
const seen = new Map<number, number>();
for (let i = 0; i < nums.length; i++) {
  const complement = target - nums[i];
  if (seen.has(complement)) return [seen.get(complement)!, i];
  seen.set(nums[i], i);
}
```

---

## Problem 2: Best Time to Buy/Sell Stock

### Level 1
Must buy before sell. Track minimum price seen. At each price, what's profit if selling today?

### Level 2
Keep `minPrice` (lowest so far) and `maxProfit` (best so far). Update both as you iterate.

### Level 3
```typescript
let minPrice = prices[0], maxProfit = 0;
for (let i = 1; i < prices.length; i++) {
  maxProfit = Math.max(maxProfit, prices[i] - minPrice);
  minPrice = Math.min(minPrice, prices[i]);
}
```

---

## Problem 3: Contains Duplicate

### Level 1
Use Set to remember seen numbers. If see number again, what does that mean?

### Level 2
Loop through array. Before adding to Set, check if already there. If yes → duplicate.

### Level 3
```typescript
const seen = new Set<number>();
for (const num of nums) {
  if (seen.has(num)) return true;
  seen.add(num);
}
return false;
```

---

## Problem 4: Product of Array Except Self

### Level 1
For each position: product of everything LEFT × everything RIGHT. Calculate separately?

### Level 2
- Pass 1: prefix products (left to right)
- Pass 2: suffix products (right to left)
- `result[i] = prefix[i] × suffix[i]`

### Level 3 (Space Optimized)
```typescript
// Build prefix in result
result[0] = 1;
for (let i = 1; i < n; i++) {
  result[i] = result[i - 1] * nums[i - 1];
}

// Multiply by suffix on fly
let suffix = 1;
for (let i = n - 1; i >= 0; i--) {
  result[i] *= suffix;
  suffix *= nums[i];
}
```

---

## Problem 5: Maximum Subarray

### Level 1
At each position: "Add to current sum or start fresh?"

### Level 2
Track `currentSum` and `maxSum`. At each element:
`currentSum = max(nums[i], currentSum + nums[i])`

### Level 3
```typescript
let maxSum = nums[0], currentSum = nums[0];
for (let i = 1; i < nums.length; i++) {
  currentSum = Math.max(nums[i], currentSum + nums[i]);
  maxSum = Math.max(maxSum, currentSum);
}
```

---

## Problem 6: Maximum Product Subarray

### Level 1
Multiplication twist: negative × negative = positive! Track both max AND min products.

### Level 2
When encounter negative, min becomes max and vice versa. Track `currentMax`, `currentMin`, `maxProduct`.

### Level 3
```typescript
let maxProd = nums[0], currentMax = nums[0], currentMin = nums[0];
for (let i = 1; i < nums.length; i++) {
  if (nums[i] < 0) {
    [currentMax, currentMin] = [currentMin, currentMax];
  }
  currentMax = Math.max(nums[i], currentMax * nums[i]);
  currentMin = Math.min(nums[i], currentMin * nums[i]);
  maxProd = Math.max(maxProd, currentMax);
}
```

---

## Problem 7: Find Min in Rotated Sorted Array

### Level 1
Binary search, but which half? Compare mid with right element.

### Level 2
If `nums[mid] > nums[right]` → inflection point (minimum) in right half.
Otherwise → left half (including mid).

### Level 3
```typescript
let left = 0, right = nums.length - 1;
while (left < right) {
  const mid = Math.floor((left + right) / 2);
  if (nums[mid] > nums[right]) {
    left = mid + 1;
  } else {
    right = mid;
  }
}
return nums[left];
```

---

## Problem 8: Search in Rotated Sorted Array

### Level 1
Modified binary search. At least one half always sorted. Determine which half, check if target there.

### Level 2
Compare `nums[left]` with `nums[mid]` to find sorted half. If left half sorted, check if target between `nums[left]` and `nums[mid]`.

### Level 3
```typescript
while (left <= right) {
  const mid = Math.floor((left + right) / 2);
  if (nums[mid] === target) return mid;

  if (nums[left] <= nums[mid]) {
    // Left sorted
    if (nums[left] <= target && target < nums[mid]) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  } else {
    // Right sorted
    if (nums[mid] < target && target <= nums[right]) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
}
```

---

## Problem 9: 3Sum

### Level 1
Sort array! Fix one number, use two pointers for other two. Reduces to 2Sum.

### Level 2
For each `nums[i]`, use pointers (`left = i+1`, `right = n-1`) to find two numbers summing to `-nums[i]`. Skip duplicates.

### Level 3
```typescript
nums.sort((a, b) => a - b);
const result: number[][] = [];

for (let i = 0; i < nums.length - 2; i++) {
  if (i > 0 && nums[i] === nums[i - 1]) continue;

  let left = i + 1, right = nums.length - 1;
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
```

---

## Problem 10: Container With Most Water

### Level 1
Two pointers at ends. Area = `min(height[left], height[right]) × width`. Move pointer with shorter line.

### Level 2
Why move shorter? Moving taller only decreases both width AND height, making area smaller.

### Level 3
```typescript
let maxArea = 0, left = 0, right = height.length - 1;

while (left < right) {
  const width = right - left;
  const minHeight = Math.min(height[left], height[right]);
  const area = width * minHeight;
  maxArea = Math.max(maxArea, area);

  if (height[left] < height[right]) {
    left++;
  } else {
    right--;
  }
}
```

---

## Pattern Hints

**"Find pair summing to..."** → Hash Map O(n) or Two Pointers (sorted) O(n)

**"Max/min subarray"** → Kadane's or DP

**"Sorted array" + O(log n)** → Binary Search (possibly modified)

**"All except self"** → Prefix/Suffix arrays

**"Array operations"** → Check if Two Pointers works

---

## Using Hints Effectively

1. Try 10+ min before Level 1
2. Try 5+ min after each hint
3. If use Level 3, mark for review and retry similar later
4. Don't feel bad - hints are for learning

Goal: Learn pattern, not just solve one problem.

---

[Back to Problems](./PROBLEMS.md) | [Back to Solutions](./SOLUTIONS.md)
