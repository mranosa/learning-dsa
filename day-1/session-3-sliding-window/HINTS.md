# Hints - Session 3: Sliding Window

Progressive hints for all 10 problems. Use sparingly - struggling is part of learning!

---

## Problem 1: Best Time to Buy and Sell Stock

### Hint Level 1 (Gentle Nudge)
Think of this as finding the maximum difference between two elements where the smaller element comes before the larger. Can you do this in one pass?

### Hint Level 2 (More Direct)
Keep track of the minimum price seen so far. At each new price, calculate what profit you'd make if you sold today (current - min). Update your max profit.

### Hint Level 3 (Step-by-Step)
Algorithm:
1. Initialize `minPrice = prices[0]` and `maxProfit = 0`
2. For each price from index 1:
   - Calculate `profit = prices[i] - minPrice`
   - Update `maxProfit = Math.max(maxProfit, profit)`
   - Update `minPrice = Math.min(minPrice, prices[i])`
3. Return `maxProfit`

---

## Problem 2: Longest Substring Without Repeating Characters

### Hint Level 1
Use a sliding window approach. What data structure helps you quickly check if a character is already in your window?

### Hint Level 2
Use a Set to track characters in the current window. When you find a duplicate, you need to shrink the window from the left until the duplicate is removed.

### Hint Level 3
Complete approach:
1. Use `Set` for characters in window
2. Two pointers: `left = 0`, iterate `right`
3. If `s[right]` is in Set:
   - Remove `s[left]` from Set and increment `left`
   - Repeat until `s[right]` not in Set
4. Add `s[right]` to Set
5. Update `maxLength = Math.max(maxLength, right - left + 1)`

---

## Problem 3: Longest Repeating Character Replacement

### Hint Level 1
The key insight: in a valid window, you can replace all characters except the most frequent one. So `windowSize - maxFrequency <= k`.

### Hint Level 2
Track character frequencies in your window. You don't need to decrease `maxFreq` when sliding - you only care about windows that could be larger than your current best.

### Hint Level 3
Algorithm:
1. Use Map for character frequencies
2. Track `maxFreq` (highest frequency in current window)
3. For each character:
   - Update frequency and `maxFreq`
   - If `windowSize - maxFreq > k`, shrink from left
   - Update result with current window size

---

## Problem 4: Permutation in String

### Hint Level 1
A permutation means the same characters with the same frequencies. Use a fixed-size sliding window equal to `s1.length`.

### Hint Level 2
Compare character frequencies: create a frequency map for `s1`, then slide a window of the same size through `s2` and check if frequencies match.

### Hint Level 3
Optimization approach:
1. Count characters in `s1` using array `[26]`
2. Count first window in `s2`
3. Track number of matching character frequencies
4. Slide window:
   - Update counts for leaving/entering characters
   - Update match count accordingly
   - If all 26 positions match, found permutation

---

## Problem 5: Minimum Window Substring

### Hint Level 1
Use variable-size sliding window. Expand to include all required characters, then contract to find minimum while maintaining validity.

### Hint Level 2
Track two things: characters you "need" (from t) and characters you "have" (in current window). When have == need, you have a valid window.

### Hint Level 3
Detailed algorithm:
1. Count characters in `t` → `need` map
2. Use `have` counter for matching character frequencies
3. Expand right:
   - Add character to window
   - If frequency matches `need`, increment `have`
4. While `have == need.size`:
   - Update minimum window
   - Contract from left
   - If frequency drops below need, decrement `have`

---

## Problem 6: Sliding Window Maximum

### Hint Level 1
Brute force: find max in each window. Can we avoid recalculating the max from scratch? Think about what elements could potentially be the maximum.

### Hint Level 2
Use a deque (double-ended queue) to maintain elements in decreasing order. The front of the deque is always the maximum of the current window.

### Hint Level 3
Monotonic deque approach:
1. Store indices (not values) in deque
2. Before adding new element:
   - Remove indices outside current window (front of deque)
   - Remove indices of smaller elements (back of deque)
3. Add current index
4. Front of deque points to maximum element

---

## Problem 7: Maximum Sum of Distinct Subarrays

### Hint Level 1
Fixed-size sliding window with an additional constraint: all elements must be distinct. How can you track if elements are unique?

### Hint Level 2
Use a frequency map. The window is valid when `map.size === k` (all elements appear exactly once).

### Hint Level 3
Algorithm:
1. Build initial window of size k
2. Track sum and frequencies
3. Check if `freq.size === k` for valid window
4. Slide window:
   - Add new element (update sum and freq)
   - Remove old element (update sum and freq)
   - If `freq.size === k`, update max sum

---

## Problem 8: Fruit Into Baskets

### Hint Level 1
Reframe the problem: find the longest contiguous subarray with at most 2 distinct elements. Classic sliding window!

### Hint Level 2
Use a Map to track fruit types in your current window. When you have more than 2 types, shrink from the left.

### Hint Level 3
Implementation:
1. Map tracks fruit type → count
2. Expand window by adding fruits
3. While `map.size > 2`:
   - Remove leftmost fruit
   - If count becomes 0, delete from map
   - Move left pointer
4. Update max with current window size

---

## Problem 9: Longest Substring with At Most K Distinct

### Hint Level 1
Variable-size sliding window. The constraint is having at most k distinct characters. What data structure tracks distinct elements?

### Hint Level 2
Use a Map for character frequencies. When map.size > k, you need to shrink the window from the left until valid again.

### Hint Level 3
Step-by-step:
1. Map: character → frequency
2. Expand with right pointer
3. While `map.size > k`:
   - Decrease frequency of `s[left]`
   - If frequency becomes 0, remove from map
   - Increment left
4. Update max length with current window

---

## Problem 10: Minimum Size Subarray Sum

### Hint Level 1
Variable-size window: expand until sum >= target, then try to contract while maintaining validity to find minimum size.

### Hint Level 2
Since all numbers are positive, once your window sum >= target, you can greedily shrink from the left to find the minimum valid window.

### Hint Level 3
Algorithm:
1. Initialize `left = 0`, `sum = 0`, `minLen = Infinity`
2. Expand with right pointer:
   - Add `nums[right]` to sum
3. While `sum >= target`:
   - Update `minLen` with current window size
   - Subtract `nums[left]` and increment left
4. Return `minLen` or 0 if no valid window

---

## General Sliding Window Tips

### Recognizing the Pattern
- Keywords: "subarray", "substring", "window", "contiguous"
- Optimization from O(n²) to O(n)
- Finding optimal (longest/shortest/max/min) sequence

### Fixed vs Variable
- **Fixed:** Window size k is given
- **Variable:** Find optimal window size meeting constraints

### Common Mistakes to Avoid
1. Not handling empty input
2. Off-by-one errors in window size calculation
3. Forgetting to update result before contracting
4. Using wrong data structure (Set vs Map)
5. Not considering when no valid window exists