# Hints: Backtracking

Progressive hints for 10 problems. Struggling is part of learning - try before looking!

---

## Problem 1: Subsets

### Level 1 (Gentle)
Think about the decision you make for each element in the array. What are your two choices?

### Level 2 (Direct)
For each element, you have two choices: include it in the current subset or exclude it. This forms a binary decision tree. But how do you code it efficiently without generating duplicates like [1,2] and [2,1]?

### Level 3 (Detailed)
Use recursion with a start index parameter. At each index:
1. Add the current path to results (every path is valid)
2. For each remaining element from start to end, include it and recurse
3. Remember to backtrack by removing the element after recursion

```typescript
function backtrack(start: number, path: number[]): void {
    result.push([...path]); // Don't forget to copy!
    for (let i = start; i < nums.length; i++) {
        path.push(nums[i]);
        backtrack(i + 1, path); // i+1 prevents duplicates
        path.pop();
    }
}
```

---

## Problem 2: Subsets II

### Level 1 (Gentle)
This is similar to Subsets I, but you need to handle duplicates. What preprocessing step helps with duplicate handling?

### Level 2 (Direct)
Sort the array first. Then, when iterating through choices at the same recursion level, skip an element if it's the same as the previous element.

### Level 3 (Detailed)
After sorting, use this pattern to skip duplicates:
```typescript
nums.sort((a, b) => a - b);

for (let i = start; i < nums.length; i++) {
    // Skip duplicates at the same tree level
    if (i > start && nums[i] === nums[i - 1]) continue;

    path.push(nums[i]);
    backtrack(i + 1, path);
    path.pop();
}
```

The key insight: `i > start` ensures we only skip when we're not at the first choice at this level.

---

## Problem 3: Permutations

### Level 1 (Gentle)
Unlike subsets, permutations care about order. How do you ensure each element is used exactly once but in all possible positions?

### Level 2 (Direct)
Track which elements have been used with a boolean array or Set. At each position, try all unused elements.

### Level 3 (Detailed)
Structure your recursion like this:
```typescript
function backtrack(path: number[], used: boolean[]): void {
    // Base case: Found complete permutation
    if (path.length === nums.length) {
        result.push([...path]);
        return;
    }

    // Try each element
    for (let i = 0; i < nums.length; i++) {
        if (used[i]) continue; // Skip if already used

        // Make choice
        path.push(nums[i]);
        used[i] = true;

        // Recurse
        backtrack(path, used);

        // Undo choice (backtrack)
        used[i] = false;
        path.pop();
    }
}
```

---

## Problem 4: Permutations II

### Level 1 (Gentle)
Combine the techniques from Permutations I and Subsets II. What do both problems teach you about handling order and duplicates?

### Level 2 (Direct)
Sort the array and track used elements. Skip a duplicate element only if its previous occurrence hasn't been used yet in the current path.

### Level 3 (Detailed)
The key condition for skipping:
```typescript
nums.sort((a, b) => a - b);
const used = new Array(nums.length).fill(false);

for (let i = 0; i < nums.length; i++) {
    if (used[i]) continue;

    // Skip duplicate if previous same value not used
    if (i > 0 && nums[i] === nums[i-1] && !used[i-1]) continue;

    path.push(nums[i]);
    used[i] = true;
    backtrack(path, used);
    used[i] = false;
    path.pop();
}
```

This ensures duplicates are used in order, preventing duplicate permutations.

---

## Problem 5: Combination Sum

### Level 1 (Gentle)
Each element can be used multiple times. How does this change your recursion compared to regular combinations?

### Level 2 (Direct)
When you include an element, don't move to the next index. Stay at the same index to allow reuse of the same element.

### Level 3 (Detailed)
```typescript
function backtrack(start: number, path: number[], sum: number): void {
    // Base case: Found valid combination
    if (sum === target) {
        result.push([...path]);
        return;
    }

    // Pruning: Stop if exceeded target
    if (sum > target) return;

    for (let i = start; i < candidates.length; i++) {
        path.push(candidates[i]);
        // Pass i (not i+1) to allow reuse
        backtrack(i, path, sum + candidates[i]);
        path.pop();
    }
}
```

Don't forget to prune when sum exceeds target!

---

## Problem 6: Combination Sum II

### Level 1 (Gentle)
This combines single-use elements (like regular combinations) with duplicate handling. What two techniques do you need?

### Level 2 (Direct)
Sort the array, use each element only once (pass i+1 in recursion), and skip duplicates at the same recursion level.

### Level 3 (Detailed)
```typescript
candidates.sort((a, b) => a - b);

function backtrack(start: number, path: number[], sum: number): void {
    if (sum === target) {
        result.push([...path]);
        return;
    }

    if (sum > target) return; // Prune

    for (let i = start; i < candidates.length; i++) {
        // Skip duplicates at same level
        if (i > start && candidates[i] === candidates[i-1]) continue;

        path.push(candidates[i]);
        // Use i+1 for single use
        backtrack(i + 1, path, sum + candidates[i]);
        path.pop();
    }
}
```

---

## Problem 7: Letter Combinations of a Phone Number

### Level 1 (Gentle)
Each digit maps to multiple letters. How do you handle multiple choice sets at each position?

### Level 2 (Direct)
Use the index to track which digit you're processing. For each digit, iterate through all its corresponding letters.

### Level 3 (Detailed)
```typescript
const phoneMap = new Map([
    ['2', 'abc'], ['3', 'def'], ['4', 'ghi'],
    ['5', 'jkl'], ['6', 'mno'], ['7', 'pqrs'],
    ['8', 'tuv'], ['9', 'wxyz']
]);

function backtrack(index: number, path: string[]): void {
    // Base case: Built complete combination
    if (index === digits.length) {
        result.push(path.join(''));
        return;
    }

    // Get letters for current digit
    const letters = phoneMap.get(digits[index])!;

    // Try each letter
    for (const letter of letters) {
        path.push(letter);
        backtrack(index + 1, path); // Move to next digit
        path.pop();
    }
}
```

---

## Problem 8: Palindrome Partitioning

### Level 1 (Gentle)
You need to try all possible ways to partition the string. At each position, what are your choices for where to cut?

### Level 2 (Direct)
At position `start`, try taking substrings of length 1, 2, 3... up to the end. Only recurse if the substring is a palindrome.

### Level 3 (Detailed)
```typescript
function isPalindrome(s: string, left: number, right: number): boolean {
    while (left < right) {
        if (s[left] !== s[right]) return false;
        left++;
        right--;
    }
    return true;
}

function backtrack(start: number, path: string[]): void {
    // Base case: Reached end of string
    if (start === s.length) {
        result.push([...path]);
        return;
    }

    // Try all possible partition points
    for (let end = start; end < s.length; end++) {
        // Only recurse if substring is palindrome
        if (isPalindrome(s, start, end)) {
            path.push(s.substring(start, end + 1));
            backtrack(end + 1, path); // Next partition starts at end+1
            path.pop();
        }
    }
}
```

The key: `end + 1` becomes the new start for the next partition.

---

## Problem 9: Generate Parentheses

### Level 1 (Gentle)
Valid parentheses have rules: you can't close what you haven't opened. What state should you track?

### Level 2 (Direct)
Track the count of open '(' and close ')' parentheses used so far. You can add '(' if open < n, and ')' if close < open.

### Level 3 (Detailed)
```typescript
function backtrack(path: string[], open: number, close: number): void {
    // Base case: Built complete string
    if (path.length === 2 * n) {
        result.push(path.join(''));
        return;
    }

    // Can add '(' if we haven't used all n
    if (open < n) {
        path.push('(');
        backtrack(path, open + 1, close);
        path.pop();
    }

    // Can add ')' if it won't make invalid (must have unclosed '(')
    if (close < open) {
        path.push(')');
        backtrack(path, open, close + 1);
        path.pop();
    }
}

backtrack([], 0, 0);
```

The key condition: `close < open` ensures we only add ')' when there's an unclosed '('.

---

## Problem 10: N-Queens

### Level 1 (Gentle)
Process one row at a time. For each row, what do you need to check before placing a queen in a column?

### Level 2 (Direct)
A queen attacks its column and both diagonals. Track which columns and diagonals are under attack. Diagonals can be identified by:
- Main diagonal (↘): All cells have same `row - col`
- Anti-diagonal (↙): All cells have same `row + col`

### Level 3 (Detailed)
```typescript
const board: string[][] = Array(n).fill(null).map(() => Array(n).fill('.'));
const cols = new Set<number>();
const diag1 = new Set<number>(); // row - col
const diag2 = new Set<number>(); // row + col

function backtrack(row: number): void {
    // Base case: Placed all queens
    if (row === n) {
        result.push(board.map(r => r.join('')));
        return;
    }

    // Try each column in current row
    for (let col = 0; col < n; col++) {
        // Check if position is under attack
        if (cols.has(col) ||
            diag1.has(row - col) ||
            diag2.has(row + col)) {
            continue; // Skip invalid position
        }

        // Place queen
        board[row][col] = 'Q';
        cols.add(col);
        diag1.add(row - col);
        diag2.add(row + col);

        // Recurse to next row
        backtrack(row + 1);

        // Remove queen (backtrack)
        board[row][col] = '.';
        cols.delete(col);
        diag1.delete(row - col);
        diag2.delete(row + col);
    }
}

backtrack(0);
```

---

## General Backtracking Tips

### When You're Stuck

1. **Draw the decision tree** - Visualize first 2-3 levels on paper
2. **Identify the choices** - What decisions do you make at each step?
3. **Define the state** - What needs to be tracked and passed down?
4. **Find the base case** - When do you collect/return results?
5. **Check your backtracking** - Are you properly undoing changes?

### Common Debugging Steps

**1. Add logging to see the tree:**
```typescript
function backtrack(depth: number, path: number[]): void {
    console.log('  '.repeat(depth) + `Exploring: [${path}]`);
    // ... rest of logic
}
```

**2. Verify you're copying arrays:**
```typescript
// ❌ Wrong - shares reference
result.push(path);

// ✅ Correct - creates copy
result.push([...path]);
result.push(path.slice());
result.push(Array.from(path));
```

**3. Check backtracking symmetry:**
```typescript
// Every operation must be reversed!
path.push(choice);      // Make choice
used[i] = true;         // Update state
backtrack(/* ... */);   // Recurse
used[i] = false;        // Undo state (MUST match above)
path.pop();             // Undo choice (MUST match above)
```

### Pattern Matching

Look for these keywords to identify the pattern:

- **"All possible"** → Backtracking likely
- **"All subsets/combinations"** → Start index pattern
- **"All permutations"** → Track used elements
- **"Generate valid X"** → Add constraint checks
- **"With duplicates"** → Sort first, skip at same level
- **"Sum to target"** → Track running sum, prune early

### Quick Reference Table

| Pattern | When to Use | Key Technique |
|---------|-------------|---------------|
| **Subsets** | Order doesn't matter | Start index: `backtrack(i+1, ...)` |
| **Permutations** | Order matters | Track used: `if (used[i]) continue` |
| **Combinations** | Fixed size k | Base case: `path.length === k` |
| **Duplicates** | Array has duplicates | Sort + skip: `if (i > start && nums[i] === nums[i-1])` |
| **Target sum** | Sum constraint | Prune: `if (sum > target) return` |
| **String building** | Build character by character | Track counts: `open`, `close` |
| **Constraint satisfaction** | Complex rules | Use Sets for O(1) validation |

---

## Still Stuck?

If you've tried all three hint levels and are still stuck:

1. **Simplify the input** - Try with n=2 or n=3 manually
2. **Draw the tree** - Sketch out the full decision tree for small input
3. **Check the solution** - Sometimes seeing one solution helps understand the pattern
4. **Come back later** - Your brain works on problems in the background

Remember: Struggling is normal and valuable for learning. The "aha!" moment is worth the effort!

---

[Back to Problems](./PROBLEMS.md) | [View Solutions](./SOLUTIONS.md)
