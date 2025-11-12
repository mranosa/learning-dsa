# Hints - Session 4: Two Pointers

Progressive hints for 10 problems. Struggling is part of learning.

---

## Problem 1: Valid Palindrome

### Level 1
Two pointers from both ends. Skip non-alphanumeric. Compare case-insensitively.

### Level 2
Use while loops to skip non-alphanumeric characters. Use `.toLowerCase()` for comparison.

### Level 3
```typescript
let left = 0, right = s.length - 1;
while (left < right) {
  while (left < right && !isAlphaNumeric(s[left])) left++;
  while (left < right && !isAlphaNumeric(s[right])) right--;
  if (s[left].toLowerCase() !== s[right].toLowerCase()) return false;
  left++;
  right--;
}
```

---

## Problem 2: Two Sum II - Input Array Is Sorted

### Level 1
Two pointers at ends. If sum < target, move left. If sum > target, move right.

### Level 2
Array is sorted, so moving left increases sum, moving right decreases sum. Use this property.

### Level 3
```typescript
let left = 0, right = numbers.length - 1;
while (left < right) {
  const sum = numbers[left] + numbers[right];
  if (sum === target) return [left + 1, right + 1];
  else if (sum < target) left++;
  else right--;
}
```

---

## Problem 3: 3Sum

### Level 1
Sort first. Fix one number, use two pointers for other two. Skip duplicates.

### Level 2
For each `nums[i]`, find two numbers summing to `-nums[i]` using two pointers. Skip duplicate `i`, `left`, `right` values.

### Level 3
```typescript
nums.sort((a, b) => a - b);
for (let i = 0; i < nums.length - 2; i++) {
  if (i > 0 && nums[i] === nums[i - 1]) continue;

  let left = i + 1, right = nums.length - 1;
  while (left < right) {
    const sum = nums[i] + nums[left] + nums[right];
    if (sum === 0) {
      result.push([nums[i], nums[left], nums[right]]);
      while (left < right && nums[left] === nums[left + 1]) left++;
      while (left < right && nums[right] === nums[right - 1]) right--;
      left++;
      right--;
    } else if (sum < 0) left++;
    else right--;
  }
}
```

---

## Problem 4: Container With Most Water

### Level 1
Two pointers at ends. Calculate area. Move pointer with smaller height.

### Level 2
Why move smaller height? Moving taller only decreases both width and height. Moving shorter might find taller line.

### Level 3
```typescript
let maxArea = 0, left = 0, right = height.length - 1;
while (left < right) {
  const width = right - left;
  const minHeight = Math.min(height[left], height[right]);
  maxArea = Math.max(maxArea, width * minHeight);

  if (height[left] < height[right]) left++;
  else right--;
}
```

---

## Problem 5: Trapping Rain Water

### Level 1
Water at position = min(maxLeft, maxRight) - height. Use two pointers to track max from each side.

### Level 2
Move pointer on side with smaller max. Can safely calculate water on that side.

### Level 3
```typescript
let left = 0, right = height.length - 1;
let leftMax = 0, rightMax = 0, water = 0;

while (left < right) {
  if (height[left] < height[right]) {
    if (height[left] >= leftMax) leftMax = height[left];
    else water += leftMax - height[left];
    left++;
  } else {
    if (height[right] >= rightMax) rightMax = height[right];
    else water += rightMax - height[right];
    right--;
  }
}
```

---

## Problem 6: Remove Duplicates from Sorted Array

### Level 1
Slow pointer tracks last unique. Fast pointer scans. When different, advance slow and copy.

### Level 2
Start slow at 0, fast at 1. When `nums[fast] !== nums[slow]`, increment slow and copy fast to slow.

### Level 3
```typescript
let slow = 0;
for (let fast = 1; fast < nums.length; fast++) {
  if (nums[fast] !== nums[slow]) {
    slow++;
    nums[slow] = nums[fast];
  }
}
return slow + 1;
```

---

## Problem 7: Move Zeroes

### Level 1
Slow tracks next non-zero position. Fast scans. Swap when non-zero found.

### Level 2
When `nums[fast] !== 0`, swap with `nums[slow]` and increment slow.

### Level 3
```typescript
let slow = 0;
for (let fast = 0; fast < nums.length; fast++) {
  if (nums[fast] !== 0) {
    [nums[slow], nums[fast]] = [nums[fast], nums[slow]];
    slow++;
  }
}
```

---

## Problem 8: Sort Colors

### Level 1
Three pointers: low (next 0), mid (current), high (next 2). Swap based on mid's value.

### Level 2
If mid is 0, swap with low and move both. If 2, swap with high and move high only. If 1, just move mid.

### Level 3
```typescript
let low = 0, mid = 0, high = nums.length - 1;
while (mid <= high) {
  if (nums[mid] === 0) {
    [nums[low], nums[mid]] = [nums[mid], nums[low]];
    low++;
    mid++;
  } else if (nums[mid] === 2) {
    [nums[mid], nums[high]] = [nums[high], nums[mid]];
    high--;
  } else {
    mid++;
  }
}
```

---

## Problem 9: Partition Labels

### Level 1
Track last occurrence of each character. Extend partition end as you scan. When reach end, create partition.

### Level 2
First pass: build map of last indices. Second pass: track partition end, update it with each character's last occurrence.

### Level 3
```typescript
const lastOccurrence = new Map<string, number>();
for (let i = 0; i < s.length; i++) {
  lastOccurrence.set(s[i], i);
}

const result: number[] = [];
let start = 0, end = 0;

for (let i = 0; i < s.length; i++) {
  end = Math.max(end, lastOccurrence.get(s[i])!);
  if (i === end) {
    result.push(end - start + 1);
    start = i + 1;
  }
}
```

---

## Problem 10: Boats to Save People

### Level 1
Sort people. Try pairing heaviest with lightest. If too heavy, heaviest goes alone.

### Level 2
Two pointers: left (lightest), right (heaviest). If sum ≤ limit, both board. Otherwise just heaviest. Increment boats each iteration.

### Level 3
```typescript
people.sort((a, b) => a - b);
let left = 0, right = people.length - 1, boats = 0;

while (left <= right) {
  if (people[left] + people[right] <= limit) {
    left++;
  }
  right--;
  boats++;
}
```

---

## Pattern Hints

**"Palindrome/symmetric check"** → Opposite direction pointers

**"Sorted array + find pair"** → Opposite direction pointers

**"Container/area problems"** → Opposite direction, move smaller value

**"In-place removal/modification"** → Same direction fast/slow

**"Partition into sections"** → Multiple pointers (Dutch Flag)

**"Pairing/grouping optimization"** → Sort + opposite direction

---

## Using Hints Effectively

1. Try 10+ min before Level 1
2. Try 5+ min after each hint
3. If use Level 3, mark for review and retry similar later
4. Don't feel bad - hints are for learning

Goal: Learn pattern, not just solve one problem.

---

[Back to Problems](./PROBLEMS.md) | [Back to Solutions](./SOLUTIONS.md)
