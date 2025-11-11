# Problems: Backtracking

## Problem 1: Subsets
**Difficulty:** Medium
**LeetCode:** [78. Subsets](https://leetcode.com/problems/subsets/)

Given an integer array `nums` of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

**Example 1:**
```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Example 2:**
```
Input: nums = [0]
Output: [[],[0]]
```

**Constraints:**
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique

---

## Problem 2: Subsets II
**Difficulty:** Medium
**LeetCode:** [90. Subsets II](https://leetcode.com/problems/subsets-ii/)

Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

**Example 1:**
```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

**Example 2:**
```
Input: nums = [0]
Output: [[],[0]]
```

**Constraints:**
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10

---

## Problem 3: Permutations
**Difficulty:** Medium
**LeetCode:** [46. Permutations](https://leetcode.com/problems/permutations/)

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.

**Example 1:**
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Example 2:**
```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

**Example 3:**
```
Input: nums = [1]
Output: [[1]]
```

**Constraints:**
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique

---

## Problem 4: Permutations II
**Difficulty:** Medium
**LeetCode:** [47. Permutations II](https://leetcode.com/problems/permutations-ii/)

Given a collection of numbers, `nums`, that might contain duplicates, return all possible unique permutations in any order.

**Example 1:**
```
Input: nums = [1,1,2]
Output: [[1,1,2],[1,2,1],[2,1,1]]
```

**Example 2:**
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Constraints:**
- 1 <= nums.length <= 8
- -10 <= nums[i] <= 10

---

## Problem 5: Combination Sum
**Difficulty:** Medium
**LeetCode:** [39. Combination Sum](https://leetcode.com/problems/combination-sum/)

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

**Example 1:**
```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

**Example 2:**
```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

**Example 3:**
```
Input: candidates = [2], target = 1
Output: []
```

**Constraints:**
- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of candidates are distinct
- 1 <= target <= 40

---

## Problem 6: Combination Sum II
**Difficulty:** Medium
**LeetCode:** [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

**Example 1:**
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
```

**Example 2:**
```
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
```

**Constraints:**
- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

---

## Problem 7: Letter Combinations of a Phone Number
**Difficulty:** Medium
**LeetCode:** [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

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

**Example 1:**
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**Example 2:**
```
Input: digits = ""
Output: []
```

**Example 3:**
```
Input: digits = "2"
Output: ["a","b","c"]
```

**Constraints:**
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9']

---

## Problem 8: Palindrome Partitioning
**Difficulty:** Medium
**LeetCode:** [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)

Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

**Example 1:**
```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

**Example 2:**
```
Input: s = "a"
Output: [["a"]]
```

**Constraints:**
- 1 <= s.length <= 16
- s contains only lowercase English letters

---

## Problem 9: Generate Parentheses
**Difficulty:** Medium
**LeetCode:** [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**Example 1:**
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2:**
```
Input: n = 1
Output: ["()"]
```

**Constraints:**
- 1 <= n <= 8

---

## Problem 10: N-Queens
**Difficulty:** Hard
**LeetCode:** [51. N-Queens](https://leetcode.com/problems/n-queens/)

The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

**Example 1:**
```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown.
```

**Example 2:**
```
Input: n = 1
Output: [["Q"]]
```

**Constraints:**
- 1 <= n <= 9

**Visual for n=4:**
```
Solution 1:          Solution 2:
. Q . .             . . Q .
. . . Q             Q . . .
Q . . .             . . . Q
. . Q .             . Q . .
```

---

## Problem Order Strategy

### Recommended Path:
1. **Start with Subsets (Problem 1)** - Learn the basic template
2. **Then Permutations (Problem 3)** - Different traversal pattern
3. **Handle duplicates (Problems 2, 4)** - Common variation
4. **Try Combination Sum (Problem 5)** - Add constraints
5. **Letter Combinations (Problem 7)** - Multiple choice sets
6. **Generate Parentheses (Problem 9)** - Building valid strings
7. **Palindrome Partitioning (Problem 8)** - String partitioning
8. **Combination Sum II (Problem 6)** - Complex duplicate handling
9. **N-Queens (Problem 10)** - Classic constraint satisfaction

### Time Targets:
- **Medium problems:** 20-30 minutes each
- **Hard problems:** 30-45 minutes each
- **If stuck:** Use hints after 15 minutes

### Practice Tips:
1. Draw the decision tree before coding
2. Identify what choices you have at each step
3. Determine when to collect results
4. Think about pruning opportunities
5. Test with small inputs first

---

## Common Patterns Summary

### Pattern 1: Generate All Subsets
- Use start index to avoid duplicates
- Every node in decision tree is a valid result

### Pattern 2: Generate Permutations
- Track used elements
- Result only at leaf nodes (full length)

### Pattern 3: With Duplicates
- Sort first
- Skip duplicates at same tree level

### Pattern 4: With Target/Constraint
- Prune invalid branches early
- Track running state (sum, count, etc.)

### Pattern 5: String Building
- Character by character construction
- Validate as you build