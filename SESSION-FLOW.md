# Interactive Session Flow Guide

How each interactive interview session works from start to finish.

---

## Session Overview

Each session follows a **6-phase structure** designed to simulate real interview conditions while maximizing learning.

**Total Time:** ~2-4 hours per session
- Video: 15-30 min
- Concept Check: 10 min
- Tips: 5 min
- Problems: 10 problems × 15-45 min each
- Reviews: 5 min × 10 problems

---

## The 6 Phases

### Phase 1: Video Assignment (5-30 min)

**Your Action:**
```
"Claude, start session [day] [session]"
```

**My Response:**
```
"Starting Day 1, Session 1: Big O & Arrays.

📹 Watch this video first:
- Title: "Big O Notation - Full Course" by NeetCode
- Length: 20 minutes
- Link: https://www.youtube.com/watch?v=...

This covers:
- What is Big O notation
- Common time complexities (O(1), O(n), O(n²), O(log n))
- Space complexity
- How to analyze algorithms

Say 'Claude, I watched the video' when ready."
```

**What Happens:**
- I load session context from `SESSION-STATE.json`
- Review your previous performance
- Assign curated video (15-30 min)
- Video link is in session's `LESSON.md`

**Your Task:**
- Watch the video (on or off stream)
- Take notes if helpful
- Return when ready

---

### Phase 2: Concept Check (5-10 min)

**Your Action:**
```
"Claude, I watched the video"
```

**My Response:**
```
"Great! Let's verify your understanding with a quick quiz.

Question 1: Explain Big O notation in your own words. What does O(n) mean?
"
```

**What Happens:**
- I quiz you on 3-5 key concepts
- Tests understanding before coding
- I correct misconceptions immediately
- Ensures you have foundation

**Example Questions:**
```
Q1: "What's the time complexity of accessing an array element by index?"
Q2: "If an algorithm has nested loops over n elements, what's the time complexity?"
Q3: "What's the difference between time and space complexity?"
```

**How to Answer:**
- Explain in your own words (not memorized)
- Think aloud through reasoning
- It's okay to be unsure - I'll teach you!

**My Feedback:**
```
"Good explanation! You understand that O(n) means linear time.

Small correction: You said 'it doubles when input doubles' - actually,
it grows proportionally. If input doubles from 10→20, time also doubles
from 10→20 operations.

Let's move on!"
```

---

### Phase 3: Tips & Tricks (5 min)

**Your Action:**
```
"Claude, give me tips"
```

**My Response:**
```
"Here are 3 essential tips for Hash Maps:

Tip 1: Pattern Recognition
When you hear 'find pair' or 'check if exists', think hash map immediately.
O(1) lookup is the key advantage.

Tip 2: TypeScript Gotcha
Use `new Map()` not `{}` objects. Maps can have any type as key, objects
convert everything to strings.
❌ obj[1] and obj["1"] are the same
✅ map.set(1, ...) and map.set("1", ...) are different

Tip 3: Interview Communication
Always mention 'trading space for time' when using hash maps. Shows you
understand the O(n) space trade-off for O(1) lookup.

Ready to apply these tips in problems?"
```

**What This Covers:**
- Non-obvious insights
- Common mistakes to avoid
- TypeScript-specific gotchas
- Interview communication tips
- Patterns to watch for

**When to Use:**
- After concept check (recommended)
- Before starting first problem
- Any time you need refresher

---

### Phase 4: Problem Solving (30-45 min per problem)

This is the main phase where you solve 10 problems using UMPIRE method.

#### Step 4.1: Problem Presentation

**Your Action:**
```
"Claude, give me the problem"  (or just "Go")
```

**My Response:**
```
"Here's your problem: Two Sum (Easy)

Given an array of integers `nums` and an integer `target`, return
indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and
you may not use the same element twice.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9

What clarifying questions do you have?"
```

**What I'm Looking For:**
- Do you ask clarifying questions?
- Do you restate the problem?
- Do you ask about constraints?

#### Step 4.2: UNDERSTAND - Clarifying Questions (2-3 min)

**Your Task:**
Ask clarifying questions like:
```
- "Can the array be empty?"
- "Are there always exactly two numbers that sum to target?"
- "Can I use the same element twice?"
- "Should I return indices or values?"
- "Is the array sorted?"
- "Can there be negative numbers?"
```

**My Response (as Interviewer):**
```
"Great questions!
- Array will have at least 2 elements
- Yes, exactly one solution exists
- No, you cannot use the same element twice
- Return indices
- Array is not sorted
- Yes, there can be negative numbers

Any other questions?"
```

**Red Flag:** Jumping straight to coding without asking questions!

#### Step 4.3: MATCH - Pattern Identification (1-2 min)

**Your Task:**
```
"This looks like a hash map problem because we need to check if a
number exists quickly. We're looking for pairs, which is a classic
hash map use case."
```

**My Response:**
```
"Excellent! You identified the hash map pattern. Why did you choose
hash map over other approaches?"
```

**What I'm Evaluating:**
- Can you identify patterns from keywords?
- Do you understand WHY you're using this approach?

#### Step 4.4: PLAN - Approach Discussion (3-5 min)

**Your Task:**
```
"Let me start with brute force:
- Nested loop checking all pairs
- Time: O(n²), Space: O(1)

Optimized approach using hash map:
- Single loop, store seen numbers
- For each number, check if target-number exists in map
- Time: O(n), Space: O(n)

The hash map approach is better for large arrays."
```

**My Response:**
```
"Good! You discussed both brute force and optimal. Walk me through
the hash map approach with the example:
nums = [2,7,11,15], target = 9"
```

**What I'm Looking For:**
- Did you discuss brute force first?
- Can you explain complexity?
- Can you walk through with an example?
- Getting my approval before coding!

**Red Flag:** Jumping to code without explaining approach!

#### Step 4.4b: WHERE TO CODE

**After getting approval, switch to LeetCode:**

**Browser Tab 2:** Open the problem on LeetCode.com

**Why LeetCode:**
- ✅ Built-in code editor
- ✅ Test cases already provided
- ✅ Instant testing with "Run" button
- ✅ Sees which tests pass/fail
- ✅ Real interview environment

**Workflow:**
1. I present problem (in Claude Code terminal)
2. **You switch to LeetCode browser tab**
3. **Code in LeetCode's editor**
4. **Think aloud** (interactive mode listens!)
5. **I respond with voice** while you code
6. **Click "Run"** to test your code
7. **Use F12** to discuss results with me

**Alternative:** You can code in VSCode if preferred, but LeetCode is recommended for built-in tests.

---

#### Step 4.5: IMPLEMENT - Coding (15-25 min)

**Where:** LeetCode editor (Browser Tab 2)

**Your Task:**
- Code the solution in LeetCode
- Think aloud while coding (use THINKING-ALOUD-PHRASES.md!)
- Use technical vocabulary (use TECHNICAL-VOCABULARY.md!)
- Handle edge cases

**My Role:**
- I stay mostly silent
- I observe your process
- I take notes on mistakes
- I only interrupt for major issues

**What I'm Evaluating:**
- Do you think aloud?
- Is your code clean and readable?
- Do you handle edge cases?
- Good variable names?
- Proper TypeScript types?

**Example of Good Thinking Aloud:**
```
"I'll create a Map to store numbers I've seen...
Let me call it 'seen' with type Map<number, number>...
Now I'll loop through the array with index i...
For each number, I'll calculate the complement: target minus current...
If complement exists in my map, I've found the pair...
Otherwise, I'll add current number to the map with its index..."
```

#### Step 4.6: REVIEW - Testing (3-5 min)

**Your Action:**
```
"Claude, I'm done coding"
```

**My Response:**
```
"Good! Now walk me through your solution using the example:
nums = [2,7,11,15], target = 9

Trace through your code step by step."
```

**Your Task:**
- Walk through code with given example
- Test edge cases
- Catch bugs

**My Follow-up:**
```
"I see your logic works for the example. Now test these edge cases:
1. nums = [3, 3], target = 6 (duplicate values)
2. nums = [1, 2], target = 10 (no solution - wait, problem says solution exists)
3. nums = [5, 2, 3], target = 7 (solution at indices 0, 2)

Walk through each one."
```

**What I'm Looking For:**
- Can you trace through code?
- Do you catch bugs?
- Do you test edge cases?

#### Step 4.7: EVALUATE - Complexity Analysis (2 min)

**My Question:**
```
"What's the time and space complexity of your solution?"
```

**Your Task:**
```
"Time complexity: O(n) because we loop through the array once,
and hash map operations (has, get, set) are O(1).

Space complexity: O(n) because in the worst case, we store n-1
elements in the hash map."
```

**My Response:**
```
"Perfect! You correctly identified both complexities and explained
your reasoning. That's exactly what interviewers want to hear."
```

---

### Phase 5: Feedback (5 min per problem)

**Your Action:**
```
"Claude, evaluate me"
```

**My Response:**
```
"Let me evaluate your performance on Two Sum:

📊 EVALUATION RUBRIC

Communication: 8/10
✅ Good thinking aloud
✅ Explained approach clearly
✅ Asked clarifying questions
⚠️ Could ask more about constraints upfront

Problem Solving: 7/10
✅ Identified hash map pattern quickly
⚠️ Jumped to optimal without discussing brute force first
⚠️ Should show thought process: simple → optimal

Code Quality: 9/10
✅ Clean, readable code
✅ Good variable names ('seen', 'complement')
✅ Proper TypeScript types
✅ Handled edge cases in code

Edge Cases: 7/10
✅ Tested duplicate values
✅ Considered when solution doesn't exist
⚠️ Didn't initially ask about empty array

Overall: 7.8/10 - Strong performance!

ACTION ITEMS FOR NEXT PROBLEM:
1. Discuss brute force approach first, even if obvious
2. Ask about all edge cases before coding
3. Mention time/space trade-off explicitly

Keep up the great work!"
```

**What This Covers:**
- Structured feedback on 4 dimensions
- Specific strengths and improvements
- Action items for next problem
- Positive reinforcement

---

### Phase 6: Next Problem or Next Session

**Your Options:**

**Continue Session:**
```
"Claude, next problem"
```
→ I present Problem 2/10

**Take Break:**
```
"Claude, end session"
```
→ Saves progress, you can resume later with "Claude, resume"

**Complete Session:**
```
"Claude, next session"
```
→ Auto-commits all progress, moves to next session

---

## Special Scenarios

### When You're Stuck

```
"Claude, I'm stuck"
```

**My Response:**
```
"Let's work through this. What have you tried so far?"
```

I'll ask probing questions to guide you, not give direct answers.

### Progressive Hints

```
"Claude, give me a hint"          → Level 1 (gentle nudge)
"Claude, another hint"             → Level 2 (specific direction)
"Claude, I really need help"       → Level 3 (step-by-step outline)
"Claude, show me the solution"     → Full solution (marked for review)
```

### Mid-Problem Questions

```
"Claude, show pattern two pointers"        → I show template
"Claude, TypeScript map methods"           → I show syntax reference
"Claude, what pattern is this"             → I help identify
```

---

## Session State Persistence

After each problem:
- `SESSION-STATE.json` is updated
- Auto-commit with detailed message
- Progress tracked in `PROGRESS-STATE.md`

You can always:
```
"Claude, resume"      → Continue where left off
"Claude, my progress" → See stats
"Claude, save my work" → Manual commit
```

---

## Tips for Effective Sessions

### Do's ✅
- Follow UMPIRE method strictly
- Think aloud constantly
- Ask clarifying questions first
- Discuss brute force before optimal
- Test edge cases
- Explain complexity
- Use voice commands for natural flow

### Don'ts ❌
- Don't jump straight to coding
- Don't code silently
- Don't skip testing phase
- Don't ignore feedback
- Don't use hints too quickly

---

## Example Full Session Timeline

**Day 1, Session 1: Big O & Arrays**

```
00:00  "Claude, start session 1 1"
00:02  I assign video
00:02  You watch 20-min video
00:22  "Claude, I watched the video"
00:23  I quiz you (5 min)
00:28  "Claude, give me tips"
00:33  "Claude, give me the problem"
00:35  Problem 1: Two Sum
       - Clarify (2 min)
       - Plan (4 min)
       - Code (10 min)
       - Test (3 min)
       - Evaluate (2 min)
       - Feedback (3 min)
00:59  "Claude, next problem"
01:00  Problem 2: Best Time to Buy/Sell Stock
       - [Repeat 24-min cycle]
...
03:48  "Claude, next problem"
03:49  Problem 10: Product of Array Except Self
       - [Solve]
04:13  "Claude, next session" or "Claude, end session"
```

**Total:** ~4 hours for 10 problems

---

## Customizing Your Flow

### Faster Pace (Advanced Users)
- Skip video if you know the topic
- Reduce testing time
- Aim for 15 min per Easy, 25 per Medium

### Slower Pace (Beginners)
- Rewatch video sections
- Use hints liberally
- Spend extra time on testing
- Do fewer problems per session

### Streaming Mode
- Use "Claude, explain for viewers" frequently
- "Claude, summarize so far" when needed
- More verbose thinking aloud

---

## Summary

**Remember:**
1. Each session is ~2-4 hours
2. Follow 6 phases for every problem
3. UMPIRE method is mandatory
4. Use voice commands for natural interaction
5. I'm your interviewer - treat it like real interview
6. Progress auto-saves - you can resume anytime

**Ready to start?**
```
"Claude, start session 1 1"
```

[Back to README](./README.md)
