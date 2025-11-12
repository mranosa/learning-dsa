# Day 2, Session 5: Fast/Slow Pointers

## Overview

Master Floyd's tortoise and hare algorithm for cycle detection and linked list manipulation.

**Duration:** 2-4 hours | **Problems:** 10 (5 Easy, 5 Medium)

---

## Learning Objectives

- ✅ Understand Floyd's cycle detection
- ✅ Apply fast/slow pointer pattern
- ✅ Detect cycles efficiently
- ✅ Find middle elements in O(1) space
- ✅ Solve intersection problems

---

## Session Flow

### 1. Videos (22 min)
- Fast/Slow Pointers Fundamentals (9 min)
- Floyd's Algorithm Deep Dive (8 min)
- Advanced Applications (5 min)

### 2. Concept Check (10 min)
Quiz on Floyd's algorithm, pointer speeds, cycle detection.

### 3. Tips & Tricks (5 min)
Pattern recognition, edge cases, TypeScript null handling.

### 4. Problems (2-3 hours)
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
- **Slow:** 1 step per iteration
- **Fast:** 2 steps per iteration
- **Cycle exists:** Pointers meet
- **No cycle:** Fast reaches end

### Pointer Speeds
- **1 and 2:** Standard cycle detection
- **Same speed:** Finding cycle entry after detection
- **Gap of n:** Finding nth from end

### Applications
- Cycle detection: O(n) time, O(1) space
- Middle element: O(n) time, O(1) space
- Duplicate numbers in arrays
- Palindrome checking

---

## Prerequisites

**Must know:**
- Linked list structure
- Pointer manipulation
- Basic TypeScript syntax

---

## Success Criteria

- [ ] Implement Floyd's algorithm from memory
- [ ] Identify when to use fast/slow pointers
- [ ] Handle edge cases (null, single node)
- [ ] Find cycle entry points
- [ ] Apply pattern to array problems

---

## Resources

**Video:** LESSON.md
**Practice:** PROBLEMS.md
**Solutions:** SOLUTIONS.md
**Hints:** HINTS.md

---

## Tips

1. Draw diagrams - visualize pointer movement
2. Test edge cases - empty, single node, no cycle
3. Count steps carefully - track relationships
4. Practice null checks - TypeScript safety
5. Understand the math - why they meet
6. Time yourself - build speed
7. Review solutions even if correct

---

## Common Mistakes

- ❌ Forgetting null checks
- ❌ Wrong loop condition (use `fast && fast.next`)
- ❌ Confusing cycle detection with cycle entry
- ❌ Not handling single-node lists
- ❌ Using extra space when O(1) possible

---

## What's Next

After completion:
1. 10-minute break
2. Review scores
3. Note action items
4. Session 6: Merge Intervals

Session 6 introduces interval manipulation and overlap detection.

---

**Ready?** Say: `"Claude, start session 2 5"`
