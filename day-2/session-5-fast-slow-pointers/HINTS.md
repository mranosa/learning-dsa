# Fast/Slow Pointers - Hints

## Problem 1: Linked List Cycle

### Hint 1
Think about two runners on a circular track at different speeds. Will they meet?

### Hint 2
Use two pointers: slow (1 step) and fast (2 steps). If there's a cycle, they'll meet.

### Hint 3
```typescript
let slow = head, fast = head;
while (fast && fast.next) {
    slow = slow.next!;
    fast = fast.next.next;
    if (slow === fast) return true; // Cycle!
}
return false; // No cycle
```

---

## Problem 2: Linked List Cycle II

### Hint 1
After detecting a cycle, there's a mathematical relationship between meeting point and cycle entrance.

### Hint 2
Two phases: (1) Detect cycle. (2) Reset one pointer to head, move both one step at a time.

### Hint 3
Distance from head to cycle start = distance from meeting point to cycle start. Reset slow to head after detection, move both at same speed.

---

## Problem 3: Happy Number

### Hint 1
If not happy, the sequence cycles. This is cycle detection!

### Hint 2
Treat transformation as "next" pointer. Use Floyd's algorithm on the sequence.

### Hint 3
```typescript
const getNext = (n) => sum of squares of digits;
let slow = n, fast = n;
do {
    slow = getNext(slow);
    fast = getNext(getNext(fast));
} while (slow !== fast);
return slow === 1;
```

---

## Problem 4: Middle of the Linked List

### Hint 1
If someone runs 2x as fast, where are you when they finish?

### Hint 2
When fast reaches end, slow is at middle.

### Hint 3
```typescript
let slow = head, fast = head;
while (fast && fast.next) {
    slow = slow.next!;
    fast = fast.next.next;
}
return slow; // Middle!
```

---

## Problem 5: Find the Duplicate Number

### Hint 1
Array as linked list: nums[i] → index nums[i]. Duplicate means cycle!

### Hint 2
Treat array as implicit linked list. Apply Floyd's algorithm.

### Hint 3
Phase 1: Start at nums[0], move slow to nums[slow], fast to nums[nums[fast]].
Phase 2: Reset slow to nums[0], move both one step. They meet at duplicate.

---

## Problem 6: Remove Nth Node From End of List

### Hint 1
If one pointer is n nodes ahead, what happens when it reaches end?

### Hint 2
Fast pointer leads by n nodes. When fast reaches end, slow is at target.

### Hint 3
Use dummy node. Move fast n+1 steps ahead. Move both together. Remove slow.next.

---

## Problem 7: Reorder List

### Hint 1
Pattern: first, last, second, second-to-last. Need to access second half in reverse.

### Hint 2
Three steps: (1) Find middle. (2) Reverse second half. (3) Merge alternately.

### Hint 3
Use fast/slow to find middle. Reverse from middle. Merge: take one from first, one from reversed second, repeat.

---

## Problem 8: Palindrome Linked List

### Hint 1
Compare first half with reversed second half in O(1) space.

### Hint 2
Find middle, reverse second half, compare.

### Hint 3
```typescript
// Find middle (fast/slow)
// Reverse from slow.next
// Compare head with reversed half
// For odd length, middle doesn't matter
```

---

## Problem 9: Circular Array Loop

### Hint 1
Cycle detection in array where values determine next index. Must verify direction and length.

### Hint 2
For each start: (1) Use fast/slow. (2) Check same direction. (3) Check length > 1. (4) Mark visited.

### Hint 3
```typescript
getNext = (i) => ((i + nums[i]) % n + n) % n;
// Check: nums[slow] * nums[fast] > 0 (same sign)
// Check: slow !== getNext(slow) (not self-loop)
// Mark visited with 0
```

---

## Problem 10: Intersection of Two Linked Lists

### Hint 1
If lists intersect, they share tail. Need to align them for same distance.

### Hint 2
When pointer reaches end, redirect to other list's head. They'll meet at intersection!

### Hint 3
```typescript
let pA = headA, pB = headB;
while (pA !== pB) {
    pA = pA ? pA.next : headB;
    pB = pB ? pB.next : headA;
}
return pA; // Intersection or null
```

**Why:** A travels a+c+b, B travels b+c+a. Same distance!

---

## General Tips

1. **Always check:** `while (fast && fast.next)` for linked lists
2. **Guard clauses:** Handle null/empty at start
3. **Draw it:** Visualize pointer movements
4. **Edge cases:** Empty, single node, two nodes
5. **TypeScript:** Use `!` assertion carefully after null checks
