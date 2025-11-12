# Fast/Slow Pointers - Solutions

## Problem 1: Linked List Cycle

### Optimal: Floyd's Cycle Detection
```typescript
function hasCycle(head: ListNode | null): boolean {
    if (!head || !head.next) return false;

    let slow: ListNode | null = head;
    let fast: ListNode | null = head;

    while (fast && fast.next) {
        slow = slow!.next;
        fast = fast.next.next;

        if (slow === fast) return true;
    }

    return false;
}
```
**Time:** O(n) | **Space:** O(1)

### Alternative: Hash Set
```typescript
function hasCycle(head: ListNode | null): boolean {
    const visited = new Set<ListNode>();

    let current = head;
    while (current) {
        if (visited.has(current)) return true;
        visited.add(current);
        current = current.next;
    }

    return false;
}
```
**Time:** O(n) | **Space:** O(n)

---

## Problem 2: Linked List Cycle II

### Optimal: Two-Phase Floyd's
```typescript
function detectCycle(head: ListNode | null): ListNode | null {
    if (!head || !head.next) return null;

    let slow: ListNode | null = head;
    let fast: ListNode | null = head;

    // Phase 1: Detect cycle
    while (fast && fast.next) {
        slow = slow!.next;
        fast = fast.next.next;

        if (slow === fast) {
            // Phase 2: Find entry
            slow = head;
            while (slow !== fast) {
                slow = slow!.next;
                fast = fast!.next;
            }
            return slow;
        }
    }

    return null;
}
```
**Time:** O(n) | **Space:** O(1)

---

## Problem 3: Happy Number

### Optimal: Floyd's on Sequence
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

## Problem 4: Middle of the Linked List

### Optimal: Fast/Slow Pointers
```typescript
function middleNode(head: ListNode | null): ListNode | null {
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
**Time:** O(n) | **Space:** O(1)

---

## Problem 5: Find the Duplicate Number

### Optimal: Floyd's on Array
```typescript
function findDuplicate(nums: number[]): number {
    // Phase 1: Find meeting point
    let slow = nums[0];
    let fast = nums[0];

    do {
        slow = nums[slow];
        fast = nums[nums[fast]];
    } while (slow !== fast);

    // Phase 2: Find duplicate
    slow = nums[0];
    while (slow !== fast) {
        slow = nums[slow];
        fast = nums[fast];
    }

    return slow;
}
```
**Time:** O(n) | **Space:** O(1)

### Alternative: Binary Search
```typescript
function findDuplicate(nums: number[]): number {
    let left = 1;
    let right = nums.length - 1;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        let count = 0;

        for (const num of nums) {
            if (num <= mid) count++;
        }

        if (count > mid) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
}
```
**Time:** O(n log n) | **Space:** O(1)

---

## Problem 6: Remove Nth Node From End of List

### Optimal: Two Pointers with Gap
```typescript
function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    const dummy = new ListNode(0, head);
    let slow: ListNode = dummy;
    let fast: ListNode | null = dummy;

    // Move fast n+1 steps ahead
    for (let i = 0; i <= n; i++) {
        fast = fast!.next;
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
**Time:** O(n) | **Space:** O(1)

---

## Problem 7: Reorder List

### Optimal: Find Middle + Reverse + Merge
```typescript
function reorderList(head: ListNode | null): void {
    if (!head || !head.next) return;

    // Step 1: Find middle
    let slow = head;
    let fast = head;
    while (fast.next && fast.next.next) {
        slow = slow.next!;
        fast = fast.next.next;
    }

    // Step 2: Reverse second half
    let prev: ListNode | null = null;
    let curr = slow.next;
    slow.next = null;

    while (curr) {
        const next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }

    // Step 3: Merge
    let first = head;
    let second = prev;

    while (second) {
        const temp1 = first.next;
        const temp2 = second.next;

        first.next = second;
        second.next = temp1;

        first = temp1!;
        second = temp2;
    }
}
```
**Time:** O(n) | **Space:** O(1)

---

## Problem 8: Palindrome Linked List

### Optimal: Reverse Second Half
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

    // Compare
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

## Problem 9: Circular Array Loop

### Optimal: Fast/Slow with Validation
```typescript
function circularArrayLoop(nums: number[]): boolean {
    const n = nums.length;

    const getNext = (index: number): number => {
        return ((index + nums[index]) % n + n) % n;
    };

    for (let i = 0; i < n; i++) {
        if (nums[i] === 0) continue;

        let slow = i;
        let fast = i;

        // Check same direction
        while (nums[slow] * nums[fast] > 0 &&
               nums[slow] * nums[getNext(fast)] > 0) {
            slow = getNext(slow);
            fast = getNext(getNext(fast));

            if (slow === fast) {
                // Check cycle length > 1
                if (slow === getNext(slow)) break;
                return true;
            }
        }

        // Mark visited
        slow = i;
        const sign = nums[i];
        while (sign * nums[slow] > 0) {
            const next = getNext(slow);
            nums[slow] = 0;
            slow = next;
        }
    }

    return false;
}
```
**Time:** O(n) | **Space:** O(1)

---

## Problem 10: Intersection of Two Linked Lists

### Optimal: Two Pointers
```typescript
function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
    if (!headA || !headB) return null;

    let pA: ListNode | null = headA;
    let pB: ListNode | null = headB;

    // Switch to other list when reaching end
    while (pA !== pB) {
        pA = pA ? pA.next : headB;
        pB = pB ? pB.next : headA;
    }

    return pA;
}
```
**Time:** O(m + n) | **Space:** O(1)

**Why it works:**
- List A: a + c (a = unique, c = common)
- List B: b + c
- Pointer A: a + c + b
- Pointer B: b + c + a
- Both travel same distance, meet at intersection!

### Alternative: Length Difference
```typescript
function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
    if (!headA || !headB) return null;

    // Get lengths
    let lengthA = 0, lengthB = 0;
    let currA = headA, currB = headB;

    while (currA) {
        lengthA++;
        currA = currA.next;
    }
    while (currB) {
        lengthB++;
        currB = currB.next;
    }

    // Align
    currA = headA;
    currB = headB;

    if (lengthA > lengthB) {
        for (let i = 0; i < lengthA - lengthB; i++) {
            currA = currA!.next;
        }
    } else {
        for (let i = 0; i < lengthB - lengthA; i++) {
            currB = currB!.next;
        }
    }

    // Find intersection
    while (currA && currB && currA !== currB) {
        currA = currA.next;
        currB = currB.next;
    }

    return currA;
}
```
**Time:** O(m + n) | **Space:** O(1)
