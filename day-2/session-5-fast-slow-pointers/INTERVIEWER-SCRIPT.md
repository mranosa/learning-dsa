# Interviewer Script: Fast/Slow Pointers

## Session Introduction (2 min)

"Welcome to Session 5: Fast/Slow Pointers! Today we're exploring Floyd's Tortoise and Hare algorithm - one of the most elegant patterns in computer science.

Before we begin:
1. Have you watched the videos?
2. Development environment ready?
3. Any questions about the pattern?"

---

## Concept Check (5-10 min)

### Q1: Basic Understanding
"Explain Floyd's cycle detection algorithm."

**Expected:**
- Two pointers, different speeds
- Slow: 1 step, Fast: 2 steps
- Cycle: they meet
- No cycle: fast reaches null

**Follow-up:** "Why do they meet?"

### Q2: Complexity
"Time/space complexity: Floyd's vs HashSet?"

**Expected:**
- Floyd's: O(n) time, O(1) space
- HashSet: O(n) time, O(n) space
- Floyd's wins on space

### Q3: Pattern Recognition
"Name three problem types using fast/slow pointers."

**Expected:**
- Cycle detection
- Finding middle
- Nth from end
- Detecting loops in sequences
- Finding duplicates

---

## Problem Selection

"Based on your level:
- **Beginner:** Problem 1 (Linked List Cycle)
- **Intermediate:** Problem 3 (Happy Number)
- **Advanced:** Problem 5 (Find Duplicate)

Which would you prefer?"

---

## Problem 1: Linked List Cycle (Easy)

### Presentation
"Determine if linked list has a cycle using O(1) space."

### Good Questions
- "Can list be empty?" → Yes
- "Single node?" → Yes
- "Can I modify list?" → No
- "Return type?" → Boolean

### UMPIRE Guidance

**Understand (2 min):**
- Clarify cycle meaning
- Draw example

**Match (1 min):**
- "What pattern fits?"
- Guide to fast/slow

**Plan (3 min):**
- Explain algorithm
- Discuss edge cases

**Implement (5-7 min):**
- Watch null checking
- Verify loop conditions

**Review (2 min):**
- "Trace through example"
- "Time complexity?"

**Evaluate (1 min):**
- "Can we optimize?"
- "What if we could modify?"

### Watch For
- Missing null checks
- Wrong condition (should be `fast && fast.next`)
- Incorrect pointer initialization

---

## Problem 2: Linked List Cycle II (Medium)

### Presentation
"Find where cycle begins. O(1) space."

### Teaching Moment
"This requires understanding the math. Let me explain..."

Draw:
- Distance head → cycle start: `a`
- Distance cycle start → meeting: `b`
- Remaining cycle: `c`

"When they meet: slow = a + b, fast = a + 2b + c"

### Focus
- Two-phase approach
- Phase 1: Detect
- Phase 2: Find entry

---

## Problem 3: Happy Number (Easy)

### Presentation
"Happy number reaches 1 by repeatedly replacing with sum of digit squares. Otherwise loops."

### Pattern Recognition
"How is this cycle detection?"
- Sequence of transformations
- Either reaches 1 or cycles
- Apply fast/slow to sequence

### Implementation
- Helper for transformation
- Same fast/slow pattern
- Check if meeting point is 1

---

## Problem 5: Find Duplicate (Medium)

### Presentation
"Array of n+1 integers in [1,n]. Find duplicate. O(1) space, don't modify."

### Key Insight
"Think of array as implicit linked list where nums[i] points to index nums[i]."

### Visualization
```
nums = [1,3,4,2,2]
0→1→3→2→4→2 (cycle!)
```

### Guidance
- Start at nums[0]
- Apply Floyd's treating array as list
- Find cycle, then entrance

---

## Difficulty Management

### If Struggling:
1. "Let's draw pointer movements"
2. "What happens each iteration?"
3. "Handle simplest case first"
4. Use hint levels from HINTS.md

### If Succeeding:
1. "Great! Think of edge cases?"
2. "What about cycle length?"
3. "Try Problem 7 (Reorder List)"

---

## Time Management

- **Easy:** 15 min max
- **Medium:** 25 min max

If over time:
"Let's move to implementation. I'll guide you."

---

## Engagement

### For Each Problem:
1. **Visualize:** "Draw an example"
2. **Think aloud:** "Walk me through your thought process"
3. **Test:** "Trace with input [1,2,3,4]"
4. **Complexity:** "Runtime? Can we do better?"

### Encouragement:
- "Good observation about edge case!"
- "Right track with that approach"
- "Common mistake - let's fix it"
- "Excellent use of the pattern!"

---

## Problem-Specific Tips

### Linked Lists:
- Always check null/empty
- Use dummy nodes when needed
- Draw pointer movements

### Arrays:
- Think implicit graph/list structure
- Handle modulo carefully
- Consider negative indices

### Sequences:
- Define transformation clearly
- Check termination
- Consider cycle length

---

## Common Struggles

### "Why do they meet?"
Running track analogy:
- Faster laps slower
- Relative speed determines when

### "Why reset to head?"
Mathematical proof:
- Distance relationships force meeting at entry

### "When different speeds?"
- 1 and 2: cycle detection
- Same speed: after meeting, find entry
- Gap of n: nth from end

---

## Session Wrap-up (5 min)

### Review:
1. "Key insight for fast/slow?"
2. "Most challenging problem? Why?"
3. "How to recognize this pattern?"

### Action Items:
1. "Practice drawing pointer movements"
2. "Try remaining problems"
3. "Review Floyd's mathematical proof"

### Next Session:
"Next: Merge Intervals - array manipulation pattern building on sorting and comparison skills."

---

## Indicators

### Understanding:
- ✅ Implements basic cycle detection
- ✅ Handles edge cases unprompted
- ✅ Explains why algorithm works
- ✅ Recognizes pattern in different contexts

### Red Flags:
- ❌ Can't handle null checks
- ❌ Confused about pointer speeds
- ❌ Doesn't understand cycle vs no cycle
- ❌ Can't adapt pattern

### Adjustments:
- **Too easy:** Jump to Problem 9
- **Too hard:** More visualization time
- **Conceptual gap:** Review video together
- **Implementation issues:** Pair program one solution

---

## Sample Dialog

**I:** "Happy Number. How does this relate to cycle detection?"

**C:** "Hmm, not really. It's about numbers, not lists."

**I:** "Think about transformation sequence. What are two possible outcomes?"

**C:** "Oh! Either reach 1, or loop!"

**I:** "Exactly! How to detect loop?"

**C:** "HashSet to track seen... or wait, fast/slow on the sequence!"

**I:** "Perfect! Show me."

---

Remember: Guide discovery, don't just evaluate. Build confidence with this powerful pattern!
