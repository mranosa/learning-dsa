# Session 0 - Quick Solutions Reference

Quick solutions for the 3 test problems. Focus is on testing the system, not solving from scratch.

---

## Problem 1: Two Sum

```typescript
function twoSum(nums: number[], target: number): number[] {
  const seen = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];

    if (seen.has(complement)) {
      return [seen.get(complement)!, i];
    }

    seen.set(nums[i], i);
  }

  return [];
}
```

**Time:** O(n) | **Space:** O(n)

**What to say while coding:**
- "I'm creating a map to store values I've seen"
- "Iterating through the array with index i"
- "Calculating the complement as target minus current number"
- "If complement exists in map, I found the pair"
- "The time complexity is O of n because..."

---

## Problem 2: Valid Palindrome

```typescript
function isPalindrome(s: string): boolean {
  // Clean string: lowercase, remove non-alphanumeric
  const cleaned = s.toLowerCase().replace(/[^a-z0-9]/g, '');

  let left = 0;
  let right = cleaned.length - 1;

  while (left < right) {
    if (cleaned[left] !== cleaned[right]) {
      return false;
    }
    left++;
    right--;
  }

  return true;
}
```

**Time:** O(n) | **Space:** O(n) for cleaned string

**What to say while coding:**
- "Using two pointers starting at opposite ends"
- "Initialize left at start, right at end"
- "Comparing characters and moving pointers inward"
- "This is O of n time, O of n space for the cleaned string"

---

## Problem 3: Contains Duplicate

```typescript
function containsDuplicate(nums: number[]): boolean {
  const seen = new Set<number>();

  for (const num of nums) {
    if (seen.has(num)) {
      return true;
    }
    seen.add(num);
  }

  return false;
}
```

**Time:** O(n) | **Space:** O(n)

**What to say while coding:**
- "I'll use a set to track numbers I've seen"
- "Iterating through the array"
- "If number already in set, found duplicate"
- "Optimal solution: O of n time and space"

---

## Session 0 Purpose

**Remember:**
- This is a system test, not a real session
- Focus on testing features, not problem difficulty
- Use vocabulary guides liberally
- Make sure all components work
- Have fun with it!

If everything works → Session 1 will be smooth! 🚀

[Back to Problems](./PROBLEMS.md) | [Back to Session 0](./README.md)
