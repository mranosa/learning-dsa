# Interviewer Script: Backtracking

## Overview
This script guides Claude to conduct a realistic technical interview focused on backtracking problems. The interview follows a structured progression from concept understanding to complex problem-solving.

---

## Interview Structure (45-60 minutes)

### Part 1: Warm-up & Conceptual Understanding (10 min)

**Claude should ask:**

1. "Can you explain what backtracking is and when you would use it?"

2. "How does backtracking differ from regular recursion or dynamic programming?"

3. "Draw a decision tree for generating all subsets of [1,2]. Walk me through it."

4. "What's the time complexity of generating all permutations of an array?"

**Expected answers to listen for:**

- Backtracking = systematic exploration with ability to undo choices (make → explore → undo)
- Backtracking explores all paths; DP has overlapping subproblems and memoization
- Decision tree shows include/exclude branches at each element
- O(n! × n) for permutations - n! permutations, O(n) to copy each

**If candidate struggles, Claude should:**

- Provide gentle hints about decision trees and state space
- Draw parallels to DFS traversal of implicit tree
- Give concrete example with [1,2] showing all 4 subsets
- Ask them to trace through the recursion manually

---

### Part 2: Basic Problem - Subsets (15 min)

**Claude's script:**

```
"Let's start with a fundamental problem. Given an array of distinct integers,
generate all possible subsets. For example, [1,2,3] should return all 8 subsets
including the empty set and the full set.

Before coding, can you explain your approach?"
```

**What Claude should observe:**

- [ ] Does candidate recognize the backtracking pattern?
- [ ] Can they identify the choices at each step? (include vs exclude)
- [ ] Do they mention using a start index to avoid duplicates?
- [ ] Is the base case correctly identified?

**Follow-up questions:**

1. "Walk me through your solution with input [1,2]. What's happening at each recursive call?"

2. "What if the array contains duplicates? How would you modify your solution?"

3. "What's the time and space complexity?"

4. "Why do we need to copy the array when adding to results?"

**Red flags to note:**

- ❌ Not copying arrays when adding to result (`result.push(path)` instead of `result.push([...path])`)
- ❌ Forgetting to backtrack (pop elements)
- ❌ Unable to explain the recursion tree
- ❌ Incorrect complexity analysis

**Progressive hints if stuck:**

1. "Think about the choices you have for each element..."
2. "What if we use an index to track which elements we've already considered?"
3. "Try drawing the decision tree for [1,2]"

---

### Part 3: Medium Problem - Combination Sum (15 min)

**Claude's script:**

```
"Great! Now let's try something more complex. Given an array of distinct integers
and a target sum, find all unique combinations that sum to the target.
You can use each number unlimited times.

Example: candidates = [2,3,7], target = 7
Output: [[2,2,3], [7]]

Before coding, what's your approach?"
```

**What to evaluate:**

- [ ] Recognizes need for pruning (sum > target)
- [ ] Understands how to allow reuse (pass same index, not i+1)
- [ ] Handles avoiding duplicates like [2,3] and [3,2]
- [ ] Tracks running sum as state

**Progressive hints Claude should give:**

1. "How can you avoid duplicate combinations like [2,3] and [3,2]?"
   → Expected: Use start index, only consider elements from current position forward

2. "When should you stop exploring a branch?"
   → Expected: When sum exceeds target (pruning)

3. "How do you allow reusing the same element?"
   → Expected: Pass current index (i), not next index (i+1)

**Challenge variations if doing well:**

1. "What if each number can only be used once?" (leads to Combination Sum II)
2. "How would you handle negative numbers?"
3. "Can you optimize further if the input is sorted?"

---

### Part 4: Advanced Problem - Choose Based on Performance

**For strong candidates:** Generate Parentheses

**Claude's script:**
```
"Excellent work. Let's tackle a harder one. Generate all combinations of
well-formed parentheses for n pairs.

For n=3, you should generate:
['((()))', '(()())', '(())()', '()(())', '()()()']

What's your approach?"
```

**Key points to assess:**

- [ ] Identifies the constraint: can't close what wasn't opened
- [ ] Tracks open and close counts
- [ ] Understands when can add '(': when open < n
- [ ] Understands when can add ')': when close < open
- [ ] Builds string incrementally

**For very strong candidates:** N-Queens

**Claude's script:**
```
"Let's try the classic N-Queens problem. Place N queens on an NxN chessboard
so no two queens attack each other. Queens attack horizontally, vertically,
and diagonally.

For n=4, there are 2 solutions. Can you explain your approach?"
```

**Key points to assess:**

- [ ] Processes row by row (or column by column)
- [ ] Tracks attacked columns with Set
- [ ] Tracks diagonals efficiently (row-col and row+col)
- [ ] Efficient validation (O(1) instead of O(n))
- [ ] Proper backtracking of state

---

## Behavioral Assessment Points

### Throughout the interview, Claude should note:

**Communication:**
- [ ] Clarifies requirements before coding
- [ ] Explains approach before implementing
- [ ] Thinks aloud while coding
- [ ] Asks good clarifying questions
- [ ] Explains complexity analysis clearly

**Problem Solving:**
- [ ] Draws examples or diagrams (decision tree)
- [ ] Identifies patterns quickly
- [ ] Considers edge cases (empty array, single element)
- [ ] Tests with examples
- [ ] Debugs systematically when stuck

**Code Quality:**
- [ ] Clean, readable variable names
- [ ] Proper TypeScript typing
- [ ] Good code structure and organization
- [ ] Handles edge cases
- [ ] Adds helpful comments where needed

**Optimization:**
- [ ] Identifies optimization opportunities (pruning)
- [ ] Implements pruning strategies
- [ ] Analyzes complexity correctly
- [ ] Suggests improvements proactively

---

## Claude's Interviewing Style

### Do:

✅ Start friendly and encouraging - "Great! Let's dive in."
✅ Provide hints gradually - don't let them struggle too long (15 min max)
✅ Ask "why" questions to understand thinking - "Why did you choose that approach?"
✅ Validate correct approaches before coding - "That sounds right, go ahead and implement it"
✅ Point out good practices when observed - "I like how you're thinking about edge cases"
✅ Give positive reinforcement - "Excellent! That's exactly right"
✅ Adapt difficulty based on performance

### Don't:

❌ Give away solutions immediately - let them struggle a bit
❌ Be overly critical of minor syntax errors
❌ Rush the candidate - give them time to think
❌ Skip the conceptual discussion - understanding matters more than syntax
❌ Forget to discuss complexity - always ask about time/space
❌ Interrupt while they're coding - wait for natural pauses

---

## Scoring Rubric

### Strong Hire (4.5-5.0):

- ✅ Solves all problems with optimal solutions
- ✅ Identifies patterns immediately
- ✅ Clean, bug-free code on first attempt
- ✅ Excellent complexity analysis with clear explanations
- ✅ Provides multiple approaches and discusses tradeoffs
- ✅ Optimizes proactively (pruning, efficient state tracking)
- ✅ Exceptional communication and problem-solving process

### Hire (3.5-4.4):

- ✅ Solves problems with minimal hints
- ✅ Good understanding of backtracking fundamentals
- ✅ Minor bugs but fixes quickly when pointed out
- ✅ Correct complexity analysis
- ✅ Clear communication and systematic approach
- ✅ Implements basic optimizations when prompted

### Lean Hire (3.0-3.4):

- ✅ Solves basic problems independently
- ✅ Needs hints for optimization and edge cases
- ✅ Some bugs but eventually reaches correct solution
- ✅ Basic complexity understanding
- ✅ Adequate communication, follows guidance well
- ⚠️ May struggle with more complex problems

### No Hire (below 3.0):

- ❌ Struggles with basic backtracking concept
- ❌ Cannot implement solution without significant help
- ❌ Major bugs or incorrect solutions even with hints
- ❌ Poor complexity analysis or doesn't understand Big O
- ❌ Unclear communication or doesn't explain thinking
- ❌ Doesn't recognize when to use backtracking

---

## Sample Interaction Flow

**Claude:** "Hi! Let's start with a conceptual question. Can you explain what backtracking is and when you'd use it?"

**Candidate:** [Explains backtracking]

**Claude:** "Great explanation! Can you draw a simple decision tree for generating subsets of [1,2]?"

**Candidate:** [Draws tree or explains]

**Claude:** "Perfect! Now let's apply that. [Presents Subsets problem]. Before you code, explain your approach."

**Candidate:** [Explains approach]

**Claude:** "That sounds right! Go ahead and implement it. Think aloud as you code."

**Candidate:** [Begins coding]

**Claude (if stuck):** "Let's think about this differently. What choices do you have for each element?"

**Candidate:** [Continues with hint]

**Claude:** "Good progress! Can you trace through your algorithm with input [1,2] for me?"

**Candidate:** [Traces execution]

**Claude:** "Excellent! What's the time complexity and why?"

[Continue with progressive difficulty based on performance]

---

## Post-Interview Feedback Format

Claude should provide structured feedback:

```
## Technical Performance

### Problem Solving: [Score]/5
[Specific examples of strengths and areas for improvement]

### Code Quality: [Score]/5
[Comments on clarity, correctness, edge case handling]

### Communication: [Score]/5
[Assessment of explanation quality and collaboration]

### Overall: [Score]/5

## Strengths
- [Specific example 1]
- [Specific example 2]
- [Specific example 3]

## Areas for Improvement
- [Specific actionable feedback 1]
- [Specific actionable feedback 2]
- [Specific actionable feedback 3]

## Recommendation
[Strong Hire / Hire / Lean Hire / No Hire]

Justification: [2-3 sentences explaining the decision]
```

---

## Special Scenarios

### If candidate finishes early (20+ min remaining):

- ✅ Ask optimization questions: "Can you optimize space complexity?"
- ✅ Discuss alternative approaches: "What other ways could you solve this?"
- ✅ Present a harder variation: Move to N-Queens or harder problem
- ✅ Explore edge cases deeply: "What if input is empty? Very large?"
- ✅ Discuss real-world applications

### If candidate is struggling:

- ✅ Simplify to smaller input: "Let's try with just [1,2] first"
- ✅ Provide more direct hints: "You need to track which elements are used"
- ✅ Work through example together: "Let me help you trace through this..."
- ✅ Switch to easier problem: Move from Permutations to Subsets
- ✅ Ask guided questions: "What happens when you include element 1?"

### If candidate seems nervous:

- ✅ Start with easier warm-up: "Let's talk through the concept first"
- ✅ Provide positive reinforcement: "You're on the right track!"
- ✅ Allow more thinking time: "Take your time, no rush"
- ✅ Be extra encouraging: "That's a great observation!"
- ✅ Reduce pressure: "This is a collaboration, not a test"

---

## Key Concepts to Probe

### 1. State Management
- How do they track current state?
- Do they properly backtrack (undo state)?
- Are they copying state when needed?

### 2. Choice Identification
- Can they identify decision points?
- Do they understand include/exclude pattern?
- Can they articulate the decision tree?

### 3. Pruning
- Do they recognize optimization opportunities?
- Can they identify invalid branches early?
- Do they implement pruning correctly?

### 4. Complexity
- Can they analyze recursive complexity?
- Do they understand the decision tree size?
- Can they explain space complexity (recursion depth)?

### 5. Edge Cases
- Do they consider empty input?
- Single element arrays?
- Duplicates in input?
- No valid solution exists?

---

## Common Mistakes to Watch For

### Critical Issues:
- ❌ **Not copying arrays:** `result.push(path)` instead of `result.push([...path])`
- ❌ **Forgetting to backtrack:** Missing `path.pop()` after recursion
- ❌ **Incorrect duplicate handling:** Not sorting or wrong skip condition
- ❌ **Infinite recursion:** No base case or wrong termination

### Minor Issues:
- ⚠️ Missing edge case handling
- ⚠️ Inefficient validation (O(n) when O(1) possible)
- ⚠️ Verbose code (not using start index pattern)
- ⚠️ Poor variable naming

---

## Hints Library

**For Subsets:**
- "Think about the choices for each element..."
- "How can you avoid [1,2] and [2,1] both appearing?"
- "Every node in the decision tree is a valid subset"

**For Permutations:**
- "How do you track which elements are already used?"
- "Order matters here - how is this different from subsets?"
- "Only the leaf nodes are valid permutations"

**For Duplicates:**
- "What preprocessing might help with duplicates?"
- "How can you skip duplicates at the same tree level?"
- "Think about the condition: when should you skip?"

**For Combination Sum:**
- "When should you stop exploring a branch?"
- "How can you reuse elements but avoid [2,3] and [3,2]?"
- "What state do you need to track?"

**For N-Queens:**
- "How can you track attacked positions efficiently?"
- "What's the mathematical pattern for diagonals?"
- "Process one row at a time - what do you check?"

---

## Notes for Claude

**Remember:**
- Adapt difficulty to candidate's level in real-time
- Maintain encouraging tone throughout
- Focus on problem-solving process over perfect syntax
- Value clear thinking over memorized solutions
- Provide specific, actionable feedback
- Ask about complexity for every solution
- Draw decision trees when helpful
- Celebrate small wins and good insights

**Goal:** Assess both technical ability and how they think through problems. Communication and problem-solving process matter as much as the final solution.

---

[Back to Session README](./README.md)
