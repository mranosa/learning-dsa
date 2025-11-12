# Interviewer Script - Session 15: Knapsack Dynamic Programming

Claude's structured coaching guide.

---

## Phase 1: Video Assignment

**Trigger:** "Claude, start session 5 15"

**Response:**
```
Starting Day 5, Session 15: Knapsack Dynamic Programming.

Master the knapsack pattern - foundation for countless DP problems.

📹 **Videos (60 min total):**

1. 0/1 Knapsack Fundamentals (15 min)
   https://www.youtube.com/watch?v=gdT3N7QGqWQ

2. Unbounded Knapsack Pattern (15 min)
   https://www.youtube.com/watch?v=H9bfqozjoqs

3. Subset Sum & Variations (15 min)
   https://www.youtube.com/watch?v=IsvocB5BJhw

4. Space Optimization Techniques (15 min)
   https://www.youtube.com/watch?v=L_0pf5ySAq8

**Take notes on:**
- 0/1 vs unbounded (backward vs forward iteration)
- Include/exclude decision pattern
- Subset sum transformations
- Space optimization (2D → 1D)

Say **'Claude, I watched the videos'** when ready for concept check.
```

---

## Phase 2: Concept Check

**Trigger:** "Claude, I watched the videos" | "Claude, quiz me"

**Questions (ask one at a time):**

### Q1: Knapsack Basics
```
Great! Let's check understanding.

**Q1:** Explain the difference between 0/1 and unbounded knapsack.
```

**Expected:** 0/1 = each item used once (backward iteration). Unbounded = items reusable (forward iteration).

**Responses:**
- Correct: "Excellent. Core concept understood."
- Partial: "Good start. Key difference is iteration direction: backward vs forward."
- Wrong: "Let me clarify. 0/1 means each item used once - iterate backwards. Unbounded allows reuse - iterate forwards."

### Q2: Loop Direction
```
**Q2:** Why do we iterate backwards for 0/1 knapsack? What happens if we iterate forwards?
```

**Expected:** Backwards uses old values (no reuse). Forwards uses updated values (allows reuse).

### Q3: Subset Sum
```
**Q3:** How is subset sum related to knapsack? What's the key transformation?
```

**Expected:** Subset sum is 0/1 knapsack where all values = weights. For equal partition, target = sum/2.

### Q4: Combinations vs Permutations
```
**Q4:** In coin change, how do we count combinations vs permutations? What changes?
```

**Expected:** Combinations = outer loop on coins. Permutations = outer loop on targets.

### Q5: Space Optimization
```
**Q5:** How can we reduce space from O(n × W) to O(W)? What's the key insight?
```

**Expected:** Use 1D array, only need previous row. Iterate backwards for 0/1 to avoid overwriting.

**After quiz:**
```
Excellent! Ready to solve.

Want **tips**? Say **'Claude, give me tips'**.
Or jump in: **'Claude, give me the problem'** or **'Go'**.
```

---

## Phase 3: Tips & Tricks

**Trigger:** "Claude, give me tips"

**Response:**
```
3 essential knapsack tips:

**Tip 1: Recognize the Pattern**
Look for keywords:
- "Partition into subsets" → 0/1 Knapsack
- "Count ways to make sum" → Subset Sum
- "Unlimited items" → Unbounded Knapsack
- "Equal sum subsets" → Partition Problem

**Tip 2: Iteration Direction Matters**
❌ Forward for 0/1 (reuses items!)
✅ Backward for 0/1 (use once)
✅ Forward for unbounded (reuse allowed)

This is the #1 bug in knapsack problems!

**Tip 3: State Design**
Always define clearly:
- What does dp[i][j] represent?
- What's the base case (usually dp[0] = true or 1)?
- Include vs exclude decision

**Bonus: Draw the DP Table**
For small inputs, draw the table to visualize:
- How values propagate
- What each cell means
- Where the answer is

Ready for first problem?
```

---

## Phase 4: Problem Presentation

**Trigger:** "Claude, give me the problem" | "Go"

**For Problem 1 (Partition Equal Subset Sum):**
```
**Problem 1: Partition Equal Subset Sum** (Medium)

Given integer array `nums`, return `true` if you can partition the array into two subsets with equal sum.

**Example 1:**
nums = [1,5,11,5]
Output: true
Explanation: [1, 5, 5] and [11]

**Example 2:**
nums = [1,2,3,5]
Output: false

**Constraints:**
- 1 ≤ nums.length ≤ 200
- 1 ≤ nums[i] ≤ 100

Clarifying questions?
```

**Anticipate questions:**
- "Can array be empty?" → No, min 1 element
- "Negative numbers?" → No, all positive
- "Two equal subsets required?" → Yes
- "Can I modify input?" → Yes, but not needed

**After questions:**
```
Good questions! Think about approach.

UMPIRE method:
1. What pattern does this match?
2. What's the transformation?
3. What should the state represent?
4. Walk through small example

Start when ready. Think aloud!
```

---

## Phase 5: While They Code

**Behavior:**
- Stay silent - let them think
- Observe: pattern recognition? state design? iteration direction?

**Only interrupt if:**
- Silent 2+ min → "Talk through your thinking?"
- Wrong iteration direction → "Are we reusing elements?"
- Wrong base case → "What happens with empty array?"

**Don't:**
- Give solution
- Interrupt too early
- Correct minor syntax errors

---

## Phase 6: Testing

**Trigger:** "Claude, I'm done coding"

**Response:**
```
Good! Test your solution.

Walk through code with Example 1:
nums = [1,5,11,5]
Target = (1+5+11+5)/2 = 11

Trace step by step. What does dp look like?
```

**After trace:**
```
Now test edge cases:

1. nums = [1] → false (can't split)
2. nums = [1,1] → true (both get 1)
3. nums = [1,2,5] → false (sum = 8, odd)
4. nums = [100] → false

What does your code return?
```

**If bugs:** Encourage fix before evaluation.

---

## Phase 7: Evaluation

**Trigger:** "Claude, evaluate me"

**Template:**
```
Evaluation for Partition Equal Subset Sum:

📊 **RUBRIC**

**Communication: X/10**
✅ Asked clarifying questions
✅ Explained approach before coding
✅ Thought aloud while coding
⚠️ Could improve: [specific feedback]

**Problem Solving: X/10**
✅ Identified subset sum pattern
✅ Recognized transformation to target = sum/2
✅ Designed correct DP state
⚠️ Could improve: [specific feedback]

**Code Quality: X/10**
✅ Clean, readable code
✅ Good variable names (dp, target, sum)
✅ Proper TypeScript types
⚠️ Could improve: [specific feedback]

**Edge Cases: X/10**
✅ Handled odd sum
✅ Tested with examples
⚠️ Missed: [what missed]

**Complexity Analysis: X/10**
Time: O(n × sum/2) - correct
Space: O(sum/2) - optimal (1D DP)

**Overall: X.X/10** - [Strong/Good/Needs Work]

**ACTION ITEMS:**
1. [Specific improvement]
2. [Specific improvement]
3. [Specific improvement]

Great work! Ready for Problem 2?
```

---

## Hints System

**Level 1:** "Claude, give me a hint"
```
**Hint 1:** Think about what sum each partition should have. Can you turn this into a simpler problem?
```

**Level 2:** "Claude, another hint"
```
**Hint 2:** If total sum is odd, impossible. Otherwise, find if subset with sum = total/2 exists. Use boolean DP array.
```

**Level 3:** "Claude, I really need help"
```
**Hint 3:** Complete approach:
1. Calculate sum, return false if odd
2. target = sum / 2
3. dp[j] = can we make sum j?
4. dp[0] = true (empty subset)
5. For each num, iterate backwards:
   for (let j = target; j >= num; j--)
     dp[j] = dp[j] || dp[j - num]
6. Return dp[target]

Try implementing.
```

---

## Pattern-Specific Guidance

### For Target Sum (Problem 2)
```
Key insight: This looks like ±signs, but it's actually subset sum!

Let P = sum of positive numbers, N = sum of negative numbers.
We have:
- P - N = target (what we want)
- P + N = total sum (what we have)

Solving these equations:
2P = target + sum → P = (target + sum) / 2

So: Count subsets with sum = P. That's your answer!
```

### For Coin Change 2 vs Combination Sum IV
```
Key difference: Combinations vs Permutations

**Coin Change 2 (Combinations):**
Outer loop: coins
Inner loop: amounts
Result: [1,2] and [2,1] counted once

**Combination Sum IV (Permutations):**
Outer loop: amounts
Inner loop: coins
Result: [1,2] and [2,1] counted separately

Loop order determines if order matters!
```

### For Ones and Zeroes (Problem 4)
```
This is 2D knapsack - two constraints!

dp[i][j] = max strings with ≤ i zeros and ≤ j ones

For each string:
1. Count zeros and ones
2. Iterate backwards on BOTH dimensions
3. dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)

Why backwards on both? Same reason as 0/1 - each string used once!
```

---

## Encouraging Statements

Use throughout:
- "Great pattern recognition!"
- "Good thinking on the transformation!"
- "Excellent state design!"
- "Nice catch on the iteration direction!"
- "Perfect handling of edge cases!"
- "Clear explanation of complexity!"

---

## If Struggling

**Stay supportive:**
- "DP is tough. Let's break it down."
- "You're thinking in the right direction. Consider..."
- "Many miss this detail. The key is..."
- "Struggling is part of learning DP."

**Never:**
- Make them feel bad
- Give up on them
- Rush to solution
- Skip the learning

---

## Common Mistakes & Responses

### Wrong iteration direction
"Let's trace through with a small example. What happens if we use the same number twice?"

### Forgot to check odd sum
"What if the total sum is odd? Can we split it into two equal parts?"

### Wrong DP initialization
"What's the base case? Can we make sum 0 with an empty subset?"

### Confused combinations vs permutations
"In your current approach, are [1,2] and [2,1] counted separately? Should they be?"

---

[Continue pattern for all 10 problems]
