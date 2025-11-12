# Day 7, Session 20: Bit Manipulation

## Overview

Master bit manipulation - essential for optimization problems and solving unique interview challenges efficiently.

**Duration:** 2-4 hours | **Problems:** 10 (5 Easy, 5 Medium)

---

## Learning Objectives

- ✅ Understand binary representation and bit operations
- ✅ Master XOR, AND, OR, NOT, and shift operations
- ✅ Recognize bit manipulation patterns
- ✅ Solve problems with O(1) space using bits
- ✅ Apply bit tricks for optimization

---

## Session Flow

### 1. Videos (47 min)
- Binary & Bitwise Operators (15 min)
- XOR Properties & Applications (12 min)
- Bit Manipulation Patterns (20 min)

### 2. Concept Check (10 min)
Quiz on binary system, bitwise operators, XOR properties, bit tricks.

### 3. Tips & Tricks (5 min)
XOR for uniqueness, bit masking, counting set bits, TypeScript gotchas.

### 4. Problems (2-3 hours)
1. Single Number (Easy)
2. Number of 1 Bits (Easy)
3. Counting Bits (Easy)
4. Reverse Bits (Easy)
5. Missing Number (Easy)
6. Sum of Two Integers (Medium)
7. Single Number II (Medium)
8. Single Number III (Medium)
9. Bitwise AND of Numbers Range (Medium)
10. Maximum XOR of Two Numbers (Medium)

---

## Key Concepts

### Bitwise Operators
- **AND (&)** - Both bits must be 1
- **OR (|)** - At least one bit must be 1
- **XOR (^)** - Bits must be different
- **NOT (~)** - Flips all bits
- **Left Shift (<<)** - Multiply by 2^n
- **Right Shift (>>)** - Divide by 2^n (signed)
- **Right Shift (>>>)** - Divide by 2^n (unsigned)

### Common Bit Tricks
- **Check power of 2:** n & (n-1) == 0
- **Get i-th bit:** (n >> i) & 1
- **Set i-th bit:** n | (1 << i)
- **Clear i-th bit:** n & ~(1 << i)
- **Toggle i-th bit:** n ^ (1 << i)
- **Count set bits:** n & (n-1) removes rightmost set bit

### XOR Properties
- a ^ 0 = a
- a ^ a = 0
- a ^ b = b ^ a (commutative)
- (a ^ b) ^ c = a ^ (b ^ c) (associative)

---

## Prerequisites

**Must know:**
- Binary number representation
- Basic boolean logic
- TypeScript number operations

---

## Success Criteria

- [ ] Convert between decimal and binary
- [ ] Apply all bitwise operators correctly
- [ ] Solve Easy problems <15 min
- [ ] Recognize when to use XOR
- [ ] Implement bit tricks from memory

---

## Resources

**Video:** LESSON.md
**Practice:** PROBLEMS.md
**Solutions:** SOLUTIONS.md
**Hints:** HINTS.md

---

## Tips

1. Watch all videos - visualize bit operations
2. Do concept check - reveals gaps
3. Draw binary representations
4. Master XOR first - most useful
5. Practice mental binary conversion
6. Think aloud - explain bit operations
7. Review solutions even if correct

---

## Common Mistakes

- ❌ Forgetting negative numbers (two's complement)
- ❌ Not handling overflow in JavaScript
- ❌ Confusing logical (&&, ||) with bitwise (&, |)
- ❌ Using signed (>>) when unsigned (>>>) needed
- ❌ Not considering 32-bit integer limits
- ❌ Ignoring XOR properties

---

## What's Next

After completion:
1. 10-minute break
2. Review scores
3. Note action items
4. Session 21: Mixed Review

Session 21 covers the hardest Blind 75 problems in a final comprehensive review.

---

**Ready?** Say: `"Claude, start session 7 20"`
