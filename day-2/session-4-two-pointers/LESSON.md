# Lesson: Two Pointers

## Videos (20 min)

**Primary:**
Two Pointers - NeetCode (20 min)
https://www.youtube.com/watch?v=On03HWe2tZM

**Alternatives:**
- Take U Forward (15 min): https://www.youtube.com/watch?v=0wvj8tLv2L8
- AlgoExpert (25 min): https://www.youtube.com/watch?v=Rh43o-5CXaA

**Focus on:**
- When two pointers is optimal
- Opposite vs same direction patterns
- Complexity improvements
- Common problem types

---

## 📚 Two Pointers - Core Concepts

### What is Two Pointers?

Two pointers is a technique where we use two references to traverse data structures (usually arrays or strings) to solve problems efficiently. Instead of nested loops, we use clever pointer movement to achieve better time complexity.

**Key insight:** By moving pointers based on problem logic, we can often reduce O(n²) to O(n).

### Pattern 1: Opposite Direction (Converging)

Pointers start at opposite ends and move toward each other.

```typescript
function isPalindrome(s: string): boolean {
    let left = 0;
    let right = s.length - 1;

    while (left < right) {
        if (s[left] !== s[right]) {
            return false;
        }
        left++;
        right--;
    }

    return true;
}
// O(n) time, O(1) space
```

**When to use:**
- Palindrome checking
- Finding pairs with target sum (sorted array)
- Container problems (maximizing area)

---

### Pattern 2: Same Direction (Fast/Slow)

Pointers move in the same direction but at different speeds or conditions.

```typescript
function removeDuplicates(nums: number[]): number {
    if (nums.length === 0) return 0;

    let slow = 0;  // Points to last unique element

    for (let fast = 1; fast < nums.length; fast++) {
        if (nums[fast] !== nums[slow]) {
            slow++;
            nums[slow] = nums[fast];
        }
    }

    return slow + 1;  // Length of unique elements
}
// O(n) time, O(1) space
```

**When to use:**
- Removing duplicates in-place
- Finding cycles (Floyd's algorithm)
- Partitioning arrays

---

## 🎯 Classic Two Pointers Problems

### 1. Two Sum in Sorted Array

**Problem:** Find two numbers that sum to target in sorted array.

**Approach:** Use opposite direction pointers.

```typescript
function twoSumSorted(numbers: number[], target: number): number[] {
    let left = 0;
    let right = numbers.length - 1;

    while (left < right) {
        const sum = numbers[left] + numbers[right];

        if (sum === target) {
            return [left + 1, right + 1];  // 1-indexed
        } else if (sum < target) {
            left++;   // Need larger sum
        } else {
            right--;  // Need smaller sum
        }
    }

    return [];
}
// O(n) time, O(1) space
```

**Why it works:** Sorted property lets us decide which pointer to move.
