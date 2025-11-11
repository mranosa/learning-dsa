# Hints: Hash Maps

## Problem 1: Contains Duplicate

### Hint Level 1 (Gentle)
Think about what data structure automatically handles uniqueness for you.

### Hint Level 2 (Direct)
A Set only stores unique values. What happens if you try to add a duplicate?

### Hint Level 3 (Detailed)
```typescript
// Pseudocode approach:
// 1. Create an empty Set
// 2. For each number in the array:
//    - If the number is already in the Set, return true
//    - Otherwise, add it to the Set
// 3. If we finish the loop, return false
```

---

## Problem 2: Valid Anagram

### Hint Level 1 (Gentle)
Anagrams have the same characters with the same frequencies. How can you count character frequencies?

### Hint Level 2 (Direct)
Use a Map to count character frequencies in the first string, then verify the second string matches exactly.

### Hint Level 3 (Detailed)
```typescript
// Pseudocode approach:
// 1. If lengths differ, return false immediately
// 2. Create a Map to count characters in string s
// 3. For each character in string t:
//    - Decrement its count in the Map
//    - If count goes negative or character doesn't exist, return false
// 4. Check if all counts are zero
```

---

## Problem 3: Two Sum

### Hint Level 1 (Gentle)
For each number, you need to find if its complement (target - number) exists. How can you check this efficiently?

### Hint Level 2 (Direct)
Use a Map to store numbers you've seen along with their indices. For each new number, check if its complement exists in the Map.

### Hint Level 3 (Detailed)
```typescript
// Pseudocode approach:
// 1. Create a Map<number, index>
// 2. For each number at index i:
//    - Calculate complement = target - number
//    - If complement exists in Map, return [map.get(complement), i]
//    - Add current number and index to Map
// 3. No solution found (shouldn't happen per problem constraints)
```

---

## Problem 4: Group Anagrams

### Hint Level 1 (Gentle)
Anagrams become identical when sorted. Can you use this property to group them?

### Hint Level 2 (Direct)
Create a Map where the key is the sorted string and the value is an array of original strings that match that sorted form.

### Hint Level 3 (Detailed)
```typescript
// Pseudocode approach:
// 1. Create a Map<sortedString, string[]>
// 2. For each string:
//    - Sort its characters to create a key
//    - If key doesn't exist in Map, create empty array
//    - Add original string to the array for this key
// 3. Return all values from the Map
```

---

## Problem 5: Top K Frequent Elements

### Hint Level 1 (Gentle)
First count frequencies, then you need to find the k most frequent. Think about how to avoid full sorting.

### Hint Level 2 (Direct)
After counting frequencies with a Map, you can use bucket sort since frequencies are bounded by array length.

### Hint Level 3 (Detailed)
```typescript
// Pseudocode approach:
// 1. Count frequencies using Map<number, frequency>
// 2. Create buckets array where index = frequency
// 3. Place each number in its frequency bucket
// 4. Iterate from highest frequency down, collecting k elements
// Note: Frequency can't exceed array length, so bucket sort is O(n)
```

---

## Problem 6: Product of Array Except Self

### Hint Level 1 (Gentle)
The product at index i equals the product of all elements to its left multiplied by the product of all elements to its right.

### Hint Level 2 (Direct)
Build two arrays: leftProducts[i] = product of all elements before i, rightProducts[i] = product of all elements after i.

### Hint Level 3 (Detailed)
```typescript
// Pseudocode approach:
// 1. Create result array
// 2. First pass (left to right):
//    - result[i] = product of all elements before i
// 3. Second pass (right to left):
//    - Maintain running product from right
//    - result[i] *= running product
// This way you use the result array for left products and a variable for right
```

---

## Problem 7: Valid Sudoku

### Hint Level 1 (Gentle)
You need to check three constraints: rows, columns, and 3×3 boxes. How can you track what numbers you've seen in each?

### Hint Level 2 (Direct)
Use 9 Sets for rows, 9 for columns, and 9 for boxes. The tricky part is mapping (row, col) to box index.

### Hint Level 3 (Detailed)
```typescript
// Pseudocode approach:
// 1. Create 9 Sets each for rows, cols, and boxes
// 2. For each cell (r, c):
//    - Skip if empty ('.')
//    - Calculate box index: floor(r/3) * 3 + floor(c/3)
//    - Check if value exists in row[r], col[c], or box[boxIndex]
//    - If duplicate found, return false
//    - Add value to all three sets
// 3. Return true if no duplicates found
```

---

## Problem 8: Encode and Decode Strings

### Hint Level 1 (Gentle)
You need a way to know where one string ends and another begins. What if the delimiter you choose appears in the string?

### Hint Level 2 (Direct)
Prefix each string with its length followed by a delimiter. This way, you know exactly how many characters to read.

### Hint Level 3 (Detailed)
```typescript
// Encode pseudocode:
// For each string: append "length#string"
// Example: ["abc", "de"] becomes "3#abc2#de"

// Decode pseudocode:
// 1. Start at index 0
// 2. Find next '#' to get length
// 3. Read that many characters after '#'
// 4. Move index to after the string
// 5. Repeat until end
```

---

## Problem 9: Longest Consecutive Sequence

### Hint Level 1 (Gentle)
You need O(n) time, so sorting is out. What if you could instantly check if a number exists?

### Hint Level 2 (Direct)
Put all numbers in a Set. For each number, check if it's the start of a sequence (num-1 doesn't exist), then count how long the sequence extends.

### Hint Level 3 (Detailed)
```typescript
// Pseudocode approach:
// 1. Add all numbers to a Set
// 2. For each number in Set:
//    - If (num - 1) exists, skip (not start of sequence)
//    - Otherwise, count consecutive numbers: num, num+1, num+2, ...
//    - Track maximum sequence length
// 3. Each number is visited at most twice (once in loop, once in counting)
```

---

## Problem 10: Subarray Sum Equals K

### Hint Level 1 (Gentle)
If you know the sum from index 0 to i and from 0 to j, can you calculate the sum from i+1 to j?

### Hint Level 2 (Direct)
Use prefix sums. If prefixSum[j] - prefixSum[i] = k, then the subarray from i+1 to j sums to k. Store prefix sum frequencies in a Map.

### Hint Level 3 (Detailed)
```typescript
// Pseudocode approach:
// 1. Initialize: count = 0, currentSum = 0, Map with (0, 1)
// 2. For each number:
//    - Add to currentSum
//    - If (currentSum - k) exists in Map, add its frequency to count
//    - Add/increment currentSum in Map
// 3. Why (0, 1)? For subarrays starting at index 0
// Example: [1, 1, 1], k=2
// - After [1]: sum=1, check for -1 (not found)
// - After [1,1]: sum=2, check for 0 (found! count=1)
// - After [1,1,1]: sum=3, check for 1 (found! count=2)
```

---

## Progressive Difficulty Tips

### Starting Out (Problems 1-3)
- Focus on basic Map/Set operations
- Don't worry about optimization yet
- Draw out the hash map state at each step

### Building Skills (Problems 4-6)
- Start recognizing patterns (grouping, frequency)
- Think about space-time tradeoffs
- Practice explaining your approach out loud

### Advanced Patterns (Problems 7-10)
- Combine multiple hash maps
- Use hash maps with other techniques (prefix sums)
- Focus on optimal solutions

---

## General Hash Map Tips

1. **Always check if key exists before accessing**
   ```typescript
   // Good
   if (map.has(key)) {
       const value = map.get(key)!;
   }

   // Also good
   const value = map.get(key) || defaultValue;
   ```

2. **Initialize counts properly**
   ```typescript
   // For counting
   map.set(key, (map.get(key) || 0) + 1);
   ```

3. **Consider Set when you only need membership**
   ```typescript
   // If you only need to check existence, Set is clearer
   const seen = new Set();
   if (seen.has(value)) { /* ... */ }
   ```

4. **Use Map over Object for non-string keys**
   ```typescript
   // Map handles any key type
   const map = new Map<number, string>();
   map.set(1, "one");

   // Object converts keys to strings
   const obj = {};
   obj[1] = "one"; // Actually obj["1"] = "one"
   ```

5. **Remember Map preserves insertion order**
   ```typescript
   // Useful when order matters
   const map = new Map();
   map.set("c", 3);
   map.set("a", 1);
   map.set("b", 2);
   // Iteration order: c, a, b (not alphabetical)
   ```