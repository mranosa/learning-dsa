# Problems - Session 4: Two Pointers

10 problems in order. Use UMPIRE method.

**Targets:** Easy <15 min | Medium <30 min | Hard <45 min

---

## Problem 1: Valid Palindrome ⭐ BLIND 75

**Difficulty:** Easy | **Pattern:** Opposite Direction
**LeetCode:** https://leetcode.com/problems/valid-palindrome/

### Problem

String `s`. Return `true` if palindrome (reads same forward and backward), ignoring non-alphanumeric characters and case.

### Examples

```
s = "A man, a plan, a canal: Panama"
Output: true

s = "race a car"
Output: false

s = " "
Output: true
```

### Constraints

- 1 ≤ s.length ≤ 2×10⁵
- `s` consists of printable ASCII characters

### Hints
- Two pointers from both ends
- Skip non-alphanumeric characters
- Compare case-insensitively
- O(n) time, O(1) space

---

## Problem 2: Two Sum II - Input Array Is Sorted ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Opposite Direction
**LeetCode:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

### Problem

Given 1-indexed sorted array `numbers`, return indices of two numbers that add to `target`. Exactly one solution. Can't use same element twice.

Return in format `[index1, index2]` where `index1 < index2`.

### Examples

```
numbers = [2,7,11,15], target = 9
Output: [1,2]  (1-indexed)

numbers = [2,3,4], target = 6
Output: [1,3]

numbers = [-1,0], target = -1
Output: [1,2]
```

### Constraints

- 2 ≤ numbers.length ≤ 3×10⁴
- -1000 ≤ numbers[i] ≤ 1000
- numbers sorted in non-decreasing order
- -1000 ≤ target ≤ 1000
- Exactly one solution exists

### Hints
- Two pointers: left at start, right at end
- If sum < target → move left
- If sum > target → move right
- O(n) time, O(1) space

---

## Problem 3: 3Sum ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Opposite Direction + Fixed
**LeetCode:** https://leetcode.com/problems/3sum/

### Problem

Return all triplets `[nums[i], nums[j], nums[k]]` where `i ≠ j ≠ k` and sum = 0.

No duplicate triplets.

### Examples

```
nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

nums = [0,1,1]
Output: []

nums = [0,0,0]
Output: [[0,0,0]]
```

### Constraints

- 3 ≤ nums.length ≤ 3000
- -10⁵ ≤ nums[i] ≤ 10⁵

### Hints
- Sort array first
- Fix one number, two pointers for other two
- Skip duplicates to avoid duplicate triplets
- O(n²) time, O(1) space (excluding output)

---

## Problem 4: Container With Most Water ⭐ BLIND 75

**Difficulty:** Medium | **Pattern:** Opposite Direction
**LeetCode:** https://leetcode.com/problems/container-with-most-water/

### Problem

Array `height[i]` = vertical lines. Find two lines forming container with most water.

Can't slant container.

### Examples

```
height = [1,8,6,2,5,4,8,3,7]
Output: 49  (lines at index 1 and 8)

height = [1,1]
Output: 1
```

### Constraints

- 2 ≤ n ≤ 10⁵
- 0 ≤ height[i] ≤ 10⁴

### Hints
- Two pointers at both ends
- Area = min(height[left], height[right]) × width
- Move pointer with smaller height
- O(n) time, O(1) space

---

## Problem 5: Trapping Rain Water ⭐ BLIND 75

**Difficulty:** Hard | **Pattern:** Opposite Direction
**LeetCode:** https://leetcode.com/problems/trapping-rain-water/

### Problem

Array `height` representing elevation map. Width of each bar is 1. Compute how much water it can trap after raining.

### Examples

```
height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

height = [4,2,0,3,2,5]
Output: 9
```

### Constraints

- n == height.length
- 1 ≤ n ≤ 2×10⁴
- 0 ≤ height[i] ≤ 10⁵

### Hints
- Water at position = min(maxLeft, maxRight) - height[i]
- Two pointers tracking max heights from each side
- Move pointer with smaller max height
- O(n) time, O(1) space

---

## Problem 6: Remove Duplicates from Sorted Array

**Difficulty:** Easy | **Pattern:** Same Direction (Fast/Slow)
**LeetCode:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/

### Problem

Remove duplicates from sorted array `nums` in-place. Return `k` (number of unique elements).

First `k` elements of `nums` should contain unique elements in order.

### Examples

```
nums = [1,1,2]
Output: 2, nums = [1,2,_]

nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
```

### Constraints

- 1 ≤ nums.length ≤ 3×10⁴
- -100 ≤ nums[i] ≤ 100
- `nums` sorted in non-decreasing order

### Hints
- Slow pointer tracks last unique position
- Fast pointer scans array
- When different, copy to slow+1
- O(n) time, O(1) space

---

## Problem 7: Move Zeroes

**Difficulty:** Easy | **Pattern:** Same Direction (Fast/Slow)
**LeetCode:** https://leetcode.com/problems/move-zeroes/

### Problem

Move all 0's to end while maintaining relative order of non-zero elements. In-place.

### Examples

```
nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

nums = [0]
Output: [0]
```

### Constraints

- 1 ≤ nums.length ≤ 10⁴
- -2³¹ ≤ nums[i] ≤ 2³¹ - 1

### Follow-up
Minimize total operations?

### Hints
- Slow pointer for next non-zero position
- Fast pointer scans array
- When non-zero, swap with slow position
- O(n) time, O(1) space

---

## Problem 8: Sort Colors

**Difficulty:** Medium | **Pattern:** Three Pointers (Dutch National Flag)
**LeetCode:** https://leetcode.com/problems/sort-colors/

### Problem

Array `nums` with `n` objects colored red (0), white (1), or blue (2). Sort in-place so objects of same color are adjacent: 0's, 1's, 2's.

Must not use library's sort function.

### Examples

```
nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

nums = [2,0,1]
Output: [0,1,2]
```

### Constraints

- n == nums.length
- 1 ≤ n ≤ 300
- nums[i] is 0, 1, or 2

### Follow-up
One-pass algorithm using O(1) space?

### Hints
- Three pointers: low, mid, high
- low tracks next 0 position, high tracks next 2 position
- mid scans: if 0 swap with low, if 2 swap with high
- O(n) time, O(1) space

---

## Problem 9: Partition Labels

**Difficulty:** Medium | **Pattern:** Greedy + Two Pointers
**LeetCode:** https://leetcode.com/problems/partition-labels/

### Problem

String `s`. Partition into as many parts as possible so each letter appears in at most one part.

Return list of integers representing sizes of parts.

### Examples

```
s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation: "ababcbaca", "defegde", "hijhklij"

s = "eccbbbbdec"
Output: [10]
```

### Constraints

- 1 ≤ s.length ≤ 500
- `s` consists of lowercase English letters

### Hints
- Track last occurrence of each character
- Extend partition end to last occurrence
- When reach end, create partition
- O(n) time, O(1) space (fixed 26 letters)

---

## Problem 10: Boats to Save People

**Difficulty:** Medium | **Pattern:** Opposite Direction
**LeetCode:** https://leetcode.com/problems/boats-to-save-people/

### Problem

Array `people` where `people[i]` is weight of i-th person. Boat can carry at most 2 people if their weight sum ≤ `limit`.

Return minimum number of boats to carry everyone.

### Examples

```
people = [1,2], limit = 3
Output: 1

people = [3,2,2,1], limit = 3
Output: 3

people = [3,5,3,4], limit = 5
Output: 4
```

### Constraints

- 1 ≤ people.length ≤ 5×10⁴
- 1 ≤ people[i] ≤ limit ≤ 3×10⁴

### Hints
- Sort people by weight
- Try pairing heaviest with lightest
- If pair too heavy, heaviest takes own boat
- O(n log n) time, O(1) space

---

## Summary

**Total:** 10 problems (4 Easy, 5 Medium, 1 Hard)

**Patterns:**
- Opposite Direction (5)
- Same Direction Fast/Slow (2)
- Multiple Pointers (2)
- Greedy + Two Pointers (1)

**Blind 75:** 5/75 complete (7%)

---

**Ready?** Say: `"Claude, give me the problem"` or `"Go"`

[Solutions](./SOLUTIONS.md) | [Hints](./HINTS.md)
