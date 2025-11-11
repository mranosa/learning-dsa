# Day 2, Session 5: Fast/Slow Pointers

## Overview
Master the tortoise and hare algorithm pattern for cycle detection and linked list manipulation.

**Duration:** 2-4 hours
**Problems:** 10 (5 Easy, 5 Medium)
**Prerequisites:** Linked Lists, Basic pointer manipulation

---

## Learning Objectives

By the end of this session, you will:
- ✅ Understand Floyd's cycle detection algorithm
- ✅ Apply fast/slow pointer pattern to various problems
- ✅ Detect cycles in linked lists and sequences
- ✅ Find middle elements efficiently
- ✅ Solve intersection and reordering problems

---

## Session Flow

### 1. Video (20 min)
Watch the assigned video on Fast/Slow Pointers and Floyd's algorithm.

### 2. Concept Check (10 min)
Claude will quiz you on:
- Floyd's cycle detection principle
- Fast vs slow pointer movement rates
- Cycle detection mathematics
- Common fast/slow pointer patterns

### 3. Tips & Tricks (5 min)
Learn interview-specific insights about:
- When to use fast/slow pointers
- Choosing pointer speeds
- Handling edge cases in linked lists

### 4. Problem Solving (2-3 hours)
Solve 10 carefully selected problems:
1. Linked List Cycle (Easy)
2. Linked List Cycle II (Medium)
3. Happy Number (Easy)
4. Middle of the Linked List (Easy)
5. Find the Duplicate Number (Medium)
6. Remove Nth Node From End of List (Medium)
7. Reorder List (Medium)
8. Palindrome Linked List (Easy)
9. Circular Array Loop (Medium)
10. Intersection of Two Linked Lists (Easy)

---

## Key Concepts

### Floyd's Cycle Detection
- **Tortoise:** Moves one step at a time
- **Hare:** Moves two steps at a time
- **Cycle exists:** If they meet
- **No cycle:** If hare reaches end

### Fast/Slow Pointer Speeds
- **Standard:** Slow = 1 step, Fast = 2 steps
- **Finding middle:** Fast moves 2x speed
- **Nth from end:** Fast leads by n nodes
- **Cycle entry:** Reset one to head after meeting

### Common Applications
- Cycle detection in lists
- Finding middle element
- Detecting loops in sequences
- Finding duplicate numbers
- Palindrome checking with reversal

### Time Complexity Benefits
- **Cycle detection:** O(n) time, O(1) space
- **Middle finding:** O(n) time, O(1) space
- **No extra data structures needed**

---

## Prerequisites

**Must know:**
- Linked list structure and traversal
- Pointer manipulation in TypeScript
- Basic modular arithmetic

**Nice to have:**
- Understanding of graph cycles
- Mathematical proof concepts
- Two-pointer technique basics

---

## Success Criteria

You're ready to move on when you can:
- [ ] Implement Floyd's algorithm from memory
- [ ] Identify when to use fast/slow pointers
- [ ] Handle edge cases (null, single node, etc.)
- [ ] Find cycle entry points
- [ ] Apply pattern to array problems

---

## Resources

**Video:** See LESSON.md for link

**Readings:**
- Floyd's Algorithm: https://en.wikipedia.org/wiki/Cycle_detection
- Linked List patterns: TYPESCRIPT-LEETCODE.md

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Draw diagrams** - Visualize pointer movement
2. **Test edge cases** - Empty list, single node, no cycle
3. **Count steps carefully** - Track distance relationships
4. **Consider pointer speeds** - Not always 1 and 2
5. **Practice null checks** - TypeScript type safety
6. **Understand the math** - Why they meet in cycles
7. **Time yourself** - Build speed with practice

---

## Common Mistakes

**Avoid these:**
- ❌ Forgetting null checks for linked lists
- ❌ Incorrect loop termination conditions
- ❌ Not handling single-node lists
- ❌ Confusing cycle detection with cycle entry
- ❌ Using extra space when O(1) is possible

---

## What's Next

After completing this session:
1. Take a 10-minute break
2. Review your performance scores
3. Note patterns you struggled with
4. Move to Session 6: Merge Intervals

Session 6 introduces interval manipulation and overlap detection patterns.

---

**Ready to start?** Say: `"Claude, start session 2 5"`