# Problems - Session 3: Sliding Window

Complete these 10 problems in order. Use the UMPIRE method for each.

**Target Times:**
- Easy: <15 min
- Medium: <30 min
- Hard: <45 min

---

## Problem 1: Best Time to Buy and Sell Stock ⭐ BLIND 75

**Difficulty:** Easy
**Time Target:** 10-15 min
**Pattern:** Single Pass / Sliding Window
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
- Track minimum price seen so far
- Calculate profit if selling at current price
- This is essentially a sliding window of size 2 (buy and sell points)

---

## Problem 2: Longest Substring Without Repeating Characters ⭐ BLIND 75

**Difficulty:** Medium
**Time Target:** 20-25 min
**Pattern:** Variable-size Sliding Window
**LeetCode:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

### Problem Statement

Given a string `s`, find the length of the **longest substring** without repeating characters.

### Examples

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with length 3.
```

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with length 1.
```

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with length 3.
Notice that "pwke" is a subsequence, not a substring.
```

```
Input: s = ""
Output: 0
```

### Constraints

- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces

### Hints
- Use a Set to track characters in current window
- Expand window by moving right pointer
- Contract window when duplicate found

---

## Problem 3: Longest Repeating Character Replacement ⭐ BLIND 75

**Difficulty:** Medium
**Time Target:** 25-30 min
**Pattern:** Variable-size Sliding Window with Frequency
**LeetCode:** https://leetcode.com/problems/longest-repeating-character-replacement/

### Problem Statement

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

### Examples

```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
```

### Constraints

- 1 <= s.length <= 10^5
- s consists of only uppercase English letters
- 0 <= k <= s.length

### Hints
- Track frequency of characters in window
- Valid window: windowSize - maxFrequency <= k
- No need to decrease maxFrequency when sliding

---

## Problem 4: Permutation in String ⭐ BLIND 75

**Difficulty:** Medium
**Time Target:** 20-25 min
**Pattern:** Fixed-size Sliding Window
**LeetCode:** https://leetcode.com/problems/permutation-in-string/

### Problem Statement

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is a substring of `s2`.

### Examples

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

```
Input: s1 = "adc", s2 = "dcda"
Output: true
```

### Constraints

- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters

### Hints
- Fixed window of size s1.length
- Compare character frequencies
- Use hash map or array for counting

---

## Problem 5: Minimum Window Substring ⭐ BLIND 75

**Difficulty:** Hard
**Time Target:** 35-45 min
**Pattern:** Variable-size Sliding Window
**LeetCode:** https://leetcode.com/problems/minimum-window-substring/

### Problem Statement

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

### Examples

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

```
Input: s = "a", t = "a"
Output: "a"
```

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

### Constraints

- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters

### Hints
- Use two hash maps: one for t, one for window
- Track "formed" characters (matching count)
- Contract window when all characters found

---

## Problem 6: Sliding Window Maximum

**Difficulty:** Hard
**Time Target:** 35-45 min
**Pattern:** Fixed-size Sliding Window with Deque
**LeetCode:** https://leetcode.com/problems/sliding-window-maximum/

### Problem Statement

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window (array of maximums for each window).

### Examples

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

```
Input: nums = [1], k = 1
Output: [1]
```

### Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length

### Hints
- Use monotonic decreasing deque
- Deque stores indices, not values
- Remove indices outside window

---

## Problem 7: Maximum Sum of Distinct Subarrays With Length K

**Difficulty:** Medium
**Time Target:** 25-30 min
**Pattern:** Fixed-size Sliding Window with Frequency
**LeetCode:** https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

### Problem Statement

You are given an integer array `nums` and an integer `k`. Find the maximum sum of a subarray of size `k` that contains **distinct** elements.

Return the maximum sum of any such subarray. If no such subarray exists, return `0`.

### Examples

```
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays [5,4,2] and [4,2,9] have distinct elements with sum 11 and 15.
```

```
Input: nums = [4,4,4], k = 3
Output: 0
Explanation: No subarray of size 3 has all distinct elements.
```

```
Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: [4,5] has maximum sum among all distinct subarrays of size 2.
```

### Constraints

- 1 <= k <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5

### Hints
- Fixed window of size k
- Use Map to track frequencies
- Valid window: map.size === k

---

## Problem 8: Fruit Into Baskets

**Difficulty:** Medium
**Time Target:** 25-30 min
**Pattern:** Variable-size Sliding Window
**LeetCode:** https://leetcode.com/problems/fruit-into-baskets/

### Problem Statement

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit the `i`th tree produces.

You want to collect as much fruit as possible. However, the owner has some rules:
- You only have two baskets
- Each basket can only hold one type of fruit
- Once you start, you must pick exactly one fruit from every tree while moving right
- You must stop when you cannot pick anymore

Given the integer array `fruits`, return the maximum number of fruits you can pick.

### Examples

```
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick all 3 fruits.
```

```
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick [1,2,2].
```

```
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick [2,3,2,2].
```

### Constraints

- 1 <= fruits.length <= 10^5
- 0 <= fruits[i] < fruits.length

### Hints
- This is "longest subarray with at most 2 distinct elements"
- Use Map to track fruit types in window
- Contract when map.size > 2

---

## Problem 9: Longest Substring with At Most K Distinct Characters

**Difficulty:** Medium
**Time Target:** 25-30 min
**Pattern:** Variable-size Sliding Window
**LeetCode:** https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

### Problem Statement

Given a string `s` and an integer `k`, return the length of the longest substring of `s` that contains at most `k` distinct characters.

### Examples

```
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
```

```
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
```

```
Input: s = "abcde", k = 3
Output: 3
Explanation: The substring is "abc", "bcd", or "cde" with length 3.
```

### Constraints

- 1 <= s.length <= 5 * 10^4
- 0 <= k <= 50
- s consists of English letters

### Hints
- Track character frequencies with Map
- Contract when map.size > k
- Update result before contracting

---

## Problem 10: Minimum Size Subarray Sum

**Difficulty:** Medium
**Time Target:** 20-25 min
**Pattern:** Variable-size Sliding Window
**LeetCode:** https://leetcode.com/problems/minimum-size-subarray-sum/

### Problem Statement

Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

### Examples

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

```
Input: target = 4, nums = [1,4,4]
Output: 1
```

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

### Constraints

- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4

### Hints
- Expand window to reach target
- Contract to find minimum length
- Use while loop for contracting

---

## Problem-Solving Strategy

For each problem:
1. **Identify the pattern** - Fixed or variable window?
2. **Set up the window** - Initialize pointers and data structures
3. **Expand the window** - Move right pointer
4. **Check validity** - Does window meet criteria?
5. **Contract if needed** - Move left pointer to maintain validity
6. **Update result** - Track maximum/minimum/count
7. **Handle edge cases** - Empty input, single element, no valid window

Remember: The key to sliding window is avoiding recalculation by updating incrementally!