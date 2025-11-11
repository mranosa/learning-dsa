# Interviewer Script: Binary Search Session

## Session Introduction

**Claude:** Welcome to Session 6 on Binary Search! This is a fundamental algorithm that transforms O(n) searches into O(log n) operations. Before we dive into problems, let me assess your understanding of the core concepts.

---

## Concept Check Questions

### Question 1: Binary Search Basics
**Claude:** "Can you explain why binary search requires a sorted array? What would happen if we tried to use it on an unsorted array?"

**Expected Answer:** Binary search works by eliminating half of the search space based on comparisons. This only works if elements are ordered - otherwise, we can't determine which half contains our target.

**Follow-up:** "What's the time complexity of binary search and why?"

### Question 2: Template Understanding
**Claude:** "When would you use `while (left <= right)` versus `while (left < right)` in binary search?"

**Expected Answer:**
- `left <= right` for finding exact matches (search space is inclusive)
- `left < right` for finding boundaries or positions (avoiding infinite loops)

### Question 3: Overflow Prevention
**Claude:** "Why do we calculate mid as `left + (right - left) / 2` instead of `(left + right) / 2`?"

**Expected Answer:** To prevent integer overflow when left and right are large numbers.

---

## Problem Walkthroughs

### Problem 1: Binary Search

**Initial Question:**
"Let's start with the classic binary search problem. Given a sorted array and a target, return the index if found, or -1 if not found."

**UMPIRE Guidance:**

**Understand:**
- "Is the array guaranteed to be sorted?"
- "Are all elements unique?"
- "What should I return if the array is empty?"

**Match:**
"This is a classic binary search problem - we can eliminate half the search space with each comparison."

**Plan:**
```
1. Initialize left = 0, right = array.length - 1
2. While left <= right:
   - Calculate mid
   - Compare with target
   - Adjust search space
3. Return -1 if not found
```

**Implementation Check:**
- Watch for: Off-by-one errors, overflow prevention
- If stuck: "Think about what each pointer represents"

**Review:**
"What's the time complexity? Space complexity? Any edge cases we should test?"

**Evaluate:**
"Can you trace through your solution with the array [1,3,5,7,9] searching for 5?"

---

### Problem 4: Search a 2D Matrix

**Transition:**
"Good work! Now let's apply binary search to a 2D matrix. Each row is sorted, and the first element of each row is greater than the last element of the previous row."

**Key Insights to Guide:**
- "How would this matrix look if we flattened it into a 1D array?"
- "Can you convert a 1D index to 2D coordinates?"

**If Struggling:**
"Let's think about it differently - if we have index 5 in a flattened array, and the matrix has 3 columns, which row and column would that be?"

---

### Problem 5: Koko Eating Bananas

**Transition:**
"Excellent! Now let's look at a different type of binary search - searching for an answer rather than in an array."

**Problem Introduction:**
"Koko needs to eat all bananas within h hours. She eats at a constant speed k bananas per hour. Find the minimum k."

**Guiding Questions:**
- "What's the minimum possible eating speed?"
- "What's the maximum eating speed we need to consider?"
- "If Koko can eat all bananas at speed k, can she eat them at speed k+1?"

**Key Insight:**
"Notice that if speed k works, all speeds greater than k also work. This creates a monotonic property we can binary search on!"

---

### Problem 10: Median of Two Sorted Arrays

**Transition:**
"Let's tackle a challenging problem - finding the median of two sorted arrays in O(log(m+n)) time."

**Building Understanding:**
1. "What does the median represent in terms of array partitioning?"
2. "If we partition both arrays, what property should the partitions have?"

**Approach Guidance:**
- "We need to find a partition where all left elements <= all right elements"
- "Binary search on the smaller array for efficiency"
- "The partition positions are related: i + j = (m + n + 1) / 2"

**Implementation Hints:**
- Handle edge cases: "What if partition is at position 0?"
- "Use -Infinity and Infinity for boundary cases"

---

## Common Mistakes to Address

### Mistake 1: Infinite Loops
**When you see:** Code running forever
**Say:** "Let's trace through your loop. Are your pointers always moving toward termination?"

### Mistake 2: Off-by-One Errors
**When you see:** Wrong answer by 1 position
**Say:** "Let's be clear about what left and right represent. Are they inclusive or exclusive bounds?"

### Mistake 3: Not Handling Edge Cases
**When you see:** Missing edge case checks
**Say:** "What happens with an empty array? Single element? Target at boundaries?"

---

## Encouragement Messages

### When They're Stuck:
- "Binary search can be tricky with boundaries. Let's draw out a small example."
- "Think about what property allows us to eliminate half the search space."
- "Sometimes it helps to think about the invariant - what's always true about left and right?"

### When They Solve It:
- "Excellent! You correctly identified the binary search pattern."
- "Great job handling those edge cases!"
- "Nice optimization using binary search on the answer space!"

---

## Time Management

### Pacing Guidelines:
- Concept check: 10 minutes
- Easy problems (1, 7, 8): 15-20 minutes each
- Medium problems (2, 3, 4, 5, 6, 9): 25-35 minutes each
- Hard problem (10): 40-50 minutes

### When Running Behind:
"Let's move to the next problem and come back if we have time. The key is understanding the patterns."

### When Running Ahead:
"Great pace! Let's discuss some variations. What if the array had duplicates? What if we wanted all occurrences?"

---

## Problem Difficulty Progression

1. **Warm-up** (Problems 1, 7, 8): Standard templates
2. **Core Concepts** (Problems 2, 3, 6): Modified binary search
3. **Advanced** (Problems 4, 5, 9): Creative applications
4. **Challenge** (Problem 10): Complex logic

---

## Key Teaching Points

### For Each Problem Type:

**Classic Binary Search:**
- Emphasize the importance of sorted input
- Focus on loop invariants

**Rotated Arrays:**
- "At least one half is always sorted"
- Draw the array to visualize

**Binary Search on Answer:**
- "We're searching a range of possible answers"
- "Find the monotonic property"

**2D Matrix:**
- "Think of it as a flattened 1D array"
- Practice index conversion

---

## Session Wrap-up

### Review Questions:
1. "What are the three main binary search templates we used?"
2. "When can we apply binary search beyond sorted arrays?"
3. "What was the most challenging aspect for you?"

### Action Items:
- "Practice implementing binary search from memory"
- "Try to recognize binary search patterns in other problems"
- "Review the problems you found difficult"

### Encouragement:
"Binary search is one of those algorithms that seems simple but has many nuances. You did great working through these patterns. The more you practice, the more natural it becomes. Remember - if you can eliminate half the possibilities at each step, think binary search!"

---

## Follow-up Suggestions

If the student wants more practice:
1. "Try implementing binary search recursively"
2. "Look for binary search applications in system design (load balancing, distributed systems)"
3. "Practice with problems involving floating-point binary search"

If moving to next session:
"Great work with binary search! Next, we'll explore tree traversals, where we'll see similar divide-and-conquer thinking applied to tree structures."