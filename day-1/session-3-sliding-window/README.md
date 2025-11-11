# Day 1, Session 3: Sliding Window

## Overview
Master the sliding window technique - a powerful pattern for optimizing array/string problems from O(n²) to O(n).

**Duration:** 3-5 hours
**Problems:** 10 (1 Easy, 7 Medium, 2 Hard)
**Prerequisites:** Arrays, hash maps, two pointers

---

## Learning Objectives

By the end of this session, you will:
- ✅ Understand fixed-size vs variable-size sliding windows
- ✅ Recognize when to apply sliding window optimization
- ✅ Master the expand/contract technique
- ✅ Handle multiple constraints in window problems
- ✅ Optimize from brute force O(n²) to O(n)

---

## Session Flow

### 1. Video (25 min)
Watch the assigned video on Sliding Window technique and patterns.

### 2. Concept Check (10 min)
Claude will quiz you on:
- Fixed vs variable windows
- When to expand vs contract
- Time complexity improvements
- Common sliding window patterns

### 3. Tips & Tricks (5 min)
Learn interview-specific insights about:
- Recognizing sliding window problems
- Template for variable-size windows
- Handling edge cases
- TypeScript optimization tips

### 4. Problem Solving (3-4 hours)
Solve 10 carefully selected problems:
1. Best Time to Buy and Sell Stock (Easy)
2. Longest Substring Without Repeating Characters (Medium)
3. Longest Repeating Character Replacement (Medium)
4. Permutation in String (Medium)
5. Minimum Window Substring (Hard)
6. Sliding Window Maximum (Hard)
7. Maximum Sum of Distinct Subarrays (Medium)
8. Fruits Into Baskets (Medium)
9. Longest Substring with At Most K Distinct Characters (Medium)
10. Minimum Size Subarray Sum (Medium)

---

## Key Concepts

### Sliding Window Types
- **Fixed-size window:** Window size remains constant
- **Variable-size window:** Window expands and contracts
- **Two-pointer variation:** Start and end pointers

### Common Patterns
- **Maximum/Minimum window:** Find optimal window meeting criteria
- **Count valid windows:** Count all windows satisfying condition
- **Substring problems:** Find substrings with specific properties
- **Subarray sum:** Find subarrays with target sum/product

### Time Complexity
- **Brute force:** O(n²) or O(n³) - check all subarrays
- **Sliding window:** O(n) - each element visited at most twice
- **With sorting:** O(n log n) - when order doesn't matter

### Window Management
- **Expand:** Move right pointer to include more elements
- **Contract:** Move left pointer to maintain validity
- **Update:** Track window state with hash maps/counters

---

## Prerequisites

**Must know:**
- Two pointers technique
- Hash maps for frequency counting
- Basic string/array manipulation

**Nice to have:**
- Experience with substring problems
- Understanding of amortized analysis
- Familiarity with deques

---

## Success Criteria

You're ready to move on when you can:
- [ ] Identify sliding window problems immediately
- [ ] Choose between fixed and variable window
- [ ] Implement the expand-contract pattern
- [ ] Solve Medium sliding window problems in <25 min
- [ ] Optimize from O(n²) to O(n) consistently

---

## Resources

**Video:** See LESSON.md for link

**Readings:**
- Sliding Window Patterns: leetcode.com/explore
- Template solutions: SOLUTIONS.md

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Draw the window** - Visualize window movement
2. **Start with brute force** - Then optimize with sliding window
3. **Track window validity** - Know when to expand/contract
4. **Use hash maps** - For frequency/character counting
5. **Handle edge cases** - Empty input, single element
6. **Practice the template** - Variable window has a standard pattern
7. **Time yourself** - Speed matters in interviews

---

## Common Mistakes

**Avoid these:**
- ❌ Not handling empty strings/arrays
- ❌ Off-by-one errors with window boundaries
- ❌ Forgetting to update result before contracting
- ❌ Not considering all valid windows
- ❌ Using Set when frequency matters (use Map instead)

---

## What's Next

After completing this session:
1. Take a 15-minute break
2. Review your performance scores
3. Note patterns you struggled with
4. Move to Session 4: Stacks

Session 4 introduces LIFO data structures and monotonic stacks.

---

**Ready to start?** Say: `"Claude, start session 1 3"`