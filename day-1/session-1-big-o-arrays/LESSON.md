# Lesson: Big O Notation & Arrays

## 📹 Video Assignment (20 minutes)

**Primary Video:**
"Big O Notation - Full Tutorial" by NeetCode
https://www.youtube.com/watch?v=BgLTDT03QtU

**Alternative Videos** (if you need different explanations):
- "Big O Notation" by freeCodeCamp (6 min): https://www.youtube.com/watch?v=v4cd1O4zkGw
- "Data Structures Easy to Advanced" by freeCodeCamp (skip to Big O section, 8 hours total): https://www.youtube.com/watch?v=RBSGKlAvoiM

**What to focus on:**
- Understanding what Big O represents
- Common time complexities and their growth rates
- Space complexity
- How to analyze simple algorithms

---

## 📚 Big O Notation - Core Concepts

### What is Big O?

Big O notation describes how an algorithm's runtime or space requirements grow as the input size increases. It answers: **"How does performance scale?"**

**Key insight:** We care about **worst-case** behavior and **growth rate**, not exact operations.

### The Big O Hierarchy (Fastest to Slowest)

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

**Visual representation of growth:**
```
n=10:   1 < 3 < 10 < 33 < 100 < 1024 < 3,628,800
n=100:  1 < 7 < 100 < 664 < 10,000 < 10³⁰ < 10¹⁵⁷
n=1000: 1 < 10 < 1000 < 9,966 < 1,000,000 < 10³⁰¹ < 10²⁵⁶⁷
```

Notice how exponential and factorial explode!

---

### O(1) - Constant Time

**Definition:** Runtime doesn't change with input size.

**Examples:**
```typescript
// Array access
function getFirst(arr: number[]): number {
  return arr[0];  // Always 1 operation
}

// Hash map lookup
function lookup(map: Map<string, number>, key: string): number | undefined {
  return map.get(key);  // Always ~1 operation
}

// Math operation
function add(a: number, b: number): number {
  return a + b;  // Always 1 operation
}
```

**Interview tip:** Even if you have 10 O(1) operations, it's still O(1). Constants are dropped.

---

### O(log n) - Logarithmic Time

**Definition:** Runtime grows slowly. Doubling input size only adds one more step.

**When it appears:** Dividing problem in half repeatedly (binary search, balanced trees).

**Example - Binary Search:**
```typescript
function binarySearch(arr: number[], target: number): number {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] === target) return mid;
    if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;
  }

  return -1;
}
// Every iteration cuts search space in half
// 1000 elements → only ~10 iterations max
```

**Key insight:** log₂(1000) ≈ 10. That's why binary search is so fast!

---

### O(n) - Linear Time

**Definition:** Runtime grows proportionally with input size.

**When it appears:** Single loop through data.

**Examples:**
```typescript
// Find max in array
function findMax(arr: number[]): number {
  let max = arr[0];
  for (let i = 1; i < arr.length; i++) {  // n iterations
    if (arr[i] > max) max = arr[i];
  }
  return max;
}

// Sum array
function sum(arr: number[]): number {
  return arr.reduce((acc, val) => acc + val, 0);  // O(n)
}
```

**Interview tip:** If you must look at every element at least once, you can't do better than O(n).

---

### O(n log n) - Linearithmic Time

**Definition:** Runtime is n × log n.

**When it appears:** Efficient sorting algorithms.

**Example - Merge Sort:**
```typescript
// TypeScript built-in sort is O(n log n)
arr.sort((a, b) => a - b);
```

**Why n log n?**
- You must touch every element (n)
- But you do it in log n "levels" (divide and conquer)

**Interview tip:** If asked to sort, that's O(n log n). You usually can't sort faster.

---

### O(n²) - Quadratic Time

**Definition:** Runtime grows with square of input size.

**When it appears:** Nested loops over same data.

**Example - Find all pairs:**
```typescript
function findAllPairs(arr: number[]): number[][] {
  const pairs: number[][] = [];

  for (let i = 0; i < arr.length; i++) {       // n iterations
    for (let j = i + 1; j < arr.length; j++) { // n iterations
      pairs.push([arr[i], arr[j]]);
    }
  }

  return pairs;
}
// n × n = n² pairs
```

**Interview tip:** Nested loops often mean O(n²). This is usually what you're trying to optimize away!

---

### O(2ⁿ) - Exponential Time

**Definition:** Runtime doubles with each additional input.

**When it appears:** Brute force recursion, generating all subsets.

**Example - Fibonacci (naive):**
```typescript
function fib(n: number): number {
  if (n <= 1) return n;
  return fib(n - 1) + fib(n - 2);  // 2 recursive calls per level
}
// fib(10) makes 177 calls!
// fib(30) makes 2,692,537 calls!
```

**Interview tip:** If you see exponential complexity, there's usually a DP optimization available.

---

## Space Complexity

Space complexity measures **extra memory** used, not counting the input.

**Examples:**
```typescript
// O(1) space - only a few variables
function sum(arr: number[]): number {
  let total = 0;  // One variable
  for (const num of arr) {
    total += num;
  }
  return total;
}

// O(n) space - creating new array
function double(arr: number[]): number[] {
  return arr.map(x => x * 2);  // New array of size n
}

// O(n) space - recursion call stack
function factorial(n: number): number {
  if (n <= 1) return 1;
  return n * factorial(n - 1);  // n calls on stack
}
```

**Interview tip:** Mention space complexity even if not asked. It shows thoroughness.

---

## Analyzing Algorithms

### Rules for Big O:

1. **Drop constants:**
   - 3n → O(n), not O(3n)
   - n/2 → O(n), not O(n/2)

2. **Drop lower terms:**
   - n² + n → O(n²), not O(n² + n)
   - n log n + n → O(n log n)

3. **Different variables for different inputs:**
   - Two arrays of size n and m → O(n + m) or O(n × m), NOT O(n²)

4. **Amortized complexity:**
   - Dynamic array push is O(1) amortized (even though occasional resize is O(n))

---

## Array Fundamentals

### Why Arrays?

**Strengths:**
- ✅ O(1) access by index
- ✅ Cache-friendly (contiguous memory)
- ✅ Simple and fast
- ✅ Built into every language

**Weaknesses:**
- ❌ O(n) insertion/deletion (except at end)
- ❌ Fixed size (in some languages)
- ❌ O(n) search (unsorted)

---

### Array Operations Complexity

| Operation | Time | Notes |
|-----------|------|-------|
| Access `arr[i]` | O(1) | Direct index |
| Update `arr[i] = x` | O(1) | Direct index |
| Push to end | O(1) | Amortized |
| Pop from end | O(1) | |
| Insert at start | O(n) | Shift all elements |
| Delete at start | O(n) | Shift all elements |
| Search unsorted | O(n) | Must check each |
| Search sorted | O(log n) | Binary search |
| Sort | O(n log n) | Depends on algorithm |

---

### Common Array Patterns

#### 1. Two Pointers (will see in problems)
```typescript
let left = 0;
let right = arr.length - 1;
while (left < right) {
  // Process elements
  // Move pointers based on condition
}
```

#### 2. Sliding Window (next session)
```typescript
let windowSum = 0;
for (let i = 0; i < k; i++) {
  windowSum += arr[i];
}
// Slide window...
```

#### 3. Prefix Sum
```typescript
const prefix: number[] = [arr[0]];
for (let i = 1; i < arr.length; i++) {
  prefix[i] = prefix[i - 1] + arr[i];
}
// Now range sum is O(1)
```

#### 4. Kadane's Algorithm (Maximum Subarray)
```typescript
let maxSum = arr[0];
let currentSum = arr[0];
for (let i = 1; i < arr.length; i++) {
  currentSum = Math.max(arr[i], currentSum + arr[i]);
  maxSum = Math.max(maxSum, currentSum);
}
```

---

## Interview Tips

### How to Analyze Complexity Quickly

1. **Count the loops:**
   - 1 loop → probably O(n)
   - 2 nested loops → probably O(n²)
   - Loop that halves → probably O(log n)

2. **Look for keywords:**
   - "Sorted array" → O(log n) possible (binary search)
   - "All pairs" → O(n²) likely
   - "Recursive" → Could be O(2ⁿ), check tree

3. **Common operations:**
   - Sorting → O(n log n)
   - Hash map operations → O(1)
   - Array access → O(1)
   - Array search → O(n)

### What Interviewers Want to Hear

**Good:**
- "I'll use a hash map for O(1) lookup instead of O(n) array search"
- "This is O(n) time and O(n) space. I'm trading space for time."
- "The brute force is O(n²), but I can optimize to O(n) using..."

**Bad:**
- "I think it's fast" (be specific!)
- Saying O(n) when it's O(n²)
- Not mentioning space complexity

---

## Practice Time!

Now that you understand Big O and arrays, you're ready to solve problems.

**Remember:**
- Start with UMPIRE method
- Think about complexity BEFORE coding
- Consider edge cases (empty, single element, etc.)
- Use TypeScript array methods correctly

**Say:** `"Claude, I watched the video"` when ready for the concept check!

---

## Quick Reference

**Time Complexities (Fastest to Slowest):**
O(1) → O(log n) → O(n) → O(n log n) → O(n²) → O(2ⁿ) → O(n!)

**Space Complexity:**
- In-place algorithm: O(1)
- One extra array: O(n)
- Recursion: O(depth)

**Array Access:** O(1)
**Array Search:** O(n) unsorted, O(log n) sorted
**Array Sort:** O(n log n)

---

[Back to Session README](./README.md)
