# Day 2, Session 4: Two Pointers

## Overview
Master the two pointers technique - a powerful pattern for optimizing array and string problems from O(n²) to O(n).

**Duration:** 2-4 hours
**Problems:** 10 (3 Easy, 6 Medium, 1 Hard)
**Prerequisites:** Basic array manipulation, understanding of time complexity

---

## Learning Objectives

By the end of this session, you will:
- ✅ Understand when and why to use two pointers
- ✅ Master opposite directional two pointers
- ✅ Master same directional two pointers (fast/slow)
- ✅ Solve classic two pointers problems efficiently
- ✅ Recognize two pointers patterns in interview questions

---

## Session Flow

### 1. Video (20 min)
Watch the assigned video on Two Pointers technique and common patterns.

### 2. Concept Check (10 min)
Claude will quiz you on:
- When to use two pointers
- Opposite vs same direction patterns
- Time complexity improvements
- Common two pointers scenarios

### 3. Tips & Tricks (5 min)
Learn interview-specific insights about:
- Recognizing two pointers problems
- Avoiding common pitfalls
- TypeScript-specific optimizations

### 4. Problem Solving (2-3 hours)
Solve 10 carefully selected problems:
1. Valid Palindrome (Easy)
2. Two Sum II - Input Array Is Sorted (Medium)
3. 3Sum (Medium)
4. Container With Most Water (Medium)
5. Trapping Rain Water (Hard)
6. Remove Duplicates from Sorted Array (Easy)
7. Move Zeroes (Easy)
8. Sort Colors (Medium)
9. Partition Labels (Medium)
10. Boats to Save People (Medium)

---

## Key Concepts

### Two Pointers Patterns
- **Opposite Direction:** Start from both ends, move inward
- **Same Direction (Fast/Slow):** Different speeds or conditions
- **Sliding Window:** Fixed or variable size window (preview)
- **Multiple Pointers:** 3+ pointers for complex problems

### Common Scenarios
- **Palindrome checking:** O(n) instead of O(n²)
- **Pair/triplet finding:** O(n) or O(n²) instead of O(n²) or O(n³)
- **In-place operations:** O(1) space complexity
- **Partitioning:** Dutch National Flag, quicksort partition

### Time Complexity Improvements
- Nested loops → Single pass: O(n²) → O(n)
- Triplet search: O(n³) → O(n²)
- Sorted array operations: Leverage ordering

---

## Prerequisites

**Must know:**
- Array manipulation in TypeScript
- Basic sorting understanding
- Time complexity analysis

**Nice to have:**
- Experience with nested loops
- Understanding of in-place operations

---

## Success Criteria

You're ready to move on when you can:
- [ ] Identify when two pointers is optimal
- [ ] Choose between opposite/same direction patterns
- [ ] Solve Easy two pointers problems in <10 min
- [ ] Solve Medium two pointers problems in <20 min
- [ ] Explain why two pointers reduces complexity

---

## Resources

**Video:** See LESSON.md for link

**Readings:**
- Two Pointers Pattern: https://leetcode.com/discuss/study-guide/1688903/
- In-place algorithms: TYPESCRIPT-LEETCODE.md

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Visualize with examples** - Draw the pointers moving
2. **Consider sorted vs unsorted** - Sorting may enable two pointers
3. **Watch for off-by-one errors** - Pointer boundaries are critical
4. **Practice pointer movement logic** - When to move which pointer
5. **Think about invariants** - What stays true throughout
6. **Consider edge cases** - Empty, single element, all same
7. **Time yourself** - Build speed with the pattern

---

## Common Mistakes

**Avoid these:**
- ❌ Moving both pointers simultaneously without logic
- ❌ Forgetting to handle pointer crossing
- ❌ Not considering when arrays need sorting first
- ❌ Off-by-one errors with pointer boundaries
- ❌ Using two pointers when hash map is better

---

## What's Next

After completing this session:
1. Take a 10-minute break
2. Review your performance scores
3. Note patterns you struggled with
4. Move to Session 5: Binary Search

Session 5 builds on sorted array concepts with logarithmic search techniques.

---

**Ready to start?** Say: `"Claude, start session 2 4"`