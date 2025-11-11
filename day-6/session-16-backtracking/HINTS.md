# Hints: Backtracking

## Problem 1: Subsets

### Hint 1 (Gentle)
Think about the decision you make for each element in the array. What are your choices?

### Hint 2 (Direct)
For each element, you have two choices: include it in the current subset or exclude it. This forms a binary decision tree.

### Hint 3 (Detailed)
Use recursion with an index parameter. At each index:
1. Add the current path to results (every path is valid)
2. For each remaining element, include it and recurse
3. Remember to backtrack by removing the element after recursion

```typescript
function backtrack(start: number, path: number[]): void {
    result.push([...path]); // Don't forget to copy!
    for (let i = start; i < nums.length; i++) {
        // Include nums[i] and explore
    }
}
```

---

## Problem 2: Subsets II

### Hint 1 (Gentle)
This is similar to Subsets I, but you need to handle duplicates. What preprocessing step helps with duplicate handling?

### Hint 2 (Direct)
Sort the array first. Then, when iterating through choices, skip an element if it's the same as the previous element at the same recursion level.

### Hint 3 (Detailed)
After sorting, use this pattern to skip duplicates:
```typescript
for (let i = start; i < nums.length; i++) {
    if (i > start && nums[i] === nums[i - 1]) continue;
    // This skips duplicates at the same tree level
}
```
The key insight: `i > start` ensures we only skip when we're not at the first choice.

---

## Problem 3: Permutations

### Hint 1 (Gentle)
Unlike subsets, permutations care about order. How do you ensure each element is used exactly once?

### Hint 2 (Direct)
Track which elements have been used with a boolean array or Set. At each position, try all unused elements.

### Hint 3 (Detailed)
Structure your recursion like this:
```typescript
function backtrack(path: number[], used: boolean[]): void {
    if (path.length === nums.length) {
        // Found complete permutation
    }
    for (let i = 0; i < nums.length; i++) {
        if (used[i]) continue;
        // Mark as used, recurse, then unmark
    }
}
```

---

## Problem 4: Permutations II

### Hint 1 (Gentle)
Combine the techniques from Permutations I and Subsets II. What do both problems teach you?

### Hint 2 (Direct)
Sort the array and track used elements. Skip a duplicate only if its previous occurrence hasn't been used yet in the current path.

### Hint 3 (Detailed)
The key condition for skipping:
```typescript
if (i > 0 && nums[i] === nums[i-1] && !used[i-1]) continue;
```
This ensures duplicates are used in order, preventing duplicate permutations.

---

## Problem 5: Combination Sum

### Hint 1 (Gentle)
Each element can be used multiple times. How does this change your recursion compared to regular combinations?

### Hint 2 (Direct)
When you include an element, don't move to the next index. Stay at the same index to allow reuse.

### Hint 3 (Detailed)
```typescript
for (let i = start; i < candidates.length; i++) {
    path.push(candidates[i]);
    // Pass i, not i+1, to allow reuse
    backtrack(i, path, sum + candidates[i]);
    path.pop();
}
```
Don't forget to prune when sum exceeds target!

---

## Problem 6: Combination Sum II

### Hint 1 (Gentle)
This combines single-use elements (like regular combinations) with duplicate handling. What two techniques do you need?

### Hint 2 (Direct)
Sort the array, use each element only once (pass i+1), and skip duplicates at the same recursion level.

### Hint 3 (Detailed)
```typescript
candidates.sort((a, b) => a - b);
for (let i = start; i < candidates.length; i++) {
    if (i > start && candidates[i] === candidates[i-1]) continue;
    // Use i+1 for single use
    backtrack(i + 1, path, sum + candidates[i]);
}
```

---

## Problem 7: Letter Combinations of a Phone Number

### Hint 1 (Gentle)
Each digit maps to multiple letters. How do you handle multiple choice sets at each position?

### Hint 2 (Direct)
Use the index to track which digit you're processing. For each digit, iterate through all its corresponding letters.

### Hint 3 (Detailed)
```typescript
function backtrack(index: number, path: string[]): void {
    if (index === digits.length) {
        // Complete combination
    }
    const letters = phoneMap.get(digits[index]);
    for (const letter of letters) {
        path.push(letter);
        backtrack(index + 1, path);
        path.pop();
    }
}
```

---

## Problem 8: Palindrome Partitioning

### Hint 1 (Gentle)
You need to try all possible ways to partition the string. At each position, what are your choices?

### Hint 2 (Direct)
At position `start`, try taking substrings of length 1, 2, 3... up to the end. Only recurse if the substring is a palindrome.

### Hint 3 (Detailed)
```typescript
for (let end = start; end < s.length; end++) {
    if (isPalindrome(s, start, end)) {
        path.push(s.substring(start, end + 1));
        backtrack(end + 1, path);
        path.pop();
    }
}
```
The key: `end + 1` becomes the new start for the next partition.

---

## Problem 9: Generate Parentheses

### Hint 1 (Gentle)
Valid parentheses have rules: you can't close what you haven't opened. What should you track?

### Hint 2 (Direct)
Track the count of open and close parentheses used. You can add '(' if open < n, and ')' if close < open.

### Hint 3 (Detailed)
```typescript
function backtrack(path: string[], open: number, close: number): void {
    if (path.length === 2 * n) {
        // Valid combination
    }
    if (open < n) {
        path.push('(');
        backtrack(path, open + 1, close);
        path.pop();
    }
    if (close < open) {  // Key condition!
        path.push(')');
        backtrack(path, open, close + 1);
        path.pop();
    }
}
```

---

## Problem 10: N-Queens

### Hint 1 (Gentle)
Process one row at a time. For each row, what do you need to check before placing a queen?

### Hint 2 (Direct)
A queen attacks its column and both diagonals. Track which columns and diagonals are under attack. Diagonals can be identified by row-col and row+col.

### Hint 3 (Detailed)
```typescript
const cols = new Set<number>();
const diag1 = new Set<number>(); // row - col
const diag2 = new Set<number>(); // row + col

function backtrack(row: number): void {
    for (let col = 0; col < n; col++) {
        if (cols.has(col) ||
            diag1.has(row - col) ||
            diag2.has(row + col)) continue;

        // Place queen and update sets
        cols.add(col);
        diag1.add(row - col);
        diag2.add(row + col);

        backtrack(row + 1);

        // Remove queen and update sets
    }
}
```

---

## General Backtracking Tips

### When You're Stuck

1. **Draw the decision tree** - Visualize first 2-3 levels
2. **Identify the choices** - What decisions at each step?
3. **Define the state** - What needs to be tracked?
4. **Find the base case** - When to collect results?
5. **Check your backtracking** - Are you properly undoing changes?

### Common Debugging Steps

1. **Add logging**:
```typescript
console.log(`Level ${depth}: path = ${path}, choices = ${choices}`);
```

2. **Verify copying**:
```typescript
result.push([...path]); // NOT result.push(path)
```

3. **Check bounds**:
```typescript
if (index >= nums.length) return; // Prevent out of bounds
```

### Pattern Matching

- **"All possible"** → Backtracking likely
- **"Subsets/Combinations"** → Start index pattern
- **"Permutations"** → Track used elements
- **"With duplicates"** → Sort and skip
- **"Sum to target"** → Track running sum, prune