# Solutions: Backtracking

## Problem 1: Subsets

### Solution 1: Backtracking (Include/Exclude)
```typescript
function subsets(nums: number[]): number[][] {
    const result: number[][] = [];

    function backtrack(index: number, path: number[]): void {
        // Base case: processed all elements
        if (index === nums.length) {
            result.push([...path]);
            return;
        }

        // Choice 1: Exclude current element
        backtrack(index + 1, path);

        // Choice 2: Include current element
        path.push(nums[index]);
        backtrack(index + 1, path);
        path.pop();
    }

    backtrack(0, []);
    return result;
}
```
**Time:** O(2^n × n) - 2^n subsets, each takes O(n) to copy
**Space:** O(n) - recursion depth

### Solution 2: Iterative Approach
```typescript
function subsets(nums: number[]): number[][] {
    const result: number[][] = [[]];

    for (const num of nums) {
        const newSubsets: number[][] = [];
        for (const subset of result) {
            newSubsets.push([...subset, num]);
        }
        result.push(...newSubsets);
    }

    return result;
}
```
**Time:** O(2^n × n)
**Space:** O(1) excluding output

### Solution 3: Classic Backtracking Template
```typescript
function subsets(nums: number[]): number[][] {
    const result: number[][] = [];

    function backtrack(start: number, path: number[]): void {
        // Every path is a valid subset
        result.push([...path]);

        // Try adding each remaining element
        for (let i = start; i < nums.length; i++) {
            path.push(nums[i]);
            backtrack(i + 1, path);
            path.pop();
        }
    }

    backtrack(0, []);
    return result;
}
```
**Time:** O(2^n × n)
**Space:** O(n) - recursion depth

---

## Problem 2: Subsets II

### Solution: Backtracking with Duplicate Handling
```typescript
function subsetsWithDup(nums: number[]): number[][] {
    nums.sort((a, b) => a - b); // Sort to group duplicates
    const result: number[][] = [];

    function backtrack(start: number, path: number[]): void {
        result.push([...path]);

        for (let i = start; i < nums.length; i++) {
            // Skip duplicates at the same tree level
            if (i > start && nums[i] === nums[i - 1]) continue;

            path.push(nums[i]);
            backtrack(i + 1, path);
            path.pop();
        }
    }

    backtrack(0, []);
    return result;
}
```
**Time:** O(2^n × n)
**Space:** O(n)

---

## Problem 3: Permutations

### Solution 1: Backtracking with Used Array
```typescript
function permute(nums: number[]): number[][] {
    const result: number[][] = [];
    const used = new Array(nums.length).fill(false);

    function backtrack(path: number[]): void {
        if (path.length === nums.length) {
            result.push([...path]);
            return;
        }

        for (let i = 0; i < nums.length; i++) {
            if (used[i]) continue;

            path.push(nums[i]);
            used[i] = true;
            backtrack(path);
            used[i] = false;
            path.pop();
        }
    }

    backtrack([]);
    return result;
}
```
**Time:** O(n! × n) - n! permutations, each takes O(n) to copy
**Space:** O(n) - recursion depth + used array

### Solution 2: Swap-based Approach
```typescript
function permute(nums: number[]): number[][] {
    const result: number[][] = [];

    function backtrack(first: number): void {
        if (first === nums.length) {
            result.push([...nums]);
            return;
        }

        for (let i = first; i < nums.length; i++) {
            [nums[first], nums[i]] = [nums[i], nums[first]];
            backtrack(first + 1);
            [nums[first], nums[i]] = [nums[i], nums[first]];
        }
    }

    backtrack(0);
    return result;
}
```
**Time:** O(n! × n)
**Space:** O(n) - recursion depth

---

## Problem 4: Permutations II

### Solution: Sort and Skip Duplicates
```typescript
function permuteUnique(nums: number[]): number[][] {
    nums.sort((a, b) => a - b);
    const result: number[][] = [];
    const used = new Array(nums.length).fill(false);

    function backtrack(path: number[]): void {
        if (path.length === nums.length) {
            result.push([...path]);
            return;
        }

        for (let i = 0; i < nums.length; i++) {
            // Skip used elements
            if (used[i]) continue;

            // Skip duplicates: use duplicate only if previous same value was used
            if (i > 0 && nums[i] === nums[i - 1] && !used[i - 1]) continue;

            path.push(nums[i]);
            used[i] = true;
            backtrack(path);
            used[i] = false;
            path.pop();
        }
    }

    backtrack([]);
    return result;
}
```
**Time:** O(n! × n)
**Space:** O(n)

---

## Problem 5: Combination Sum

### Solution: Backtracking with Repeated Use
```typescript
function combinationSum(candidates: number[], target: number): number[][] {
    const result: number[][] = [];

    function backtrack(start: number, path: number[], sum: number): void {
        if (sum === target) {
            result.push([...path]);
            return;
        }

        if (sum > target) return; // Prune

        for (let i = start; i < candidates.length; i++) {
            path.push(candidates[i]);
            // Use i (not i+1) to allow reuse of same element
            backtrack(i, path, sum + candidates[i]);
            path.pop();
        }
    }

    backtrack(0, [], 0);
    return result;
}
```
**Time:** O(n^(target/min) × target) - worst case
**Space:** O(target/min) - max recursion depth

---

## Problem 6: Combination Sum II

### Solution: Single Use with Duplicate Handling
```typescript
function combinationSum2(candidates: number[], target: number): number[][] {
    candidates.sort((a, b) => a - b);
    const result: number[][] = [];

    function backtrack(start: number, path: number[], sum: number): void {
        if (sum === target) {
            result.push([...path]);
            return;
        }

        if (sum > target) return;

        for (let i = start; i < candidates.length; i++) {
            // Skip duplicates at same level
            if (i > start && candidates[i] === candidates[i - 1]) continue;

            path.push(candidates[i]);
            backtrack(i + 1, path, sum + candidates[i]);
            path.pop();
        }
    }

    backtrack(0, [], 0);
    return result;
}
```
**Time:** O(2^n × n)
**Space:** O(n)

---

## Problem 7: Letter Combinations of a Phone Number

### Solution: Backtracking with Multiple Choice Sets
```typescript
function letterCombinations(digits: string): string[] {
    if (digits.length === 0) return [];

    const phone: Map<string, string> = new Map([
        ['2', 'abc'], ['3', 'def'], ['4', 'ghi'],
        ['5', 'jkl'], ['6', 'mno'], ['7', 'pqrs'],
        ['8', 'tuv'], ['9', 'wxyz']
    ]);

    const result: string[] = [];

    function backtrack(index: number, path: string[]): void {
        if (index === digits.length) {
            result.push(path.join(''));
            return;
        }

        const letters = phone.get(digits[index])!;
        for (const letter of letters) {
            path.push(letter);
            backtrack(index + 1, path);
            path.pop();
        }
    }

    backtrack(0, []);
    return result;
}
```
**Time:** O(4^n × n) - worst case (digits 7 or 9)
**Space:** O(n) - recursion depth

---

## Problem 8: Palindrome Partitioning

### Solution: Backtracking with Validation
```typescript
function partition(s: string): string[][] {
    const result: string[][] = [];

    function isPalindrome(str: string, left: number, right: number): boolean {
        while (left < right) {
            if (str[left] !== str[right]) return false;
            left++;
            right--;
        }
        return true;
    }

    function backtrack(start: number, path: string[]): void {
        if (start === s.length) {
            result.push([...path]);
            return;
        }

        for (let end = start; end < s.length; end++) {
            if (isPalindrome(s, start, end)) {
                path.push(s.substring(start, end + 1));
                backtrack(end + 1, path);
                path.pop();
            }
        }
    }

    backtrack(0, []);
    return result;
}
```
**Time:** O(n × 2^n) - 2^n partitions, each checked in O(n)
**Space:** O(n) - recursion depth

---

## Problem 9: Generate Parentheses

### Solution 1: Backtracking with Counting
```typescript
function generateParenthesis(n: number): string[] {
    const result: string[] = [];

    function backtrack(path: string[], open: number, close: number): void {
        if (path.length === 2 * n) {
            result.push(path.join(''));
            return;
        }

        // Add open parenthesis if we haven't used all
        if (open < n) {
            path.push('(');
            backtrack(path, open + 1, close);
            path.pop();
        }

        // Add close parenthesis if it won't make invalid
        if (close < open) {
            path.push(')');
            backtrack(path, open, close + 1);
            path.pop();
        }
    }

    backtrack([], 0, 0);
    return result;
}
```
**Time:** O(4^n / √n) - Catalan number
**Space:** O(n)

### Solution 2: String Building
```typescript
function generateParenthesis(n: number): string[] {
    const result: string[] = [];

    function generate(current: string, open: number, close: number): void {
        if (current.length === 2 * n) {
            result.push(current);
            return;
        }

        if (open < n) {
            generate(current + '(', open + 1, close);
        }

        if (close < open) {
            generate(current + ')', open, close + 1);
        }
    }

    generate('', 0, 0);
    return result;
}
```
**Time:** O(4^n / √n)
**Space:** O(n)

---

## Problem 10: N-Queens

### Solution: Backtracking with Constraint Checking
```typescript
function solveNQueens(n: number): string[][] {
    const result: string[][] = [];
    const board: string[][] = Array(n).fill(null).map(() => Array(n).fill('.'));

    // Track attacked columns and diagonals
    const cols = new Set<number>();
    const diag1 = new Set<number>(); // row - col
    const diag2 = new Set<number>(); // row + col

    function backtrack(row: number): void {
        if (row === n) {
            result.push(board.map(r => r.join('')));
            return;
        }

        for (let col = 0; col < n; col++) {
            // Check if position is under attack
            if (cols.has(col) ||
                diag1.has(row - col) ||
                diag2.has(row + col)) {
                continue;
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
    return result;
}
```
**Time:** O(n!) - n choices first row, at most n-2 second row, etc.
**Space:** O(n) - recursion depth + sets

---

## Key Takeaways

### 1. Template Recognition
- **Subsets:** Start index, all nodes valid
- **Permutations:** Track used, only leaves valid
- **Combinations:** Target/constraint, prune early

### 2. Duplicate Handling
- Always sort first
- Skip at same tree level: `if (i > start && nums[i] === nums[i-1])`

### 3. Optimization Strategies
- Prune invalid branches early
- Use efficient state tracking (sets, arrays)
- Precompute when possible

### 4. Common Pitfalls
- Forgetting to copy when adding to result
- Not properly backtracking (undoing changes)
- Incorrect duplicate handling logic

### 5. Time Complexity Patterns
- Subsets: O(2^n)
- Permutations: O(n!)
- With constraints: Often between O(2^n) and O(n!)