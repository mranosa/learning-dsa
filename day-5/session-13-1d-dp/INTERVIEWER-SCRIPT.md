# Session 13: Claude's Interview Script - 1D Dynamic Programming

## Introduction (2 minutes)
"Welcome to our technical interview. Today we'll be working on a dynamic programming problem. We'll spend about 45 minutes total - I'll present the problem, you'll work through a solution, and we'll discuss optimizations. Feel free to think out loud and ask clarifying questions. Ready to begin?"

---

## Problem Selection

Based on candidate level, choose one problem:

### For Junior/Mid-Level: Climbing Stairs
"You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"

### For Senior Level: House Robber
"You're a professional robber planning to rob houses along a street. Each house has money stashed, but adjacent houses have connected security systems. Given an array representing money in each house, what's the maximum amount you can rob without triggering alarms?"

### For Staff/Principal Level: Decode Ways
"A message containing letters A-Z can be encoded into numbers (A=1, B=2, ..., Z=26). Given a string containing only digits, return the number of ways to decode it."

---

## Interview Flow

### Phase 1: Problem Understanding (5 minutes)

**Initial Questions to Expect:**
- "Can I see some examples?"
- "What about edge cases?"
- "What's the expected time/space complexity?"

**Provide Examples:**
```typescript
// Climbing Stairs
n = 3 → Output: 3
// Explanation: 1+1+1, 1+2, 2+1

// House Robber
nums = [2,7,9,3,1] → Output: 12
// Explanation: Rob house 1 (2) + house 3 (9) + house 5 (1)

// Decode Ways
s = "226" → Output: 3
// Explanation: "BZ" (2,26), "VF" (22,6), "BBF" (2,2,6)
```

### Phase 2: Approach Discussion (10 minutes)

**Good Signs:**
- ✅ Mentions overlapping subproblems
- ✅ Identifies optimal substructure
- ✅ Starts with recursive approach
- ✅ Recognizes need for memoization

**Red Flags:**
- ❌ Jumps straight to coding
- ❌ Can't identify DP pattern
- ❌ Confuses with greedy approach
- ❌ No clear state definition

**Guiding Questions:**
- "What makes this a DP problem?"
- "What's your state definition?"
- "Can you write the recurrence relation?"
- "What are your base cases?"

### Phase 3: Implementation (20 minutes)

**Expected Progression:**

#### Step 1: Recursive Solution (5 min)
```typescript
// Candidate should start with naive recursion
function climbStairs(n: number): number {
    if (n <= 2) return n;
    return climbStairs(n - 1) + climbStairs(n - 2);
}
```

**Feedback:** "Good start. What's the time complexity? Can you optimize?"

#### Step 2: Memoization (5 min)
```typescript
// Add memoization
function climbStairs(n: number): number {
    const memo = new Map<number, number>();

    function dp(i: number): number {
        if (i <= 2) return i;
        if (memo.has(i)) return memo.get(i)!;

        const result = dp(i - 1) + dp(i - 2);
        memo.set(i, result);
        return result;
    }

    return dp(n);
}
```

**Feedback:** "Much better! Can you convert this to iterative?"

#### Step 3: Bottom-Up DP (5 min)
```typescript
// Iterative with array
function climbStairs(n: number): number {
    if (n <= 2) return n;
    const dp = [0, 1, 2];

    for (let i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n];
}
```

**Feedback:** "Great! Notice any pattern in space usage?"

#### Step 4: Space Optimization (5 min)
```typescript
// Optimize to O(1) space
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

---

## Common Mistakes & Interventions

### Mistake 1: Wrong State Definition
**Candidate:** "I'll use dp[i][j] for..."
**Intervention:** "This is a 1D problem. What single parameter defines each subproblem?"

### Mistake 2: Incorrect Base Cases
**Candidate:** Forgets to handle n=0 or n=1
**Intervention:** "What happens with very small inputs?"

### Mistake 3: Off-by-One Errors
**Candidate:** Array index issues
**Intervention:** "Walk through your indexing with n=3"

### Mistake 4: Not Testing
**Candidate:** Assumes solution works
**Intervention:** "Can you trace through an example?"

---

## Complexity Analysis (5 minutes)

**Questions to Ask:**
1. "What's the time complexity of each approach?"
2. "What's the space complexity?"
3. "Which approach would you use in production and why?"

**Expected Answers:**
- Recursive: O(2^n) time, O(n) space
- Memoized: O(n) time, O(n) space
- Bottom-up: O(n) time, O(n) space
- Optimized: O(n) time, O(1) space

---

## Follow-up Questions (5 minutes)

### For Strong Candidates:

1. **Variation:** "What if you can take 1, 2, or 3 steps?"
   - Answer: dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

2. **Harder:** "What if each step has a cost array?"
   - Answer: Min cost climbing stairs problem

3. **System Design:** "How would you handle n = 10^9?"
   - Answer: Matrix exponentiation, O(log n)

### For Struggling Candidates:

1. **Simpler:** "Can you identify the pattern in outputs?"
   - Guide toward Fibonacci recognition

2. **Hint:** "Think about the last step taken"
   - Help build recurrence relation

3. **Debug:** "Add print statements to trace execution"
   - Help identify logical errors

---

## Evaluation Rubric

### Strong Hire (4/4)
- ✅ Identifies DP immediately
- ✅ Clear state definition and recurrence
- ✅ Implements multiple approaches
- ✅ Optimizes space naturally
- ✅ Handles follow-ups well

### Hire (3/4)
- ✅ Recognizes DP with hints
- ✅ Implements memoization correctly
- ✅ Converts to bottom-up
- ⚠️ Needs prompting for optimization
- ✅ Solid complexity analysis

### Maybe (2/4)
- ⚠️ Struggles with DP recognition
- ✅ Eventually gets recursive solution
- ⚠️ Needs help with memoization
- ❌ Can't optimize space
- ⚠️ Weak complexity analysis

### No Hire (1/4)
- ❌ Can't identify DP pattern
- ❌ No clear approach
- ❌ Major implementation issues
- ❌ Poor problem-solving process
- ❌ Can't analyze complexity

---

## Post-Interview Notes

Document:
1. **Approach:** How quickly did they recognize DP?
2. **Implementation:** Code quality and correctness
3. **Optimization:** Did they optimize proactively?
4. **Communication:** How well did they explain?
5. **Debug Skills:** How did they handle bugs?

---

## Time Management Guide

- 0:00-0:02 - Introduction
- 0:02-0:07 - Problem presentation & clarification
- 0:07-0:17 - Approach discussion
- 0:17-0:37 - Implementation
- 0:37-0:42 - Complexity analysis
- 0:42-0:45 - Follow-up questions

**Remember:** Be encouraging but maintain standards. Guide struggling candidates without giving away solutions. Challenge strong candidates with harder variations.