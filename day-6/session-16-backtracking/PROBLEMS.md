# Problems: Backtracking

10 problems in order. Use UMPIRE method.

**Targets:** Medium <30 min | Hard <45 min

---

## Problem 1: Subsets

**Difficulty:** Medium | **Pattern:** Backtracking
**LeetCode:** https://leetcode.com/problems/subsets/

### Problem

Given an integer array `nums` of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

### Examples

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

```
Input: nums = [0]
Output: [[],[0]]
```

### Constraints

- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique

### Hints

- Each element has 2 choices: include or exclude
- Decision tree: binary choices at each level
- Every node in the tree is a valid subset
- Use start index to avoid duplicate combinations

---

## Problem 2: Subsets II

**Difficulty:** Medium | **Pattern:** Backtracking with Duplicates
**LeetCode:** https://leetcode.com/problems/subsets-ii/

### Problem

Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

### Examples

```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

```
Input: nums = [0]
Output: [[],[0]]
```

### Constraints

- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10

### Hints

- Sort first to group duplicates together
- Skip duplicates at the same recursion level
- Use condition: `if (i > start && nums[i] === nums[i-1]) continue`

---

## Problem 3: Permutations

**Difficulty:** Medium | **Pattern:** Backtracking
**LeetCode:** https://leetcode.com/problems/permutations/

### Problem

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.

### Examples

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

```
Input: nums = [1]
Output: [[1]]
```

### Constraints

- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique

### Hints

- Order matters in permutations
- Track which elements have been used
- Try all unused elements at each position
- Only collect results when path.length === n

---

## Problem 4: Permutations II

**Difficulty:** Medium | **Pattern:** Backtracking with Duplicates
**LeetCode:** https://leetcode.com/problems/permutations-ii/

### Problem

Given a collection of numbers, `nums`, that might contain duplicates, return all possible unique permutations in any order.

### Examples

```
Input: nums = [1,1,2]
Output: [[1,1,2],[1,2,1],[2,1,1]]
```

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

### Constraints

- 1 <= nums.length <= 8
- -10 <= nums[i] <= 10

### Hints

- Sort array first
- Track used elements with boolean array
- Skip duplicate: `if (i > 0 && nums[i] === nums[i-1] && !used[i-1]) continue`
- This ensures duplicates are used in order

---

## Problem 5: Combination Sum

**Difficulty:** Medium | **Pattern:** Backtracking with Reuse
**LeetCode:** https://leetcode.com/problems/combination-sum/

### Problem

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

### Examples

```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

```
Input: candidates = [2], target = 1
Output: []
```

### Constraints

- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of candidates are distinct
- 1 <= target <= 40

### Hints

- Elements can be reused unlimited times
- Pass same index (not i+1) to allow reuse
- Prune when sum > target
- Track running sum

---

## Problem 6: Combination Sum II

**Difficulty:** Medium | **Pattern:** Backtracking with Single Use
**LeetCode:** https://leetcode.com/problems/combination-sum-ii/

### Problem

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

### Examples

```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
```

```
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
```

### Constraints

- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

### Hints

- Sort array to handle duplicates
- Each element used at most once (pass i+1)
- Skip duplicates at same level
- Prune when sum exceeds target

---

## Problem 7: Letter Combinations of a Phone Number

**Difficulty:** Medium | **Pattern:** Backtracking
**LeetCode:** https://leetcode.com/problems/letter-combinations-of-a-phone-number/

### Problem

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

```
2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz
```

### Examples

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

```
Input: digits = ""
Output: []
```

```
Input: digits = "2"
Output: ["a","b","c"]
```

### Constraints

- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9']

### Hints

- Create map of digit to letters
- Use index to track current digit
- For each digit, try all its letters
- Build string character by character

---

## Problem 8: Palindrome Partitioning

**Difficulty:** Medium | **Pattern:** Backtracking
**LeetCode:** https://leetcode.com/problems/palindrome-partitioning/

### Problem

Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

### Examples

```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

```
Input: s = "a"
Output: [["a"]]
```

### Constraints

- 1 <= s.length <= 16
- s contains only lowercase English letters

### Hints

- Try all possible partition points
- Check if substring is palindrome before recursing
- Use helper function to check palindrome
- Explore from start to all possible end positions

---

## Problem 9: Generate Parentheses

**Difficulty:** Medium | **Pattern:** Backtracking
**LeetCode:** https://leetcode.com/problems/generate-parentheses/

### Problem

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

### Examples

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

```
Input: n = 1
Output: ["()"]
```

### Constraints

- 1 <= n <= 8

### Hints

- Track count of open and close parentheses
- Can add '(' if open < n
- Can add ')' if close < open (must have unclosed '(')
- Build string character by character

---

## Problem 10: N-Queens

**Difficulty:** Hard | **Pattern:** Constraint Satisfaction
**LeetCode:** https://leetcode.com/problems/n-queens/

### Problem

The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

### Examples

```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown.
```

```
Input: n = 1
Output: [["Q"]]
```

### Constraints

- 1 <= n <= 9

### Visual for n=4

```
Solution 1:          Solution 2:
. Q . .             . . Q .
. . . Q             Q . . .
Q . . .             . . . Q
. . Q .             . Q . .
```

### Hints

- Process one row at a time
- Track attacked columns with Set
- Track diagonals: row-col and row+col
- Queen attacks same column and both diagonals

---

## Problem Order Strategy

### Recommended Path:

1. **Start with Subsets (Problem 1)** - Learn the basic template
2. **Then Permutations (Problem 3)** - Different traversal pattern
3. **Handle duplicates (Problems 2, 4)** - Common variation
4. **Try Combination Sum (Problem 5)** - Add constraints and reuse
5. **Combination Sum II (Problem 6)** - Single use with duplicates
6. **Letter Combinations (Problem 7)** - Multiple choice sets
7. **Palindrome Partitioning (Problem 8)** - String partitioning
8. **Generate Parentheses (Problem 9)** - Building valid strings
9. **N-Queens (Problem 10)** - Classic constraint satisfaction

### Time Targets:

- **Medium problems:** 20-30 minutes each
- **Hard problems:** 30-45 minutes each
- **If stuck:** Use hints after 15 minutes

### Practice Tips:

1. **Draw the decision tree** before coding (seriously!)
2. **Identify the choices** at each step
3. **Determine base case** - when to collect results?
4. **Think about pruning** - skip invalid early
5. **Test with small inputs** first (n=2, n=3)
6. **Verify copying** - always copy when adding to results
7. **Check backtracking** - every push needs a pop

---

## Common Patterns Summary

### Pattern 1: Generate All Subsets
- Use start index to avoid duplicates
- Every node in decision tree is a valid result
- Time: O(2^n × n)

### Pattern 2: Generate Permutations
- Track used elements
- Result only at leaf nodes (full length)
- Time: O(n! × n)

### Pattern 3: With Duplicates
- Sort first
- Skip duplicates at same tree level
- Condition: `i > start && nums[i] === nums[i-1]`

### Pattern 4: With Target/Constraint
- Prune invalid branches early
- Track running state (sum, count, etc.)
- Check constraint before and after recursion

### Pattern 5: String Building
- Character by character construction
- Validate as you build
- Use counters to track validity

### Pattern 6: Constraint Satisfaction
- Complex validation at each step
- Use efficient state tracking (Sets)
- Process dimension by dimension (row by row)

---

## Complexity Quick Reference

| Problem | Time | Space | Notes |
|---------|------|-------|-------|
| Subsets | O(2^n × n) | O(n) | 2^n subsets to generate |
| Subsets II | O(2^n × n) | O(n) | With duplicate handling |
| Permutations | O(n! × n) | O(n) | n! permutations |
| Permutations II | O(n! × n) | O(n) | With duplicate handling |
| Combination Sum | O(n^(t/m) × t) | O(t/m) | t=target, m=min candidate |
| Combination Sum II | O(2^n × n) | O(n) | Each element once |
| Letter Combos | O(4^n × n) | O(n) | Worst: 4 letters per digit |
| Palindrome Part. | O(n × 2^n) | O(n) | 2^n partitions |
| Generate Parens | O(4^n / √n) | O(n) | Catalan number |
| N-Queens | O(n!) | O(n) | n! possible placements |

---

[Back to Session README](./README.md)
