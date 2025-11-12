# Problems - Session 2: Hash Maps

10 problems in order. Use UMPIRE method.

**Targets:** Easy <15 min | Medium <30 min

---

## Problem 1: Contains Duplicate

**Difficulty:** Easy | **Pattern:** Set
**LeetCode:** https://leetcode.com/problems/contains-duplicate/

### Problem

Given array `nums`, return `true` if any value appears at least twice, `false` if all distinct.

### Examples

```
nums = [1,2,3,1] → true

nums = [1,2,3,4] → false

nums = [1,1,1,3,3,4,3,2,4,2] → true
```

### Constraints

- 1 ≤ nums.length ≤ 10⁵
- -10⁹ ≤ nums[i] ≤ 10⁹

### Hints
- Use Set to track seen numbers
- If already in set → duplicate
- O(n) time, O(n) space

---

## Problem 2: Valid Anagram

**Difficulty:** Easy | **Pattern:** Frequency Counting
**LeetCode:** https://leetcode.com/problems/valid-anagram/

### Problem

Given strings `s` and `t`, return `true` if `t` is an anagram of `s`.

Anagram = rearrangement using all letters exactly once.

### Examples

```
s = "anagram", t = "nagaram" → true

s = "rat", t = "car" → false

s = "a", t = "ab" → false
```

### Constraints

- 1 ≤ s.length, t.length ≤ 5×10⁴
- Lowercase English letters only

### Hints
- Check lengths first
- Count character frequencies
- Increment for s, decrement for t
- O(n) time, O(k) space (k = unique chars)

---

## Problem 3: Two Sum ⭐ BLIND 75

**Difficulty:** Easy | **Pattern:** Hash Map
**LeetCode:** https://leetcode.com/problems/two-sum/

### Problem

Given array `nums` and integer `target`, return indices of two numbers that add up to `target`.

Exactly one solution exists. Can't use same element twice.

### Examples

```
nums = [2,7,11,15], target = 9
Output: [0,1]  (2 + 7 = 9)

nums = [3,2,4], target = 6
Output: [1,2]

nums = [3,3], target = 6
Output: [0,1]
```

### Constraints

- 2 ≤ nums.length ≤ 10⁴
- -10⁹ ≤ nums[i], target ≤ 10⁹
- One valid answer exists

### Hints
- Hash map for O(1) lookups → O(n) total
- Store value→index as you iterate
- Check complement before storing current
- `complement = target - nums[i]`

---

## Problem 4: Group Anagrams ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Grouping
**LeetCode:** https://leetcode.com/problems/group-anagrams/

### Problem

Given array of strings `strs`, group the anagrams together. Return in any order.

### Examples

```
strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = [""] → [[""]]

strs = ["a"] → [["a"]]
```

### Constraints

- 1 ≤ strs.length ≤ 10⁴
- 0 ≤ strs[i].length ≤ 100
- Lowercase English letters only

### Hints
- Anagrams have identical sorted strings
- Use sorted string as Map key
- Map<sortedString, string[]>
- O(n × k log k) time, O(n × k) space

---

## Problem 5: Top K Frequent Elements ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Frequency + Bucket Sort
**LeetCode:** https://leetcode.com/problems/top-k-frequent-elements/

### Problem

Given array `nums` and integer `k`, return the `k` most frequent elements. Return in any order.

### Examples

```
nums = [1,1,1,2,2,3], k = 2
Output: [1,2]  (1 appears 3×, 2 appears 2×)

nums = [1], k = 1
Output: [1]

nums = [1,2], k = 2
Output: [1,2]
```

### Constraints

- 1 ≤ nums.length ≤ 10⁵
- -10⁴ ≤ nums[i] ≤ 10⁴
- k in range [1, number of unique elements]
- Answer is unique

### Hints
- Count frequencies with Map
- Bucket sort: frequency → array of numbers
- Collect from highest frequency down
- O(n) time, O(n) space (better than O(n log n) sort)

---

## Problem 6: Product of Array Except Self ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Prefix/Suffix
**LeetCode:** https://leetcode.com/problems/product-of-array-except-self/

### Problem

Return array where `answer[i]` = product of all elements except `nums[i]`.

Must run in O(n) time. No division operation.

### Examples

```
nums = [1,2,3,4]
Output: [24,12,8,6]

nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

### Constraints

- 2 ≤ nums.length ≤ 10⁵
- -30 ≤ nums[i] ≤ 30
- Product fits in 32-bit integer

### Follow-up
O(1) extra space? (output doesn't count)

### Hints
- Product except self = left product × right product
- Calculate prefix products (L→R)
- Calculate suffix products on fly (R→L)
- Reuse output array for O(1) space

---

## Problem 7: Valid Sudoku ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Multiple Hash Maps
**LeetCode:** https://leetcode.com/problems/valid-sudoku/

### Problem

Determine if 9×9 Sudoku board is valid:
1. Each row: digits 1-9 without repetition
2. Each column: digits 1-9 without repetition
3. Each 3×3 box: digits 1-9 without repetition

Partially filled board is acceptable.

### Constraints

- board.length == 9
- board[i].length == 9
- board[i][j] is digit 1-9 or '.'

### Hints
- 9 Sets for rows, 9 for columns, 9 for boxes
- Box index: `Math.floor(r/3) * 3 + Math.floor(c/3)`
- Single pass with three checks
- O(1) time (fixed 81 cells), O(1) space

---

## Problem 8: Encode and Decode Strings ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** String Encoding
**LeetCode:** https://leetcode.com/problems/encode-and-decode-strings/ (Premium)

### Problem

Design algorithm to encode list of strings to single string, then decode back to original list.

Implement `encode` and `decode` methods.

### Examples

```
Input: ["hello","world"]
encode(): "5#hello5#world"
decode(): ["hello","world"]

Input: [""]
encode(): "0#"
decode(): [""]
```

### Constraints

- 1 ≤ strs.length ≤ 200
- 0 ≤ strs[i].length ≤ 200
- Any ASCII character possible

### Hints
- Length prefix prevents delimiter collision
- Format: `length#string` for each
- Decode: find '#', read length, extract that many chars
- O(n) encode, O(n) decode

---

## Problem 9: Longest Consecutive Sequence ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Set Optimization
**LeetCode:** https://leetcode.com/problems/longest-consecutive-sequence/

### Problem

Given unsorted array `nums`, return length of longest consecutive elements sequence.

Must run in O(n) time.

### Examples

```
nums = [100,4,200,1,3,2]
Output: 4  ([1,2,3,4])

nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9  ([0,1,2,3,4,5,6,7,8])

nums = [] → 0
```

### Constraints

- 0 ≤ nums.length ≤ 10⁵
- -10⁹ ≤ nums[i] ≤ 10⁹

### Hints
- Put all numbers in Set for O(1) lookup
- Only start counting from sequence beginnings (num-1 doesn't exist)
- Count consecutive: num, num+1, num+2...
- Each number visited max twice
- O(n) time, O(n) space

---

## Problem 10: Subarray Sum Equals K

**Difficulty:** Medium | **Pattern:** Prefix Sum + Hash Map
**LeetCode:** https://leetcode.com/problems/subarray-sum-equals-k/

### Problem

Given array `nums` and integer `k`, return total number of subarrays whose sum equals `k`.

Subarray = contiguous non-empty sequence.

### Examples

```
nums = [1,1,1], k = 2
Output: 2  ([1,1] at [0,1] and [1,2])

nums = [1,2,3], k = 3
Output: 2  ([1,2] and [3])

nums = [1,-1,0], k = 0
Output: 3  ([1,-1], [0], [1,-1,0])
```

### Constraints

- 1 ≤ nums.length ≤ 2×10⁴
- -1000 ≤ nums[i] ≤ 1000
- -10⁷ ≤ k ≤ 10⁷

### Hints
- If `prefixSum[j] - prefixSum[i] = k`, then subarray [i+1,j] sums to k
- Store frequency of prefix sums in Map
- Check if `(currentSum - k)` exists
- Initialize with `(0, 1)` for subarrays starting at 0
- O(n) time, O(n) space

---

## Summary

**Total:** 10 problems (3 Easy, 7 Medium)

**Patterns:**
- Set for duplicates
- Frequency counting
- Two Sum pattern
- Grouping/categorizing
- Multiple hash maps
- Set optimization
- Prefix sum + hash map

**Blind 75:** 9/75 complete (12%)

---

**Ready?** Say: `"Claude, give me the problem"` or `"Go"`

[Solutions](./SOLUTIONS.md) | [Hints](./HINTS.md)
