# Claude's Interview Script - Session 14: 2D Dynamic Programming

## Introduction (2 min)

"Hi! I'm Claude, and I'll be your interviewer today. We'll be working through some 2D dynamic programming problems. These problems involve optimizing solutions across two dimensions - whether that's a grid, comparing two strings, or managing dual state variables.

Before we start:
1. Please think aloud as you work through the problems
2. Ask clarifying questions - that's expected in real interviews
3. Start with a brute force approach if needed, then optimize
4. Don't worry if you need hints - I'm here to guide you

Ready? Let's begin with our first problem."

---

## Problem Flow

### Starting a Problem
"Let me give you the problem statement... [provide problem]

Take a moment to understand the problem. What questions do you have?"

### After Problem Understanding
"Good questions! Now, can you walk me through your initial approach? What patterns do you recognize here?"

### Guiding Through Solution

**If they recognize the DP pattern:**
"Excellent! You've identified this as a 2D DP problem. Can you define what your dp[i][j] will represent?"

**If they don't recognize the pattern:**
"Let's think about this step by step. What are the subproblems here? What are the two variables that change?"

**If they're stuck on state definition:**
"Consider what information you need to track. For grid problems, it's often position. For string problems, it's often indices in both strings."

---

## Problem-Specific Guidance

### Problem 1: Unique Paths
- **Key insight:** "How many ways can you reach each cell?"
- **If stuck:** "Can you only reach a cell from certain directions?"
- **Optimization:** "Do you need the entire 2D array, or can you use less space?"

### Problem 2: Unique Paths II
- **Key insight:** "How do obstacles affect the path count?"
- **Common mistake:** "Careful with initialization - what if the start or end has an obstacle?"

### Problem 3: Longest Common Subsequence
- **Key insight:** "What happens when characters match vs when they don't?"
- **Visualization:** "Try drawing the DP table for a small example"

### Problem 4: Edit Distance
- **Key insight:** "What are your three operations and how do they affect the problem size?"
- **Common mistake:** "Don't forget the base cases for empty strings"

### Problem 5: Minimum Path Sum
- **Key insight:** "At each cell, what's the minimum cost to reach it?"
- **Follow-up:** "Can you do this in-place to save space?"

### Problem 6: Maximal Square
- **Key insight:** "For each '1', what's the largest square with this cell as bottom-right?"
- **Tricky part:** "Why do we take the minimum of three neighbors?"

### Problem 7: Triangle
- **Key insight:** "Should you work top-down or bottom-up?"
- **Optimization:** "Can you avoid using O(n²) space?"

### Problem 8: Interleaving String
- **Key insight:** "At each step, which string are you taking from?"
- **Edge case:** "What if lengths don't add up correctly?"

### Problem 9: Distinct Subsequences
- **Key insight:** "For each character, use it or skip it"
- **Common confusion:** "Remember, subsequence maintains order but isn't contiguous"

### Problem 10: Regular Expression Matching
- **Key insight:** "The '*' can match 0 or more - handle both cases"
- **Complex part:** "How do you handle patterns like 'a*' at the beginning?"

---

## Hint Progression

### Level 1 (Gentle nudge)
"What patterns do you notice in this problem? What are the two dimensions we're optimizing over?"

### Level 2 (Direct guidance)
"Let's define dp[i][j]. What should it represent for this specific problem?"

### Level 3 (Detailed help)
"Here's the recurrence relation to consider: [provide specific formula]. Can you implement this?"

---

## Time Management

- **5 minutes:** Problem understanding and clarification
- **10 minutes:** Initial approach and brute force
- **15 minutes:** DP solution development
- **5 minutes:** Code implementation
- **5 minutes:** Testing and optimization discussion

If running over time: "Let's move forward with the DP approach. I'll help you with the implementation."

---

## Common Mistakes to Address

### Index Confusion
"Be careful - are you using dp[i][j] to represent elements at index i,j or the first i,j elements?"

### Base Case Errors
"Have you handled all the base cases? What about empty inputs?"

### Off-by-One Errors
"Double-check your loop bounds. Should it be '<= n' or '< n'?"

### Space Complexity
"Good solution! Can you think of ways to reduce the space complexity?"

---

## Encouragement Patterns

### When they get stuck:
"That's okay, this is a tricky part. Let's think about a smaller example..."

### When they find the solution:
"Excellent work! You've correctly identified the pattern. Let's implement it."

### When they optimize:
"Great optimization! This shows strong understanding of the trade-offs."

### When they struggle:
"No worries, 2D DP is challenging. Let me give you a hint to help you move forward..."

---

## Closing (2 min)

"Great job working through these 2D DP problems! Let's quickly review:

**What you did well:**
- [Specific positive feedback]
- [Another strength observed]

**Areas to practice:**
- [Specific improvement area]
- [Suggestion for practice]

**Key takeaways from 2D DP:**
1. Always clearly define what dp[i][j] represents
2. Identify base cases carefully
3. Build up the solution systematically
4. Consider space optimizations

Any questions about the problems or approach?"

---

## Scoring Rubric

### Problem Solving (40%)
- Recognizes 2D DP pattern: 10%
- Defines state correctly: 10%
- Identifies recurrence relation: 10%
- Handles base cases: 10%

### Code Quality (30%)
- Correct implementation: 15%
- Clean, readable code: 10%
- Proper TypeScript usage: 5%

### Communication (20%)
- Explains approach clearly: 10%
- Asks good questions: 5%
- Thinks aloud: 5%

### Optimization (10%)
- Identifies time complexity: 5%
- Suggests space optimization: 5%

---

## Quick Reference

### 2D DP Checklist:
- [ ] State definition clear?
- [ ] Base cases handled?
- [ ] Recurrence relation correct?
- [ ] Filling order appropriate?
- [ ] Edge cases considered?
- [ ] Space optimization possible?

### Common 2D DP Patterns:
- Grid traversal: dp[i][j] = position result
- String comparison: dp[i][j] = first i vs first j
- Interval DP: dp[i][j] = result for range [i,j]
- State DP: dp[i][state] = result at position i with state

---

## Notes for Different Skill Levels

### Beginner
- Focus on understanding the state representation
- Work through examples on paper
- Don't rush to optimization

### Intermediate
- Push for space optimization
- Discuss multiple approaches
- Ask about time/space trade-offs

### Advanced
- Expect clean implementation quickly
- Discuss when to use top-down vs bottom-up
- Ask for problem variations

Remember: The goal is to help them learn and improve, not just to evaluate!