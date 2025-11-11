# Problems: Hash Maps

## Problem Order
1. Contains Duplicate (Easy) - Warm-up with Sets
2. Valid Anagram (Easy) - Frequency counting
3. Two Sum (Easy) - Classic hash map pattern
4. Group Anagrams (Medium) - Grouping with hash maps
5. Top K Frequent Elements (Medium) - Frequency + sorting
6. Product of Array Except Self (Medium) - Prefix/suffix products
7. Valid Sudoku (Medium) - Multiple hash maps
8. Encode and Decode Strings (Medium) - String manipulation
9. Longest Consecutive Sequence (Medium) - Set optimization
10. Subarray Sum Equals K (Medium) - Prefix sum pattern

---

## Problem 1: Contains Duplicate

**Difficulty:** Easy
**Time:** 10 minutes
**LeetCode:** https://leetcode.com/problems/contains-duplicate/

### Problem Statement
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Examples
```typescript
// Example 1
Input: nums = [1,2,3,1]
Output: true
Explanation: 1 appears twice

// Example 2
Input: nums = [1,2,3,4]
Output: false
Explanation: All elements are distinct

// Example 3
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

### Constraints
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

### Hints Available
See HINTS.md for progressive hints.

---

## Problem 2: Valid Anagram

**Difficulty:** Easy
**Time:** 10 minutes
**LeetCode:** https://leetcode.com/problems/valid-anagram/

### Problem Statement
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Examples
```typescript
// Example 1
Input: s = "anagram", t = "nagaram"
Output: true

// Example 2
Input: s = "rat", t = "car"
Output: false

// Example 3
Input: s = "a", t = "ab"
Output: false
```

### Constraints
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters

### Follow-up
What if the inputs contain Unicode characters? How would you adapt your solution?

---

## Problem 3: Two Sum

**Difficulty:** Easy
**Time:** 15 minutes
**LeetCode:** https://leetcode.com/problems/two-sum/

### Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

### Examples
```typescript
// Example 1
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9, so return [0, 1]

// Example 2
Input: nums = [3,2,4], target = 6
Output: [1,2]

// Example 3
Input: nums = [3,3], target = 6
Output: [0,1]
```

### Constraints
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists

### Follow-up
Can you come up with an algorithm that is less than O(n²) time complexity?

---

## Problem 4: Group Anagrams

**Difficulty:** Medium
**Time:** 20 minutes
**LeetCode:** https://leetcode.com/problems/group-anagrams/

### Problem Statement
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

### Examples
```typescript
// Example 1
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

// Example 2
Input: strs = [""]
Output: [[""]]

// Example 3
Input: strs = ["a"]
Output: [["a"]]
```

### Constraints
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters

---

## Problem 5: Top K Frequent Elements

**Difficulty:** Medium
**Time:** 20 minutes
**LeetCode:** https://leetcode.com/problems/top-k-frequent-elements/

### Problem Statement
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

### Examples
```typescript
// Example 1
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Explanation: 1 appears 3 times, 2 appears 2 times

// Example 2
Input: nums = [1], k = 1
Output: [1]

// Example 3
Input: nums = [1,2], k = 2
Output: [1,2]
```

### Constraints
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements]
- It is guaranteed that the answer is unique

### Follow-up
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

---

## Problem 6: Product of Array Except Self

**Difficulty:** Medium
**Time:** 20 minutes
**LeetCode:** https://leetcode.com/problems/product-of-array-except-self/

### Problem Statement
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

### Examples
```typescript
// Example 1
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation: [2*3*4, 1*3*4, 1*2*4, 1*2*3]

// Example 2
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

### Constraints
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- Product of any prefix or suffix fits in a 32-bit integer

### Follow-up
Can you solve the problem in O(1) extra space? (Output array doesn't count)

---

## Problem 7: Valid Sudoku

**Difficulty:** Medium
**Time:** 25 minutes
**LeetCode:** https://leetcode.com/problems/valid-sudoku/

### Problem Statement
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes must contain the digits 1-9 without repetition.

Note: A partially filled sudoku which is valid is acceptable.

### Examples
```typescript
// Example 1
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

// Example 2
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with 8 in top left. Two 8s in top row.
```

### Constraints
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit 1-9 or '.'

---

## Problem 8: Encode and Decode Strings

**Difficulty:** Medium
**Time:** 20 minutes
**LeetCode:** https://leetcode.com/problems/encode-and-decode-strings/ (Premium)

### Problem Statement
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Implement the `encode` and `decode` methods.

### Examples
```typescript
// Example 1
Input: ["hello","world"]
encode() returns: "5#hello5#world"
decode() returns: ["hello","world"]

// Example 2
Input: [""]
encode() returns: "0#"
decode() returns: [""]

// Example 3
Input: ["C","o","d","e"]
encode() returns: "1#C1#o1#d1#e"
decode() returns: ["C","o","d","e"]
```

### Constraints
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] contains any possible characters out of 256 valid ASCII characters

### Note
The string may contain any ASCII character, including delimiters you might want to use.

---

## Problem 9: Longest Consecutive Sequence

**Difficulty:** Medium
**Time:** 25 minutes
**LeetCode:** https://leetcode.com/problems/longest-consecutive-sequence/

### Problem Statement
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

### Examples
```typescript
// Example 1
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: [1, 2, 3, 4] is the longest consecutive sequence

// Example 2
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: [0,1,2,3,4,5,6,7,8]

// Example 3
Input: nums = []
Output: 0
```

### Constraints
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

---

## Problem 10: Subarray Sum Equals K

**Difficulty:** Medium
**Time:** 25 minutes
**LeetCode:** https://leetcode.com/problems/subarray-sum-equals-k/

### Problem Statement
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

### Examples
```typescript
// Example 1
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: [1,1] appears at indices [0,1] and [1,2]

// Example 2
Input: nums = [1,2,3], k = 3
Output: 2
Explanation: [1,2] and [3]

// Example 3
Input: nums = [1,-1,0], k = 0
Output: 3
Explanation: [1,-1], [0], and [1,-1,0]
```

### Constraints
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

### Follow-up
Can you solve it in O(n) time and O(n) space?

---

## Summary

### Difficulty Distribution
- Easy: 3 problems (1-3)
- Medium: 7 problems (4-10)

### Key Patterns Covered
- Set for duplicates (Problem 1)
- Frequency counting (Problems 2, 5)
- Two Sum pattern (Problem 3)
- Grouping/categorizing (Problem 4)
- Multiple hash maps (Problem 7)
- String encoding (Problem 8)
- Set optimization (Problem 9)
- Prefix sum with hash map (Problem 10)

### Time Allocation
- Total: ~3 hours
- Easy problems: 35 minutes
- Medium problems: 145 minutes

**Ready for solutions?** Check SOLUTIONS.md
**Need hints?** See HINTS.md
**Mock interview practice?** Use INTERVIEWER-SCRIPT.md