# Hints - Session 3: Sliding Window

Progressive hints. Struggling is part of learning.

---

## Problem 1: Best Time to Buy/Sell Stock

### Level 1
What's the minimum price seen so far? What's the profit if selling today?

### Level 2
Track minPrice and maxProfit. At each price: `profit = price - minPrice`.

### Level 3
```typescript
let minPrice = prices[0], maxProfit = 0;
for (let i = 1; i < prices.length; i++) {
  maxProfit = Math.max(maxProfit, prices[i] - minPrice);
  minPrice = Math.min(minPrice, prices[i]);
}
```

---

## Problem 2: Longest Substring Without Repeating

### Level 1
Use Set to track window. When find duplicate, shrink from left until removed.

### Level 2
Two pointers. While s[right] in Set, remove s[left] and increment left.

### Level 3
```typescript
const seen = new Set<string>();
let left = 0, maxLen = 0;
for (let right = 0; right < s.length; right++) {
  while (seen.has(s[right])) {
    seen.delete(s[left++]);
  }
  seen.add(s[right]);
  maxLen = Math.max(maxLen, right - left + 1);
}
```

---

## Problem 3: Longest Repeating Character Replacement

### Level 1
Valid window when: `windowSize - maxFrequency ≤ k`.

### Level 2
Track frequencies. Don't decrease maxFreq - only care about larger windows.

### Level 3
```typescript
const count = new Map<string, number>();
let left = 0, maxFreq = 0, result = 0;
for (let right = 0; right < s.length; right++) {
  count.set(s[right], (count.get(s[right]) || 0) + 1);
  maxFreq = Math.max(maxFreq, count.get(s[right])!);
  if (right - left + 1 - maxFreq > k) {
    count.set(s[left], count.get(s[left])! - 1);
    left++;
  }
  result = Math.max(result, right - left + 1);
}
```

---

## Problem 4: Permutation in String

### Level 1
Fixed window of size s1.length. Compare character frequencies.

### Level 2
Use array[26] for counts. Track number of matching positions (when matches === 26).

### Level 3
```typescript
const s1Count = new Array(26).fill(0);
const windowCount = new Array(26).fill(0);
// Count s1, build initial window
let matches = 0;
for (let i = 0; i < 26; i++) {
  if (s1Count[i] === windowCount[i]) matches++;
}
// Slide and check matches === 26
```

---

## Problem 5: Minimum Window Substring

### Level 1
Expand to include all needed characters. Contract to find minimum.

### Level 2
Track "have" (matching character frequencies) vs "need" (distinct chars in t).

### Level 3
```typescript
const tCount = new Map<string, number>();
// Count t
let have = 0, need = tCount.size;
const windowCount = new Map<string, number>();
// Expand right, when have === need, contract left
while (have === need) {
  // Update min, then shrink
}
```

---

## Problem 6: Maximum Sum of Distinct Subarrays

### Level 1
Fixed window k. Track sum and frequencies. Valid when freq.size === k.

### Level 2
Build initial window. Slide: add right, remove left. Check freq.size === k.

### Level 3
```typescript
const freq = new Map<number, number>();
let sum = 0;
// Build first k elements
for (let i = k; i < nums.length; i++) {
  sum += nums[i];
  freq.set(nums[i], (freq.get(nums[i]) || 0) + 1);
  // Remove left
  sum -= nums[i - k];
  // Update freq
  if (freq.size === k) maxSum = Math.max(maxSum, sum);
}
```

---

## Problem 7: Fruit Into Baskets

### Level 1
"Longest subarray with at most 2 distinct elements".

### Level 2
Map tracks fruit type → count. Contract when map.size > 2.

### Level 3
```typescript
const basket = new Map<number, number>();
let left = 0;
for (let right = 0; right < fruits.length; right++) {
  basket.set(fruits[right], (basket.get(fruits[right]) || 0) + 1);
  while (basket.size > 2) {
    basket.set(fruits[left], basket.get(fruits[left])! - 1);
    if (basket.get(fruits[left]) === 0) basket.delete(fruits[left]);
    left++;
  }
  maxFruits = Math.max(maxFruits, right - left + 1);
}
```

---

## Problem 8: Longest Substring with At Most K Distinct

### Level 1
Variable window. Contract when map.size > k.

### Level 2
Map tracks character frequencies. When > k distinct, shrink left.

### Level 3
```typescript
const charCount = new Map<string, number>();
let left = 0;
for (let right = 0; right < s.length; right++) {
  charCount.set(s[right], (charCount.get(s[right]) || 0) + 1);
  while (charCount.size > k) {
    charCount.set(s[left], charCount.get(s[left])! - 1);
    if (charCount.get(s[left]) === 0) charCount.delete(s[left]);
    left++;
  }
  maxLen = Math.max(maxLen, right - left + 1);
}
```

---

## Problem 9: Minimum Size Subarray Sum

### Level 1
Expand until sum ≥ target. Contract while maintaining validity.

### Level 2
All positive: greedy shrinking works. Contract while sum ≥ target.

### Level 3
```typescript
let left = 0, sum = 0, minLen = Infinity;
for (let right = 0; right < nums.length; right++) {
  sum += nums[right];
  while (sum >= target) {
    minLen = Math.min(minLen, right - left + 1);
    sum -= nums[left++];
  }
}
return minLen === Infinity ? 0 : minLen;
```

---

## Problem 10: Sliding Window Maximum

### Level 1
Brute force finds max in each window O(nk). Can we avoid recalculating?

### Level 2
Monotonic decreasing deque. Store indices. Front always has maximum.

### Level 3
```typescript
const deque: number[] = []; // indices
for (let i = 0; i < nums.length; i++) {
  // Remove outside window
  while (deque.length && deque[0] <= i - k) deque.shift();
  // Remove smaller elements
  while (deque.length && nums[deque[deque.length - 1]] <= nums[i]) {
    deque.pop();
  }
  deque.push(i);
  if (i >= k - 1) result.push(nums[deque[0]]);
}
```

---

## Pattern Recognition

**Fixed window indicators:**
- "Subarray of size k"
- "Window size k"
- Comparing patterns

**Variable window indicators:**
- "Longest/shortest"
- "With at most/at least"
- "Meeting constraint"

**Use Map when:**
- Need frequencies
- Tracking distinct elements
- Comparing character counts

**Use Set when:**
- Only need presence/absence
- No frequency counting

---

[Back to Problems](./PROBLEMS.md) | [Back to Solutions](./SOLUTIONS.md)
