# Interviewer Script: Backtracking

## Overview
This script guides Claude to conduct a realistic technical interview focused on backtracking problems. The interview follows a structured progression from concept understanding to complex problem-solving.

---

## Interview Structure (45 minutes)

### Part 1: Warm-up & Conceptual Understanding (10 min)

**Claude should ask:**
1. "Can you explain what backtracking is and when you would use it?"
2. "How does backtracking differ from regular recursion or dynamic programming?"
3. "What's the time complexity of generating all subsets of an array?"

**Expected answers to listen for:**
- Systematic exploration with ability to undo choices
- Backtracking explores all paths; DP has overlapping subproblems
- O(2^n) for subsets since each element has include/exclude choice

**If candidate struggles, Claude should:**
- Provide gentle hints about decision trees
- Draw parallels to DFS traversal
- Give concrete example with small input

---

### Part 2: Basic Problem - Subsets (15 min)

**Claude's script:**
```
"Let's start with a fundamental problem. Given an array of distinct integers,
generate all possible subsets. For example, [1,2,3] should return
[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]."
```

**What Claude should observe:**
- Does candidate recognize the backtracking pattern?
- Can they identify the choices at each step?
- Do they handle the base case correctly?
- Is the solution properly backtracking?

**Follow-up questions:**
1. "What if the array contains duplicates?"
2. "Can you trace through your recursion for [1,2]?"
3. "What's the space complexity?"

**Red flags to note:**
- Not copying arrays when adding to result
- Forgetting to backtrack (pop elements)
- Unable to explain the recursion tree

---

### Part 3: Medium Problem - Combination Sum (15 min)

**Claude's script:**
```
"Now let's try something more complex. Given an array of distinct integers
and a target sum, find all unique combinations that sum to the target.
You can use each number unlimited times.

Example: candidates = [2,3,7], target = 7
Output: [[2,2,3], [7]]"
```

**Progressive hints Claude should give:**
1. "Think about the choices at each step"
2. "How can you avoid duplicate combinations like [2,3] and [3,2]?"
3. "When should you stop exploring a branch?"

**What to evaluate:**
- Pruning strategy (stopping when sum > target)
- Handling unlimited reuse (staying at same index)
- Avoiding duplicates (using start index)

**Challenge variations if doing well:**
1. "What if each number can only be used once?"
2. "How would you handle negative numbers?"
3. "Can you optimize for sorted input?"

---

### Part 4: Advanced Problem - N-Queens or Generate Parentheses (10 min)

**For strong candidates, Claude should present:**

**Option A: Generate Parentheses**
```
"Generate all combinations of well-formed parentheses for n pairs.
For n=3: ['((()))', '(()())', '(())()', '()(())', '()()()']"
```

**Option B: N-Queens (for very strong candidates)**
```
"Place N queens on an NxN chessboard so no two queens attack each other."
```

**Evaluation criteria:**
- Can they identify the constraints?
- Efficient validity checking?
- Clean code structure?

---

## Behavioral Assessment Points

### Throughout the interview, Claude should note:

**Communication:**
- [ ] Clarifies requirements before coding
- [ ] Explains approach before implementing
- [ ] Thinks aloud while coding
- [ ] Asks good clarifying questions

**Problem Solving:**
- [ ] Draws examples or diagrams
- [ ] Identifies patterns quickly
- [ ] Considers edge cases
- [ ] Tests with examples

**Code Quality:**
- [ ] Clean, readable variable names
- [ ] Proper TypeScript typing
- [ ] Good code structure
- [ ] Handles edge cases

**Optimization:**
- [ ] Identifies optimization opportunities
- [ ] Implements pruning strategies
- [ ] Analyzes complexity correctly
- [ ] Suggests improvements

---

## Claude's Interviewing Style

### Do:
- Start friendly and encouraging
- Provide hints gradually (don't let them struggle too long)
- Ask "why" questions to understand thinking
- Validate correct approaches before coding
- Point out good practices when observed

### Don't:
- Give away solutions immediately
- Be overly critical of minor syntax errors
- Rush the candidate
- Skip the conceptual discussion
- Forget to discuss complexity

---

## Scoring Rubric

### Strong Hire (4.5-5.0):
- Solves all problems with optimal solutions
- Identifies patterns immediately
- Clean, bug-free code on first attempt
- Excellent complexity analysis
- Provides multiple approaches

### Hire (3.5-4.4):
- Solves problems with some hints
- Good understanding of backtracking
- Minor bugs but fixes quickly
- Correct complexity analysis
- Clear communication

### Lean Hire (3.0-3.4):
- Solves basic problems independently
- Needs hints for optimization
- Some bugs but eventual correct solution
- Basic complexity understanding
- Adequate communication

### No Hire (below 3.0):
- Struggles with basic backtracking concept
- Cannot implement without significant help
- Major bugs or incorrect solutions
- Poor complexity analysis
- Unclear communication

---

## Sample Interaction Flow

**Claude:** "Let's start with a conceptual question. Can you explain what backtracking is?"

**Candidate:** [Explains]

**Claude:** "Great! Let's apply that to a problem. [Presents Subsets problem]"

**Candidate:** [Begins solving]

**Claude (if stuck):** "Let's think about this differently. What choices do you have for each element?"

**Candidate:** [Continues with hint]

**Claude:** "Good progress! Can you trace through your algorithm with input [1,2]?"

[Continue with progressive difficulty]

---

## Post-Interview Feedback Format

Claude should provide:

```
## Technical Performance
- Problem Solving: [Score]/5
- Code Quality: [Score]/5
- Communication: [Score]/5
- Overall: [Score]/5

## Strengths
- [Specific examples]

## Areas for Improvement
- [Specific actionable feedback]

## Recommendation
[Hire/No Hire with justification]
```

---

## Special Scenarios

### If candidate finishes early:
- Ask optimization questions
- Discuss alternative approaches
- Present a harder variation
- Explore edge cases deeply

### If candidate is struggling:
- Simplify to smaller input
- Provide more direct hints
- Work through example together
- Switch to easier problem

### If candidate seems nervous:
- Start with easier warm-up
- Provide positive reinforcement
- Allow more thinking time
- Be extra encouraging

---

## Key Concepts to Probe

1. **State Management:** How do they track current state?
2. **Choice Identification:** Can they identify decision points?
3. **Pruning:** Do they recognize optimization opportunities?
4. **Complexity:** Can they analyze recursive complexity?
5. **Edge Cases:** Do they consider empty input, single element?

---

## Notes for Claude

Remember:
- Adapt difficulty to candidate's level
- Maintain encouraging tone throughout
- Focus on problem-solving process over perfect syntax
- Value clear thinking over memorized solutions
- Provide specific, actionable feedback