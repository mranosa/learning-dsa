# Lesson: Fast/Slow Pointers

---

## 📹 Video 1: Fast/Slow Pointers Fundamentals (9 min)

**"Fast & Slow Pointers - Linked List Cycle - Leetcode 141" by NeetCode**
https://www.youtube.com/watch?v=gBTe7lFR3vc

**Focus on:**
- Floyd's tortoise and hare concept
- Why pointers meet in a cycle
- Basic implementation pattern
- Time/space complexity benefits

---

## 📹 Video 2: Floyd's Algorithm Deep Dive (8 min)

**"Linked List Cycle II - Leetcode 142" by NeetCode**
https://www.youtube.com/watch?v=gBTe7lFR3vc

**Focus on:**
- Two-phase cycle detection
- Finding cycle entry point
- Mathematical proof
- Distance relationships

---

## 📹 Video 3: Advanced Applications (5 min)

**"Find the Duplicate Number - Leetcode 287" by NeetCode**
https://www.youtube.com/watch?v=wjYnzkAhcNk

**Focus on:**
- Array as implicit linked list
- Applying Floyd's to sequences
- Pattern variations

---

## 🎯 Floyd's Cycle Detection

### Core Concept

Two pointers moving at different speeds:
- **Tortoise (slow):** Moves 1 step
- **Hare (fast):** Moves 2 steps
- **If cycle exists:** They meet
- **If no cycle:** Fast reaches null

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
    let fast = head;

    while (fast && fast.next) {
        slow = slow.next!;
        fast = fast.next.next;

        if (slow === fast) return true;
    }

    return false;
}
```

**Time:** O(n) | **Space:** O(1)

---

## 🔧 Pattern Variations

### 1. Finding Middle Element

When fast reaches end, slow is at middle.

```typescript
function findMiddle(head: ListNode | null): ListNode | null {
    if (!head) return null;

    let slow = head;
    let fast = head;

    while (fast && fast.next) {
        slow = slow.next!;
        fast = fast.next.next;
    }

    return slow; // For even length, returns second middle
}
```

**Time:** O(n) | **Space:** O(1)

---

### 2. Finding Cycle Entry

Two-phase: detect cycle, then find entry.

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

    if (!fast || !fast.next) return null; // No cycle

    // Phase 2: Find entry
    slow = head;
    while (slow !== fast) {
        slow = slow.next!;
        fast = fast.next!;
    }

    return slow;
}
```

**Time:** O(n) | **Space:** O(1)

**Why it works:** Distance from head to cycle start = distance from meeting point to cycle start.

---

### 3. Nth Node from End

Fast pointer leads by n nodes.

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

    // Remove nth node
    slow.next = slow.next!.next;

    return dummy.next;
}
```

**Time:** O(n) - single pass | **Space:** O(1)

---

## 🧩 Advanced Applications

### Happy Number Detection

Apply cycle detection to number sequences.

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

**Time:** O(log n) | **Space:** O(1)

---

### Find Duplicate in Array

Treat array as implicit linked list: nums[i] → index nums[i].

```typescript
function findDuplicate(nums: number[]): number {
    // Phase 1: Find meeting point
    let slow = nums[0];
    let fast = nums[0];

    do {
        slow = nums[slow];
        fast = nums[nums[fast]];
    } while (slow !== fast);

    // Phase 2: Find duplicate (cycle entry)
    slow = nums[0];
    while (slow !== fast) {
        slow = nums[slow];
        fast = nums[fast];
    }

    return slow;
}
```

**Time:** O(n) | **Space:** O(1)

**Why it works:** Duplicate value = multiple indices point to same next index = cycle!

---

### Palindrome Linked List

Combine with list reversal.

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

**Time:** O(n) | **Space:** O(1)

---

## 💡 Interview Tips

### When to Use Fast/Slow Pointers

| Problem Type | Pattern | Key Insight |
|--------------|---------|-------------|
| Cycle detection | Fast=2, Slow=1 | Meet in cycle |
| Middle element | Fast=2, Slow=1 | Fast reaches end |
| Nth from end | Fast leads by n | Distance relationship |
| Cycle entry | Two phases | Reset after detection |

---

### TypeScript Edge Cases

```typescript
// ❌ Wrong - missing null checks
while (fast.next) {
    fast = fast.next.next; // Can fail!
}

// ✅ Correct - safe null handling
while (fast && fast.next) {
    fast = fast.next.next; // Safe
}

// ❌ Wrong - single node not handled
let fast = head.next; // Can be null!

// ✅ Correct - guard clauses
if (!head || !head.next) return false;
```

---

### Common Interview Questions

**Q: Why move fast 2 steps?**
**A:** Optimal. Faster speeds work but don't improve complexity and add code complexity.

**Q: Why reset to head for cycle entry?**
**A:** Mathematical proof: distance(head → entry) = distance(meeting point → entry, going around cycle).

**Q: Can this work with arrays?**
**A:** Yes! If array values can be indices (like Find Duplicate problem).

---

## 📊 Complexity Analysis

| Operation | Hash Set | Fast/Slow | Winner |
|-----------|----------|-----------|--------|
| **Cycle detection** | O(n) time, O(n) space | O(n) time, O(1) space | Fast/Slow |
| **Middle element** | O(n) two-pass | O(n) one-pass | Fast/Slow |
| **Nth from end** | O(n) two-pass | O(n) one-pass | Fast/Slow |

---

## ✅ Quick Reference

```typescript
// Basic cycle detection
let slow = head, fast = head;
while (fast && fast.next) {
    slow = slow.next!;
    fast = fast.next.next;
    if (slow === fast) return true; // Cycle found
}
return false; // No cycle

// Finding middle
while (fast && fast.next) {
    slow = slow.next!;
    fast = fast.next.next;
}
// slow is now at middle

// Nth from end (advance fast first)
for (let i = 0; i < n; i++) {
    fast = fast.next!;
}
while (fast) {
    slow = slow.next!;
    fast = fast.next;
}
// slow is now n steps from end
```

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Key Takeaways:**
- Fast/slow pointers: O(1) space cycle detection
- Different speeds for different problems
- Two-phase pattern for cycle entry
- Works on lists, arrays, sequences

---

[Back to Session README](./README.md)
