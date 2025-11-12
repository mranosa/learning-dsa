# Solutions - Session 3: Sliding Window

TypeScript solutions with complexity analysis.

---

## Problem 1: Best Time to Buy/Sell Stock

### Optimal Solution ✅

```typescript
function maxProfit(prices: number[]): number {
  if (prices.length === 0) return 0;

  let minPrice = prices[0];
  let maxProfit = 0;

  for (let i = 1; i < prices.length; i++) {
    const profit = prices[i] - minPrice;
    maxProfit = Math.max(maxProfit, profit);
    minPrice = Math.min(minPrice, prices[i]);
  }

  return maxProfit;
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** Track minimum price, calculate profit at each sell point.

---

## Problem 2: Longest Substring Without Repeating Characters

### Approach 1: Sliding Window with Set

```typescript
function lengthOfLongestSubstring(s: string): number {
  const seen = new Set<string>();
  let left = 0, maxLen = 0;

  for (let right = 0; right < s.length; right++) {
    while (seen.has(s[right])) {
      seen.delete(s[left]);
      left++;
    }
    seen.add(s[right]);
    maxLen = Math.max(maxLen, right - left + 1);
  }

  return maxLen;
}
```

**Time:** O(n) | **Space:** O(min(n, m))

---

### Approach 2: Optimized with Map ✅

```typescript
function lengthOfLongestSubstring(s: string): number {
  const lastSeen = new Map<string, number>();
  let left = 0, maxLen = 0;

  for (let right = 0; right < s.length; right++) {
    const char = s[right];
    if (lastSeen.has(char) && lastSeen.get(char)! >= left) {
      left = lastSeen.get(char)! + 1;
    }
    lastSeen.set(char, right);
    maxLen = Math.max(maxLen, right - left + 1);
  }

  return maxLen;
}
```

**Time:** O(n) | **Space:** O(min(n, m))

**Key:** Map stores indices to jump directly instead of sliding one-by-one.

---

## Problem 3: Longest Repeating Character Replacement

```typescript
function characterReplacement(s: string, k: number): number {
  const count = new Map<string, number>();
  let left = 0, maxFreq = 0, result = 0;

  for (let right = 0; right < s.length; right++) {
    count.set(s[right], (count.get(s[right]) || 0) + 1);
    maxFreq = Math.max(maxFreq, count.get(s[right])!);

    // Invalid: need more than k replacements
    if (right - left + 1 - maxFreq > k) {
      count.set(s[left], count.get(s[left])! - 1);
      left++;
    }

    result = Math.max(result, right - left + 1);
  }

  return result;
}
```

**Time:** O(n) | **Space:** O(26) = O(1)

**Key:** Don't decrease maxFreq - only care about windows larger than current best.

---

## Problem 4: Permutation in String

### Approach: Match Count with Arrays ✅

```typescript
function checkInclusion(s1: string, s2: string): boolean {
  if (s1.length > s2.length) return false;

  const s1Count = new Array(26).fill(0);
  const windowCount = new Array(26).fill(0);

  // Count s1
  for (let i = 0; i < s1.length; i++) {
    s1Count[s1.charCodeAt(i) - 97]++;
    windowCount[s2.charCodeAt(i) - 97]++;
  }

  let matches = 0;
  for (let i = 0; i < 26; i++) {
    if (s1Count[i] === windowCount[i]) matches++;
  }

  // Slide window
  for (let i = 0; i < s2.length - s1.length; i++) {
    if (matches === 26) return true;

    // Add right
    const rightIdx = s2.charCodeAt(i + s1.length) - 97;
    windowCount[rightIdx]++;
    if (windowCount[rightIdx] === s1Count[rightIdx]) matches++;
    else if (windowCount[rightIdx] === s1Count[rightIdx] + 1) matches--;

    // Remove left
    const leftIdx = s2.charCodeAt(i) - 97;
    windowCount[leftIdx]--;
    if (windowCount[leftIdx] === s1Count[leftIdx]) matches++;
    else if (windowCount[leftIdx] === s1Count[leftIdx] - 1) matches--;
  }

  return matches === 26;
}
```

**Time:** O(n) | **Space:** O(1)

---

## Problem 5: Minimum Window Substring

```typescript
function minWindow(s: string, t: string): string {
  if (s.length < t.length) return "";

  const tCount = new Map<string, number>();
  for (const char of t) {
    tCount.set(char, (tCount.get(char) || 0) + 1);
  }

  const windowCount = new Map<string, number>();
  let have = 0, need = tCount.size;
  let minLen = Infinity, minStart = 0;
  let left = 0;

  for (let right = 0; right < s.length; right++) {
    const char = s[right];
    windowCount.set(char, (windowCount.get(char) || 0) + 1);

    if (tCount.has(char) && windowCount.get(char) === tCount.get(char)) {
      have++;
    }

    while (have === need) {
      if (right - left + 1 < minLen) {
        minLen = right - left + 1;
        minStart = left;
      }

      const leftChar = s[left];
      windowCount.set(leftChar, windowCount.get(leftChar)! - 1);
      if (tCount.has(leftChar) && windowCount.get(leftChar)! < tCount.get(leftChar)!) {
        have--;
      }
      left++;
    }
  }

  return minLen === Infinity ? "" : s.substring(minStart, minStart + minLen);
}
```

**Time:** O(|s| + |t|) | **Space:** O(|s| + |t|)

**Key:** Track "have" vs "need" for efficient validity check.

---

## Problem 6: Maximum Sum of Distinct Subarrays

```typescript
function maximumSubarraySum(nums: number[], k: number): number {
  const freq = new Map<number, number>();
  let sum = 0, maxSum = 0;

  // Build initial window
  for (let i = 0; i < k; i++) {
    sum += nums[i];
    freq.set(nums[i], (freq.get(nums[i]) || 0) + 1);
  }

  if (freq.size === k) maxSum = sum;

  // Slide window
  for (let i = k; i < nums.length; i++) {
    // Add right
    sum += nums[i];
    freq.set(nums[i], (freq.get(nums[i]) || 0) + 1);

    // Remove left
    const leftNum = nums[i - k];
    sum -= leftNum;
    if (freq.get(leftNum) === 1) {
      freq.delete(leftNum);
    } else {
      freq.set(leftNum, freq.get(leftNum)! - 1);
    }

    if (freq.size === k) {
      maxSum = Math.max(maxSum, sum);
    }
  }

  return maxSum;
}
```

**Time:** O(n) | **Space:** O(k)

---

## Problem 7: Fruit Into Baskets

```typescript
function totalFruit(fruits: number[]): number {
  const basket = new Map<number, number>();
  let left = 0, maxFruits = 0;

  for (let right = 0; right < fruits.length; right++) {
    basket.set(fruits[right], (basket.get(fruits[right]) || 0) + 1);

    while (basket.size > 2) {
      const leftFruit = fruits[left];
      basket.set(leftFruit, basket.get(leftFruit)! - 1);
      if (basket.get(leftFruit) === 0) {
        basket.delete(leftFruit);
      }
      left++;
    }

    maxFruits = Math.max(maxFruits, right - left + 1);
  }

  return maxFruits;
}
```

**Time:** O(n) | **Space:** O(1) - at most 3 types

**Key:** "Longest subarray with at most 2 distinct elements".

---

## Problem 8: Longest Substring with At Most K Distinct

```typescript
function lengthOfLongestSubstringKDistinct(s: string, k: number): number {
  if (k === 0) return 0;

  const charCount = new Map<string, number>();
  let left = 0, maxLen = 0;

  for (let right = 0; right < s.length; right++) {
    charCount.set(s[right], (charCount.get(s[right]) || 0) + 1);

    while (charCount.size > k) {
      charCount.set(s[left], charCount.get(s[left])! - 1);
      if (charCount.get(s[left]) === 0) {
        charCount.delete(s[left]);
      }
      left++;
    }

    maxLen = Math.max(maxLen, right - left + 1);
  }

  return maxLen;
}
```

**Time:** O(n) | **Space:** O(k)

---

## Problem 9: Minimum Size Subarray Sum

```typescript
function minSubArrayLen(target: number, nums: number[]): number {
  let left = 0, sum = 0, minLen = Infinity;

  for (let right = 0; right < nums.length; right++) {
    sum += nums[right];

    while (sum >= target) {
      minLen = Math.min(minLen, right - left + 1);
      sum -= nums[left];
      left++;
    }
  }

  return minLen === Infinity ? 0 : minLen;
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** All positive numbers → greedy contraction works.

---

## Problem 10: Sliding Window Maximum

```typescript
function maxSlidingWindow(nums: number[], k: number): number[] {
  const result: number[] = [];
  const deque: number[] = []; // indices

  for (let i = 0; i < nums.length; i++) {
    // Remove indices outside window
    while (deque.length && deque[0] <= i - k) {
      deque.shift();
    }

    // Remove smaller elements
    while (deque.length && nums[deque[deque.length - 1]] <= nums[i]) {
      deque.pop();
    }

    deque.push(i);

    if (i >= k - 1) {
      result.push(nums[deque[0]]);
    }
  }

  return result;
}
```

**Time:** O(n) | **Space:** O(k)

**Key:** Monotonic decreasing deque - front always has maximum.

---

## Pattern Summary

### Fixed Window
- Size k given
- Calculate once, slide
- O(n) time, O(1)-O(k) space

### Variable Window
- Find optimal size
- Expand then contract
- O(n) time, each element visited ≤2 times

### Frequency Counting
- Use Map for character/element counts
- Valid when counts match constraint
- Clean up: delete when count = 0

### Monotonic Deque
- For sliding min/max
- Maintain decreasing/increasing order
- Front has optimal value

---

[Back to Problems](./PROBLEMS.md) | [Back to README](./README.md)
