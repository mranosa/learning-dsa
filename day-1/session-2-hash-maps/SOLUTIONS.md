# Solutions - Session 2: Hash Maps

TypeScript solutions with complexity analysis.

---

## Problem 1: Contains Duplicate

### Optimal Solution ✅

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

**Key:** Set automatically handles uniqueness. Early return on duplicate.

**Say:** "Using Set for O(1) membership testing. Single pass through array."

---

## Problem 2: Valid Anagram

### Optimal Solution ✅

```typescript
function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const charCount = new Map<string, number>();

  for (const char of s) {
    charCount.set(char, (charCount.get(char) || 0) + 1);
  }

  for (const char of t) {
    if (!charCount.has(char)) return false;
    const count = charCount.get(char)! - 1;
    if (count < 0) return false;
    charCount.set(char, count);
  }

  return Array.from(charCount.values()).every(c => c === 0);
}
```

**Time:** O(n) | **Space:** O(k) where k = unique characters

**Key:** Count chars in first string, decrement for second. All counts should reach zero.

**Say:** "Frequency counting pattern. Anagrams have identical character frequencies."

---

## Problem 3: Two Sum

### Optimal Solution ✅

```typescript
function twoSum(nums: number[], target: number): number[] {
  const seen = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (seen.has(complement)) {
      return [seen.get(complement)!, i];
    }
    seen.set(nums[i], i);
  }

  return [];
}
```

**Time:** O(n) | **Space:** O(n)

**Key:** Store value→index mapping. Check complement before adding current element.

**Say:** "Trading O(n) space for O(n) time using hash map. Avoids O(n²) nested loops."

---

## Problem 4: Group Anagrams

### Optimal Solution ✅

```typescript
function groupAnagrams(strs: string[]): string[][] {
  const groups = new Map<string, string[]>();

  for (const str of strs) {
    const key = str.split('').sort().join('');

    if (!groups.has(key)) {
      groups.set(key, []);
    }
    groups.get(key)!.push(str);
  }

  return Array.from(groups.values());
}
```

**Time:** O(n × k log k) where n = strings, k = max length | **Space:** O(n × k)

**Key:** Anagrams have identical sorted strings. Use sorted form as Map key.

**Say:** "Canonical form grouping. Sorting creates unique key for each anagram group."

---

## Problem 5: Top K Frequent Elements

### Approach 1: Bucket Sort (Optimal) ✅

```typescript
function topKFrequent(nums: number[], k: number): number[] {
  const freq = new Map<number, number>();

  // Count frequencies
  for (const num of nums) {
    freq.set(num, (freq.get(num) || 0) + 1);
  }

  // Bucket sort: index = frequency
  const buckets: number[][] = Array.from({ length: nums.length + 1 }, () => []);

  for (const [num, count] of freq) {
    buckets[count].push(num);
  }

  // Collect top k from highest frequency
  const result: number[] = [];
  for (let i = buckets.length - 1; i >= 0 && result.length < k; i--) {
    result.push(...buckets[i]);
  }

  return result.slice(0, k);
}
```

**Time:** O(n) | **Space:** O(n)

**Key:** Bucket sort works because frequencies ≤ array length. O(n) beats O(n log n) sorting.

---

## Problem 6: Product of Array Except Self

### Optimal Solution ✅

```typescript
function productExceptSelf(nums: number[]): number[] {
  const n = nums.length;
  const result = new Array(n).fill(1);

  // Build prefix products in result
  for (let i = 1; i < n; i++) {
    result[i] = result[i - 1] * nums[i - 1];
  }

  // Multiply by suffix products on the fly
  let suffixProduct = 1;
  for (let i = n - 1; i >= 0; i--) {
    result[i] *= suffixProduct;
    suffixProduct *= nums[i];
  }

  return result;
}
```

**Time:** O(n) | **Space:** O(1) (excluding output)

**Key:** Product except self = left product × right product. Reuse output array for prefix, calculate suffix on fly.

**Say:** "Two passes: prefix left-to-right, suffix right-to-left. Reusing output achieves O(1) space."

---

## Problem 7: Valid Sudoku

### Optimal Solution ✅

```typescript
function isValidSudoku(board: string[][]): boolean {
  const rows = Array.from({ length: 9 }, () => new Set<string>());
  const cols = Array.from({ length: 9 }, () => new Set<string>());
  const boxes = Array.from({ length: 9 }, () => new Set<string>());

  for (let r = 0; r < 9; r++) {
    for (let c = 0; c < 9; c++) {
      const val = board[r][c];
      if (val === '.') continue;

      const boxIndex = Math.floor(r / 3) * 3 + Math.floor(c / 3);

      if (rows[r].has(val) || cols[c].has(val) || boxes[boxIndex].has(val)) {
        return false;
      }

      rows[r].add(val);
      cols[c].add(val);
      boxes[boxIndex].add(val);
    }
  }

  return true;
}
```

**Time:** O(1) - fixed 81 cells | **Space:** O(1) - fixed size sets

**Key:** Three separate validations with Sets. Box index formula: `Math.floor(r/3) * 3 + Math.floor(c/3)`.

---

## Problem 8: Encode and Decode Strings

### Optimal Solution ✅

```typescript
class Codec {
  encode(strs: string[]): string {
    let encoded = '';
    for (const str of strs) {
      encoded += str.length + '#' + str;
    }
    return encoded;
  }

  decode(s: string): string[] {
    const result: string[] = [];
    let i = 0;

    while (i < s.length) {
      // Find delimiter
      let j = i;
      while (s[j] !== '#') j++;

      // Get length
      const length = parseInt(s.substring(i, j));

      // Extract string
      result.push(s.substring(j + 1, j + 1 + length));

      // Move to next
      i = j + 1 + length;
    }

    return result;
  }
}
```

**Time:** O(n) encode/decode | **Space:** O(1) extra (excluding output)

**Key:** Length prefix format `length#string` prevents delimiter collision. Works with any characters.

---

## Problem 9: Longest Consecutive Sequence

### Optimal Solution ✅

```typescript
function longestConsecutive(nums: number[]): number {
  if (nums.length === 0) return 0;

  const numSet = new Set(nums);
  let maxLength = 0;

  for (const num of numSet) {
    // Only start counting from sequence beginnings
    if (!numSet.has(num - 1)) {
      let currentNum = num;
      let currentLength = 1;

      while (numSet.has(currentNum + 1)) {
        currentNum++;
        currentLength++;
      }

      maxLength = Math.max(maxLength, currentLength);
    }
  }

  return maxLength;
}
```

**Time:** O(n) | **Space:** O(n)

**Key:** Only start counting from sequence starts (num-1 doesn't exist). Each number visited max twice. Set gives O(1) lookups.

**Say:** "Set optimization for O(n) time. Only count sequences from their start to avoid redundant work."

---

## Problem 10: Subarray Sum Equals K

### Optimal Solution ✅

```typescript
function subarraySum(nums: number[], k: number): number {
  let count = 0;
  let sum = 0;
  const sumFreq = new Map<number, number>();
  sumFreq.set(0, 1);  // Empty subarray

  for (const num of nums) {
    sum += num;

    // Check if (sum - k) exists
    if (sumFreq.has(sum - k)) {
      count += sumFreq.get(sum - k)!;
    }

    // Add current sum to map
    sumFreq.set(sum, (sumFreq.get(sum) || 0) + 1);
  }

  return count;
}
```

**Time:** O(n) | **Space:** O(n)

**Key:** If `prefixSum[j] - prefixSum[i] = k`, then subarray [i+1, j] sums to k. Store prefix sum frequencies. Initialize with (0, 1) for subarrays starting at index 0.

**Say:** "Prefix sum with hash map. Looking for sum - k in accumulated prefix sums."

---

## Pattern Summary

### Frequency Counting (Problems 2, 5)
```typescript
const freq = new Map<T, number>();
for (const item of arr) {
  freq.set(item, (freq.get(item) || 0) + 1);
}
```

### Two Sum Pattern (Problems 3, 10)
```typescript
const seen = new Map<number, number>();
for (let i = 0; i < nums.length; i++) {
  const complement = target - nums[i];
  if (seen.has(complement)) {
    // Found pair
  }
  seen.set(nums[i], i);
}
```

### Grouping (Problem 4)
```typescript
const groups = new Map<string, T[]>();
for (const item of items) {
  const key = getKey(item);
  if (!groups.has(key)) groups.set(key, []);
  groups.get(key)!.push(item);
}
```

### Set for Uniqueness (Problems 1, 9)
```typescript
const set = new Set(arr);
if (set.has(target)) { }  // O(1)
```

### Multiple Hash Maps (Problem 7)
```typescript
const maps = Array.from({ length: n }, () => new Map());
// Track different constraints separately
```

---

[Back to Problems](./PROBLEMS.md) | [Back to README](./README.md)
