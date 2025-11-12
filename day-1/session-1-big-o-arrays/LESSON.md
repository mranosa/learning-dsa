# Lesson: Big O & Arrays

---

## 📹 Video 1: Array Fundamentals (15 min)

**"JavaScript Arrays Crash Course" by freeCodeCamp**
https://www.youtube.com/watch?v=QEZXbRiaY1I

**Focus on:**
- Array creation syntax
- Core methods (push, pop, shift, unshift)
- Iteration methods
- TypeScript typing

---

## 📹 Video 2: Big O Notation (20 min)

**"Big O Notation - Full Tutorial" by NeetCode**
https://www.youtube.com/watch?v=BgLTDT03QtU

**Focus on:**
- Time/space complexity
- Common complexities (O(1) through O(n²))
- How to analyze algorithms

---

## 📹 Video 3: Array Patterns (12 min)

**"5 Simple Steps for Solving Any Recursive Problem" by Reducible**
https://www.youtube.com/watch?v=ngCos392W4w

**Alternative - Two Pointers:**
https://www.youtube.com/watch?v=On03HWe2tZM

**Focus on:**
- Two pointers technique
- Sliding window pattern
- When to use each pattern

---

## 🎯 Arrays: Creation & Syntax

### Creating Arrays

```typescript
// Method 1: Literal syntax (most common)
const nums: number[] = [1, 2, 3, 4, 5];
const names: string[] = ["Alice", "Bob"];

// Method 2: Array constructor
const arr1 = new Array<number>(5);        // [empty × 5]
const arr2 = new Array<number>(1, 2, 3);  // [1, 2, 3]

// Method 3: Array.of()
const arr3 = Array.of(1, 2, 3);           // [1, 2, 3]

// Method 4: Array.from()
const arr4 = Array.from({ length: 5 }, (_, i) => i);  // [0, 1, 2, 3, 4]

// Empty arrays
const empty: number[] = [];
const empty2 = new Array<string>();

// Mixed types (avoid in interviews)
const mixed: (number | string)[] = [1, "two", 3];

// Read-only arrays
const readonly: readonly number[] = [1, 2, 3];
```

---

## 🔧 TypeScript Array Functions

### Core Functions (Must Know)

| Function | Description | Example | Time |
|----------|-------------|---------|------|
| `push(x)` | Add to end | `arr.push(5)` | O(1) |
| `pop()` | Remove from end | `arr.pop()` | O(1) |
| `shift()` | Remove from start | `arr.shift()` | O(n) |
| `unshift(x)` | Add to start | `arr.unshift(0)` | O(n) |
| `length` | Get size | `arr.length` | O(1) |
| `arr[i]` | Access by index | `arr[0]` | O(1) |

```typescript
const arr = [1, 2, 3];
arr.push(4);          // [1, 2, 3, 4]
arr.pop();            // [1, 2, 3], returns 4
arr.unshift(0);       // [0, 1, 2, 3]
arr.shift();          // [1, 2, 3], returns 0
```

---

### Interview Essentials

| Function | Description | Example | Time |
|----------|-------------|---------|------|
| `slice(start, end)` | Copy subarray (non-mutating) | `arr.slice(1, 3)` | O(k) |
| `splice(i, n, ...items)` | Remove/insert (mutates) | `arr.splice(1, 2)` | O(n) |
| `sort(compareFn)` | Sort in-place | `arr.sort((a,b) => a-b)` | O(n log n) |
| `reverse()` | Reverse in-place | `arr.reverse()` | O(n) |
| `includes(x)` | Check existence | `arr.includes(5)` | O(n) |
| `indexOf(x)` | Find index | `arr.indexOf(5)` | O(n) |
| `join(sep)` | Convert to string | `arr.join(",")` | O(n) |
| `concat(arr2)` | Merge arrays | `arr1.concat(arr2)` | O(n+m) |

```typescript
const arr = [3, 1, 4, 1, 5];

// slice - extract portion (doesn't mutate)
arr.slice(1, 4);           // [1, 4, 1]

// splice - remove/insert (mutates!)
arr.splice(2, 1);          // Remove 1 item at index 2
arr.splice(1, 0, 9);       // Insert 9 at index 1

// sort - MUST use comparator for numbers!
arr.sort((a, b) => a - b); // [1, 1, 3, 4, 5] ✅
arr.sort();                 // ["1","1","3","4","5"] ❌ (string sort!)

// reverse
arr.reverse();             // [5, 4, 3, 1, 1]

// includes/indexOf
arr.includes(4);           // true
arr.indexOf(4);            // 2
arr.indexOf(99);           // -1 (not found)
```

---

### Functional Methods (Interview Power Tools)

| Function | Description | Returns | Time |
|----------|-------------|---------|------|
| `map(fn)` | Transform each element | New array | O(n) |
| `filter(fn)` | Keep elements matching condition | New array | O(n) |
| `reduce(fn, init)` | Accumulate to single value | Single value | O(n) |
| `forEach(fn)` | Execute function on each (no return) | undefined | O(n) |
| `find(fn)` | First element matching condition | Element or undefined | O(n) |
| `findIndex(fn)` | Index of first match | Number | O(n) |
| `every(fn)` | All elements match? | Boolean | O(n) |
| `some(fn)` | Any element matches? | Boolean | O(n) |

```typescript
const nums = [1, 2, 3, 4, 5];

// map - transform each element
nums.map(x => x * 2);              // [2, 4, 6, 8, 10]

// filter - keep elements matching condition
nums.filter(x => x % 2 === 0);     // [2, 4]

// reduce - accumulate
nums.reduce((sum, x) => sum + x, 0);  // 15

// forEach - side effects (no return)
nums.forEach(x => console.log(x));

// find - first match
nums.find(x => x > 3);             // 4

// findIndex
nums.findIndex(x => x > 3);        // 3 (index of 4)

// every - all match?
nums.every(x => x > 0);            // true

// some - any match?
nums.some(x => x > 4);             // true
```

---

## 📊 Big O Notation

### What is Big O?

Big O describes how performance scales as input size increases.

**Hierarchy (fastest → slowest):**
```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

**Growth comparison:**
```
n=100:   1 vs 7 vs 100 vs 664 vs 10,000 vs 10³⁰ vs 10¹⁵⁷
```

---

### Common Complexities

| Complexity | Name | Example | When |
|------------|------|---------|------|
| **O(1)** | Constant | Array access `arr[i]` | Fixed operations |
| **O(log n)** | Logarithmic | Binary search | Divide in half |
| **O(n)** | Linear | Single loop | Check each element |
| **O(n log n)** | Linearithmic | Merge sort | Efficient sort |
| **O(n²)** | Quadratic | Nested loops | All pairs |
| **O(2ⁿ)** | Exponential | Fibonacci (naive) | Brute force recursion |

**Examples:**

```typescript
// O(1) - Constant
function getFirst(arr: number[]): number {
  return arr[0];
}

// O(log n) - Logarithmic (binary search)
function binarySearch(arr: number[], target: number): number {
  let left = 0, right = arr.length - 1;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (arr[mid] === target) return mid;
    if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;
  }
  return -1;
}

// O(n) - Linear
function sum(arr: number[]): number {
  let total = 0;
  for (const num of arr) total += num;
  return total;
}

// O(n log n) - Merge sort
arr.sort((a, b) => a - b);

// O(n²) - Quadratic
function allPairs(arr: number[]): number[][] {
  const pairs: number[][] = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      pairs.push([arr[i], arr[j]]);
    }
  }
  return pairs;
}

// O(2ⁿ) - Exponential
function fib(n: number): number {
  if (n <= 1) return n;
  return fib(n - 1) + fib(n - 2);
}
```

---

### Space Complexity

Space complexity measures extra memory used (excluding input).

```typescript
// O(1) space - only variables
function findMax(arr: number[]): number {
  let max = arr[0];
  for (const num of arr) {
    if (num > max) max = num;
  }
  return max;
}

// O(n) space - new array
function double(arr: number[]): number[] {
  return arr.map(x => x * 2);
}

// O(n) space - recursion stack
function factorial(n: number): number {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}
```

---

### Analysis Rules

1. **Drop constants:** 3n → O(n)
2. **Drop lower terms:** n² + n → O(n²)
3. **Different inputs:** Two arrays of size n, m → O(n + m) or O(n × m)
4. **Worst case:** Analyze worst-case scenario

---

## 🎯 Array Operations Complexity

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Access `arr[i]` | O(1) | O(1) | Direct index |
| Update `arr[i] = x` | O(1) | O(1) | Direct index |
| Push (end) | O(1) | O(1) | Amortized |
| Pop (end) | O(1) | O(1) | |
| Shift (start) | O(n) | O(1) | Shifts all elements |
| Unshift (start) | O(n) | O(1) | Shifts all elements |
| Search unsorted | O(n) | O(1) | Must check each |
| Search sorted | O(log n) | O(1) | Binary search |
| Sort | O(n log n) | O(1)-O(n) | Depends on algorithm |
| Slice | O(k) | O(k) | k = slice length |
| Map/Filter | O(n) | O(n) | New array |

---

## 🧩 Common Array Patterns

### Pattern 1: Two Pointers

Used when: Sorted array, finding pairs/triplets, removing duplicates.

```typescript
// Two pointers from ends
function twoSum(arr: number[], target: number): number[] {
  let left = 0, right = arr.length - 1;

  while (left < right) {
    const sum = arr[left] + arr[right];
    if (sum === target) return [left, right];
    if (sum < target) left++;
    else right--;
  }

  return [-1, -1];
}
```

**Time:** O(n) | **Space:** O(1)

---

### Pattern 2: Sliding Window

Used when: Subarray/substring with condition, fixed or variable size window.

```typescript
// Fixed window - max sum of k elements
function maxSum(arr: number[], k: number): number {
  let windowSum = 0;

  // Initial window
  for (let i = 0; i < k; i++) {
    windowSum += arr[i];
  }

  let maxSum = windowSum;

  // Slide window
  for (let i = k; i < arr.length; i++) {
    windowSum += arr[i] - arr[i - k];
    maxSum = Math.max(maxSum, windowSum);
  }

  return maxSum;
}
```

**Time:** O(n) | **Space:** O(1)

---

### Pattern 3: Prefix Sum

Used when: Range queries, subarray sums.

```typescript
// Build prefix sum array
function buildPrefixSum(arr: number[]): number[] {
  const prefix: number[] = [arr[0]];
  for (let i = 1; i < arr.length; i++) {
    prefix[i] = prefix[i - 1] + arr[i];
  }
  return prefix;
}

// Range sum using prefix: O(1)
function rangeSum(prefix: number[], left: number, right: number): number {
  if (left === 0) return prefix[right];
  return prefix[right] - prefix[left - 1];
}
```

**Build:** O(n) | **Query:** O(1) | **Space:** O(n)

---

### Pattern 4: Kadane's Algorithm

Used when: Maximum subarray sum.

```typescript
function maxSubArray(nums: number[]): number {
  let maxSum = nums[0];
  let currentSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    currentSum = Math.max(nums[i], currentSum + nums[i]);
    maxSum = Math.max(maxSum, currentSum);
  }

  return maxSum;
}
```

**Key insight:** At each position, either extend current subarray or start fresh.

**Time:** O(n) | **Space:** O(1)

---

## 💡 Interview Tips

### Complexity Analysis

**Quick rules:**
- 1 loop → O(n)
- Nested loops → O(n²)
- Halving each step → O(log n)
- Sorting → O(n log n)
- Hash map lookup → O(1)

**Say this:**
- "This is O(n) time because we iterate once, O(1) space for variables."
- "I'm trading O(n) space for O(n) time using a hash map instead of O(n²) nested loops."
- "Binary search gives us O(log n) since we halve the search space each iteration."

---

### TypeScript Gotchas

```typescript
// ❌ Wrong - sorts as strings
[1, 10, 2, 20].sort();           // [1, 10, 2, 20]

// ✅ Correct - numeric sort
[1, 10, 2, 20].sort((a, b) => a - b);  // [1, 2, 10, 20]

// ❌ Wrong - mutation without asking
function process(arr: number[]) {
  arr.sort();  // Mutates input!
}

// ✅ Better - copy first
function process(arr: number[]) {
  const sorted = [...arr].sort((a, b) => a - b);
}
```

---

### Common Patterns

| Problem Type | Pattern | Complexity |
|--------------|---------|------------|
| Find pair with sum | Hash map or Two pointers | O(n) |
| Max subarray sum | Kadane's | O(n) |
| Subarray with condition | Sliding window | O(n) |
| Range sum queries | Prefix sum | O(n) build, O(1) query |
| Find in rotated array | Modified binary search | O(log n) |
| All pairs | Nested loops | O(n²) |

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **Array access:** O(1)
- **Array search:** O(n) unsorted, O(log n) sorted
- **Array sort:** O(n log n)
- **Space:** In-place = O(1), new array = O(n)

---

[Back to Session README](./README.md)
