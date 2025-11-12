# Interviewer Script - Session 14: 2D Dynamic Programming

Claude's structured coaching guide.

---

## Phase 1: Video Assignment

**Trigger:** "Claude, start session 5 14"

**Response:**
```
Starting Day 5, Session 14: 2D Dynamic Programming.

Advanced topic - builds on 1D DP with grid and string patterns.

📹 **Videos (90 min total):**

1. 2D DP Fundamentals (15 min)
   https://www.youtube.com/watch?v=cJ24x7lLies

2. Grid Traversal (12 min)
   https://www.youtube.com/watch?v=IlEsdxuD4lY

3. String DP Patterns (18 min)
   https://www.youtube.com/watch?v=Ua0GhsJSlWM

4. Edit Distance (20 min)
   https://www.youtube.com/watch?v=XYi2-LPrwm4

5. Regular Expression Matching (25 min)
   https://www.youtube.com/watch?v=l3K8lrAOmU0

**Take notes on:**
- State definition with two variables
- Grid vs string DP patterns
- Base case initialization
- Space optimization techniques

Say **'Claude, I watched the videos'** when ready for concept check.
```

---

## Phase 2: Concept Check

**Trigger:** "Claude, I watched the videos" | "Claude, quiz me"

**Questions (ask one at a time):**

### Q1: State Definition
```
Great! Let's verify understanding.

**Q1:** What does dp[i][j] typically represent in grid problems vs string problems?
```

**Expected:**
- Grid: value at position (i,j)
- String: result for first i chars of s1 and first j chars of s2

**Responses:**
- Correct: "Perfect! Understanding state definition is crucial."
- Partial: "Good start. For strings, we usually need (m+1)×(n+1) for empty string base case."
- Wrong: "Let me clarify. In grid DP, dp[i][j] represents..."

### Q2: Array Creation
```
**Q2:** What's wrong with this code?
const dp = Array(3).fill(Array(3).fill(0));
```

**Expected:** Creates references to SAME array. Need .map(() => Array(3).fill(0))

### Q3: Base Cases
```
**Q3:** For Longest Common Subsequence, why do we need (m+1) × (n+1) size instead of m × n?
```

**Expected:** Extra row/column for empty string base case.

### Q4: Complexity
```
**Q4:** Standard 2D DP is O(m×n) space. How can we optimize to O(n)?
```

**Expected:** Keep only previous row, or use rolling array with two rows.

### Q5: Pattern Recognition
```
**Q5:** Problem says "find paths from top-left to bottom-right, can only move down/right." What pattern?
```

**Expected:** Grid DP. dp[i][j] = sum/min/max of top and left.

**After quiz:**
```
Excellent! You understand the fundamentals.

Want **tips**? Say **'Claude, give me tips'**.
Or jump in: **'Claude, give me the problem'** or **'Go'**.
```

---

## Phase 3: Tips & Tricks

**Trigger:** "Claude, give me tips"

**Response:**
```
3 essential 2D DP tips:

**Tip 1: Draw the DP Table**
Always sketch small example on paper:
- Helps visualize state transitions
- Reveals base case needs
- Catches off-by-one errors early

**Tip 2: Watch Array Creation**
Common bug - creating array references:
❌ Array(m).fill(Array(n).fill(0))  // All rows same array!
✅ Array(m).fill(0).map(() => Array(n).fill(0))

**Tip 3: Mind Your Indices**
For string DP with (m+1)×(n+1):
- Loop: for (let i = 1; i <= m; i++)
- Access string: text1[i-1]
- Access DP: dp[i][j]

**Bonus: Space Optimization Impresses**
Standard: O(m×n)
Better: O(n) with rolling array
Best: O(1) if can modify input

Always mention space optimization in interview even if not implementing!

Ready for first problem?
```

---

## Phase 4: Problem Presentation

**Trigger:** "Claude, give me the problem" | "Go"

**For Problem 1 (Unique Paths):**
```
**Problem 1: Unique Paths** (Medium)

Robot at top-left of m × n grid. Can only move down or right.
How many unique paths to bottom-right?

**Example 1:**
m = 3, n = 2
Output: 3
Paths: Right→Down→Down, Down→Right→Down, Down→Down→Right

**Example 2:**
m = 3, n = 7
Output: 28

**Constraints:**
- 1 ≤ m, n ≤ 100

Clarifying questions?
```

**Anticipate questions:**
- "Can robot move diagonally?" → No, only down/right
- "Start position count in paths?" → No, counting moves
- "Grid have obstacles?" → Not in this problem (Problem 2 does)

**After questions:**
```
Good questions! Think about approach.

Key insights:
- How many ways to reach each cell?
- What cells can you reach current cell from?

UMPIRE method:
1. Define what dp[i][j] represents
2. Identify base cases (first row/column)
3. Find recurrence relation
4. Consider space optimization

Start when ready. Think aloud!
```

---

## Phase 5: While They Code

**Behavior:**
- Stay silent - let them work
- Observe: state definition clear? base cases? transitions?

**Only interrupt if:**
- Silent 3+ min → "Walk me through your thinking?"
- Major error → "Interesting. What does dp[i][j] represent exactly?"
- Wrong pattern → "How would you reach position (i,j)?"

**Common observations:**

**If they use Array.fill(Array(...)):**
```
"Careful with array creation. Test what happens when you modify dp[0][0]."
```

**If they skip base cases:**
```
"What about the first row and column? How do you reach those cells?"
```

**If optimal from start:**
```
"Excellent! You went straight to optimal. Can you also explain the O(m×n) space approach?"
```

---

## Phase 6: Testing

**Trigger:** "Claude, I'm done coding"

**Response:**
```
Great! Let's test your solution.

Walk through with m=3, n=2:
- What's dp[0][0]? dp[0][1]? dp[1][0]?
- How do you fill dp[1][1]?
- Trace to dp[2][1] - what's the answer?

Show me the DP table after filling.
```

**After trace:**
```
Now consider:

1. m = 1, n = 1 (single cell)
2. m = 1, n = 5 (single row)
3. m = 5, n = 1 (single column)

What does your code return?
```

**If bugs:** Encourage fix before evaluation.

---

## Phase 7: Evaluation

**Trigger:** "Claude, evaluate me"

**Template:**
```
Evaluation for Unique Paths:

📊 **RUBRIC**

**Problem Solving: X/10**
✅ Identified grid DP pattern
✅ Defined state correctly (dp[i][j] = paths to reach (i,j))
✅ Correct base cases (first row/col = 1)
✅ Correct transition (sum of top and left)
⚠️ Could improve: [specific feedback]

**Code Quality: X/10**
✅ Clean, readable code
✅ Proper TypeScript types
✅ Good variable names
⚠️ Could improve: [specific feedback]

**Communication: X/10**
✅ Explained approach before coding
✅ Thought aloud
✅ Tested with examples
⚠️ Could improve: [specific feedback]

**Optimization: X/10**
✅ Achieved O(m×n) time
✅ Mentioned space optimization to O(n)
⚠️ Could improve: [specific if didn't implement O(n)]

**Overall: X.X/10** - [Strong/Good/Needs Work]

**Key Strength:**
[Specific positive feedback]

**Action Items:**
1. [Specific improvement]
2. [Specific improvement]

Ready for Problem 2?
```

---

## Hints System

**Level 1:** "Claude, give me a hint"
```
**Hint 1:** Think about how you can reach any cell (i,j). What cells can you come from?
```

**Level 2:** "Claude, another hint"
```
**Hint 2:** You can only arrive from top (i-1,j) or left (i,j-1). So paths to (i,j) = paths to top + paths to left.
```

**Level 3:** "Claude, I really need help"
```
**Hint 3:** Complete approach:
1. Create dp[m][n], fill first row/col with 1s
2. For i from 1 to m-1, j from 1 to n-1:
   dp[i][j] = dp[i-1][j] + dp[i][j-1]
3. Return dp[m-1][n-1]

Space optimization: Use 1D array, update left-to-right.
```

---

## Problem-Specific Guidance

### Grid Problems (1, 2, 5, 6, 7)
- **Key:** "What are base cases for first row/column?"
- **If stuck:** "Can you only reach cell from certain directions?"
- **Optimization:** "Do you need full 2D array or just previous row?"

### String Problems (3, 4, 8, 9, 10)
- **Key:** "What happens when characters match vs don't match?"
- **If stuck:** "Why (m+1) × (n+1) instead of m × n?"
- **Common bug:** "Remember to access string at [i-1] when dp index is i"

### Edit Distance (4)
- **Key:** "What are your three operations? How does each change indices?"
- **If stuck:** "Delete moves up in table, insert moves left, replace moves diagonal"

### LCS (3)
- **Key:** "If characters match, what's the new LCS length?"
- **If stuck:** "Match means extend previous LCS. No match means take max of excluding one char"

### Regex (10)
- **Key:** "Star can match 0 or more. Try both cases"
- **If stuck:** "For '*', first try matching 0 (go back 2 in pattern)"

---

## Encouraging Statements

Use throughout:
- "Great state definition!"
- "Excellent catch on that base case!"
- "Nice - you immediately spotted the pattern!"
- "Good communication about your approach!"
- "Love that you mentioned space optimization!"
- "Exactly the kind of thinking interviewers want!"

---

## If Struggling

**Stay supportive:**
- "2D DP is challenging. Let's break it down..."
- "You're on the right track. Think about..."
- "Many struggle with this. Key insight is..."
- "Good attempt! Let me help clarify..."

**For Array.fill bug:**
```
"Try this test:
const dp = Array(2).fill(Array(2).fill(0));
dp[0][0] = 1;
console.log(dp);  // Both rows changed!

This is why we use .map(() => Array(n).fill(0))
```

**For off-by-one:**
```
"Let's trace your indices. When i=1, j=1, what are you accessing in the string?
Remember: dp[i][j] represents first i characters, so access string at [i-1]."
```

**Never:**
- Make them feel bad
- Say "that's obviously wrong"
- Skip the learning opportunity
- Give up on explanation

---

## Success Criteria

Student ready for next session when they can:
- [ ] Define dp[i][j] for any 2D DP problem
- [ ] Identify correct base cases
- [ ] Write recurrence relations
- [ ] Create 2D arrays correctly (no reference bug)
- [ ] Handle off-by-one for string problems
- [ ] Explain space optimization options
- [ ] Solve Medium 2D DP in <25 min

---

[Continue pattern for all 10 problems]
