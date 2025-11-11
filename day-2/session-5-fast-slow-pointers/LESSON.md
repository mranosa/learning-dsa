# Fast/Slow Pointers - Complete Learning Guide

## Video Lesson

**Watch this first:** [Fast & Slow Pointers - Linked List Cycle - Leetcode 141](https://www.youtube.com/watch?v=gBTe7lFR3vc)

**Duration:** 9 minutes

**Backup videos:**
- [Floyd's Tortoise & Hare Algorithm](https://www.youtube.com/watch?v=gBTe7lFR3vc)
- [Linked List Problems - Fast & Slow Pointers](https://www.youtube.com/watch?v=gBTe7lFR3vc)

---

## Core Concept: Floyd's Cycle Detection Algorithm

### The Tortoise and Hare

Imagine two runners on a track:
- **Tortoise (slow):** Moves 1 step at a time
- **Hare (fast):** Moves 2 steps at a time

**Key insight:** If there's a cycle, they will eventually meet. If no cycle, fast reaches the end.

```typescript
class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
}

function hasCycle(head: ListNode | null): boolean {
    if (!head || !head.next) return false;

    let slow = head;
    let fast = head.next;

    while (fast && fast.next) {
        if (slow === fast) return true;
        slow = slow.next!;
        fast = fast.next.next;
    }

    return false;
}
```

---

## Why Fast/Slow Pointers Work

### Mathematical Foundation

If there's a cycle of length `L`:
- Slow pointer moves at speed 1
- Fast pointer moves at speed 2
- Relative speed = 2 - 1 = 1

**Distance closing rate:** Fast catches up by 1 node per iteration

**Time to meet:** At most `n` iterations where `n` is total nodes

### Visual Example

```
Without cycle:
slow: 1 -> 2 -> 3 -> 4 -> null
fast: 1 -> 3 -> null (reaches end)

With cycle:
     1 -> 2 -> 3
           ^    |
           |    v
           5 <- 4

Iteration 1: slow=1, fast=2
Iteration 2: slow=2, fast=4
Iteration 3: slow=3, fast=2
Iteration 4: slow=4, fast=4 (MEET!)
```

---

## Pattern Variations

### 1. Finding Middle Element

Fast moves 2x speed, when fast reaches end, slow is at middle:

```typescript
function findMiddle(head: ListNode | null): ListNode | null {
    if (!head) return null;

    let slow = head;
    let fast = head;

    while (fast && fast.next) {
        slow = slow.next!;
        fast = fast.next.next;
    }

    return slow;
}
```

### 2. Finding Cycle Entry Point

After detecting cycle, reset one pointer and move both at same speed:

```typescript
function detectCycle(head: ListNode | null): ListNode | null {
    if (!head || !head.next) return null;

    let slow = head;
    let fast = head;

    // Phase 1: Detect cycle
    while (fast && fast.next) {
        slow = slow.next!;
        fast = fast.next.next;
        if (slow === fast) break;
    }

    if (!fast || !fast.next) return null;

    // Phase 2: Find entry point
    slow = head;
    while (slow !== fast) {
        slow = slow.next!;
        fast = fast.next!;
    }

    return slow;
}
```

### 3. Nth Node from End

Fast pointer leads by N nodes:

```typescript
function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    const dummy = new ListNode(0, head);
    let slow = dummy;
    let fast = dummy;

    // Move fast n+1 steps ahead
    for (let i = 0; i <= n; i++) {
        fast = fast.next!;
    }

    // Move both until fast reaches end
    while (fast) {
        slow = slow.next!;
        fast = fast.next;
    }

    // Skip the nth node
    slow.next = slow.next!.next;

    return dummy.next;
}
```

---

## Advanced Applications

### 1. Happy Number Detection

Apply cycle detection to number sequences:

```typescript
function isHappy(n: number): boolean {
    const getNext = (num: number): number => {
        let sum = 0;
        while (num > 0) {
            const digit = num % 10;
            sum += digit * digit;
            num = Math.floor(num / 10);
        }
        return sum;
    };

    let slow = n;
    let fast = n;

    do {
        slow = getNext(slow);
        fast = getNext(getNext(fast));
    } while (slow !== fast);

    return slow === 1;
}
```

### 2. Find Duplicate in Array

Treat array as implicit linked list:

```typescript
function findDuplicate(nums: number[]): number {
    let slow = nums[0];
    let fast = nums[0];

    // Phase 1: Find intersection point
    do {
        slow = nums[slow];
        fast = nums[nums[fast]];
    } while (slow !== fast);

    // Phase 2: Find entrance to cycle
    slow = nums[0];
    while (slow !== fast) {
        slow = nums[slow];
        fast = nums[fast];
    }

    return slow;
}
```

### 3. Palindrome Linked List

Combine with list reversal:

```typescript
function isPalindrome(head: ListNode | null): boolean {
    if (!head || !head.next) return true;

    // Find middle
    let slow = head;
    let fast = head;
    while (fast.next && fast.next.next) {
        slow = slow.next!;
        fast = fast.next.next;
    }

    // Reverse second half
    let prev: ListNode | null = null;
    let curr = slow.next;
    while (curr) {
        const next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }

    // Compare halves
    let p1 = head;
    let p2 = prev;
    while (p2) {
        if (p1.val !== p2.val) return false;
        p1 = p1.next!;
        p2 = p2.next;
    }

    return true;
}
```

---

## Edge Cases to Remember

### 1. Empty or Single Node
```typescript
if (!head || !head.next) return false; // No cycle possible
```

### 2. Two-Node Cycle
```typescript
// 1 -> 2 -> 1
// Must handle fast starting at different position
```

### 3. Self-Loop
```typescript
// Node points to itself
// 1 -> 1
```

### 4. TypeScript Null Safety
```typescript
// Always check before accessing .next
while (fast && fast.next) {
    // Safe to use fast.next.next here
}
```

---

## Common Interview Questions

### Q: Why does fast move 2 steps?
**A:** It's optimal. Moving faster (3+ steps) still works but doesn't improve time complexity and adds complexity to code.

### Q: What if pointers move at speeds 1 and 3?
**A:** Still works! As long as speeds differ, they'll meet in a cycle. The relative speed determines convergence rate.

### Q: Why reset to head for finding cycle entry?
**A:** Mathematical proof: Distance from head to cycle entry equals distance from meeting point to cycle entry (traveling around the cycle).

### Q: Can this work with arrays?
**A:** Yes! If array values can be interpreted as "next" indices (like in Find Duplicate problem).

---

## Practice Problems

Start with these in order:
1. **Linked List Cycle** - Basic implementation
2. **Middle of Linked List** - Simple variation
3. **Happy Number** - Apply to sequences
4. **Linked List Cycle II** - Find entry point
5. **Find Duplicate Number** - Array as linked list

---

## Key Takeaways

1. **Pattern recognition:** Fast/slow pointers excel at cycle detection
2. **Space efficiency:** O(1) space vs O(n) for hash set approach
3. **Versatility:** Works on lists, arrays, and number sequences
4. **Speed matters:** Different speeds for different problems
5. **Two phases:** Often detection phase + action phase

---

## Quick Reference

```typescript
// Basic pattern
let slow = head;
let fast = head;

while (fast && fast.next) {
    slow = slow.next!;
    fast = fast.next.next;

    if (slow === fast) {
        // Cycle detected
    }
}

// Finding middle
while (fast && fast.next) {
    slow = slow.next!;
    fast = fast.next.next;
}
// slow is now at middle

// Nth from end
// Advance fast by n first
for (let i = 0; i < n; i++) {
    fast = fast.next!;
}
// Then move both together
```

---

## Next Steps

After understanding the concept:
1. Implement basic cycle detection
2. Practice finding middle element
3. Try cycle entry point problem
4. Apply to array problems
5. Combine with other patterns (reversal, etc.)

Remember: Drawing pointer movements helps visualize the solution!