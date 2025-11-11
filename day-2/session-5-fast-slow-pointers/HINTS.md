# Fast/Slow Pointers - Progressive Hints

## Problem 1: Linked List Cycle

### Hint Level 1 (Gentle)
Think about what happens if two people run around a circular track at different speeds. Will they eventually meet?

### Hint Level 2 (Direct)
Use two pointers moving at different speeds. If there's a cycle, the faster pointer will eventually catch up to the slower one. What speeds should you use?

### Hint Level 3 (Detailed)
Initialize two pointers at head. Move `slow` one step and `fast` two steps in each iteration. If they meet, there's a cycle. If `fast` reaches null, there's no cycle. Handle edge cases: empty list or single node.

---

## Problem 2: Linked List Cycle II

### Hint Level 1 (Gentle)
This builds on Problem 1. After detecting a cycle exists, how can you find where it starts? There's a mathematical relationship between the meeting point and the cycle entrance.

### Hint Level 2 (Direct)
Use Floyd's algorithm in two phases:
1. Detect if cycle exists (like Problem 1)
2. When pointers meet, reset one to head. Move both one step at a time - they'll meet at cycle entrance.

### Hint Level 3 (Detailed)
Phase 1: Use fast/slow pointers to detect cycle. If they meet, proceed to Phase 2.
Phase 2: Reset slow to head, keep fast at meeting point. Move both one step at a time. They will meet at the cycle's starting node. This works because the distance from head to cycle start equals the distance from meeting point to cycle start (traveling through the cycle).

---

## Problem 3: Happy Number

### Hint Level 1 (Gentle)
If a number isn't happy, the sequence of transformations will eventually repeat. Sound familiar? This is just cycle detection in a different form!

### Hint Level 2 (Direct)
Treat the transformation as a "next" pointer. Use Floyd's cycle detection:
- Slow: apply transformation once
- Fast: apply transformation twice
If they meet at 1, it's happy. If they meet elsewhere, it's not happy.

### Hint Level 3 (Detailed)
Create a helper function `getNext(n)` that returns the sum of squares of digits. Then apply Floyd's algorithm:
```typescript
let slow = n, fast = n;
do {
    slow = getNext(slow);
    fast = getNext(getNext(fast));
} while (slow !== fast);
return slow === 1;
```

---

## Problem 4: Middle of the Linked List

### Hint Level 1 (Gentle)
If someone runs twice as fast as you, where are you when they finish the race?

### Hint Level 2 (Direct)
Use fast/slow pointers. When fast reaches the end, slow will be at the middle. Remember: if there are two middle nodes, return the second one.

### Hint Level 3 (Detailed)
Initialize both pointers at head. Move slow one step and fast two steps. When fast can't move anymore (fast === null or fast.next === null), slow is at the middle. For even-length lists, this naturally gives you the second middle node.

---

## Problem 5: Find the Duplicate Number

### Hint Level 1 (Gentle)
The array can be viewed as a linked list where nums[i] points to index nums[i]. Since there's a duplicate, there must be a cycle. Can you apply cycle detection?

### Hint Level 2 (Direct)
Treat the array as an implicit linked list:
- Value at index i tells you the next index to visit
- A duplicate means two indices point to the same value (cycle!)
Use Floyd's algorithm to find the cycle entrance.

### Hint Level 3 (Detailed)
Phase 1: Start both pointers at nums[0]. Move slow to nums[slow] and fast to nums[nums[fast]]. They'll meet in the cycle.
Phase 2: Reset slow to nums[0]. Move both pointers one step at a time (slow = nums[slow], fast = nums[fast]). They'll meet at the duplicate number.

---

## Problem 6: Remove Nth Node From End of List

### Hint Level 1 (Gentle)
If you had two pointers and one was N nodes ahead, what happens when the leading pointer reaches the end?

### Hint Level 2 (Direct)
Use two pointers with a gap of n nodes between them. When the fast pointer reaches the end, the slow pointer will be just before the node to remove.

### Hint Level 3 (Detailed)
1. Use a dummy node to handle edge case of removing head
2. Advance fast pointer n+1 times (to position slow pointer before target)
3. Move both pointers until fast reaches end
4. Now slow.next is the node to remove
5. Skip it: slow.next = slow.next.next

---

## Problem 7: Reorder List

### Hint Level 1 (Gentle)
The pattern is: first, last, second, second-to-last... This suggests you need to work with both halves of the list. How can you access the second half in reverse order?

### Hint Level 2 (Direct)
Three steps:
1. Find the middle of the list (fast/slow pointers)
2. Reverse the second half of the list
3. Merge the two halves alternately

### Hint Level 3 (Detailed)
1. Use fast/slow to find middle (slow will be at middle)
2. Split list at middle: slow.next = null
3. Reverse second half starting from what was slow.next
4. Merge: Take one from first half, then one from reversed second half, repeat
Remember to save next pointers before modifying them during merge!

---

## Problem 8: Palindrome Linked List

### Hint Level 1 (Gentle)
To check if something is a palindrome, you need to compare the first half with the reversed second half. How can you do this with O(1) space?

### Hint Level 2 (Direct)
1. Find the middle using fast/slow pointers
2. Reverse the second half of the list
3. Compare first half with reversed second half
4. (Optional) Restore the list structure

### Hint Level 3 (Detailed)
```typescript
// Find middle (slow will be at middle)
while (fast.next && fast.next.next) { slow = slow.next; fast = fast.next.next; }
// Reverse from slow.next
// Compare head with reversed second half
// Return false if any values don't match
```
Note: For odd-length lists, middle element doesn't affect palindrome check.

---

## Problem 9: Circular Array Loop

### Hint Level 1 (Gentle)
This is cycle detection in an array where values determine the "next" index. But there are additional constraints: the cycle must have consistent direction and length > 1.

### Hint Level 2 (Direct)
For each starting position:
1. Use fast/slow pointers to detect cycles
2. Verify all moves in cycle are same direction (all positive or all negative)
3. Verify cycle length > 1 (not self-loop)
4. Mark visited elements to avoid reprocessing

### Hint Level 3 (Detailed)
Key insights:
- Next index = (current + nums[current]) % n (handle negative with additional modulo)
- Check direction: nums[slow] * nums[fast] > 0
- Self-loop check: if slow === getNext(slow), it's invalid
- Optimization: Mark processed paths with 0 to avoid revisiting
Remember to handle negative indices correctly in circular array!

---

## Problem 10: Intersection of Two Linked Lists

### Hint Level 1 (Gentle)
If two lists intersect, they share the same tail portion. What if you could align them so they both have the same distance to travel to the intersection?

### Hint Level 2 (Direct)
Brilliant trick: When pointer A reaches the end of list A, redirect it to head of list B. Do the same for pointer B. They'll meet at the intersection (or null if no intersection).

### Hint Level 3 (Detailed)
Why this works:
- List A: a + c (a = unique part, c = common part)
- List B: b + c (b = unique part, c = common part)
- Pointer A travels: a + c + b
- Pointer B travels: b + c + a
- Both travel same total distance and meet at intersection!

If no intersection, both will reach null at the same time after traveling a+b distance each.

---

## General Fast/Slow Pointer Tips

1. **Initialization matters:** Sometimes both start at head, sometimes fast starts at head.next
2. **Loop conditions:** Usually `while (fast && fast.next)` for linked lists
3. **Null checks:** TypeScript requires careful null handling
4. **Drawing helps:** Visualize pointer movements on paper
5. **Edge cases:** Always test with 0, 1, and 2 element inputs