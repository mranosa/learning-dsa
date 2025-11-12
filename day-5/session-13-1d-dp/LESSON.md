# Lesson: 1D Dynamic Programming

---

## 📹 Video 1: Dynamic Programming Fundamentals (25 min)

**"Dynamic Programming - Learn to Solve Algorithmic Problems" by freeCodeCamp**
https://www.youtube.com/watch?v=oBt53YbR9Kk

**Focus on:**
- What is Dynamic Programming
- Overlapping subproblems
- Optimal substructure
- When to use DP vs recursion
- Basic DP examples

---

## 📹 Video 2: Memoization vs Tabulation (15 min)

**"Memoization and Dynamic Programming Explained" by Back To Back SWE**
https://www.youtube.com/watch?v=P8Xa2BitN3I

**Alternative - NeetCode DP Intro:**
https://www.youtube.com/watch?v=73r3KWiEvyk

**Focus on:**
- Top-down memoization approach
- Bottom-up tabulation approach
- When to use each technique
- Space complexity tradeoffs

---

## 📹 Video 3: 1D DP Patterns (15 min)

**"Dynamic Programming Patterns" by NeetCode**
https://www.youtube.com/watch?v=aPQY__2H3tE

**Focus on:**
- Linear sequence pattern
- Decision making pattern
- Counting ways pattern
- Optimization pattern

---

## 🎯 Dynamic Programming Fundamentals

### What is Dynamic Programming?

DP is an optimization technique that solves complex problems by:
1. Breaking them into simpler overlapping subproblems
2. Storing results to avoid redundant calculations
3. Building up solutions from smallest subproblems

**Key Requirements:**
- **Overlapping Subproblems:** Same subproblems solved multiple times
- **Optimal Substructure:** Optimal solution contains optimal sub-solutions

---

## 🔧 DP vs Recursion vs Memoization

### Comparison: Fibonacci Example

```typescript
// Recursive (Exponential - O(2ⁿ))
function fibRecursive(n: number): number {
  if (n <= 1) return n;
  return fibRecursive(n - 1) + fibRecursive(n - 2);
}

// Top-Down DP with Memoization (O(n))
function fibMemo(n: number, memo: Map<number, number> = new Map()): number {
  if (n <= 1) return n;
  if (memo.has(n)) return memo.get(n)!;

  const result = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);
  memo.set(n, result);
  return result;
}

// Bottom-Up DP/Tabulation (O(n))
function fibDP(n: number): number {
  if (n <= 1) return n;
  const dp = new Array(n + 1);
  dp[0] = 0;
  dp[1] = 1;

  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }
  return dp[n];
}

// Space-Optimized (O(1) space)
function fibOptimized(n: number): number {
  if (n <= 1) return n;
  let prev2 = 0, prev1 = 1;

  for (let i = 2; i <= n; i++) {
    const curr = prev1 + prev2;
    prev2 = prev1;
    prev1 = curr;
  }
  return prev1;
}
```

**Time Comparison:**
```
Recursive:    O(2ⁿ) - fib(40) takes seconds
Memoization:  O(n)  - fib(40) instant
Tabulation:   O(n)  - fib(40) instant
Optimized:    O(n)  - fib(40) instant, O(1) space
```

---

## 📊 Memoization vs Tabulation

| Aspect | Memoization (Top-Down) | Tabulation (Bottom-Up) |
|--------|------------------------|------------------------|
| **Approach** | Recursive + cache | Iterative + table |
| **Start** | From target, recurse down | From base cases, build up |
| **Cache** | Only computed states | All states up to target |
| **Stack** | Uses call stack | No recursion |
| **Space** | Cache + stack O(n) | Table O(n) |
| **Intuitive** | Easier to think through | Requires reverse thinking |
| **Speed** | Slightly slower (recursion overhead) | Slightly faster |

**When to use:**
- **Memoization:** Easier to implement, only computes needed states
- **Tabulation:** Faster, no stack overflow risk, easier to optimize space

---

## 🧩 Common 1D DP Patterns

### Pattern 1: Linear Sequence

**📹 Learn:** [Climbing Stairs Explained](https://www.youtube.com/watch?v=Y0lT9Fck7qI) by NeetCode (~8 min)

Problems where dp[i] depends on previous elements.

```typescript
// Example: Climbing Stairs
// dp[i] = number of ways to reach step i
// Recurrence: dp[i] = dp[i-1] + dp[i-2]

function climbStairs(n: number): number {
  if (n <= 2) return n;

  let prev2 = 1, prev1 = 2;
  for (let i = 3; i <= n; i++) {
    const curr = prev1 + prev2;
    prev2 = prev1;
    prev1 = curr;
  }
  return prev1;
}
```

**Time:** O(n) | **Space:** O(1)

---

### Pattern 2: Decision Making

**📹 Learn:** [House Robber Explained](https://www.youtube.com/watch?v=73r3KWiEvyk) by NeetCode (~11 min)

At each step, make choice: include or exclude element.

```typescript
// Example: House Robber
// dp[i] = max money robbing up to house i
// Recurrence: dp[i] = max(dp[i-1], dp[i-2] + nums[i])

function rob(nums: number[]): number {
  if (nums.length === 0) return 0;
  if (nums.length === 1) return nums[0];

  let prev2 = nums[0];
  let prev1 = Math.max(nums[0], nums[1]);

  for (let i = 2; i < nums.length; i++) {
    const curr = Math.max(prev1, prev2 + nums[i]);
    prev2 = prev1;
    prev1 = curr;
  }

  return prev1;
}
```

**Key insight:** Rob current house OR skip it - choose max profit.

**Time:** O(n) | **Space:** O(1)

---

### Pattern 3: Optimization

**📹 Learn:** [Coin Change DP](https://www.youtube.com/watch?v=H9bfqozjoqs) by NeetCode (~13 min)

Find minimum/maximum over all choices.

```typescript
// Example: Coin Change
// dp[i] = minimum coins to make amount i
// Recurrence: dp[i] = min(dp[i-coin] + 1) for all coins

function coinChange(coins: number[], amount: number): number {
  const dp = new Array(amount + 1).fill(amount + 1);
  dp[0] = 0;

  for (let i = 1; i <= amount; i++) {
    for (const coin of coins) {
      if (i - coin >= 0) {
        dp[i] = Math.min(dp[i], dp[i - coin] + 1);
      }
    }
  }

  return dp[amount] > amount ? -1 : dp[amount];
}
```

**Key insight:** Try all coins, take minimum.

**Time:** O(amount × coins) | **Space:** O(amount)

---

### Pattern 4: Counting

**📹 Learn:** [Decode Ways DP](https://www.youtube.com/watch?v=6aEyTjOwlJU) by NeetCode (~12 min)

Count number of ways to achieve something.

```typescript
// Example: Decode Ways
// dp[i] = number of ways to decode up to index i
// Recurrence: dp[i] = dp[i-1] (if valid single) + dp[i-2] (if valid double)

function numDecodings(s: string): number {
  if (s[0] === '0') return 0;

  const n = s.length;
  let prev2 = 1, prev1 = 1;

  for (let i = 1; i < n; i++) {
    let curr = 0;

    // Single digit
    if (s[i] !== '0') {
      curr += prev1;
    }

    // Two digits
    const twoDigit = parseInt(s.substring(i - 1, i + 1));
    if (twoDigit >= 10 && twoDigit <= 26) {
      curr += prev2;
    }

    prev2 = prev1;
    prev1 = curr;
  }

  return prev1;
}
```

**Key insight:** Add ways from all valid previous states.

**Time:** O(n) | **Space:** O(1)

---

### Pattern 5: Existence/Reachability

**📹 Learn:** [Jump Game DP vs Greedy](https://www.youtube.com/watch?v=Yan0cv2cLy8) by NeetCode (~7 min)

Check if target state is reachable.

```typescript
// Example: Jump Game
// Greedy approach - track furthest reachable position

function canJump(nums: number[]): boolean {
  let maxReach = 0;

  for (let i = 0; i < nums.length; i++) {
    if (i > maxReach) return false;
    maxReach = Math.max(maxReach, i + nums[i]);
  }

  return true;
}
```

**Note:** Not all reachability problems need DP - greedy can work if no backtracking needed.

**Time:** O(n) | **Space:** O(1)

---

## 🎯 DP Problem-Solving Framework

### Step 1: Identify if DP Applies

**Questions to ask:**
- Does problem ask for optimal solution (min/max/count)?
- Can problem be broken into subproblems?
- Do subproblems overlap (same calculation repeated)?
- Does optimal solution depend on optimal sub-solutions?

**Red flags (DP might NOT work):**
- No overlapping subproblems
- No optimal substructure
- Greedy choice property exists

---

### Step 2: Define State

**State = parameters uniquely identifying a subproblem**

Examples:
- Fibonacci: `dp[n]` = nth Fibonacci number
- House Robber: `dp[i]` = max money robbing houses 0..i
- Coin Change: `dp[amount]` = min coins to make amount
- LIS: `dp[i]` = longest increasing subsequence ending at i

**Common state types:**
- Index: `dp[i]`
- Index + value: `dp[i][j]`
- Amount: `dp[amount]`
- Position: `dp[pos]`

---

### Step 3: Write Recurrence Relation

**Recurrence = formula connecting current state to previous states**

Examples:
```typescript
// Fibonacci
dp[n] = dp[n-1] + dp[n-2]

// House Robber
dp[i] = max(dp[i-1], dp[i-2] + nums[i])

// Coin Change
dp[i] = min(dp[i-coin] + 1) for all coins

// Climbing Stairs
dp[i] = dp[i-1] + dp[i-2]
```

**How to derive:**
1. Think about last decision made
2. What states does it depend on?
3. How to combine previous states?

---

### Step 4: Identify Base Cases

**Base cases = smallest subproblems with known answers**

Examples:
```typescript
// Fibonacci
dp[0] = 0, dp[1] = 1

// House Robber
dp[0] = nums[0], dp[1] = max(nums[0], nums[1])

// Coin Change
dp[0] = 0  (0 coins to make 0)

// Climbing Stairs
dp[1] = 1, dp[2] = 2
```

---

### Step 5: Determine Computation Order

**For tabulation:** What order to fill DP table?

Usually:
- Left to right for linear sequences
- Smaller amounts to larger
- Earlier indices to later

**For memoization:** Start from target, recurse to base cases.

---

## 💡 Implementation Templates

### Top-Down Template (Memoization)

```typescript
function solveMemo(n: number): number {
  const memo = new Map<number, number>();

  function dp(i: number): number {
    // Base cases
    if (i <= 0) return baseValue;

    // Check memo
    if (memo.has(i)) return memo.get(i)!;

    // Compute result using recurrence
    let result = 0;
    // Example: result = dp(i-1) + dp(i-2)

    // Store and return
    memo.set(i, result);
    return result;
  }

  return dp(n);
}
```

**Pros:** Easier to code, only computes needed states
**Cons:** Recursion overhead, stack space

---

### Bottom-Up Template (Tabulation)

```typescript
function solveDP(n: number): number {
  // Edge cases
  if (n <= 0) return baseValue;

  // Initialize DP array
  const dp = new Array(n + 1);

  // Base cases
  dp[0] = baseValue0;
  dp[1] = baseValue1;

  // Fill DP table
  for (let i = 2; i <= n; i++) {
    // Recurrence relation
    dp[i] = /* compute from dp[i-1], dp[i-2], etc. */
  }

  return dp[n];
}
```

**Pros:** Faster, no stack overflow, easier to optimize space
**Cons:** Need to think in reverse

---

### Space-Optimized Template

```typescript
function solveOptimized(n: number): number {
  // Edge cases
  if (n <= 0) return baseValue;

  // Only keep necessary previous states
  let prev2 = baseValue0;
  let prev1 = baseValue1;

  for (let i = 2; i <= n; i++) {
    const curr = /* compute from prev1, prev2 */
    prev2 = prev1;
    prev1 = curr;
  }

  return prev1;
}
```

**Optimization:** If only need k previous states, use k variables instead of array.

**Time:** Same as tabulation
**Space:** O(1) instead of O(n)

---

## 🎯 State Transition Examples

### Example 1: Climbing Stairs

**Problem:** Ways to climb n stairs, 1 or 2 steps at a time.

**State:** `dp[i]` = ways to reach stair i

**Transition:** To reach stair i, came from i-1 or i-2
```typescript
dp[i] = dp[i-1] + dp[i-2]
```

**Base:** `dp[0] = 1, dp[1] = 1`

---

### Example 2: House Robber

**Problem:** Max money robbing houses, can't rob adjacent.

**State:** `dp[i]` = max money robbing houses 0..i

**Transition:** Rob house i or skip it
```typescript
dp[i] = max(
  dp[i-1],           // Skip house i
  dp[i-2] + nums[i]  // Rob house i
)
```

**Base:** `dp[0] = nums[0], dp[1] = max(nums[0], nums[1])`

---

### Example 3: Coin Change

**Problem:** Min coins to make amount.

**State:** `dp[amount]` = min coins to make amount

**Transition:** Try each coin, take minimum
```typescript
dp[amount] = min(
  dp[amount - coin1] + 1,
  dp[amount - coin2] + 1,
  ...
)
```

**Base:** `dp[0] = 0`

---

## 💡 Interview Tips

### Problem Recognition

**DP keywords:**
- "Maximum", "Minimum", "Longest", "Shortest"
- "Count ways", "Number of ways"
- "Can you reach", "Is it possible"
- "Optimal", "Best"

**Check overlapping subproblems:**
- Draw recursion tree for small input
- Same calculations repeated?
- Use DP!

---

### Communication Strategy

**Say this:**
1. "This looks like DP - we need optimal solution with overlapping subproblems"
2. "Let me define state: dp[i] represents..."
3. "Recurrence relation is..."
4. "Base cases are..."
5. "I'll start with tabulation, O(n) space, then optimize to O(1)"

**Walk through example:**
- Show small input (n=3 or n=4)
- Fill DP table step by step
- Explain each transition

---

### Common Follow-ups

**Q: "Can you optimize space?"**
- If only need k previous states, use k variables

**Q: "Can you solve it recursively?"**
- Show memoization approach

**Q: "Print the actual solution, not just the value?"**
- Backtrack through DP table to reconstruct solution

**Q: "What if n is very large?"**
- Discuss space optimization
- Consider if closed-form formula exists

---

## 🎯 TypeScript Specifics

### Array Initialization

```typescript
// Wrong - creates array with undefined
const dp = new Array(n);

// Correct - fill with default value
const dp = new Array(n).fill(0);

// For infinity
const dp = new Array(n).fill(Infinity);

// For large value (coin change)
const dp = new Array(n).fill(n + 1);
```

---

### Map for Memoization

```typescript
// Use Map for memo
const memo = new Map<number, number>();

// Check if exists
if (memo.has(key)) return memo.get(key)!;

// Store result
memo.set(key, result);
```

---

### Max/Min Tracking

```typescript
// Initialize max
let maxVal = -Infinity;
let maxVal = nums[0];

// Initialize min
let minVal = Infinity;
let minVal = nums[0];

// Update
maxVal = Math.max(maxVal, current);
minVal = Math.min(minVal, current);
```

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **DP requirements:** Overlapping subproblems + optimal substructure
- **Memoization:** Top-down, recursive + cache
- **Tabulation:** Bottom-up, iterative + table
- **Space optimization:** Keep only k previous states

**Pattern Checklist:**
- Linear sequence: dp[i] from dp[i-1], dp[i-2]
- Decision making: max(include, exclude)
- Optimization: min/max over choices
- Counting: sum of ways from previous states

---

[Back to Session README](./README.md)
