# Solutions: Hash Maps

## Problem 1: Contains Duplicate

### Approach 1: Using Set (Optimal)
```typescript
function containsDuplicate(nums: number[]): boolean {
    const seen = new Set<number>();

    for (let num of nums) {
        if (seen.has(num)) {
            return true;
        }
        seen.add(num);
    }

    return false;
}
```

**Time Complexity:** O(n) - iterate through array once
**Space Complexity:** O(n) - Set can contain up to n elements

### Approach 2: One-liner with Set
```typescript
function containsDuplicate(nums: number[]): boolean {
    return new Set(nums).size !== nums.length;
}
```

**Time Complexity:** O(n) - creating Set from array
**Space Complexity:** O(n) - Set storage

### Approach 3: Sorting (No extra space for duplicates)
```typescript
function containsDuplicate(nums: number[]): boolean {
    nums.sort((a, b) => a - b);

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] === nums[i - 1]) {
            return true;
        }
    }

    return false;
}
```

**Time Complexity:** O(n log n) - dominated by sorting
**Space Complexity:** O(1) - sorting in place (ignoring sort's internal space)

### Key Insights
- Set automatically handles uniqueness
- Early return optimization when duplicate found
- Trading time for space with the Set approach

---

## Problem 2: Valid Anagram

### Approach 1: Character Frequency Map (Optimal)
```typescript
function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false;

    const charCount = new Map<string, number>();

    // Count characters in s
    for (let char of s) {
        charCount.set(char, (charCount.get(char) || 0) + 1);
    }

    // Decrement for characters in t
    for (let char of t) {
        if (!charCount.has(char)) return false;

        const count = charCount.get(char)! - 1;
        if (count < 0) return false;

        if (count === 0) {
            charCount.delete(char);
        } else {
            charCount.set(char, count);
        }
    }

    return charCount.size === 0;
}
```

**Time Complexity:** O(n) where n is string length
**Space Complexity:** O(k) where k is unique characters (at most 26 for lowercase)

### Approach 2: Sorting
```typescript
function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false;

    return s.split('').sort().join('') === t.split('').sort().join('');
}
```

**Time Complexity:** O(n log n) - dominated by sorting
**Space Complexity:** O(n) - arrays for sorting

### Approach 3: Array for ASCII (Fixed Space)
```typescript
function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false;

    const counts = new Array(26).fill(0);

    for (let i = 0; i < s.length; i++) {
        counts[s.charCodeAt(i) - 97]++;
        counts[t.charCodeAt(i) - 97]--;
    }

    return counts.every(count => count === 0);
}
```

**Time Complexity:** O(n)
**Space Complexity:** O(1) - fixed size array of 26

### Key Insights
- Early termination on length mismatch
- Character frequency is the key pattern
- Array approach works well for limited character set

---

## Problem 3: Two Sum

### Approach 1: Hash Map One Pass (Optimal)
```typescript
function twoSum(nums: number[], target: number): number[] {
    const numToIndex = new Map<number, number>();

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];

        if (numToIndex.has(complement)) {
            return [numToIndex.get(complement)!, i];
        }

        numToIndex.set(nums[i], i);
    }

    return []; // Should never reach here given problem constraints
}
```

**Time Complexity:** O(n) - single pass
**Space Complexity:** O(n) - hash map storage

### Approach 2: Brute Force
```typescript
function twoSum(nums: number[], target: number): number[] {
    for (let i = 0; i < nums.length - 1; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                return [i, j];
            }
        }
    }

    return [];
}
```

**Time Complexity:** O(n²) - nested loops
**Space Complexity:** O(1) - no extra storage

### Key Insights
- Store value->index mapping as we iterate
- Check for complement before storing current element
- One pass is sufficient with hash map

---

## Problem 4: Group Anagrams

### Approach 1: Sorted String as Key (Most Intuitive)
```typescript
function groupAnagrams(strs: string[]): string[][] {
    const groups = new Map<string, string[]>();

    for (let str of strs) {
        const key = str.split('').sort().join('');

        if (!groups.has(key)) {
            groups.set(key, []);
        }
        groups.get(key)!.push(str);
    }

    return Array.from(groups.values());
}
```

**Time Complexity:** O(n * k log k) where n = number of strings, k = max string length
**Space Complexity:** O(n * k) - storing all strings in groups

### Approach 2: Character Count as Key (Optimal)
```typescript
function groupAnagrams(strs: string[]): string[][] {
    const groups = new Map<string, string[]>();

    for (let str of strs) {
        const count = new Array(26).fill(0);

        for (let char of str) {
            count[char.charCodeAt(0) - 97]++;
        }

        const key = count.join('#');

        if (!groups.has(key)) {
            groups.set(key, []);
        }
        groups.get(key)!.push(str);
    }

    return Array.from(groups.values());
}
```

**Time Complexity:** O(n * k) where n = number of strings, k = max string length
**Space Complexity:** O(n * k)

### Key Insights
- Anagrams have identical sorted strings
- Character frequency can be used as unique key
- Map groups strings by their canonical form

---

## Problem 5: Top K Frequent Elements

### Approach 1: Frequency Map + Sort (Simple)
```typescript
function topKFrequent(nums: number[], k: number): number[] {
    const freq = new Map<number, number>();

    // Count frequencies
    for (let num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    // Sort by frequency
    const sorted = Array.from(freq.entries())
        .sort((a, b) => b[1] - a[1]);

    // Return top k
    return sorted.slice(0, k).map(entry => entry[0]);
}
```

**Time Complexity:** O(n log n) - sorting dominates
**Space Complexity:** O(n) - frequency map

### Approach 2: Bucket Sort (Optimal)
```typescript
function topKFrequent(nums: number[], k: number): number[] {
    const freq = new Map<number, number>();

    // Count frequencies
    for (let num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    // Create buckets where index = frequency
    const buckets: number[][] = new Array(nums.length + 1)
        .fill(null)
        .map(() => []);

    for (let [num, count] of freq) {
        buckets[count].push(num);
    }

    // Collect top k from highest frequency buckets
    const result: number[] = [];
    for (let i = buckets.length - 1; i >= 0 && result.length < k; i--) {
        result.push(...buckets[i]);
    }

    return result.slice(0, k);
}
```

**Time Complexity:** O(n) - linear bucket sort
**Space Complexity:** O(n) - buckets array

### Key Insights
- Bucket sort works because frequencies are bounded by array length
- No need for full sorting, just top k
- Frequency map is essential first step

---

## Problem 6: Product of Array Except Self

### Approach 1: Left and Right Products (Two Arrays)
```typescript
function productExceptSelf(nums: number[]): number[] {
    const n = nums.length;
    const left = new Array(n).fill(1);
    const right = new Array(n).fill(1);
    const result = new Array(n);

    // Calculate left products
    for (let i = 1; i < n; i++) {
        left[i] = left[i - 1] * nums[i - 1];
    }

    // Calculate right products
    for (let i = n - 2; i >= 0; i--) {
        right[i] = right[i + 1] * nums[i + 1];
    }

    // Combine
    for (let i = 0; i < n; i++) {
        result[i] = left[i] * right[i];
    }

    return result;
}
```

**Time Complexity:** O(n) - three passes
**Space Complexity:** O(n) - left and right arrays

### Approach 2: Space Optimized (O(1) Extra Space)
```typescript
function productExceptSelf(nums: number[]): number[] {
    const n = nums.length;
    const result = new Array(n).fill(1);

    // Calculate left products in result array
    for (let i = 1; i < n; i++) {
        result[i] = result[i - 1] * nums[i - 1];
    }

    // Calculate right products on the fly
    let rightProduct = 1;
    for (let i = n - 1; i >= 0; i--) {
        result[i] *= rightProduct;
        rightProduct *= nums[i];
    }

    return result;
}
```

**Time Complexity:** O(n) - two passes
**Space Complexity:** O(1) - output array doesn't count

### Key Insights
- Product except self = left product × right product
- Can reuse output array to store intermediate results
- Right product can be calculated on the fly

---

## Problem 7: Valid Sudoku

### Approach: Three Sets per Index
```typescript
function isValidSudoku(board: string[][]): boolean {
    const rows = new Array(9).fill(null).map(() => new Set<string>());
    const cols = new Array(9).fill(null).map(() => new Set<string>());
    const boxes = new Array(9).fill(null).map(() => new Set<string>());

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

**Time Complexity:** O(1) - fixed 81 cells
**Space Complexity:** O(1) - fixed size sets

### Key Insights
- Track seen numbers for each row, column, and 3×3 box
- Box index formula: `Math.floor(r/3) * 3 + Math.floor(c/3)`
- Early return on duplicate detection

---

## Problem 8: Encode and Decode Strings

### Approach: Length Prefix Encoding
```typescript
class Codec {
    encode(strs: string[]): string {
        let encoded = '';

        for (let str of strs) {
            encoded += str.length + '#' + str;
        }

        return encoded;
    }

    decode(s: string): string[] {
        const result: string[] = [];
        let i = 0;

        while (i < s.length) {
            // Find the delimiter
            let j = i;
            while (s[j] !== '#') {
                j++;
            }

            // Get the length
            const length = parseInt(s.substring(i, j));

            // Extract the string
            result.push(s.substring(j + 1, j + 1 + length));

            // Move to next string
            i = j + 1 + length;
        }

        return result;
    }
}
```

**Time Complexity:** O(n) for both encode and decode
**Space Complexity:** O(1) extra space (not counting output)

### Key Insights
- Length prefix prevents delimiter collision
- Format: `length#string` for each string
- Works with any character including the delimiter itself

---

## Problem 9: Longest Consecutive Sequence

### Approach: HashSet with Sequence Start Detection
```typescript
function longestConsecutive(nums: number[]): number {
    if (nums.length === 0) return 0;

    const numSet = new Set(nums);
    let maxLength = 0;

    for (let num of numSet) {
        // Check if this is the start of a sequence
        if (!numSet.has(num - 1)) {
            let currentNum = num;
            let currentLength = 1;

            // Count consecutive numbers
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

**Time Complexity:** O(n) - each number visited at most twice
**Space Complexity:** O(n) - HashSet storage

### Key Insights
- Only start counting from sequence beginnings
- Set provides O(1) lookups for consecutive checking
- Avoids counting same sequence multiple times

---

## Problem 10: Subarray Sum Equals K

### Approach: Prefix Sum with Hash Map
```typescript
function subarraySum(nums: number[], k: number): number {
    let count = 0;
    let sum = 0;
    const sumFreq = new Map<number, number>();
    sumFreq.set(0, 1); // Empty subarray

    for (let num of nums) {
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

**Time Complexity:** O(n) - single pass
**Space Complexity:** O(n) - hash map for prefix sums

### Key Insights
- If `prefixSum[j] - prefixSum[i] = k`, then subarray [i+1, j] sums to k
- Store frequency of prefix sums seen so far
- Initialize with (0, 1) for subarrays starting at index 0

---

## Common Patterns Summary

1. **Frequency Counting:** Problems 2, 5
   - Use Map to count occurrences
   - Often combined with sorting or bucketing

2. **Two Sum Pattern:** Problems 3, 10
   - Store complements/differences in hash map
   - Check for existence before adding current

3. **Grouping/Categorizing:** Problem 4
   - Use canonical form as key (sorted string, frequency array)
   - Map groups elements with same property

4. **Set for Uniqueness:** Problems 1, 9
   - O(1) membership testing
   - Automatic duplicate handling

5. **Multiple Hash Maps:** Problem 7
   - Track different constraints separately
   - Combine checks for validation

6. **Prefix Techniques:** Problems 6, 10
   - Build cumulative information
   - Use for range queries/calculations