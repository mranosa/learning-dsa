# Fast/Slow Pointers - Complete Solutions

## Problem 1: Linked List Cycle

### Approach 1: Floyd's Cycle Detection (Optimal)
```typescript
function hasCycle(head: ListNode | null): boolean {
    if (!head || !head.next) return false;

    let slow: ListNode | null = head;
    let fast: ListNode | null = head;

    while (fast && fast.next) {
        slow = slow!.next;
        fast = fast.next.next;

        if (slow === fast) {
            return true;
        }
    }

    return false;
}
```
**Time:** O(n) - visit each node at most twice
**Space:** O(1) - only two pointers

### Approach 2: Hash Set
```typescript
function hasCycle(head: ListNode | null): boolean {
    const visited = new Set<ListNode>();

    let current = head;
    while (current) {
        if (visited.has(current)) {
            return true;
        }
        visited.add(current);
        current = current.next;
    }

    return false;
}
```
**Time:** O(n) - visit each node once
**Space:** O(n) - store all nodes in set

---

## Problem 2: Linked List Cycle II

### Approach 1: Two-Phase Floyd's Algorithm (Optimal)
```typescript
function detectCycle(head: ListNode | null): ListNode | null {
    if (!head || !head.next) return null;

    let slow: ListNode | null = head;
    let fast: ListNode | null = head;

    // Phase 1: Detect if cycle exists
    while (fast && fast.next) {
        slow = slow!.next;
        fast = fast.next.next;

        if (slow === fast) {
            // Phase 2: Find cycle entry point
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
**Time:** O(n) - at most 2n iterations
**Space:** O(1) - only pointers

### Approach 2: Hash Set
```typescript
function detectCycle(head: ListNode | null): ListNode | null {
    const visited = new Set<ListNode>();

    let current = head;
    while (current) {
        if (visited.has(current)) {
            return current;
        }
        visited.add(current);
        current = current.next;
    }

    return null;
}
```
**Time:** O(n) - visit each node once
**Space:** O(n) - store visited nodes

---

## Problem 3: Happy Number

### Approach 1: Floyd's Cycle Detection (Optimal)
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
**Time:** O(log n) - number of digits proportional to log n
**Space:** O(1) - only two variables

### Approach 2: Hash Set
```typescript
function isHappy(n: number): boolean {
    const seen = new Set<number>();

    while (n !== 1 && !seen.has(n)) {
        seen.add(n);
        let sum = 0;
        while (n > 0) {
            const digit = n % 10;
            sum += digit * digit;
            n = Math.floor(n / 10);
        }
        n = sum;
    }

    return n === 1;
}
```
**Time:** O(log n)
**Space:** O(log n) - store seen numbers

---

## Problem 4: Middle of the Linked List

### Approach 1: Fast/Slow Pointers (Optimal)
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
**Time:** O(n) - single pass
**Space:** O(1) - only pointers

### Approach 2: Two Pass
```typescript
function middleNode(head: ListNode | null): ListNode | null {
    if (!head) return null;

    // Count nodes
    let length = 0;
    let current = head;
    while (current) {
        length++;
        current = current.next;
    }

    // Find middle
    const middle = Math.floor(length / 2);
    current = head;
    for (let i = 0; i < middle; i++) {
        current = current.next!;
    }

    return current;
}
```
**Time:** O(n) - two passes
**Space:** O(1)

---

## Problem 5: Find the Duplicate Number

### Approach 1: Floyd's Cycle Detection (Optimal)
```typescript
function findDuplicate(nums: number[]): number {
    // Phase 1: Find intersection point in cycle
    let slow = nums[0];
    let fast = nums[0];

    do {
        slow = nums[slow];
        fast = nums[nums[fast]];
    } while (slow !== fast);

    // Phase 2: Find entrance to cycle (duplicate)
    slow = nums[0];
    while (slow !== fast) {
        slow = nums[slow];
        fast = nums[fast];
    }

    return slow;
}
```
**Time:** O(n) - at most 2n iterations
**Space:** O(1) - only pointers

### Approach 2: Binary Search
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
**Time:** O(n log n) - binary search with linear counting
**Space:** O(1)

---

## Problem 6: Remove Nth Node From End of List

### Approach 1: Two Pointers with Gap (Optimal)
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
**Time:** O(n) - single pass
**Space:** O(1) - only pointers

### Approach 2: Two Pass
```typescript
function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    const dummy = new ListNode(0, head);
    let length = 0;
    let current = head;

    // Count nodes
    while (current) {
        length++;
        current = current.next;
    }

    // Find node before target
    current = dummy;
    for (let i = 0; i < length - n; i++) {
        current = current.next!;
    }

    // Remove node
    current.next = current.next!.next;

    return dummy.next;
}
```
**Time:** O(n) - two passes
**Space:** O(1)

---

## Problem 7: Reorder List

### Approach: Find Middle + Reverse + Merge
```typescript
function reorderList(head: ListNode | null): void {
    if (!head || !head.next) return;

    // Step 1: Find middle using fast/slow pointers
    let slow = head;
    let fast = head;
    while (fast.next && fast.next.next) {
        slow = slow.next!;
        fast = fast.next.next;
    }

    // Step 2: Reverse second half
    let prev: ListNode | null = null;
    let curr = slow.next;
    slow.next = null; // Split the list

    while (curr) {
        const next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }

    // Step 3: Merge two halves
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
**Time:** O(n) - three linear passes
**Space:** O(1) - in-place reordering

---

## Problem 8: Palindrome Linked List

### Approach 1: Reverse Second Half (Optimal)
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

    // Compare two halves
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
**Time:** O(n) - three passes
**Space:** O(1) - in-place operations

### Approach 2: Stack
```typescript
function isPalindrome(head: ListNode | null): boolean {
    const stack: number[] = [];
    let current = head;

    // Push all values to stack
    while (current) {
        stack.push(current.val);
        current = current.next;
    }

    // Compare with popped values
    current = head;
    while (current) {
        if (current.val !== stack.pop()) {
            return false;
        }
        current = current.next;
    }

    return true;
}
```
**Time:** O(n)
**Space:** O(n) - stack storage

---

## Problem 9: Circular Array Loop

### Approach: Fast/Slow Pointers with Validation
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

        // Check if all movements are in same direction
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

        // Mark visited path as 0
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
**Time:** O(n) - each element visited at most twice
**Space:** O(1) - modify input array

---

## Problem 10: Intersection of Two Linked Lists

### Approach 1: Two Pointers (Optimal)
```typescript
function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
    if (!headA || !headB) return null;

    let pA: ListNode | null = headA;
    let pB: ListNode | null = headB;

    // When reaching end, switch to other list's head
    while (pA !== pB) {
        pA = pA ? pA.next : headB;
        pB = pB ? pB.next : headA;
    }

    return pA;
}
```
**Time:** O(m + n) - traverse both lists
**Space:** O(1) - only pointers

### Approach 2: Length Difference
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

    // Align starting points
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
**Time:** O(m + n)
**Space:** O(1)