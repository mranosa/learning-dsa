# Hints - Session 1: Big O & Arrays

Progressive hints for all 10 problems. Use sparingly - struggling is part of learning!

---

## Problem 1: Two Sum

### Hint Level 1 (Gentle Nudge)
Think about how to avoid checking every pair. What data structure gives you O(1) lookup? You need to quickly check "does the complement exist?"

### Hint Level 2 (More Direct)
Use a hash map to store numbers you've seen. For each number, calculate `complement = target - current`. If complement exists in your map, you found the pair!

### Hint Level 3 (Step-by-Step)
Complete algorithm:
1. Create `seen = new Map<number, number>()` to store value→index
2. Loop through array with index `i`
3. Calculate `complement = target - nums[i]`
4. If `seen.has(complement)`, return `[seen.get(complement)!, i]`
5. Otherwise, `seen.set(nums[i], i)`

---

## Problem 2: Best Time to Buy and Sell Stock

### Hint Level 1
You must buy before you sell. Track the minimum price you've seen so far. At each price, what's the profit if you sold today?

### Hint Level 2
Keep two variables: `minPrice` (lowest price seen so far) and `maxProfit` (best profit so far). Update both as you iterate through prices.

### Hint Level 3
Algorithm:
1. Initialize `minPrice = prices[0]`, `maxProfit = 0`
2. For each price from index 1:
   - Calculate profit if selling today: `prices[i] - minPrice`
   - Update `maxProfit` if this is better
   - Update `minPrice` to `min(minPrice, prices[i])`
3. Return `maxProfit`

---

## Problem 3: Contains Duplicate

### Hint Level 1
Use a Set to remember what numbers you've seen. If you see a number again, what does that mean?

### Hint Level 2
Loop through the array. Before adding each number to the Set, check if it's already there. If yes → duplicate found!

### Hint Level 3
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

### Hint Level 1
For each position, you need the product of everything to its LEFT × everything to its RIGHT. Can you calculate these separately?

### Hint Level 2
Make two passes:
- First pass: calculate prefix products (product of all elements to the left)
- Second pass: calculate suffix products (product of all elements to the right)
- Result[i] = prefix[i] × suffix[i]

### Hint Level 3 (Space Optimized)
You can optimize space by:
1. Store prefix products in the result array
2. Then multiply by suffix products on the fly (don't need suffix array)
```typescript
// Build prefix in result
result[0] = 1;
for (let i = 1; i < n; i++) {
  result[i] = result[i - 1] * nums[i - 1];
}

// Multiply by suffix
let suffix = 1;
for (let i = n - 1; i >= 0; i--) {
  result[i] *= suffix;
  suffix *= nums[i];
}
```

---

## Problem 5: Maximum Subarray (Kadane's Algorithm)

### Hint Level 1
At each position, ask yourself: "Should I add this number to my current sum, or start fresh from here?"

### Hint Level 2
Keep track of `currentSum` and `maxSum`. At each element:
- `currentSum = max(nums[i], currentSum + nums[i])`
- If adding to previous sum makes it worse than just current element, start fresh

### Hint Level 3
Kadane's Algorithm:
```typescript
let maxSum = nums[0];
let currentSum = nums[0];

for (let i = 1; i < nums.length; i++) {
  // Extend or start new
  currentSum = Math.max(nums[i], currentSum + nums[i]);

  // Track best
  maxSum = Math.max(maxSum, currentSum);
}
```

---

## Problem 6: Maximum Product Subarray

### Hint Level 1
Similar to max subarray, but multiplication has a twist: negative × negative = positive! You need to track both the maximum AND minimum products.

### Hint Level 2
When you encounter a negative number, your min becomes your max and vice versa. Track `currentMax`, `currentMin`, and overall `maxProduct`.

### Hint Level 3
Algorithm:
```typescript
let maxProd = nums[0];
let currentMax = nums[0];
let currentMin = nums[0];

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

## Problem 7: Find Minimum in Rotated Sorted Array

### Hint Level 1
Use binary search, but how do you know which half to search? Compare the middle element with the rightmost element.

### Hint Level 2
If `nums[mid] > nums[right]`, the inflection point (and minimum) must be in the right half. Otherwise, it's in the left half (including mid).

### Hint Level 3
Binary search:
```typescript
let left = 0, right = nums.length - 1;

while (left < right) {
  const mid = Math.floor((left + right) / 2);

  if (nums[mid] > nums[right]) {
    left = mid + 1;  // Min in right half
  } else {
    right = mid;      // Min in left half (could be mid)
  }
}

return nums[left];
```

---

## Problem 8: Search in Rotated Sorted Array

### Hint Level 1
Modified binary search. Key insight: at least one half of the array is always sorted. Figure out which half, then check if target is in that half.

### Hint Level 2
Compare `nums[left]` with `nums[mid]` to determine which half is sorted. If left half sorted, check if target is between `nums[left]` and `nums[mid]`.

### Hint Level 3
Algorithm:
```typescript
while (left <= right) {
  const mid = Math.floor((left + right) / 2);
  if (nums[mid] === target) return mid;

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
```

---

## Problem 9: 3Sum

### Hint Level 1
Sort the array first! Then fix one number and use two pointers to find the other two. This reduces it to the 2Sum problem.

### Hint Level 2
For each number `nums[i]`, use two pointers (`left = i+1`, `right = n-1`) to find two numbers that sum to `-nums[i]`. Remember to skip duplicates!

### Hint Level 3
Algorithm:
```typescript
nums.sort((a, b) => a - b);
const result: number[][] = [];

for (let i = 0; i < nums.length - 2; i++) {
  if (i > 0 && nums[i] === nums[i - 1]) continue;  // Skip duplicates

  let left = i + 1, right = nums.length - 1;
  const target = -nums[i];

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
```

---

## Problem 10: Container With Most Water

### Hint Level 1
Use two pointers starting at both ends. Calculate area = `min(height[left], height[right]) × width`. Move the pointer pointing to the shorter line.

### Hint Level 2
Why move the shorter line's pointer? Because moving the taller line's pointer would only decrease both width AND height, making area smaller.

### Hint Level 3
Algorithm:
```typescript
let maxArea = 0;
let left = 0, right = height.length - 1;

while (left < right) {
  const width = right - left;
  const minHeight = Math.min(height[left], height[right]);
  const area = width * minHeight;

  maxArea = Math.max(maxArea, area);

  // Move pointer with smaller height
  if (height[left] < height[right]) {
    left++;
  } else {
    right--;
  }
}

return maxArea;
```

---

## General Hints by Pattern

### When You See "Find Pair That Sums To..."
→ Consider Hash Map (O(n)) or Two Pointers if sorted (O(n))

### When You See "Maximum/Minimum Subarray"
→ Consider Kadane's Algorithm or DP

### When You See "Sorted Array" + O(log n) Required
→ Binary Search (possibly modified for rotation)

### When You See "All Except Self"
→ Consider Prefix/Suffix arrays

### When You See "Array Operations"
→ Check if Two Pointers can work

---

## How to Use Hints Effectively

1. **Try for at least 10 minutes** before asking for Hint Level 1
2. **Try again for 5+ minutes** after each hint before asking for next level
3. **If you use Level 3 hint**, mark this problem for review and try a similar one later
4. **Don't feel bad** about using hints - it's part of learning!

Remember: The goal is to learn the pattern, not just solve this one problem.

---

[Back to Problems](./PROBLEMS.md) | [Back to Solutions](./SOLUTIONS.md)
