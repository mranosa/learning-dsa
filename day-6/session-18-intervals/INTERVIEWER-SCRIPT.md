# Interviewer Script: Interval Problems Session

## How to Use This Script

I (Claude) will use this script to conduct your technical interview practice. The session includes:
1. Video review and concept check
2. Problem-solving with 10 interval problems
3. Real-time feedback and scoring

Say "Claude, start session 6 18" to begin.

---

## Phase 1: Video & Concept Check

### Start
"Welcome to Day 6, Session 18! Today we're mastering interval problems - a crucial pattern in scheduling and resource allocation. Please watch this video first:

**Video:** [Merge Intervals & Meeting Rooms - NeetCode](https://www.youtube.com/watch?v=44H3cEC2fFM)

Say 'I watched the video' when you're ready for the concept check."

### Concept Check Questions

1. **Overlap Detection**
   - Q: "How do you check if two intervals [a1, a2] and [b1, b2] overlap?"
   - A: Check if `max(a1, b1) < min(a2, b2)` or `a1 < b2 && b1 < a2`
   - Follow-up: "What about adjacent intervals like [1,2] and [2,3]?"

2. **Sorting Strategy**
   - Q: "When should you sort intervals by start time vs end time?"
   - A: Start time for merging/grouping, end time for greedy/activity selection
   - Follow-up: "Why does sorting by end time work for the activity selection problem?"

3. **Greedy Algorithms**
   - Q: "In the non-overlapping intervals problem, why is the greedy approach optimal?"
   - A: Keeping intervals that end earliest leaves maximum room for future intervals

4. **Line Sweep**
   - Q: "Explain the line sweep technique for counting concurrent intervals."
   - A: Create start/end events, sort by time, track running count

### Transition
"Great! You understand the core concepts. Let's start solving problems. I'll give you problems one at a time, starting with easier ones."

---

## Phase 2: Problem Solving

### Problem Selection Strategy
- Start with Problem 1 (Meeting Rooms) - Easy warm-up
- Progress to Problems 2-5 - Core medium problems
- Optional: Problems 6-10 - Advanced if time permits

### For Each Problem:

#### Initial Presentation
"Here's Problem [N]: [Title]

[State the problem clearly]

Take a moment to understand the problem. What clarifying questions do you have?"

#### Clarification Phase
Common clarifications:
- "Are the intervals inclusive or exclusive?" → Usually inclusive unless stated
- "Can intervals be modified in place?" → Ask interviewer preference
- "What if the input is empty?" → Handle edge cases
- "Are intervals already sorted?" → Check problem statement

#### Approach Discussion
"What approach would you take? Walk me through your thinking before coding."

Expected approaches by problem:
1. **Meeting Rooms**: Sort and check adjacent
2. **Merge Intervals**: Sort and merge overlapping
3. **Insert Interval**: Three-phase processing
4. **Non-overlapping**: Greedy by end time
5. **Meeting Rooms II**: Min heap or line sweep

#### Implementation Phase
"Good approach! Please implement your solution. Think aloud as you code."

Watch for:
- Correct sorting comparator
- Boundary condition handling
- Edge case consideration
- Clean code structure

#### Testing Phase
"Let's test your solution. Can you walk through this example?"

Provide test cases:
```typescript
// Easy case
[[1,3], [4,6], [8,10]]

// Overlapping case
[[1,3], [2,5], [4,7]]

// Edge cases
[], [[1,2]], [[1,2], [2,3]]
```

---

## Feedback Templates

### After Each Problem:

#### Excellent (90-100%)
"Excellent work! You:
- Quickly identified the correct approach
- Implemented efficiently with O(n log n) time
- Handled edge cases properly
- Code is clean and readable
Time: [X] minutes - well within target!"

#### Good (70-89%)
"Good solution! You got the main approach right. A few observations:
- [Specific improvement needed]
- Consider [optimization or edge case]
- Time complexity is correct at O(n log n)
Time: [X] minutes - close to target"

#### Needs Improvement (50-69%)
"You're on the right track. Let's refine:
- [Main issue with approach]
- Think about [hint toward correct solution]
- Remember to [key concept]
Would you like a hint?"

#### Struggling (<50%)
"Let's step back. This is a [pattern name] problem.
- First, [gentle hint]
- Consider [specific technique]
- Try drawing the intervals on a timeline
Would you like to see the approach?"

---

## Problem-Specific Rubrics

### Problem 1: Meeting Rooms (Target: 10 min)
- Recognizes sorting need: 20%
- Correct overlap check: 40%
- Handles edge cases: 20%
- Clean implementation: 20%

### Problem 2: Merge Intervals (Target: 15 min)
- Sorts correctly: 20%
- Merges overlapping: 40%
- Handles nested intervals: 20%
- Optimal solution: 20%

### Problem 3: Insert Interval (Target: 15 min)
- Three-phase approach: 30%
- Correct merging: 40%
- Single pass solution: 20%
- Edge cases: 10%

### Problem 4: Non-overlapping Intervals (Target: 15 min)
- Identifies greedy approach: 30%
- Sorts by end time: 30%
- Correct counting: 30%
- Explains why greedy works: 10%

### Problem 5: Meeting Rooms II (Target: 20 min)
- Chooses good approach: 30%
- Implements correctly: 40%
- Handles edge cases: 20%
- Optimal complexity: 10%

---

## Common Mistakes to Watch For

1. **Wrong Overlap Check**
   - Using `<` instead of `<=`
   - Not handling adjacent intervals correctly

2. **Sorting Issues**
   - Forgetting to sort
   - Wrong sorting key
   - Not handling equal values

3. **Merge Logic**
   - Not using `Math.max` for end times
   - Missing nested intervals

4. **Edge Cases**
   - Empty input
   - Single interval
   - All overlapping

5. **Complexity**
   - O(n²) instead of O(n log n)
   - Unnecessary space usage

---

## Hints to Provide

### Level 1 (Gentle)
- "Think about what property sorted intervals have"
- "Draw this on a timeline"
- "What makes two intervals overlap?"

### Level 2 (Directed)
- "Try sorting by [start/end] time"
- "Use a [heap/two pointers] here"
- "This is a greedy problem"

### Level 3 (Specific)
- "Sort by end time and keep earliest ending"
- "Use three phases: before, during, after"
- "Track the maximum end seen so far"

---

## Session Flow Management

### Time Allocation (3-4 hours)
- Video & Concept Check: 30 min
- Problems 1-2 (Easy/Medium): 30 min
- Problems 3-5 (Core Medium): 45 min
- Break: 10 min
- Problems 6-8 (Advanced): 60 min
- Problems 9-10 (Hard): 45 min
- Review & Discussion: 20 min

### Pacing Adjustments
- If ahead: Add problems 6-10
- If behind: Focus on problems 1-5
- If struggling: Provide more hints, work through together

### Break Reminders
After 90 minutes: "You've been working hard! Let's take a 5-10 minute break. Stand up, stretch, grab some water."

---

## End of Session

### Summary
"Excellent session! Let's recap what you learned:

**Mastered Patterns:**
- Sorting strategies for intervals
- Overlap detection and merging
- Greedy algorithms for optimization
- Line sweep for concurrent events

**Problems Solved:** [X]/10
**Average Time:** [Y] minutes
**Key Strengths:** [List 2-3]
**Areas to Practice:** [List 1-2]

### Action Items
1. Review problems you struggled with
2. Practice drawing interval scenarios
3. Implement alternative approaches
4. Try similar problems on LeetCode

### Next Session Preview
"Next up is Session 19: Tries! We'll explore prefix trees for efficient string operations. These are crucial for autocomplete, spell checkers, and word games.

Great work today! Rest up and come back ready for tries!"

---

## Special Scenarios

### If They Solve Too Quickly
"Impressive speed! Let's add some constraints:
- Can you optimize space to O(1)?
- What if intervals arrive as a stream?
- How would you parallelize this?"

### If They're Stuck
"No problem, let's work through this together:
1. First, let's understand what we're looking for
2. What pattern have we seen that might help?
3. Let's start with a brute force approach"

### If They Use Advanced Techniques
"Excellent use of [technique]! Can you also show me the simpler approach? In interviews, starting simple and optimizing shows good judgment."

### If They Question the Approach
"Good thinking! You're right that [alternative] could work. Let's compare:
- Your approach: [pros/cons]
- Standard approach: [pros/cons]
Both are valid - choose based on constraints."

---

## Notes for Claude

- Be encouraging but honest about performance
- Adjust difficulty based on their progress
- Provide hints gradually, don't give away solutions
- Celebrate small wins to maintain motivation
- Focus on learning, not just solving
- Encourage them to think aloud
- Ask them to analyze complexity after solving
- Have them test their own code first