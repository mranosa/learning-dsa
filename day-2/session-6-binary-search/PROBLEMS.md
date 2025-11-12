# Problems - Session 6: Binary Search

10 problems in order. Use UMPIRE method.

**Targets:** Easy <15 min | Medium <30 min | Hard <45 min

---

## Problem 1: Binary Search

**Difficulty:** Easy | **Pattern:** Classic Binary Search
**LeetCode:** https://leetcode.com/problems/binary-search/

### Problem

Given sorted array `nums` (ascending) and integer `target`, search for `target`. Return index if exists, otherwise -1.

Must be O(log n).

### Examples

```
nums = [-1,0,3,5,9,12], target = 9
Output: 4

nums = [-1,0,3,5,9,12], target = 2
Output: -1
```

### Constraints

- 1 ≤ nums.length ≤ 10⁴
- -10⁴ < nums[i], target < 10⁴
- All values unique
- Sorted ascending

### Hints
- Use two pointers: left, right
- Calculate mid, compare with target
- Eliminate half each iteration

---

## Problem 2: Search Insert Position

**Difficulty:** Easy | **Pattern:** Binary Search Boundary
**LeetCode:** https://leetcode.com/problems/search-insert-position/

### Problem

Sorted array of distinct integers. Given `target`, return index if found, else return index where it would be inserted.

Must be O(log n).

### Examples

```
nums = [1,3,5,6], target = 5 → 2

nums = [1,3,5,6], target = 2 → 1

nums = [1,3,5,6], target = 7 → 4
```

### Constraints

- 1 ≤ nums.length ≤ 10⁴
- -10⁴ ≤ nums[i] ≤ 10⁴
- Distinct values, sorted ascending
- -10⁴ ≤ target ≤ 10⁴

### Hints
- Standard binary search
- When not found, `left` is insertion position
- Why? All elements before `left` are < target

---

## Problem 3: First Bad Version

**Difficulty:** Easy | **Pattern:** Binary Search for Boundary
**LeetCode:** https://leetcode.com/problems/first-bad-version/

### Problem

You have `n` versions `[1, 2, ..., n]`. Find first bad version using API `isBadVersion(version)` which returns boolean.

All versions after bad version are also bad.

Minimize API calls.

### Examples

```
n = 5, bad = 4
Output: 4
(call isBadVersion(3) → false)
(call isBadVersion(5) → true)
(call isBadVersion(4) → true)
```

### Constraints

- 1 ≤ bad ≤ n ≤ 2³¹ - 1

### Hints
- Find first position where condition becomes true
- Use `left < right` template
- When isBadVersion(mid) is true, search left

---

## Problem 4: Find Minimum in Rotated Sorted Array

**Difficulty:** Medium | **Pattern:** Modified Binary Search
**LeetCode:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

### Problem

Sorted array rotated between 1 and n times. All elements unique. Return minimum element.

Must be O(log n).

### Examples

```
nums = [3,4,5,1,2] → 1

nums = [4,5,6,7,0,1,2] → 0

nums = [11,13,15,17] → 11 (no rotation)
```

### Constraints

- 1 ≤ n ≤ 5000
- -5000 ≤ nums[i] ≤ 5000
- All values unique
- Original array was sorted

### Hints
- Compare mid with right element
- If nums[mid] > nums[right] → minimum in right half
- Otherwise → minimum in left half (including mid)

---

## Problem 5: Search in Rotated Sorted Array

**Difficulty:** Medium | **Pattern:** Modified Binary Search
**LeetCode:** https://leetcode.com/problems/search-in-rotated-sorted-array/

### Problem

Sorted array rotated at unknown pivot. Find `target` index. Return -1 if not found.

Must be O(log n).

### Examples

```
nums = [4,5,6,7,0,1,2], target = 0 → 4

nums = [4,5,6,7,0,1,2], target = 3 → -1

nums = [1], target = 0 → -1
```

### Constraints

- 1 ≤ nums.length ≤ 5000
- -10⁴ ≤ nums[i] ≤ 10⁴
- All values unique
- Rotated at pivot

### Hints
- At least one half always sorted
- Determine which half sorted
- Check if target in sorted half
- Search appropriate half

---

## Problem 6: Search a 2D Matrix

**Difficulty:** Medium | **Pattern:** 2D Binary Search
**LeetCode:** https://leetcode.com/problems/search-a-2d-matrix/

### Problem

`m × n` matrix where:
- Each row sorted non-decreasing
- First integer of row > last integer of previous row

Return true if `target` in matrix.

Must be O(log(m × n)).

### Examples

```
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

### Constraints

- m == matrix.length
- n == matrix[i].length
- 1 ≤ m, n ≤ 100
- -10⁴ ≤ matrix[i][j], target ≤ 10⁴

### Hints
- Treat as flattened 1D array
- Index conversion: row = idx / cols, col = idx % cols
- Standard binary search on indices [0, m×n-1]

---

## Problem 7: Koko Eating Bananas

**Difficulty:** Medium | **Pattern:** Binary Search on Answer
**LeetCode:** https://leetcode.com/problems/koko-eating-bananas/

### Problem

n piles of bananas, pile[i] has count. Guards return in h hours.

Koko chooses eating speed k (bananas/hour). Each hour, picks pile and eats k bananas. If pile < k, eats all and waits.

Return minimum k to eat all within h hours.

### Examples

```
piles = [3,6,7,11], h = 8 → 4

piles = [30,11,23,4,20], h = 5 → 30

piles = [30,11,23,4,20], h = 6 → 23
```

### Constraints

- 1 ≤ piles.length ≤ 10⁴
- piles.length ≤ h ≤ 10⁹
- 1 ≤ piles[i] ≤ 10⁹

### Hints
- Binary search on speed (not array)
- Min speed = 1, max speed = max(piles)
- For each speed, check if can finish in h hours
- Hours for pile = Math.ceil(pile / speed)

---

## Problem 8: Find Peak Element

**Difficulty:** Medium | **Pattern:** Binary Search on Property
**LeetCode:** https://leetcode.com/problems/find-peak-element/

### Problem

Peak element = strictly greater than neighbors.

Given array `nums`, find peak index. If multiple peaks, return any.

Assume `nums[-1] = nums[n] = -∞`.

Must be O(log n).

### Examples

```
nums = [1,2,3,1] → 2 (3 is peak)

nums = [1,2,1,3,5,6,4] → 5 or 1
```

### Constraints

- 1 ≤ nums.length ≤ 1000
- -2³¹ ≤ nums[i] ≤ 2³¹ - 1
- nums[i] ≠ nums[i+1] for all valid i

### Hints
- Compare nums[mid] with nums[mid+1]
- If ascending (mid < mid+1), peak must be right
- If descending (mid > mid+1), peak at mid or left
- Always moves toward higher slope

---

## Problem 9: Time Based Key-Value Store

**Difficulty:** Medium | **Pattern:** Binary Search in Data Structure
**LeetCode:** https://leetcode.com/problems/time-based-key-value-store/

### Problem

Design time-based key-value store with multiple values per key at different timestamps.

Implement `TimeMap`:
- `set(key, value, timestamp)` - store key with value at timestamp
- `get(key, timestamp)` - return value where set was called with timestamp_prev ≤ timestamp (largest such timestamp). Return "" if none.

### Examples

```
timeMap.set("foo", "bar", 1)
timeMap.get("foo", 1) → "bar"
timeMap.get("foo", 3) → "bar"
timeMap.set("foo", "bar2", 4)
timeMap.get("foo", 4) → "bar2"
timeMap.get("foo", 5) → "bar2"
```

### Constraints

- 1 ≤ key.length, value.length ≤ 100
- Lowercase English letters and digits
- 1 ≤ timestamp ≤ 10⁷
- Timestamps strictly increasing
- At most 2×10⁵ calls to set and get

### Hints
- Map<key, Array<[timestamp, value]>>
- Timestamps are sorted (strictly increasing)
- Binary search for largest timestamp ≤ requested

---

## Problem 10: Median of Two Sorted Arrays

**Difficulty:** Hard | **Pattern:** Advanced Binary Search
**LeetCode:** https://leetcode.com/problems/median-of-two-sorted-arrays/

### Problem

Two sorted arrays `nums1` and `nums2` of size m and n. Return median of combined arrays.

Must be O(log(m+n)).

### Examples

```
nums1 = [1,3], nums2 = [2]
Output: 2.00000
(merged = [1,2,3])

nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
(merged = [1,2,3,4], median = (2+3)/2)
```

### Constraints

- nums1.length == m
- nums2.length == n
- 0 ≤ m ≤ 1000
- 0 ≤ n ≤ 1000
- 1 ≤ m + n ≤ 2000
- -10⁶ ≤ nums1[i], nums2[i] ≤ 10⁶

### Hints
- Binary search on smaller array
- Partition both arrays into equal halves
- Ensure max(left) ≤ min(right) for both arrays
- Handle odd/even total length

---

## Summary

**Total:** 10 problems (3 Easy, 6 Medium, 1 Hard)

**Patterns:**
- Classic Binary Search
- Modified Binary Search (rotated)
- Binary Search on Answer Space
- 2D Binary Search
- Boundary Finding

**Blind 75:** 2/75 (Search in Rotated, Find Minimum)

---

**Ready?** Say: `"Claude, give me the problem"` or `"Go"`

[Solutions](./SOLUTIONS.md) | [Hints](./HINTS.md)
