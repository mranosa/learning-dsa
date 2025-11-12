# Hints - Session 2: Hash Maps

Progressive hints for 10 problems. Struggle first, learn deeper.

---

## Problem 1: Contains Duplicate

### Level 1
What data structure automatically handles uniqueness?

### Level 2
Set stores only unique values. If add fails, duplicate found.

### Level 3
```typescript
const seen = new Set();
for (const num of nums) {
  if (seen.has(num)) return true;
  seen.add(num);
}
return false;
```

---

## Problem 2: Valid Anagram

### Level 1
Anagrams have same characters with same frequencies. How to count?

### Level 2
Use Map to count chars in first string. Decrement counts for second string. All should reach zero.

### Level 3
```typescript
if (s.length !== t.length) return false;
const charCount = new Map();
for (const char of s) {
  charCount.set(char, (charCount.get(char) || 0) + 1);
}
for (const char of t) {
  if (!charCount.has(char)) return false;
  charCount.set(char, charCount.get(char) - 1);
}
// Check all counts are 0
```

---

## Problem 3: Two Sum

### Level 1
For each number, need to find if complement exists. What gives O(1) lookup?

### Level 2
Hash map stores value→index. For each num, check if `(target - num)` exists in map.

### Level 3
```typescript
const seen = new Map();
for (let i = 0; i < nums.length; i++) {
  const complement = target - nums[i];
  if (seen.has(complement)) {
    return [seen.get(complement), i];
  }
  seen.set(nums[i], i);
}
```

---

## Problem 4: Group Anagrams

### Level 1
Anagrams become identical when sorted. Use this as grouping key?

### Level 2
Map with sorted string as key. Each key holds array of original strings.

### Level 3
```typescript
const groups = new Map();
for (const str of strs) {
  const key = str.split('').sort().join('');
  if (!groups.has(key)) groups.set(key, []);
  groups.get(key).push(str);
}
return Array.from(groups.values());
```

---

## Problem 5: Top K Frequent Elements

### Level 1
Count frequencies first. How to find top k without full sorting?

### Level 2
Bucket sort. Index = frequency, value = array of numbers with that frequency.

### Level 3
```typescript
// Count frequencies
const freq = new Map();
for (const num of nums) {
  freq.set(num, (freq.get(num) || 0) + 1);
}

// Bucket sort
const buckets = Array.from({ length: nums.length + 1 }, () => []);
for (const [num, count] of freq) {
  buckets[count].push(num);
}

// Collect top k from highest
const result = [];
for (let i = buckets.length - 1; i >= 0 && result.length < k; i--) {
  result.push(...buckets[i]);
}
```

---

## Problem 6: Product of Array Except Self

### Level 1
Product at i = product of all left × product of all right.

### Level 2
Build prefix products left-to-right in result array. Then multiply by suffix products right-to-left using variable.

### Level 3
```typescript
const result = new Array(n).fill(1);
// Prefix
for (let i = 1; i < n; i++) {
  result[i] = result[i - 1] * nums[i - 1];
}
// Suffix
let suffix = 1;
for (let i = n - 1; i >= 0; i--) {
  result[i] *= suffix;
  suffix *= nums[i];
}
```

---

## Problem 7: Valid Sudoku

### Level 1
Need to check three constraints: rows, columns, 3×3 boxes. How to track seen numbers?

### Level 2
9 Sets for rows, 9 for cols, 9 for boxes. Box index: `Math.floor(r/3) * 3 + Math.floor(c/3)`.

### Level 3
```typescript
const rows = Array.from({ length: 9 }, () => new Set());
const cols = Array.from({ length: 9 }, () => new Set());
const boxes = Array.from({ length: 9 }, () => new Set());

for (let r = 0; r < 9; r++) {
  for (let c = 0; c < 9; c++) {
    if (board[r][c] === '.') continue;
    const val = board[r][c];
    const boxIdx = Math.floor(r/3) * 3 + Math.floor(c/3);

    if (rows[r].has(val) || cols[c].has(val) || boxes[boxIdx].has(val)) {
      return false;
    }

    rows[r].add(val);
    cols[c].add(val);
    boxes[boxIdx].add(val);
  }
}
```

---

## Problem 8: Encode and Decode Strings

### Level 1
Need delimiter, but what if delimiter appears in string?

### Level 2
Prefix each string with its length: `length#string`. Know exactly how many chars to read.

### Level 3
```typescript
encode(strs: string[]): string {
  let result = '';
  for (const str of strs) {
    result += str.length + '#' + str;
  }
  return result;
}

decode(s: string): string[] {
  const result = [];
  let i = 0;
  while (i < s.length) {
    let j = i;
    while (s[j] !== '#') j++;
    const length = parseInt(s.substring(i, j));
    result.push(s.substring(j + 1, j + 1 + length));
    i = j + 1 + length;
  }
  return result;
}
```

---

## Problem 9: Longest Consecutive Sequence

### Level 1
Need O(n) time, so no sorting. What gives O(1) membership check?

### Level 2
Put all in Set. For each number, check if it's sequence start (num-1 doesn't exist). Then count upward.

### Level 3
```typescript
const numSet = new Set(nums);
let maxLength = 0;

for (const num of numSet) {
  // Only start from sequence beginnings
  if (!numSet.has(num - 1)) {
    let current = num;
    let length = 1;

    while (numSet.has(current + 1)) {
      current++;
      length++;
    }

    maxLength = Math.max(maxLength, length);
  }
}
```

---

## Problem 10: Subarray Sum Equals K

### Level 1
If know sum from 0 to i and 0 to j, can calculate sum from i+1 to j?

### Level 2
Prefix sum. If `prefixSum[j] - prefixSum[i] = k`, then subarray [i+1,j] sums to k. Store prefix sum frequencies in Map.

### Level 3
```typescript
let count = 0;
let sum = 0;
const sumFreq = new Map();
sumFreq.set(0, 1);  // Empty subarray

for (const num of nums) {
  sum += num;

  // Check if (sum - k) exists
  if (sumFreq.has(sum - k)) {
    count += sumFreq.get(sum - k);
  }

  sumFreq.set(sum, (sumFreq.get(sum) || 0) + 1);
}
```

---

## Pattern Hints

**"Find duplicate"** → Set for O(1) membership

**"Count frequencies"** → `map.set(key, (map.get(key) || 0) + 1)`

**"Find pair with sum"** → Two Sum pattern with hash map

**"Group by property"** → Map with property as key

**"Check existence"** → Set for O(1) vs array O(n)

---

## Using Hints Effectively

1. Try 15+ min before Level 1
2. Try 10+ min after each hint
3. If use Level 3, review and redo tomorrow
4. Hints are learning tools, not cheating

Goal: Learn pattern recognition, not memorize solutions.

---

[Back to Problems](./PROBLEMS.md) | [Back to Solutions](./SOLUTIONS.md)
