# Lesson: Backtracking

---

## 📹 Video 1: Backtracking Fundamentals (25 min)

**"Backtracking - 8 Essential Problems" by NeetCode**
https://www.youtube.com/watch?v=pfiQ_PS1g8E

**Focus on:**
- What is backtracking and when to use it
- The decision tree mental model
- Universal backtracking template
- Difference from brute force and DP

**Alternative - Comprehensive Introduction:**
"Backtracking Algorithm" by Abdul Bari (20 min)
https://www.youtube.com/watch?v=DKCbsiDBN6c

---

## 📹 Video 2: Decision Trees & State Space (15 min)

**"Subsets - Backtracking" by NeetCode**
https://www.youtube.com/watch?v=REOH22Xwdkk

**Focus on:**
- Visualizing the decision tree
- Include/exclude pattern for subsets
- State space exploration
- When to collect results

**Alternative - Detailed Explanation:**
"Permutations - Backtracking" by NeetCode (7 min)
https://www.youtube.com/watch?v=s7AvT7cGdSo

---

## 📹 Video 3: Advanced Patterns (10 min)

**"Combination Sum - Backtracking" by NeetCode**
https://www.youtube.com/watch?v=GBKI9VSKdGg

**Focus on:**
- Pruning invalid branches
- Handling duplicates with sorting
- Constraint satisfaction problems
- Optimization techniques

---

## 🎯 What is Backtracking?

### Core Concept

Backtracking is a systematic way to explore all possible solutions by:
1. **Making a choice** (add to current state)
2. **Exploring** that choice recursively
3. **Undoing the choice** (backtrack) to try other options

**Key insight:** Think of it as exploring a decision tree where each node represents a choice, and you explore all paths while pruning invalid branches.

### When to Use Backtracking

Use backtracking when you see:
- **"All possible"** solutions/combinations
- **"Generate all"** permutations/subsets
- **Constraint satisfaction** (N-Queens, Sudoku)
- **Combinatorial problems** with choices at each step
- **No overlapping subproblems** (else use DP)

### Backtracking vs Other Approaches

| Approach | When to Use | Example |
|----------|-------------|---------|
| **Backtracking** | All solutions, no overlap | Subsets, Permutations |
| **Dynamic Programming** | Optimal solution, overlapping | Fibonacci, LCS |
| **Greedy** | Local optimum leads to global | Dijkstra, Activity Selection |
| **Brute Force** | Small input, simple logic | Check all pairs |

---

## 🌳 The Decision Tree Model

### Visualizing Backtracking

Every backtracking problem has an implicit decision tree:

```
Example: Subsets of [1,2,3]

                        []
                /                 \
            Include 1           Exclude 1
              [1]                  []
           /      \             /      \
      Include 2  Exclude 2  Include 2  Exclude 2
        [1,2]      [1]        [2]        []
       /    \     /   \      /   \      /   \
      ...   ...  ...  ...   ...  ...   ...  ...
```

**At each node:** Decide to include or exclude the current element.
**Leaf nodes:** Complete solutions (all elements considered).

### Tree Traversal Pattern

```typescript
// DFS traversal of the decision tree
function explore(node) {
    if (isLeaf(node)) {
        collectSolution(node);
        return;
    }

    for (child of children(node)) {
        if (isValid(child)) {  // Pruning!
            explore(child);
        }
    }
}
```

---

## 📋 The Universal Backtracking Template

### Standard Template

```typescript
function backtrack(
    state: any[],       // Current partial solution
    choices: any[],     // Available choices
    result: any[][]     // All valid solutions
): void {
    // Base case: Found a valid solution
    if (isValidSolution(state)) {
        result.push([...state]); // MUST copy!
        return;
    }

    // Explore all choices
    for (let i = 0; i < choices.length; i++) {
        const choice = choices[i];

        // Pruning: Skip invalid choices
        if (!isValidChoice(choice, state)) continue;

        // 1. Make the choice
        state.push(choice);

        // 2. Recursively explore
        backtrack(state, remainingChoices(choices, i), result);

        // 3. Undo the choice (backtrack!)
        state.pop();
    }
}
```

### Template Variations

**Variation 1: Index-based (for arrays)**
```typescript
function backtrack(index: number, path: number[]): void {
    if (index === nums.length) {
        result.push([...path]);
        return;
    }

    // Explore from current index
    for (let i = index; i < nums.length; i++) {
        path.push(nums[i]);
        backtrack(i + 1, path);
        path.pop();
    }
}
```

**Variation 2: With Used Tracking**
```typescript
function backtrack(path: number[], used: boolean[]): void {
    if (path.length === n) {
        result.push([...path]);
        return;
    }

    for (let i = 0; i < nums.length; i++) {
        if (used[i]) continue;

        path.push(nums[i]);
        used[i] = true;
        backtrack(path, used);
        used[i] = false;
        path.pop();
    }
}
```

---

## 🎯 Pattern 1: Subsets (All Combinations)

### Concept
Generate all possible subsets of a set. Each element has two choices: include or exclude.

### Decision Tree for [1,2,3]
```
                     []
            /                  \
          [1]                  []
         /   \               /    \
      [1,2]  [1]          [2]     []
       /  \   / \         / \     / \
   [1,2,3][1,2][1,3][1][2,3][2][3][]
```

### Code Template
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

**Time:** O(2^n × n) - 2^n subsets, O(n) to copy each
**Space:** O(n) - recursion depth

### Key Points
- **Start index** prevents duplicates ([1,2] and [2,1])
- **Every node** in tree is a valid result
- **Result copied** at every recursive call

---

## 🎯 Pattern 2: Permutations (All Arrangements)

### Concept
Generate all possible arrangements where order matters. Each position can have any unused element.

### Decision Tree for [1,2,3]
```
                      []
          /           |           \
        [1]          [2]          [3]
       /   \        /   \        /   \
    [1,2] [1,3]  [2,1] [2,3]  [3,1] [3,2]
      |     |      |     |      |     |
   [1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]
```

### Code Template
```typescript
function permute(nums: number[]): number[][] {
    const result: number[][] = [];
    const used = new Array(nums.length).fill(false);

    function backtrack(path: number[]): void {
        // Found a complete permutation
        if (path.length === nums.length) {
            result.push([...path]);
            return;
        }

        // Try each unused number
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

**Time:** O(n! × n) - n! permutations, O(n) to copy each
**Space:** O(n) - recursion depth + used array

### Key Points
- **Track used elements** with boolean array or Set
- **Results only at leaf nodes** (full length)
- **All positions** try all unused elements

---

## 🎯 Pattern 3: Handling Duplicates

### Key Technique
Sort the input and skip duplicates at the same decision level.

### Why Sorting Helps
```
Input: [1, 2, 2]

Without sorting:
- Might generate [1,2,2] from index [0,1,2]
- AND [1,2,2] from index [0,2,1]
- Duplicates!

With sorting + skipping:
- When at same level, skip if nums[i] === nums[i-1]
- Only use first occurrence of duplicates
```

### Code Pattern
```typescript
function subsetsWithDup(nums: number[]): number[][] {
    nums.sort((a, b) => a - b); // Sort first!
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

### The Magic Condition
```typescript
if (i > start && nums[i] === nums[i - 1]) continue;
```

**Why `i > start`?**
- `i === start`: First choice at this level → Use it
- `i > start`: Not first, and same as previous → Skip it

---

## 🎯 Pattern 4: Combinations with Constraints

### Example: Combination Sum (Target Sum)

```typescript
function combinationSum(candidates: number[], target: number): number[][] {
    const result: number[][] = [];

    function backtrack(start: number, path: number[], sum: number): void {
        // Base case: Found valid combination
        if (sum === target) {
            result.push([...path]);
            return;
        }

        // Pruning: Stop if sum exceeds target
        if (sum > target) return;

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

**Key Points:**
- **Track running state** (sum, count, etc.)
- **Prune early** when constraint violated
- **Reuse vs single-use** controlled by index parameter

---

## 🎯 Pattern 5: String Building (Generate Parentheses)

### Concept
Build valid strings character by character with constraints.

```typescript
function generateParenthesis(n: number): string[] {
    const result: string[] = [];

    function backtrack(path: string[], open: number, close: number): void {
        // Base case: Built complete string
        if (path.length === 2 * n) {
            result.push(path.join(''));
            return;
        }

        // Add '(' if we haven't used all
        if (open < n) {
            path.push('(');
            backtrack(path, open + 1, close);
            path.pop();
        }

        // Add ')' if it won't make invalid
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

**Key Insight:** Can only add ')' when `close < open` (have unclosed '(').

---

## 🎯 Pattern 6: Constraint Satisfaction (N-Queens)

### Concept
Place elements with complex constraints that must be checked at each step.

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

**Diagonal Math:**
- **Main diagonal** (↘): All cells have same `row - col`
- **Anti-diagonal** (↙): All cells have same `row + col`

---

## ⚡ Optimization Techniques

### 1. Early Pruning
Stop exploring branches that can't lead to valid solutions:

```typescript
// In combination sum with target
if (currentSum > target) return; // Prune this branch

// In combinations C(n, k)
if (path.length + (n - start + 1) < k) return; // Not enough elements left
```

### 2. Preprocessing
Sort input to enable pruning and handle duplicates:

```typescript
candidates.sort((a, b) => a - b);
// Now can skip duplicates: if (i > start && nums[i] === nums[i-1]) continue
// Also can break early: if (sum + candidates[i] > target) break
```

### 3. State Optimization
Use efficient data structures for state tracking:

```typescript
// Instead of copying entire board each time
const cols = new Set<number>();      // O(1) operations
const diag1 = new Set<number>();
const diag2 = new Set<number>();

// Instead of checking entire board: O(n)
if (cols.has(col)) continue;         // O(1) check
```

---

## 📊 Time Complexity Analysis

### General Formula
```
Time = (Number of nodes in decision tree) × (Work per node)
```

### Common Patterns

| Pattern | Nodes | Work/Node | Total | Explanation |
|---------|-------|-----------|-------|-------------|
| **Subsets** | 2^n | O(n) | **O(2^n × n)** | Each element: include/exclude |
| **Permutations** | n! | O(n) | **O(n! × n)** | n choices, then n-1, then n-2... |
| **Combinations C(n,k)** | C(n,k) | O(k) | **O(C(n,k) × k)** | Choose k from n |
| **N-Queens** | ~n! | O(1) | **O(n!)** | n choices row 1, ≤n-1 row 2... |
| **Parentheses** | Catalan | O(n) | **O(4^n / √n)** | Catalan number |

### Space Complexity
Usually **O(n)** for:
- Recursion depth (max n levels)
- Current path storage
- State tracking (used array, sets)

Plus **O(result size)** for storing all solutions.

---

## 💡 Interview Tips & Tricks

### Pattern Recognition

| Problem Phrase | Pattern | Template |
|----------------|---------|----------|
| "All possible" | Backtracking | Standard template |
| "All subsets/combinations" | Start index | `backtrack(start, path)` |
| "All permutations" | Track used | `backtrack(path, used)` |
| "Generate valid X" | Constraints | Add validation checks |
| "With duplicates" | Sort + skip | `if (i > start && nums[i] === nums[i-1])` |

### Template Selection Guide

**Use START INDEX when:**
- Order doesn't matter
- Want combinations, not permutations
- Examples: Subsets, Combination Sum

**Use USED ARRAY when:**
- Order matters
- Want permutations
- Examples: Permutations, Arrange coins

**Use CUSTOM STATE when:**
- Complex constraints
- Need validation at each step
- Examples: N-Queens, Sudoku, Palindrome Partitioning

### Common Interview Questions

**Q: "What's the time complexity?"**
```
"We're exploring all possible [subsets/permutations], which is [2^n / n!].
At each node, we do O(n) work to copy the path, so O([2^n / n!] × n) total."
```

**Q: "Can you optimize this?"**
```
"Yes, we can prune branches early by checking [constraint] before recursing.
This won't change worst-case complexity but helps in practice."
```

**Q: "How do you handle duplicates?"**
```
"First sort the array, then skip duplicates at the same tree level using:
if (i > start && nums[i] === nums[i-1]) continue"
```

---

## 🐛 Debugging Tips

### 1. Print the Decision Tree
```typescript
function backtrack(depth: number, path: number[]): void {
    console.log('  '.repeat(depth) + `Path: [${path}]`);
    // ... rest of logic
}
```

Output helps visualize the exploration:
```
Path: []
  Path: [1]
    Path: [1,2]
      Path: [1,2,3]
    Path: [1,3]
  Path: [2]
    Path: [2,3]
  Path: [3]
```

### 2. Verify Copying
```typescript
// ❌ Wrong - shares reference
result.push(path);

// ✅ Correct - creates copy
result.push([...path]);
result.push(path.slice());
result.push(Array.from(path));
```

### 3. Check Backtracking
```typescript
// Every push must have matching pop!
path.push(choice);
backtrack(/* ... */);
path.pop();  // Must be here!
```

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **Template:** Make choice → Explore → Undo choice
- **Subsets:** O(2^n × n), every node valid
- **Permutations:** O(n! × n), only leaves valid
- **Duplicates:** Sort + skip at same level
- **Always copy** when adding to results!

---

[Back to Session README](./README.md)
