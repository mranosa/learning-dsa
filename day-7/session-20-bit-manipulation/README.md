# Day 7, Session 20: Bit Manipulation

## Overview
Master bit manipulation techniques - essential for optimizing memory usage and solving unique interview problems efficiently.

**Duration:** 2-4 hours
**Problems:** 10 (5 Easy, 5 Medium)
**Prerequisites:** Understanding of binary numbers and basic boolean operations

---

## Learning Objectives

By the end of this session, you will:
- ✅ Understand binary representation and bit operations
- ✅ Master XOR, AND, OR, NOT, and shift operations
- ✅ Recognize bit manipulation patterns in problems
- ✅ Solve problems with O(1) space using bits
- ✅ Optimize solutions using bit tricks

---

## Session Flow

### 1. Video (20 min)
Watch the assigned video on Bit Manipulation fundamentals and common patterns.

### 2. Concept Check (10 min)
Claude will quiz you on:
- Binary number system
- Bitwise operators (AND, OR, XOR, NOT)
- Bit shifting operations
- Common bit manipulation tricks

### 3. Tips & Tricks (5 min)
Learn interview-specific insights about:
- XOR properties for finding unique elements
- Bit masking techniques
- Counting set bits efficiently
- TypeScript bitwise operation gotchas

### 4. Problem Solving (2-3 hours)
Solve 10 carefully selected problems:
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
- **AND (&)** - Sets bit to 1 if both bits are 1
- **OR (|)** - Sets bit to 1 if at least one bit is 1
- **XOR (^)** - Sets bit to 1 if bits are different
- **NOT (~)** - Flips all bits
- **Left Shift (<<)** - Shifts bits left, multiplies by 2
- **Right Shift (>>)** - Shifts bits right, divides by 2

### Common Bit Tricks
- **Check if power of 2:** n & (n-1) == 0
- **Get i-th bit:** (n >> i) & 1
- **Set i-th bit:** n | (1 << i)
- **Clear i-th bit:** n & ~(1 << i)
- **Toggle i-th bit:** n ^ (1 << i)
- **Count set bits:** Brian Kernighan's algorithm

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

**Nice to have:**
- Understanding of hexadecimal
- Two's complement representation
- Basic computer architecture

---

## Success Criteria

You're ready to move on when you can:
- [ ] Convert between decimal and binary mentally
- [ ] Apply all bitwise operators correctly
- [ ] Solve bit manipulation problems efficiently
- [ ] Recognize when to use XOR for uniqueness
- [ ] Implement common bit tricks from memory

---

## Resources

**Video:** See LESSON.md for link

**Readings:**
- Bit Twiddling Hacks: https://graphics.stanford.edu/~seander/bithacks.html
- Binary operations: MDN Web Docs

**Practice:**
- All problems in PROBLEMS.md
- Solutions in SOLUTIONS.md
- Hints in HINTS.md

---

## Tips for Success

1. **Draw binary representations** - Visualize the bits
2. **Work through examples** - Trace operations step by step
3. **Master XOR first** - It's the most useful for interviews
4. **Learn the patterns** - Many problems use similar tricks
5. **Practice mental binary conversion** - Speed matters
6. **Consider edge cases** - Negative numbers, overflow
7. **Think about space optimization** - Bits can replace arrays

---

## Common Mistakes

**Avoid these:**
- ❌ Forgetting about negative numbers (two's complement)
- ❌ Not handling overflow in TypeScript/JavaScript
- ❌ Confusing logical (&&, ||) with bitwise (&, |) operators
- ❌ Using signed right shift (>>) when >>> is needed
- ❌ Not considering 32-bit integer limits in JavaScript

---

## What's Next

After completing this session:
1. Take a 10-minute break
2. Review your performance scores
3. Note your action items
4. Move to Session 21: Mixed Review

Session 21 is the final review session covering the hardest Blind 75 problems.

---

**Ready to start?** Say: `"Claude, start session 7 20"`