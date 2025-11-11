# Solutions - Session 3: Sliding Window

Comprehensive TypeScript solutions with multiple approaches and complexity analysis.

---

## Problem 1: Best Time to Buy and Sell Stock

### Approach 1: Brute Force (Not Optimal)

```typescript
function maxProfit(prices: number[]): number {
  let maxProfit = 0;

  for (let i = 0; i < prices.length; i++) {
    for (let j = i + 1; j < prices.length; j++) {
      maxProfit = Math.max(maxProfit, prices[j] - prices[i]);
    }
  }

  return maxProfit;
}
```

**Complexity:**
- Time: O(n²) - nested loops
- Space: O(1) - only variables

---

### Approach 2: One Pass (Optimal) ✅

```typescript
function maxProfit(prices: number[]): number {
  if (prices.length === 0) return 0;

  let minPrice = prices[0];
  let maxProfit = 0;

  for (let i = 1; i < prices.length; i++) {
    // Calculate profit if we sell today
    const profit = prices[i] - minPrice;
    maxProfit = Math.max(maxProfit, profit);

    // Update minimum price for future transactions
    minPrice = Math.min(minPrice, prices[i]);
  }

  return maxProfit;
}
```

**Complexity:**
- Time: O(n) - single pass
- Space: O(1) - only two variables

**Key Insight:** This is essentially a sliding window where we track the best buy point (minimum) and calculate profit at each potential sell point.

---

## Problem 2: Longest Substring Without Repeating Characters

### Approach 1: Brute Force with Set

```typescript
function lengthOfLongestSubstring(s: string): number {
  let maxLength = 0;

  for (let i = 0; i < s.length; i++) {
    const seen = new Set<string>();
    let j = i;

    while (j < s.length && !seen.has(s[j])) {
      seen.add(s[j]);
      j++;
    }

    maxLength = Math.max(maxLength, j - i);
  }

  return maxLength;
}
```

**Complexity:**
- Time: O(n²) - nested loops
- Space: O(min(n, m)) where m is alphabet size

---

### Approach 2: Sliding Window with Set (Good)

```typescript
function lengthOfLongestSubstring(s: string): number {
  const seen = new Set<string>();
  let left = 0;
  let maxLength = 0;

  for (let right = 0; right < s.length; right++) {
    // Contract window until no duplicate
    while (seen.has(s[right])) {
      seen.delete(s[left]);
      left++;
    }

    seen.add(s[right]);
    maxLength = Math.max(maxLength, right - left + 1);
  }

  return maxLength;
}
```

**Complexity:**
- Time: O(2n) = O(n) - each character visited at most twice
- Space: O(min(n, m)) - Set size

---

### Approach 3: Optimized with Map (Best) ✅

```typescript
function lengthOfLongestSubstring(s: string): number {
  const lastSeen = new Map<string, number>();
  let left = 0;
  let maxLength = 0;

  for (let right = 0; right < s.length; right++) {
    const char = s[right];

    // Jump left pointer if we've seen this character
    if (lastSeen.has(char) && lastSeen.get(char)! >= left) {
      left = lastSeen.get(char)! + 1;
    }

    lastSeen.set(char, right);
    maxLength = Math.max(maxLength, right - left + 1);
  }

  return maxLength;
}
```

**Complexity:**
- Time: O(n) - single pass, no inner loop
- Space: O(min(n, m)) - Map size

**Key Insight:** Map stores indices so we can jump directly to the right position instead of sliding one by one.

---

## Problem 3: Longest Repeating Character Replacement

### Approach: Sliding Window with Frequency Count ✅

```typescript
function characterReplacement(s: string, k: number): number {
  const count = new Map<string, number>();
  let left = 0;
  let maxFreq = 0;
  let result = 0;

  for (let right = 0; right < s.length; right++) {
    // Update frequency of right character
    const rightChar = s[right];
    count.set(rightChar, (count.get(rightChar) || 0) + 1);

    // Track max frequency in current window
    maxFreq = Math.max(maxFreq, count.get(rightChar)!);

    // Window is invalid if we need more than k replacements
    const windowSize = right - left + 1;
    const replacementsNeeded = windowSize - maxFreq;

    if (replacementsNeeded > k) {
      // Shrink window from left
      const leftChar = s[left];
      count.set(leftChar, count.get(leftChar)! - 1);
      left++;
    }

    result = Math.max(result, right - left + 1);
  }

  return result;
}
```

**Complexity:**
- Time: O(n) - single pass
- Space: O(26) = O(1) - at most 26 uppercase letters

**Key Insight:** We never need to decrease maxFreq when sliding because we only care about windows that could be larger than our current best.

---

## Problem 4: Permutation in String

### Approach 1: Fixed Window with Map Comparison

```typescript
function checkInclusion(s1: string, s2: string): boolean {
  if (s1.length > s2.length) return false;

  const s1Count = new Map<string, number>();
  const windowCount = new Map<string, number>();

  // Count s1 characters
  for (const char of s1) {
    s1Count.set(char, (s1Count.get(char) || 0) + 1);
  }

  // Sliding window of size s1.length
  for (let i = 0; i < s2.length; i++) {
    // Add right character
    const rightChar = s2[i];
    windowCount.set(rightChar, (windowCount.get(rightChar) || 0) + 1);

    // Remove left character if window too large
    if (i >= s1.length) {
      const leftChar = s2[i - s1.length];
      if (windowCount.get(leftChar) === 1) {
        windowCount.delete(leftChar);
      } else {
        windowCount.set(leftChar, windowCount.get(leftChar)! - 1);
      }
    }

    // Check if maps are equal
    if (i >= s1.length - 1 && mapsEqual(s1Count, windowCount)) {
      return true;
    }
  }

  return false;
}

function mapsEqual(map1: Map<string, number>, map2: Map<string, number>): boolean {
  if (map1.size !== map2.size) return false;

  for (const [key, value] of map1) {
    if (map2.get(key) !== value) return false;
  }

  return true;
}
```

**Complexity:**
- Time: O(n × 26) = O(n) where n is s2.length
- Space: O(26) = O(1) - fixed alphabet size

---

### Approach 2: Optimized with Match Count ✅

```typescript
function checkInclusion(s1: string, s2: string): boolean {
  if (s1.length > s2.length) return false;

  const s1Count: number[] = new Array(26).fill(0);
  const windowCount: number[] = new Array(26).fill(0);

  // Count s1 characters
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

    // Add right character
    const rightIdx = s2.charCodeAt(i + s1.length) - 97;
    windowCount[rightIdx]++;
    if (windowCount[rightIdx] === s1Count[rightIdx]) {
      matches++;
    } else if (windowCount[rightIdx] === s1Count[rightIdx] + 1) {
      matches--;
    }

    // Remove left character
    const leftIdx = s2.charCodeAt(i) - 97;
    windowCount[leftIdx]--;
    if (windowCount[leftIdx] === s1Count[leftIdx]) {
      matches++;
    } else if (windowCount[leftIdx] === s1Count[leftIdx] - 1) {
      matches--;
    }
  }

  return matches === 26;
}
```

**Complexity:**
- Time: O(n) - single pass
- Space: O(1) - fixed arrays of size 26

---

## Problem 5: Minimum Window Substring

### Approach: Variable Sliding Window ✅

```typescript
function minWindow(s: string, t: string): string {
  if (s.length < t.length) return "";

  // Count characters in t
  const tCount = new Map<string, number>();
  for (const char of t) {
    tCount.set(char, (tCount.get(char) || 0) + 1);
  }

  const windowCount = new Map<string, number>();
  let have = 0;
  const need = tCount.size;
  let minLen = Infinity;
  let minStart = 0;
  let left = 0;

  for (let right = 0; right < s.length; right++) {
    const char = s[right];
    windowCount.set(char, (windowCount.get(char) || 0) + 1);

    // Check if this character's frequency matches t
    if (tCount.has(char) && windowCount.get(char) === tCount.get(char)) {
      have++;
    }

    // Contract window while valid
    while (have === need) {
      // Update result
      if (right - left + 1 < minLen) {
        minLen = right - left + 1;
        minStart = left;
      }

      // Remove from left
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

**Complexity:**
- Time: O(|s| + |t|) - linear in both strings
- Space: O(|s| + |t|) - for the hash maps

**Key Insight:** Track "have" vs "need" to know when window is valid without comparing maps each time.

---

## Problem 6: Sliding Window Maximum

### Approach 1: Brute Force

```typescript
function maxSlidingWindow(nums: number[], k: number): number[] {
  const result: number[] = [];

  for (let i = 0; i <= nums.length - k; i++) {
    let max = nums[i];
    for (let j = i; j < i + k; j++) {
      max = Math.max(max, nums[j]);
    }
    result.push(max);
  }

  return result;
}
```

**Complexity:**
- Time: O(n × k) - find max for each window
- Space: O(1) - excluding output

---

### Approach 2: Monotonic Deque (Optimal) ✅

```typescript
function maxSlidingWindow(nums: number[], k: number): number[] {
  const result: number[] = [];
  const deque: number[] = []; // stores indices

  for (let i = 0; i < nums.length; i++) {
    // Remove indices outside current window
    while (deque.length && deque[0] <= i - k) {
      deque.shift();
    }

    // Remove indices of smaller elements
    while (deque.length && nums[deque[deque.length - 1]] <= nums[i]) {
      deque.pop();
    }

    deque.push(i);

    // Add to result if window is complete
    if (i >= k - 1) {
      result.push(nums[deque[0]]);
    }
  }

  return result;
}
```

**Complexity:**
- Time: O(n) - each element added and removed at most once
- Space: O(k) - deque size

**Key Insight:** Maintain decreasing monotonic deque - the front always has the maximum for current window.

---

## Problem 7: Maximum Sum of Distinct Subarrays

### Approach: Fixed Sliding Window with Frequency Map ✅

```typescript
function maximumSubarraySum(nums: number[], k: number): number {
  const freq = new Map<number, number>();
  let sum = 0;
  let maxSum = 0;

  // Build initial window
  for (let i = 0; i < k; i++) {
    sum += nums[i];
    freq.set(nums[i], (freq.get(nums[i]) || 0) + 1);
  }

  // Check if all distinct
  if (freq.size === k) {
    maxSum = sum;
  }

  // Slide window
  for (let i = k; i < nums.length; i++) {
    // Add right element
    sum += nums[i];
    freq.set(nums[i], (freq.get(nums[i]) || 0) + 1);

    // Remove left element
    const leftNum = nums[i - k];
    sum -= leftNum;
    if (freq.get(leftNum) === 1) {
      freq.delete(leftNum);
    } else {
      freq.set(leftNum, freq.get(leftNum)! - 1);
    }

    // Update max if all distinct
    if (freq.size === k) {
      maxSum = Math.max(maxSum, sum);
    }
  }

  return maxSum;
}
```

**Complexity:**
- Time: O(n) - single pass
- Space: O(k) - map size at most k

---

## Problem 8: Fruit Into Baskets

### Approach: Variable Sliding Window (At Most 2 Types) ✅

```typescript
function totalFruit(fruits: number[]): number {
  const basket = new Map<number, number>();
  let left = 0;
  let maxFruits = 0;

  for (let right = 0; right < fruits.length; right++) {
    // Add fruit to basket
    basket.set(fruits[right], (basket.get(fruits[right]) || 0) + 1);

    // If more than 2 types, remove from left
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

**Complexity:**
- Time: O(n) - each element visited at most twice
- Space: O(1) - at most 3 fruit types in map

**Key Insight:** This is "longest subarray with at most 2 distinct elements" - classic sliding window pattern.

---

## Problem 9: Longest Substring with At Most K Distinct

### Approach: Variable Sliding Window ✅

```typescript
function lengthOfLongestSubstringKDistinct(s: string, k: number): number {
  if (k === 0) return 0;

  const charCount = new Map<string, number>();
  let left = 0;
  let maxLength = 0;

  for (let right = 0; right < s.length; right++) {
    // Add character to window
    const rightChar = s[right];
    charCount.set(rightChar, (charCount.get(rightChar) || 0) + 1);

    // Contract if too many distinct characters
    while (charCount.size > k) {
      const leftChar = s[left];
      charCount.set(leftChar, charCount.get(leftChar)! - 1);
      if (charCount.get(leftChar) === 0) {
        charCount.delete(leftChar);
      }
      left++;
    }

    maxLength = Math.max(maxLength, right - left + 1);
  }

  return maxLength;
}
```

**Complexity:**
- Time: O(n) - linear pass
- Space: O(k) - at most k+1 distinct characters

---

## Problem 10: Minimum Size Subarray Sum

### Approach 1: Brute Force

```typescript
function minSubArrayLen(target: number, nums: number[]): number {
  let minLen = Infinity;

  for (let i = 0; i < nums.length; i++) {
    let sum = 0;
    for (let j = i; j < nums.length; j++) {
      sum += nums[j];
      if (sum >= target) {
        minLen = Math.min(minLen, j - i + 1);
        break;
      }
    }
  }

  return minLen === Infinity ? 0 : minLen;
}
```

**Complexity:**
- Time: O(n²) - nested loops
- Space: O(1)

---

### Approach 2: Sliding Window (Optimal) ✅

```typescript
function minSubArrayLen(target: number, nums: number[]): number {
  let left = 0;
  let sum = 0;
  let minLen = Infinity;

  for (let right = 0; right < nums.length; right++) {
    sum += nums[right];

    // Contract window while sum >= target
    while (sum >= target) {
      minLen = Math.min(minLen, right - left + 1);
      sum -= nums[left];
      left++;
    }
  }

  return minLen === Infinity ? 0 : minLen;
}
```

**Complexity:**
- Time: O(n) - each element visited at most twice
- Space: O(1) - only variables

**Key Insight:** Since all numbers are positive, we can greedily shrink the window once we reach the target.

---

## Common Patterns Summary

1. **Fixed Window:** Use when window size is given
2. **Variable Window (expand-contract):** Use for optimal window problems
3. **Frequency Counting:** Use Map/array for character counts
4. **Monotonic Deque:** For sliding window min/max
5. **Two Maps:** For comparing window with target pattern