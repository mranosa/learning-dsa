# Problems - Session 1: Big O & Arrays

Complete these 10 problems in order. Use the UMPIRE method for each.

**Target Times:**
- Easy: <15 min
- Medium: <30 min
- Hard: <45 min

---

## Problem 1: Two Sum ⭐ BLIND 75

**Difficulty:** Easy
**Time Target:** 10-15 min
**Pattern:** Hash Map
**LeetCode:** https://leetcode.com/problems/two-sum/

### Problem Statement

Given an array of integers `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

### Examples

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

### Constraints

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists

### Hints
- Brute force: O(n²) with nested loops
- Optimal: Use hash map for O(1) lookups → O(n) time
- Store value→index mapping as you iterate

---

## Problem 2: Best Time to Buy and Sell Stock ⭐ BLIND 75

**Difficulty:** Easy
**Time Target:** 10-15 min
**Pattern:** Kadane's Algorithm / Greedy
**LeetCode:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

### Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve. If you cannot achieve any profit, return `0`.

### Examples

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
```

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No profit possible (prices only decrease).
```

### Constraints

- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

### Hints
- Must buy before selling
- Track minimum price seen so far
- Track maximum profit at each step
- One pass: O(n) time, O(1) space

---

## Problem 3: Contains Duplicate ⭐ BLIND 75

**Difficulty:** Easy
**Time Target:** 5-10 min
**Pattern:** Hash Set
**LeetCode:** https://leetcode.com/problems/contains-duplicate/

### Problem Statement

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

### Examples

```
Input: nums = [1,2,3,1]
Output: true
```

```
Input: nums = [1,2,3,4]
Output: false
```

```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

### Constraints

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

### Hints
- Use Set to track seen numbers
- If number already in set → duplicate found
- O(n) time, O(n) space

---

## Problem 4: Product of Array Except Self ⭐ BLIND 75

**Difficulty:** Medium
**Time Target:** 20-25 min
**Pattern:** Prefix/Suffix Products
**LeetCode:** https://leetcode.com/problems/product-of-array-except-self/

### Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

You must write an algorithm that runs in **O(n)** time and **without using the division operation**.

### Examples

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation:
- answer[0] = 2*3*4 = 24
- answer[1] = 1*3*4 = 12
- answer[2] = 1*2*4 = 8
- answer[3] = 1*2*3 = 6
```

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

### Constraints

- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix is guaranteed to fit in a 32-bit integer

### Follow-up
Can you solve it in O(1) extra space? (Output array doesn't count)

### Hints
- For each position, need product of all elements to its left × all elements to its right
- Calculate prefix products (left to right)
- Calculate suffix products (right to left)
- Can optimize to O(1) space by reusing output array

---

## Problem 5: Maximum Subarray (Kadane's Algorithm) ⭐ BLIND 75

**Difficulty:** Easy
**Time Target:** 15-20 min
**Pattern:** Kadane's Algorithm / DP
**LeetCode:** https://leetcode.com/problems/maximum-subarray/

### Problem Statement

Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

A **subarray** is a contiguous non-empty sequence of elements within an array.

### Examples

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

```
Input: nums = [1]
Output: 1
```

```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has sum 23.
```

### Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

### Follow-up
If you figured out the O(n) solution, try coding another solution using the divide and conquer approach (harder, O(n log n)).

### Hints
- Kadane's Algorithm: At each position, decide whether to extend current subarray or start new one
- `currentSum = max(nums[i], currentSum + nums[i])`
- Track maximum sum seen so far
- O(n) time, O(1) space

---

## Problem 6: Maximum Product Subarray ⭐ BLIND 75

**Difficulty:** Medium
**Time Target:** 25-30 min
**Pattern:** Dynamic Programming
**LeetCode:** https://leetcode.com/problems/maximum-product-subarray/

### Problem Statement

Given an integer array `nums`, find a subarray that has the largest product, and return the product.

A **subarray** is a contiguous non-empty sequence of elements within an array.

### Examples

```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

```
Input: nums = [-2,0,-1]
Output: 0
```

```
Input: nums = [-2,3,-4]
Output: 24
Explanation: [-2,3,-4] has product 24.
```

### Constraints

- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any subarray is guaranteed to fit in a 32-bit integer

### Hints
- Similar to max subarray, but multiplication is trickier
- Negative numbers: a negative × negative = positive!
- Track both max AND min products (min can become max when multiplied by negative)
- Handle zero specially (resets products)
- O(n) time, O(1) space

---

## Problem 7: Find Minimum in Rotated Sorted Array ⭐ BLIND 75

**Difficulty:** Medium
**Time Target:** 20-25 min
**Pattern:** Binary Search
**LeetCode:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

### Problem Statement

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times.

Given the rotated sorted array `nums` of **unique** elements, return the minimum element.

You must write an algorithm that runs in **O(log n)** time.

### Examples

```
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

```
Input: nums = [4,5,6,7,0,1,2]
Output: 0
```

```
Input: nums = [11,13,15,17]
Output: 11
Explanation: Not rotated at all.
```

### Constraints

- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All integers are **unique**
- nums is sorted and rotated between 1 and n times

### Hints
- Binary search, but need to figure out which half to search
- Compare mid with right element
- If nums[mid] > nums[right] → minimum is in right half
- Otherwise → minimum is in left half (including mid)
- O(log n) time, O(1) space

---

## Problem 8: Search in Rotated Sorted Array ⭐ BLIND 75

**Difficulty:** Medium
**Time Target:** 25-30 min
**Pattern:** Binary Search
**LeetCode:** https://leetcode.com/problems/search-in-rotated-sorted-array/

### Problem Statement

There is an integer array `nums` sorted in ascending order (with **distinct** values), rotated at some pivot.

Given the array `nums` after rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not.

You must write an algorithm with **O(log n)** runtime complexity.

### Examples

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

```
Input: nums = [1], target = 0
Output: -1
```

### Constraints

- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values are **unique**
- nums is rotated at some pivot
- -10^4 <= target <= 10^4

### Hints
- Modified binary search
- At least one half of the array is always sorted
- Figure out which half is sorted, then check if target is in that half
- O(log n) time, O(1) space

---

## Problem 9: 3Sum ⭐ BLIND 75

**Difficulty:** Medium
**Time Target:** 30-35 min
**Pattern:** Two Pointers
**LeetCode:** https://leetcode.com/problems/3sum/

### Problem Statement

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

The solution set must not contain duplicate triplets.

### Examples

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
```

```
Input: nums = [0,1,1]
Output: []
```

```
Input: nums = [0,0,0]
Output: [[0,0,0]]
```

### Constraints

- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

### Hints
- Sort array first
- Fix one number, use two pointers for the other two (like Two Sum)
- Skip duplicates to avoid duplicate triplets
- O(n²) time, O(1) space (not counting output)

---

## Problem 10: Container With Most Water ⭐ BLIND 75

**Difficulty:** Medium
**Time Target:** 20-25 min
**Pattern:** Two Pointers
**LeetCode:** https://leetcode.com/problems/container-with-most-water/

### Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container that contains the most water.

Return the maximum amount of water the container can store.

**Note:** You may not slant the container.

### Examples

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The lines at index 1 and 8 form the container. Area = min(8,7) * (8-1) = 7 * 7 = 49.
```

```
Input: height = [1,1]
Output: 1
```

### Constraints

- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

### Hints
- Two pointers: start at both ends
- Area = min(height[left], height[right]) * (right - left)
- Move pointer with smaller height inward (might find taller line)
- O(n) time, O(1) space

---

## Session Summary

**Total Problems:** 10
- Easy: 5 (Problems 1, 2, 3, 5, and warmup parts)
- Medium: 5 (Problems 4, 6, 7, 8, 9, 10)
- Hard: 0 (gradually building up!)

**Patterns Covered:**
- Hash Map / Hash Set
- Kadane's Algorithm
- Prefix/Suffix Arrays
- Binary Search (Rotated)
- Two Pointers

**Blind 75 Coverage:** 10/75 problems (13% complete after this session!)

---

**Ready to start?** Say: `"Claude, give me the problem"` or `"Go"`

[Solutions in SOLUTIONS.md] | [Hints in HINTS.md]
