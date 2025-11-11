# Interview Framework: The UMPIRE Method

The **UMPIRE method** is your structured approach to solving every coding interview problem. Master this framework and you'll never feel lost in an interview.

---

## What is UMPIRE?

**UMPIRE** is an acronym for the 6 steps of problem-solving:

1. **U**nderstand
2. **M**atch
3. **P**lan
4. **I**mplement
5. **R**eview
6. **E**valuate

Each step is critical. **Don't skip any!**

---

## The 6 Steps in Detail

### 1. UNDERSTAND (2-3 minutes)

**Goal:** Ensure you completely understand the problem before attempting to solve it.

#### What to Do:
- **Restate the problem** in your own words
- **Ask clarifying questions**
- **Identify inputs and outputs**
- **Understand constraints**
- **Clarify edge cases**

#### Clarifying Questions Checklist:
```
□ What are the input types and ranges?
□ Can the input be empty or null?
□ Are there duplicates?
□ Is the input sorted?
□ What should I return for edge cases?
□ Are there any time/space constraints?
□ Can I modify the input?
□ What values can be negative/zero/positive?
```

#### Example - Two Sum:
```
Interviewer: "Given an array of integers and a target, return indices of
two numbers that add up to the target."

You:
"Let me make sure I understand:
- Input is an array of integers, any size?
- Target is also an integer?
- I return the indices (not the values)?
- Can the array be empty?
- Are there always two numbers that sum to target?
- Can I use the same element twice?
- Is the array sorted?"

Interviewer: "Great questions! Array has at least 2 elements, exactly
one solution exists, you cannot use the same element twice, array is
not sorted."

You: "Perfect, so I need to find two different elements whose values
sum to target, and return their indices."
```

#### Why This Matters:
- Shows you're thoughtful, not rushing
- Prevents solving the wrong problem
- Clarifies ambiguous requirements
- Demonstrates communication skills
- Saves time by avoiding wrong assumptions

---

### 2. MATCH (1-2 minutes)

**Goal:** Identify which pattern or algorithm applies to this problem.

#### What to Do:
- **Recognize patterns** from keywords and structure
- **Match to known algorithms** and data structures
- **Recall similar problems** you've solved

#### Pattern Recognition Keywords:
```
"Subarray" → Sliding Window, Prefix Sum, Kadane's
"Subsequence" → DP (usually 2D)
"Find pair/triplet" → Two Pointers, Hash Map
"Sorted array" → Binary Search, Two Pointers
"Top K elements" → Heap
"All combinations" → Backtracking
"Shortest path" → BFS (unweighted), Dijkstra (weighted)
"Connected components" → DFS, Union-Find
"Maximum/minimum" → DP, Greedy, Kadane's
"Palindrome" → Two Pointers, DP
"Anagram" → Hash Map (frequency counter)
"Tree level-order" → BFS
"Tree paths" → DFS
```

#### Example - Two Sum:
```
You: "This problem involves finding a pair that sums to a target.
I've seen similar problems that use either:

1. Two Pointers (if array was sorted) - O(n) time, O(1) space
2. Hash Map (for unsorted) - O(n) time, O(n) space

Since the array is not sorted, I'll use a hash map to store values
I've seen, and check if target-current exists."
```

#### Why This Matters:
- Shows pattern recognition skills
- Demonstrates you've practiced similar problems
- Helps you quickly choose the right approach
- Interviewers want to see you think in patterns

---

### 3. PLAN (3-5 minutes)

**Goal:** Explain your approach before writing any code.

#### What to Do:
- **Start with brute force** (even if obvious)
- **Explain the optimized approach**
- **Walk through an example**
- **Discuss time and space complexity**
- **Get interviewer approval before coding**

#### Planning Template:
```
1. Brute Force Approach:
   - Algorithm: [describe steps]
   - Time: O(?)
   - Space: O(?)
   - Why not optimal: [explain]

2. Optimized Approach:
   - Algorithm: [describe steps]
   - Time: O(?)
   - Space: O(?)
   - Trade-offs: [explain]

3. Walk through with example

4. Get approval: "Does this approach make sense? Should I proceed?"
```

#### Example - Two Sum:
```
You: "Let me outline my approach:

**Brute Force:**
Use nested loops to check all pairs.
- Outer loop: i from 0 to n-1
- Inner loop: j from i+1 to n-1
- If nums[i] + nums[j] == target, return [i, j]
- Time: O(n²), Space: O(1)
- Not optimal for large arrays

**Optimized (Hash Map):**
Use a hash map to store values we've seen.
- Create empty map
- Loop through array once
- For each number, calculate complement = target - number
- If complement exists in map, we found the pair
- Otherwise, add current number to map with its index
- Time: O(n), Space: O(n)

**Example walkthrough:** nums = [2, 7, 11, 15], target = 9
- i=0: num=2, complement=7, map={}, add 2→0, map={2:0}
- i=1: num=7, complement=2, map={2:0}, found! return [0,1]

**Trade-off:** Using O(n) extra space for O(n) time instead of O(n²).

Does this approach make sense?"

Interviewer: "Yes, proceed with the hash map approach."
```

#### Why This Matters:
- Shows you think before you code
- Demonstrates you understand complexity analysis
- Gives interviewer chance to guide you
- Prevents coding wrong solution
- **Most candidates skip this and fail!**

---

### 4. IMPLEMENT (15-25 minutes)

**Goal:** Write clean, correct code while communicating your thought process.

#### What to Do:
- **Think aloud** while coding
- **Use descriptive variable names**
- **Handle edge cases in your code**
- **Write TypeScript with proper types**
- **Keep code clean and readable**

#### Implementation Checklist:
```
□ Think aloud - explain what you're writing
□ Use meaningful variable names (not x, y, z)
□ Add TypeScript type annotations
□ Handle edge cases
□ Write helper functions if needed
□ Keep code modular and clean
□ Avoid premature optimization
```

#### Example - Two Sum (Good Implementation):
```typescript
function twoSum(nums: number[], target: number): number[] {
  // Create hash map to store value → index mapping
  const seen = new Map<number, number>();

  // Loop through array once
  for (let i = 0; i < nums.length; i++) {
    const currentNum = nums[i];
    const complement = target - currentNum;

    // Check if complement exists in our map
    if (seen.has(complement)) {
      // Found the pair! Return their indices
      return [seen.get(complement)!, i];
    }

    // Haven't found pair yet, store current number
    seen.set(currentNum, i);
  }

  // Problem guarantees solution exists, but TypeScript needs return
  return [];
}
```

#### Good Thinking Aloud Example:
```
"I'll create a Map called 'seen' to store the numbers I've encountered...
Using Map<number, number> for value-to-index mapping...

Now I'll loop through the array with index i...
For each iteration, I'll store the current number in a variable...
Calculate the complement by subtracting from target...

Check if complement exists in my map using has()...
If it does, I've found the pair, so return both indices...
The complement's index is from the map, current index is i...

If no match, add the current number to the map with its index...
This way, future iterations can find it if needed...

After the loop, return empty array - though problem says solution always exists..."
```

#### Why This Matters:
- Interviewers want to hear your thought process
- Shows you're not just memorizing solutions
- Helps catch bugs early
- Demonstrates communication skills
- Makes you seem confident and organized

---

### 5. REVIEW (3-5 minutes)

**Goal:** Test your solution and catch bugs before the interviewer does.

#### What to Do:
- **Walk through code with given example**
- **Test edge cases**
- **Look for common bugs**
- **Dry run with small input**

#### Testing Checklist:
```
□ Trace through code with given example
□ Test empty input
□ Test single element
□ Test two elements (minimum)
□ Test duplicate values
□ Test negative numbers/zero
□ Test maximum constraints
□ Check for off-by-one errors
□ Verify array bounds
□ Check null/undefined handling
```

#### Example - Two Sum:
```
You: "Let me trace through my code with the example:

nums = [2, 7, 11, 15], target = 9
seen = {}

i=0: currentNum=2, complement=7
- seen.has(7)? No
- seen.set(2, 0) → seen = {2:0}

i=1: currentNum=7, complement=2
- seen.has(2)? Yes!
- return [seen.get(2), 1] = [0, 1] ✓

Now let me test edge cases:

1. nums = [3, 3], target = 6 (duplicates)
   - i=0: complement=3, not in map, add 3:0
   - i=1: complement=3, found at index 0, return [0,1] ✓

2. nums = [1, 2], target = 10 (no solution)
   - Problem says solution always exists, so we won't hit this
   - But our code returns [] which is reasonable ✓

3. What if target = 0, nums = [-1, 1]?
   - i=0: currentNum=-1, complement=1, add -1:0
   - i=1: currentNum=1, complement=-1, found! return [0,1] ✓

My solution looks correct!"
```

#### Common Bugs to Check:
```
□ Off-by-one errors (i < n vs i <= n)
□ Array index out of bounds
□ Null/undefined not handled
□ Wrong comparison operators (< vs <=)
□ Infinite loops (forgot to increment)
□ Integer overflow
□ Modifying array while iterating
□ Uninitialized variables
□ Wrong base case in recursion
```

#### Why This Matters:
- Shows you care about correctness
- Catches bugs before interviewer finds them
- Demonstrates thoroughness
- Most candidates skip this!

---

### 6. EVALUATE (2 minutes)

**Goal:** Analyze complexity and discuss potential optimizations.

#### What to Do:
- **State time complexity with justification**
- **State space complexity**
- **Discuss trade-offs**
- **Mention potential optimizations**

#### Evaluation Template:
```
**Time Complexity:** O(?)
**Justification:** [Explain why]

**Space Complexity:** O(?)
**Justification:** [Explain why]

**Trade-offs:** [What we gained and what we gave up]

**Potential Optimizations:** [Can we do better? Why or why not?]
```

#### Example - Two Sum:
```
You: "Let me analyze the complexity:

**Time Complexity: O(n)**
We loop through the array once (n iterations). Each hash map operation
(has, get, set) is O(1) average. So overall: O(n).

**Space Complexity: O(n)**
In the worst case (no solution found until the end), we store n-1
elements in our hash map. So space is O(n).

**Trade-off:**
We're trading space (O(n) for the hash map) to get better time
complexity (O(n) instead of O(n²) brute force). For large arrays,
this is a worthwhile trade-off.

**Could we optimize further?**
- Time: O(n) is optimal - we must look at each element at least once.
- Space: We could use O(1) space with two pointers, BUT only if array
  is sorted. Sorting would take O(n log n), making time worse.

So our hash map solution is optimal for an unsorted array."

Interviewer: "Excellent analysis!"
```

#### Why This Matters:
- Shows you understand algorithm analysis
- Demonstrates you think about trade-offs
- Proves you know when a solution is optimal
- Differentiates strong candidates

---

## UMPIRE in Action: Complete Example

**Problem:** Contains Duplicate
*Given an integer array nums, return true if any value appears at least twice.*

### U - UNDERSTAND
```
"Let me understand:
- Input: array of integers, any size?
- Output: boolean (true if duplicate exists)
- Can array be empty? Should I return false?
- Are we looking for any duplicates, not just adjacent ones?
- Any constraints on array size or values?"

Interviewer: "Array can be empty (return false). Looking for any
duplicates anywhere in array. Array size up to 10^5."
```

### M - MATCH
```
"This is a 'check if exists' problem. I can use:
1. Hash Set - O(n) time, O(n) space
2. Sorting - O(n log n) time, O(1) space (if in-place sorting allowed)
3. Brute force - O(n²) time, O(1) space

Given the array can be large (10^5), I'll use a hash set for O(n) time."
```

### P - PLAN
```
"Here's my approach:

**Brute Force:** Check every pair - O(n²) time, too slow.

**Optimized (Hash Set):**
1. Create empty set
2. Loop through array
3. For each number:
   - If it exists in set, return true (found duplicate)
   - Otherwise, add it to set
4. If loop completes, return false (no duplicates)

Time: O(n), Space: O(n)

**Example:** nums = [1, 2, 3, 1]
- i=0: 1 not in set, add → set={1}
- i=1: 2 not in set, add → set={1,2}
- i=2: 3 not in set, add → set={1,2,3}
- i=3: 1 in set! return true

Makes sense?"
```

### I - IMPLEMENT
```typescript
function containsDuplicate(nums: number[]): boolean {
  // Use Set to track numbers we've seen
  const seen = new Set<number>();

  // Loop through array once
  for (const num of nums) {
    // If number already exists, we found a duplicate
    if (seen.has(num)) {
      return true;
    }

    // Add number to set for future checks
    seen.add(num);
  }

  // No duplicates found
  return false;
}
```

### R - REVIEW
```
"Testing with examples:

nums = [1, 2, 3, 1]
- 1: not in set, add
- 2: not in set, add
- 3: not in set, add
- 1: in set! return true ✓

nums = [1, 2, 3, 4]
- Add all to set
- return false ✓

nums = []
- Loop doesn't run
- return false ✓

nums = [1]
- Add 1, no duplicates
- return false ✓

Looks correct!"
```

### E - EVALUATE
```
"**Time Complexity: O(n)**
Loop through array once, set operations are O(1).

**Space Complexity: O(n)**
In worst case (no duplicates), store all n elements in set.

**Trade-off:** Using O(n) space for O(n) time instead of O(n log n)
sorting approach.

**Optimization:** If we could modify input, we could sort in-place
for O(1) space but O(n log n) time. Current solution is better for
time-critical scenarios."
```

---

## Quick Reference

### Time Budget Per Phase
- Understand: 2-3 min
- Match: 1-2 min
- Plan: 3-5 min
- Implement: 15-25 min
- Review: 3-5 min
- Evaluate: 2 min

**Total: ~30-45 minutes** (varies by difficulty)

### Most Common Mistakes
1. ❌ Jumping straight to code (skipping Understand, Match, Plan)
2. ❌ Not asking clarifying questions
3. ❌ Coding silently without thinking aloud
4. ❌ Not discussing brute force first
5. ❌ Skipping the testing phase
6. ❌ Not explaining complexity analysis

### Pro Tips
- ✅ Always follow all 6 steps
- ✅ Get interviewer approval before coding
- ✅ Think aloud during implementation
- ✅ Test edge cases
- ✅ Explain your trade-offs

---

## Practice This!

Use UMPIRE for **every single problem** in this bootcamp. It will become second nature.

Print this framework and keep it visible during practice sessions.

---

[Back to README](./README.md)
