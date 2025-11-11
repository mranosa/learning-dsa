# Lesson: Backtracking

## 📹 Video Assignment (25 minutes)

**Primary Video:**
"Backtracking Explained - 8 Problems" by NeetCode
https://www.youtube.com/watch?v=pfiQ_PS1g8E

**Alternative Videos** (if you need different explanations):
- "Backtracking Algorithm" by Abdul Bari (20 min): https://www.youtube.com/watch?v=DKCbsiDBN6c
- "Subsets - Backtracking" by NeetCode (12 min): https://www.youtube.com/watch?v=REOH22Xwdkk

**What to focus on:**
- The decision tree mental model
- How backtracking differs from brute force
- The universal template pattern
- When to use backtracking vs other approaches

---

## 📚 Backtracking - Core Concepts

### What is Backtracking?

Backtracking is a systematic way to explore all possible solutions by building them incrementally and abandoning ("backtracking") partial solutions that cannot lead to valid complete solutions.

**Key insight:** Think of it as exploring a decision tree where each node represents a choice, and you explore all paths but can prune invalid branches.

### The Decision Tree Model

```
                    []
           /         |         \
         [1]        [2]        [3]
        /  \       /  \       /  \
    [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
```

Each level represents a decision point. Backtracking explores this tree systematically.

---

### The Universal Backtracking Template

```typescript
function backtrack(
    path: any[],      // Current partial solution
    choices: any[],   // Available choices
    result: any[][]   // All valid solutions
): void {
    // Base case: Found a valid solution
    if (isValidSolution(path)) {
        result.push([...path]); // Important: copy the path!
        return;
    }

    // Explore all choices
    for (let i = 0; i < choices.length; i++) {
        const choice = choices[i];

        // Skip invalid choices (pruning)
        if (!isValidChoice(choice, path)) continue;

        // Make the choice
        path.push(choice);

        // Recursively explore
        backtrack(path, remainingChoices(choices, i), result);

        // Undo the choice (backtrack)
        path.pop();
    }
}
```

---

## Pattern 1: Subsets (Combinations without Constraint)

### Concept
Generate all possible subsets of a set. Each element has two choices: include or exclude.

### Template
```typescript
function subsets(nums: number[]): number[][] {
    const result: number[][] = [];

    function backtrack(start: number, path: number[]): void {
        // Every path is a valid subset
        result.push([...path]);

        // Try including each remaining element
        for (let i = start; i < nums.length; i++) {
            path.push(nums[i]);
            backtrack(i + 1, path);  // Move to next index
            path.pop();
        }
    }

    backtrack(0, []);
    return result;
}
```

### Decision Tree for [1,2,3]
```
                     []
            /         |         \
          [1]        [2]        [3]
         /   \        |
      [1,2] [1,3]   [2,3]
        |
     [1,2,3]
```

---

## Pattern 2: Permutations (All Arrangements)

### Concept
Generate all possible arrangements where order matters. Each position can have any unused element.

### Template
```typescript
function permute(nums: number[]): number[][] {
    const result: number[][] = [];

    function backtrack(path: number[], used: Set<number>): void {
        // Found a complete permutation
        if (path.length === nums.length) {
            result.push([...path]);
            return;
        }

        // Try each unused number
        for (const num of nums) {
            if (used.has(num)) continue;

            path.push(num);
            used.add(num);
            backtrack(path, used);
            used.delete(num);
            path.pop();
        }
    }

    backtrack([], new Set());
    return result;
}
```

---

## Pattern 3: Combinations (Selections with Constraints)

### Concept
Select k elements from n choices. Like subsets but with a fixed size.

### Template
```typescript
function combine(n: number, k: number): number[][] {
    const result: number[][] = [];

    function backtrack(start: number, path: number[]): void {
        // Found a valid combination
        if (path.length === k) {
            result.push([...path]);
            return;
        }

        // Optimization: not enough elements left
        if (path.length + (n - start + 1) < k) return;

        for (let i = start; i <= n; i++) {
            path.push(i);
            backtrack(i + 1, path);
            path.pop();
        }
    }

    backtrack(1, []);
    return result;
}
```

---

## Pattern 4: Handling Duplicates

### Key Technique
Sort the input and skip duplicates at the same decision level.

```typescript
function subsetsWithDup(nums: number[]): number[][] {
    nums.sort((a, b) => a - b); // Sort first!
    const result: number[][] = [];

    function backtrack(start: number, path: number[]): void {
        result.push([...path]);

        for (let i = start; i < nums.length; i++) {
            // Skip duplicates at the same level
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

---

## Pattern 5: Constraint Satisfaction (N-Queens)

### Concept
Place elements with constraints that must be checked at each step.

### Template Structure
```typescript
function solveNQueens(n: number): string[][] {
    const result: string[][] = [];
    const board: string[][] = Array(n).fill(null)
        .map(() => Array(n).fill('.'));

    function isValid(row: number, col: number): boolean {
        // Check column
        for (let i = 0; i < row; i++) {
            if (board[i][col] === 'Q') return false;
        }

        // Check diagonals
        for (let i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] === 'Q') return false;
        }
        for (let i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] === 'Q') return false;
        }

        return true;
    }

    function backtrack(row: number): void {
        if (row === n) {
            result.push(board.map(r => r.join('')));
            return;
        }

        for (let col = 0; col < n; col++) {
            if (!isValid(row, col)) continue;

            board[row][col] = 'Q';
            backtrack(row + 1);
            board[row][col] = '.';
        }
    }

    backtrack(0);
    return result;
}
```

---

## Time Complexity Analysis

### General Formula
Time = (Number of nodes in decision tree) × (Work per node)

### Common Patterns
- **Subsets:** O(2ⁿ × n) - Each element: include/exclude
- **Permutations:** O(n! × n) - n choices, then n-1, then n-2...
- **Combinations C(n,k):** O(C(n,k) × k)
- **N-Queens:** O(n!) - n choices first row, at most n-1 second...

### Space Complexity
Usually O(n) for recursion depth + O(result size) for storing solutions.

---

## Optimization Techniques

### 1. Early Pruning
Stop exploring branches that can't lead to valid solutions:
```typescript
// In combination sum with target
if (currentSum > target) return; // Prune this branch
```

### 2. Preprocessing
Sort input to enable pruning and handle duplicates:
```typescript
nums.sort((a, b) => a - b);
// Now can skip duplicates and prune more effectively
```

### 3. State Optimization
Use bit manipulation or arrays instead of Sets when possible:
```typescript
// Instead of Set<number> for used elements
const used = new Array(n).fill(false);
```

---

## Common Interview Patterns

### Pattern Recognition
1. **"All possible"** → Backtracking
2. **"Combinations/Subsets"** → Start index pattern
3. **"Permutations"** → Used set pattern
4. **"Generate valid"** → Constraint checking
5. **"Partition"** → Try all split points

### Edge Cases to Consider
- Empty input
- Single element
- All duplicates
- No valid solution exists
- Multiple valid solutions

---

## Debugging Tips

### 1. Print the Decision Tree
```typescript
function backtrack(depth: number, path: number[]): void {
    console.log('  '.repeat(depth) + path);
    // ... rest of logic
}
```

### 2. Track State Changes
```typescript
console.log(`Choose: ${choice}, Path: ${path}`);
// ... make choice and recurse
console.log(`Unchoose: ${choice}, Path: ${path}`);
```

### 3. Verify Base Cases
Always check:
- Are you copying the result?
- Is the base case correct?
- Are you properly backtracking?

---

## Practice Strategy

1. **Start with Subsets** - Simplest pattern
2. **Then Permutations** - Adds complexity
3. **Handle duplicates** - Common variation
4. **Add constraints** - Combination sum, N-Queens
5. **Optimize** - Practice pruning techniques

Remember: The key is recognizing when to use backtracking and adapting the template to each problem's specific requirements.