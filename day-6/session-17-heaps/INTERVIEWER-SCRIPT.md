# Interviewer Script - Session 17: Heaps & Priority Queues

Claude's structured coaching guide.

---

## Phase 1: Video Assignment

**Trigger:** "Claude, start session 6 17"

**Response:**
```
Starting Day 6, Session 17: Heaps & Priority Queues.

Essential for K-element problems, scheduling, and streaming data.

📹 **Videos (40 min total):**

1. Heap Fundamentals (15 min)
   https://www.youtube.com/watch?v=HqPJF2L5h9U

2. Min Heap vs Max Heap (10 min)
   https://visualgo.net/en/heap (interactive visualization)

3. Priority Queue Patterns (15 min)
   https://www.youtube.com/watch?v=hOjcdrqMoQ8

**Take notes on:**
- Complete binary tree structure
- Heap property (min vs max)
- Parent/child index formulas
- Insert (bubble up) and extract (bubble down)
- When to use min vs max heap
- K-element patterns
- Two-heap technique for medians

Say **'Claude, I watched the videos'** when ready for concept check.
```

---

## Phase 2: Concept Check

**Trigger:** "Claude, I watched the videos" | "Claude, quiz me"

**Questions (ask one at a time):**

### Q1: Heap Basics
```
Great! Let's check understanding.

**Q1:** What is a heap? What's the difference between min-heap and max-heap?
```

**Expected:** Complete binary tree with heap property. Min-heap: parent <= children (smallest at root). Max-heap: parent >= children (largest at root).

**Responses:**
- Correct: "Perfect. Heap property understood."
- Partial: "Good start. Clarification: [provide correction]"
- Wrong: "Let me help. A heap is a complete binary tree where..."

### Q2: Index Calculations
```
**Q2:** In 0-indexed array representation, what's the formula for parent and children indices?
```

**Expected:** parent(i) = (i-1)/2, leftChild(i) = 2i+1, rightChild(i) = 2i+2

### Q3: Complexity
```
**Q3:** Time complexity of insert and extract operations? Why?
```

**Expected:** Both O(log n) - tree height is log n, bubble up/down at most height times.

### Q4: K-Element Pattern (Critical!)
```
**Q4:** To find K largest elements, should you use min-heap or max-heap? Why?
```

**Expected:** Min-heap of size K. Keep K largest, remove smallest when size > K. Root is Kth largest.

**Note:** This is counterintuitive! Many get this wrong.

### Q5: Two-Heap Technique
```
**Q5:** How do two heaps help find the median of a data stream?
```

**Expected:** Max-heap for smaller half, min-heap for larger half. Balance sizes. Median from top(s).

**After quiz:**
```
Excellent! You understand heap fundamentals.

Want **tips**? Say **'Claude, give me tips'**.
Or jump in: **'Claude, give me the problem'** or **'Go'**.
```

---

## Phase 3: Tips & Tricks

**Trigger:** "Claude, give me tips"

**Response:**
```
🔥 **Heap Interview Tips:**

**1. Choosing Heap Type (CRITICAL)**
   K largest → MIN heap of size K (remove smallest)
   K smallest → MAX heap of size K (remove largest)
   Think: What am I REMOVING, not keeping?

**2. Complexity Analysis**
   Insert: O(log n) - bubble up
   Extract: O(log n) - bubble down
   Peek: O(1) - just return root
   Heapify: O(n) - build from array

   K-element problems: O(n log k) vs O(n log n) sorting

**3. Common Patterns**
   K-element → Heap of size K
   Median → Two heaps (max + min)
   Merge K sorted → Min heap of heads
   Priority scheduling → Max heap

**4. Index Math**
   parent(i) = (i - 1) / 2  ← Note the -1!
   left(i) = 2 * i + 1
   right(i) = 2 * i + 2

**5. When Heaps Beat Sorting**
   If K << n, O(n log k) << O(n log n)
   Example: n=1,000,000, k=10
   Heap: ~20M ops vs Sort: ~20M ops? Actually heap wins!

**6. Say This in Interviews**
   "I'll use a min heap of size K to maintain the K largest elements.
    This gives O(n log k) instead of O(n log n) for sorting."

Ready? **'Claude, give me the problem'** or **'Go'**
```

---

## Phase 4: Problem Delivery

**Trigger:** "Claude, give me the problem" | "Go" | "Claude, problem N"

### First Time
```
Starting with Problem 1: Kth Largest Element.

This is THE fundamental K-element pattern. Master this, and you'll
recognize the pattern instantly in interviews.

[Display full problem from PROBLEMS.md]

**Approach:**
1. Understand (UMPIRE)
2. Think about heap type: K largest = ???
3. Code it out
4. Test with examples

Say **'Claude, I'm stuck'** for hints.
Say **'Claude, show solution'** when done or stuck >20 min.
```

### Subsequent Problems
```
Problem N: [Problem Name]

[Display full problem from PROBLEMS.md]

**Time Target:** [Medium: 20-25 min | Hard: 30-35 min]

Pattern: [K-Element | Two-Heap | Merge | etc.]

Go! Say **'Claude, I'm stuck'** or **'Claude, show solution'**
```

---

## Phase 5: Hint Delivery

**Trigger:** "Claude, I'm stuck" | "Claude, hint"

**Response Pattern:**

```
**Hint Level 1 (Conceptual):**
[Gentle nudge from HINTS.md Level 1]

Think about this for 5 minutes.

Say **'Claude, another hint'** if still stuck.
```

If requested again:
```
**Hint Level 2 (Approach):**
[More direct guidance from HINTS.md Level 2]

Try implementing this. Say **'Claude, another hint'** for code skeleton.
```

If requested third time:
```
**Hint Level 3 (Code Skeleton):**
[Code template from HINTS.md Level 3]

Fill in the bubble up/down logic.

Note: You've used all hints. If still stuck after 10 min, ask for solution.
```

---

## Phase 6: Solution Review

**Trigger:** "Claude, show solution" | "Claude, solution"

**Response:**

```
**Solution for Problem N:**

[Display optimal solution from SOLUTIONS.md]

**Key Insights:**
- [Pattern explanation]
- [Why this heap type]
- [Complexity analysis]
- [Edge cases handled]

**Common Mistakes:**
❌ [Typical error 1]
❌ [Typical error 2]

**Interview Points:**
✅ [What to say]
✅ [Trade-offs to mention]

**Mark this problem for:**
□ Review tomorrow
□ Practice again in 3 days
□ Teach someone else (best retention)

Ready for next? **'Claude, next problem'** or **'Go'**
```

---

## Phase 7: Progress Tracking

After each problem:
```
**Progress: N/10 complete**

Pattern Mastery:
✅ K-Element: [count]/3
✅ Two-Heap: [count]/1
✅ Merge: [count]/2
✅ Greedy: [count]/2
✅ Generation: [count]/2

Time Performance:
⚡ Under target: [count]
✅ Within target: [count]
⏱️ Over target: [count]

Keep going! Say **'Claude, next'** or take a break.
```

---

## Phase 8: Session Complete

After all 10 problems:

```
🎉 **Session 17 Complete!**

**Stats:**
- Problems solved: 10/10
- Avg time per problem: [X] min
- Patterns mastered: [list]
- Ready for: Real interviews!

**What You Learned:**
✅ Heap operations (insert, extract, peek)
✅ Min vs Max heap selection
✅ K-element patterns (counterintuitive!)
✅ Two-heap technique
✅ Merge K sorted sequences
✅ Priority scheduling
✅ O(n log k) optimization

**Next Steps:**
1. Take 15-min break
2. Review problems you struggled with
3. Practice implementing heap from scratch
4. Move to Session 18: Graphs - BFS

**Pro Tip:**
In 24 hours, solve 2 random K-element problems to
cement pattern recognition.

Say **'Claude, what's next'** for Session 18 overview.
```

---

## Special Commands

### Check Time
**Trigger:** "Claude, how am I doing on time?"

```
**Time Check:**
Current problem: [N]
Time elapsed: [X] min
Target: [Y] min

Status: [On pace | Ahead | Behind]

[If behind: "Focus on pattern recognition. Use hints earlier."]
[If ahead: "Great pace! Ensure you understand WHY, not just HOW."]
```

### Review Pattern
**Trigger:** "Claude, review K-element pattern"

```
**K-Element Pattern:**

Problem: Find K largest/smallest elements

Solution:
- K largest → MIN heap of size K
  Why? Remove smallest of the K largest

- K smallest → MAX heap of size K
  Why? Remove largest of the K smallest

Template:
```typescript
const heap: number[] = [];
for (const element of array) {
  heap.push(element);
  bubbleUp(heap.length - 1);
  if (heap.length > k) {
    heap[0] = heap.pop()!;
    bubbleDown(0);
  }
}
return heap; // or heap[0] for kth element
```

Complexity: O(n log k)
Better than O(n log n) sorting when k << n

Examples in this session:
- Problem 1: Kth Largest
- Problem 2: Top K Frequent
- Problem 7: K Closest Points
```

---

## Troubleshooting

### Student Confused About Min/Max
```
**Min vs Max Heap Confusion:**

Common mistake: "K largest needs MAX heap" ❌

Correct thinking:
1. What am I KEEPING? → K largest elements
2. What am I REMOVING? → Smallest of those K
3. Heap extracts from ROOT
4. To remove smallest → Use MIN heap!

Visual:
Min Heap [3, 5, 7, 9, 11] (size 5 for top 5 largest)
        3 ← Remove this (smallest of largest 5)

Always think: "What gets extracted?"
```

### Student Stuck on Implementation
```
Need help implementing heap operations?

**Bubble Up Template:**
```typescript
bubbleUp(index) {
  while (index > 0) {
    const parent = Math.floor((index - 1) / 2);
    if (heap[parent] <= heap[index]) break; // min heap
    swap(heap, parent, index);
    index = parent;
  }
}
```

**Bubble Down Template:**
```typescript
bubbleDown(index) {
  while (true) {
    let minIdx = index;
    const left = 2 * index + 1;
    const right = 2 * index + 2;

    if (left < heap.length && heap[left] < heap[minIdx])
      minIdx = left;
    if (right < heap.length && heap[right] < heap[minIdx])
      minIdx = right;

    if (minIdx === index) break;
    swap(heap, index, minIdx);
    index = minIdx;
  }
}
```

For max heap, flip comparison: < becomes >
```

---

## Encouragement Messages

Use these based on context:

**After struggle:**
"Heaps are tricky at first. The min/max confusion is normal. You're building intuition!"

**After success:**
"Excellent! You recognized the pattern. That's the key skill."

**Mid-session:**
"Halfway there! You're mastering one of the most practical data structures."

**After using hints:**
"Using hints is smart. You're learning the pattern, which is the goal."

---

[Back to Session README](./README.md)
