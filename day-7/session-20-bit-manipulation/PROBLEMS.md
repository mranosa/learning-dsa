# Problems - Session 20: Bit Manipulation

10 problems in order. Use UMPIRE method.

**Targets:** Easy <15 min | Medium <30 min

---

## Problem 1: Single Number

**Difficulty:** Easy | **Pattern:** XOR
**LeetCode:** https://leetcode.com/problems/single-number/

### Problem

Given non-empty array where every element appears twice except one, find the single element.

Must use O(n) time and O(1) space.

### Examples

```
nums = [2,2,1]
Output: 1

nums = [4,1,2,1,2]
Output: 4

nums = [1]
Output: 1
```

### Constraints

- 1 ≤ nums.length ≤ 3×10⁴
- -3×10⁴ ≤ nums[i] ≤ 3×10⁴
- Every element appears twice except one

### Hints
- What operation gives 0 when used with itself?
- XOR properties: a^a=0, a^0=a
- All pairs cancel out

---

## Problem 2: Number of 1 Bits (Hamming Weight)

**Difficulty:** Easy | **Pattern:** Bit Counting
**LeetCode:** https://leetcode.com/problems/number-of-1-bits/

### Problem

Return the number of '1' bits in an unsigned integer (Hamming weight).

### Examples

```
n = 00000000000000000000000000001011
Output: 3

n = 00000000000000000000000010000000
Output: 1

n = 11111111111111111111111111111101
Output: 31
```

### Constraints

- Input is 32-bit unsigned integer

### Hints
- Naive: Check each of 32 bits
- Better: n & (n-1) removes rightmost set bit
- Brian Kernighan's algorithm - loop only k times for k set bits

---

## Problem 3: Counting Bits

**Difficulty:** Easy | **Pattern:** DP + Bit Manipulation
**LeetCode:** https://leetcode.com/problems/counting-bits/

### Problem

Given integer n, return array where `ans[i]` is the number of 1's in binary of i.

### Examples

```
n = 2
Output: [0,1,1]
Explanation:
0 → 0
1 → 1
2 → 10

n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 → 0
1 → 1
2 → 10
3 → 11
4 → 100
5 → 101
```

### Constraints

- 0 ≤ n ≤ 10⁵

### Hints
- DP relation: count[i] relates to count[i/2]
- i >> 1 removes last bit, i & 1 checks last bit
- result[i] = result[i >> 1] + (i & 1)

---

## Problem 4: Reverse Bits

**Difficulty:** Easy | **Pattern:** Bit Manipulation
**LeetCode:** https://leetcode.com/problems/reverse-bits/

### Problem

Reverse bits of a 32-bit unsigned integer.

### Examples

```
n = 00000010100101000001111010011100
Output: 00111001011110000010100101000000

n = 11111111111111111111111111111101
Output: 10111111111111111111111111111111
```

### Constraints

- Input is 32-bit unsigned integer

### Hints
- Process bit by bit from right
- Build result from left
- Use >>> for unsigned shift

---

## Problem 5: Missing Number

**Difficulty:** Easy | **Pattern:** XOR/Math
**LeetCode:** https://leetcode.com/problems/missing-number/

### Problem

Array contains n distinct numbers in range [0, n]. Find the missing number.

### Examples

```
nums = [3,0,1]
Output: 2

nums = [0,1]
Output: 2

nums = [9,6,4,2,3,5,7,0,1]
Output: 8
```

### Constraints

- n == nums.length
- 1 ≤ n ≤ 10⁴
- 0 ≤ nums[i] ≤ n
- All numbers unique

### Hints
- XOR approach: XOR indices with array values
- Math approach: expectedSum - actualSum
- XOR: all present numbers cancel out

---

## Problem 6: Sum of Two Integers

**Difficulty:** Medium | **Pattern:** Bit Arithmetic
**LeetCode:** https://leetcode.com/problems/sum-of-two-integers/

### Problem

Return sum of two integers without using + or - operators.

### Examples

```
a = 1, b = 2
Output: 3

a = 2, b = 3
Output: 5

a = -1, b = 1
Output: 0
```

### Constraints

- -1000 ≤ a, b ≤ 1000

### Hints
- XOR for sum without carry
- AND for carry positions
- Shift carry left by 1
- Repeat until no carry

---

## Problem 7: Single Number II

**Difficulty:** Medium | **Pattern:** Bit Counting
**LeetCode:** https://leetcode.com/problems/single-number-ii/

### Problem

Every element appears three times except one which appears once. Find it.

Must use O(n) time and O(1) space.

### Examples

```
nums = [2,2,3,2]
Output: 3

nums = [0,1,0,1,0,1,99]
Output: 99

nums = [1]
Output: 1
```

### Constraints

- 1 ≤ nums.length ≤ 3×10⁴
- -2³¹ ≤ nums[i] ≤ 2³¹-1

### Hints
- Count bits at each position
- If count % 3 != 0, single number has 1 there
- Loop through 32 bit positions

---

## Problem 8: Single Number III

**Difficulty:** Medium | **Pattern:** XOR + Partitioning
**LeetCode:** https://leetcode.com/problems/single-number-iii/

### Problem

Array where exactly two elements appear once, all others appear twice. Find the two unique elements.

### Examples

```
nums = [1,2,1,3,2,5]
Output: [3,5]

nums = [-1,0]
Output: [-1,0]

nums = [0,1]
Output: [0,1]
```

### Constraints

- 2 ≤ nums.length ≤ 3×10⁴
- -2³¹ ≤ nums[i] ≤ 2³¹-1
- Each integer appears twice except two

### Hints
- First XOR all → gets a^b
- Find bit where a and b differ (xor & -xor)
- Partition array based on this bit
- XOR each partition separately

---

## Problem 9: Bitwise AND of Numbers Range

**Difficulty:** Medium | **Pattern:** Bit Analysis
**LeetCode:** https://leetcode.com/problems/bitwise-and-of-numbers-range/

### Problem

Return bitwise AND of all numbers in range [left, right] inclusive.

### Examples

```
left = 5, right = 7
Output: 4
Explanation: 5 AND 6 AND 7 = 4

left = 0, right = 0
Output: 0

left = 1, right = 2147483647
Output: 0
```

### Constraints

- 0 ≤ left ≤ right ≤ 2³¹-1

### Hints
- Bits that change in range become 0
- Find common prefix of left and right
- Shift both right until equal, track shifts
- Shift result back left

---

## Problem 10: Maximum XOR of Two Numbers

**Difficulty:** Medium | **Pattern:** Greedy + Trie
**LeetCode:** https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

### Problem

Return maximum result of nums[i] XOR nums[j] where 0 ≤ i ≤ j < n.

### Examples

```
nums = [3,10,5,25,2,8]
Output: 28
Explanation: 5 XOR 25 = 28

nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127

nums = [1]
Output: 0
```

### Constraints

- 1 ≤ nums.length ≤ 2×10⁵
- 0 ≤ nums[i] ≤ 2³¹-1

### Hints
- Build result bit by bit from MSB to LSB
- Use prefix matching with HashSet
- Or build Trie of binary representations
- Try to set each bit to 1 greedily

---

## Summary

**Total:** 10 problems (5 Easy, 5 Medium)

**Patterns:**
- XOR for Uniqueness
- Brian Kernighan's Algorithm
- Bit Counting with DP
- Bit Masking & Manipulation
- Prefix Analysis

**Key Techniques:**
- n & (n-1) removes rightmost set bit
- n & -n isolates rightmost set bit
- XOR cancellation property
- Bit-by-bit processing
- Greedy bit construction

---

**Ready?** Say: `"Claude, give me the problem"` or `"Go"`

[Solutions](./SOLUTIONS.md) | [Hints](./HINTS.md)
