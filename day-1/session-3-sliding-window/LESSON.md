# Lesson: Sliding Window Technique

## 📹 Video Assignment (25 minutes)

**Primary Video:**
"Sliding Window Technique - Algorithmic Mental Models" by NeetCode
https://www.youtube.com/watch?v=GcW4mgmgSbw

**Alternative Videos** (if you need different explanations):
- "Sliding Window Algorithm" by Nick White (15 min): https://www.youtube.com/watch?v=MK-NZ4hN7rs
- "Master Sliding Window" by Tech Dose (20 min): https://www.youtube.com/watch?v=uX0N1PY0uGI

**What to focus on:**
- Fixed-size vs variable-size windows
- When sliding window optimizes from O(n²) to O(n)
- The expand-contract pattern
- Common problem indicators

---

## 📚 Sliding Window - Core Concepts

### What is Sliding Window?

The sliding window technique processes arrays/strings by maintaining a window of elements and sliding it across the data. Instead of recalculating everything from scratch for each position, we update incrementally.

**Key insight:** Convert nested loops into a single pass by maintaining window state.

### Visual Representation

```
Array: [1, 3, 2, 6, -1, 4, 1, 8, 2]
Find max sum of window size 3

Window 1: [1, 3, 2] = 6
Window 2: [3, 2, 6] = 11  (slide right: -1, +6)
Window 3: [2, 6, -1] = 7  (slide right: -3, -1)
...continues...
```

Notice: We don't recalculate the entire sum - we just update!

---

### Fixed-Size Sliding Window

**Definition:** Window size remains constant throughout.

**When to use:**
- Find max/min sum of subarray of size k
- Find average of all subarrays of size k
- Check if pattern of length k exists

**Template:**
```typescript
function fixedSlidingWindow(arr: number[], k: number): number {
  if (arr.length < k) return -1;

  let windowSum = 0;
  let maxSum = 0;

  // Build first window
  for (let i = 0; i < k; i++) {
    windowSum += arr[i];
  }
  maxSum = windowSum;

  // Slide window
  for (let i = k; i < arr.length; i++) {
    windowSum = windowSum - arr[i - k] + arr[i];  // Remove left, add right
    maxSum = Math.max(maxSum, windowSum);
  }

  return maxSum;
}
```

**Complexity:**
- Time: O(n) - single pass
- Space: O(1) - constant variables

---

### Variable-Size Sliding Window

**Definition:** Window expands and contracts based on conditions.

**When to use:**
- Find longest/shortest subarray with property X
- Find all subarrays meeting criteria
- Optimize window size for constraint

**The Expand-Contract Pattern:**
```typescript
function variableSlidingWindow(s: string): number {
  let left = 0;
  let result = 0;
  const window = new Map<string, number>();

  // Expand window with right pointer
  for (let right = 0; right < s.length; right++) {
    // Add s[right] to window
    const char = s[right];
    window.set(char, (window.get(char) || 0) + 1);

    // Contract window while invalid
    while (!isValid(window)) {
      const leftChar = s[left];
      window.set(leftChar, window.get(leftChar)! - 1);
      if (window.get(leftChar) === 0) {
        window.delete(leftChar);
      }
      left++;
    }

    // Update result with valid window
    result = Math.max(result, right - left + 1);
  }

  return result;
}
```

---

### Common Sliding Window Patterns

#### 1. Maximum/Minimum Window
Find the maximum or minimum window satisfying a condition.

**Example:** Longest substring without repeating characters
```typescript
function lengthOfLongestSubstring(s: string): number {
  const seen = new Set<string>();
  let left = 0;
  let maxLength = 0;

  for (let right = 0; right < s.length; right++) {
    // Contract until valid
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

#### 2. Count Windows
Count all windows meeting criteria.

**Example:** Count subarrays with sum k
```typescript
function subarraySum(nums: number[], k: number): number {
  const prefixSums = new Map<number, number>();
  prefixSums.set(0, 1);

  let sum = 0;
  let count = 0;

  for (const num of nums) {
    sum += num;
    // Check if (sum - k) exists
    if (prefixSums.has(sum - k)) {
      count += prefixSums.get(sum - k)!;
    }
    prefixSums.set(sum, (prefixSums.get(sum) || 0) + 1);
  }

  return count;
}
```

#### 3. String Matching
Find substrings with specific character properties.

**Example:** Check if s1's permutation exists in s2
```typescript
function checkInclusion(s1: string, s2: string): boolean {
  if (s1.length > s2.length) return false;

  const s1Count = new Map<string, number>();
  const windowCount = new Map<string, number>();

  // Count s1 characters
  for (const char of s1) {
    s1Count.set(char, (s1Count.get(char) || 0) + 1);
  }

  // Fixed-size window of s1.length
  for (let i = 0; i < s2.length; i++) {
    const char = s2[i];
    windowCount.set(char, (windowCount.get(char) || 0) + 1);

    // Remove leftmost character if window too large
    if (i >= s1.length) {
      const leftChar = s2[i - s1.length];
      if (windowCount.get(leftChar) === 1) {
        windowCount.delete(leftChar);
      } else {
        windowCount.set(leftChar, windowCount.get(leftChar)! - 1);
      }
    }

    // Check if window matches s1
    if (i >= s1.length - 1 && mapsEqual(s1Count, windowCount)) {
      return true;
    }
  }

  return false;
}
```

---

### When to Use Sliding Window

**Problem indicators:**
- "Contiguous subarray/substring"
- "Window", "subarray of size k"
- "Longest/shortest sequence with property X"
- "Maximum/minimum sum of subarray"
- Optimizing from O(n²) brute force

**Not suitable for:**
- Non-contiguous elements
- Problems requiring sorting
- When order doesn't matter

---

### Advanced Techniques

#### 1. Multiple Pointers
Sometimes you need more than just left/right pointers.

```typescript
// Three pointers for special cases
let left = 0, mid = 0, right = 0;
```

#### 2. Window with Data Structure
Use deque for sliding window maximum:

```typescript
class MonotonicDeque {
  private deque: number[] = [];

  push(val: number): void {
    while (this.deque.length && this.deque[this.deque.length - 1] < val) {
      this.deque.pop();
    }
    this.deque.push(val);
  }

  max(): number {
    return this.deque[0];
  }

  pop(val: number): void {
    if (this.deque[0] === val) {
      this.deque.shift();
    }
  }
}
```

#### 3. Two-Pass Sliding Window
Sometimes you need to slide in both directions:

```typescript
// First pass: left to right
const leftMax = new Array(n);
// ... calculate left maximums

// Second pass: right to left
const rightMax = new Array(n);
// ... calculate right maximums

// Combine results
```

---

### Complexity Analysis

**Fixed-size window:**
- Time: O(n) - visit each element once
- Space: O(1) or O(k) depending on what we track

**Variable-size window:**
- Time: O(n) - each element visited at most twice
- Space: O(min(n, k)) where k is alphabet/unique elements

**With sorting:**
- Time: O(n log n) - if we need to sort first
- Space: O(n) - for sorted array

---

### Common Edge Cases

Always handle:
1. Empty input: `[]` or `""`
2. Single element: `[5]` or `"a"`
3. Window size > array length
4. All elements same
5. No valid window exists
6. Multiple valid windows (which to return?)

---

### Interview Tips

1. **Start with brute force** - Show you understand the problem
2. **Identify the optimization** - "I notice we're recalculating..."
3. **Draw the window** - Visual aids help explain
4. **State the pattern** - "This is a variable-size sliding window"
5. **Handle edges first** - Show attention to detail
6. **Optimize space** - Can you avoid the hash map?

---

### Practice Problems by Pattern

**Fixed-size window:**
- Maximum sum subarray of size k
- Find all anagrams in string
- Sliding window maximum

**Variable-size (expand-contract):**
- Longest substring without repeating
- Longest substring with k distinct chars
- Minimum window substring

**Two pointers variation:**
- Container with most water
- Trapping rain water
- Best time to buy/sell stock

---

**Ready to test your knowledge?** The concept check will verify you understand these patterns!