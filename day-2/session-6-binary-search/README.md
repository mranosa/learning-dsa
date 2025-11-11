# Day 2, Session 6: Binary Search

## Overview
Master the art of efficient searching with binary search - a cornerstone algorithm that reduces O(n) operations to O(log n).

**Duration:** 3-5 hours
**Problems:** 10 (3 Easy, 6 Medium, 1 Hard)
**Prerequisites:** Arrays, basic recursion, understanding of sorted data

---

## Learning Objectives

By the end of this session, you will:
- ✅ Understand binary search fundamentals and when to apply it
- ✅ Recognize binary search patterns in disguised problems
- ✅ Master iterative and recursive implementations
- ✅ Apply binary search on answer space (min/max problems)
- ✅ Handle edge cases in rotated and modified arrays
- ✅ Solve complex binary search variations

---

## Session Flow

### 1. Video (25 min)
Watch the assigned video on Binary Search fundamentals and patterns.

### 2. Concept Check (10 min)
Claude will quiz you on:
- Binary search invariants
- Left vs right boundary decisions
- When to use left <= right vs left < right
- Handling duplicates and edge cases

### 3. Tips & Tricks (5 min)
Learn interview-specific insights about:
- Template patterns for binary search
- Common off-by-one errors
- When to use mid = left + (right - left) / 2
- Binary search on answer space

### 4. Problem Solving (3-4 hours)
Solve 10 carefully selected problems:
1. Binary Search (Easy - LC 704)
2. Search in Rotated Sorted Array (Medium - LC 33)
3. Find Minimum in Rotated Sorted Array (Medium - LC 153)
4. Search a 2D Matrix (Medium - LC 74)
5. Koko Eating Bananas (Medium - LC 875)
6. Find Peak Element (Medium - LC 162)
7. Search Insert Position (Easy - LC 35)
8. First Bad Version (Easy - LC 278)
9. Time Based Key-Value Store (Medium - LC 981)
10. Median of Two Sorted Arrays (Hard - LC 4)

---

## Key Concepts

### Binary Search Fundamentals
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1) iterative, O(log n) recursive
- **Requirement:** Sorted array (or monotonic property)
- **Key Insight:** Eliminate half the search space each iteration

### Binary Search Templates

**Template 1: Basic Binary Search**
```typescript
while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);
    if (nums[mid] === target) return mid;
    if (nums[mid] < target) left = mid + 1;
    else right = mid - 1;
}
```

**Template 2: Find First/Last Position**
```typescript
while (left < right) {
    const mid = left + Math.floor((right - left) / 2);
    if (condition(mid)) right = mid; // or left = mid + 1
    else left = mid + 1; // or right = mid
}
```

### Common Patterns
- Classic binary search
- Search in rotated arrays
- Binary search on answer space
- Find peak/valley elements
- Search in 2D matrix
- Minimize/Maximize problems

---

## Prerequisites

**Must know:**
- Array manipulation in TypeScript
- While loops and recursion
- Basic mathematical operations
- Understanding of sorted order

**Nice to have:**
- Two pointers technique
- Logarithmic complexity understanding
- Divide and conquer concept

---

## Success Criteria

You're ready to move on when you can:
- [ ] Implement binary search bug-free from memory
- [ ] Choose the right template for each problem type
- [ ] Handle edge cases correctly (empty array, single element)
- [ ] Apply binary search to non-obvious problems
- [ ] Explain why binary search works and its invariants

---

## Resources

**Video:** See LESSON.md for link

**Readings:**
- Binary Search Patterns: https://leetcode.com/discuss/general-discussion/786126/
- TypeScript array methods: TYPESCRIPT-LEETCODE.md

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Draw it out** - Visualize the search space shrinking
2. **Track your pointers** - Know what left/right represent
3. **Check edge cases** - Empty array, single element, all same
4. **Avoid overflow** - Use left + (right - left) / 2
5. **Test boundaries** - Check off-by-one errors
6. **Think monotonic** - Binary search works on any monotonic property
7. **Practice templates** - Master the 2-3 core patterns

---

## Common Mistakes

**Avoid these:**
- ❌ Infinite loops from incorrect pointer updates
- ❌ Off-by-one errors in boundaries
- ❌ Integer overflow with (left + right) / 2
- ❌ Wrong template for the problem type
- ❌ Not handling duplicates correctly
- ❌ Missing edge cases (array boundaries)

---

## What's Next

After completing this session:
1. Take a 15-minute break
2. Review your performance scores
3. Note patterns you struggled with
4. Move to Session 7: Tree Traversals

Session 7 introduces tree structures and traversal patterns, building on your understanding of recursive thinking from binary search.

---

**Ready to start?** Say: `"Claude, start session 2 6"`