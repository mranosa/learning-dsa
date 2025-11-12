# Solutions - Session 4: Two Pointers

TypeScript solutions with complexity analysis.

---

## Problem 1: Valid Palindrome

```typescript
function isPalindrome(s: string): boolean {
  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    // Skip non-alphanumeric from left
    while (left < right && !isAlphaNumeric(s[left])) {
      left++;
    }

    // Skip non-alphanumeric from right
    while (left < right && !isAlphaNumeric(s[right])) {
      right--;
    }

    // Compare characters
    if (s[left].toLowerCase() !== s[right].toLowerCase()) {
      return false;
    }

    left++;
    right--;
  }

  return true;
}

function isAlphaNumeric(char: string): boolean {
  return /[a-zA-Z0-9]/.test(char);
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** Opposite direction pointers. Skip non-alphanumeric. Compare case-insensitively.

**Say:** "Two pointers from both ends converging inward. Skipping non-alphanumeric and comparing case-insensitively gives us O(n) time with O(1) space."

---

## Problem 2: Two Sum II - Input Array Is Sorted

```typescript
function twoSum(numbers: number[], target: number): number[] {
  let left = 0;
  let right = numbers.length - 1;

  while (left < right) {
    const sum = numbers[left] + numbers[right];

    if (sum === target) {
      return [left + 1, right + 1]; // 1-indexed
    } else if (sum < target) {
      left++; // Need larger sum
    } else {
      right--; // Need smaller sum
    }
  }

  return [];
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** Sorted array enables opposite direction pointers. Sum too small → move left. Sum too large → move right.

**Say:** "Using sorted property with two pointers. If sum is less than target, we need a larger number so move left pointer. If greater, move right pointer. This gives O(n) instead of O(n²) nested loops."

---

## Problem 3: 3Sum

```typescript
function threeSum(nums: number[]): number[][] {
  const result: number[][] = [];
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    // Skip duplicates for first number
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let left = i + 1;
    let right = nums.length - 1;
    const target = -nums[i];

    while (left < right) {
      const sum = nums[left] + nums[right];

      if (sum === target) {
        result.push([nums[i], nums[left], nums[right]]);

        // Skip duplicates for second number
        while (left < right && nums[left] === nums[left + 1]) left++;
        // Skip duplicates for third number
        while (left < right && nums[right] === nums[right - 1]) right--;

        left++;
        right--;
      } else if (sum < target) {
        left++;
      } else {
        right--;
      }
    }
  }

  return result;
}
```

**Time:** O(n²) | **Space:** O(1) (excluding output)

**Key:** Fix one number, use two pointers for other two. Sort enables pointer technique and duplicate handling.

**Say:** "Sorting first enables two pointers. Fix one element, use two pointers to find pairs summing to its negative. Carefully skip duplicates to avoid duplicate triplets. O(n²) from outer loop × inner two pointers."

---

## Problem 4: Container With Most Water

```typescript
function maxArea(height: number[]): number {
  let maxWater = 0;
  let left = 0;
  let right = height.length - 1;

  while (left < right) {
    const width = right - left;
    const minHeight = Math.min(height[left], height[right]);
    const area = width * minHeight;

    maxWater = Math.max(maxWater, area);

    // Move pointer with smaller height
    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return maxWater;
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** Start with maximum width. Area limited by shorter line. Move shorter line's pointer to potentially find taller line.

**Say:** "Two pointers at ends give maximum width. Area = min height × width. Moving shorter pointer gives chance to find taller line. Moving taller only decreases both dimensions."

---

## Problem 5: Trapping Rain Water

```typescript
function trap(height: number[]): number {
  if (height.length === 0) return 0;

  let left = 0;
  let right = height.length - 1;
  let leftMax = 0;
  let rightMax = 0;
  let water = 0;

  while (left < right) {
    if (height[left] < height[right]) {
      // Process left side
      if (height[left] >= leftMax) {
        leftMax = height[left];
      } else {
        water += leftMax - height[left];
      }
      left++;
    } else {
      // Process right side
      if (height[right] >= rightMax) {
        rightMax = height[right];
      } else {
        water += rightMax - height[right];
      }
      right--;
    }
  }

  return water;
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** Water at position = min(maxLeft, maxRight) - height. Two pointers track max heights from each side. Process side with smaller max.

**Say:** "Water trapped at any position depends on minimum of max heights on both sides. Using two pointers to track these maxes, we can process in one pass. When one side has smaller max, we can safely calculate water there."

---

## Problem 6: Remove Duplicates from Sorted Array

```typescript
function removeDuplicates(nums: number[]): number {
  if (nums.length === 0) return 0;

  let slow = 0; // Last unique element position

  for (let fast = 1; fast < nums.length; fast++) {
    if (nums[fast] !== nums[slow]) {
      slow++;
      nums[slow] = nums[fast];
    }
  }

  return slow + 1;
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** Slow tracks last unique position. Fast scans. When different, advance slow and copy.

**Say:** "Same direction pointers. Slow marks last unique element, fast scans ahead. When we find a different element, we advance slow and copy. This maintains unique elements in-place."

---

## Problem 7: Move Zeroes

```typescript
function moveZeroes(nums: number[]): void {
  let slow = 0; // Next position for non-zero

  // Move all non-zeros to front
  for (let fast = 0; fast < nums.length; fast++) {
    if (nums[fast] !== 0) {
      nums[slow] = nums[fast];
      slow++;
    }
  }

  // Fill rest with zeros
  for (let i = slow; i < nums.length; i++) {
    nums[i] = 0;
  }
}
```

**Time:** O(n) | **Space:** O(1)

**Alternative (fewer writes):**
```typescript
function moveZeroes(nums: number[]): void {
  let slow = 0; // Next position for non-zero

  for (let fast = 0; fast < nums.length; fast++) {
    if (nums[fast] !== 0) {
      // Swap instead of overwrite
      [nums[slow], nums[fast]] = [nums[fast], nums[slow]];
      slow++;
    }
  }
}
```

**Key:** Slow tracks next non-zero position. Fast scans. Swap when non-zero found.

**Say:** "Same direction pointers. Slow marks where next non-zero should go, fast finds them. Swapping maintains relative order and minimizes operations."

---

## Problem 8: Sort Colors

```typescript
function sortColors(nums: number[]): void {
  let low = 0;    // Next position for 0
  let mid = 0;    // Current element
  let high = nums.length - 1; // Next position for 2

  while (mid <= high) {
    if (nums[mid] === 0) {
      // Swap with low
      [nums[low], nums[mid]] = [nums[mid], nums[low]];
      low++;
      mid++;
    } else if (nums[mid] === 2) {
      // Swap with high
      [nums[mid], nums[high]] = [nums[high], nums[mid]];
      high--;
      // Don't increment mid (need to examine swapped element)
    } else {
      // nums[mid] === 1, just move forward
      mid++;
    }
  }
}
```

**Time:** O(n) | **Space:** O(1)

**Key:** Dutch National Flag algorithm. Three pointers partition array into three sections.

**Say:** "Three pointers for three colors. Low marks next 0 position, high marks next 2 position, mid scans. When we see 0, swap with low. When 2, swap with high. This partitions array in one pass."

---

## Problem 9: Partition Labels

```typescript
function partitionLabels(s: string): number[] {
  // Track last occurrence of each character
  const lastOccurrence = new Map<string, number>();
  for (let i = 0; i < s.length; i++) {
    lastOccurrence.set(s[i], i);
  }

  const result: number[] = [];
  let start = 0;
  let end = 0;

  for (let i = 0; i < s.length; i++) {
    // Extend partition end to include all occurrences
    end = Math.max(end, lastOccurrence.get(s[i])!);

    // When we reach partition end, record size
    if (i === end) {
      result.push(end - start + 1);
      start = i + 1;
    }
  }

  return result;
}
```

**Time:** O(n) | **Space:** O(1) (26 letters max)

**Key:** Track last occurrence. Extend partition end as we see characters. When reach end, create partition.

**Say:** "First pass to find last occurrence of each character. Second pass extending partition end to encompass all characters seen. When we reach the end of current partition, we know all its characters are contained."

---

## Problem 10: Boats to Save People

```typescript
function numRescueBoats(people: number[], limit: number): number {
  people.sort((a, b) => a - b);

  let left = 0;
  let right = people.length - 1;
  let boats = 0;

  while (left <= right) {
    // Try to pair heaviest with lightest
    if (people[left] + people[right] <= limit) {
      left++; // Lightest person gets on boat
    }
    right--; // Heaviest person always gets on boat
    boats++;
  }

  return boats;
}
```

**Time:** O(n log n) | **Space:** O(1)

**Key:** Greedy approach. Pair heaviest with lightest when possible. Heaviest always takes boat.

**Say:** "Sort people, then use two pointers. Try pairing heaviest with lightest. If they fit together, great. Otherwise, heaviest goes alone. This greedy approach is optimal because if the heaviest can't pair with the lightest, they can't pair with anyone."

---

## Pattern Summary

### Opposite Direction (Problems 1, 2, 3, 4, 5, 10)
- Start at both ends, move inward
- Useful for palindromes, pair finding, containers
- Often requires sorted data
- O(n) single pass instead of O(n²) nested loops

### Same Direction Fast/Slow (Problems 6, 7)
- Both pointers move same direction, different speeds
- Slow tracks valid position, fast scans
- Useful for in-place modifications
- Maintains relative order

### Multiple Pointers (Problem 8)
- 3+ pointers for partitioning
- Dutch National Flag pattern
- One-pass sorting/partitioning

### Greedy + Two Pointers (Problem 9)
- Combine greedy strategy with pointer technique
- Pre-compute necessary information
- Make locally optimal choices

---

[Back to Problems](./PROBLEMS.md) | [Back to README](./README.md)
