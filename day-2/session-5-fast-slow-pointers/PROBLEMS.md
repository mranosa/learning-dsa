# Fast/Slow Pointers - Problem Set

## Problem 1: Linked List Cycle (Easy)

**Link:** [LeetCode 141](https://leetcode.com/problems/linked-list-cycle/)

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

**Example 1:**
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

**Example 2:**
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

**Example 3:**
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

**Constraints:**
- The number of nodes in the list is in the range [0, 10^4]
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list

---

## Problem 2: Linked List Cycle II (Medium)

**Link:** [LeetCode 142](https://leetcode.com/problems/linked-list-cycle-ii/)

Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

**Do not modify** the linked list.

**Example 1:**
```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

**Example 2:**
```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

**Example 3:**
```
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
```

**Constraints:**
- The number of nodes in the list is in the range [0, 10^4]
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list

**Follow up:** Can you solve it using O(1) memory?

---

## Problem 3: Happy Number (Easy)

**Link:** [LeetCode 202](https://leetcode.com/problems/happy-number/)

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return `true` if `n` is a happy number, and `false` otherwise.

**Example 1:**
```
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
```

**Example 2:**
```
Input: n = 2
Output: false
Explanation: The cycle is 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4...
```

**Constraints:**
- 1 <= n <= 2^31 - 1

---

## Problem 4: Middle of the Linked List (Easy)

**Link:** [LeetCode 876](https://leetcode.com/problems/middle-of-the-linked-list/)

Given the `head` of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return **the second middle** node.

**Example 1:**
```
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
```

**Example 2:**
```
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
```

**Constraints:**
- The number of nodes in the list is in the range [1, 100]
- 1 <= Node.val <= 100

---

## Problem 5: Find the Duplicate Number (Medium)

**Link:** [LeetCode 287](https://leetcode.com/problems/find-the-duplicate-number/)

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return this repeated number.

You must solve the problem **without** modifying the array `nums` and uses only constant extra space.

**Example 1:**
```
Input: nums = [1,3,4,2,2]
Output: 2
```

**Example 2:**
```
Input: nums = [3,1,3,4,2]
Output: 3
```

**Example 3:**
```
Input: nums = [3,3,3,3,3]
Output: 3
```

**Constraints:**
- 1 <= n <= 10^5
- nums.length == n + 1
- 1 <= nums[i] <= n
- All the integers in nums appear only once except for precisely one integer which appears two or more times

**Follow up:**
- How can you prove that at least one duplicate number must exist in nums?
- Can you solve the problem in linear runtime complexity?

---

## Problem 6: Remove Nth Node From End of List (Medium)

**Link:** [LeetCode 19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

**Example 1:**
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

**Example 2:**
```
Input: head = [1], n = 1
Output: []
```

**Example 3:**
```
Input: head = [1,2], n = 1
Output: [1]
```

**Constraints:**
- The number of nodes in the list is sz
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

**Follow up:** Could you do this in one pass?

---

## Problem 7: Reorder List (Medium)

**Link:** [LeetCode 143](https://leetcode.com/problems/reorder-list/)

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder it to:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

**Example 1:**
```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

**Example 2:**
```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

**Constraints:**
- The number of nodes in the list is in the range [1, 5 * 10^4]
- 1 <= Node.val <= 1000

---

## Problem 8: Palindrome Linked List (Easy)

**Link:** [LeetCode 234](https://leetcode.com/problems/palindrome-linked-list/)

Given the `head` of a singly linked list, return `true` if it is a palindrome or `false` otherwise.

**Example 1:**
```
Input: head = [1,2,2,1]
Output: true
```

**Example 2:**
```
Input: head = [1,2]
Output: false
```

**Constraints:**
- The number of nodes in the list is in the range [1, 10^5]
- 0 <= Node.val <= 9

**Follow up:** Could you do it in O(n) time and O(1) space?

---

## Problem 9: Circular Array Loop (Medium)

**Link:** [LeetCode 457](https://leetcode.com/problems/circular-array-loop/)

You are playing a game involving a **circular** array of non-zero integers `nums`. Each `nums[i]` denotes the number of indices forward/backward you must move if you are located at index `i`:

- If `nums[i]` is positive, move `nums[i]` steps forward
- If `nums[i]` is negative, move `nums[i]` steps backward

Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backward from the first element puts you on the last element.

A **cycle** in the array consists of a sequence of indices `seq` of length `k` where:
- Following the movement rules above results in the repeating index sequence `seq[0] -> seq[1] -> ... -> seq[k-1] -> seq[0] -> ...`
- Every `nums[seq[j]]` is either all positive or all negative
- `k > 1`

Return `true` if there is a cycle in `nums`, or `false` otherwise.

**Example 1:**
```
Input: nums = [2,-1,1,2,2]
Output: true
Explanation: The graph has a cycle: 0 -> 2 -> 3 -> 0
```

**Example 2:**
```
Input: nums = [-1,2]
Output: false
Explanation: The sequence from index 1 -> 1 -> 1 ... is not a cycle because the sequence's length is 1.
```

**Example 3:**
```
Input: nums = [-2,1,-1,-2,-2]
Output: false
Explanation: The graph does not have any cycle.
```

**Constraints:**
- 1 <= nums.length <= 5000
- -1000 <= nums[i] <= 1000
- nums[i] != 0

**Follow up:** Could you solve it in O(n) time complexity and O(1) extra space complexity?

---

## Problem 10: Intersection of Two Linked Lists (Easy)

**Link:** [LeetCode 160](https://leetcode.com/problems/intersection-of-two-linked-lists/)

Given the heads of two singly linked-lists `headA` and `headB`, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return `null`.

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

**Note** that the linked lists must retain their original structure after the function returns.

**Example 1:**
```
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The value of the node where the two lists intersect is 8.
```

**Example 2:**
```
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
```

**Example 3:**
```
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
```

**Constraints:**
- The number of nodes of listA is in the m
- The number of nodes of listB is in the n
- 1 <= m, n <= 3 * 10^4
- 1 <= Node.val <= 10^5
- 0 <= skipA < m
- 0 <= skipB < n
- intersectVal is 0 if listA and listB do not intersect
- intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect

**Follow up:** Could you write a solution that runs in O(m + n) time and use only O(1) memory?

---

## Problem Order

**Recommended solving order:**
1. Start with Problem 1 (Linked List Cycle) - Basic pattern
2. Then Problem 4 (Middle of the Linked List) - Simple variation
3. Problem 3 (Happy Number) - Apply to sequences
4. Problem 2 (Linked List Cycle II) - Advanced cycle detection
5. Problem 8 (Palindrome Linked List) - Combine with reversal
6. Problem 10 (Intersection of Two Linked Lists) - Two list manipulation
7. Problem 6 (Remove Nth Node) - Precise pointer control
8. Problem 5 (Find Duplicate) - Array as linked list
9. Problem 7 (Reorder List) - Complex manipulation
10. Problem 9 (Circular Array Loop) - Most complex

---

## Time Goals

- **Easy problems:** 15-20 minutes each
- **Medium problems:** 25-30 minutes each
- **Total session:** 2-4 hours

Don't worry if you take longer initially. Speed comes with practice!