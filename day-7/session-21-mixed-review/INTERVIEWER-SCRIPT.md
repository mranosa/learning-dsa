# Interviewer Script: Mixed Review - Hardest Blind 75

## Overview

This session tests mastery of complex algorithmic problems. These are genuinely difficult problems that require deep understanding and careful implementation.

---

## Opening (2 minutes)

**Claude:** "Welcome to Session 21, our final session! Today we're tackling the hardest problems from the Blind 75. These problems are challenging even for experienced engineers, so don't worry if they feel difficult - that's the point!

These problems combine multiple concepts and require careful thinking. We'll focus on:
- Breaking down complex problems
- Identifying the right approach
- Clean implementation despite complexity
- Thorough testing

Remember, in real interviews, solving even part of these problems well is impressive. Let's start with your choice of problem."

---

## Problem 1: Alien Dictionary (Topological Sort)

### Introduction (2 min)
"This problem asks us to determine the ordering of letters in an alien alphabet given a sorted dictionary. This is a classic topological sort problem. Can you explain your approach?"

### Clarifying Questions
- "What should we return if there's a cycle?" → Return empty string
- "What about invalid inputs like ["abc", "ab"]?" → Return empty string
- "Multiple valid orderings?" → Return any valid one

### Approach Discussion (5 min)

**Expected approaches:**
1. Build a directed graph from character dependencies
2. Topological sort (BFS with in-degrees or DFS)

**Follow-up questions:**
- "How do you extract the ordering rules from adjacent words?"
- "How do you detect if the ordering is impossible?"
- "What's the time complexity?"

### Implementation Phase (20 min)

**Watch for:**
- Correctly building the graph
- Handling edge cases (prefix words)
- Cycle detection
- Clean topological sort implementation

**If stuck:**
- "Think about what each pair of adjacent words tells you"
- "Remember to check if word2 is a prefix of word1"
- "Consider using in-degree for Kahn's algorithm"

### Testing (3 min)
"Test with these cases:"
- ["wrt","wrf","er","ett","rftt"] → "wertf"
- ["z","x"] → "zx"
- ["z","x","z"] → "" (cycle)
- ["abc","ab"] → "" (invalid)

---

## Problem 2: Serialize and Deserialize Binary Tree

### Introduction (2 min)
"Design an algorithm to serialize a binary tree to a string and deserialize it back. There's no required format - you design the encoding. How would you approach this?"

### Implementation Guidance

**If using pre-order:**
```typescript
// Serialize: "1,2,null,null,3,4,null,null,5,null,null"
// Include nulls to maintain structure
```

**Common mistakes:**
- Forgetting null markers
- Index management in deserialization
- Not handling empty trees

**Hints if stuck:**
- "Pre-order traversal processes root first - easier for deserialization"
- "Use a delimiter between values"
- "Keep track of your position when deserializing"

---

## Problem 3: Longest Increasing Path in a Matrix

### Introduction (2 min)
"Find the longest increasing path in a matrix where you can move in 4 directions. This combines DFS with dynamic programming. What's your approach?"

### Key Points
- Each cell can be the start of a path
- Memoization prevents recalculation
- No need to track visited (increasing constraint prevents cycles)

**If struggling:**
- "What if you cache the longest path from each cell?"
- "The increasing property guarantees no cycles"
- "Try DFS with memoization"

---

## Problem 4: Maximum Profit in Job Scheduling

### Introduction (2 min)
"Given jobs with start time, end time, and profit, find the maximum profit by scheduling non-overlapping jobs. This is weighted interval scheduling. How would you solve it?"

### Approach Guidance
- Sort by end time
- DP[i] = max profit using first i jobs
- Binary search for non-overlapping jobs

**Common issues:**
- Not sorting correctly
- Linear search instead of binary search
- Off-by-one in binary search

---

## Problem 5: Reverse Nodes in k-Group

### Introduction (2 min)
"Reverse every k consecutive nodes in a linked list. If the remaining nodes are less than k, leave them as is. This tests precise pointer manipulation."

### Implementation Tips
- Use dummy node
- Count nodes first
- Reverse exactly k nodes at a time
- Update connections carefully

**Watch for:**
- Correct pointer updates
- Handling last group with < k nodes
- Maintaining connections between groups

---

## Problem 6: Minimum Window Subsequence

### Introduction (2 min)
"Find the minimum window in s1 that contains s2 as a subsequence. Note: subsequence, not substring. Two-pointer approach works well here."

### Algorithm Flow
1. Forward scan to find subsequence
2. Backward scan to minimize window
3. Track minimum window
4. Continue from next position

**Key insight:** "The backward scan ensures you find the tightest window ending at the current position"

---

## Problem 7: Wildcard Matching

### Introduction (2 min)
"Implement wildcard pattern matching with '?' and '*'. This is a classic DP problem similar to regular expression matching."

### DP Table Setup
```
dp[i][j] = s[0:i] matches p[0:j]
'*' can match empty or any sequence
'?' matches exactly one character
```

**Edge cases:**
- Multiple consecutive '*'
- Pattern starting/ending with '*'
- Empty string/pattern

---

## Problem 8: Burst Balloons

### Introduction (2 min)
"Burst balloons to maximize coins. When you burst balloon i, you get nums[i-1] * nums[i] * nums[i+1] coins. This is a classic interval DP problem."

### Key Insight
"Instead of which balloon to burst first, think about which to burst last in an interval. This makes the subproblems independent."

**DP approach:**
- Add dummy balloons with value 1
- dp[left][right] = max coins in interval
- Try each balloon as last to burst

---

## Problem 9: Distinct Subsequences

### Introduction (2 min)
"Count the number of distinct subsequences of s that equal t. This is a 2D DP counting problem."

### DP Formulation
```
dp[i][j] = ways to form t[0:j] from s[0:i]
If s[i] == t[j]: can use or skip s[i]
Otherwise: must skip s[i]
```

---

## Problem 10: Basic Calculator III

### Introduction (2 min)
"Implement a calculator that handles +, -, *, /, and parentheses. This requires understanding expression parsing and operator precedence."

### Parser Structure
1. Expression: handles +/-
2. Term: handles *÷
3. Factor: handles () and numbers

**Implementation advice:**
- "Each level handles its operators and delegates higher precedence to the next level"
- "Recursion naturally handles parentheses"

---

## Common Feedback Points

### For Excellent Performance
- "Excellent problem decomposition!"
- "Great job identifying the core algorithm"
- "Clean implementation despite the complexity"
- "Good edge case handling"

### For Good Performance
- "Good approach, let's optimize further"
- "Right idea, but watch the implementation details"
- "Consider this edge case..."

### For Struggling Candidates
- "These are meant to be challenging"
- "Let's break it down further"
- "Good progress on the approach"
- "Even partial solutions show strong thinking"

---

## Session Closing (3 minutes)

**If all problems attempted:**
"Congratulations on completing the entire bootcamp! You've tackled some of the hardest interview problems. You're well-prepared for technical interviews."

**Key takeaways:**
1. Complex problems require systematic approaches
2. Start with brute force, then optimize
3. Clean code matters even more in complex problems
4. Partial solutions with good thinking are valuable

**Final advice:**
"Remember, even experienced engineers find these problems challenging. In real interviews:
- Communicate your thinking clearly
- Ask clarifying questions
- Start with simpler approaches
- Test thoroughly
- Stay calm under pressure

You've built a strong foundation. Keep practicing, and good luck with your interviews!"

---

## Scoring Rubric

### Problem Solving (40%)
- **Excellent (36-40):** Solves 8+ problems correctly
- **Good (28-35):** Solves 5-7 problems correctly
- **Satisfactory (20-27):** Solves 3-4 problems correctly
- **Needs Improvement (<20):** Solves <3 problems

### Code Quality (30%)
- **Excellent (27-30):** Clean, efficient, well-organized despite complexity
- **Good (21-26):** Mostly clean with minor issues
- **Satisfactory (15-20):** Working but messy code
- **Needs Improvement (<15):** Significant quality issues

### Communication (30%)
- **Excellent (27-30):** Clear explanation of complex concepts
- **Good (21-26):** Good communication with some gaps
- **Satisfactory (15-20):** Basic communication
- **Needs Improvement (<15):** Struggles to explain approach

---

## Final Notes

These problems are genuinely difficult. Success means:
- Understanding the approach even if implementation is incomplete
- Breaking down complex problems systematically
- Recognizing which algorithms/data structures apply
- Communicating clearly under pressure

Congratulations on completing this challenging session!