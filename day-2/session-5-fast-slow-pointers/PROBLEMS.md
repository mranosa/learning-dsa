# Fast/Slow Pointers - Problems

## Problem 1: Linked List Cycle (Easy)

**Link:** [LeetCode 141](https://leetcode.com/problems/linked-list-cycle/)

Given `head`, determine if the linked list has a cycle.

**Example:**
```
Input: head = [3,2,0,-4], pos = 1
Output: true
```

**Constraints:**
- 0 <= nodes <= 10^4
- -10^5 <= Node.val <= 10^5

---

## Problem 2: Linked List Cycle II (Medium)

**Link:** [LeetCode 142](https://leetcode.com/problems/linked-list-cycle-ii/)

Return the node where the cycle begins. Return `null` if no cycle.

**Example:**
```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
```

**Constraints:**
- 0 <= nodes <= 10^4
- **Do not modify** the list

**Follow up:** O(1) memory?

---

## Problem 3: Happy Number (Easy)

**Link:** [LeetCode 202](https://leetcode.com/problems/happy-number/)

A happy number reaches 1 when repeatedly replacing with sum of squares of digits.

**Example:**
```
Input: n = 19
Output: true
Explanation: 1² + 9² = 82 → 8² + 2² = 68 → ... → 1
```

**Constraints:**
- 1 <= n <= 2^31 - 1

---

## Problem 4: Middle of the Linked List (Easy)

**Link:** [LeetCode 876](https://leetcode.com/problems/middle-of-the-linked-list/)

Return the middle node. If two middle nodes, return the second.

**Example:**
```
Input: head = [1,2,3,4,5]
Output: [3,4,5]
```

**Constraints:**
- 1 <= nodes <= 100

---

## Problem 5: Find the Duplicate Number (Medium)

**Link:** [LeetCode 287](https://leetcode.com/problems/find-the-duplicate-number/)

Array of `n + 1` integers where each is in `[1, n]`. Find the duplicate.

**Example:**
```
Input: nums = [1,3,4,2,2]
Output: 2
```

**Constraints:**
- 1 <= n <= 10^5
- **Cannot modify** array
- **O(1) extra space**

**Follow up:** Prove duplicate must exist. Linear time?

---

## Problem 6: Remove Nth Node From End of List (Medium)

**Link:** [LeetCode 19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

Remove the nth node from end and return head.

**Example:**
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

**Constraints:**
- 1 <= sz <= 30
- 1 <= n <= sz

**Follow up:** One pass?

---

## Problem 7: Reorder List (Medium)

**Link:** [LeetCode 143](https://leetcode.com/problems/reorder-list/)

Reorder L₀ → L₁ → ... → Lₙ to L₀ → Lₙ → L₁ → Lₙ₋₁ → L₂ → Lₙ₋₂ → ...

**Example:**
```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

**Constraints:**
- 1 <= nodes <= 5 × 10^4
- Only nodes may be changed, not values

---

## Problem 8: Palindrome Linked List (Easy)

**Link:** [LeetCode 234](https://leetcode.com/problems/palindrome-linked-list/)

Return `true` if palindrome.

**Example:**
```
Input: head = [1,2,2,1]
Output: true
```

**Constraints:**
- 1 <= nodes <= 10^5

**Follow up:** O(n) time, O(1) space?

---

## Problem 9: Circular Array Loop (Medium)

**Link:** [LeetCode 457](https://leetcode.com/problems/circular-array-loop/)

Return `true` if valid cycle exists in circular array.

Valid cycle:
- All moves same direction (all positive or all negative)
- Length > 1

**Example:**
```
Input: nums = [2,-1,1,2,2]
Output: true
Explanation: Cycle 0 → 2 → 3 → 0
```

**Constraints:**
- 1 <= nums.length <= 5000
- -1000 <= nums[i] <= 1000
- nums[i] != 0

**Follow up:** O(n) time, O(1) space?

---

## Problem 10: Intersection of Two Linked Lists (Easy)

**Link:** [LeetCode 160](https://leetcode.com/problems/intersection-of-two-linked-lists/)

Return the intersection node of two lists. Return `null` if no intersection.

**Example:**
```
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]
Output: Intersected at '8'
```

**Constraints:**
- 1 <= m, n <= 3 × 10^4
- Lists must retain original structure

**Follow up:** O(m + n) time, O(1) memory?

---

## Recommended Order

1. **Problem 1** - Basic pattern
2. **Problem 4** - Simple variation
3. **Problem 3** - Apply to sequences
4. **Problem 2** - Cycle entry
5. **Problem 8** - Combine with reversal
6. **Problem 10** - Two-list manipulation
7. **Problem 6** - Precise control
8. **Problem 5** - Array as list
9. **Problem 7** - Complex manipulation
10. **Problem 9** - Most complex

---

## Time Goals

- **Easy:** 15-20 min
- **Medium:** 25-30 min
- **Total:** 2-4 hours

Speed comes with practice!
