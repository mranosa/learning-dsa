# Hints: Bit Manipulation

## Problem 1: Single Number

### Hint 1 (Gentle)
Think about an operation where applying it twice gives you back the original value, but also has a special property with 0.

### Hint 2 (Direct)
XOR has the property that a ^ a = 0 and a ^ 0 = a. What happens if you XOR all numbers together?

### Hint 3 (Detailed)
Since XOR is commutative and associative, when you XOR all numbers, pairs cancel out (a ^ a = 0). The single number XORed with 0 remains unchanged. Just XOR all elements together.

---

## Problem 2: Number of 1 Bits

### Hint 1 (Gentle)
You could check each bit position, but there's a clever trick involving n & (n-1). What does this operation do to the binary representation?

### Hint 2 (Direct)
n & (n-1) removes the rightmost set bit. How can you use this to count all set bits efficiently?

### Hint 3 (Detailed)
Use Brian Kernighan's algorithm: repeatedly apply n = n & (n-1) until n becomes 0. Each iteration removes one set bit, so count the iterations. This is more efficient than checking all 32 bits.

---

## Problem 3: Counting Bits

### Hint 1 (Gentle)
There's a pattern between a number and half of that number (i >> 1). How do their bit counts relate?

### Hint 2 (Direct)
For any number i, the count of 1s equals the count in i/2 plus the last bit. Use dynamic programming to build from previous results.

### Hint 3 (Detailed)
result[i] = result[i >> 1] + (i & 1). The i >> 1 gives you the count for all bits except the last one, and (i & 1) adds 1 if the last bit is set. Build the array from 0 to n.

---

## Problem 4: Reverse Bits

### Hint 1 (Gentle)
Process the number bit by bit. How can you extract the rightmost bit and build the result from left to right?

### Hint 2 (Direct)
Extract each bit with (n & 1), shift n right, and build result by shifting left and adding the extracted bit.

### Hint 3 (Detailed)
For 32 iterations: get the last bit with (n & 1), add it to result with (result << 1) | bit, then shift n right with n >>>= 1. Use unsigned right shift (>>>) to handle the sign bit correctly.

---

## Problem 5: Missing Number

### Hint 1 (Gentle)
You have numbers from 0 to n with one missing. What if you had all numbers from 0 to n twice, except the missing one?

### Hint 2 (Direct)
XOR all indices [0...n] with all array elements. What remains after all XOR operations?

### Hint 3 (Detailed)
XOR has the property a ^ a = 0. If you XOR all indices 0 to n with all array elements, every number except the missing one appears twice and cancels out. Start with result = n, then XOR with each index and array element.

---

## Problem 6: Sum of Two Integers

### Hint 1 (Gentle)
In binary addition, XOR gives you the sum without carry, and AND tells you where carries occur. How can you combine these?

### Hint 2 (Direct)
Use a ^ b for sum without carry, and (a & b) << 1 for the carry. Keep adding the carry until it becomes 0.

### Hint 3 (Detailed)
While b != 0: calculate carry = (a & b) << 1, then a = a ^ b (sum without carry), then b = carry. The carry needs to be shifted left because it affects the next higher bit. Repeat until no carry remains.

---

## Problem 7: Single Number II

### Hint 1 (Gentle)
If every number appears 3 times except one, what happens to the sum of bits at each position modulo 3?

### Hint 2 (Direct)
Count the number of 1s at each bit position across all numbers. If count % 3 != 0, the single number has a 1 at that position.

### Hint 3 (Detailed)
For each bit position (0-31), count how many numbers have a 1 at that position. If the count isn't divisible by 3, the single number has a 1 there. Reconstruct the single number by setting appropriate bits: result |= (1 << i) when count % 3 != 0.

---

## Problem 8: Single Number III

### Hint 1 (Gentle)
First, XOR all numbers to get a ^ b where a and b are the two unique numbers. This result tells you something about how a and b differ.

### Hint 2 (Direct)
Find any bit where a and b differ (use xor & -xor to get the rightmost set bit). Use this bit to partition the array into two groups.

### Hint 3 (Detailed)
After getting xor = a ^ b, find rightmost set bit with xor & -xor. This bit is 1 in one unique number and 0 in the other. Partition array based on this bit: numbers with this bit set go to one group, others to another. XOR each group separately to find the two unique numbers.

---

## Problem 9: Bitwise AND of Numbers Range

### Hint 1 (Gentle)
When you AND consecutive numbers, what happens to the bits that change within the range?

### Hint 2 (Direct)
Bits that change within the range will become 0 after AND. Only the common prefix (leftmost bits) that don't change will remain.

### Hint 3 (Detailed)
Keep shifting both left and right boundaries to the right until they become equal (finding common prefix). Count the shifts. The result is this common value shifted back left by the shift count. Alternatively, use right &= (right - 1) to remove trailing 1s until right <= left.

---

## Problem 10: Maximum XOR of Two Numbers

### Hint 1 (Gentle)
Build the result bit by bit from most significant to least significant. For each bit position, try to set it to 1 in the result.

### Hint 2 (Direct)
Use a greedy approach: for each bit from left to right, check if it's possible to have a 1 at that position in the XOR result using prefix matching.

### Hint 3 (Detailed)
For each bit position from 31 to 0: create a set of all number prefixes up to current bit. Try to set current bit to 1 in result. For this to be possible, there must exist two prefixes p1 and p2 such that p1 ^ p2 equals our target prefix. Check if for any prefix p, the set contains target ^ p.

---

## General Bit Manipulation Tips

### Recognition Patterns
- **Single/unique element** → Think XOR
- **Counting bits** → Brian Kernighan or DP
- **Range operations** → Common prefix
- **Addition/arithmetic** → Bit-by-bit with carry
- **Maximum/minimum** → Greedy bit construction

### Common Techniques
1. **n & (n-1)** - Remove rightmost set bit
2. **n & -n** - Isolate rightmost set bit
3. **XOR properties** - Cancellation, commutative
4. **Bit masking** - 1 << i for i-th bit
5. **Prefix building** - Construct result bit by bit

### Debugging Tips
- Print binary representation: `num.toString(2)`
- Use parentheses to ensure operation order
- Remember >>> for unsigned shift in JavaScript
- Test with small examples first
- Trace through bit operations step by step

---

## Problem-Specific Strategies

### XOR Problems (1, 5, 7, 8)
- Use cancellation property
- Think about pairing/grouping
- Consider bit-by-bit analysis
- Remember commutative and associative properties
- XOR of identical elements is always 0

### Counting Problems (2, 3)
- Brian Kernighan for single number
- DP for ranges
- Reuse previous results
- Look for patterns in binary representation
- Consider relationship between n and n/2

### Manipulation Problems (4, 6)
- Process bit by bit
- Handle carry/borrow carefully
- Watch for overflow
- Use unsigned shift when needed
- Think about two's complement for negatives

### Advanced Problems (9, 10)
- Think about prefixes
- Use greedy approach
- Consider trie for optimization
- Analyze bit stability in ranges
- Build solutions from MSB to LSB

---

## Additional Practice Hints

### Binary Conversion Practice
1. **Quick mental conversion:**
   - 15 = 1111 (all 4 bits set)
   - 16 = 10000 (power of 2)
   - 31 = 11111 (all 5 bits set)
   - 255 = 11111111 (all 8 bits set)

2. **Powers of 2:**
   - 1 << 0 = 1
   - 1 << 1 = 2
   - 1 << 2 = 4
   - 1 << 3 = 8
   - 1 << 4 = 16

### Common Bit Patterns

1. **All 1s mask:**
   ```typescript
   ~0         // All 1s
   (1 << n) - 1  // n rightmost bits set
   ```

2. **Alternating bits:**
   ```typescript
   0xAAAAAAAA  // 10101010...
   0x55555555  // 01010101...
   ```

3. **Check specific bit:**
   ```typescript
   (n >> i) & 1  // Is i-th bit set?
   n & (1 << i)  // Non-zero if i-th bit set
   ```

### Edge Cases to Consider

1. **Zero:**
   - 0 XOR anything = that thing
   - 0 AND anything = 0
   - 0 OR anything = that thing

2. **Negative numbers:**
   - Use >>> for unsigned shift
   - Two's complement representation
   - Sign bit considerations

3. **Overflow:**
   - JavaScript uses 32-bit integers
   - Large numbers may overflow
   - Consider using BigInt if needed

### Performance Optimization

1. **Prefer bit operations over arithmetic:**
   - Multiply by 2: n << 1
   - Divide by 2: n >> 1
   - Modulo 2: n & 1
   - Check even: (n & 1) === 0

2. **Batch operations:**
   - Process multiple bits at once
   - Use masks for parallel operations
   - Leverage CPU's bitwise capabilities

### Interview Communication

1. **Explain your thought process:**
   - "I'm using XOR because..."
   - "This bit represents..."
   - "The pattern I notice is..."

2. **Visualize for clarity:**
   - Draw binary representations
   - Show bit operations step by step
   - Use examples with small numbers

3. **Discuss trade-offs:**
   - Bit manipulation vs. readable code
   - Space savings vs. complexity
   - Platform-specific considerations

---

## Quick Reference Card

### Essential Formulas
```typescript
// Toggle bit
n ^= (1 << i)

// Check power of 2
(n & (n - 1)) === 0 && n !== 0

// Get rightmost set bit
n & -n

// Remove rightmost set bit
n & (n - 1)

// Set all bits from 0 to i
(1 << (i + 1)) - 1

// Clear all bits from MSB to i
mask = (1 << i) - 1
n & mask

// Update bit at position i
// Clear then set
n = (n & ~(1 << i)) | (value << i)
```

### Bit Manipulation Checklist
- [ ] Understand the problem's bit pattern
- [ ] Consider XOR for uniqueness
- [ ] Think about masking for isolation
- [ ] Check for standard bit tricks
- [ ] Handle edge cases (0, negative, overflow)
- [ ] Optimize using bit properties
- [ ] Test with binary examples
- [ ] Verify with extreme values