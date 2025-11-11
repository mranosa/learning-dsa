# Problems: Bit Manipulation

## Problem 1: Single Number
**Difficulty:** Easy
**LeetCode:** [136. Single Number](https://leetcode.com/problems/single-number/)

Given a non-empty array of integers where every element appears twice except for one, find that single element.

**Constraints:**
- You must implement a solution with O(n) runtime complexity
- You must use only O(1) extra space

**Example:**
```typescript
Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1
```

---

## Problem 2: Number of 1 Bits
**Difficulty:** Easy
**LeetCode:** [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

**Constraints:**
- The input must be a binary string of length 32

**Example:**
```typescript
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input has three '1' bits.

Input: n = 00000000000000000000000010000000
Output: 1

Input: n = 11111111111111111111111111111101
Output: 31
```

---

## Problem 3: Counting Bits
**Difficulty:** Easy
**LeetCode:** [338. Counting Bits](https://leetcode.com/problems/counting-bits/)

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

**Constraints:**
- 0 <= n <= 10^5

**Example:**
```typescript
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
```

---

## Problem 4: Reverse Bits
**Difficulty:** Easy
**LeetCode:** [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/)

Reverse bits of a given 32 bits unsigned integer.

**Constraints:**
- The input must be a binary string of length 32

**Example:**
```typescript
Input: n = 00000010100101000001111010011100
Output:    00111001011110000010100101000000
Explanation: The reversed bit string is 00111001011110000010100101000000.

Input: n = 11111111111111111111111111111101
Output:   10111111111111111111111111111111
```

---

## Problem 5: Missing Number
**Difficulty:** Easy
**LeetCode:** [268. Missing Number](https://leetcode.com/problems/missing-number/)

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

**Constraints:**
- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All numbers in nums are unique

**Example:**
```typescript
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3, numbers are in range [0,3]. 2 is missing.

Input: nums = [0,1]
Output: 2

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
```

---

## Problem 6: Sum of Two Integers
**Difficulty:** Medium
**LeetCode:** [371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)

Given two integers a and b, return the sum of the two integers without using the operators + and -.

**Constraints:**
- -1000 <= a, b <= 1000

**Example:**
```typescript
Input: a = 1, b = 2
Output: 3

Input: a = 2, b = 3
Output: 5

Input: a = -1, b = 1
Output: 0
```

---

## Problem 7: Single Number II
**Difficulty:** Medium
**LeetCode:** [137. Single Number II](https://leetcode.com/problems/single-number-ii/)

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

**Constraints:**
- You must implement a solution with O(n) runtime complexity
- You must use only O(1) extra space

**Example:**
```typescript
Input: nums = [2,2,3,2]
Output: 3

Input: nums = [0,1,0,1,0,1,99]
Output: 99

Input: nums = [1]
Output: 1
```

---

## Problem 8: Single Number III
**Difficulty:** Medium
**LeetCode:** [260. Single Number III](https://leetcode.com/problems/single-number-iii/)

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

**Constraints:**
- 2 <= nums.length <= 3 * 10^4
- -2^31 <= nums[i] <= 2^31 - 1
- Each integer in nums appears twice, except for two integers that appear once

**Example:**
```typescript
Input: nums = [1,2,1,3,2,5]
Output: [3,5] or [5,3]
Explanation: 3 and 5 appear only once.

Input: nums = [-1,0]
Output: [-1,0] or [0,-1]

Input: nums = [0,1]
Output: [0,1] or [1,0]
```

---

## Problem 9: Bitwise AND of Numbers Range
**Difficulty:** Medium
**LeetCode:** [201. Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)

Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

**Constraints:**
- 0 <= left <= right <= 2^31 - 1

**Example:**
```typescript
Input: left = 5, right = 7
Output: 4
Explanation: 5 AND 6 AND 7 = 4

Input: left = 0, right = 0
Output: 0

Input: left = 1, right = 2147483647
Output: 0
```

---

## Problem 10: Maximum XOR of Two Numbers in an Array
**Difficulty:** Medium
**LeetCode:** [421. Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

**Constraints:**
- 1 <= nums.length <= 2 * 10^5
- 0 <= nums[i] <= 2^31 - 1

**Example:**
```typescript
Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum XOR is 5 XOR 25 = 28.

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127

Input: nums = [1]
Output: 0
```

---

## Problem-Solving Strategy

### For XOR Problems (1, 5, 7, 8):
1. Remember XOR properties: a^a=0, a^0=a
2. Think about cancellation patterns
3. Consider bit-by-bit analysis for complex cases

### For Bit Counting (2, 3):
1. Use Brian Kernighan's algorithm for efficiency
2. Consider dynamic programming for ranges
3. Look for patterns in binary representation

### For Bit Manipulation (4, 6):
1. Process bit-by-bit
2. Use masks to isolate specific bits
3. Handle overflow and negative numbers carefully

### For Range Problems (9, 10):
1. Look for common bit patterns
2. Consider prefix/suffix analysis
3. Think about when bits become stable

---

## Approach Order

**Beginner Path:**
1. Start with Problem 1 (Single Number) - Basic XOR
2. Move to Problem 2 (Number of 1 Bits) - Bit counting
3. Try Problem 5 (Missing Number) - XOR application
4. Tackle Problem 3 (Counting Bits) - DP with bits
5. Solve Problem 4 (Reverse Bits) - Bit manipulation

**Intermediate Path:**
6. Problem 6 (Sum of Two Integers) - Bit addition
7. Problem 7 (Single Number II) - Advanced XOR
8. Problem 8 (Single Number III) - Complex XOR pattern

**Advanced Path:**
9. Problem 9 (Bitwise AND Range) - Range analysis
10. Problem 10 (Maximum XOR) - Trie optimization

---

## Time Management

**Suggested time allocation:**
- Easy problems (1-5): 10-15 minutes each
- Medium problems (6-10): 20-25 minutes each
- Review and optimization: 30 minutes

**If stuck:**
- 5 minutes: Review the bit operation needed
- 10 minutes: Check hint level 1
- 15 minutes: Check hint level 2
- 20 minutes: Review solution approach

---

## Self-Evaluation Checklist

After completing each problem:
- [ ] Did I recognize the bit pattern immediately?
- [ ] Did I use the most efficient bit operations?
- [ ] Did I handle edge cases (0, negative, overflow)?
- [ ] Can I explain why the bit manipulation works?
- [ ] Did I achieve optimal time/space complexity?

---

## Common Pitfalls

1. **Forgetting XOR properties**
   - Review: a^a=0, a^0=a, commutative, associative

2. **Not handling negative numbers**
   - Remember two's complement representation

3. **Integer overflow in JavaScript**
   - Use >>> for unsigned right shift

4. **Inefficient bit counting**
   - Use n & (n-1) to remove rightmost bit

5. **Complex solutions for simple problems**
   - Most bit problems have elegant tricks

---

## Next Steps

After completing all problems:
1. Review all XOR-based solutions
2. Practice bit manipulation without looking at references
3. Try to optimize further using bit tricks
4. Implement a bit manipulation utility library

Remember: Bit manipulation is about recognizing patterns and applying the right tricks!