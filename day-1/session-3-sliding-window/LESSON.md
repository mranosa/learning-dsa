# Lesson: Sliding Window

---

## 📹 Video 1: Sliding Window Fundamentals (10 min)

**"Sliding Window Technique - Algorithmic Mental Models" by NeetCode**
https://www.youtube.com/watch?v=GcW4mgmgSbw

**Focus on:**
- What is sliding window
- When it optimizes O(n²) to O(n)
- Fixed vs variable windows
- Problem indicators

---

## 📹 Video 2: Fixed vs Variable Windows (12 min)

**"Sliding Window Algorithm" by Nick White**
https://www.youtube.com/watch?v=MK-NZ4hN7rs

**Focus on:**
- Fixed-size window template
- Variable-size expand-contract
- Common mistakes
- Edge cases

---

## 📹 Video 3: Advanced Patterns (13 min)

**"Master Sliding Window" by Tech Dose**
https://www.youtube.com/watch?v=uX0N1PY0uGI

**Focus on:**
- Frequency counting with Map
- Multiple constraints
- Monotonic deque
- String matching patterns

---

## 🎯 What is Sliding Window?

Process arrays/strings by maintaining a window of elements and sliding it across data.

**Key insight:** Update incrementally instead of recalculating from scratch.

```
Array: [1, 3, 2, 6, -1, 4, 1, 8, 2]
Find max sum of window size 3

[1, 3, 2] = 6
   [3, 2, 6] = 11  (slide: -1, +6)
      [2, 6, -1] = 7  (slide: -3, -1)
```

**Optimization:** O(n²) → O(n)

---

## 🔧 Fixed-Size Window

### Template

```typescript
function fixedWindow(arr: number[], k: number): number {
  if (arr.length < k) return -1;

  let windowSum = 0;

  // Build first window
  for (let i = 0; i < k; i++) {
    windowSum += arr[i];
  }
  let maxSum = windowSum;

  // Slide window
  for (let i = k; i < arr.length; i++) {
    windowSum = windowSum - arr[i - k] + arr[i];
    maxSum = Math.max(maxSum, windowSum);
  }

  return maxSum;
}
```

**Time:** O(n) | **Space:** O(1)

### When to Use
- Max/min sum of subarray size k
- Find pattern of length k
- Average of subarrays size k

---

## 🔧 Variable-Size Window

### Expand-Contract Template

```typescript
function variableWindow(s: string): number {
  let left = 0;
  let result = 0;
  const window = new Map<string, number>();

  for (let right = 0; right < s.length; right++) {
    // 1. Expand: Add to window
    const char = s[right];
    window.set(char, (window.get(char) || 0) + 1);

    // 2. Contract: Shrink while invalid
    while (!isValid(window)) {
      const leftChar = s[left];
      window.set(leftChar, window.get(leftChar)! - 1);
      if (window.get(leftChar) === 0) {
        window.delete(leftChar);
      }
      left++;
    }

    // 3. Update result
    result = Math.max(result, right - left + 1);
  }

  return result;
}
```

**Time:** O(n) - each element visited ≤2 times | **Space:** O(k)

### When to Use
- Longest/shortest subarray with property X
- All subarrays meeting criteria
- Optimize window size for constraint

---

## 🧩 Common Patterns

### Pattern 1: Maximum/Minimum Window

```typescript
// Longest substring without repeating
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

### Pattern 2: String Matching

```typescript
// Permutation in string (fixed window)
function checkInclusion(s1: string, s2: string): boolean {
  if (s1.length > s2.length) return false;

  const s1Count: number[] = new Array(26).fill(0);
  const windowCount: number[] = new Array(26).fill(0);

  // Count s1
  for (let i = 0; i < s1.length; i++) {
    s1Count[s1.charCodeAt(i) - 97]++;
    windowCount[s2.charCodeAt(i) - 97]++;
  }

  let matches = 0;
  for (let i = 0; i < 26; i++) {
    if (s1Count[i] === windowCount[i]) matches++;
  }

  // Slide
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

### Pattern 3: Frequency Counting

```typescript
// Longest repeating character replacement
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

---

### Pattern 4: Monotonic Deque

```typescript
// Sliding window maximum
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

---

## 📊 Complexity Analysis

| Window Type | Time | Space | Notes |
|------------|------|-------|-------|
| Fixed-size | O(n) | O(1)-O(k) | Visit each once |
| Variable-size | O(n) | O(min(n,k)) | Each visited ≤2 times |
| With deque | O(n) | O(k) | Monotonic structure |
| With sorting | O(n log n) | O(n) | Rare for windows |

---

## 🎯 When to Use Sliding Window

**Problem indicators:**
- "Contiguous subarray/substring"
- "Window", "subarray of size k"
- "Longest/shortest sequence with property X"
- "Maximum/minimum sum of subarray"
- Can optimize from O(n²) brute force

**Not suitable:**
- Non-contiguous elements
- Need sorting
- Order doesn't matter

---

## 💡 Interview Tips

### Recognition
**Look for:**
- Array/string input
- "Contiguous" or "subarray/substring"
- "Longest/shortest/maximum/minimum"
- Optimization opportunity

**Ask:**
- Fixed or variable window size?
- What makes a window valid?
- What are we optimizing for?

### Communication
**Say:**
- "This is a [fixed/variable]-size sliding window"
- "Expanding window to meet constraint, contracting to find minimum"
- "Using Map to track frequencies in current window"
- "Optimizing from O(n²) brute force to O(n) single pass"

### TypeScript Gotchas

```typescript
// ❌ Wrong - doesn't handle 0 count
const window = new Map<string, number>();
window.set(char, window.get(char) + 1); // NaN if not present

// ✅ Correct
window.set(char, (window.get(char) || 0) + 1);

// ❌ Wrong - leaves entry with 0
window.set(char, window.get(char)! - 1);

// ✅ Better - clean up
window.set(char, window.get(char)! - 1);
if (window.get(char) === 0) {
  window.delete(char);
}
```

---

## 📋 Edge Cases

Always handle:
1. Empty input: `[]` or `""`
2. Single element
3. Window size k > array length
4. All elements same
5. No valid window exists
6. k = 0 or k = array.length

---

## 🎓 Practice Strategy

1. **Identify pattern** - Fixed or variable?
2. **Draw it out** - Visualize window movement
3. **Start brute force** - Show understanding
4. **Optimize** - Apply sliding window
5. **Track state** - Use right data structure
6. **Handle edges** - Check all cases

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **Fixed window:** Size k given → calculate once, slide
- **Variable window:** Find optimal size → expand then contract
- **Key:** Update incrementally, don't recalculate

---

[Back to Session README](./README.md)
