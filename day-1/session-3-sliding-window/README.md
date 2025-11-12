# Day 1, Session 3: Sliding Window

## Overview

Optimize array/string problems from O(n²) to O(n) using window technique.

**Duration:** 2-4 hours | **Problems:** 10 (1 Easy, 9 Medium)

---

## Learning Objectives

- ✅ Master fixed-size windows
- ✅ Master variable-size windows
- ✅ Use expand/contract pattern
- ✅ Recognize sliding window problems
- ✅ Optimize from O(n²) to O(n)

---

## Session Flow

### 1. Videos (35 min)
- Sliding Window Fundamentals (10 min)
- Fixed vs Variable Windows (12 min)
- Advanced Patterns (13 min)

### 2. Concept Check (10 min)
Quiz on window types, when to expand/contract, complexity.

### 3. Tips & Tricks (5 min)
Pattern recognition, TypeScript gotchas, interview insights.

### 4. Problems (2-3 hours)
1. Best Time to Buy/Sell Stock (Easy)
2. Longest Substring Without Repeating Characters (Medium)
3. Longest Repeating Character Replacement (Medium)
4. Permutation in String (Medium)
5. Minimum Window Substring (Medium)
6. Maximum Sum of Distinct Subarrays (Medium)
7. Fruits Into Baskets (Medium)
8. Longest Substring with At Most K Distinct Characters (Medium)
9. Minimum Size Subarray Sum (Medium)
10. Sliding Window Maximum (Medium)

---

## Key Concepts

### Window Types
- **Fixed-size** - Size stays constant (k elements)
- **Variable-size** - Expand/contract based on condition
- **Two-pointer** - Start/end pointers variation

### Complexity
- **Brute force:** O(n²) or O(n³)
- **Sliding window:** O(n) - each element visited ≤2 times
- **Space:** O(1) to O(k)

### Patterns
- Maximum/minimum window
- Count valid windows
- Substring with constraints
- Subarray sum/product

---

## Prerequisites

**Must know:**
- Arrays and two pointers
- Hash maps/Sets
- String manipulation

---

## Success Criteria

- [ ] Identify sliding window problems
- [ ] Choose fixed vs variable window
- [ ] Implement expand-contract pattern
- [ ] Solve Medium problems <25 min
- [ ] Optimize from O(n²) to O(n)

---

## Resources

**Video:** LESSON.md
**Practice:** PROBLEMS.md
**Solutions:** SOLUTIONS.md
**Hints:** HINTS.md

---

## Tips

1. Draw the window - visualize movement
2. Start with brute force - optimize with window
3. Track window validity - know when to expand/contract
4. Use Map for frequencies
5. Handle edge cases (empty, single element)
6. Time yourself

---

## Common Mistakes

- ❌ Not handling empty input
- ❌ Off-by-one errors
- ❌ Forgetting to update result before contracting
- ❌ Using Set when frequency matters (use Map)
- ❌ Not checking if window size > array length

---

## What's Next

After completion:
1. 10-minute break
2. Review scores
3. Note problem patterns
4. Session 4: Stacks

Session 4 introduces LIFO data structures and monotonic stacks.

---

**Ready?** Say: `"Claude, start session 1 3"`
