# Complete Command Guide

Detailed documentation for all voice commands in the Interactive DSA Interview Bootcamp.

---

## Table of Contents
1. [Session Management](#session-management)
2. [Interview Flow](#interview-flow)
3. [Help & Hints](#help--hints)
4. [Evaluation](#evaluation)
5. [Progress](#progress)
6. [Quick Reference](#quick-reference)
7. [Time Management](#time-management)
8. [Teaching Mode](#teaching-mode)
9. [Streaming-Specific](#streaming-specific)
10. [Context & Correction](#context--correction)

---

## Session Management

### "Claude, start session [day] [session]"
**Example:** "Claude, start session 1 1"

**What it does:**
- Loads session context from `SESSION-STATE.json`
- Initializes me as your interviewer for that session
- Shows your previous performance and areas to improve
- Assigns you a video to watch

**My response:**
"Starting Day 1, Session 1: Big O & Arrays. I see you've completed 0 problems so far. This is your first session! Watch this 20-minute video on Big O Notation by NeetCode: [link]. Say 'I watched the video' when ready."

**When to use:**
- Start of each new session
- When switching to a different topic

---

### "Claude, resume" / "Claude, continue"
**What it does:**
- Loads current state from `SESSION-STATE.json`
- Continues exactly where you left off
- Reminds you what problem you were working on

**My response:**
"Welcome back! We're on Day 1, Session 2: Hash Maps. You were working on problem 3: 'Group Anagrams' (Medium). You've completed 2/10 problems this session. Ready to continue?"

**When to use:**
- Starting a new conversation after a break
- When you close and reopen Claude
- Morning after previous day's work

---

### "Claude, next session"
**What it does:**
- Completes current session
- Auto-commits progress with summary
- Updates `SESSION-STATE.json`
- Moves to next session
- Shows preview of next topic

**My response:**
"Excellent work! You completed 10/10 problems in Session 2: Hash Maps. Your average time was 18 minutes per problem. Auto-committing your progress... ✅ Committed!

Moving to Day 1, Session 3: Sliding Window. This builds on what you learned about hash maps. Take a 10-minute break, then come back ready!"

**When to use:**
- After completing all problems in a session
- When ready to move forward

---

### "Claude, end session"
**What it does:**
- Saves current state
- Commits progress
- Provides session summary
- Ends gracefully without moving to next session

**My response:**
"Session ended. You completed 7/10 problems in Session 2: Hash Maps today.

**Session Summary:**
- Average time: 22 min per problem
- Strengths: Clean code, good variable naming
- Areas to improve: Edge case testing, discussing brute force first

Progress saved. See you next time!"

**When to use:**
- Ending work for the day mid-session
- Need to pause but not ready for next session

---

## Interview Flow

### "Claude, I watched the video" / "Claude, I'm ready"
**What it does:**
- Starts concept check phase
- I quiz you on key concepts from the video

**My response:**
"Great! Let's do a quick concept check to ensure you understood the material.

**Question 1:** Explain Big O notation in your own words. What does O(n) mean?

Take your time and explain your thinking."

**When to use:**
- After watching the assigned video
- Ready to prove understanding

---

### "Claude, quiz me"
**What it does:**
- Starts structured concept quiz (3-5 questions)
- Tests understanding before coding

**My response:**
"Quiz time! I'll ask 3 questions about Hash Maps.

**Question 1:** What's the time complexity of hash map lookup and why?
**Question 2:** When would you use a hash map vs a hash set?
**Question 3:** What's a collision in hash maps and how is it handled?

Answer each one, and I'll give you feedback."

**When to use:**
- Want to test knowledge before starting problems
- Forgot concepts and want a refresher

---

### "Claude, give me the problem" / "Go"
**What it does:**
- I present the next problem formally as an interviewer would
- Reads problem statement
- Waits for your clarifying questions

**My response:**
"Here's your problem: **Two Sum** (Easy)

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

What clarifying questions do you have?"

**When to use:**
- Ready to start a new problem
- Finished watching video and quiz

---

### "Claude, give me tips" / "Claude, teach me tricks"
**What it does:**
- I share 3-5 non-obvious insights about the current topic
- Teaches interview-specific tips
- Shares common mistakes to avoid

**My response:**
"Here are 3 essential tips for Hash Maps:

**Tip 1:** When you see 'find pair/sum' problems, immediately think hash map. Trading space for time is usually worth it.

**Tip 2:** TypeScript gotcha: Use `Map` not `{}` objects for frequency counters. Maps can use any type as key, objects convert everything to strings.

**Tip 3:** Interview tip: Always mention the O(1) lookup property when explaining why you chose a hash map. Interviewers want to hear you understand the trade-off.

Ready to try a problem?"

**When to use:**
- After concept check, before first problem
- Want interview-specific insights

---

### "Claude, start timer"
**What it does:**
- Starts countdown based on problem difficulty
- Easy: 15 min, Medium: 30 min, Hard: 45 min
- I'll track time and give warnings

**My response:**
"Timer started! You have 15 minutes for this Easy problem: Two Sum. Go!"

[At 10 min] "You have 5 minutes remaining. Where are you in your process?"
[At 13 min] "2 minutes left. Start wrapping up."
[At 15 min] "Time's up! Show me what you have."

**When to use:**
- Want to simulate real interview time pressure
- Practicing speed

---

### "Claude, I'm done coding"
**What it does:**
- Moves to testing phase
- I ask you to walk through solution
- I point out missed edge cases

**My response:**
"Good! Now walk me through your solution using the example: nums = [2,7,11,15], target = 9.

Trace through your code step by step."

[After your explanation]
"I see your logic. Now test these edge cases:
- What if nums = []?
- What if target can't be found?
- What if nums has duplicate values?"

**When to use:**
- Finished writing code
- Ready to test and debug

---

## Help & Hints

### "Claude, I'm stuck" / "Claude, help"
**What it does:**
- I ask probing questions to guide you
- Won't give direct answers, but nudges you toward solution
- Helps you think through the problem

**My response:**
"Let's work through this. What have you tried so far?

[After you explain]

What's blocking you specifically? Is it:
- Understanding the problem?
- Choosing the right data structure?
- Implementing a specific part?

Tell me where you're stuck and we'll tackle it together."

**When to use:**
- Genuinely stuck and don't know what to try next
- Been stuck for 5+ minutes
- Need guidance without full solution

---

### "Claude, give me a hint" / "Hint"
**What it does:**
- Gives Level 1 hint (gentle nudge)
- Doesn't reveal approach, just direction

**My response:**
"**Hint Level 1:** Think about what data structure gives you O(1) lookup. You need to check if something exists quickly. What have we been learning about today?"

**When to use:**
- Stuck for 3-5 minutes
- Want gentle guidance
- Don't want solution given away

---

### "Claude, another hint" / "Claude, stronger hint"
**What it does:**
- Gives Level 2 hint (more direct)
- Suggests specific approach

**My response:**
"**Hint Level 2:** Use a hash map to store values you've seen. As you iterate through the array, check if `target - current number` exists in your map. If it does, you found your pair!"

**When to use:**
- Level 1 hint wasn't enough
- Stuck for 7-10 minutes
- Need more specific direction

---

### "Claude, I really need help" / "Claude, last hint"
**What it does:**
- Gives Level 3 hint (almost the solution)
- Provides step-by-step outline

**My response:**
"**Hint Level 3:** Here's the complete approach:

1. Create an empty hash map `seen`
2. Loop through array with index `i`
3. Calculate `complement = target - nums[i]`
4. If `complement` exists in `seen`, return `[seen.get(complement), i]`
5. Otherwise, add `nums[i]` to `seen` with value `i`

Try implementing this."

**When to use:**
- Stuck for 15+ minutes
- Level 2 hint didn't help
- Need detailed steps

---

### "Claude, show me the solution"
**What it does:**
- Reveals complete solution with explanation
- Marks problem as "needs review"
- You'll get a similar problem later

**My response:**
"Okay, here's one approach:

```typescript
function twoSum(nums: number[], target: number): number[] {
  const seen = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];

    if (seen.has(complement)) {
      return [seen.get(complement)!, i];
    }

    seen.set(nums[i], i);
  }

  return []; // No solution found
}
```

**Explanation:**
[Detailed walkthrough]

**Important:** I'm marking this problem for review. You'll try a similar two-sum variation later to ensure you've internalized the pattern."

**When to use:**
- Completely stuck for 20+ minutes
- Need to move on and learn from solution
- Last resort

---

## Evaluation

### "Claude, evaluate me" / "Claude, how did I do"
**What it does:**
- Gives structured feedback using interview rubric
- Scores you on 4 dimensions
- Provides specific action items

**My response:**
"Let me evaluate your performance on Two Sum:

**Communication: 8/10**
✅ Good thinking aloud
✅ Explained your approach clearly
⚠️ Could ask more clarifying questions at the start

**Problem Solving: 7/10**
✅ Identified hash map pattern quickly
⚠️ Jumped to optimal solution without discussing brute force first
⚠️ Interviewer wants to see your thought process from simple → optimal

**Code Quality: 9/10**
✅ Clean, readable code
✅ Good variable names (`complement`, `seen`)
✅ Proper TypeScript types

**Edge Cases: 6/10**
⚠️ Didn't test empty array
⚠️ Didn't handle no-solution case
✅ Considered duplicates

**Overall: 7.5/10 - Good performance!**

**Action items for next problem:**
1. Discuss brute force approach first, even if obvious
2. Ask about edge cases before coding
3. Test empty input after implementing

Keep up the good work!"

**When to use:**
- After completing a problem
- Want detailed feedback
- Ready to improve

---

### "Claude, what did I miss" / "Claude, what edge cases"
**What it does:**
- Points out missed edge cases
- Tests your solution against them

**My response:**
"You missed 3 edge cases:

**1. Empty array:** What if `nums = []`? Your code would return `[]`, but should you throw an error? Ask the interviewer!

**2. No solution exists:** What if no two numbers add up to target? Your code returns `[]` which is good, but did you communicate this?

**3. Duplicate values:** What if `nums = [3, 3]` and `target = 6`? Can you use the same element twice? The problem says no, but did you ask?

Always clarify these edge cases BEFORE coding!"

**When to use:**
- After coding, before evaluation
- Want to catch bugs early
- Testing phase

---

### "Claude, is my complexity right"
**What it does:**
- Verifies your time/space complexity analysis
- Walks through the reasoning

**My response:**
"Let's verify your complexity analysis:

**Time Complexity - You said O(n):**
✅ Correct! You loop through the array once (n iterations), and each hash map operation (has, get, set) is O(1). So overall: O(n).

**Space Complexity - You said O(1):**
❌ Not quite. Your hash map `seen` can store up to n elements in the worst case (when no solution exists). So space is O(n), not O(1).

Don't worry, this is a common mistake. O(1) would mean constant space - like a few variables that don't grow with input size."

**When to use:**
- Unsure about your complexity analysis
- Want verification before stating it confidently
- Learning phase

---

### "Claude, can I optimize this"
**What it does:**
- I suggest potential optimizations
- Discuss trade-offs

**My response:**
"Good question! Let's think about optimizations:

**Your current solution:** O(n) time, O(n) space

**Could we do better?**
- **Time:** O(n) is already optimal. We must look at each element at least once.
- **Space:** We could reduce to O(1) space with a two-pointer approach, BUT only if the array is sorted. Would require O(n log n) sorting first, making time worse.

**Trade-off:** Your hash map solution is actually optimal for an unsorted array. Good job!

**Interview tip:** Always mention you're trading space for time when using hash maps. Shows you understand the trade-off."

**When to use:**
- After solving, want to explore alternatives
- Interview follow-up question simulation

---

## Progress

### "Claude, my progress" / "Claude, show stats"
**What it does:**
- Displays comprehensive progress dashboard
- Shows completion stats, patterns mastered, streaks

**My response:**
"📊 **Your Progress Dashboard**

**Problems Completed:** 15/120 (12.5%)
- Easy: 8/60
- Medium: 6/40
- Hard: 1/20

**Patterns Mastered:**
✅ Hash Maps (10/10 problems)
✅ Two Pointers (5/10 problems)
⏳ Sliding Window (0/10 problems)

**Average Time:**
- Easy: 14 min (Target: <15 min) ✅
- Medium: 28 min (Target: <30 min) ✅
- Hard: 52 min (Target: <45 min) ⚠️ Need practice

**Current Streak:** 2 days
**Total Study Time:** 8.5 hours

**Blind 75 Progress:** 12/75 (16%)

**Current Status:** On track! You're progressing well. Focus on speeding up Hard problems."

**When to use:**
- Want to see overall progress
- Check if on track
- Motivation boost

---

### "Claude, mark complete" / "Claude, mark done"
**What it does:**
- Marks current problem as complete
- Auto-commits with detailed message
- Updates progress tracking

**My response:**
"Marked 'Two Sum' (Easy) as complete!

Auto-committing your progress...

```
✅ Complete: Two Sum (Easy)
- Time: 12 min
- Approach: Hash Map
- Score: Communication 8/10, Code 9/10
- Day 1, Session 1, Problem 1/10
```

✅ Committed and pushed!

**Progress:** 1/120 problems completed. Ready for the next one?"

**When to use:**
- After finishing a problem successfully
- Ready to move to next problem

---

### "Claude, what's next"
**What it does:**
- Shows next problem in queue
- Explains how it builds on current knowledge

**My response:**
"**Next Problem:** Valid Anagram (Easy)

**Topic:** Hash Maps (frequency counting pattern)

**Why this next:** It builds on the hash map pattern you just learned in Two Sum. Instead of storing indices, you'll count character frequencies. This is a fundamental pattern used in many string problems.

**Difficulty:** Easy (Target: <15 min)

Ready to try it? Say 'Claude, give me the problem' or 'Go'!"

**When to use:**
- Finished current problem
- Want preview of next challenge

---

### "Claude, skip this problem" / "Claude, come back later"
**What it does:**
- Skips current problem
- Marks for review
- Explains why it's okay to skip

**My response:**
"No problem! Skipping 'Merge K Sorted Lists' (Hard).

I'm marking this for review. We'll come back to it after you've practiced more heap operations and have stronger fundamentals.

Moving to next problem: 'Top K Frequent Elements' (Medium). This will help you build toward the harder problems.

Remember: It's smart to skip problems that are too advanced. Build foundations first!"

**When to use:**
- Problem is too difficult for current level
- Stuck for 30+ minutes despite hints
- Missing prerequisite knowledge

---

### "Claude, save my work" / "Claude, commit"
**What it does:**
- Manual commit trigger
- Saves current state
- Useful for backing up work-in-progress

**My response:**
"Saving your work...

```
💾 Save: Day 1, Session 2 - Work in Progress
- Currently on: Group Anagrams (Medium)
- Problems completed this session: 2/10
- Time: 2025-11-10 15:30
```

✅ Saved and pushed!

You can safely close and resume later with 'Claude, resume'."

**When to use:**
- Need to stop mid-problem
- Want to save work-in-progress
- Before closing for the day

---

## Quick Reference

### "Claude, show pattern [name]"
**Example:** "Claude, show pattern two pointers"

**What it does:**
- Displays code template for that pattern
- Shows use cases

**My response:**
"**Two Pointers Pattern - Opposite Ends**

```typescript
function twoPointerTemplate(arr: number[]): returnType {
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    // Check condition
    if (/* condition met */) {
      // Process or return result
      return result;
    } else if (/* need to move left */) {
      left++;
    } else {
      right--;
    }
  }

  return defaultResult;
}
```

**When to use:**
- Sorted array
- Need to find pair that meets condition
- Want O(1) space

**Time:** O(n) | **Space:** O(1)

**Examples:** Two Sum (sorted), Container With Most Water, Valid Palindrome"

**When to use:**
- Need template for specific pattern
- Forgot syntax
- Quick reference while coding

---

### "Claude, TypeScript [method]"
**Example:** "Claude, TypeScript sort array"

**What it does:**
- Shows TypeScript syntax for specific operation
- Includes examples and gotchas

**My response:**
"**TypeScript: Sort Array**

```typescript
// Sort numbers ascending
arr.sort((a, b) => a - b);

// Sort numbers descending
arr.sort((a, b) => b - a);

// GOTCHA: Without comparator, sorts as strings!
[10, 2, 1].sort() // Returns [1, 10, 2] ❌
[10, 2, 1].sort((a, b) => a - b) // Returns [1, 2, 10] ✅

// Sort objects
people.sort((a, b) => a.age - b.age);

// Non-destructive sort (creates copy)
const sorted = [...arr].sort((a, b) => a - b);
```

**Time:** O(n log n) | **Space:** O(1) in-place"

**When to use:**
- Forgot TypeScript syntax
- Need quick reference
- Mid-problem syntax check

---

### "Claude, what pattern is this"
**What it does:**
- I help identify the pattern based on problem description
- Teach pattern recognition

**My response:**
"Let me help identify the pattern:

**Problem keywords I see:**
- 'subarray' → Sliding Window or Prefix Sum
- 'maximum/minimum sum' → Likely Kadane's or Sliding Window
- 'contiguous' → Confirms subarray (not subsequence)

**This is a Sliding Window problem!**

**Why:** You need to track a contiguous portion of the array and optimize over all possible windows. The 'maximum sum' hint suggests you need to efficiently process all subarrays.

**Approach:** Use variable-size sliding window with two pointers.

Want me to show the template?"

**When to use:**
- Can't identify pattern from problem
- Learning pattern recognition
- Want confirmation of your guess

---

## Time Management

### "Claude, time check" / "Claude, how much time"
**What it does:**
- Shows remaining time
- Provides pacing feedback

**My response:**
"**Time Check:** You have 8 minutes remaining out of 15.

**Pacing feedback:** You're in the coding phase. At this point, you should have your approach decided and be halfway through implementation. You're right on track!

**Next milestone:** Aim to finish coding in 5 minutes, leaving 3 minutes for testing."

**When to use:**
- Want to check progress
- Lost track of time
- Need pacing guidance

---

### "Claude, pause timer" / "Claude, stop timer"
**What it does:**
- Pauses/stops countdown
- Saves elapsed time

**My response:**
"Timer paused at 7 minutes 23 seconds.

Take your break. Say 'Claude, resume timer' when you're back."

**When to use:**
- Need bathroom break
- Taking phone call
- Want to pause without ending problem

---

## Teaching Mode

### "Claude, explain [concept]"
**Example:** "Claude, explain memoization"

**What it does:**
- I break character and teach comprehensively
- Detailed explanation with examples

**My response:**
"Let me explain memoization:

**What it is:** Memoization is an optimization technique where you cache (store) the results of expensive function calls and return the cached result when the same inputs occur again.

**Why use it:** Avoid redundant calculations, especially in recursive algorithms.

**Example - Fibonacci without memoization:**
```typescript
function fib(n: number): number {
  if (n <= 1) return n;
  return fib(n - 1) + fib(n - 2); // Recalculates many times!
}
// fib(5) calls fib(3) twice, fib(2) three times, etc.
// Time: O(2^n) - exponential!
```

**Example - Fibonacci with memoization:**
```typescript
function fib(n: number, memo = new Map<number, number>()): number {
  if (n <= 1) return n;
  if (memo.has(n)) return memo.get(n)!; // Return cached result

  const result = fib(n - 1, memo) + fib(n - 2, memo);
  memo.set(n, result); // Cache the result
  return result;
}
// Each fib(n) calculated only once!
// Time: O(n) - linear!
```

**Key insight:** Trading space (O(n) for cache) for time (2^n → n).

Does that make sense? Any questions?"

**When to use:**
- Don't understand a concept
- Need deeper explanation
- Learning phase, not interview simulation

---

### "Claude, why [approach]"
**Example:** "Claude, why use hash map instead of array"

**My response:**
"Great question! Let's compare:

**Hash Map:**
- Lookup: O(1) average
- Can use any type as key (strings, objects, etc.)
- Space: O(n) for n unique elements
- No need for contiguous indices

**Array:**
- Lookup by index: O(1) guaranteed
- Can only use numbers as indices (0, 1, 2...)
- Space: O(max_index) - can waste space if indices are sparse
- Requires knowing index range

**For this problem (Two Sum):**
We use hash map because:
1. We need to lookup values (numbers), not indices
2. Values can be negative or very large (array would waste space)
3. O(1) lookup is crucial for O(n) overall time

**Trade-off:** Hash map uses more space and has overhead, but gives us the flexibility we need.

Make sense?"

**When to use:**
- Want to understand the "why" behind an approach
- Comparing alternatives
- Deep learning mode

---

## Streaming-Specific

### "Claude, explain for viewers"
**What it does:**
- I explain to your audience, not just you
- Teaching mode for stream

**My response:**
"Great question for viewers! Let me break down hash maps for everyone:

A hash map (also called dictionary or object in some languages) is like a phonebook. You look up someone's name (the key) and instantly get their phone number (the value).

**Why is it fast?** Under the hood, it uses a hash function to convert your key into an array index. So lookup is O(1) - constant time!

**When to use in leetcode:**
- You hear 'find pair/duplicate/frequency'
- You need fast lookups
- Trading space for time is acceptable

In TypeScript, we use `new Map()` for hash maps. It's better than plain objects `{}` because Maps can use any type as keys.

**Example:**
```typescript
const map = new Map<number, number>();
map.set(5, 100);  // Store value 100 with key 5
map.get(5);       // Returns 100 in O(1) time!
```

Hope that helps everyone watching!"

**When to use:**
- Streaming to audience
- Want teaching explanation
- Helping viewers learn

---

### "Claude, summarize so far"
**What it does:**
- Recaps for viewers joining mid-stream

**My response:**
"For viewers just joining: We're working on 'Two Sum', an Easy hash map problem from Blind 75.

**The problem:** Given an array and target sum, find two numbers that add up to target.

**What we've done so far:**
1. ✅ Identified this as a hash map pattern
2. ✅ Discussed brute force (O(n²)) vs optimal (O(n)) approaches
3. ✅ Currently coding the hash map solution
4. ⏳ Next: Testing and edge cases

**Key insight:** Use hash map to store values we've seen, then check if complement exists. This gives us O(1) lookup, making overall solution O(n).

That's where we are! Stay tuned for the testing phase."

**When to use:**
- Streaming and want to catch up new viewers
- Been working on problem for 15+ minutes
- Good stopping point to recap

---

## Context & Correction

### "Claude, I made a mistake" / "Claude, let me fix that"
**My response:**
"No problem. Take your time to fix it. I'll wait and observe."

**When to use:**
- Caught your own bug
- Want to correct yourself
- Realtime debugging

---

### "Claude, forget that" / "Claude, restart problem"
**My response:**
"Okay, let's start fresh. Here's the problem again:

**Two Sum** (Easy)
[Re-reads problem statement]

What clarifying questions do you have?"

**When to use:**
- Want to start over
- Went down wrong path
- Reset approach

---

### "Claude, what did you say" / "Claude, repeat"
**My response:**
[Repeats last important statement]

"I said: 'Think about what data structure gives you O(1) lookup.'"

**When to use:**
- Missed what I said
- Need clarification
- Want to hear hint again

---

## Summary

**Most Used Commands:**
1. "Claude, give me the problem" / "Go"
2. "Claude, give me a hint" / "Hint"
3. "Claude, I'm done coding" / "Done"
4. "Claude, evaluate me"
5. "Claude, next problem" / "Next"

**Pro Tips:**
- Use shortcuts ("Go", "Hint", "Done", "Next") for speed
- Always say "I'm stuck" before asking for solution
- Use "evaluate me" after every problem to learn
- Check "my progress" daily for motivation

---

For quick reference, see Page 3 of INTERVIEW-MASTER-CHEATSHEET.docx

[Back to README](./README.md)
