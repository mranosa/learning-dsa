# TypeScript for LeetCode - Complete Reference

Everything you need to know about TypeScript for coding interviews.

---

## Table of Contents
1. [Array Methods](#array-methods)
2. [Map (Hash Map)](#map-hash-map)
3. [Set (Hash Set)](#set-hash-set)
4. [String Methods](#string-methods)
5. [Math Operations](#math-operations)
6. [Type Annotations](#type-annotations)
7. [Common Patterns](#common-patterns)
8. [TypeScript Gotchas](#typescript-gotchas)

---

## Array Methods

### Creation
```typescript
// Basic creation
const arr: number[] = [1, 2, 3];
const arr2 = new Array<number>(5).fill(0);        // [0, 0, 0, 0, 0]
const arr3 = Array.from({length: 5}, (_, i) => i); // [0, 1, 2, 3, 4]
const arr4 = [...Array(5)].map((_, i) => i);      // [0, 1, 2, 3, 4]

// 2D array
const matrix: number[][] = Array.from(
  {length: rows},
  () => new Array(cols).fill(0)
);

// Copy array
const copy = [...arr];
const copy2 = arr.slice();
const copy3 = Array.from(arr);
```

### Access
```typescript
arr[0]                    // First element
arr[arr.length - 1]       // Last element
arr.at(-1)                // Last element (ES2022)
arr.at(-2)                // Second to last
```

### Modification
```typescript
// Add/remove from end (O(1))
arr.push(4)               // Add to end, returns new length
arr.pop()                 // Remove from end, returns removed element

// Add/remove from start (O(n) - slow!)
arr.unshift(0)            // Add to start
arr.shift()               // Remove from start

// Remove at index (O(n))
arr.splice(index, 1)      // Remove 1 element at index
arr.splice(index, 0, val) // Insert val at index (doesn't remove)
arr.splice(index, 1, val) // Replace element at index

// Replace element
arr[index] = newValue
```

### Sorting
```typescript
// Sort numbers ascending (IMPORTANT: must provide comparator!)
arr.sort((a, b) => a - b);         // [1, 2, 3, 10, 20]

// Without comparator, sorts as strings!
arr.sort();                         // [1, 10, 2, 20, 3] ❌ WRONG!

// Sort descending
arr.sort((a, b) => b - a);

// Sort strings (default is fine)
arr.sort();                         // Alphabetical

// Sort objects
people.sort((a, b) => a.age - b.age);
points.sort((a, b) => a[0] - b[0]);

// Non-destructive sort (creates copy)
const sorted = [...arr].sort((a, b) => a - b);
```

### Iteration
```typescript
// forEach - no return value
arr.forEach((val, idx, array) => {
  console.log(val, idx);
});

// for...of - modern, clean
for (const val of arr) {
  console.log(val);
}

// for...of with index
for (const [idx, val] of arr.entries()) {
  console.log(idx, val);
}

// Traditional for loop - when you need index
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

// Reverse iteration
for (let i = arr.length - 1; i >= 0; i--) {
  console.log(arr[i]);
}
```

### Transformation
```typescript
// map - transform each element
const doubled = arr.map(x => x * 2);
const strings = arr.map(x => String(x));
const indexed = arr.map((x, i) => [x, i]);

// filter - keep elements that pass test
const evens = arr.filter(x => x % 2 === 0);
const positives = arr.filter(x => x > 0);

// reduce - accumulate into single value
const sum = arr.reduce((acc, cur) => acc + cur, 0);
const max = arr.reduce((acc, cur) => Math.max(acc, cur), -Infinity);
const product = arr.reduce((acc, cur) => acc * cur, 1);

// reduce to object
const freq = arr.reduce((acc, val) => {
  acc[val] = (acc[val] || 0) + 1;
  return acc;
}, {} as Record<number, number>);
```

### Searching
```typescript
// indexOf - first occurrence (-1 if not found)
arr.indexOf(5)            // Index of first 5
arr.indexOf(5, 2)         // Start searching from index 2

// lastIndexOf - last occurrence
arr.lastIndexOf(5)

// includes - boolean check
arr.includes(5)           // true/false

// find - first element that passes test
arr.find(x => x > 5)      // Returns element or undefined

// findIndex - index of first element that passes test
arr.findIndex(x => x > 5) // Returns index or -1

// some - at least one passes test
arr.some(x => x > 5)      // true if any element > 5

// every - all pass test
arr.every(x => x > 0)     // true if all elements > 0
```

### Slicing
```typescript
// slice - returns shallow copy of portion
arr.slice(1, 3)           // Elements at index 1, 2 (not 3)
arr.slice(2)              // From index 2 to end
arr.slice(-2)             // Last 2 elements
arr.slice(0, -1)          // All except last
arr.slice()               // Shallow copy of entire array
```

### Other Useful Methods
```typescript
// reverse - in-place (mutates array!)
arr.reverse()

// join - array to string
arr.join(',')             // "1,2,3"
arr.join(' ')             // "1 2 3"
arr.join('')              // "123"

// concat - merge arrays (returns new array)
arr.concat([4, 5])        // [1, 2, 3, 4, 5]
[...arr1, ...arr2]        // Modern alternative

// flat - flatten nested arrays
[[1, 2], [3, 4]].flat()   // [1, 2, 3, 4]
[1, [2, [3]]].flat(2)     // [1, 2, 3] (depth 2)

// fill - fill with value
new Array(5).fill(0)      // [0, 0, 0, 0, 0]
arr.fill(0, 2, 4)         // Fill indices 2-3 with 0
```

---

## Map (Hash Map)

### Creation
```typescript
// Empty map
const map = new Map<string, number>();
const map2 = new Map<number, number>();

// From entries
const map3 = new Map([
  ['a', 1],
  ['b', 2]
]);

// From object
const map4 = new Map(Object.entries(obj));
```

### Basic Operations
```typescript
// Add/update
map.set('key', value)     // Returns the map (chainable)
map.set('a', 1).set('b', 2);

// Get
map.get('key')            // Returns value or undefined
map.get('key') ?? defaultValue  // With default

// Check existence
map.has('key')            // true/false

// Delete
map.delete('key')         // Returns true if existed, false otherwise

// Clear all
map.clear()

// Size
map.size                  // Number of entries
```

### Iteration
```typescript
// Iterate over entries
for (const [key, val] of map) {
  console.log(key, val);
}

// forEach
map.forEach((val, key) => {
  console.log(key, val);
});

// Keys only
for (const key of map.keys()) {
  console.log(key);
}

// Values only
for (const val of map.values()) {
  console.log(val);
}

// Convert to arrays
Array.from(map.keys())
Array.from(map.values())
Array.from(map.entries())
[...map.keys()]           // Modern alternative
[...map.values()]
[...map]                  // Same as entries
```

### Common Patterns
```typescript
// Frequency counter
const freq = new Map<number, number>();
for (const num of arr) {
  freq.set(num, (freq.get(num) || 0) + 1);
}

// Group by
const groups = new Map<string, number[]>();
for (const item of items) {
  const key = getKey(item);
  if (!groups.has(key)) {
    groups.set(key, []);
  }
  groups.get(key)!.push(item);
}

// Two Sum pattern
const seen = new Map<number, number>();
for (let i = 0; i < nums.length; i++) {
  const complement = target - nums[i];
  if (seen.has(complement)) {
    return [seen.get(complement)!, i];
  }
  seen.set(nums[i], i);
}
```

---

## Set (Hash Set)

### Creation
```typescript
// Empty set
const set = new Set<number>();

// From array
const set2 = new Set([1, 2, 3, 2, 1]); // {1, 2, 3}

// From string (gets unique chars)
const set3 = new Set('hello');          // {'h', 'e', 'l', 'o'}
```

### Basic Operations
```typescript
// Add
set.add(value)            // Returns the set (chainable)
set.add(1).add(2).add(3);

// Check existence
set.has(value)            // true/false

// Delete
set.delete(value)         // Returns true if existed

// Clear all
set.clear()

// Size
set.size                  // Number of elements
```

### Iteration
```typescript
// for...of
for (const val of set) {
  console.log(val);
}

// forEach
set.forEach(val => {
  console.log(val);
});

// Convert to array
Array.from(set)
[...set]                  // Modern alternative
```

### Common Patterns
```typescript
// Remove duplicates from array
const unique = [...new Set(arr)];

// Check if has duplicates
const hasDuplicates = arr.length !== new Set(arr).size;

// Intersection of two arrays
const set1 = new Set(arr1);
const intersection = arr2.filter(x => set1.has(x));

// Union of two arrays
const union = [...new Set([...arr1, ...arr2])];

// Difference (in arr1 but not arr2)
const set2 = new Set(arr2);
const difference = arr1.filter(x => !set2.has(x));

// Contains Duplicate pattern
const seen = new Set<number>();
for (const num of nums) {
  if (seen.has(num)) return true;
  seen.add(num);
}
return false;
```

---

## String Methods

### Access
```typescript
str.length                // Length of string
str[0]                    // Character at index (returns undefined if out of bounds)
str.charAt(0)             // Character at index (returns '' if out of bounds)
str.charCodeAt(0)         // ASCII/Unicode code (returns NaN if out of bounds)
String.fromCharCode(65)   // 'A' (from code)

// at() method (ES2022)
str.at(0)                 // First char
str.at(-1)                // Last char
```

### Substring Extraction
```typescript
// substring(start, end) - doesn't support negative indices
str.substring(0, 3)       // First 3 chars
str.substring(2)          // From index 2 to end

// slice(start, end) - supports negative indices
str.slice(0, 3)           // First 3 chars
str.slice(2)              // From index 2 to end
str.slice(-3)             // Last 3 chars
str.slice(2, -1)          // From index 2 to second-to-last

// substr(start, length) - DEPRECATED, don't use
```

### Case Conversion
```typescript
str.toUpperCase()         // 'HELLO'
str.toLowerCase()         // 'hello'

// For single char
str[0].toUpperCase()      // First char uppercase
```

### Splitting & Joining
```typescript
// Split into array
str.split('')             // ['h', 'e', 'l', 'l', 'o']
str.split(' ')            // Split by space
str.split(',')            // Split by comma
str.split(/\s+/)          // Split by any whitespace (regex)

// Array to string
arr.join('')              // 'hello'
arr.join(' ')             // 'h e l l o'
arr.join(',')             // 'h,e,l,l,o'

// Spread operator (handles Unicode properly)
[...str]                  // ['h', 'e', 'l', 'l', 'o']
```

### Searching
```typescript
// indexOf - first occurrence (-1 if not found)
str.indexOf('l')          // 2
str.indexOf('l', 3)       // Start from index 3

// lastIndexOf - last occurrence
str.lastIndexOf('l')      // 3

// includes - boolean check
str.includes('ell')       // true

// startsWith / endsWith
str.startsWith('he')      // true
str.endsWith('lo')        // true

// search - regex search (returns index or -1)
str.search(/[aeiou]/)     // Index of first vowel
```

### Modification (all return new string)
```typescript
// replace - replaces first occurrence
str.replace('l', 'L')     // 'heLlo'
str.replace(/l/g, 'L')    // 'heLLo' (regex global)

// replaceAll - replaces all (ES2021)
str.replaceAll('l', 'L')  // 'heLLo'

// repeat
str.repeat(3)             // 'hellohellohello'

// trim - remove whitespace
str.trim()                // Remove from both ends
str.trimStart()           // Remove from start
str.trimEnd()             // Remove from end

// pad
str.padStart(10, '0')     // '00000hello'
str.padEnd(10, '0')       // 'hello00000'
```

### Common Patterns
```typescript
// Reverse string
const reversed = [...str].reverse().join('');
const reversed2 = str.split('').reverse().join('');

// Check palindrome
const isPalindrome = str === [...str].reverse().join('');

// Count character frequency
const freq = new Map<string, number>();
for (const char of str) {
  freq.set(char, (freq.get(char) || 0) + 1);
}

// Check if anagram
const sorted1 = [...str1].sort().join('');
const sorted2 = [...str2].sort().join('');
const isAnagram = sorted1 === sorted2;

// Convert string to number
const num = Number(str);
const num2 = parseInt(str, 10);
const num3 = parseFloat(str);
const num4 = +str;            // Unary plus

// Number to string
const str = String(num);
const str2 = num.toString();
const str3 = `${num}`;        // Template literal
```

---

## Math Operations

### Min/Max
```typescript
// Two values
Math.max(a, b)
Math.min(a, b)

// Multiple values
Math.max(1, 2, 3, 4)
Math.min(1, 2, 3, 4)

// Array of values
Math.max(...arr)          // CAUTION: Stack overflow for huge arrays
Math.min(...arr)

// Safe for large arrays
const max = arr.reduce((a, b) => Math.max(a, b), -Infinity);
const min = arr.reduce((a, b) => Math.min(a, b), Infinity);
```

### Rounding
```typescript
Math.floor(3.7)           // 3 (round down)
Math.ceil(3.2)            // 4 (round up)
Math.round(3.5)           // 4 (round to nearest)
Math.round(3.4)           // 3
Math.trunc(3.7)           // 3 (remove decimal, no rounding)

// For negative numbers
Math.floor(-3.2)          // -4 (towards -infinity)
Math.ceil(-3.7)           // -3 (towards +infinity)
Math.trunc(-3.7)          // -3 (towards zero)
```

### Power & Roots
```typescript
Math.pow(2, 3)            // 8 (2^3)
2 ** 3                    // 8 (exponentiation operator, preferred)

Math.sqrt(16)             // 4
Math.cbrt(27)             // 3 (cube root)

// Integer division
Math.floor(a / b)         // Divide and round down
```

### Absolute Value & Sign
```typescript
Math.abs(-5)              // 5
Math.abs(5)               // 5

Math.sign(-5)             // -1
Math.sign(0)              // 0
Math.sign(5)              // 1
```

### Random
```typescript
Math.random()             // [0, 1) random float

// Random integer in range [min, max]
const randomInt = Math.floor(Math.random() * (max - min + 1)) + min;

// Random integer [0, n)
const randomInt = Math.floor(Math.random() * n);
```

### Constants
```typescript
Math.PI                   // 3.141592653589793
Math.E                    // 2.718281828459045
Infinity                  // Positive infinity
-Infinity                 // Negative infinity
```

---

## Type Annotations

### Primitives
```typescript
let num: number = 5;
let str: string = 'hello';
let bool: boolean = true;
let nothing: null = null;
let undef: undefined = undefined;
```

### Arrays
```typescript
let arr: number[] = [1, 2, 3];
let arr2: Array<number> = [1, 2, 3];     // Alternative syntax

let matrix: number[][] = [[1, 2], [3, 4]];
let strs: string[] = ['a', 'b'];
```

### Tuples
```typescript
let pair: [number, number] = [1, 2];
let point: [number, number, string] = [10, 20, 'red'];
```

### Function Types
```typescript
// Function signature
function add(a: number, b: number): number {
  return a + b;
}

// Arrow function
const multiply = (a: number, b: number): number => a * b;

// Optional parameters
function greet(name: string, greeting?: string): string {
  return `${greeting || 'Hello'}, ${name}`;
}

// Default parameters
function greet2(name: string, greeting: string = 'Hello'): string {
  return `${greeting}, ${name}`;
}

// Rest parameters
function sum(...numbers: number[]): number {
  return numbers.reduce((a, b) => a + b, 0);
}

// Void return type
function log(msg: string): void {
  console.log(msg);
}
```

### Objects
```typescript
// Inline type
let person: { name: string; age: number } = {
  name: 'John',
  age: 30
};

// Type alias
type Person = {
  name: string;
  age: number;
  email?: string;  // Optional
};

let person2: Person = { name: 'Jane', age: 25 };

// Interface
interface Point {
  x: number;
  y: number;
}

let point: Point = { x: 10, y: 20 };
```

### Union Types
```typescript
let value: number | string = 5;
value = 'hello';  // OK

function process(input: number | string): string {
  if (typeof input === 'number') {
    return input.toFixed(2);
  } else {
    return input.toUpperCase();
  }
}
```

### Generic Functions (Common in LeetCode)
```typescript
// Generic array function
function findMax<T>(arr: T[], compare: (a: T, b: T) => number): T {
  return arr.reduce((max, curr) => compare(max, curr) > 0 ? max : curr);
}

// Map with generic
const map = new Map<number, string>();

// Set with generic
const set = new Set<number>();

// Array with generic
const arr: Array<number> = [1, 2, 3];
```

### Non-null Assertion
```typescript
// When you know value won't be undefined/null
map.get(key)!             // ! asserts non-null

// Without it, TypeScript complains
const value: number = map.get(key) || 0;  // Safe alternative
```

---

## Common Patterns

### Stack (using Array)
```typescript
const stack: number[] = [];

stack.push(1);            // Push
stack.push(2);
const top = stack[stack.length - 1];  // Peek
const popped = stack.pop();           // Pop

// Check empty
if (stack.length === 0) { }
```

### Queue (using Array - not efficient!)
```typescript
const queue: number[] = [];

queue.push(1);            // Enqueue
queue.push(2);
const front = queue[0];   // Peek
const dequeued = queue.shift();  // Dequeue O(n) ⚠️

// Better: use index pointers for O(1)
let queue2 = [1, 2, 3, 4];
let front = 0;
while (front < queue2.length) {
  const item = queue2[front++];
  // process item
}
```

### Two Pointers
```typescript
// Opposite ends
let left = 0;
let right = arr.length - 1;

while (left < right) {
  if (condition) {
    // Found
    break;
  } else if (needMoveLeft) {
    left++;
  } else {
    right--;
  }
}

// Same direction
let slow = 0;
for (let fast = 0; fast < arr.length; fast++) {
  if (condition) {
    swap(arr, slow, fast);
    slow++;
  }
}
```

### Sliding Window
```typescript
// Fixed size window
let sum = 0;
for (let i = 0; i < k; i++) {
  sum += arr[i];
}
let maxSum = sum;

for (let i = k; i < arr.length; i++) {
  sum = sum - arr[i - k] + arr[i];
  maxSum = Math.max(maxSum, sum);
}

// Variable size window
let left = 0;
let maxLen = 0;
const seen = new Set<number>();

for (let right = 0; right < arr.length; right++) {
  while (seen.has(arr[right])) {
    seen.delete(arr[left]);
    left++;
  }
  seen.add(arr[right]);
  maxLen = Math.max(maxLen, right - left + 1);
}
```

### Swap Elements
```typescript
// Array destructuring
[arr[i], arr[j]] = [arr[j], arr[i]];

// Temporary variable
const temp = arr[i];
arr[i] = arr[j];
arr[j] = temp;
```

### 2D Array Traversal
```typescript
// Row by row
for (let i = 0; i < matrix.length; i++) {
  for (let j = 0; j < matrix[0].length; j++) {
    // matrix[i][j]
  }
}

// All directions (up, right, down, left)
const dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]];
for (const [dr, dc] of dirs) {
  const nr = row + dr;
  const nc = col + dc;
  if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
    // valid neighbor
  }
}

// Diagonals
const dirs = [[-1, -1], [-1, 1], [1, -1], [1, 1]];
```

---

## TypeScript Gotchas

### ⚠️ Array sort() without comparator
```typescript
// WRONG - sorts as strings!
[10, 2, 1].sort();        // [1, 10, 2] ❌

// CORRECT
[10, 2, 1].sort((a, b) => a - b);  // [1, 2, 10] ✅
```

### ⚠️ shift() and unshift() are O(n)
```typescript
// Slow for large arrays
arr.shift();              // O(n)
arr.unshift(val);         // O(n)

// Use push/pop instead (O(1))
arr.push(val);
arr.pop();
```

### ⚠️ Math.max(...hugeArray) can overflow stack
```typescript
// Stack overflow for huge arrays
Math.max(...arr);         // ❌ Can crash

// Use reduce instead
arr.reduce((a, b) => Math.max(a, b), -Infinity);  // ✅
```

### ⚠️ Map vs Object
```typescript
// Object keys are always strings
const obj: Record<number, number> = {};
obj[1] = 100;
obj['1'] = 200;  // Same key! obj[1] is now 200

// Map keys preserve type
const map = new Map<number, number>();
map.set(1, 100);
map.set('1', 200);  // Different keys ✅ (but TypeScript error here)
```

### ⚠️ === vs ==
```typescript
// Always use ===
5 === '5'                 // false ✅
5 == '5'                  // true ❌ (type coercion)

0 === false               // false ✅
0 == false                // true ❌
```

### ⚠️ Checking for -0 vs 0
```typescript
-0 === 0                  // true
Object.is(-0, 0)          // false
Math.abs(-0)              // 0
```

### ⚠️ Array indices out of bounds
```typescript
arr[arr.length]           // undefined (no error!)
arr.at(arr.length)        // undefined (no error!)

// Always check bounds
if (i >= 0 && i < arr.length) {
  // Safe to access arr[i]
}
```

### ⚠️ String methods vs Array methods
```typescript
// Some string methods don't exist on arrays
str.includes('x')         // ✅
arr.includes(x)           // ✅

str.repeat(3)             // ✅
arr.repeat(3)             // ❌ Doesn't exist

// Convert string to array first
[...str].map(c => c.toUpperCase()).join('');
```

---

[Back to README](./README.md)
