# Lesson: Bit Manipulation

## Overview
Bit manipulation is a powerful technique that operates directly on the binary representation of numbers. It's essential for system programming, optimization, and solving specific interview problems efficiently.

---

## Video Assignment
**Watch:** [NeetCode - Bit Manipulation](https://www.youtube.com/watch?v=5rtVTYAk9KQ) (20 minutes)

Take notes on:
- Binary number system basics
- All bitwise operators and their use cases
- XOR properties and applications
- Common bit manipulation patterns

---

## Core Concepts

### 1. Binary Number System

**Decimal to Binary Conversion:**
```typescript
// 13 in decimal = 1101 in binary
// 8 + 4 + 0 + 1 = 13
// Positions: 2³ 2² 2¹ 2⁰
```

**Two's Complement (for negative numbers):**
```typescript
// -5 in 8-bit: 11111011
// Step 1: Binary of 5 = 00000101
// Step 2: Invert bits = 11111010
// Step 3: Add 1 = 11111011
```

### 2. Bitwise Operators

**AND (&) - Both bits must be 1:**
```typescript
// 5 & 3 = 1
// 0101 & 0011 = 0001
const result = 5 & 3; // 1
```

**OR (|) - At least one bit must be 1:**
```typescript
// 5 | 3 = 7
// 0101 | 0011 = 0111
const result = 5 | 3; // 7
```

**XOR (^) - Bits must be different:**
```typescript
// 5 ^ 3 = 6
// 0101 ^ 0011 = 0110
const result = 5 ^ 3; // 6
```

**NOT (~) - Flip all bits:**
```typescript
// ~5 = -6 (in two's complement)
// ~00000101 = 11111010 (which is -6)
const result = ~5; // -6
```

**Left Shift (<<) - Multiply by 2ⁿ:**
```typescript
// 5 << 1 = 10
// 0101 << 1 = 1010
const result = 5 << 1; // 10
```

**Right Shift (>>) - Divide by 2ⁿ:**
```typescript
// 5 >> 1 = 2
// 0101 >> 1 = 0010
const result = 5 >> 1; // 2
```

### 3. XOR Properties

**Key Properties:**
```typescript
// Identity
a ^ 0 = a

// Self-inverse
a ^ a = 0

// Commutative
a ^ b = b ^ a

// Associative
(a ^ b) ^ c = a ^ (b ^ c)

// Finding unique element
[1,2,1,2,3] -> 1^2^1^2^3 = 3
```

### 4. Common Bit Manipulation Tricks

**Check if number is power of 2:**
```typescript
function isPowerOfTwo(n: number): boolean {
    return n > 0 && (n & (n - 1)) === 0;
}
// 8 & 7 = 1000 & 0111 = 0000 ✓
```

**Count set bits (Brian Kernighan):**
```typescript
function countSetBits(n: number): number {
    let count = 0;
    while (n > 0) {
        n &= (n - 1); // Removes rightmost set bit
        count++;
    }
    return count;
}
```

**Get i-th bit:**
```typescript
function getBit(n: number, i: number): number {
    return (n >> i) & 1;
}
```

**Set i-th bit:**
```typescript
function setBit(n: number, i: number): number {
    return n | (1 << i);
}
```

**Clear i-th bit:**
```typescript
function clearBit(n: number, i: number): number {
    return n & ~(1 << i);
}
```

**Toggle i-th bit:**
```typescript
function toggleBit(n: number, i: number): number {
    return n ^ (1 << i);
}
```

---

## Problem-Solving Patterns

### Pattern 1: XOR for Finding Unique Elements

**Single unique element:**
```typescript
// All elements appear twice except one
function singleNumber(nums: number[]): number {
    return nums.reduce((acc, num) => acc ^ num, 0);
}
```

### Pattern 2: Bit Masking

**Using bits as flags:**
```typescript
// Represent a set of permissions
const READ = 1 << 0;    // 001
const WRITE = 1 << 1;   // 010
const EXECUTE = 1 << 2; // 100

let permissions = 0;
permissions |= READ;    // Add READ
permissions |= WRITE;   // Add WRITE

// Check permission
if (permissions & READ) {
    console.log("Has READ permission");
}

// Remove permission
permissions &= ~WRITE;
```

### Pattern 3: Bit Counting

**Counting bits in range:**
```typescript
function countBits(n: number): number[] {
    const result: number[] = new Array(n + 1);
    for (let i = 0; i <= n; i++) {
        // i >> 1 removes last bit, i & 1 checks if last bit is 1
        result[i] = result[i >> 1] + (i & 1);
    }
    return result;
}
```

### Pattern 4: Addition Without Arithmetic Operators

**Using XOR and AND:**
```typescript
function add(a: number, b: number): number {
    while (b !== 0) {
        const carry = (a & b) << 1; // Calculate carry
        a = a ^ b;  // Add without carry
        b = carry;  // Assign carry for next iteration
    }
    return a;
}
```

---

## TypeScript/JavaScript Specifics

### Important Notes:

1. **32-bit integers:** JavaScript bitwise operations work on 32-bit signed integers
```typescript
const max = 2147483647;  // 2^31 - 1
const min = -2147483648; // -2^31
```

2. **Unsigned right shift (>>>):**
```typescript
// >>> fills with zeros, >> preserves sign
-5 >> 1  // -3 (preserves sign)
-5 >>> 1 // 2147483645 (fills with 0)
```

3. **Number precision:**
```typescript
// Be careful with large numbers
const large = 1 << 31; // Overflows to negative
```

---

## Interview Tips

1. **Always clarify:**
   - Integer range and overflow handling
   - Negative number handling
   - Input constraints

2. **Common follow-ups:**
   - "Can you do it without extra space?" → Use bit manipulation
   - "Can you do it in one pass?" → Often involves XOR
   - "What about negative numbers?" → Discuss two's complement

3. **Optimization opportunities:**
   - Replace boolean arrays with bit vectors
   - Use XOR for swap without temp variable
   - Use bit shifts for multiplication/division by powers of 2

---

## Practice Problems

Start with these patterns:
1. **XOR problems:** Single Number series
2. **Bit counting:** Number of 1 Bits, Counting Bits
3. **Bit manipulation:** Reverse Bits, Missing Number
4. **Advanced:** Sum of Two Integers, Maximum XOR

---

## Quick Reference

```typescript
// Essential operations
n & (n-1)     // Remove rightmost set bit
n & -n        // Isolate rightmost set bit
n | (n+1)     // Set rightmost unset bit
~n & (n+1)    // Isolate rightmost unset bit

// Checking conditions
n & 1         // Check if odd
~n & 1        // Check if even
n & (n-1) === 0  // Check if power of 2

// Useful constants
0xFFFFFFFF    // All 1s (32-bit)
1 << i        // i-th bit mask
~(1 << i)     // Inverse i-th bit mask
```

---

## Summary

Bit manipulation is about:
1. **Efficiency:** O(1) space, often O(1) time operations
2. **Patterns:** XOR for uniqueness, masks for flags
3. **Tricks:** Power of 2 checks, bit counting, swapping
4. **Understanding:** Binary representation and two's complement

Master these fundamentals and you'll handle any bit manipulation problem!

---

---

## Advanced Topics

### Bit Manipulation in System Design

**1. Bloom Filters:**
```typescript
class BloomFilter {
    private bits: Uint8Array;
    private hashFunctions: ((str: string) => number)[];

    constructor(size: number, numHashes: number) {
        this.bits = new Uint8Array(Math.ceil(size / 8));
        // Initialize hash functions
    }

    add(item: string): void {
        for (const hash of this.hashFunctions) {
            const index = hash(item) % (this.bits.length * 8);
            const byteIndex = Math.floor(index / 8);
            const bitIndex = index % 8;
            this.bits[byteIndex] |= (1 << bitIndex);
        }
    }

    contains(item: string): boolean {
        for (const hash of this.hashFunctions) {
            const index = hash(item) % (this.bits.length * 8);
            const byteIndex = Math.floor(index / 8);
            const bitIndex = index % 8;
            if (!(this.bits[byteIndex] & (1 << bitIndex))) {
                return false;
            }
        }
        return true; // May be false positive
    }
}
```

**2. Permission Systems:**
```typescript
enum Permission {
    READ = 1 << 0,    // 001
    WRITE = 1 << 1,   // 010
    EXECUTE = 1 << 2, // 100
    DELETE = 1 << 3,  // 1000
}

class User {
    private permissions: number = 0;

    grant(permission: Permission): void {
        this.permissions |= permission;
    }

    revoke(permission: Permission): void {
        this.permissions &= ~permission;
    }

    hasPermission(permission: Permission): boolean {
        return (this.permissions & permission) === permission;
    }

    hasAnyPermission(permissions: Permission): boolean {
        return (this.permissions & permissions) !== 0;
    }
}
```

### Bit Tricks for Competitive Programming

**1. Fast modulo for powers of 2:**
```typescript
// n % (power of 2) = n & (power of 2 - 1)
function fastModulo(n: number, powerOf2: number): number {
    return n & (powerOf2 - 1);
}
// Example: 13 % 8 = 13 & 7 = 5
```

**2. Swap without temp variable:**
```typescript
function swap(a: number, b: number): [number, number] {
    a = a ^ b;
    b = a ^ b; // b = (a^b)^b = a
    a = a ^ b; // a = (a^b)^a = b
    return [a, b];
}
```

**3. Find position of rightmost set bit:**
```typescript
function rightmostSetBitPosition(n: number): number {
    if (n === 0) return -1;
    const isolated = n & -n;
    return Math.log2(isolated);
}
```

**4. Count trailing zeros:**
```typescript
function countTrailingZeros(n: number): number {
    if (n === 0) return 32;
    let count = 0;
    while ((n & 1) === 0) {
        count++;
        n >>>= 1;
    }
    return count;
}
```

### Performance Comparisons

**Bit operations vs Traditional approaches:**

```typescript
// Traditional vs Bit manipulation
// Example: Check if number is even

// Traditional - Division
function isEvenDivision(n: number): boolean {
    return n % 2 === 0;
}

// Bit manipulation - AND
function isEvenBit(n: number): boolean {
    return (n & 1) === 0;
}

// Performance: Bit operation is ~3-5x faster
```

### Common Interview Follow-ups

**1. "Why does XOR work for finding unique elements?"**

Answer: XOR has these properties:
- Commutative: a ^ b = b ^ a
- Associative: (a ^ b) ^ c = a ^ (b ^ c)
- Identity: a ^ 0 = a
- Self-inverse: a ^ a = 0

When all duplicates are XORed, they cancel out to 0, leaving only the unique element.

**2. "What's the difference between logical and bitwise operators?"**

```typescript
// Logical operators (&&, ||) - work with booleans
if (a > 0 && b > 0) { } // Short-circuits

// Bitwise operators (&, |) - work bit by bit
let result = a & b; // No short-circuit, operates on all bits
```

**3. "How do you handle overflow in bit manipulation?"**

```typescript
// JavaScript/TypeScript specific
// All bitwise operations work on 32-bit signed integers
const MAX_INT = 2147483647;  // 2^31 - 1
const MIN_INT = -2147483648; // -2^31

// Use >>> for unsigned operations
// Use BigInt for larger numbers
const large = BigInt(1) << BigInt(40);
```

### Debugging Bit Manipulation

**Helper functions for debugging:**

```typescript
// Print binary representation
function toBinary(n: number, bits: number = 32): string {
    return (n >>> 0).toString(2).padStart(bits, '0');
}

// Visualize bit operations
function visualizeBitOp(a: number, b: number, op: string): void {
    console.log(`a = ${toBinary(a, 8)} (${a})`);
    console.log(`b = ${toBinary(b, 8)} (${b})`);

    let result: number;
    switch(op) {
        case '&': result = a & b; break;
        case '|': result = a | b; break;
        case '^': result = a ^ b; break;
        default: throw new Error('Unknown operator');
    }

    console.log(`${op} = ${toBinary(result, 8)} (${result})`);
}

// Example usage:
visualizeBitOp(5, 3, '&');
// Output:
// a = 00000101 (5)
// b = 00000011 (3)
// & = 00000001 (1)
```

---

## Practice Exercises

### Warm-up Problems
1. Set the 3rd bit of number 5
2. Clear the 2nd bit of number 7
3. Toggle the 4th bit of number 12
4. Check if 5th bit is set in number 31

### Challenge Problems
1. Implement division using only bit operations
2. Find the only number that appears once when all others appear 4 times
3. Reverse the bits of a byte (8 bits)
4. Count the number of bit differences between two integers

---

## Key Formulas Summary

```typescript
// Most important bit formulas
n & (n-1)     // Remove rightmost set bit
n & -n        // Isolate rightmost set bit
n | (n+1)     // Set rightmost unset bit
n ^ (n+1)     // Isolate rightmost unset bit
(n & (n-1)) === 0  // Check if power of 2

// Bit positions
1 << i        // Set i-th bit
~(1 << i)     // Clear i-th bit mask
n | (1 << i)  // Set i-th bit in n
n & ~(1 << i) // Clear i-th bit in n
n ^ (1 << i)  // Toggle i-th bit in n
(n >> i) & 1  // Get i-th bit

// Useful constants
0xFFFFFFFF    // All 1s (32-bit)
0x55555555    // 01010101... pattern
0xAAAAAAAA    // 10101010... pattern
0x33333333    // 00110011... pattern
0xCCCCCCCC    // 11001100... pattern
```

---

**Next:** Complete the concept check with Claude, then solve the problems in order.